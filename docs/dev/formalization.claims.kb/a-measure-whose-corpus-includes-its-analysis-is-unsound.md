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

## The fix is a temporal cut, not a content filter

The obvious repair is to classify each session as *about* the object or *using*
it and drop the meta ones. **That inverts the direction it was meant to
protect.** An analyst studying a thing also runs it, so a meta session holds real
invocations as well as bare mentions; dropping the session drops both, counts
fall, and zeros reappear *manufactured*. The census then under-approximates the
very term that licenses a deletion -- sound evidence to refrain, which is the
one thing a destructive check must never manufacture (`SOUND`'s corollary).

The repair that keeps the direction is a **temporal cut**: restrict the corpus to
events recorded before the study opened. It is decidable from a timestamp, it
makes no judgment about anybody's purpose, and for any object older than the
study it is exactly the unpolluted record. Its residual weakness is narrow and
statable: an object whose use began after the study looks unused.

The general form -- **a self-referential measurement is repaired by stratifying
its corpus** -- holds, but the stratification must be by something the analyst
cannot influence. Time is such a thing; topic is not, because the analyst chooses
the topic.

Do not reach for a longer time window instead. Averaging the pollution over more
history dilutes it without removing it, and the dilution is invisible in the
output.

## The pollution is not confined to the measure you noticed

Every measure over that corpus is affected, including the ones on the other side
of the inequality. A study that types an object's name also *edits* the object,
so a cost measure counting edits inflates alongside the use measure counting
mentions -- and a ratio of two inflated terms has an **ambiguous** bias, which is
strictly worse than a known one. Audit the whole expression, not the term whose
pollution was embarrassing enough to notice.

## What would kill it

A corpus the analyst cannot write to -- an external log, a third party's usage
telemetry. Then the sound direction survives contact with the study and the
partition is unnecessary.
