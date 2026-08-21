---
label: INFLATE
standing: agent
authority: >-
    the agent's, entirely. Presented for ratification 2026-08-11 and declined --
    "i think i don't care enough" -- so it stays `agent` and is in force by
    default, not by a ruling. Do not re-present it; the sign follows from
    `FORECAST`'s own argument and the magnitude wants a measurement, not another
    request
why:
    - predicted-use-is-discounted-by-two-thirds.md
    - a-tool-is-worth-building-when-benefit-over-cost-exceeds-one.md
---

# A Predicted Cost Is Inflated by the Same Coefficient

Carrier: the denominator of `QUOTIENT`, partitioned by evidence exactly as
`FORECAST` partitions the numerator. Law:

> *c*(*a*) = *c*<sub>observed</sub>(*a*) + 3 · *c*<sub>predicted</sub>(*a*)
>
> and the gate becomes
>
> *b*<sub>obs</sub> + ⅓·*b*<sub>pred</sub> > *c*<sub>obs</sub> + 3·*c*<sub>pred</sub>

The mechanism `FORECAST` corrects does not know which side of the fraction it is
on. A forecast made before contact with the work is optimistic because the
forecaster has not met the obstacles yet, and that is as true of the effort as of
the payoff. Discounting one term and leaving the other bare is an asymmetry
nobody chose, and it is *systematically* permissive for exactly the actions with
the least evidence -- the ones where both terms are forecast, so the discount
lands only on the side arguing against.

This is one correction per term, one level each. `PESSIMISM`'s "settled by fiat:
one" is about stacking discounts on a single quantity and is not in tension with
this.

## What it costs a speculative build

An action justified **entirely** by forecast must clear *b* > 9*c*. That number
is startling and it is the right kind of startling: it is the formal content of
the observation that most "while I'm in here" work is a mistake, and it says so
without needing an argument about any particular case.

The two corrections bite the same population rather than two different ones. For
a tool that already exists, *c* is nearly all observed -- the site is built, the
toll is being paid and can be counted. For a tool that does not exist, *c* is
entirely predicted. So both coefficients apply hardest to the unbuilt speculative
candidate, which is why they compose into 9 rather than staying separate.

## This is where `FORECAST`'s missing mechanism went

`FORECAST` maps three of YAGNI's four costs into this ledger and records **repair**
as landing nowhere. Repair is the cost of building the right thing wrong and
rebuilding it, and it exists *only* on the branch where the forecast was wrong --
so it is not a cost term the estimate omitted, it is a cost term that appears only
in *c*<sub>predicted</sub>. An inflation coefficient on that term is exactly the
shape repair has. The table in `FORECAST` now names this claim instead of nothing.

## Smallest instance

`../cost.kb/an-estimate-omits-the-cutover.md`. A realized cost underestimate,
already on file: the estimate for `claude-code-slug` was accurate about the
artifact and silent about the work of switching over to it. One instance, so this
is a conjecture with good manners -- but it is an instance of the right *kind*.
The estimate was not wrong about a number it had; it was missing a category, and
a coefficient is what you use when you cannot enumerate what you are missing.

## Observed so far

One scored forecast exists, and it is the ledger's first: `claude-code-slug`,
cost forecast "call it an hour", realized about an hour **plus two unbudgeted
steps** (`../../dispositions.md`, decision terms). Realized over forecast is
roughly 1.2-1.5 depending on how the steps are priced -- against a coefficient
of 3, from a sample of one, biased easy: the port was predicted "mechanical"
and was. The datum moves nothing yet. It starts the record this file's defeater
asks for, and the maintenance loop now feeds it: every completed action appends
its realized terms to the decision table, and this section cites them.

## What would kill it

A record showing forecast costs landed accurate while forecast benefits landed
optimistic. Then the asymmetry is observed rather than assumed and the bare
denominator was right all along. The other way out is narrower: if the omission
is always the *same* item -- cutover, every time -- then the repair is to itemize
it in `../cost.kb/` and the coefficient is a blur over a fact somebody could just
write down.

The magnitude is the weak part. Taking the reciprocal of ⅓ is an argument from
symmetry, not evidence, and the honest claim is about the **sign**: whatever
correction `FORECAST` applies to a predicted benefit, a predicted cost gets the
inverse.
