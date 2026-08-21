---
label: ACCIDENT
standing: agent
why:
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
    - ../cost.kb/cost-splits-into-site-and-item.md
---

# Building Closes Open Questions by Accident

Carrier: a set *Q* of open questions, each with a set of admissible answers.
Operation: perform an action *a*. Law:

> Some actions *a* collapse a question's admissible set to one element
> **without appealing to that question's merits.** Call that accidental
> closure. It is inflationary (closed stays closed), monotone (doing more
> closes no less), and it does not commute with deliberation: once *a* has
> happened, arguing about *q* is arguing about a migration.

The dangerous property is not irreversibility as such -- it is that the
closure is *invisible at the time*. Nobody writes "and hereby I decide the
charter of `claude-code-archeology`"; they move one file into it.

## Smallest instance

`refactors.kb/display-renders-two-schemas.md`, which spotted this before the
theory existed: "Do this before absorbing any `claude-jsonl-*` member into
`claude-code-archeology`, since the first absorption is what decides it."

The open question is whether that package's charter is *archived transcripts*
or *Claude Code record streams, live or archived*. Moving
`claude-jsonl-display` in answers it -- the package now handles live
stream-json, and the charter is retrofitted to the fact. No one chose; a
`git mv` did.

The same structure condemns building `claude-stream` as proposed: per
`../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md` its two
members are joined only through the renderer, so whichever package is built
first takes the renderer, and taking the renderer decides the charter.

## The variant that is worse than closure

Sometimes the action does not close the question -- it contaminates the
evidence the answer needed.

"When a worktree is renamed, does its store key migrate or go stale?" is an
open item in `git-localhost-store`'s todo. During unrelated work this session
it was answered once, by hand, on this kb: the store directory was `mv`'d and
the symlink re-pointed so `git log` kept working. Meanwhile three other
worktrees sit under keys naming paths they have left
(`../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md`).

Note what that expedient cost. Before it, the population was uniform and the
answer could be a single migration script or a single decision to carry the
staleness. After it, any answer has to cope with a system where both policies
are already present -- and a repaired store is indistinguishable from a store
that was always correct. The question is still open, in a state that is
strictly harder to close.

This is worth separating from accidental closure proper because the tell is
different. Closure announces itself eventually: someone asks the question and
finds it already answered. Contamination never does -- the question stays
open, so nothing prompts anyone to look for the damage.

**Contrast the encoding change**, which is the well-handled case. Same tool,
same kind of drift, 31 worktrees affected -- and it was written up, priced, and
**declined**. A decision that leaves 31 stale keys is not accidental closure;
it is a decision. The distinction this theory draws is not stale-versus-clean,
it is decided-versus-defaulted.

## What would kill it

Closures that are all cheap to reverse. In a system where every move is a
rename away from being undone, accidental closure is harmless and the
apparatus of guarding is waste. This system is not that: package moves land
in git history, in a published dist name, and -- as the store shows -- in data
on disk that outlives the decision.
