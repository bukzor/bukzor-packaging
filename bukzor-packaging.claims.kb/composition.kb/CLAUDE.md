# composition.kb -- maintenance guide

How two tools fit together mechanically, and what a calling convention buys.
This theory exists because the first attempt to formalize the kb got the
category upside down: it looked for composition *between tools as objects*,
found none, and reported "tools don't compose" -- which is false three ways
(`exec`, call, pipe). Tools are the arrows.

- `prior:` `levels.kb`, `seams.kb`, `cost.kb`
- `ontology:` stream, format, filter, fold, pipe, joint, serialization
  boundary, round trip, retraction, monoid homomorphism, prefix
  monotonicity, fusion, adapter, pure core, discipline, cut
- `defeated by:` a typed view that decides nothing the reference graph did not
  already decide. This theory is only worth its directory if arrow-typing
  changes a verdict *G* and *G*⁺ leave open; where it merely restates
  reachability, `seams.kb` already had it and this is decoration

## What belongs here

Claims about the *shape* of a tool's interface and what that shape implies for
grouping, testing, or cost. A claim here should be statable without naming any
tool, and checkable by looking at how tools take their input.

## What does NOT belong here

- Whether a given cluster is a package -> `../seams.kb/`. This theory says what
  composability means; that one says when a cluster is legitimate.
- What a boundary costs in hours -> `../cost.kb/`. `BOUNDARY` here says the
  cost is a *cut*; the numbers going into it are upstream.
- Two copies of one fact -> `../coherence.kb/`. Sibling, not prior: when two
  sides must *agree on a fact* rather than pass data, no serialization
  discipline helps and this theory has nothing to say.

## Maintenance

- **A discipline claim must name what it makes checkable.** "This convention is
  nicer" is `genesis.kb`'s FRICTION, priced as benefit like anything else. A
  claim belongs *here* only when the convention moves a predicate down the
  levels -- from judgment to check. If you cannot say which predicate, it is
  not this theory's business.
- **State laws for the discipline you have, not the one you want.**
  `composition.py --adapters` reports 1 of 20 tools naming a core for its
  command, with 5 a rename away. A law written as though the convention already
  held would be a house style guide wearing a theorem's clothes.
- The capnproto direction is the reason several of these laws are worth stating
  before the tools exist: a typed message stream makes the homomorphism law
  *statable*, which is not true of byte streams. Claims that depend on it say
  so, and say what they degrade to without it.
