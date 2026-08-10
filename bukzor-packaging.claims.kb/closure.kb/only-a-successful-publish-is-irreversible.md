---
label: PUBLISH
standing: agent
authority: >-
    found by the session that published claude-code-slug 0.1.0 to PyPI,
    2026-08-10, which rehearsed the release with a dispatch build that stopped
    short of upload
why:
    - a-guard-names-a-reversal-cost.md
    - ../cost.kb/an-estimate-omits-the-cutover.md
---

# Only a Successful Publish Is Irreversible

Carrier: an action against a registry that refuses to forget. Law:

> A **failed** publish costs nothing: no artifact is uploaded, the version
> number is not burned, and the same tag is re-runnable. A **successful** one is
> irreversible: the version can never be re-uploaded, and deleting it does not
> free the name.
>
> So the reversal cost of an *attempt* is zero and the reversal cost of a
> *success* is infinite. **The guard belongs at the success boundary, and
> rehearsals should be exhaustive because they are free.**

`a-guard-names-a-reversal-cost.md` says a guard is earned when reversing costs
more than acting. This is the sharpest instance available: the two costs are not
merely different, they are zero and infinite, and they sit one step apart in the
same pipeline. Everything upstream of the upload should be rehearsed; everything
that must be right *at* the upload should be reviewed before the first tag.

## What that reorders

Metadata review moves **before** the first tag rather than after the first
release. Name, version, license, classifiers, README rendering -- these are
exactly what cannot be re-uploaded, so reviewing them post-hoc reviews something
you can no longer change. A second release can add a file; it cannot rename the
first one.

## Smallest instance

`claude-code-slug 0.1.0`. The rehearsal was a `workflow_dispatch` run that
builds any workspace member, **skips the upload**, and mints an OIDC token at
`pypi.org/_/oidc/mint-token` -- which proves the trusted publisher is registered
and the workflow's identity matches, the one thing that actually fails on a
first release. It ran green before the tag existed.

The instructive part is what it replaces. A TestPyPI dry run cannot test this:
TestPyPI's publisher is a **separate registration on a separate index**, so a
green TestPyPI upload says nothing about whether the real one will authenticate.
The rehearsal that matters is on the real registry, stopping one step short of
the irreversible one -- which is the general shape this claim recommends, not a
detail about PyPI.

## What would kill it

A registry with a retraction that restores the name and the version -- then
attempt and success have comparable reversal costs and the guard should move.
Yanking is not that: a yanked version stays taken. A pre-release channel is not
that either, unless the same registration governs both, which is precisely what
TestPyPI is not.
