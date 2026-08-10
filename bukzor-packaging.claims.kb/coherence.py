#!/usr/bin/env python3
"""Check the coherence laws of coherence.kb/ against live state.

git-localhost-store names each relocated `.git` by a *derived key*: the
worktree path run through `claude-path`, i.e. every non-alphanumeric
character mapped to one `-`. A derived key is only sound while the deriving
function is stable, and nothing here recomputes or checks it.

Usage: coherence.py [--derived] [--shadow]

  --derived  walk the worktrees and re-derive each store key (the default)
  --shadow   which claude-slug implementation wins, and who else has one

Exits nonzero when a store key disagrees with today's encoder, or when two
worktrees claim one store.
"""

from __future__ import annotations

import collections
import os
import pathlib
import re
import shutil
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


def check_shadow() -> int:
    """Two live implementations of the encoding; search order picks one."""
    print(f"claude-slug resolves to:      {shutil.which('claude-slug')}")
    print(
        f"PATH offers:                  {os.environ.get('PATH', '').count(':') + 1} dirs"
    )
    if GLS_SHIM.is_symlink():
        print(
            f"git-localhost-store bypasses PATH via a symlink -> {GLS_SHIM.readlink()}"
        )

    for name in sorted(p.name for p in BIN.glob("claude-*")):
        body = (BIN / name).read_text(errors="replace")
        for line_no, line in enumerate(body.splitlines(), 1):
            if NON_ALNUM.pattern in line:
                print(f"encoding implemented at:      {name}:{line_no}")
    return 0


def main(argv: list[str]) -> int:
    if "--shadow" in argv:
        return check_shadow()
    return check_derived()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
