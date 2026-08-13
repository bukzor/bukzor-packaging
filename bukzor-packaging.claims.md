---
label: LEDGER
standing: agent
last-updated: 2026-08-13
---

# bukzor-packaging -- claim ledger

The theory this repo exists to produce; `README.md`'s standing questions are
its instance-facing form, and the working notes stay in the collections above
this file. Coverage is graded against `requirements.md` -- what the job needs,
before what the files contain.

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
              /    |    \        /    |    \
             /     |     \      /     |     genesis
    composition  coherence  graduation     (should it exist
   (how two       (two copies (does it      at all)
    tools fit      of one      leave           |
    together)      fact)       dotfiles)       |
        |             \          |             |
        |              +- closure +            |
        |           (what does building        |
        |            decide by accident)       |
        |                   |                  |
        |               retirement ------------+
        |            (when should a tool
        |             stop existing)
        |                   |
        +--------------- questions
                  (what we were asked,
                   twice, and the residue)
                            |
                        case-study
                     (what happened when the
                      rules met this pile of
                      scripts)
```

Rules point up. `case-study.kb/` sits under everything: it holds the
measurements, so the theories above it can be read as rules rather than as
verdicts about sixteen particular scripts.

## What each theory holds, and what would end it

| theory | holds | defeated by |
|---|---|---|
| `levels` | four grades of observation -- name/shape, program, knowledge, audience -- ordered by definability | an audience predicate computable from file contents |
| `seams` | a cluster is a package only if no member is isolated in the reference graph; a second, looser relation says which failures a refactor could fix | a package worth shipping whose members share no code, now or ever |
| `cost` | *c*(*S*) = *F* + Σ*m*(*t*); the worth-testing set is a threshold, not a property; a dependent converts an edit into a migration | a per-package cost that does not fall when a workspace exists |
| `genesis` | build iff *b*/*c* > 1, rank by *b*/*c*, discount predicted use by ⅔ and inflate predicted cost threefold; benefit is friction, error cost, or reuse; the quotient ranks only named candidates | a tool worth building whose benefit is none of the three kinds |
| `composition` | tools are the arrows and formats the objects; streaming is a monoid homomorphism; a boundary cost is a cut; a discipline pays iff it makes a predicate checkable | a typed view that decides nothing the reference graph already decided |
| `coherence` | a derived key must be recomputed or checked; duplicated facts are resolved by search order, silently; packaging replaces location with declaration | a duplicated fact that provably cannot diverge |
| `graduation` | audience is necessary; knowledge or subcommands then suffice | a graduation that came out right while ignoring audience |
| `closure` | building closes questions without deciding them; a guard must name a reversal cost | an accidental closure reversed as cheaply as it was made |
| `retirement` | deleting is a candidate action priced by the same quotient; the toll is per encounter; a subsumed tool needs no estimate; the ledger's own claims are in the population | a maintenance cost charged by the calendar rather than by encounter |
| `questions` | the four standing questions, each stated as experienced and as well-posed | a question whose two forms coincide |
| `case-study` | the measurements: what the rules found in this particular pile of scripts, with the commands | nothing -- a record is not a conjecture; it can only stop being reproducible |

## The picture, on one page

One operation and seven rules, in the order a tool meets them. None mentions a
tool name.

**Zero -- what does packaging do?** To package is to **replace location with
declaration**: a loose file at a path becomes a versioned artifact,
first-match-on-PATH becomes a dependency a resolver honors, and deletion gains
a reach no `git rm` has -- an uninstall per environment instead of a pull per
clone. That is the operation every rule below gates. And its forward price:
**shipping to an audience mints future cutovers.** Once dependents exist, an
interface edit is a migration billed at the adoption count -- a recurring term
*F* + Σ*m* cannot see, growing with exactly the factor graduation selects for.
Here it is ≈ 0; see the domain of validity.

**One -- should it exist?** Build iff *b*/*c* > 1, and among competitors for one
budget build in decreasing *b*/*c*. The quotient and the difference agree on the
gate and disagree on the *order*, which is why the quotient is the instrument.
Predicted use is discounted by ⅔; ongoing use counts as observed. A predicted
*cost* is inflated by the reciprocal -- one correction per term, both pointing the
same way -- so an action justified entirely by forecast must clear 9:1. The numerator
is one of three kinds, summed, any one sufficient: **friction** (recurrence ×
per-invocation barrier), **error cost** (incidence × detection+repair+damage,
which earns a check rather than a command), **reuse** (P(needed again) ×
re-derivation minus recall, which is what justifies a tool used twice a year).
And the quotient ranks only **named** candidates: the rivals that route around
building -- upstream it, buy it, wait, write it down -- produce no artifact for
a disposition row to point at, so a verdict with no named rival is a race with
one runner.

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
The repair has a name -- rule Zero: packaging is the one mechanism that moves
provenance, resolution, and deletion at once.

**Six -- how do two tools fit together?** **Tools are the arrows, formats are the
objects**; `|` composes and `cat` is the identity. An effectful tool is
`unit → unit`, which is why a cluster of them can have no seam. A *latent* seam
is a composite that factors through an object nothing names, so extracting is
naming it. A filter streams when it is a **monoid homomorphism** on message
sequences; everything else is a fold, and a pipeline's latency is set by its
earliest fold -- its memory by the earliest unbounded-state stage, which dedup
proves is a different thing. Composition loses information **only at the joints**, so
`dec ∘ enc = id` per format buys correctness for every pipeline over it. And two
costs that look like one: *F* is a fixed charge per package and pulls toward one
package, while joint cost is a **cut** and pulls toward one process -- so cheap
serialization buys small tools, not big packages.

**Seven -- when should a tool stop existing?** Deleting is a candidate action, so
it is priced by the *same* quotient: delete iff *m*/*cb* > 1, numerator the
maintenance toll avoided, denominator the benefit forfeited. Nothing new was
needed -- rule One already ranged over actions and had only ever been pointed at
constructive ones, which is why the rule set could grow the population and never
shrink it. The toll is charged **per encounter**, not per unit time, so lines and
sweeps multiply and cold code is nearly free; the two ways to cut it are delete
and relocate. The benefit is **marginal**, so a tool subsumed by something that
already exists has a denominator of zero and needs no estimate -- while "this
should be a flag" argues subsumption by a tool nobody built, and deleting on it
removes capability. And the ⅔ discount cuts both ways: it makes building harder
*and* deleting easier, so distrusting forecasts is monotone pressure toward less
code. Both gates rank on one list, which is what "subtract, don't accrete" means
formally. And the rules range over **their own text**: a claim is an artifact with
a read cost and a marginal benefit, so the ledger prunes itself -- hardest at this
file, which is the hottest namespace it has.

And one rule about the act of deciding: **building closes questions without
deciding them**, so a guard is earned exactly when reversing the closure costs
more than the action.

One rule about adopting rules: **a house discipline earns its keep by what it
makes checkable** -- name the predicate it moves from judgment to check, or do
not adopt it.

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
- **One arrow in twenty.** Typing the population by calling convention finds
  exactly one filter, twelve tools that take a path per invocation, and six with
  no signature at all. The house discipline the theory presumes -- a thin `main`
  over a core named for the command -- currently holds **once**, with five more a
  rename away. So the composition laws are design rules for tools not yet
  written, and the gap between them and the tools that exist is priced: five
  renames, three extractions.
- **The census was mostly measuring itself, and it hid seven findings.** Recurrence
  had been named as a proxy and never counted. Counted over the whole corpus it
  reported **1 of 20** tools with no attested invocation, and a striking
  coincidence: the three least-invoked were exactly the three members of the
  cluster killed for having no seam. Cut the corpus at the day the study opened and
  both results dissolve -- the honest figure is **8 of 20**, and two of that
  "coincidental" three have attested invocations. The agreement was three tools
  being *handled by an analyst*. An over-approximation is only sound until an
  analyst arrives, and the repair is to stratify by a timestamp, which is the one
  thing the analyst cannot influence.
- **Auditing the last one deleted the evidence.** `claude-export` was the single
  name the uncut census flagged; checking whether it still worked meant running it,
  which took the count to zero of twenty. What the run bought was worth more than
  the count: the tool works, it makes a shell variable survive between `Bash()`
  calls, its audience is *agents*, and no `CLAUDE.md` mentions it. **Zero use was
  zero discoverability.** A count cannot tell an absent benefit from an unreachable
  audience, so the gate fired and the row closed the other way.
- **The gate was correcting one term and not the other.** ⅔ came off predicted
  benefit and nothing touched predicted cost, so the bar sat loosest for exactly
  the actions with the least evidence. Corrected, a purely speculative build must
  clear **9:1** -- and the correction is where YAGNI's fourth cost, *repair*, had
  been going nowhere.
- **The terms were on file, in the wrong file.** Four decisions have been made and
  the index recorded verdicts only; the estimates were sitting in `packages.kb/`
  the whole time ("call it an hour", plus two steps nobody budgeted). Transcribed
  into the index, where the rate could use them. But the recovered cost side has a
  number and the benefit side has no unit at all, so the decisions are degenerate
  anyway: **better filing does not produce a comparable benefit**, and that residue
  is not a filing problem.
- **One retirement in twenty, and it is undone.** `claude-plan` was dispositioned
  `retire` -- one line, zero forfeited benefit, the easiest case there is -- and
  is still installed. The gate is not the bottleneck; the action is.
- **One package shipped off this reasoning, same day.** `claude-code-slug`
  (`../bukzor-tools`, `aa7535b`): 26 differential cases and all 53 live paths
  agree with the bash it replaced, `--derived` byte-identical, no key moved.
  Implementations went 3 → 2 and stop there, because the survivor is another
  repo's deliberate vendoring. The estimate was accurate about the artifact and
  omitted the cutover, which is now a claim (`cost.kb/`).

## The measurement, current

```
$ bukzor-packaging.claims.kb/seams.py
PARTIAL claude-code-archeology: shipped, but claude-jsonl-path, ... still in ~/bin
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
claude-slug resolves to:   ~/.local/bin/claude-slug  (installed in bukzor-tools)
git-localhost-store calls: ENCODED="$(claude-path "$WORK_DIR")"  (line 33)
  resolved by:             PATH, unpinned
