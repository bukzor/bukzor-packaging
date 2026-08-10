---
label: CASECLUSTER
standing: bare
why:
    - ../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
    - ../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md
verify: ../seams.py
---

# The `claude-` Prefix Splits Five Ways

Population: the sixteen `~/bin/claude-*` scripts, as indexed by
`../../dispositions.md`. Measured 2026-08-10 by `../seams.py`, which builds
*G* from textual references and *G*⁺ by adding artifact incidence.

```
SHIPPED claude-code-archeology: claude-jsonl-path, ... on PATH, not in ~/bin
SHIPPED claude-code-slug: claude-slug, claude-path on PATH, not in ~/bin
LATENT  claude-open-tasks: claude-open-tasks, claude-open-tasks-list ...
LATENT  claude-stream: claude-print-verbose, claude-s ...
--      retire: claude-plan
--      unsettled: claude-fork, claude-workspace-merge, claude-export,
                   claude-jsonl-summarize
```

Two shipped, two latent, one cluster killed outright, one relic, four unsettled.
**The prefix names no package**, which is the negative result the whole exercise
was bought to establish -- and note that the two packages it does name were
carved *out* of the prefix rather than found within it.

The first run of this table, hours earlier, read `SEAMED claude-slug` and
`LATENT claude-code-archeology`. Both rows moved by being acted on, not by being
re-measured.

## The one that was actually seamed

`claude-slug` was the only verdict in the table resting on a real `exec` rather
than on a comment mention: `claude-path` line 20 exec'd it by resolved-`$0`
sibling path. Everything else called SEAMED anywhere in this kb would rest on
weaker evidence, which is the discount `../seams.kb/`'s guide records about *G*.

**That edge is now an `import`.** The strongest edge the weak relation could see
was the one that survived extraction into a declared dependency -- which is the
outcome `../../packages.kb/claude-code-slug.md` was arguing for, and a small
piece of evidence that *G*'s over-approximation is worst at the bottom of the
scale rather than the top.

## The three latent seams, and what each predicted

Each latent verdict says the members share an artifact but no code, so the
shared artifact names the code to extract. In all three cases a refactor
answering exactly that description had already been filed independently,
before the relation existed:

| cluster | shared artifact | refactor already filed |
|---|---|---|
| `claude-stream` | `stream-json` | `extract-stream-json-invocation` |
| `claude-open-tasks` | `todo-markdown` | `dedup-open-tasks-implementations` |
| `claude-code-archeology` | `session-jsonl` | the record model in `display-renders-two-schemas` |

Three for three. That agreement is the strongest evidence in the ledger that
artifact incidence is measuring something real and not an artifact of the
regexes.

## The cluster that died

`claude-session-lifecycle` -- `claude-fork`, `claude-workspace-merge`,
`claude-export` -- fails even *G*⁺: pairwise disjoint on both code and
artifacts, so no extraction is available. Worse, `claude-workspace-merge`'s two
artifacts point *out* of the cluster, into `claude-slug` and
`claude-code-archeology`. The full argument is
`../../packages.kb/claude-session-lifecycle.md`, now `status: rejected`.

Reproducing it needs the members passed explicitly, because acting on the
verdict removed the cluster from the index:

```
$ ../seams.py --cluster claude-fork,claude-workspace-merge,claude-export
NONE    (given): ... share nothing with siblings          # exit 1
```

That is why `--cluster` exists. A verdict that stops being reproducible when it
is acted on is not evidence.

## What would make this stale

Any edit to a `~/bin/claude-*` script, or any change to
`../../dispositions.md`. The verdicts are a function of both, which is what
the `verify:` is for -- this file should be re-run rather than trusted.
