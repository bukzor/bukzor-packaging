---
label: LEVEL
standing: agent
---

# Observation Comes in Four Levels

A tool admits four grades of observation, each strictly more expensive
than the last and each answering questions the one below cannot:

| level | observation | cost | example |
|---|---|---|---|
| L0 | **name and shape** -- filename, line count, shebang, language | `ls`, `wc` | `claude-plan` is 1 line and has no shebang |
| L1 | **program** -- what it calls, reads, writes | grep, one read | `claude-path` execs `claude-slug` |
| L2 | **knowledge** -- which fact about something else it encodes | read and understand | the slug maps every non-alnum to exactly one `-` |
| L3 | **audience** -- who besides its author would want it | judgment about people | anyone with a sync-hostile filesystem wants `git-localhost-store` |

The levels are ordered by *definability*: L1 is definable from the file
contents, L2 from L1 plus knowing what upstream does, L3 from neither.
Each step up costs more and decides more.

The trade is the point. L0 claims are the most generic -- they apply to any
file tree, need no domain knowledge, and can be computed for all 16 scripts
in one command -- and they are nearly useless for the decisions this work
exists to make. L3 claims decide everything and generalize to nothing.

A claim in any other theory of this ledger should be locatable on this
table. When it isn't, either the claim is confused about what it observed,
or a level is missing.

## Smallest instance

`claude-open-tasks-list`: at L0 it is `212 lines, python3, claude- prefix`,
indistinguishable from `claude-jsonl-display` at `714 lines, python3,
claude- prefix`. At L1 they share nothing -- neither references the other,
nor any common third script. At L2 one encodes a git-behavior fact about
checkout and mtime, the other a rendering of a record format. The
observation that separates them is L1 and up; L0 groups them.

## What would kill it

A fifth level worth naming, or a demonstration that two of these collapse
-- if L2 turned out computable from L1 for the tools at hand, the middle of
the tower is decoration.
