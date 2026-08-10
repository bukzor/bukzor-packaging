#!/usr/bin/env python3
"""Check the coherence laws of coherence.kb/ against live state.

git-localhost-store names each relocated `.git` by a *derived key*: the
worktree path run through `claude-path`, i.e. every non-alphanumeric
character mapped to one `-`. A derived key is only sound while the deriving
function is stable, and nothing here recomputes or checks it.

Usage: coherence.py [--derived] [--shadow]

  --derived  walk the worktrees and re-derive each store key (the default)
  --shadow   every site implementing the encoding, which one PATH picks, and
             what a fresh clone of the dotfiles repo would get instead

Exits nonzero when a store key disagrees with today's encoder, when two
worktrees claim one store, when a fresh clone would not reproduce the live
encoder, or while more than one file implements the encoding.
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


GLS_SHIM = pathlib.Path.home() / ".local/share/git-localhost-store/bin/claude-path"

# $HOME is the dotfiles working tree, so `git -C ~` answers for `~/bin`.
DOTFILES = pathlib.Path.home()
LIVE_ENCODER = "bin/claude-path"

# Where a copy of the encoding could hide. Globbed rather than listed, so a
# sixth copy shows up here the day it is made.
SITE_GLOBS = (
    "bin/claude-*",
    "repo/github.com/bukzor/*/bin/claude-slug",
    "repo/github.com/bukzor/*/bin/claude-path",
)

LEGACY_SED = re.compile(r"s/-/--/")
DELEGATES = re.compile(r"claude-slug")


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


def check_shadow() -> int:
    """Live implementations of one fact, and what resolves between them."""
    print(f"claude-slug resolves to:      {shutil.which('claude-slug')}")
    print(
        f"PATH offers:                  {os.environ.get('PATH', '').count(':') + 1} dirs"
    )
    if GLS_SHIM.is_symlink():
        print(
            f"git-localhost-store bypasses PATH via a symlink -> {GLS_SHIM.readlink()}"
        )

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

    # The live encoder runs from one working tree. What would a clone get?
    # Delegation counts: claude-path is allowed to have no encoding of its own,
    # as long as the file it hands off to is in the same commit.
    head_path = classify(
        run(["git", "-C", str(DOTFILES), "show", f"HEAD:{LIVE_ENCODER}"])
    )
    head_slug = classify(
        run(["git", "-C", str(DOTFILES), "show", "HEAD:bin/claude-slug"])
    )
    print(f"\nHEAD:{LIVE_ENCODER} implements: {head_path or 'ABSENT'}")
    print(
        f"HEAD:bin/claude-slug implements: {head_slug or 'ABSENT -- a clone has none'}"
    )

    clone_reproduces = head_slug == "current" and head_path in ("current", "delegates")
    if not clone_reproduces:
        print(
            "\nA fresh clone of the dotfiles repo does not reproduce the live encoder,"
            "\nwhich is the encoder 53 store directories were named by."
        )
    if len(copies) > 1:
        print(
            f"\n{len(copies)} tracked files implement the encoding independently, and"
            "\nnothing declares which is authoritative -- PATH order decides."
        )
    return 0 if clone_reproduces and len(copies) <= 1 else 1


def main(argv: list[str]) -> int:
    if "--shadow" in argv:
        return check_shadow()
    return check_derived()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
