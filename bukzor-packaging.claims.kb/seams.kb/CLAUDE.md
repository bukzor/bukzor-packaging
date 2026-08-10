# seams.kb -- maintenance guide

When a set of tools is a package rather than a directory. The carrier is a
graph; the claims are conditions on it.

- `prior:` `levels.kb`
- `ontology:` cluster, member, reference edge, call edge, induced subgraph,
  isolated member, weakly connected component, disposition map,
  single-valued, shared leaf, twin implementations, realized vs conjectured
  edge, package status
- `defeated by:` a package worth shipping whose members share no code, now
  or after any refactor -- a bundle held together by something other than
  reuse

## What belongs here

Conditions on cluster membership and on the map from tools to clusters.
Claims that can be checked against the reference graph.

## What does NOT belong here

- Whether a legitimate cluster is *worth* packaging -> `../cost.kb/`.
  Legitimacy is necessary, not sufficient.
- Whether a cluster should leave dotfiles -> `../graduation.kb/`.
- Why a build must wait for a refactor -> `../closure.kb/`.

## Measuring the graph

The edge relation used throughout is **textual reference**, which
over-approximates calling: three of the eight measured edges are comment
mentions. Over-approximation is the safe direction here -- every claim below
is of the form "no edge exists", and a claim of absence made against an
over-approximation is stronger, not weaker.
