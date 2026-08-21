---
last-updated: 2026-08-13
---

# Requirements -- what the theory's job needs

The job: a **corpus-independent theory of how and why ad-hoc work becomes
packages, sound enough that an agent could run it against any population and
act on its verdicts without re-deriving them.** This file states what a theory
doing that job must cover and how far this one gets. Grade coverage here
before auditing contents: an audit finds defects in claims that exist; only a
requirements list can find the term that is missing entirely
(`docs/dev/formalization.claims.kb/state-the-job-before-distilling-the-corpus.md`).

The list is a judgment, not a derivation. Ratified by bukzor; statuses are the
agent's, as of the `last-updated` date.

## R1 -- the semantics of packaging

State what the operation *does*: the invariants it buys (provenance declared,
resolution unique, deletion propagates) and the obligations it creates (a
published package is a contract -- compatibility, dependents' upgrade costs).
**Status: met.** Rule Zero in the entry point; `DECLARE` (coherence.kb)
states the invariants as one law, `CONTRACT` (cost.kb) prices the obligation
-- dependents × change rate × per-dependent migration -- and the domain of
validity flags that the term is ≈ 0 in this population, so the law is
untested exactly where it dominates.

## R2 -- a decision procedure that runs anywhere

The rules and their instruments must take the population as an input.
**Status: open.** The entry point's rules prose is close; every instrument in
`bukzor-packaging.claims.kb/` hardwires the `claude-*` prefix (`seams.py:89`,
`composition.py:67`, `retirement.py:82`, `coherence.py:124`) -- population
selection by name prefix, the move `criteria.kb/seams-over-name-prefixes.md`
exists to forbid.

## R3 -- a priced alternative space

Packaging is one action among vendor, buy, upstream, leave in place, delete;
a theory that cannot express an alternative biases verdicts toward the
actions it can. **Status: largely met.** `RIVALS` (genesis.kb) makes the
candidate set authored and names the router-arounds -- upstream, buy, wait,
write it down. Residual: no disposition has yet been re-decided against the
enlarged set.

## R4 -- commensurable units and a live calibration loop

The gates' coefficients (⅔ off predicted benefit -- `FORECAST`; 3× predicted
cost -- `INFLATE`; jointly 9:1 for forecast-only actions) must be movable by
recorded outcomes: terms at decision time (`TERMS`), realized terms appended
beside them, a rate elicited from the pairs (`ELICIT`). **Status: wired but
nearly empty.** One scored cost forecast exists (realized/forecast ≈ 1.2-1.5,
a sample of one, biased easy); the benefit side had no unit until the ruling
below (`dispositions.md:64` predates it), so every settled decision is
degenerate and no coefficient has ever moved. Prior art for the unit, bukzor-authored and in
use: `Skill(llm-subtask)`'s `cost-benefit-sweh` schema
(`~/.claude/skills/llm-subtask/jsonschema/todo.jsonschema.yaml:70`) prices
both sides in SWE-hours (1 SWEh ≈ $100), with per-estimate rationale and
confidence bands, ranked WSJF -- the same order `QUOTIENT` argues. Ruled by
bukzor 2026-08-13: SWEh adopted. Records keep the schema's universal 2-week
rate; an optional `horizon` sub-attribute on the estimate object (ISO-8601
durations, default P2W -- machine-parseable by bukzor's requirement) lets a
lumpy benefit be stated over its natural window instead of flattened into a
constant rate, with the calibration loop as backstop for a wrong shape. The
gate carries the horizon instead: a payback bound, *c* / benefit-2w ≤ N
periods, *c* from `TERMS` re-denominated in SWEh (`timebox` is a stop-loss,
not the gate's cost). N is the one number still open; proposed 26 (one
year), `FORECAST`'s discount self-regulating the long bound. Rivals priced,
per the theory's own `RIVALS`: bare minutes, the incumbent
(`claims.kb/bukzor-packaging.claims.kb/cost.kb/CLAUDE.md:31` -- "Units are minutes,
and they are guesses"), lose on machinery -- no estimate object, no
confidence bands, no dollar leg -- not on the number, a fixed 60×
conversion; a bespoke schema loses on re-derivation for no gain.

## R5 -- stated scope

The population the theory claims to govern, stated once, globally, with what
changes outside it. **Status: met.** The entry point's "Domain of validity"
section: one author, git-tracked, dependency-free scripts, a uv/hatchling
site, zero external dependents.

## R6 -- scoreable predictions

The theory must sometimes overrule intuition, and the overrulings must be
scored. **Status: open.** No recorded case of the theory overruling
intuition, so its discriminating power is untested. Cheapest test on file:
`QCOMPOSE` names an action-log analysis nobody has run.

## Order of work

R4's unit was ruled 2026-08-13 (see above); application to the ledger is in
flight, with N the one open number. Next is R2, still gated on bukzor: it
reworks the `claude-*` instruments bukzor de-emphasized mid-review --
confirm before starting. R4 otherwise accumulates as completed actions append
realized terms; R6 accumulates out of R4's records rather than needing work
of its own. R1, R5, and most of R3 were met 2026-08-13 (`f09c359..59f2395`).
