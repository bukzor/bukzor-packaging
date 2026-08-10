---
status: rejected
home: bukzor-tools
language: bash
---

# claude-session-lifecycle

**Rejected 2026-08-10 -- measured, not merely doubted.** Kept as the record
of what was guessed and what killed it.

Candidate members:

- `~/bin/claude-fork` (42 lines) -- has a `usage()`, so it has modes
- `~/bin/claude-workspace-merge` (120 lines) -- carries an inlined copy of
  the slug encoding at line 15
- `~/bin/claude-export` (86 lines) -- operates on `~/.claude/shell-snapshots`

## What killed it

No two members share code, and no two share an artifact:

| member | references | touches |
| ------ | ---------- | ------- |
| `claude-fork` | nothing in `~/bin/claude-*` | worktrees |
| `claude-workspace-merge` | nothing in `~/bin/claude-*` | session JSONL, the slug encoding |
| `claude-export` | nothing in `~/bin/claude-*` | `~/.claude/shell-snapshots` |

Pairwise disjoint on both counts, so there is no refactor that turns this
into a package -- the usual rescue ("extract the shared part") has nothing to
extract. This is the first outcome listed under "plausible outcomes" below,
now confirmed.

Worse for the grouping: `claude-workspace-merge`'s two artifacts point *out*
of the cluster, into `claude-slug` and `claude-code-archeology`. The tool is
real; the cluster was a description of what the three touch, and that
description was wrong.

Members go to `unsettled` in `../dispositions.md` rather than to new homes --
`claude-workspace-merge` most likely joins `claude-slug` once the encoding is
one implementation, and the other two need reading before anyone signs
"dotfiles".

## Why it was speculative

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