1 live implementation; 2 WARN, both staleness that converges on a pull  # exit 0

$ bukzor-packaging.claims.kb/composition.py --adapters
20 tools: 6 EFFECT, 1 FILTER, 12 ITEM, 1 UNKNOWN
1 names a core for the command; 5 name one a rename away    # exit 1

$ bukzor-packaging.claims.kb/retirement.py
population  20 tools on PATH; ~/bin holds 197
attested    281 session logs, cut at 2026-08-09 + ~/.bash_history
no invocation attested: 8 of 20
  claude-export, claude-inventory, claude-jsonl-path, claude-jsonl-summarize,
  claude-jsonl-to-log, claude-plan, claude-s, claude-search
dispositioned retire, still installed: claude-plan
settled decisions with no recorded terms: 0 of 4                # exit 1
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

`PARTIAL` is the correction to that fix. Keying on the record made the check
*trust* the record, and the record said "shipped" while five of archeology's
planned members were still sitting in `~/bin` -- so the verdict printed "not in
`~/bin`" about five files that were in `~/bin`. **Key the verdict on the
decision; measure the state anyway.** A check that reports a location it never
probed is the same defect as the retracted symlink claim, arrived at from the
opposite direction.

`--derived` and `composition.py` exit nonzero. That is the state of the world,
not a broken check. `--shadow` reaching **exit 0** is the one that changed, and
it changed by the encoder being packaged and its rivals retired -- not by the
predicate being relaxed. What survives are two warnings about *staleness*: one
checkout awaiting a push, one clone that has not seen a deletion. Both converge
on a pull, and telling them apart from a second implementation is the whole
content of `CHECKOUT`.

