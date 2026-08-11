---
label: CASEUSE
standing: bare
why:
    - ../retirement.kb/deletion-is-a-candidate-action-like-any-other.md
    - ../retirement.kb/the-forecast-discount-cuts-both-ways.md
    - ../genesis.kb/friction-is-paid-per-invocation.md
    - ../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md
verify: ../retirement.py --observed
---

# The Unseamed Cluster Is Also the Unused One

Population: the twenty `claude-*` commands on PATH. Sources: 298 session logs
under `~/.claude/projects/`, holding every Bash call this harness has ever made,
plus `~/.bash_history`. Measured 2026-08-10 by `../retirement.py`. **Recurrence
had never been counted before this run** -- `../genesis.kb/friction-is-paid-per-invocation.md`
named the proxy and left it unrun, and every friction estimate in the kb above
predates it.

```
$ ../retirement.py --observed
population  20 tools on PATH; ~/bin holds 197
attested    298 session logs + ~/.bash_history

tool                        named  shell  called  touch  last
claude-branch-extract          18      0       9      0  2026-08-10
claude-branch-list             15      0       6      0  2026-08-09
claude-export                  11      0       0      0  2026-08-10
claude-fork                    16      0       2      1  2026-08-10
claude-inventory               16      0       6      0  2026-08-10
claude-jsonl-cwd               17      0       4      1  2026-08-11
claude-jsonl-display           15     52      32      0  2026-08-11
claude-jsonl-path              12      0       2      0  2026-08-11
claude-jsonl-summarize         10      0       1      0  2026-08-11
claude-jsonl-to-log            10      0       1      0  2026-08-11
claude-open-tasks              11      4       4      0  2026-08-10
claude-open-tasks-list         20     28      26      0  2026-08-11
claude-path                   147      2      72      5  2026-08-11
claude-plan                     9      1       2      0  2026-08-10
claude-print-verbose            7      8       4      0  2026-08-10
claude-s                       14      1       2      0  2026-08-10
claude-search                  25      0      13      0  2026-08-11
claude-slug                    98      0      11      2  2026-08-11
claude-uncolor                 13      1       3      0  2026-08-11
claude-workspace-merge         18      1       1      3  2026-08-10

no invocation attested: 1 of 20
  claude-export             named   11x, never invoked  UNDECIDED

dispositioned retire, still installed: claude-plan       # exit 1
```

Dates are the log's UTC stamps; `2026-08-11` is this evening, local.

## The agreement

The three least-invoked tools in the population are `claude-export` (0),
`claude-workspace-merge` (1) and `claude-fork` (2) -- **exactly the three members
of `claude-session-lifecycle`**, the cluster killed on `NONE` for being pairwise
disjoint on both code and artifacts
(`the-claude-prefix-splits-five-ways.md`). Two instruments that share no input --
one reading source text, one reading command lines -- return the same three
names, and neither was built with the other in mind.

**What the agreement does not license is a deletion.** Low recurrence is *expected*
for all three: a fork and a workspace merge are rare manual operations, and
`../genesis.kb/CLAUDE.md` says in as many words that reaching for the frequency
argument and finding it absent is not a verdict, because `REUSE` can carry a tool
alone. The finding is sharper than "unused": these three cannot be justified by
friction, **and nobody has said which numerator they are on.** That is
`PRUNE`'s denominator, unstated for three of twenty tools, and it is the work
this measurement creates rather than the work it finishes.

## The measurement is polluted by its own analyst

Every tool was `named` between 7 and 147 times, and nothing scored zero. That
column counts the name anywhere in a command line, so it over-approximates use --
the sound direction for a deletion, since a zero could then be trusted. It is
never zero, because studying twenty tools types their names twenty times: two
days of building this ledger put every one of them into the record.

So the sound measure is vacuous and the verdict rests on `called` -- the name in
command position -- which under-approximates and whose zero proves nothing. **An
over-approximation is only sound until an analyst arrives.** The check says so in
its own docstring rather than hiding it, and this is the reason
`../retirement.kb/a-subsumed-tool-needs-no-estimate.md` rests on the reference
graph instead of on this table.

## Three smaller things the table settled

- **`FORECAST` was right about `claude-jsonl-summarize`.** It sits `unsettled`
  with the reason "not yet read closely", and the claim argued its numerator was
  therefore all forecast. Measured: one attested invocation, ever. The prediction
  was made before anyone counted.
- **Two tools live on bukzor's recurrence, not the agents'.**
  `claude-jsonl-display` (52 shell mentions, 32 invocations, against 15 agent
  mentions) and `claude-open-tasks-list` (28) are human-driven; the rest are
  agent-driven or barely attested. The log therefore gives a **lower bound** on
  audience -- who does use it -- and still cannot decide `AUDIENCE`, which asks
  who *should be able to*. `../levels.kb/audience-is-not-in-the-files.md` survives
  intact: this is a name-abstraction narrowing, not a decision.
- **The packaged pair is the most-invoked.** `claude-path` at 72 and
  `claude-slug` at 11 lead the population by a factor of two, which is
  after-the-fact support for the one graduation call this kb has made.

## What would make this stale

Any use of any tool, which is to say: continuously. The counts are cumulative and
monotone, so a *zero* is the only durable reading here and every positive number
is a floor with today's date on it. Re-run it; do not cite the numbers.
