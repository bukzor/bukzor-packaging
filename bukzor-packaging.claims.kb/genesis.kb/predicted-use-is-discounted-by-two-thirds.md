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
