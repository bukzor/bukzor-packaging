---
label: TOLL
standing: user
authority: >-
    bukzor 2026-08-11, both halves: "every line of code has a maintenance
    cost"; "anything we _can_ delete is a win for maintenance costs, which has
    to be paid whenever the code has to be scanned/amended"
why:
    - ../genesis.kb/friction-is-paid-per-invocation.md
verify: ../retirement.py --observed
---

# Maintenance Cost Is Paid Per Encounter

The numerator of a deletion, and the mirror of `FRICTION`.

Carrier: a body of code sitting in a namespace. An **encounter** is any occasion
the code has to be scanned or amended -- a grep that sweeps it, a listing that
prints it, a rename that must consider it, a reader deciding it is irrelevant.
Law:

> *m*(*t*) = encounters × Δ(scan + amend burden)

`FRICTION` charges a barrier per invocation to whoever *uses* a tool; this
charges a barrier per encounter to whoever *maintains* it. Same shape, different
payer, and that is why the two terms of a retirement are commensurable at all.

## The two halves of the authority are not in tension

"Every line has a cost" is a stock measure and "paid whenever scanned" is a
flow, so they look like a correction of each other. They multiply: the charge is
lines × sweeps, which is what a grep actually pays. Two consequences follow
directly, and they are the only two moves available:

- **Shrink it** -- fewer lines per encounter. Deletion is the limit case.
- **Move it out of the path** -- fewer encounters per line, with the lines
  intact. That is what `../graduation.kb/` buys and it is easy to miss, because
  the code still exists and the toll still falls.

## The rule does not sweep

An unencountered file's toll is nearly zero, so *"anything we can delete is a
win"* is false for cold code -- the win is real but it rounds to nothing. This
is a consequence of the second half of the authority defeating the first, and it
is worth stating because it predicts where the population shrinks and where it
does not.

**Smallest instance, a matched pair.** `claude-plan` is one line, in `~/bin`
alongside 196 other entries -- the directory that answers every `claude-<TAB>`
and every `ls ~/bin`, which is this machine's discovery surface for the whole
family. The 959 unreferenced store directories
(`../case-study.kb/the-store-key-encoding-has-drifted-twice.md`) are orders of
magnitude more bytes, under content-addressed names nobody lists or greps. Same
deadness; the one-line file is the expensive one. **The discriminator is
namespace heat, not size** -- which is also the mechanism behind "rename
aggressively, `ls` is discovery".

## What this makes of a partial ship

`PARTIAL` reads as bookkeeping pedantry until the toll is per encounter. Five of
`claude-code-archeology`'s planned members shipped as a package and stayed in
`~/bin` anyway, so the packaging cost was paid in full and the discovery refund
-- the entire point of the relocation -- was never collected. The namespace did
not shrink, so neither did the toll.

## What would kill it

A charge that arrives on the calendar instead of on an encounter: a vendored
dependency somebody else upgrades, a CVE feed, an audit that reads every file
whether or not anyone was working there. Cold code is expensive under that
regime and the pair above inverts. Nothing in this population has such a charge
today -- the tools are dependency-free scripts -- which is why the claim holds
here and should be re-checked the moment one of them grows a lockfile.
