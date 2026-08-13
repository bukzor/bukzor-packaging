---
label: CONTRACT
standing: agent
why:
    - an-estimate-omits-the-cutover.md
    - ../levels.kb/audience-is-not-in-the-files.md
---

# A Dependent Converts an Edit into a Migration

`CUTOVER` prices the migration you pay to replace something adopted. This is
its forward image: **shipping to an audience mints future cutovers.** Once
dependents exist, an interface change stops being an edit and becomes a
migration billed at the adoption count, so a package carries a recurring term
the site/item split cannot see:

> *c*<sub>contract</sub> ≈ dependents × interface change rate ×
> per-dependent migration cost, paid for the life of the contract.

Three consequences:

- **The term grows with exactly what graduation selects for.** AUDIENCE is the
  necessary conjunct for shipping, and it is this term's first factor -- so the
  ledger as previously stated understated packaging's cost most where
  graduation most recommends it.
- **Versioning is how the term is billed, not avoided.** A version number is a
  declared boundary at which the bill comes due; compatibility promises and
  deprecation windows buy down the *rate* factor. None of that machinery has
  any other purpose.
- **In this population the term is ≈ 0** -- an audience of one, dependents
  enumerable by hand -- which is a scope condition on every verdict here, not a
  refutation. Every law in this ledger is untested exactly where this term
  dominates.

## Smallest instance

Already realized, in-corpus, before the claim existed: the store-key encoding.
The 53 store directories are data-dependents of the encoder, and the 2026-07
encoding change was an interface edit whose bill arrived as a migration priced
over 31 keys -- and declined, the staleness carried on purpose
(`../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md`, sibling not
prior). The edit did not stay an edit; it forced a priced decision over a
dependent population. Same shape at smaller scale: deleting `claude-path`
required install-before-delete sequencing because hooks in roughly fifty
repositories depend on the name (`an-estimate-omits-the-cutover.md`).

## What would kill it

A change rate of zero, or a migration cost of zero. A frozen interface --
`claude-slug`'s encoding is pinned to upstream's behavior and is the best local
approximation -- zeroes the rate factor; mechanized migrations (codemods, a
resolver that rewrites callers) zero the per-dependent factor. Dependents
pinned forever do *not* kill it: a lockfile that never upgrades pays no
migration and forfeits every fix instead, which moves the term rather than
removing it.
