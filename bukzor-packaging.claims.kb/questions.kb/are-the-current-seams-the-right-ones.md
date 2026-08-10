---
label: QSEAM
standing: agent
why:
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
    - ../closure.kb/building-closes-open-questions-by-accident.md
    - ../closure.kb/a-guard-names-a-reversal-cost.md
---

# Are the Current Seams the Right Ones?

**As experienced** (bukzor, 2026-08-09): *"are our clusters-of-tools
(candidate packages) well served by their current seams? or rather: would
things package/test 'better' if we did some work to refactor along some other
seam(s)?"*

**Well-posed, in two parts:**

1. Which clusters are *latent* rather than seamed -- isolated in *G*,
   connected in *G*⁺? Each one names a refactor, and the shared artifact
   names the code to extract.
2. Which builds would close a seam question by accident, and which of those
   closures is expensive enough to guard?

**What the difference reveals:** "well served" invites taste; the posed
version is a **count and a list**. And splitting it in two is the finding
that mattered -- the original question conflates *what the right seam is*
with *when you have to decide it*. Those come apart: three refactors are
identified and none is urgent, while one decision is urgent precisely because
an unrelated build would make it silently.

## Settled: three latent seams, one guard

`../seams.kb/a-cluster-may-be-seamed-latently.md` measured it, and the
striking part is the corroboration: each latent edge predicted a refactor
that was **already filed independently**, before the relation existed.

| latent cluster | shared artifact | refactor it predicts |
|---|---|---|
| `claude-stream` | `stream-json` | `extract-stream-json-invocation.md` |
| `claude-open-tasks` | `todo-markdown` | `dedup-open-tasks-implementations.md` |
| `claude-code-archeology` ∋ `claude-uncolor` | `session-jsonl` | the record model in `display-renders-two-schemas.md` |

So the answer to part 1 is: **no, three of five clusters are not well served,
and the work is already named.** Part 2: exactly one guard is justified --
the renderer's home -- because that closure lands in git history, a dist
name, and every machine that installed the earlier version
(`../closure.kb/a-guard-names-a-reversal-cost.md`).

## Residue

- **widen versus leaf for the renderer** is unresolved and is *not* an
  architecture question: both satisfy the seam laws, so it is a comparison of
  one more package's site cost against one wider charter
  (`../cost.kb/cost-splits-into-site-and-item.md`). The measurement that
  would settle it is stated in the refactor entry and has not been run: count
  how much of the 714 lines is schema-specific.
- **`claude-session-lifecycle` is dead** and its members need homes. That is
  not residue on this question -- it is answered -- but nothing has been
  written down in `dispositions.md` yet, and until it is, the index still
  shows a cluster that the measurement says cannot exist.
