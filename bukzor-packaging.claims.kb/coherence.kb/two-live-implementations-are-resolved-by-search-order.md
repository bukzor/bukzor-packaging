---
label: SHADOW
standing: bare
why:
    - a-derived-key-must-be-recomputed-or-checked.md
    - ../seams.kb/two-implementations-are-one-node-only-after-merging.md
verify: ../coherence.py --shadow
---

# Two Live Implementations Are Resolved by Search Order

The encoding has two implementations in `~/bin`, and **three different
mechanisms** decide which one a given caller gets:

| caller | mechanism | what it binds to |
|---|---|---|
| a shell, a hook, a person | `PATH` lookup among 19 directories | whichever `claude-slug` comes first |
| `claude-path` | `$(dirname "$(realpath "$0")")/claude-slug` | its own sibling, ignoring `PATH` |
| `git-localhost-store` | absolute symlink `bin/claude-path -> ~/bin/claude-path` | one literal path, ignoring both |
| `claude-workspace-merge:15` | nothing -- it has its own copy | itself, always |

No declaration anywhere states which implementation is authoritative. The
answer is a function of *how the caller was invoked*, which is not a fact
about the program.

That is the deployment-side counterpart of
`../seams.kb/two-implementations-are-one-node-only-after-merging.md`: that
claim says duplicated knowledge is not an edge in the code graph; this one
says the runtime does not repair the omission -- it silently picks.

## Smallest instance

`claude-workspace-merge:15` carries the char class `[^A-Za-z0-9]` inline, as
a `claudepath()` bash function. It cannot disagree with itself, and it will
disagree with `claude-slug` the moment either is edited -- with no error, no
warning, and no test. There is a fourth site that is honest about the
problem: `claude_code_archeology.session.cwd()` documents the encoding *in
prose*, because as a Python module it has no way to call a bash script it
cannot depend on.

Four sites, one fact, zero declarations. And per
`a-derived-key-must-be-recomputed-or-checked.md`, the divergence has already
happened once at a scale nobody noticed.

## Why packaging is the fix and not just a tidy-up

An importable function has exactly one resolution mechanism -- the dependency
graph -- and it is declared, versioned, and checkable. That is the whole
argument for `claude-slug` as a package rather than a helper, and it is why
`packages.kb/claude-slug.md` insists on a Python port: bash offers no import,
so a bash `claude-slug` would leave the three mechanisms in place and merely
reduce the copies from two to one.

The symlink deserves its own sentence. It looks like a dependency and is not:
it survives only because both ends live in one dotfiles repo, so packaging
either end breaks it. Replacing it with a `dependencies` row is the *point*
of the exercise, not a side effect.

## What would kill it

A single implementation with one resolution mechanism -- which is what the
port delivers, so this claim is designed to become false. Until then, the
check is the only thing standing between four sites and a fifth.
