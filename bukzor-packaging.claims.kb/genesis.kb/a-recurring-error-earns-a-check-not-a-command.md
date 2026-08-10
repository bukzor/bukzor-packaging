---
label: ERRORCOST
standing: agent
authority: >-
    bukzor 2026-08-10 names this as separate from friction: "a cost-reduction
    of frequently encountered errors"
why:
    - friction-is-paid-per-invocation.md
    - ../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md
---

# A Recurring Error Earns a Check, Not a Command

The second benefit kind. It is separate from `FRICTION` in both the numerator
and the artifact it justifies.

Carrier: a failure mode that recurs. Law:

> *b*<sub>error</sub> = incidence × (detection + repair + damage)

What distinguishes it from friction is that **the activity is not hard today
-- it succeeds.** What recurs is the failure, and the three cost terms are
separately reducible: a check cuts detection to near zero, a repair tool cuts
repair, and only prevention touches damage.

The artifact this benefit buys is therefore usually not a command anyone runs
for convenience. It is a check that runs on a schedule, in a hook, or in CI --
something whose whole job is to move a cost from *damage* to *detection*.
Reaching for a wrapper when the numerator is `ERRORCOST` builds the wrong
thing.

## Smallest instance

`coherence.py`. Nobody invokes it to get work done; it exists because a
derived key decays silently
(`../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md`). Its
incidence is low and its damage term is severe and delayed -- a store recovery
that finds nothing and quietly creates an empty one, which the session note
calls "the system's whole purpose failing quietly". Detection was infinite
before the check and is now one command. The repair and damage terms are
untouched, and the claim is honest about that: what was bought is detection.

## Why the damage term is the one to argue about

Incidence and repair are measurable; damage is where estimates go wrong,
because a silent failure's damage is a function of how long it stays silent.
That is the term that makes a low-incidence error worth a check anyway, and it
is the term with no proxy. State it explicitly or the quotient is decorative.

## What would kill it

An error whose damage a check cannot detect any earlier than the current
process does. Then detection is already zero-cost, the numerator collapses to
repair, and what is earned is a fix rather than a check. Also killed if a
class of errors turns out to be cheaper to *tolerate* than to detect --
which is a real outcome and the one
`../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md` records: the
31 stale keys were priced and carried on purpose.