## Conjectures killed

The bar: an identification carries a carrier, operations, laws, a smallest
instance, and its own defeater. These failed it.

- **`status:` as a lifecycle** -- `speculative < proposed < accepted <
  shipped` with `rejected` absorbing. *Killed:* the schema permits every
  transition and nothing enforces an order, so there is no law to state.
  Naming it a chain-with-a-sink adds a word and no content.
- **The tool graph as a category, packages as functors** -- the reach.
  *Killed as stated:* with tools as objects, composition is the free category on
  the call graph, so "composes with" means "is reachable from", which `seams.py`
  already reports. **The conjecture was not too ambitious, it was transposed.**
  *Survived, both halves, in `composition.kb/`:* formats are the objects and
  tools the arrows (`PIPE`), which makes the composition law a type equation and
  explains `NONE`; a package is a star rather than a functor; and the functor
  that does real work is the shell, which is **lax**, with all its laxity at the
  serialization joints (`ROUNDTRIP`).
- **A Galois connection between names and packages.** *Killed as a theory:*
  the abstraction map α has no adjoint worth exhibiting. *Survived reduced:*
  `PROXY` -- a predicate is decidable in the abstract iff it factors through
  α, which is the only content the conjecture had.
- **Cost as a submodular set function, greedy clustering near-optimal.**
  *Killed in the wrong objective:* *m*(*t*) is not independent of *S* --
  extracting a shared leaf changes it -- so submodularity fails on the **build**
  cost. *Survived, in the objective that has it:* `BOUNDARY` -- a crossing
  arrow's joint cost depends on the pair and not on the partition, so the
  boundary term is a **cut** and submodular by construction. The second
  objection stands unrepaired: with 16 items the optimization is still a table,
  so the structure buys the fixed-charge discontinuity rather than an algorithm.
  *Survived reduced, as before:* `SITE`'s two laws.
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

