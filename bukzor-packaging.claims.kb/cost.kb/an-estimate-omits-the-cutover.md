---
label: CUTOVER
standing: agent
authority: >-
    found by the session that shipped claude-code-slug, 2026-08-10: the hour
    estimated covered the package and not the git-localhost-store symlink
    retarget, which was load-bearing
why:
    - cost-splits-into-site-and-item.md
    - ../graduation.kb/separable-is-a-prediction-until-extracted.md
---

# An Estimate Omits the Cutover

Carrier: a migration -- building a replacement for something already in use.
Its cost has a term that estimates systematically miss:

> *c* = *c*<sub>build</sub> + *c*<sub>cutover</sub>, where the cutover is every
> edit needed to make existing dependents point at the new thing.
>
> **Estimates are written against the artifact and omit the cutover**, because
> the artifact is what the author is imagining and the dependents are
> elsewhere.

The asymmetry is not random. *c*<sub>build</sub> is bounded by a thing you can
see; *c*<sub>cutover</sub> is proportional to how well the old arrangement was
adopted -- so **the more successful the thing being replaced, the larger the
omitted term.**

## Smallest instance

`../../packages.kb/claude-code-slug.md` estimated "a `pyproject.toml`, two
entry points, a meta-package row, a README row, and the port itself -- call it
an hour." Actual: about an hour for that list, and the list was incomplete.

Missing: two steps that keep `git-localhost-store` working. It calls
`claude-path` as a bare command on *every* hook firing, at line 33, before the
`[ -L .git ]` early exit -- so **the install had to land before the deletion, or
`git commit` fails in roughly fifty repositories.** And its own `bin/` carried an
absolute symlink to the old file, which had to be retargeted or its test harness
breaks. Both were unbudgeted; neither is visible from the package.

Note what makes it the instance rather than an anecdote: the same file *already*
identified that dependency, in a section arguing for the package. The cutover was
known and still not costed. Knowing about a dependent is not the same as pricing
the edit it needs.

There is a second-order finding here, worth more than the first. The initial
write-up of this instance named the symlink as the severe step and the PATH
continuity as incidental; it was the reverse. **A cutover term guessed after the
fact is not merely low -- its parts arrive mis-ranked**, because severity lives
in how the dependent *names* what it needs, and nobody re-reads the dependent
while estimating.

## What follows for the site/item split

`cost-splits-into-site-and-item.md` reads *c*(*S*) = *F* + Σ*m*(*t*), and both
terms are build costs. Cutover attaches to neither: it scales with the
dependents of the *old* arrangement, which is a property of the world rather
than of the package. Two consequences worth carrying:

- The split understates the cost of replacing anything load-bearing, and
  understates it worst exactly where packaging is most valuable.
- A cutover cost is a one-time payment that also *removes* a class of failure,
  so it belongs in the numerator too. This claim is not "estimates are too
  low"; it is "one term is missing from both sides".

## What would kill it

A greenfield population. Where nothing depends on the old arrangement -- a tool
with no callers, a fact with one implementation -- the cutover term is zero and
this claim is noise. That is the common case for a *new* tool
(`../genesis.kb/`) and the rare case for a *package*, which is why it is filed
here and not there.
