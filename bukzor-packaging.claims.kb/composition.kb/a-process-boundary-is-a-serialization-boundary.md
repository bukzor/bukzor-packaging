---
label: BOUNDARY
standing: agent
why:
    - a-pipeline-loses-information-only-at-its-joints.md
    - ../cost.kb/cost-splits-into-site-and-item.md
    - ../cost.kb/the-site-discount-is-language-relative.md
---

# A Process Boundary Is a Serialization Boundary

Carrier: an assignment of tools to processes and to packages. Law:

> Inside one process, composition is a function call and costs nothing. Across a
> process boundary it is a **serialization round trip**, so the cost a partition
> incurs is a sum over the arrows *crossing* it -- a **cut**. The cost a
> *packaging* incurs is different in kind: a fixed charge *F* per package.

Two terms, two different pulls, and the whole value of this claim is that they
are not the same term:

| term | shape | minimized by |
|---|---|---|
| Σ *F* over packages | fixed charge per part | **one package** |
| Σ joint over crossing arrows | a cut | **one process** |

## The conflation this corrects, including mine

The long-observed "pull toward fewer, larger packages" is a property of the
*first* term. It is a fixed charge, and no arrangement of the arrows changes it.
So the hope that cheap joints would relax that pull -- "my capnproto-pipes
should make this cut near-zero-cost, making the pull near-zero" -- lands on the
second term instead, and the two are independent: two packages in one venv
compose by **import**, with no joint at all.

What cheap joints actually buy is therefore sharper and better:

> **Cheap serialization buys small tools, not big packages.** The pull it
> releases is the pull toward one monolithic command with subcommands, because
> that is the arrangement that avoids joints.

*F* is untouched by any of it, and `../cost.kb/the-site-discount-is-language-relative.md`
already says what to do about a fixed charge: lower it, do not cluster to
amortize it. With the cut below *F*'s noise floor, the package partition is free
to follow ownership and release cadence rather than data flow -- which is the
version of the dream that survives, and a better one, since data flow was never
the thing that hurt.

## The fixed charge makes package creation a discontinuity

*F* is charged on the *existence* of a package, so the marginal cost of moving
one tool into a new package is *F* + *m*(*t*) while the marginal cost of moving
it into an existing one is *m*(*t*). Consequence:

> **No sequence of single-tool improving moves can ever create a package.**

Every local step from "one package" toward "two" looks like a loss, and the
gains only appear after the second or third tool arrives. So splitting is
necessarily a deliberate act, argued in advance and against a plan -- never
discovered by local search, and never justified by the first member alone. That
is the formal shadow of the thing that actually happened here: `bukzor-tools`
lowered *F*, and the answer to a question nobody had re-asked changed.

## What a joint costs, corrected

Not fork and exec. Pipeline stages are forked concurrently, so startup is
max<sub>*i*</sub>(startup<sub>*i*</sub>) rather than a sum, paid **once per
invocation**, and amortized over however long the stream runs. bukzor's
correction, and it kills two conclusions that were resting on the opposite
assumption -- that a multi-call binary is justified by startup, and that
subcommands amortize it.

The residual is real but it lives elsewhere: an **ITEM** tool pays startup *per
item*, because the fork is per invocation and the invocation is per unit of
work. Live instance, unpriced: `git-localhost-store` invokes `claude-path` on
every hook firing in roughly fifty repositories, and the perl-to-Python port
replaced a perl one-liner with an interpreter start. Nobody measured whether
`git commit` got slower. `hyperfine` against the retired pair would settle it,
and until someone runs it this is a cost the kb asserted was negligible without
looking -- exactly the failure `../cost.kb/an-estimate-omits-the-cutover.md` is
about.

## Submodularity, resurrected in the right objective

`../../bukzor-packaging.claims.md` records a killed conjecture: cost as a
submodular set function, greedy clustering near-optimal. It died because
*m*(*t*) depends on *S* -- extracting a shared leaf changes it.

A cut does not have that defect. A crossing arrow's joint cost depends on the
pair it joins, not on the rest of the partition, so **the cut term is submodular
by construction** while the build term is not. The conjecture was killed in the
wrong objective.

That buys understanding, not a solver: with sixteen tools the optimization is
still a table, so the entry point's second objection stands unrepaired. What the
structure explains is the discontinuity above -- diminishing returns in the cut,
a fixed charge in *F*, and therefore a threshold rather than a gradient.

## What would kill it

A boundary whose cost is not a function of the arrows crossing it -- and this kb
already contains one. Three packages each embedding the store-key encoding have
a cut of **zero** and a coherence cost that took a day to repay. Duplication is
the case where two sides must agree on a *fact* rather than pass data; the cut
sees nothing, because there is no arrow. That case is
`../coherence.kb/`'s and no serialization discipline touches it, which is the
boundary of this claim rather than a defect in it.
