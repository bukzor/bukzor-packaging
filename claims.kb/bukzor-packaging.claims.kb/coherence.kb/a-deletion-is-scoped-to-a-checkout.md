---
label: CHECKOUT
standing: agent
authority: >-
    found by the session that published claude-code-slug 0.1.0, 2026-08-10,
    reading --shadow output: a LEGACY implementation of the encoding was still
    on disk in a second clone of dotfiles after the deletion was committed
why:
    - two-live-implementations-are-resolved-by-search-order.md
    - ../cost.kb/an-estimate-omits-the-cutover.md
verify: ../coherence.py --shadow
---

# A Deletion Is Scoped to a Checkout, Not to a Repo

Carrier: a file retired from a repository, and the clones of that repository.
Law:

> `git rm` plus a commit removes the file from **one working tree**. Every other
> checkout keeps it until someone pulls, and a checkout nobody pulls keeps it
> forever.
>
> So **retirement is not a repo-level event**, and a count of implementations
> taken over a repo is not a count of what is on disk.

This is the deletion-side twin of the stale-checkout row in
`two-live-implementations-are-resolved-by-search-order.md`. That row says one
tracked file can hold two encodings when two clones sit at different commits.
This says the same mechanism survives the file's *removal*: deleting one copy
does not delete the others, and the surviving copies are invisible to anyone
reasoning from `git log`.

## Smallest instance

`bin/claude-path` was deleted from dotfiles (`922d325`) as part of shipping
`claude-code-slug`, and it is still on disk at
`~/repo/github.com/bukzor/dotfiles/bin/claude-path:12`, implementing the
**pre-2026-07-05** encoding -- the one that orphans stores. Nothing has broken,
because nothing puts that `bin/` on PATH. But the deletion was performed and
believed complete while a LEGACY implementation remained in a directory the
deleter had open.

The cutover reasoned about `$HOME`, which *is* the dotfiles working tree, and
not about other clones of `$HOME`. That is the specific blind spot: the
authoritative checkout is the one you are standing in, and it is the one whose
state you mistake for the repo's.

## What this does to the sibling claims

- **CUTOVER gains a term.** `../cost.kb/an-estimate-omits-the-cutover.md` prices
  the edits dependents need. Clones are dependents nobody names, and their edit
  is a pull -- cheap individually, invisible collectively, and not schedulable
  by the person doing the cutover.
- **The check had to change to state this.** Counting sources by (origin, path)
  makes two checkouts one copy, which is right for duplication and wrong for
  deletion: it hides the surviving file entirely. `--shadow` now reports
  propagation separately and *directionally*, because `git log -- <path>`
  distinguishes a checkout that deleted the file from one that never had it.
  Only the first is a retirement someone believed was finished.
- **It is not a design defect**, and the exit code says so. A stale clone
  converges on a pull; a second implementation does not converge on anything.
  Conflating them made the check unable to reach zero, which is the failure mode
  described in that claim's "a check phrased against the current arrangement"
  paragraph -- reached this time from the other direction.

## What would kill it

A single-checkout world, or a deletion mechanism that reaches clones -- a
server-side hook that rewrites working trees, or a package manager that owns the
file so removal is an uninstall rather than a commit. **Packaging is exactly
that mechanism**, which is the interesting part: an installed distribution has
one copy per environment and `uv tool upgrade` removes what the version no
longer ships. A file in a dotfiles repo has one copy per clone and no way to
retire any of them.
