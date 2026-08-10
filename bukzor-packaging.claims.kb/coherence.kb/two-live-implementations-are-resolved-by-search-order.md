---
label: SHADOW
standing: bare
why:
    - a-derived-key-must-be-recomputed-or-checked.md
    - ../seams.kb/two-implementations-are-one-node-only-after-merging.md
verify: ../coherence.py --shadow
---

# Two Live Implementations Are Resolved by Search Order

Carrier: a fact with more than one implementation, and the callers that reach
one of them. Law:

> When *n* > 1 implementations of one fact are installed, **which one a caller
> gets is a property of how the caller was invoked, not of the program.** No
> declaration ranks them; the resolution mechanism does, silently, and
> different callers can use different mechanisms.

That is the deployment-side counterpart of
`../seams.kb/two-implementations-are-one-node-only-after-merging.md`: that
claim says duplicated knowledge is not an edge in the code graph; this one
says the runtime does not repair the omission -- it silently picks.

The mechanisms are worth enumerating because they are not interchangeable, and
a system usually has several at once:

| mechanism | binds to | who can change it |
|---|---|---|
| `PATH` lookup | whatever comes first | the environment, per shell |
| sibling-of-`$0` resolution | one file's neighbour | whoever moves the file |
| an absolute symlink | one literal path | whoever installed it |
| an inlined copy | itself, always | nobody, and it cannot be told |
| **a second checkout of one tracked file** | whatever that clone last pulled | whoever forgets to pull |
| a declared dependency | one version, resolved once | the lockfile |

Only the last is a decision anyone made. Two of them deserve a warning:
inlining is the worst *and* the one that looks safest locally, because it
cannot disagree with itself; and the second-checkout row is the one that
defeats "there is only one implementation" -- one file can hold two encodings
at once if two clones sit at different commits, with no edit anywhere.

## Smallest instance

One path encoding, which over one day went from three independent
implementations (one of them untracked, with the committed substitute
implementing the *previous* encoding) to two, by way of a package. Exhibit:
`../case-study.kb/the-store-key-encoding-has-drifted-twice.md`.

The remaining copy is the interesting one, because it is not an oversight:
`bukzor-agent-skills` vendors `bin/claude-slug` and four of its skill scripts
call it by explicit relative path so the repo works standalone. That is a
deliberate choice by a different repo, and it means this claim's population
cannot be driven to one by anybody working here. **Search order stops deciding
only when every caller declares a dependency, and a caller who wants to work
standalone is refusing to.**

The honest site deserves its own mention as a pattern: a Python module that
documents the encoding *in prose* because it has no way to call a bash script it
cannot depend on. Prose is a resolution mechanism too -- the reader is the
resolver -- and it is the least reliable one available.

## Three independent properties, discovered one at a time

The same fact was fixed twice in one day, and each fix repaired a *different*
property while leaving the others alone. They are worth naming separately
because a check written for one silently stops answering when the situation
moves:

| property | question | fixed by |
|---|---|---|
| clone fidelity | does a fresh checkout reproduce the behaviour? | committing the file |
| provenance | is the command a versioned artifact or a loose file? | packaging it |
| resolution | which of *n* implementations does a caller get? | retiring the rest |

Committing the untracked encoder fixed fidelity and changed neither of the
others. Packaging it fixed provenance -- the command on `PATH` is now a console
script beside a `pyvenv.cfg`, which is a declared, versioned dependency -- and
*also* retired two of three implementations, which is progress on resolution
but not completion: one vendored copy remains in another repo, so `PATH` order
still decides.

The instructive part is that the middle question did not exist until the second
fix, and the first fix's check *died* of it: a predicate demanding that the
dotfiles repo contain the encoder became permanently false the moment the
encoder correctly left. **A check phrased against the current arrangement
expires when the arrangement improves.** Phrase it against the property.

## Why packaging is the fix and not just a tidy-up

An importable function has exactly one resolution mechanism -- the dependency
graph -- and it is declared, versioned, and checkable. That is the whole
argument for `claude-slug` as a package rather than a helper, and it is why
`packages.kb/claude-slug.md` insists on a Python port: bash offers no import,
so a bash `claude-slug` would leave every mechanism in place and merely reduce
the copy count.

The symlink deserves its own sentence. It looks like a dependency and is not:
it survives only because both ends live in one dotfiles repo, so packaging
either end breaks it. Replacing it with a `dependencies` row is the *point*
of the exercise, not a side effect.

## What would kill it

A single implementation with one resolution mechanism -- which is what the
port delivers, so this claim is designed to become false. Until then, the
check is the only thing standing between three implementations and a fourth.
