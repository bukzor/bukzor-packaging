---
label: CASEDRIFT
standing: bare
authority: >-
    the encoding change and its blast radius are documented in
    ~/.claude/sessions.kb/penguin/claude-path-encoding-change-orphans-stores.md
    (2026-07-27); the migration was priced and declined, and
    git-localhost-store's .claude/todo.md carries both open items
why:
    - ../coherence.kb/a-derived-key-must-be-recomputed-or-checked.md
    - ../coherence.kb/two-live-implementations-are-resolved-by-search-order.md
    - ../genesis.kb/a-recurring-error-earns-a-check-not-a-command.md
verify: ../coherence.py --derived && ../coherence.py --shadow
---

# The Store Key Encoding Has Drifted Twice

Population: every worktree under `~/repo`, `~/claude`, `~/.claude`, `~/empty`,
`~/trash` whose `.git` is a symlink into git-localhost-store. Measured
2026-08-10.

`git-localhost-store` relocates a repository's `.git` to
`~/.local/state/git-localhost-store/repos/<key>/` where `<key>` is the worktree
path run through `claude-path` (line 33), and exits at `[ -L .git ]` (line 41)
whenever the symlink already exists -- so for an already-relocated repo the key
is never recomputed.

## Motion one: the function changed

```
store directories:            1012
live relocated worktrees:       53
key matches today's encoder:    19
key disagrees:                  34
  legacy encoding of it:        31  (declined migration)
  neither encoding of it:        3  (workdir moved since)
unreferenced store dirs:       959
```

The 31 carry the pre-2026-07-05 encoding -- `-` doubled, `/` → `-`, dots
verbatim -- so `~/claude/amazon-searches` is stored at
`-home-bukzor-claude-amazon--searches`. This was **priced and declined**, and
declining is defensible for the reason the early exit makes true: nothing fails
until a store must be created or recovered.

What the measurement adds is the size of what was carried. The prior sweep in
the session note counted **one** doubly-encoded repo, which is a different
quantity. The residue of the declined migration is 31 live worktrees whose
recovery would silently create an empty store. The decision stands on its
merits and was taken against an unmeasured population.

## Motion two: the input moved

Three keys match neither encoding of their current path, because the workdir
moved after relocation:

| worktree | key on disk |
|---|---|
| `~/claude/crostini-health` | `-home-bukzor-claude-vm-freeze-2026-08-08` |
| `~/claude/trash/scratch.pygame-zero` | keyed as though still outside `trash/` |
| `~/repo/github.com/bukzor/2026-05-19--task-archeology` | `-home-bukzor-claude-homedir--archeology` |

This is the open item in the tool's own todo, filed 2026-08-10 after hitting it
by hand. Nobody has priced it.

## Where the encoding lives, and where it came from

`../coherence.py --shadow`, 2026-08-10 evening, **after both repairs described
below** -- the encoder is now a package:

```
claude-slug resolves to:  ~/.local/bin/claude-slug  (installed in bukzor-tools)
claude-path resolves to:  ~/.local/bin/claude-path  (installed in bukzor-tools)

sites implementing the encoding:
  delegates  committed  ~/bin/claude-jsonl-cwd:5
  delegates  committed  ~/bin/claude-jsonl-path:3
  delegates  committed  ~/bin/claude-workspace-merge:106
  current    committed  ~/repo/.../bukzor-agent-skills/bin/claude-slug:11
  current    committed  ~/repo/.../bukzor-agent-skills--replication-run/...:11
  LEGACY     committed  ~/repo/.../dotfiles/bin/claude-path:12
  delegates  committed  .../claude-code-slug/lib/claude_code_slug/path.py:4
  current    committed  .../claude-code-slug/lib/claude_code_slug/slug.py:15

2 files implement the encoding independently, and nothing
declares which is authoritative -- PATH order decides.
```

Three `~/bin` scripts now *delegate* where two used to duplicate. The `LEGACY`
row is a second checkout eight months stale on one tracked file; it will drop
off on its next pull.

### The before-picture, and the repair

Measured earlier the same day, this check reported something worse, and it is
worth keeping because it is what prompted the fix. `$HOME` is the dotfiles
working tree, and the live encoder existed **only** in it: `~/bin/claude-slug`
was `UNTRACKED`, and `~/bin/claude-path`'s delegation to it was an uncommitted
modification five weeks old. A fresh clone got `bin/claude-path` implementing
the **legacy** encoding and no `claude-slug` at all -- so the encoder that named
53 store directories was not in version control, and the one that was would
have orphaned them.

Repaired 2026-08-10 in dotfiles by `c879ca1` (track `claude-slug`) and
`d983aad` (commit the delegation). Clone fidelity now passes. Recording this
rather than overwriting it is the point: the check found a live hazard in a
system nobody thought was broken, and the interval between finding and fixing
was under an hour.

### What the package retired, and what is still red

The before-picture counted **3 tracked implementations** -- `~/bin/claude-slug`,
`bukzor-agent-skills/bin/claude-slug` (byte-identical, tracked since `e77440e`,
2026-07-05, in a repo about agent skills rather than path tools), and
`claude-workspace-merge:15`, which inlined the char class in bash. Two are gone:
dotfiles' pair was deleted (`922d325`) once `claude-code-slug` shipped, and
`claude-workspace-merge` now calls `claude-path` (`b8559b5`). That is what a
package retires and a commit cannot.

The count stops at 2 rather than 1, and the survivor is not an oversight:
`bukzor-agent-skills` vendors its copy on purpose, so four skill scripts can
call it by relative path and the repo works standalone. Nobody working here can
drive this to 1.

### Drift by staleness, which is not a copy

Deduping by (origin, path) surfaced a failure mode neither relation had a name
for: **one tracked file, two checkouts, two encodings.** `dotfiles.git`'s
`bin/claude-path` classifies `LEGACY` in `~/repo/github.com/bukzor/dotfiles`
and `delegates` in `~`, with no edit between them -- the second checkout is
simply behind. It is not duplication, because there is one file; and it is not
the derived-key motion, because nothing was derived. It is a resolution
mechanism nobody chose: whichever checkout a caller's `PATH` happens to reach
decides which encoding runs. Filed against
`../coherence.kb/two-live-implementations-are-resolved-by-search-order.md`,
which gained a row for it.

## What would make this stale

Migrating any of the 34 keys, or retiring the last vendored implementation. Both
are good outcomes and both change these numbers, which is what `verify:` is for.
`--derived` exits nonzero on the 34; `--shadow` exits nonzero on the 2. The ship
already invalidated one version of this section, which is the argument for
keeping exhibits in files that say when they were measured.
