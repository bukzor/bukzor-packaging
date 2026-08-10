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
LATENT  claude-code-archeology: claude-uncolor share artifacts, not code
LATENT  claude-open-tasks: claude-open-tasks, claude-open-tasks-list ...
SEAMED  claude-slug
LATENT  claude-stream: claude-print-verbose, claude-s ...
--      retire: claude-plan
--      unsettled: claude-fork, claude-workspace-merge, claude-export,
                   claude-jsonl-summarize
```

One seamed cluster, three latent, one cluster killed outright, one relic, four
unsettled. **The prefix names no package**, which is the negative result the
whole exercise was bought to establish.

## The one that is actually seamed

`claude-slug` -- and it is the only verdict in the table resting on a real
`exec` rather than on a comment mention. `claude-path` line 20 execs
`claude-slug` by resolved-`$0` sibling path. Everything else called SEAMED
anywhere in this kb would rest on weaker evidence, which is the discount
`../seams.kb/`'s guide records about *G*.

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
