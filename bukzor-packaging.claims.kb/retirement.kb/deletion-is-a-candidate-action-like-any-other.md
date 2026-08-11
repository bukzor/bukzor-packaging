---
label: PRUNE
standing: agent
authority: >-
    the gate is bukzor's 2026-08-11 -- "that savings needs to outweigh the sum
    of future cost-benefit of keeping the tool (with a 2/3 discount, due to
    unreliability of such predictions)"; the identification with `QUOTIENT`,
    and the consequence that builds and deletions rank on one list, are this
    claim's own
why:
    - maintenance-cost-is-paid-per-encounter.md
    - ../genesis.kb/a-tool-is-worth-building-when-benefit-over-cost-exceeds-one.md
    - ../genesis.kb/predicted-use-is-discounted-by-two-thirds.md
    - ../closure.kb/a-guard-names-a-reversal-cost.md
verify: ../retirement.py
---

# Deletion Is a Candidate Action Like Any Other

Carrier: the action *delete t*, priced exactly as `QUOTIENT` prices any
candidate. Numerator: the toll `TOLL` stops charging. Denominator: the benefit
forfeited, under `FORECAST`'s partition. Law:

> **Gate.** Delete *t* iff *m*(*t*) / *cb*(*t*) > 1.
>
> **Order.** Among candidates competing for one budget, act in decreasing
> ratio -- deletions and builds in the same ordering.

## This is not a new gate, and that is the finding

`QUOTIENT` ranges over *candidate actions*. Deleting is one. Every rule in this
ledger was nonetheless applied only to constructive moves, so the population
could grow and never shrink -- which looked like a missing rule and was really
**a silently restricted domain of an existing one.** The index held one `retire`
verdict reached by looking rather than by pricing, and nothing generalized it.

Naming the restriction is most of the repair. Two consequences arrive with it.

**The discount transfers, but only with its partition.** The rule as stated
discounts "the sum of future cost-benefit", and read literally that cuts the
whole denominator to a third, because all of a tool's remaining benefit is in
the future. `FORECAST` says otherwise: *ongoing* use sits with the observed, not
with the predicted. So a tool in weekly use keeps a full-weight denominator and
only its speculative part -- "I will want this when I next do X" -- is cut to ⅓.
Without that partition the gate deletes live tools, which is the one failure mode
a deletion rule cannot have.

**Deletions and builds rank on one list.** This is the sharper half. A deletion
at ratio 4 outranks a build at ratio 2 for the same hour, and no list in this
project has ever held both -- `.claude/todo.md` enumerates work that adds. That
is the operational content of "subtract, don't accrete": not a preference for
small systems, a claim that removals compete at the same density and usually win,
because their numerator is measured and a build's is forecast.

## Why it is safe to be aggressive here

A gate this cheap to fire needs `GUARD`, and it has one for free: a deletion
inside a tracked tree is reversible for the price of a `git revert`, so the
reversal cost is near zero and no guard is earned. The exceptions are exactly the
two the ledger already knows -- an **untracked** file, where deletion is
irreversible and the reversal cost is the whole rebuild, and a **published**
artifact (`../closure.kb/only-a-successful-publish-is-irreversible.md`). So
"commit eagerly" is not adjacent housekeeping; it is the precondition that makes
this gate applyable without a review step.

## Smallest instance

`claude-export`: 86 lines, `unsettled`, named eleven times in the record and
**never once invoked** in 298 session logs or bukzor's shell history
(`../case-study.kb/the-unseamed-cluster-is-also-the-unused-one.md`). Its
denominator therefore has no observed component at all, so it is ⅓ of a forecast,
against a numerator of 86 lines in the hot namespace. The gate says delete, and
says it rebuttably: one named caller the logs cannot see -- a hook, another
checkout -- restores the denominator and the row closes the other way. **That is
what a gate is for; the point is that it has never been fired at this row.**

## What would kill it

The exchange rate, which does not exist. *m* is an encounter count and *cb* is an
invocation count, and nothing here has ever converted either into minutes -- so
the quotient is a form awaiting units, and `../retirement.py` reports the two
counts rather than a ratio for exactly that reason. The gate is usable today only
where one term is *zero*, which is the case `SUBSUME` covers and the case the
check flags. A worked conversion would promote this claim; a demonstration that
the two are incommensurable in principle would kill it.
