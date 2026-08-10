---
last-updated: 2026-08-10
---

# bukzor-packaging -- claim ledger

The formal account of `README.md`'s four standing questions. Thirty-one claims
in nine theories; the working notes stay in the collections above this file.

Read `questions.kb/` first if you want answers, `levels.kb/` first if you want
to know why the answers are shaped the way they are.

## The poset

Priors point up; a theory may use its priors' vocabulary and no one else's.

```
                        levels
                     (what can be seen,
                      at what price)
                       /          \
                  seams            cost
            (is it a cluster)   (is it worth it)
                 /    \          /    \    \
                /      \        /      \    genesis
        coherence      graduation       \  (should it exist
    (two copies of     (does it leave     \     at all)
     one fact)          dotfiles)          \      |
                \            |             /      |
                 \           |            /       |
                  +------ closure --------+       |
                   (what does building            |
                    decide by accident)           |
                            |                     |
                        questions                 |
                  (what we were asked,            |
                   twice, and the residue)        |
                            |                     |
                            +---- case-study -----+
                              (what happened when
                               the rules met this
                               pile of scripts)
```

Rules point up. `case-study.kb/` sits under everything: it holds the
measurements, so the theories above it can be read as rules rather than as
verdicts about sixteen particular scripts.

## What each theory holds, and what would end it

| theory | holds | defeated by |
|---|---|---|
| `levels` | four grades of observation -- name/shape, program, knowledge, audience -- ordered by definability | an audience predicate computable from file contents |
| `seams` | a cluster is a package only if no member is isolated in the reference graph; a second, looser relation says which failures a refactor could fix | a package worth shipping whose members share no code, now or ever |
| `cost` | *c*(*S*) = *F* + Σ*m*(*t*); the worth-testing set is a threshold, not a property | a per-package cost that does not fall when a workspace exists |
| `genesis` | build iff *b*/*c* > 1, rank by *b*/*c*, discount predicted use by ⅔; benefit is friction, error cost, or reuse | a tool worth building whose benefit is none of the three kinds |
| `coherence` | a derived key must be recomputed or checked; duplicated facts are resolved by search order, silently | a duplicated fact that provably cannot diverge |
| `graduation` | audience is necessary; knowledge or subcommands then suffice | a graduation that came out right while ignoring audience |
| `closure` | building closes questions without deciding them; a guard must name a reversal cost | an accidental closure reversed as cheaply as it was made |
| `questions` | the four standing questions, each stated as experienced and as well-posed | a question whose two forms coincide |
| `case-study` | the measurements: what the rules found in this particular pile of scripts, with the commands | nothing -- a record is not a conjecture; it can only stop being reproducible |

## The picture, on one page

Five rules, in the order a tool meets them. None of them mentions a tool name.

**One -- should it exist?** Build iff *b*/*c* > 1, and among competitors for one
budget build in decreasing *b*/*c*. The quotient and the difference agree on the
gate and disagree on the *order*, which is why the quotient is the instrument.
Predicted use is discounted by ⅔; ongoing use counts as observed. The numerator
is one of three kinds, summed, any one sufficient: **friction** (recurrence ×
per-invocation barrier), **error cost** (incidence × detection+repair+damage,
which earns a check rather than a command), **reuse** (P(needed again) ×
re-derivation minus recall, which is what justifies a tool used twice a year).

**Two -- do several tools form a package?** Only if no member is isolated in the
reference graph *G*. Adding artifact-incidence edges gives *G*⁺ and three
exhaustive verdicts: **seamed**, **latent** (separable but not separate -- the
shared artifact names the code to extract), **none** (no refactor makes this a
package). The gap between the two relations is where the useful findings live.

**Three -- should it leave the dotfiles repo?** `AUDIENCE ∧ (KNOWLEDGE ∨
SUBCOMMANDS)`. Audience is necessary and is not in the files, so every
graduation is a ruling and no check can stand in for it. A tool can deserve to
exist and deserve to stay.

