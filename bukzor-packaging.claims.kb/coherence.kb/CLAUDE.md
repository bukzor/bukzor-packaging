# coherence.kb -- maintenance guide

What happens to knowledge that is written down twice, or written down once
and then depended upon. This theory is why the packaging question is not
merely tidiness: the duplication is already producing wrong answers.

- `prior:` `levels.kb`, `seams.kb`, `cost.kb`
- `ontology:` derived key, deriving function, recompute, check, stale key,
  drift generation, live implementation, search order, shadowing,
  silent divergence, declaration, packaging (as the mechanism that declares)
- `defeated by:` a duplicated fact that provably cannot diverge -- one
  generated from the other at build time, or asserted equal by a test

## What belongs here

Claims about a fact having more than one home in the system, or one home and
a dependent copy on disk. Each should come with a measurement of how far
apart the copies already are.

## What does NOT belong here

- Whether the tools holding the copies form a package -> `../seams.kb/`.
  This theory says the copies are a defect; it does not say who should own
  the merged version.
- What the merge costs -> `../cost.kb/`.

## Maintenance

- **Measure the divergence, don't assert the risk.** "These could drift" is
  cheap and unfalsifiable. `coherence.py` reports how many have.
- A claim here is worthless without a re-runnable check. If a check cannot
  be written, the claim belongs in `../seams.kb/` as a structural
  observation instead.
