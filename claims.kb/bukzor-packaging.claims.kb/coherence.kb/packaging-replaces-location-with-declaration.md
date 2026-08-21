---
label: DECLARE
standing: agent
why:
    - two-live-implementations-are-resolved-by-search-order.md
    - a-deletion-is-scoped-to-a-checkout.md
verify: ../coherence.py --shadow
---

# Packaging Replaces Location with Declaration

Every coherence defect in this theory is resolved by an accident of location
-- search order, a sibling path, whichever clone you are standing in. **To
package is to replace each locational accident with a declaration, and it is
the only mechanism on file that moves all three properties at once:**

| property | location decides it by | a package decides it by |
|---|---|---|
| provenance | a loose file at a path | a versioned artifact |
| resolution | first match in search order | a dependency the resolver honors |
| deletion | one checkout at a time, per pull | an uninstall, per environment |

The rows are not new: the first two are `SHADOW`'s three-properties table, the
third is `CHECKOUT`'s defeater ("packaging is exactly that mechanism"). What is
new is stating them as one law about what the operation *does*. The declined
alternative was leaving it distributed -- but every theory upstream prices
*when* packaging is worth doing while nothing said what it buys, so "why
package" lived in two defeater sections and an aside, and each new coherence
claim re-derived packaging's role in its own margin.

Two consequences:

- **Packaging's benefit in any quotient is the coherence cost retired** --
  measured drift and defaulted decisions, not tidiness. A cluster with no
  coherence defect and no audience has no packaging benefit to claim.
- **The law gives the gate its object.** Downstream, graduation asks *whether*
  to perform this operation; this file is what "this operation" refers to.

## Smallest instance

The store-key encoder, one day, all three rows exercised separately:
committing the untracked file fixed fidelity and was not packaging; packaging
fixed provenance and most of resolution; and the PEP 723 header completed a
retirement that no `git rm` could reach -- the vendored copy in another repo
(`two-live-implementations-are-resolved-by-search-order.md`). Meanwhile the
deletion performed *without* packaging left a LEGACY implementation alive in a
second clone (`a-deletion-is-scoped-to-a-checkout.md`).

## What would kill it

A second mechanism that moves all three properties -- a Nix-style store, or a
dotfiles manager with a manifest that pins content by hash and propagates
deletions. Then packaging is one member of a family and this claim names the
family's job rather than the package's. That would demote the claim, not
embarrass it: the law is about what coherence requires, and today packaging is
the only thing on this machine that supplies it.