**Four -- is it worth testing?** The question is malformed as usually asked.
"Untestable" names nothing; there is only a threshold *b*(*t*) > *c*(*t*), and
*c* is a property of the **site**, not the tool. Lowering the site cost
silently invalidates every past "not worth it" verdict, and the discount is
language-relative -- which is what decides a port versus a move.

**Five -- what does duplication cost?** A fact with two implementations has no
authoritative copy: which one a caller gets is a property of how the caller was
invoked. A duplicated fact has **three independent properties** -- *clone
fidelity* (fixed by committing), *provenance* (fixed by packaging), *resolution*
(fixed only by retiring the rest) -- and a check written against one stops
answering when another improves. A derived key stored anywhere decays under two
motions, and doing nothing about it silently selects "carry the staleness".

And one rule about the act of deciding: **building closes questions without
deciding them**, so a guard is earned exactly when reversing the closure costs
more than the action.

## What those rules found here

The instance, with the measurements in `case-study.kb/`:

- **The `claude-` prefix names no package.** Sixteen scripts split five ways:
  one seamed cluster, three latent, one dead, one relic, four unsettled.
- **Three for three.** Each latent seam predicted a refactor that had already
  been filed independently -- the strongest evidence that artifact incidence
  measures something real.
- **One cluster killed outright.** `claude-session-lifecycle` is pairwise
  disjoint on both relations; there is no structure there.
- **31 decided, 3 defaulted.** Of 53 store keys, 34 disagree with today's
  encoder: 31 from a migration that was priced and declined -- against a
  population nobody had counted -- and 3 from worktrees that moved, which
  nobody has priced.
- **A live hazard, found and fixed inside an hour.** The encoder that named
  those 53 directories was untracked, and the committed substitute implemented
  the *previous* encoding, so a fresh clone would have silently created empty
  stores. Tracked 2026-08-10.
- **One package shipped off this reasoning, same day.** `claude-code-slug`
  (`../bukzor-tools`, `aa7535b`): 26 differential cases and all 53 live paths
  agree with the bash it replaced, `--derived` byte-identical, no key moved.
  Implementations went 3 → 2 and stop there, because the survivor is another
  repo's deliberate vendoring. The estimate was accurate about the artifact and
  omitted the cutover, which is now a claim (`cost.kb/`).

## The measurement, current

```
$ bukzor-packaging.claims.kb/seams.py
SHIPPED claude-code-archeology: claude-jsonl-path, ... on PATH, not in ~/bin
SHIPPED claude-code-slug: claude-slug, claude-path on PATH, not in ~/bin
LATENT  claude-open-tasks: claude-open-tasks, claude-open-tasks-list ...
LATENT  claude-stream: claude-print-verbose, claude-s ...
--      retire: claude-plan
--      unsettled: claude-fork, claude-workspace-merge, claude-export,
                   claude-jsonl-summarize

$ bukzor-packaging.claims.kb/seams.py --cluster \
      claude-fork,claude-workspace-merge,claude-export
NONE    (given): ... share nothing with siblings          # exit 1

$ bukzor-packaging.claims.kb/coherence.py --derived
live relocated worktrees:     53
key matches today's encoder:  19
key disagrees:                34
  legacy encoding of it:      31  (declined migration)
  neither encoding of it:      3  (workdir moved since)

$ bukzor-packaging.claims.kb/coherence.py --shadow
claude-slug resolves to: ~/.local/bin/claude-slug  (installed in bukzor-tools)
git-localhost-store bypasses PATH via a symlink -> ~/.local/bin/claude-path
2 files implement the encoding independently               # exit 1
```

`--cluster` and `SHIPPED` exist for the same reason, in opposite directions: a
verdict that stops being reproducible when it is acted on is not evidence.
`claude-session-lifecycle` was killed on `NONE` and its members moved to
`unsettled`, so the index no longer carries the cluster -- pass the members
explicitly and the kill stays checkable. `claude-code-slug` was *built*, and its
members left `~/bin`, which made the reference graph read `NONE`. **Both
successes broke the check that recommended them.** The fix in both cases is to
key the verdict on the recorded decision rather than on the current directory
listing.

