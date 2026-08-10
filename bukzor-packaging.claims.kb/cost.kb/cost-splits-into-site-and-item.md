---
label: SITE
standing: agent
why:
    - ../levels.kb/observation-comes-in-four-levels.md
---

# Cost Splits into Site and Item

Carrier: subsets *S* of tools. Operation: package *S* together. Cost:

> *c*(*S*) = *F* · [*S* ≠ ∅] + Σ*ₜ*∈*S* *m*(*t*)

*F* is the **site cost** -- everything you pay once for the existence of a
package, independent of what goes in it. *m*(*t*) is the **item cost** --
porting, doctesting, and wiring one tool.

Two laws follow, and both are visible in the record:

**Cost per tool falls with cluster size.** *c*(*S*)/|*S*| → *m̄* as |*S*|
grows. So there is always a pull toward fewer, larger packages, and
`../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md` is what
stops that pull from swallowing everything -- it is the only thing that does.

**Lowering *F* reopens settled questions.** Every "not worth packaging"
verdict is a comparison against *F*, so *F* falling invalidates the whole
back catalogue at once. That is not hypothetical: it is why this kb exists.

## Smallest instance

`claude-slug`, estimated in `packages.kb/claude-slug.md`: "a
`pyproject.toml`, two entry points, a meta-package row, a README row, and
the port itself -- call it an hour." Decomposed: *F* ≈ 15 min (the
`pyproject.toml`, the meta-package `dependencies` row plus
`[tool.uv.sources]`, the README row), *m* ≈ 20 min each for two tools that
are 12 and 23 lines.

Compare the same package as a standalone repo: a PyPI name, a CI workflow,
a README, a release process, a `.pre-commit-config.yaml` -- hours, and
recurring. `bukzor-tools` bought *F* down by roughly an order of magnitude,
which is exactly the user's framing: cost-sensitive, cost lowered by the
existence of the workspace.

## Where the split is load-bearing

Choosing between **widen** and **leaf** for the renderer
(`refactors.kb/display-renders-two-schemas.md`) is *only* a comparison of
*F* against the cost of a wider charter. There is no architectural
disagreement left once
`../seams.kb/a-shared-leaf-resolves-contention.md` shows both satisfy the
seam laws. Naming the choice as an *F*-sized decision is what keeps it from
being re-litigated as though it were a design question.

## What would kill it

Site cost that is not fixed -- a coupling term. There is a candidate: the
meta-package must re-declare every member's `[project.scripts]`, so each new
package edits a shared file, and *F* grows slowly with the number of
packages. If that term ever dominates, *c* is superadditive and the pull
reverses toward fewer packages for a second, independent reason.
