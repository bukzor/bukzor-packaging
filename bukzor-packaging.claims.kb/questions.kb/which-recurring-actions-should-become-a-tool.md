---
label: QCOMPOSE
standing: agent
why:
    - ../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md
    - ../levels.kb/observation-comes-in-four-levels.md
    - ../genesis.kb/a-tool-is-worth-building-when-benefit-over-cost-exceeds-one.md
    - ../genesis.kb/friction-is-paid-per-invocation.md
---

# Which Recurring Actions Should Become a Tool?

**As experienced** (bukzor, 2026-08-09): *"as I work, is there any 'clustering
of actions' that would be well served by being **com**posed into a new
cli/tool/tool-suite? (more for me, less for you, but i'd be delighted if i
could get claude-code to do this on the regular)"*

**Well-posed:** in the log of executed commands, is there a frequent
contiguous subsequence whose intermediate outputs are consumed only within the
subsequence?

**What the difference reveals, and it is the biggest gap in this ledger:**
every other question here ranges over tools that *exist*. This one ranges
over tools that don't. Its carrier is a **log of actions**, not a file tree --
so `ls` does not enumerate the population, `dispositions.md` cannot index it,
and *G* is undefined on it. The ledger's apparatus does not apply as built.

**It is two questions, and only one of them is open.** *Whether* a candidate
earns a tool is settled by `../genesis.kb/`: the quotient gate, the ⅓ discount
on predicted use, and the three benefit kinds it decomposes into. *Which*
candidates exist is a discovery problem over the log, and that is the part
nothing here answers.

An earlier version of this file said the ledger did not answer the question at
all. That was true when it was written and is the reason `genesis.kb` exists:
the decision rule was missing, and it was missing because this file mistook a
missing *measurement* for a missing *rule*. A rule was available without the
measurement, and the measurement is still not taken.

## The structure transfers with the carrier swapped

The seam law is not about files. Restated over actions:

- vertices: commands actually run
- edges: a data-flow edge *c* → *d* when *d* consumes what *c* produced (a
  pipe, a file written then read, a variable)
- a **candidate composed tool** is a frequent contiguous subsequence whose
  induced subgraph is connected *and whose outputs are internal* -- the
  boundary crossing is what makes it a tool rather than a habit

Note the extra condition. Over files, connectivity was enough
(`../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md`); over
actions it is not, because any two commands run in sequence in one shell share
a working directory. Frequency does the triage, internality does the deciding
-- the same triage-versus-decide split as
`../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md`, one carrier
over.

## The log already exists, and so does the reader

`~/.claude/projects/*/*.jsonl` records every `Bash` tool call of every
session, with its command string and its result. That is the log, unsampled,
going back months. And `claude_code_archeology` -- shipped, doctested, the
first graduation this kb produced -- is exactly the library that parses it.

So the answer to the parenthetical wish is: **yes, this is mechanizable, with
the tool that just shipped.** A first cut is a co-occurrence count over
command heads within a session window, ranked by frequency × (1 − boundary
crossings). Nothing about it needs new infrastructure.

That is a pleasing loop worth naming: the first product of the packaging
question is the instrument for its unanswered fourth part.

## Residue -- the discovery half

- Nobody has run the analysis. Every word above about what it would find is a
  conjecture with no exhibit, which by this ledger's own bar
  (`a citation is not an exhibit`) means this claim earns no more than
  `agent` standing.
- The same unrun analysis is the missing proxy for
  `../genesis.kb/friction-is-paid-per-invocation.md`, whose numerator is
  recurrence × barrier. So one measurement settles the discovery half of this
  question *and* grounds every friction estimate in the kb. It is the highest
  quotient unbuilt thing named anywhere here, by its own rule.
- The internality condition is guessed, not validated. Plausible failure: the
  strongest signal is a *discontiguous* pattern -- a command run at the start
  of every session and another at the end -- which the contiguity requirement
  discards.
- The composed-tool candidates it produces would then re-enter this ledger at
  `../seams.kb/`, and it is not obvious that a cluster of *actions* satisfies
  the same promotion gate as a cluster of *tools*.