`coherence.py` exits nonzero. That is the state of the world, not a broken
check.

## Conjectures killed

The bar: an identification carries a carrier, operations, laws, a smallest
instance, and its own defeater. These failed it.

- **`status:` as a lifecycle** -- `speculative < proposed < accepted <
  shipped` with `rejected` absorbing. *Killed:* the schema permits every
  transition and nothing enforces an order, so there is no law to state.
  Naming it a chain-with-a-sink adds a word and no content.
- **The tool graph as a category, packages as functors** -- the reach.
  *Killed:* objects and arrows exist, but no composition law does any work and
  nothing is preserved between two categories anybody needs. It named a shape
  and proved nothing, which is exactly what the bar forbids.
- **A Galois connection between names and packages.** *Killed as a theory:*
  the abstraction map α has no adjoint worth exhibiting. *Survived reduced:*
  `PROXY` -- a predicate is decidable in the abstract iff it factors through
  α, which is the only content the conjecture had.
- **Cost as a submodular set function, greedy clustering near-optimal.**
  *Killed:* *m*(*t*) is not independent of *S* -- extracting a shared leaf
  changes it -- so submodularity fails on the data. And with 16 items the
  optimization is a table. *Survived reduced:* `SITE`'s two laws.
- **Graduation as three independent tests.** *Killed:* the kb asserted
  independence and sufficiency, then asserted AUDIENCE decides ties; both
  cannot hold. *Survived corrected:* `GRAD`, AUDIENCE necessary and the code
  tests jointly sufficient given it -- which fits every settled call including
  the one that discriminates them, `claude-s`. The tests are named rather than
  numbered because "3 decides" hid the contradiction that "AUDIENCE decides"
  makes obvious.

Two conjectures survived intact, and both earned their keep: **artifact
incidence** (`LATENT`, which found three refactors and killed one cluster) and
**the derived-key invariant** (`DERIVED`, whose check separated 31 decided
mismatches from 3 undecided ones -- a distinction no one could draw before it
ran).

## Compartmentalized away

- **What the tools actually do.** The ledger reasons about references and
  artifacts, never about what a renderer renders. Deliberate -- it is what
  makes the claims checkable -- but it means a genuinely bad design inside a
  well-seamed cluster is invisible here.
- **`bukzor/work-stuff`.** Authorship-gated in `scope.md`; untouched.
- **Whether `bukzor-tools` is the right home at all.** Assumed throughout.
- **Release mechanics** beyond the two hatchling probes.

## What each abstraction costs

- ***G* is textual reference, not calling.** Over-approximation: three of
  eight edges are comment mentions. So the *negative* verdicts are sound and
  the positive ones are weaker than they look -- `SEAMED` can rest on a
  comment. Only `claude-slug` currently rests on a real `exec`.
- ***G*⁺ is regex artifact markers.** A tool merely mentioning `.jsonl` gets
  the edge; a shared artifact nobody thought to name gets missed. A `NONE`
  verdict is therefore an invitation to name a missing artifact, not a proof.
- ***c* = *F* + Σ*m* hides a coupling term.** The meta-package re-declares
  every member's scripts, so *F* grows slowly with package count. Ignored;
  named in `SITE`'s defeater.
- **`closure` is called an operator on two laws, not three.** Monotone and
  inflationary are exhibited; idempotence is not. The word is doing more work
  than the evidence supports, and this line is the discount.
- **L2 versus L3 is a judgment.** Two readers could file the same claim in
  different theories. The filing rule in
  `bukzor-packaging.claims.kb/CLAUDE.md` is the tiebreak, not a proof.

## Scans

```sh
cd bukzor-packaging.claims.kb
grep -rH '^standing:' */*.md | sort -t: -k3      # who signed what
grep -rl 'standing: open' */*.md                  # nobody has yet
./seams.py --edges --artifacts                    # the two relations
./coherence.py --derived                          # the exposed population
./seams.py --twins                                # the drifting pair
```

Plus `bin/llm.claims-graph` from `Skill(llm-claims-kb)` -- it lints dangling
`why:` targets, cycles, and claims that never joined the graph.
