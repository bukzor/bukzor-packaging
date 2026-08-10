# Candidate packages

One file per package, existing or proposed. Frontmatter per
`../packages.jsonschema.yaml`.

## What belongs here

A cluster someone could build: its members, the seam that holds them
together, its dependencies on other candidates, and what it costs.

Every entry must answer: **what would a member import from its siblings?**
If the answer is "nothing", the entry is a directory, not a package, and
belongs in `../dispositions.md` as unsettled instead.

## What does NOT belong here

- The work required to make a bad seam good -> `../refactors.kb/`. An
  entry here may cite a refactor as a precondition; it shouldn't contain
  the refactor's argument.
- Per-tool fate for tools no candidate claims -> `../dispositions.md`.

## Maintenance

- Members are listed with a path and a line count, so a later reader can
  see the shape without opening anything.
- `status: shipped` entries are kept, not deleted. They're the record of
  which seam won and what the move actually cost.
- When a member moves between candidates, fix `../dispositions.md` in the
  same edit.
