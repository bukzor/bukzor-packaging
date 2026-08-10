---
last-updated: 2026-08-10
---

# bukzor-packaging -- claim ledger

The formal account of `README.md`'s four standing questions. Twenty-two claims
in seven theories; the working notes stay in the collections above this file.

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
                 /    \          /    \
                /      \        /      \
        coherence      graduation       \
    (two copies of     (does it leave     \
     one fact)          dotfiles)          \
                \            |             /
                 \           |            /
                  +------ closure --------+
                   (what does building
                    decide by accident)
                            |
                        questions
                  (what we were asked,
                   twice, and the residue)
```

## What each theory holds, and what would end it

| theory | holds | defeated by |
|---|---|---|
| `levels` | four grades of observation -- name/shape, program, knowledge, audience -- ordered by definability | an audience predicate computable from file contents |
| `seams` | a cluster is a package only if no member is isolated in the reference graph; a second, looser relation says which failures a refactor could fix | a package worth shipping whose members share no code, now or ever |
| `cost` | *c*(*S*) = *F* + Σ*m*(*t*); the worth-testing set is a threshold, not a property | a per-package cost that does not fall when a workspace exists |
| `coherence` | a derived key must be recomputed or checked; duplicated facts are resolved by search order, silently | a duplicated fact that provably cannot diverge |
| `graduation` | audience is necessary; knowledge or subcommands then suffice | a graduation that came out right while ignoring audience |
| `closure` | building closes questions without deciding them; a guard must name a reversal cost | an accidental closure reversed as cheaply as it was made |
| `questions` | the four standing questions, each stated as experienced and as well-posed | a question whose two forms coincide |

## The picture, on one page

**One.** The `claude-` prefix is not a package. Sixteen scripts sharing it
split into one seamed cluster, three latent, one dead cluster, one relic, and
one unread script. A second `claude-code-tools` would be bundling, which is
what the `bukzor-tools` meta-package already does.

**Two.** Three of five candidate clusters are held together by a *shared
artifact* rather than shared code. Each such latent seam predicted a refactor
that had already been filed independently -- `stream-json` →
`extract-stream-json-invocation`, `todo-markdown` →
`dedup-open-tasks-implementations`, `session-jsonl` → the record model in
`display-renders-two-schemas`. Three for three.

**Three.** One cluster fails even the loose relation and should not be built:
`claude-session-lifecycle`'s three members share no artifact pairwise, and
`claude-workspace-merge`'s artifacts point out of the cluster into two others.
There is no structure there.

**Four.** "Untestable" names nothing. Testability is a relation between a tool
and a site, the site already moved, and the moved site is Python-only -- a
doctest costs one line, a bash test costs a hook plus a wrapper nobody has
written. That single asymmetry decides `claude-slug`: port it, don't move it.

**Five.** The duplication is not hypothetical. Of 53 live
`git-localhost-store` keys, 34 disagree with today's encoder, and the check
splits them into two different findings: **31** carry the pre-2026-07-05
encoding -- a migration that was written up, priced, and *declined*, which is a
decision and not a defect -- and **3** are keyed under paths their worktrees
have left, which is nobody's decision. The number the declined migration was
decided without is the 31. The encoding has four implementation sites and
three different mechanisms for choosing between them; packaging replaces all
three with a declared dependency. That is the actual argument, and it is
stronger than tidiness.

## The measurement, current

```
$ bukzor-packaging.claims.kb/seams.py
LATENT  claude-code-archeology: claude-uncolor share artifacts, not code
LATENT  claude-open-tasks: claude-open-tasks, claude-open-tasks-list ...
SEAMED  claude-slug
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
```

The second command is why `--cluster` exists. `claude-session-lifecycle` was
rejected on that verdict and its members moved to `unsettled`, so the index no
longer carries the cluster -- and a verdict that stops being reproducible when
it is acted on is not evidence. Pass the members explicitly and the kill stays
checkable.

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
