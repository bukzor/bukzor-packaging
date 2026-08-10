---
label: DERIVED
standing: bare
authority: >-
    the encoding change and its blast radius are documented in
    ~/.claude/sessions.kb/penguin/claude-path-encoding-change-orphans-stores.md
    (2026-07-27); the migration was priced and declined, and
    git-localhost-store's .claude/todo.md carries both open items
why:
    - ../cost.kb/cheap-tools-pin-drifting-facts.md
    - ../seams.kb/a-shared-leaf-resolves-contention.md
verify: ../coherence.py --derived
---

# A Derived Key Must Be Recomputed or Checked

Carrier: pairs (*x*, *k*) where *k* = *f*(*x*) was computed once and stored.
The invariant *k* = *f*(*x*) is not maintained by anything; it decays under
two independent motions:

1. ***f* changes** -- the deriving function is edited.
2. ***x* changes** -- the input is renamed or moved.

A system storing a derived key must recompute it on use, check and repair it,
or **decide** to carry the staleness. Doing nothing is not a fourth option; it
silently selects the third, and the difference between selecting it and
deciding it is the whole content of this claim.

## Both motions, exhibited

`git-localhost-store` stores 53 such keys and never recomputes them, because it
exits early whenever the relocation symlink already exists. Both decay motions
have happened to it, and the measurement separates them: **31** keys where *f*
changed (an encoding migration that was priced and **declined** -- a decision,
and it stands on its merits) and **3** where *x* changed (worktrees that moved
after relocation, which nobody has priced).

Exhibit, with the commands and the dates:
`../case-study.kb/the-store-key-encoding-has-drifted-twice.md`.

That split is the whole point of the claim. Stale-versus-clean is not the
distinction that matters; decided-versus-defaulted is. A system carrying 31
stale keys on purpose is in better shape than one carrying 3 by accident, and
only a check can tell the two populations apart.

## What follows for anyone porting a deriving function

- **The early exit is load-bearing, not an oversight.** A rewrite that eagerly
  recomputes turns dormant mismatches into empty stores -- silent failure at
  exactly the moment the system is supposed to work.
- **Ship the check with the encoder.** Its job is to bound a decision already
  taken, not to reopen it. This is `ERRORCOST`, not `FRICTION`: nobody runs it
  for convenience (`../genesis.kb/a-recurring-error-earns-a-check-not-a-command.md`).

## What would kill it

A back-reference making recompute unnecessary -- if each store recorded its
worktree, staleness would be repairable without guessing, and both motions
would be detectable at zero cost. It does not: all 1012 store directories
record no worktree at all, which is why this check had to walk the filesystem
instead of reading the store.
