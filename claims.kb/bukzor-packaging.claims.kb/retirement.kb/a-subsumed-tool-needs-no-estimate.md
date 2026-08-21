---
label: SUBSUME
standing: user
authority: >-
    bukzor 2026-08-11: "a tool that's been completely subsumed has zero
    cost-benefit, since future benefits will come from elsewhere and
    (presumably) better"
why:
    - deletion-is-a-candidate-action-like-any-other.md
    - ../coherence.kb/two-live-implementations-are-resolved-by-search-order.md
---

# A Subsumed Tool Needs No Estimate

`PRUNE`'s fast path, and the only case the gate decides without units.

Carrier: the **existing** population, ordered by *t* ⊑ *u* -- "*u* does
everything *t* does, at least as well". Operations: ⊑ is a preorder; retirement
by subsumption deletes non-maximal elements; mutual subsumption is duplication.
Law:

> The benefit of keeping is **marginal**: *cb*(*t*) = value(*t*) − value(best
> existing alternative to *t*). So *t* ⊑ *u* for any *u* ≠ *t* forces
> *cb*(*t*) ≤ 0, `PRUNE`'s denominator vanishes, and the deletion is decided
> with no estimate of anything.

The marginal reading is the whole content. An absolute benefit is what makes dead
code feel valuable -- it does work, the work is useful -- and the counterfactual
is that the work still happens, elsewhere, better.

## Mutual subsumption is coherence's case

When *t* ⊑ *u* **and** *u* ⊑ *t*, the order collapses to an equivalence and the
theory says only "delete one". It does not say which, and neither does anything
else: `SHADOW` shows the runtime picking by search order, silently, with nobody
deciding. So duplication is the degenerate case of subsumption -- which is why
`../coherence.kb/` can diagnose a duplicate and never name the survivor, and why
that omission is not an oversight in it.

## Two boundaries the population walks right up to

**The subsumer must exist.** "This should be a flag, not a command" argues
*t* ⊑ *u* for a *u* nobody has built, and by that standard everything is
subsumed by an imagined better version. `claude-jsonl-to-log` is indexed
precisely so -- 25 lines, "thin driver over `-display`; likely a flag, not a
command" -- and it is **not** retirable: deleting it before the flag exists
removes capability. That is why the index files it as a refactor and not as
`retire`, and the distinction is load-bearing enough to be worth the sentence.

**Use counts cannot decide it.** A subsumed tool may be the most-invoked thing on
the machine; the replacement absorbs every one of those invocations, so the
*difference* is zero at any count. `../retirement.py`'s histogram therefore
answers a different question than this claim does, and reading a subsumption off
it is a category error. Subsumption is a statement about code, and the instrument
for it is the reference graph.

## Smallest instance

The store-key encoder, three implementations down to one. The interesting
retirement is the vendored copy in `bukzor-agent-skills`: it survived a
packaging, defended by needing to run standalone, and was retired the same day a
PEP 723 header let it name `claude-code-slug` as a dependency. **Subsumption
completed by the subsumer becoming reachable, not by becoming better** --
`(bukzor-agent-skills ba513bc)`, and the argument it overturned is quoted against
itself in `../coherence.kb/two-live-implementations-are-resolved-by-search-order.md`.

## What would kill it

A dominance that fails on one axis nobody wrote down: startup time, working
offline, running on a machine without the package, an exit code somebody parses.
Then ⊑ never held, and the deletion removed capability while the ledger recorded
a tidy-up. The test is not "does the replacement do more" but **"does it do more
on every axis some caller uses"**, and callers rarely publish their axes -- which
is the same blind spot that makes an unlogged caller invisible to `PRUNE`'s check.
