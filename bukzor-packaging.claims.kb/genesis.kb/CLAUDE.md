# genesis.kb -- maintenance guide

When a repeated action earns a command line interface of its own. This is the
first question in the whole subject and the last one to get a theory: the
others here take a set of tools as given and ask how to group, price, and
ship it. This one asks why any of them should exist.

- `prior:` `cost.kb`
- `ontology:` action, recurrence, activation energy, friction, invocation,
  observed use, predicted use, prediction discount, benefit kind, quotient,
  ranking under a budget, incidence, re-derivation cost, paged out
- `defeated by:` a tool that was clearly worth building whose benefit is none
  of the three kinds -- which would mean the decomposition is incomplete and
  every quotient here is computed against a benefit nobody can name

## What belongs here

Claims about whether an artifact should exist at all, and what its benefit is
made of. `../cost.kb/` gives the threshold and the denominator; this theory
supplies the numerator.

## The three benefit kinds are summed, not selected

`FRICTION`, `ERRORCOST` and `REUSE` are separate because they have different
proxies and different failure modes -- but a candidate clears the bar on the
*sum*, and any one of them can carry it alone. This matters in one direction
especially: a tool invoked twice a year scores near zero on friction and can
still be obviously worth building on `REUSE`. Reaching for the frequency
argument and finding it absent is not a verdict.

## What does NOT belong here

- Whether several tools that already exist form a package -> `../seams.kb/`.
- What the site costs -> `../cost.kb/`. This theory consumes the denominator
  and does not compute it.
- Whether the tool should leave dotfiles -> `../graduation.kb/`. Genesis is
  about existing; graduation is about distribution.

## Maintenance

- **Name the benefit kind before estimating.** An estimate that does not say
  which numerator it is estimating is a number with no units, and it is
  usually friction being assumed because friction is the easiest to picture.
- Recurrence is countable and nobody counts it. Where a proxy exists -- shell
  history, the Bash calls in `~/.claude/projects/*/*.jsonl` -- say so in the
  claim, even when the count has not been taken.
