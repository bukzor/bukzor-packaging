---
label: PROXY
standing: bare
why:
    - observation-comes-in-four-levels.md
verify: ../seams.py --isolated
---

# The Name Abstraction May Narrow but Never Decide

Let α send a tool to its L0 observation. A predicate P is *decidable in the
abstract* when it factors through α -- when α(t) = α(u) forces P(t) = P(u).

`is-it-python` factors. `carries-knowledge-worth-testing` does not:
`claude-plan` and `claude-jsonl-path` are both one-to-three-line shell files
with a `claude-` prefix, and one is a dead preference while the other is a
locator over a reverse-engineered encoding.

So α licenses exactly one move: **ordering what to read**. It never licenses
a conclusion about a non-factoring predicate. Triage by name, decide by
contents.

## The instance that produced it

2026-08-09, two calls made in one paragraph by reading filenames and
recalling roles rather than opening files:

- `claude-path` was left in dotfiles because "it has an external consumer".
  The consumer was 49 files in the *same* repo, and itself a graduation
  candidate -- which inverts the conclusion.
- The residual group was called glue with "no testable knowledge".
  `claude-open-tasks-list` is 212 lines of Python implementing worktree
  dedup by effective mtime.

Both are the same error: substituting α(t) for t. The `verify` above makes
the substitution's damage visible -- grouping by L0 leaves eight of sixteen
scripts isolated at L1, so an L0 cluster is not even a candidate for a
package by `../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md`.

## What would kill it

A cheap L0 feature that happens to correlate with the predicate well enough
to decide -- a shebang-and-line-count rule, say, that never misfiles a tool.
The 2026-08-09 instances are two counterexamples, so this would need to
explain them away, not merely score well elsewhere.
