---
label: DISCIPLINE
standing: agent
authority: >-
    bukzor, 2026-08-10, ruling out a shared schema package: "Ick! Absolutely
    not. Instead, we'll develop house conventions and tooling to bring the
    incremental costs toward zero."
why:
    - ../levels.kb/observation-comes-in-four-levels.md
    - ../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md
    - an-adapter-is-where-the-environment-leaks-in.md
---

# A House Discipline Earns Its Keep by What It Makes Checkable

Carrier: a candidate convention, and the predicates one wants to decide about a
tool. Law:

> A discipline adopted for *formal* reasons pays off exactly when it moves a
> predicate down the levels -- from judgment (L2/L3) to check (L1/L0). Name the
> predicate or do not adopt the convention. Its benefit is then priced like any
> other, by `../genesis.kb/`'s quotient.

This is the answer to the question that prompted this theory -- *are there
calling conventions or house disciplines that would make the structure more
regular?* -- and the answer has a filter attached, because the tempting reply is
a style guide.

| discipline | predicate it moves | to |
|---|---|---|
| data on stdin, configuration in flags | is this tool an arrow? | L0 -- read the invocation |
| a thin `main` over a core named for the command | what is the pure core? | L0 -- `grep` for the name |
| declare map-or-fold per tool | can this stream? | L1 -- split-and-compare test |
| a typed message stream | do these two compose? | L0 -- schema id equality |
| a round-trip test per schema | is the joint faithful? | L1 -- generated property test |
| `X-to-Y` command naming | what is the signature? | L0 -- the name itself |

Only the second row is measured today, at 1 of 20
(`an-adapter-is-where-the-environment-leaks-in.md`), which is the reason to
write the list down before the tools rather than after.

## The last row has a cost, and it is a real one

`../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md` says a name
narrows the candidates and never decides. An `X-to-Y` naming discipline makes the
name decide -- that is the point of it. The two do not contradict, and the
distinction is worth being precise about: that claim is about names as
**found**, which are descriptive and therefore evidence; this is about names as
**contracts**, which are prescriptive and therefore checkable. A discipline
converts the second into the first by fiat, and it holds only as far as the check
that enforces it. Adopt the naming without the check and the claim upstream is
simply true again. That file now carries the qualification.

## What this rules out, and why

A shared schema package -- one distribution everything imports its message types
from -- was proposed here and rejected outright. The reasoning agrees with the
ruling on three grounds, and it is worth keeping because the proposal is the
obvious move:

- **The registry already exists and is not a package.** A capnp schema carries a
  64-bit id, unique by construction. Uniqueness is what a central registry is
  *for*; buying a package to get it is paying twice.
- **It centralizes the wrong thing.** One shared distribution charges every
  member lockstep upgrades, gives the fan-in node no owner, and makes the
  release cadence of the slowest schema everyone's release cadence.
- **It violates this ledger's own cost law.** `../cost.kb/cost-splits-into-site-and-item.md`
  says lower *F*, do not cluster to amortize it. A schema package is clustering
  to amortize *F*, proposed in the same directory that says not to.

The tooling that replaces it is the fifth row of the table: **schema-evolution
lint in CI**, run against the previous release's schema. That is what actually
prevents the failure a registry was imagined to prevent, and it is per-package,
which is the point.

## What would kill it

A convention plainly worth adopting that makes nothing checkable -- consistent
flag spellings, a help-text shape, error messages that name the file first.
Those are real, and they are priced elsewhere: their benefit is
`../genesis.kb/friction-is-paid-per-invocation.md`, paid in human recall rather
than in decidability. So this criterion is a filter for the *formal* case, not a
theory of conventions. If the disciplines that end up mattering here are mostly
the friction kind, this file is a niche instrument and `genesis.kb` was the whole
story.
