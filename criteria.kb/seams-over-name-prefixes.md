# Cluster on seams, never on name prefixes

A shared filename prefix is evidence of shared *history*, not shared
purpose. `~/bin/claude-*` contains at least five unrelated subjects: an
encoding, transcript rendering, live streaming, task aggregation, and
session-file surgery. A `claude-code-tools` package defined by the prefix
would have no seam at all -- its members would share nothing but the
author's habit of prefixing.

The rule works in both directions, and the second direction is the one
that bites:

- **Don't cluster by prefix.** Ask what a member would import from its
  siblings. If nothing, it isn't a package, it's a directory.
- **Don't rule out by prefix either.** `claude-slug` and
  `claude-code-archeology` share more than a prefix: one implements the
  encoding the other must never invert. That's a seam.

## The failure this came from

2026-08-09, in one paragraph, two calls were made by reading filenames and
recalling roles rather than opening files:

- `claude-path` was left in dotfiles because "it has an external consumer
  (git-localhost-store symlinks it)". The consumer is not external -- it's
  49 files in the same dotfiles repo -- and it is itself a graduation
  candidate, which inverts the conclusion completely.
- The residual group was called glue with "no testable knowledge".
  `claude-open-tasks-list` is 212 lines of Python implementing worktree
  dedup by effective mtime.

Both errors are one error: **grading a tool by its name and its place in
the author's habits instead of by its contents.** The correction is
mechanical -- open the file before assigning it -- and the cost of skipping
it is a wrong cluster that then gets built.

## Counter-pressure

Opening 16 files costs real context. The cheap partial defense: a prefix
group may be *triaged* by name (size, language, shebang) but may not be
*decided* by name. Triage narrows what to read; it never substitutes for
reading.
