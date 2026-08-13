---
label: QUOTIENT
standing: user
authority: >-
    bukzor 2026-08-10: "a cost/benefit quotient evaluation whose aim is to
    lower activation energy/friction on past-and-ongoing activities or (with a
    steep discount, maybe 2/3 off, due to inaccuracies in prediction)
    predicted future activities"
why:
    - ../cost.kb/the-testable-set-is-a-threshold-not-a-property.md
    - ../cost.kb/cost-splits-into-site-and-item.md
---

# A Tool Is Worth Building When Benefit Over Cost Exceeds One

Carrier: candidate actions *a*, each with an estimated benefit *b*(*a*) and
cost *c*(*a*) > 0 in the same units (minutes). Operations: estimate both,
then either gate or rank. Laws:

> **Gate.** Build *a* iff *b*(*a*) / *c*(*a*) > 1.
>
> **Order.** Among candidates competing for one budget, build in decreasing
> *b*/*c*.

## Why a quotient and not a difference

The gate is indifferent: for *c* > 0, *b*/*c* > 1 exactly when *b* − *c* > 0.
So the two forms cannot disagree about whether a single tool is worth
building, and any argument that they do is confused.

They disagree about **order**, and the regime decides which theorem backs the
quotient. When everything worth doing will eventually be done and the order
only decides *when* each benefit starts arriving, minimizing the benefit
forgone to delay (Σ *b*ⱼ · completion time) is a sequencing problem, and
decreasing *b*/*c* is **Smith's rule** -- optimal, not heuristic. When a hard
budget truncates the list instead, the problem is 0/1 knapsack and
density-greedy is only an approximation: with budget 10, an item at *b*/*c* =
10, *c* = 1 ranks above one at *b*/*c* = 2, *c* = 10, and taking the dense one
first yields 10 where the big one alone yields 20. The situation here is the
first regime -- one person, a rolling budget, no deadline -- so the quotient is
the right instrument for a better reason than this section used to give: the
earlier text claimed optimality *under a budget*, which is the regime where the
claim is false. The difference form still answers a question nobody asked.

## Smallest instance

`claude-slug` versus `claude-open-tasks`. The second has the larger *b* − *c*
by any estimate: a real algorithm, worktree dedup by effective mtime, a
sibling to absorb. It also costs several times more. `claude-slug` is an hour,
and two other candidates depend on it. Ranked by difference the big one goes
first; ranked by quotient the leaf goes first, and the leaf is also what
unblocks the others. The quotient agrees with the intuition that put
`claude-slug` at the top of `packages.kb/` in the first place.

## What would kill it

A binding constraint that is not a budget of one fungible resource. If the
real limit were "only one release this quarter" or "this needs a capability
nothing else provides", density ranking is wrong and the answer is chosen by
the constraint instead. Watch for it when the tools stop being independent:
quotient ranking assumes the items do not change each other's numerators, and
`../seams.kb/a-shared-leaf-resolves-contention.md` describes a case where one
build lowers the next one's cost.
