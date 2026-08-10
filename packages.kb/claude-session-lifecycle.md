---
status: speculative
home: bukzor-tools
language: bash
---

# claude-session-lifecycle

**Speculative -- the seam has not been argued, only guessed.** Filed so the
guess is visible and attackable, not so it gets built.

Candidate members:

- `~/bin/claude-fork` (42 lines) -- has a `usage()`, so it has modes
- `~/bin/claude-workspace-merge` (120 lines) -- carries an inlined copy of
  the slug encoding at line 12
- `~/bin/claude-export` (86 lines) -- operates on `~/.claude/shell-snapshots`

## Why it's speculative

The three were grouped by "they manipulate sessions rather than read them",
which is a description of what they touch, not a seam. Nothing yet shows
what a member would import from a sibling -- the test
`../packages.kb/CLAUDE.md` demands. None has been read past its header.

Plausible outcomes, all still open:

- they're really three unrelated one-offs, and each is either a
  `claude-code-archeology` subcommand or stays in dotfiles
- `claude-fork` and `claude-branch-extract` are the same idea from two
  directions, in which case `claude-fork` is an archeology member and this
  candidate loses its center
- `claude-export` is about shell snapshots, a different subsystem than
  session JSONL, and doesn't belong with either

## Next step

Read all three in full before any clustering claim. Cheapest useful output
is deciding whether `claude-fork` overlaps `claude-branch-extract`, since
that single answer either dissolves this candidate or gives it a seam.
