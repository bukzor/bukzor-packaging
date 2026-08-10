---
label: TWIN
standing: bare
why:
    - a-cluster-is-legitimate-when-no-member-is-isolated.md
verify: ../seams.py --twins
---

# Two Implementations Are One Node Only After Merging

Duplication is not an edge. Two tools that implement the same knowledge
twice are two vertices of *G* with nothing between them, and *G* is right
about that: neither breaks when the other changes. They drift instead, which
is strictly worse than breaking, because breaking is observable.

This is why the promotion gate in
`a-cluster-is-legitimate-when-no-member-is-isolated.md` is stated on *G*.
A cluster of twins looks cohesive at every level a reader inspects -- same
domain, same artifact, same vocabulary -- and shares no line of code.

## Smallest instance

Two ~200-line scripts that scan for the same files, name neither each other,
and already answer differently in three measurable ways -- including one where
14 task files are visible to one and not the other. Exhibit and measurements:
`../case-study.kb/the-open-tasks-twins-already-disagree.md`.

## What this costs the seam law

It means a latent verdict (`a-cluster-may-be-seamed-latently.md`) is a
finding of *risk*, not of cohesion. The cluster that reads as the most natural
in a plan can be the one carrying a live inconsistency, and then the merge is a
precondition for the package rather than a cleanup afterward.

## What would kill it

Deliberate, tested duplication: two implementations kept apart on purpose
with a differential test asserting they agree. Then the test is the edge --
it references both, so *G* joins them through it -- and the law is satisfied
without a merge. Nothing in `~/bin` has such a test, which is why this claim
is worth writing down rather than assuming.
