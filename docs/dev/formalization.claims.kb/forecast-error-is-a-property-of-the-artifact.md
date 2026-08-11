---
label: COVERAGE
standing: agent
why:
    - discount-the-predicted-term-once-at-the-outermost-level.md
---

# Forecast Error Is a Property of the Artifact, Not the Forecaster

Carrier: the artifact you build, *p*, and the need that eventually arrives, *q*.
Law:

> realized benefit = benefit(*q*) × P(*p* covers *q*)
>
> and the second factor is read off *p*'s **shape**, not off the forecaster's
> confidence.

A coefficient on the magnitude of a forecast models "you will not need it". It
cannot model the more common failure: you *did* need it, and what you built is not
what was needed, because the requirement took its shape after you committed to
one. That is a mismatch in kind, not in size.

## Why this is the useful half

**P(needed) is not controllable and P(cover) is.** A typed, composable thing can be
recomposed when *q* turns out different, so its coverage is high by construction;
an opaque effectful thing offers nothing to recompose and gets rewritten instead.
The whole of "build it composable" is hiding inside a term that looked like a
statement about prediction.

## The exemption becomes a theorem

YAGNI's own carve-out is that it "only applies when you introduce extra complexity
now that you won't take advantage of until later", and does not apply to work that
makes the software easier to modify. That is precisely the P(cover) = 1 case. So
the exemption is not a caveat bolted onto the principle -- it is where the second
factor is one, and the principle has nothing left to say.

The same reasoning bounds how far the principle reaches. Speculation carried in a
small composable unit costs a fraction of the same speculation carried as an
abstraction everything routes through, because coverage is high *and* the thing is
encountered rarely.

## What would kill it

A drift event running the other way: the well-typed composable unit rewritten
while the opaque one survived untouched. One such event is enough, and it is the
observation to watch for, because it would mean coverage tracks something other
than shape.
