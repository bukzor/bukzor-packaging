#!/usr/bin/env python3
"""Check the composition disciplines of composition.kb/ against live state.

One tool composes with another only through its calling convention: what it
reads, what it writes, and whether a real function sits behind the adapter.
This censuses the population for those three facts.

Usage: composition.py [--adapters]

  --adapters  how each tool takes its input, and whether it names a pure core

Verdicts:

  FILTER  reads a stream and writes one -- an arrow in the pipe category, and
          the only kind whose composability carries information
  ITEM    takes paths or arguments, one invocation per item -- which is where
          per-invocation cost stops amortizing, because the fork is per item
          rather than per stream
  EFFECT  writes files or mutates state -- `unit -> unit`, so every such tool
          composes with every other and the typing says nothing

The classifier is regex-grade, like seams.py's relations, and its discount runs
the *other* way: it over-approximates effects (a `rm` in a comment counts) and
under-approximates pure cores (a core whose name differs from the command is
missed). So its FILTER verdicts are the weak ones and its EFFECT verdicts are
sound -- the opposite of seams.py, which is worth saying out loud because the
two checks live in one directory.

Exits nonzero while an EFFECT tool names no core at all, which is the single rule
composition.kb asks of a new tool.
"""

from __future__ import annotations

import os
import pathlib
import re
import sys

STDIN = re.compile(r"sys\.stdin|/dev/stdin|while\s+read\b|\bread\s+-r\b|fileinput")
ITEMARG = re.compile(r"sys\.argv|argparse|\"\$1\"|\$\{1|\"\$@\"")
EFFECTS = re.compile(
    r"write_text|open\([^)]*[\"'][wa]|\bmkdir\b|shutil\.(copy|move|rmtree)"
    r"|^\s*(cp|mv|rm|git|find)\s|>\s*\"\$",
    re.M,
)

DEFS = re.compile(r"^\s*(?:def|function)\s+([A-Za-z_]\w*)|^\s*([a-z_]\w*)\s*\(\)", re.M)
# `main` and the error/usage boilerplate are the adapter, by definition -- a
# core found among them would be the check answering its own question.
NOISE = frozenset(("main", "onerror", "usage", "parse_args", "cli", "die", "warn"))

# A console script is a stub over a module: `from x.y import main`. Follow it,
# or the census grades the packaging rather than the tool.
STUB = re.compile(r"^from ([\w.]+) import", re.M)
STUB_LINES = 20


def population() -> dict[str, pathlib.Path]:
    """Every `claude-*` command reachable on PATH, first match winning.

    Keyed on PATH rather than on ~/bin so a tool stays in the census after it
    graduates -- the failure seams.py had to grow SHIPPED verdicts for.
    """
    found: dict[str, pathlib.Path] = {}
    for entry in os.environ.get("PATH", "").split(":"):
        for path in sorted(pathlib.Path(entry).glob("claude-*")):
            if path.name not in found and os.access(path, os.X_OK):
                found[path.name] = path
    return found


def source_for(path: pathlib.Path) -> pathlib.Path:
    """The file holding the logic, following a console-script stub to its module."""
    try:
        body = path.read_text(errors="replace")
    except (OSError, UnicodeError):
        return path
    found = STUB.search(body)
    if not found or len(body.splitlines()) > STUB_LINES:
        return path
    module = found.group(1).replace(".", "/")
    prefix = pathlib.Path(os.path.realpath(path)).parent.parent
    for candidate in sorted(prefix.glob(f"lib/python*/site-packages/{module}.py")):
        return candidate
    return path


def defined(body: str) -> list[str]:
    """Every function the file defines, in order, minus the scaffolding."""
    names: list[str] = []
    for found in DEFS.finditer(body):
        name = found.group(1) or found.group(2)
        if name not in NOISE and name not in names:
            names.append(name)
    return names


def pure_core(command: str, body: str) -> tuple[str, bool]:
    """A function named for the command, which `main` adapts to the CLI.

    The discipline is bukzor's: a thin `main` adapting "a bona-fide function of
    the same name as the script". Exact matches are the check; a *near* match --
    a function sharing a word with the command, like `path_slug` under
    `claude-path` -- is reported separately, because the distance between the
    two populations is the whole value of the discipline. A core named by a
    synonym (`find` under `claude-search`) is invisible to any name-based rule,
    which is an argument for the naming convention rather than against the check.
    """
    stem = command.removeprefix("claude-").replace("-", "_")
    names = defined(body)
    if stem in names:
        return stem, True
    words = set(stem.split("_"))
    scored = [
        (len(words & set(name.split("_"))), -rank, name)
        for rank, name in enumerate(names)
    ]
    best = max(scored, default=(0, 0, ""))
    return (best[2], False) if best[0] else ("", False)


def classify(body: str) -> str:
    if EFFECTS.search(body):
        return "EFFECT"
    if STDIN.search(body):
        return "FILTER"
    if ITEMARG.search(body):
        return "ITEM"
    return "UNKNOWN"


def check_adapters() -> int:
    rows: list[tuple[str, str, str, bool, pathlib.Path]] = []
    for command, path in sorted(population().items()):
        source = source_for(path)
        try:
            body = source.read_text(errors="replace")
        except (OSError, UnicodeError):
            continue
        core, exact = pure_core(command, body)
        rows.append((command, classify(body), core, exact, source))

    home = str(pathlib.Path.home())
    print(f"{'tool':<28}{'takes':<9}{'pure core':<20}source")
    for command, kind, core, exact, source in rows:
        shown = core if exact else f"~{core}" if core else "--"
        print(f"{command:<28}{kind:<9}{shown:<20}{str(source).replace(home, '~')}")

    kinds = [kind for _, kind, _, _, _ in rows]
    print(
        f"\n{len(rows)} tools: "
        + ", ".join(f"{kinds.count(k)} {k}" for k in sorted(set(kinds)))
    )
    hit = [command for command, _, _, exact, _ in rows if exact]
    near = [command for command, _, core, exact, _ in rows if core and not exact]
    print(f"{len(hit)} name a core for the command; {len(near)} name one a rename away")

    bare = [
        command for command, kind, core, _, _ in rows if kind == "EFFECT" and not core
    ]
    if bare:
        print(
            f"\n{len(bare)} effectful tools name no core at all:"
            f"\n  {', '.join(bare)}"
            "\nAn effect-only tool is `unit -> unit`, so nothing about it can be"
            "\ncomposed, tested at a boundary, or reused -- naming the core is the"
            "\nwhole of the discipline composition.kb asks for."
        )
    return 1 if bare else 0


def main(argv: list[str]) -> int:
    if argv and argv[0] not in ("--adapters",):
        print(__doc__, file=sys.stderr)
        return 2
    return check_adapters()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
