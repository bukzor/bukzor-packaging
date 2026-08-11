# retirement.kb -- maintenance guide

When a tool that exists should stop existing. `../genesis.kb/` asks whether to
build, `../graduation.kb/` whether to ship; this asks whether to delete, and it
is the last theory here because the whole rest of the ledger could not answer
it.

- `prior:` `genesis.kb`, `coherence.kb`, `graduation.kb`, `closure.kb`
- `ontology:` maintenance toll, encounter (a scan or an amendment), namespace,
  discovery surface, hot and cold code, subsumption, dominance, marginal
  benefit, deletion as a candidate action, ratchet, attested use, disposition
  slippage
- `defeated by:` a maintenance cost charged by the calendar rather than by
  encounter -- a dependency somebody else upgrades, an audit that happens
  whether or not anyone reads the file. Cold code would then be expensive, and
  `TOLL`'s "the rule does not sweep" is exactly backwards

## Why this theory exists

Before it, **the rule set was monotone.** Genesis creates, seams cluster,
graduation promotes, coherence merges, closure records -- every rule mapped the
population to a superset or left it fixed, so the only fixed point was every
tool forever. The index carried one `retire` disposition, reached by hand, with
no rule behind it.

The repair is smaller than it looked. `QUOTIENT` ranges over *candidate
actions*, and deleting is one; nothing was missing but the habit of pointing the
instrument backwards. So `PRUNE` is an application of a rule the ledger already
had, and the claims here are mostly about the two terms it needs.

## What belongs here

Claims about removing something that works, and about what the removal costs and
saves. The distinguishing test against `../coherence.kb/`: that theory says two
copies of a fact are a defect and does not say which copy dies; this one prices
the death.

## What does NOT belong here

- Whether a tool should have been built -> `../genesis.kb/`. Retirement is
  genesis re-evaluated later, not a different gate, and re-arguing the original
  build belongs upstream.
- Whether the *code* should move rather than go -> `../graduation.kb/`.
  Relocation and deletion are the two ways to cut the toll, and only one of
  them forfeits a benefit.
- The reversal cost of a destructive act -> `../closure.kb/`. `GUARD` is what
  makes aggressive deletion safe here, and it is cited rather than restated.

## Maintenance

- **Name which term the argument is about.** Nearly every dispute about a
  deletion is really about the denominator -- somebody has a use in mind and has
  not said it. "This is dead code" asserts the numerator and settles nothing.
- **A count of uses cannot decide a subsumption.** The marginal benefit of a
  subsumed tool is zero at any invocation count, so the histogram and the
  reference graph answer different questions. Do not let `../retirement.py`'s
  table stand in for `SUBSUME`.
- **Measure the state, not just the decision.** The index records verdicts and
  the filesystem records facts; `claude-plan` has been dispositioned `retire`
  and installed at the same time since 2026-08-10. This is the same failure
  `SHIPPED` had before `PARTIAL` corrected it.
