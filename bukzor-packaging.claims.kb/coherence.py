#!/usr/bin/env python3
"""Check the coherence laws of coherence.kb/ against live state.

git-localhost-store names each relocated `.git` by a *derived key*: the
worktree path run through `claude-path`, i.e. every non-alphanumeric
character mapped to one `-`. A derived key is only sound while the deriving
function is stable, and nothing here recomputes or checks it.

Usage: coherence.py [--derived] [--shadow]

  --derived  walk the worktrees and re-derive each store key (the default)
  --shadow   every site implementing the encoding, which one PATH picks, and
             whether that one arrives as a declared dependency

Exits nonzero when a store key disagrees with today's encoder, when two
worktrees claim one store, when the command on PATH is a loose file rather
than an installed distribution, or while more than one file implements the
encoding.
"""

from __future__ import annotations

import collections
import os
import pathlib
import re
import shutil
import subprocess
import sys

STORE = pathlib.Path.home() / ".local/state/git-localhost-store/repos"
BIN = pathlib.Path.home() / "bin"

# `claude-slug`, as it exists today: perl -CSD -pe 's/[^A-Za-z0-9]/-/g'
NON_ALNUM = re.compile(r"[^A-Za-z0-9]")

# The store records no `core.worktree` -- the symlink *is* the back-reference,
# so the only way to check a key is to walk worktrees and re-derive.
WALK_ROOTS = ("repo", "claude", ".claude", "empty", "trash")
PRUNE = {"node_modules", ".venv", ".git", "__pycache__"}
MAX_DEPTH = 6


def encode(path: str) -> str:
    return NON_ALNUM.sub("-", path)


def encode_legacy(path: str) -> str:
    """The pre-2026-07-05 encoding: `-` doubled, `/` to `-`, everything else
    verbatim -- so dots survived. Still what git-localhost-store's own
    CLAUDE.md and docs/dev/testing.kb/path-encoding.md document.
    """
    return path.replace("-", "--").replace("/", "-")


def relocated_worktrees() -> dict[pathlib.Path, str]:
    """Worktrees whose `.git` is a symlink into the store, and the key it names."""
    home = pathlib.Path.home()
    found: dict[pathlib.Path, str] = {}
    for root in WALK_ROOTS:
        base = home / root
        for dirpath, dirnames, _ in os.walk(base):
            here = pathlib.Path(dirpath)
            if len(here.relative_to(base).parts) >= MAX_DEPTH:
                dirnames[:] = []
            dirnames[:] = [d for d in dirnames if d not in PRUNE]
            dot_git = here / ".git"
            if dot_git.is_symlink() and STORE in dot_git.resolve().parents:
                found[here] = dot_git.resolve().name
    return found


def check_derived() -> int:
    live = relocated_worktrees()
    agree: list[str] = []
    disagree: list[tuple[pathlib.Path, str, str]] = []
    for worktree, key in sorted(live.items()):
        expected = encode(str(worktree))
        if expected == key:
            agree.append(key)
        else:
            disagree.append((worktree, key, expected))

    stores = [p.name for p in STORE.iterdir() if p.is_dir()]
    legacy = [w for w, key, _ in disagree if encode_legacy(str(w)) == key]
    unexplained = [
        (w, key, exp) for w, key, exp in disagree if encode_legacy(str(w)) != key
    ]

    print(f"store directories:            {len(stores)}")
    print(f"live relocated worktrees:     {len(live)}")
    print(f"key matches today's encoder:  {len(agree)}")
    print(f"key disagrees:                {len(disagree)}")
    print(f"  legacy encoding of it:      {len(legacy)}  (declined migration)")
    print(f"  neither encoding of it:      {len(unexplained)}  (workdir moved since)")
    print(f"unreferenced store dirs:      {len(stores) - len(live)}")

    by_key = collections.Counter(live.values())
    for worktree, key, expected in unexplained[:6]:
        print(f"\n  worktree: {str(worktree).replace(str(pathlib.Path.home()), '~')}")
        print(f"  on disk:  {key}")
        print(f"  encoder:  {expected}")
        if expected in stores:
            print("  BOTH KEYS EXIST -- two stores for one worktree")

    dup = [k for k, n in by_key.items() if n > 1]
    if dup:
        print(f"\nkeys claimed by two worktrees: {dup}")

    return 1 if disagree or dup else 0


GLS_BIN = pathlib.Path.home() / ".local/share/git-localhost-store/bin"
GLS_HOOK = GLS_BIN / "git-localhost-store"
GLS_SHIM = GLS_BIN / "claude-path"

COMMANDS = ("claude-slug", "claude-path")

# Where a copy of the encoding could hide. Globbed rather than listed, so a
# new copy shows up here the day it is made. The package's own module is in
# the list: it is an implementation like any other, and the goal is that it
# be the only one -- not that it be exempt from counting.
SITE_GLOBS = (
    "bin/claude-*",
    "repo/github.com/bukzor/*/bin/claude-slug",
    "repo/github.com/bukzor/*/bin/claude-path",
    "repo/github.com/bukzor/*/packages/claude-code-slug/lib/claude_code_slug/*.py",
)

LEGACY_SED = re.compile(r"s/-/--/")
DELEGATES = re.compile(r"claude-(slug|path)\b")


def classify(body: str) -> str:
    """Which encoding a file implements, by inspection."""
    if NON_ALNUM.pattern in body:
        return "current"
    if LEGACY_SED.search(body):
        return "LEGACY"
    if DELEGATES.search(body):
        return "delegates"
    return ""


