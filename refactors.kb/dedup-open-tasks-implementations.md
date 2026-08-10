---
status: proposed
blocks: [claude-open-tasks]
---

# Two implementations of open-task aggregation

`~/bin/claude-open-tasks` (198 lines, PEP-723 `uv run --script`) and
`~/bin/claude-open-tasks-list` (212 lines, plain `python3`) scan
overlapping sets of the same todo conventions and print open work.

410 lines of Python for one job, in two files, with no stated relationship
between them.

## What has to be established first

Not "merge them" -- **which one is ahead, and on what.** Neither header
mentions the other, so the divergence is undocumented:

- `-list`'s docstring claims worktree dedup by effective mtime and the
  "existence IS the signal" rule for `todo.kb/`-style files. Does the
  other have either?
- What does each scan? `-list` says `~/repo` and `~/.claude`; the other
  says `~/repo` and `~/.claude` with an explicit three-pattern list. Same
  intent, possibly different globs.
- Output shape: is one a superset, or do they disagree?

A diff of their *outputs* on this machine settles most of this in one
command, and is worth more than reading both files.

## Then

One implementation, one command name, doctests for the two rules worth
pinning (effective-mtime dedup, existence-as-signal). The loser is deleted,
not kept as a fallback -- keeping it is how the ambiguity survived.

## Name

`claude-` is wrong for the survivor. It scans bukzor's todo conventions,
not Claude Code sessions; the prefix records where the habit came from, not
what the tool is about. `open-tasks` is the honest name, and renaming is
cheapest before packaging rather than after.
