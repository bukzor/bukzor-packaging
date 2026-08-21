---
label: GUARD
standing: agent
why:
    - building-closes-open-questions-by-accident.md
---

# A Guard Names a Reversal Cost

`refactors.kb/` entries carry `blocks:` -- the candidates that should not be
built until this refactor resolves. It is the kb's only mechanism against
accidental closure, and it is load-bearing precisely because it is cheap to
overuse.

The rule that keeps it honest:

> **Block *a* on *q* only when reversing *a*'s closure of *q* costs more than
> performing *a*.** Otherwise build, learn, and revisit.

A `blocks:` without a named reversal cost is a superstition, and it does
active harm: a field that fires on everything is a field readers learn to
route around. The kb already says the sharp version of this -- *a stale
`blocks:` is worse than none* -- and the reversal-cost test is what keeps
guards from going stale in the first place, since a guard with a stated cost
is a guard you can see has been paid.

## Justified guard

`display-renders-two-schemas.md` carries
`blocks: [claude-code-archeology, claude-stream]`. Reversal cost, named: the
renderer's home shows up in git history, in a dist name that
`uv tool install` shims, in the meta-package's `[project.scripts]` block, and
in whatever imports it. Undoing it is a second move plus a deprecation, and
it is the kind of move that leaves a stale command on every machine that
installed the first version. Costlier than doing the analysis first -- which
the entry itself sizes at "count how much of the 714 lines is
schema-specific". Guard justified.

## Guard not needed

The twins' `ROOTS` disagreement
(`../seams.kb/two-implementations-are-one-node-only-after-merging.md`) is a
real undecided question -- union or intersection, and each choice changes one
tool's output. It still needs no `blocks:`. Reversal is a one-line edit to a
tuple, with no released surface and no data on disk keyed by the answer. Merge
first, argue about `ROOTS` in the review, change the line if wrong.

Distinguishing those two cases is the whole content of the claim. Both are
"an undecided question in the path of a build"; only one is worth stopping
for.

## The uncomfortable corollary

`blocks:` covers acts of commission only, and the two failure modes it cannot
reach are both live:

- **A decision whose residue nobody measured.** The encoding migration was
  declined deliberately -- and the population it left stale was counted for the
  first time months later, at 31
  (`../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md`). No guard
  applies; the decision was made on purpose. What was missing is a number.
- **An expedient nobody was going to block.** The hand-repair of one store
  during unrelated work was not an action anyone would have thought to guard.

Both need the other instrument: a check that runs. That is why
`../coherence.kb/` demands a `verify:` of every claim, and why its guide says a
claim without one belongs in a different theory.

## What would kill it

A cheap-to-reverse action whose closure still did real damage -- damage that
is not proportional to reversal cost. Reputational or coordination damage
would qualify: a decision that is trivial to undo in the repo but that a
second person has already built on.
