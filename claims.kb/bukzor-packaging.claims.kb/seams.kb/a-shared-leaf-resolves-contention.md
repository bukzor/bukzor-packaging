---
label: LEAF
standing: agent
why:
    - a-tool-has-at-most-one-home.md
---

# A Shared Leaf Resolves Contention

The operation that repairs a violation of
`a-tool-has-at-most-one-home.md`. Given a tool *t* that clusters *A* and *B*
both need, split *t* into a leaf *L* (the knowledge both need) and whatever
per-cluster surface remains, then give *L* its own home and let both *A* and
*B* depend on it.

Laws it must satisfy to count as a resolution:

1. *d* is single-valued again -- *L* has one home, *t* is gone.
2. Every edge that crossed between *A* and *B* now terminates in *L*; no
   *A*↔*B* edge survives.
3. `a-cluster-is-legitimate-when-no-member-is-isolated.md` still holds for
   *A*, for *B*, and for *L*'s home.

Law 2 is the one that does work. If an *A*↔*B* edge survives the split, the
extraction picked the wrong *L* -- the clusters are entangled somewhere else
too, and the second entanglement is the real finding.

## Smallest instance

`claude-slug`, 12 lines: `printf '%s' "$1" | perl -CSD -pe
's/[^A-Za-z0-9]/-/g'`. Three consumers in two would-be packages plus a live
symlink: `claude-path` execs it, `claude-jsonl-path` reaches it through
`claude-path`, and `git-localhost-store` symlinks it to encode store
directory names. It is a leaf by construction -- it references nothing --
and every consumer reaches the encoding through it. Laws 1-3 hold.

That instance is also why the symlink is the wrong mechanism rather than a
clever one: the dependency is real and cross-cluster, which is exactly what
a packaging dependency expresses and a symlink only mimics.

## The pending instance

The renderer. `refactors.kb/display-renders-two-schemas.md` names three
resolutions; **leaf** is this operation applied to `claude-jsonl-display`.
Note it is *not* automatically right: **widen** (widen one package's charter
and let the other collapse into it) satisfies laws 1-3 too, by making *B*
empty. Choosing between them is a cost question
(`../cost.kb/cost-splits-into-site-and-item.md`), not a seam question -- one
more package versus one wider charter.

**split**, cutting the renderer along the schema boundary, is the one
this claim rules out on law 2: the ~40 shared `format_*` content handlers
would have to be duplicated or cross-referenced, so either
`two-implementations-are-one-node-only-after-merging.md` applies or an
*A*↔*B* edge survives.

## What would kill it

A contested tool whose knowledge does not factor -- where every candidate
leaf either drags one cluster's domain into the other or leaves a surviving
cross edge. Then contention is evidence the two clusters are one cluster,
and the honest move is to merge them rather than to extract.
