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
| an inline script dependency (PEP 723) | one requirement, resolved per run | the script's own header |
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

The remaining copy looked like the interesting one, because it was not an
oversight: `bukzor-agent-skills` vendored `bin/claude-slug` and four of its skill
scripts call it by explicit relative path so the repo works standalone. I drew a
tradeoff from that and wrote: *"search order stops deciding only when every
caller declares a dependency, and a caller who wants to work standalone is
refusing to."*

**That is false, and the same day it was published to PyPI the copy was
retired.** `bukzor-agent-skills/bin/claude-slug` is now
`#!/usr/bin/env -S uv run --script` with `dependencies = ["claude-code-slug"]` in
a PEP 723 header (`ba513bc`). The script is standalone in the sense that
mattered -- clone the repo, run the file, no install step and no environment to
manage -- *and* it names a versioned dependency that a resolver honors. The
tradeoff I asserted between standing alone and declaring a dependency was an
artifact of assuming bash. **Ask what makes standalone-ness necessary before
concluding that duplication buys it.**

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
`../../packages.kb/claude-code-slug.md` insisted on a Python port: bash offers no
import, so a bash `claude-slug` would leave every mechanism in place and merely
reduce the copy count. Carried out 2026-08-10, and `claude-path`'s `exec` of its
sibling is now an import.

## One consumer, two mechanisms, and the one that looked like the problem

`git-localhost-store` is worth reading closely, because the obvious defect is
not the live one. It calls the encoder **as a bare command** --
`ENCODED="$(claude-path "$WORK_DIR")"`, line 33 -- on every hook firing in every
relocated repo. That is row one of the table: PATH decides, per shell, and the
first entry wins. Separately, its own `bin/` holds an absolute symlink to a
`claude-path`, and that directory is on PATH **only when its test harness
prepends it** (`docs/dev/testing.kb/CLAUDE.md:37`).

So the two mechanisms partition by audience: **production is unpinned, and the
tests are pinned to a machine-specific location.** Two defects, two fixes, and
only the second one is a symlink. The correction that produced this section had
the blast radii backwards -- a dangling symlink there breaks the test harness,
while what would break `git commit` in roughly fifty repositories is
`claude-path` missing from PATH.

And the symlink is not really a *fifth* mechanism: it is the content of a
directory that something else injects into PATH. **Mechanisms compose, and the
composition is what decides** -- which is why a claim about "the symlink" was
answering the wrong question, and why the check now prints the call site.

The live hazard the corrected check surfaces is neither of those: the first
entry on PATH is `~/bin`, the directory the encoder was just deleted from. Any
file that reappears there silently wins in every hook firing
(`../../mechanics.kb/path-shadowing-blocks-migration.md`).

## What would kill it

A single implementation reached by a declared dependency. The port halved the
count and fixed provenance, and the remaining gap is now named as work rather
than as a caveat: `../../refactors.kb/declare-the-encoder-in-git-localhost-store.md`,
blocked on packaging its consumer. That is the shape a claim takes on its way
out, and the reason `--shadow` counts sites rather than asserting a state.