def tracking(path: pathlib.Path) -> str:
    """Whether the file is committed, modified, or in no repo at all."""
    top = run(["git", "-C", str(path.parent), "rev-parse", "--show-toplevel"])
    if not top:
        return "no repo"
    rel = str(path.relative_to(pathlib.Path(top)))
    status = run(["git", "-C", top, "status", "--porcelain", "--", rel])
    if status.startswith("??"):
        return "UNTRACKED"
    return "modified" if status else "committed"


def run(argv: list[str]) -> str:
    done = subprocess.run(argv, capture_output=True, text=True)
    return done.stdout.strip() if done.returncode == 0 else ""


def source_of(path: pathlib.Path) -> str:
    """Which tracked file this is, so two checkouts of one repo count once."""
    top = run(["git", "-C", str(path.parent), "rev-parse", "--show-toplevel"])
    if not top:
        return str(path)
    remote = run(["git", "-C", top, "remote", "get-url", "origin"]) or top
    return f"{remote}:{path.relative_to(pathlib.Path(top))}"


def installed_prefix(command: str) -> pathlib.Path | None:
    """The Python environment providing `command` on PATH, if one does.

    A console script sits in `<prefix>/bin` beside a `<prefix>/pyvenv.cfg`,
    and that prefix is the whole difference between a dependency and a loose
    file: it came from a named, versioned distribution that something
    declared. A script in `~/bin` came from whoever put it there.
    """
    found = shutil.which(command)
    if not found:
        return None
    prefix = pathlib.Path(os.path.realpath(found)).parent.parent
    return prefix if (prefix / "pyvenv.cfg").is_file() else None


def sites() -> list[tuple[pathlib.Path, int, str]]:
    """Every file implementing the encoding, with the line that does it."""
    found: list[tuple[pathlib.Path, int, str]] = []
    for glob in SITE_GLOBS:
        for path in sorted(pathlib.Path.home().glob(glob)):
            if path.is_symlink() or not path.is_file():
                continue
            body = path.read_text(errors="replace")
            kind = classify(body)
            if not kind:
                continue
            hit = next(
                line_no
                for line_no, line in enumerate(body.splitlines(), 1)
                if classify(line) == kind
            )
            found.append((path, hit, kind))
    return found


def gls_call_site() -> tuple[int, str] | None:
    """How git-localhost-store names the encoder, and so what resolves it.

    A *bare command* is resolved by PATH on every hook firing, in every
    relocated repo. The symlink in the tool's own `bin/` binds only when
    something puts that directory on PATH, which only its test harness does.
    Those are two different defects with two different fixes, and only the
    second one is a symlink -- so report the call site, not the symlink.
    """
    if not GLS_HOOK.is_file():
        return None
    for line_no, line in enumerate(GLS_HOOK.read_text().splitlines(), 1):
        if "claude-path" in line and not line.lstrip().startswith("#"):
            return line_no, line.strip()
    return None


def check_shadow() -> int:
    """Live implementations of one fact, and what resolves between them."""
    declared: list[str] = []
    for command in COMMANDS:
        prefix = installed_prefix(command)
        where = shutil.which(command) or "NOWHERE ON PATH"
        source = f"installed in {prefix.name}" if prefix else "a loose file"
        print(f"{command + ' resolves to:':<30}{where}  ({source})")
        if prefix:
            declared.append(command)
    path_dirs = os.environ.get("PATH", "").split(":")
    print(f"{'PATH offers:':<30}{len(path_dirs)} dirs, first is {path_dirs[0]}")

    call = gls_call_site()
    if call:
        line_no, text = call
        print(f"{'git-localhost-store calls:':<30}{text}  (line {line_no})")
        pinned = str(GLS_BIN) in path_dirs
        print(
            f"{'  resolved by:':<30}"
            + ("its own bin/, which is on PATH here" if pinned else "PATH, unpinned")
        )
        if GLS_SHIM.is_symlink() and not GLS_SHIM.exists():
            print(f"{'  test-harness pin:':<30}DANGLING -> {GLS_SHIM.readlink()}")

    print("\nsites implementing the encoding:")
    by_source: dict[str, set[str]] = collections.defaultdict(set)
    for path, line_no, kind in sites():
        short = str(path).replace(str(pathlib.Path.home()), "~")
        print(f"  {kind:<10} {tracking(path):<10} {short}:{line_no}")
        by_source[source_of(path)].add(kind)

    # Two checkouts of one repo are one copy of the fact -- unless they are at
    # different commits, in which case the fact has forked without an edit.
    copies = [source for source, kinds in by_source.items() if "current" in kinds]
    for source, kinds in sorted(by_source.items()):
        if len(kinds) > 1:
            print(
                f"\none tracked file, checkouts disagreeing: {source} -> {sorted(kinds)}"
            )

    if len(declared) < len(COMMANDS):
        print(
            f"\n{sorted(set(COMMANDS) - set(declared))} arrive as loose files rather than"
            "\nas an installed distribution, so nothing versions the encoder that"
            "\n53 store directories were named by."
        )
    if len(copies) > 1:
        print(
            f"\n{len(copies)} files implement the encoding independently, and nothing"
            "\ndeclares which is authoritative -- PATH order decides."
        )
    return 0 if len(declared) == len(COMMANDS) and len(copies) <= 1 else 1


def main(argv: list[str]) -> int:
    if "--shadow" in argv:
        return check_shadow()
    return check_derived()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
