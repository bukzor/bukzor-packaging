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

## The instance, measured

`git-localhost-store` relocates a repository's `.git` to
`~/.local/state/git-localhost-store/repos/<key>/` and leaves a symlink, where
`<key>` = `claude-path <worktree>` (line 33). It exits at `[ -L .git ]`
(line 41) whenever the symlink already exists, so for an already-relocated
repo the key is never recomputed.

`coherence.py --derived`, 2026-08-10, over the worktrees under `~/repo`,
`~/claude`, `~/.claude`, `~/empty`, `~/trash`:

| | |
|---|---|
| live relocated worktrees | 53 |
| key matches today's encoder | 19 |
| key disagrees | 34 |
| ... legacy encoding of the same path | **31** |
| ... neither encoding of it -- workdir moved since | **3** |

Both decay motions, separated:

***f* changed, and this was decided.** 31 keys are the pre-2026-07-05
encoding: `-` doubled, `/` → `-`, dots verbatim. `~/claude/amazon-searches`
is stored at `-home-bukzor-claude-amazon--searches`. The change came from an
uncommitted rewrite of `~/bin/claude-path` delegating to the then-new
`claude-slug`; it is written up in the session note above, and **the migration
was declined on cost/benefit.** Declining is defensible for exactly the reason
the early exit makes true: nothing fails until a store must be *created or
recovered*, so the 31 are exposed only on recovery -- which is, however, the
system's whole purpose.

***x* changed, and this was not decided.** 3 keys match neither encoding of
their current path, because the workdir moved after relocation:
`~/claude/crostini-health` still keyed as `-home-bukzor-claude-vm-freeze-2026-08-08`;
`~/claude/trash/scratch.pygame-zero` keyed as though it were still outside
`trash/`; `~/repo/github.com/bukzor/2026-05-19--task-archeology` keyed under
its old `~/claude/homedir-archeology` name. This is the open item in the
tool's own todo, filed 2026-08-10 after hitting it by hand on this kb.

## What the measurement adds

The prior sweep in the session note counted **one** doubly-encoded repo -- two
stores for one worktree. That is a different quantity from this one. The
declined migration's residue is not one repo; it is **31 live worktrees whose
recovery would silently create an empty store**, plus 3 more from a cause
nobody has priced.

So the decision to decline stands unchallenged on its merits, and it was
taken against an unmeasured population. That is the correction this claim
carries -- not "nobody noticed", which would be false.

## What this costs the packaging plan

`packages.kb/claude-slug.md` proposes porting the encoder to Python and calls
the port faithful. Faithful is the right target -- **the encoding is frozen,
and the port must not improve it** -- but two things follow that a port alone
does not deliver:

- the early exit is load-bearing, not an oversight. Any packaged
  `claude-path` that eagerly recomputes keys turns 34 dormant mismatches
  into 34 empty stores.
- the check should ship with the encoder. `coherence.py --derived` is its
  prototype, and its value is bounding a decision already made rather than
  reopening it.

## What would kill it

A back-reference making recompute unnecessary -- if each store recorded its
worktree, staleness would be repairable without guessing, and both motions
would be detectable at zero cost. It does not: all 1012 store directories
record no worktree at all, which is why this check had to walk the filesystem
instead of reading the store.
