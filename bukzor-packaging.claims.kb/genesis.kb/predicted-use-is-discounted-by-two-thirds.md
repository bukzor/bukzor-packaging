---
label: FORECAST
standing: user
authority: >-
    bukzor 2026-08-10, naming the discount and its reason: "with a steep
    discount, maybe 2/3 off, due to inaccuracies in prediction"
why:
    - a-tool-is-worth-building-when-benefit-over-cost-exceeds-one.md
---

# Predicted Use Is Discounted by Two Thirds

Carrier: the uses of a candidate tool, partitioned by evidence rather than by
time. Operation: sum them into the numerator of `QUOTIENT`. Law:

> *b*(*a*) = *b*<sub>observed</sub>(*a*) + ⅓ · *b*<sub>predicted</sub>(*a*)
>
> where *observed* covers past **and ongoing** activity -- things there is
> already a record of -- and *predicted* covers everything argued from "I will
> probably want to".

The partition is the load-bearing part; the coefficient is a stated guess.
Ongoing sits with observed, not with predicted: a thing being done weekly
right now is evidence, not a forecast.

## What the discount does

It sets a price on speculation. A tool justified entirely by prediction needs
**three times** the benefit of one justified by record to clear the same bar.
That is enough to kill most "while I'm in here" tools without needing an
argument about them, and it is why the discount is worth stating as a number
rather than as an attitude.

It also explains a pattern in `dispositions.md` that otherwise looks like
inconsistency: `claude-jsonl-summarize` sits at `unsettled` with the reason
"not yet read closely", while tools of similar size are settled. Nothing about
it has been observed. Under this law that is not a gap in the analysis, it is
the analysis -- a candidate with no observed use and no read code has a
numerator that is all forecast, and ⅓ of an unmeasured guess does not clear
anything.

## What the coefficient stands in for

The discount operationalizes YAGNI, and exactly one of its four mechanisms.
Fowler's *Yagni* (martinfowler.com, 2015) prices a presumptive feature at cost of
**build**, **delay**, **carry** and **repair**. Three of those already have homes
here, in three different theories:

| YAGNI cost | where it lives |
|---|---|
| build | `QUOTIENT`'s denominator, *c*(*a*) |
| delay | `QUOTIENT`'s *Order* law -- ranking by density under one budget *is* displacement |
| carry | `../cost.kb/cost-splits-into-site-and-item.md`'s *m*(*t*), paid for the whole wait |
| repair | `a-predicted-cost-is-inflated-by-the-same-coefficient.md` -- it lives in the *denominator*, and only in its predicted part |

**Repair was the gap, and finding it took two steps.** The first is that it is a
bias where this claim models a variance. The coefficient shrinks the *magnitude*
of a forecast benefit, which says "you probably will not need it". Fowler's middle
case is the right feature built wrong: you do need it, and the artifact you built
is not the artifact needed, because the requirement took its shape after you
committed to one. A coefficient on the magnitude cannot express a mismatch in
kind. The honest decomposition is two factors:

> *b*<sub>predicted</sub> = P(needed) × P(what you build is what is needed |
> needed) × Δ

and the **second factor decays with the forecast horizon** while a flat ⅓ does
not. So ⅓ is about right for something wanted next week and far too generous for
something wanted next year.

The second step is that repair is not a shrunken benefit at all. It is work --
rebuilding the thing you built wrong -- and work is a cost, incurred only on the
branch where the forecast missed. So it belongs to *c*<sub>predicted</sub>, which
this ledger left uncorrected while correcting *b*. `INFLATE` carries it, and the
gate gets its missing half.

One consequence runs the other way, and it is why this population is not simply
a YAGNI violation. Fowler's carve-out is explicit: the principle "only applies
when you introduce extra complexity now that you won't take advantage of until
later", and not to work that makes the software easier to modify. A standalone
command is nearly the minimum-complexity case -- `unit -> unit` to everything
else, encountered only in an `ls` of a flat namespace, obscuring no code that
serves a current requirement -- so its carry cost is a fraction of what the same
speculation costs as an abstraction inside a program. **YAGNI binds far less
tightly on a tool than on a feature**, which is a defensible basis for building
many small ones rather than an excuse for it.

Left unsettled: `REUSE` already carries a P(needed again), and this claim then
takes ⅓ of it. Two corrections for one uncertainty, composed by nobody -- a
`REUSE`-justified tool is discounted twice, and whether that is intended has
never been said.

## Smallest instance

`claude-plan`, one line, retired. Its entire benefit was predicted -- a
`--model=opusplan` alias for a flag value that current `claude --help` does
not offer. Observed use: none findable. Discounted forecast of a benefit that
no longer exists is still zero, which is why the retirement needed no
argument beyond looking.

## What would kill it

A domain where prediction is reliable. The discount is a correction for
forecast error, so if a class of predictions turned out well-calibrated --
say, tools predicted from a written plan rather than from a hunch -- the
coefficient should rise toward 1 for that class. The honest version of this
claim is that ⅓ is a prior, and the way to overturn it is a record of past
predictions and how they landed. No such record exists here, which is itself
an argument for keeping the discount steep.
