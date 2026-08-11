---
label: REFLEX
standing: agent
why:
    - a-heuristic-check-declares-which-verdicts-are-sound.md
verify: ../../../bukzor-packaging.claims.kb/retirement.py --observed
---

# A Measure Whose Corpus Includes Its Own Analysis Is Unsound

Carrier: a measure *M* over a corpus *C*, where the act of measuring appends to
*C*. Law:

> Studying an object writes evidence about that object into the record. So the
> over-approximating direction -- the one where a **zero** is trustworthy -- is
> destroyed by the analyst, and destroyed worst for exactly the objects under
> study.

## Smallest instance

A use census counting a tool's name anywhere in a command line. Over-approximating
by design, so a zero would have been sound; every one of twenty tools scored
nonzero, because two days of formalizing typed all twenty names. **The measure was
not wrong, it was polluted, and the pollution was the analysis itself.**

## The fix is a partition, not a caveat

Stratify the corpus by whether the session was *about* the object or *using* it,
and exclude the meta sessions. Here that is computable and cheap: a session that
greps the tool namespace and edits the ledger is meta. The general form -- **a
self-referential measurement is repaired by stratifying its corpus** -- is the
standard move against self-reference and it works for the same reason it always
does.

Do not reach for a longer time window instead. Averaging the pollution over more
history dilutes it without removing it, and the dilution is invisible in the
output.

## What would kill it

A corpus the analyst cannot write to -- an external log, a third party's usage
telemetry. Then the sound direction survives contact with the study and the
partition is unnecessary.
