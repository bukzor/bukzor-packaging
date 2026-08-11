---
label: LATENT
standing: agent
why:
    - a-cluster-is-legitimate-when-no-member-is-isolated.md
    - two-implementations-are-one-node-only-after-merging.md
verify: ../seams.py --artifacts
---

# A Cluster May Be Seamed Latently

There is a second relation, and the gap between the two is the object worth
having.

Carrier: tools, plus **artifacts** -- schemas and data locations a tool reads
or writes (`session-jsonl`, `record-schema`, `stream-json`,
`todo-markdown`, `worktree`, `shell-snapshots`, `slug-encoding`). Take the
bipartite incidence *I* ⊆ tools × artifacts, and define

> *G*⁺ := *G* ∪ { *t*–*u* : *I*(*t*) ∩ *I*(*u*) ≠ ∅ }

so *G* ⊆ *G*⁺ by construction, and any cluster connected in *G* is connected
in *G*⁺. Three verdicts follow, and they are exhaustive:

| verdict | condition | meaning |
|---|---|---|
| **seamed** | no isolated vertex in *G*[*S*] | the sharing is in the code; ship it |
| **latent** | isolated in *G*[*S*], not in *G*⁺[*S*] | separable but not separate; a refactor realizes the edge |
| **none** | isolated in *G*⁺[*S*] | no refactoring makes this a package |

**The latent verdict is the whole point.** It is the formal content of
"separable but not currently separate" (`criteria.kb/separable-vs-separate.md`),
and it comes with an obligation rather than a compliment: the members share
knowledge that *no code expresses*, which means each member expresses it
separately, which is `two-implementations-are-one-node-only-after-merging.md`
-- a drift bug waiting. The shared artifact tells you exactly which code to
extract.

Downstream this gets a witness rather than a hint: the shared artifact **is** an
unnamed intermediate object, and naming its type is what discharges the verdict
(`../composition.kb/an-extraction-names-an-intermediate-object.md`). If no type
can be named, the seam was not latent -- it was absent.

Why the promotion gate is *G* and not *G*⁺: *G*⁺ is far too loose to gate on.
Any two tools that touch one file format share an artifact, so *G*⁺ would
license `{claude-uncolor, claude-jsonl-summarize}` as a package on the
strength of both mentioning `.jsonl`. *G*⁺'s value is entirely negative --
what it *fails*, no refactor rescues.

## Smallest instance

`{claude-print-verbose, claude-s}`. No edge between them in *G*. Both match
`stream-json`, so they are joined in *G*⁺. And the extraction the artifact
predicts is already written down independently, before this relation existed:
`refactors.kb/extract-stream-json-invocation.md` -- the shared core is
`claude --print --output-format=stream-json --input-format=MODE`. The latent
edge and the filed refactor are the same fact found twice, which is the
strongest evidence available that the relation is measuring something real.

The other two latent verdicts corroborate the same way:
`claude-open-tasks` ↔ `todo-markdown` predicts
`refactors.kb/dedup-open-tasks-implementations.md`; `claude-uncolor` ↔
`session-jsonl` predicts a record model that `claude-jsonl-display` should
also import, which is
`refactors.kb/display-renders-two-schemas.md`'s "related overlap" section.
Three latent edges, three refactors already filed, none of them filed with
this relation in mind.

## The negative result

`claude-session-lifecycle` = `{claude-fork, claude-workspace-merge,
claude-export}` fails *G*⁺: `worktree`, `{session-jsonl, slug-encoding}`,
`shell-snapshots`, pairwise disjoint. **This cluster should not be built, and
no refactor will fix it** -- the three tools share a lifecycle in the
author's head and nothing on disk.

Better, the measurement says where the members do belong:
`claude-workspace-merge` has `slug-encoding` (→ `claude-slug`) and
`session-jsonl` (→ `claude-code-archeology`). Its artifact edges point out of
its cluster into two established ones. `claude-fork` and `claude-export` have
no artifact in common with anything and are, on this evidence, `dotfiles`.

That is the result the `/formalize` bar asks for stated plainly: for this
cluster there is no structure here.

## What would kill it

A cluster that fails *G*⁺ and is nonetheless worth building -- which would
mean a real seam invisible to both relations. The likely shape is a shared
*protocol* rather than a shared artifact: three tools that must agree on an
exit-code convention or a lock file, with no schema in common. If one turns
up, the incidence needs protocols as artifacts; the fix is to widen *I*, not
to abandon the verdict scheme.

That widening is available: in `../composition.kb/` an object is any format two
tools must agree on, so a protocol is already one. What *I* would gain is a row,
not a redefinition.
