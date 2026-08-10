# Mechanics -- verified facts about how packaging behaves here

One fact per file, each with the command and output that established it.
These lower the cost of the next packaging decision by removing a guess.

## What belongs here

- Behavior of the toolchain (`uv`, hatchling, `uv tool install`, pre-commit)
  that a packaging decision depends on, **verified by running it**.
- Migration hazards discovered the hard way.

## What does NOT belong here

- Contestable judgment -> `../criteria.kb/`. The split: a mechanic can be
  falsified by a command; a criterion can only be argued with.
- Facts already documented in `bukzor-tools`' own README ("Adding a tool"
  covers the workspace member shape and the meta-package script re-export).
  Duplicating upstream docs here means two things to keep true.

## Maintenance

Record the version or date something was verified against. A mechanic whose
tool has since changed is worse than no mechanic, and toolchain behavior in
this area is not stable.
