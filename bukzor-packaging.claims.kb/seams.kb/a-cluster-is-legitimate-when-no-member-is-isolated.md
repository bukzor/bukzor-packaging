---
label: SEAM
standing: agent
why:
    - ../levels.kb/observation-comes-in-four-levels.md
    - ../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md
verify: ../seams.py --edges
---

# A Cluster Is Legitimate When No Member Is Isolated

Carrier: the directed graph *G* on tools, with an edge *t → u* when *t*
references *u*. Operation: take a cluster *S* and form the induced subgraph
*G*[*S*]. Law:

> **A cluster of two or more may reach status `accepted` or `shipped` only
> if *G*[*S*] has no isolated vertex.**

An isolated member shares nothing with its siblings -- it would import
nothing from them and export nothing to them. A set of such members is a
directory with a common prefix, which is the trap
`../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md` names.

Three qualifications, each doing work:

**Vacuous on singletons.** A one-member package has no siblings, so the law
says nothing about it. `git-localhost-store` needs no seam argument at all;
it is decided entirely by `../cost.kb/` and `../graduation.kb/`. "Is this a
cluster" and "should this be packaged" are different questions, and the law
answers only the first.

**A gate on promotion, not on proposal.** A proposal may rest on edges a
refactor would create; that is `a-cluster-may-be-seamed-latently.md`, and
the distance between the two relations is the refactor backlog.

**Measured on textual reference,** which over-approximates calling: three of
the eight edges (`claude-jsonl-cwd → claude-jsonl-path`,
`claude-jsonl-cwd → claude-slug`, `claude-slug → claude-path`) are comment
mentions. That is the safe direction, because every verdict below is a claim
of *absence*: an over-approximation that still finds nothing found nothing.

## Smallest instance

`{claude-slug, claude-path}`: `claude-path`'s last line is
`exec "$(dirname …)/claude-slug" "$path"`. One edge, no isolated vertex,
seamed. Contrast `{claude-plan, claude-s, claude-print-verbose}` -- the group
originally filed as launcher aliases -- where `claude-plan` has no edge in
either direction, and no shared artifact either. It was never a candidate;
it is being retired.

## What the data says

`bin/seam-check`, over the 16 `~/bin/claude-*` scripts and the disposition
index:

| cluster | *G* | with latent edges |
|---|---|---|
| `claude-slug` | **seamed** | seamed |
| `claude-code-archeology` | isolated: `claude-uncolor` | latent |
| `claude-open-tasks` | isolated: both | latent |
| `claude-stream` | isolated: both | latent |
| `claude-session-lifecycle` | isolated: all three | **none** |

One clean pass, three latent, one dead. `claude-stream` failing *G* is a
result worth stating on its own: `claude-print-verbose` does have an edge --
it pipes into `claude-jsonl-display` -- but that edge *leaves the cluster*
and lands in `claude-code-archeology`. Two clients of one library is not a
library.

## A defect this exposed in the index

`dispositions.md` has one disposition column, and it is doing two jobs: where
a tool *is* and where it *goes*. `claude-code-archeology` is `shipped`, but
its shipped members (`claude-search`, `claude-inventory`,
`claude-branch-list`, `claude-branch-extract`, all over one library) are
seamed; the LATENT verdict comes from the five `~/bin` scripts the index
*assigns* to it, which have not moved. So the law is not violated today, and
the index cannot say so. It needs a state column, or the planned absorptions
belong in `refactors.kb/` rather than in the index.

## What would kill it

A package whose value is bundling rather than sharing -- a coherent suite
whose commands genuinely never touch each other's code but that a user wants
installed as one thing. `bukzor-tools` is exactly that, which is why it is a
meta-package: it re-exports entry points and declares dependencies, and owns
no code for a member to import.
