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

## The corollary worth the whole claim

For a **destructive** verdict, arrange both approximations to point the same way:
under-approximate the numerator, over-approximate the denominator, and the
computed ratio is a *lower bound* on the true one. Such a check can supply sound
evidence to act and never sound evidence to refrain -- which is the asymmetry a
deletion wants and the opposite of what a keep-list needs.

## What would kill it

An exact decision procedure. The declaration is vacuous when both directions are
sound, and demanding it then is ceremony.
