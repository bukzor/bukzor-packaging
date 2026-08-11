---
label: RATCHET
standing: agent
authority: >-
    the coefficient is `FORECAST`'s and therefore bukzor's; that one
    coefficient gates both directions, and that the observed bottleneck is the
    action rather than the verdict, are this claim's own
why:
    - deletion-is-a-candidate-action-like-any-other.md
    - ../genesis.kb/predicted-use-is-discounted-by-two-thirds.md
verify: ../retirement.py
---

# The Forecast Discount Cuts Both Ways

Carrier: the population of tools over time, under repeated application of the two
gates. Law:

> One coefficient, two gates, one direction. ⅓ on speculation **raises** the bar
> to build -- a forecast-only tool needs three times the benefit -- and
> **lowers** the bar to delete, because a forecast-only denominator survives at a
> third of its claimed size. Distrust of prediction is monotone pressure toward
> less code.

Neither gate is symmetric on its own, and the asymmetry is not an accident of
where the coefficient was written down: the discount lands on the **predicted**
term both times, and the predicted term is the numerator at genesis and the
denominator at retirement. So the same epistemic policy shrinks the population
from both ends.

## Two things keep the ratchet from turning

Both are observed, and the second is the one that matters.

**It turns only where the work is.** `TOLL` is per encounter, so cold code never
accumulates enough numerator to trip the gate. Prediction: the population shrinks
in hot namespaces and grows without limit in cold ones. `~/bin` holds 197 entries
and is hot; the 959 unreferenced store directories are cold and will still be
there next year, correctly.

**Reaching a verdict is not performing it.** `claude-plan` was dispositioned
`retire` -- one line, zero forfeited benefit, the easiest possible case, decided
in the time it took to read the file -- and it is still installed. One tool of
twenty has ever been retired here, and even that one has not actually gone.
**The gate is not the bottleneck; the action is.** So the checkable form of this
claim is not "is the ratio right" but "does the index hold a decided retirement
that has not been carried out", which is the second block `../retirement.py`
exits nonzero for.

That reframing is the claim's practical content. A theory of retirement that
produced better verdicts would change nothing at all in this population, because
the one verdict it already has is undone.

## Smallest instance

One row, from the check: `dispositioned retire, still installed: claude-plan`,
open since 2026-08-10.

## What would kill it

`FORECAST`'s own defeater, inherited whole: a domain where prediction is
calibrated. The ratchet's direction is entirely a function of the coefficient
being below 1, so a class of well-calibrated forecasts relaxes both gates at once
and the pressure disappears. It would also be killed the other way, by a
population where deletion is not cheaply reversible -- the asymmetry is only safe
because `PRUNE` inherits a near-zero reversal cost from version control, and in a
system without that, distrusting forecasts should make you delete *less*.
