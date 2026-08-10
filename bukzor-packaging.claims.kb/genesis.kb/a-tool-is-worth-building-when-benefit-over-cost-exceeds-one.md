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

They disagree about **order**, and that is the whole reason to prefer the
quotient. With a time budget *B* and many candidates, choosing by decreasing
*b*/*c* is what maximizes total benefit; choosing by decreasing *b* − *c*
does not. The situation here is exactly that shape -- sixteen candidates and
one person -- so the ranking instrument is the one that matters, and the
difference form quietly answers a question nobody asked.

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