## Domain of validity

The laws are stated generally and validated narrowly. This is the population
the numbers come from; outside it, re-derive before reusing them:

- **one author** -- no coordination or review cost appears in any term;
- **git-tracked** -- `PRUNE`'s aggression is safe only at near-zero reversal
  cost;
- **dependency-free scripts** -- `TOLL` charges per encounter because nothing
  here charges by the calendar;
- **a uv/hatchling Python site** -- `AMORTIZE`'s discount is language-relative
  and measured only there;
- **zero external dependents** -- `CONTRACT`'s recurring term is ≈ 0, so every
  verdict here is untested exactly where that term dominates.

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
- **`composition`'s laws range over a population of one.** With a single FILTER
  among twenty tools, `STREAM` and `ROUNDTRIP` describe a family that does not
  exist yet. Filed anyway, because a calling convention is cheapest to fix before
  it has callers -- but a law with one instance is a conjecture with good
  manners, and this line is the discount.
- **`retirement`'s quotient has no exchange rate.** *m* is an encounter count and
  *cb* is an invocation count; nothing here converts either into minutes, so the
  gate is a form awaiting units and is usable only where one term is *zero*. That
  is why `retirement.py` prints two columns instead of a ratio, and it is the
  same discount `cost.kb` carries about estimates generally. The rate is
  recoverable in principle from past decisions -- and three of the four made here
  recorded no terms, so nothing can be recovered from them either. That is now a
  failing check rather than a paragraph.
- **The use census sees nothing after 2026-08-09.** Both terms were polluted by
  this study in the same direction, which made the bias ambiguous rather than
  conservative, so agent log events from the day the census opened are now cut.
  The price is exact: the pre-study numbers became durable and the present became
  invisible. `~/.bash_history` is exempt because bash records no times.
- **The population is a PATH scan, so it mixes candidates with package output.**
  `claude-inventory` and `claude-search` are generated console scripts of a shipped
  package; their zeros mean "a shipped command goes uncalled", which is a finding
  about that package rather than a retirement candidate. Two of the twenty rows in
  every table here are that kind.
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
./composition.py --adapters                       # who is an arrow, and who has a core
./retirement.py --observed                        # what the logs attest about use
```

Plus `bin/llm-claims-kb-graph` from `Skill(llm-claims-kb)` -- it lints dangling
`why:` targets, cycles, and claims that never joined the graph.
