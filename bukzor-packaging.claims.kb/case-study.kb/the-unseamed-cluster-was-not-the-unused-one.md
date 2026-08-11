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

# The Unseamed Cluster Was Not the Unused One

Population: the twenty `claude-*` commands on PATH. Sources: 281 session logs
under `~/.claude/projects/`, **cut at 2026-08-09** -- the day this study opened --
plus `~/.bash_history`, which bash leaves undated and which is therefore counted
entire. Re-measured 2026-08-11 by `../retirement.py`.

This file was first written on 2026-08-10 over the *uncut* corpus, and its
headline finding did not survive the cut. What follows is the corrected
measurement and then what the correction destroyed, because the destroyed version
is the more useful of the two.

```
$ ../retirement.py --observed
population  20 tools on PATH; ~/bin holds 197
attested    281 session logs, cut at 2026-08-09 + ~/.bash_history

tool                        named  shell  called  touch  last
claude-branch-extract           8      0       5      0  2026-08-08
claude-branch-list              3      0       1      0  2026-08-08
claude-export                   0      0       0      0  --
claude-fork                     5      0       1      1  2026-08-08
claude-inventory                0      0       0      0  --
claude-jsonl-cwd                9      0       3      1  2026-08-08
claude-jsonl-display            5     52      31      0  2026-08-08
claude-jsonl-path               2      0       0      0  2026-08-08
claude-jsonl-summarize          1      0       0      0  2026-08-08
claude-jsonl-to-log             2      0       0      0  2026-08-08
claude-open-tasks               0      4       4      0  --
claude-open-tasks-list          4     28      24      0  2026-07-19
claude-path                    45      2      28      2  2026-08-08
claude-plan                     1      1       0      0  2026-08-08
claude-print-verbose            1      8       4      0  2026-08-08
claude-s                        1      1       0      0  2026-08-08
claude-search                   0      0       0      0  --
claude-slug                    13      0       1      0  2026-08-08
claude-uncolor                  1      1       1      0  2026-08-08
claude-workspace-merge          0      1       1      0  --

no invocation attested: 8 of 20
  claude-export, claude-inventory, claude-jsonl-path, claude-jsonl-summarize,
  claude-jsonl-to-log, claude-plan, claude-s, claude-search        # exit 1
```

## What the cut destroyed, and why that is the finding

The first version reported **1 of 20** unattested and built its central claim on
it: that the three least-invoked tools were *exactly* the three members of
`claude-session-lifecycle`, the cluster killed on `NONE` for pairwise disjointness
(`the-claude-prefix-splits-five-ways.md`) -- two instruments sharing no input,
returning the same three names.

**That agreement was manufactured by the study.** Cut the corpus at the day the
census opened and `claude-fork` has an attested invocation, `claude-workspace-merge`
has one from bukzor's own shell, and the only ad-hoc candidate that has never been
invoked by anybody is `claude-export`. The coincidence was three tools being
*handled* by an analyst, not three tools being unused.

The honest number is **8 of 20, not 1 of 20** -- eight times as many candidates,
in the direction that licenses action. So the pollution was not a caveat on the
margin of a good measurement; it was hiding seven of eight findings, and the one
it left visible was the one it had invented.

The cut is stratification by something the analyst cannot influence. Stratifying
by *topic* instead -- dropping the sessions that were "about" the tools -- would
have dropped real invocations along with the mentions and manufactured zeros in
the same permissive direction, which is why that repair was rejected
(`../../docs/dev/formalization.claims.kb/a-measure-whose-corpus-includes-its-analysis-is-unsound.md`).

## The audit that erased its own evidence

`claude-export` was the one name the uncut census flagged, and checking whether it
still worked meant running it. On 2026-08-11 it was invoked once, by the agent
auditing it, and `no invocation attested` fell to **0 of 20**: the finding was
deleted by the act of confirming it. That is the sharpest available instance of
the law this file exhibits, and it is the reason the cut is now in the check
rather than in a maintenance note.

What the run established is worth more than the count it cost. `claude-export`
appends `export VAR=value` to the running session's shell snapshot -- located
race-free through `/proc/self/stat` field 6 and `ps --sid` -- so a variable set in
one `Bash()` call survives into the next. Verified working. Its audience is
*agents*, and no `CLAUDE.md` on this machine mentions it. **Zero use here is zero
discoverability, not zero benefit**, which is a different verdict from the one the
number invited.

## The over-approximation was vacuous, and now it is not

In the uncut corpus every tool was `named` between 7 and 147 times and nothing
scored zero -- so the column that over-approximates use, and whose zero would have
been the *sound* direction for a deletion, was worthless. Cut, four tools score a
genuine zero on it. **The sound direction was not lost, it was borrowed by the
analyst and has been returned.** The verdict block still keys on `called`, which
under-approximates, so a zero there remains a candidate rather than a decision.

## Four smaller things the corrected table settles

- **`FORECAST` was right about `claude-jsonl-summarize`, more so.** Filed
  `unsettled` for "not yet read closely", its numerator argued to be all forecast.
  Measured over the pre-study corpus: **never invoked**, and named once. The
  earlier reading gave it one invocation, which was the study opening the file.
- **Two tools live on bukzor's recurrence, not the agents'.** `claude-jsonl-display`
  (52 shell mentions, 31 invocations, against 5 agent mentions) and
  `claude-open-tasks-list` (28 and 24, last invoked 2026-07-19) are human-driven.
  The log gives a **lower bound** on audience and still cannot decide `AUDIENCE`,
  which asks who *should* be able to use it;
  `../levels.kb/audience-is-not-in-the-files.md` survives intact.
- **The packaged pair is not uniformly the most-invoked.** `claude-path` leads the
  population at 28 attested invocations, which is after-the-fact support for the
  graduation call. `claude-slug` has **one**. The uncut table showed 72 and 11 and
  read as joint vindication; the port was justified by the encoder's use, not by
  the slug command's.
- **Two of the twenty are not candidates at all.** `claude-inventory` and
  `claude-search` are generated console scripts of the shipped
  `claude-code-archeology` package, living in `~/.local/bin`. Their zeros mean "a
  shipped package's commands go uncalled", which is a real finding about that
  package and not a retirement candidate here. The population is measured by a
  PATH scan, so it mixes candidates with package output -- named as a cost in
  `../../bukzor-packaging.claims.md`.

## What would make this stale

The cut makes the *pre-2026-08-09* numbers durable, which is new: they cannot grow
and no future session can move them. What can still rot is the corpus itself --
between two runs on 2026-08-11 the log count read 299, then 280, then 281, so the
directory is not append-only and a count here is not a promise. The post-cut
window is unmeasured by design; the price of a corpus the analyst cannot pollute
is a corpus that cannot see today.
