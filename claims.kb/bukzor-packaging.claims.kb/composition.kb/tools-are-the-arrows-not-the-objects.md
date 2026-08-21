---
label: PIPE
standing: agent
why:
    - ../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md
    - ../levels.kb/observation-comes-in-four-levels.md
verify: ../composition.py --adapters
---

# Tools Are the Arrows, Not the Objects

Carrier: the data formats a tool can read or write -- `jsonl` session records,
a path, a slug, ANSI text, a capnp message stream. Operations: a tool is an
arrow between two of them, `|` is composition, `cat` is the identity. Law:

> **Two tools compose exactly when the writer's output format is the reader's
> input format.** Composition is associative (`(a|b)|c` and `a|(b|c)` are the
> same function of a complete input stream) and `cat` is a two-sided unit.

The first formalization of this kb conjectured a category with **tools as
objects** and something like "calls" as arrows, found the laws vacuous, and
concluded that tools do not compose. Both halves were wrong, and the diagnosis
is worth keeping because it is a general trap: the conjecture was not too
ambitious, it was *transposed*.

## The three informal modes, sorted

| mode | example | what it is |
|---|---|---|
| pipe | `seq 999 \| a \| b \| c` | this category -- the informative one |
| call | any script invoking another | the free category on the call graph |
| exec | `time sleep 3` | not an arrow: an operator `Command -> Command` |

The middle row is what killed the original conjecture, and it deserved to die.
The free category on a graph has exactly one arrow per path, so "does *a*
compose with *b*" reduces to "is *b* reachable from *a*" -- true of any graph
whatsoever, and already reported by `seams.py --edges`. **A structure that
restates a relation you already have is worth nothing**; that is not a slur on
category theory, it is the difference between the two orientations.

The third row is genuinely higher-order and genuinely useful to name: `time`,
`env`, `nohup`, `uv run --script` take a command and return a command. They
never appear as arrows because their domain is not a data format, which is
why they are invisible to every packaging question here -- nothing imports
from them and they import from nothing.

## Smallest instance

`composition.py --adapters` types the population by how it takes input, and
the answer is stark: of 20 `claude-*` commands, **one is a FILTER**
(`claude-jsonl-display`, a `jsonl`-stream to ANSI-text arrow), 12 are ITEM
(they take a path per invocation), and 6 are EFFECT.

An EFFECT tool is an arrow `unit -> unit`. Every such arrow composes with every
other, and the composite is uninformative -- which is the precise reason
`seams.py` returns `NONE` for clusters made of them. **The verdict was right
and the explanation was missing:** those clusters have no seam because their
tools have no types, not because nobody factored them well.

## Consequences worth having

- **`NONE` is explained, not just observed.** A cluster of `unit -> unit`
  arrows cannot exhibit a seam, so the verdict is structural rather than a
  judgment about effort.
- **A package is a star.** Its members share one object (the imported module's
  types), and every member is an arrow touching it -- which is
  `../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md` read as a
  connectivity condition on this category rather than on the reference graph.
- **The census is a to-do list.** Twelve ITEM tools are twelve tools that
  cannot appear in a pipeline. Each is one calling convention away from being
  an arrow, which is `an-adapter-is-where-the-environment-leaks-in.md`.

## What would kill it

A verdict this typing gets right that *G* gets wrong -- or, killing it, the
absence of one. So far it has produced two: the explanation of `NONE`, and the
FILTER count. If the typed view never contradicts nor refines the reference
graph on this population, `seams.kb` had it all along and this theory is
decoration (`CLAUDE.md`'s `defeated by:`).
