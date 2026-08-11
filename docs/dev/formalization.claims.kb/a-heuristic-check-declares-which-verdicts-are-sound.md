---
label: SOUND
standing: agent
why:
    - a-structure-earns-its-keep-by-the-decision-it-changes.md
verify: ../../../bukzor-packaging.claims.kb/retirement.py
---

# A Heuristic Check Declares Which of Its Verdicts Are Sound

Carrier: a check approximating a predicate too expensive or too undecidable to
compute. Law:

> An **over**-approximation makes its negatives sound. An **under**-approximation
> makes its positives sound. Composing one of each yields a verdict with **no
> sound direction at all**, and a check that measures nothing has none to begin
> with.

Every heuristic check must say which it is, in its own docstring, because the
declaration is not recoverable from the output.

## The three failures, each seen once

- **Weak positives.** A reference graph built from textual mentions
  over-approximates: a comment counts as an edge. Its `NONE` verdicts are
  trustworthy and its "these are coupled" verdicts can rest on a comment.
- **Weak negatives.** A census that recognises a function only when its name
  matches the command under-approximates: a core named by a synonym is invisible.
  Its hits are trustworthy and its misses are not evidence.
- **Neither.** A claim asserting where a file was installed, by a check that had
  never looked at that directory. Not an approximation -- an assertion. **A check
  may not report a location it did not probe.**

## The precondition, which is easy to miss

A one-sided approximation induces a soundness direction **only for a predicate
monotone in the approximated quantity.** Set membership is monotone by
construction, which is why the rule above feels universal -- most checks ask
"is *x* in the set". A threshold on a ratio is monotone too, increasing in the
numerator and decreasing in the denominator, and that is the fact the corollary
below actually uses.

A *two-sided* predicate has no sound direction from any one-sided approximation:
"within ten percent of the target", "this cluster is the right size", any
goldilocks judgment. Approximating either input moves the answer both ways
depending on which side of the target you were on. A check computing such a
predicate must say **neither direction is sound** rather than pick one, and the
temptation is to report the direction that would have applied if the predicate
had been membership.

## The corollary worth the whole claim

For a **destructive** verdict, arrange both approximations to point the same way:
under-approximate the numerator, over-approximate the denominator, and the
computed ratio is a *lower bound* on the true one. Such a check can supply sound
evidence to act and never sound evidence to refrain -- which is the asymmetry a
deletion wants and the opposite of what a keep-list needs.

Stated generally: **the soundness direction is chosen by the cost of being
wrong, not by what is convenient to compute.** For an irreversible act, aim the
approximations so the computed quantity bounds the permitting side. For a cheaply
reversible one, aim them the other way and let the revert be the check -- a
guard is what you build when you cannot aim them at all.

## What would kill it

An exact decision procedure. The declaration is vacuous when both directions are
sound, and demanding it then is ceremony.
