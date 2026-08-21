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

`git-localhost-store 0.1.0`, 2026-08-10. The tag was pushed with the
publisher unregistered; the upload bounced with `400 Non-user identities
cannot create new projects`. Registering the pending publisher and running
`gh run rerun <id>` published it -- **same tag, same run, no version
burned**. The attempt's reversal cost was not merely small, it was zero,
measured.

The instructive part is what a rehearsal could *not* do here. The
`workflow_dispatch` build that stops one step short and mints an OIDC token
at `pypi.org/_/oidc/mint-token` ran **green** minutes before that bounce:
the mint request carries only the token, no project name, so PyPI answers
for the identity and one already-registered sibling is enough. See
`../../mechanics.kb/the-first-upload-is-the-only-publisher-test.md`.

That does not weaken the law -- it relocates the guard. Rehearse everything
a rehearsal can actually decide, and accept that the publisher question for
a *new* project is answered only by the attempt. Which is fine, because the
attempt is free; the cost is entirely in the metadata you cannot re-upload.

A TestPyPI dry run is no help either: its publisher is a **separate
registration on a separate index**, so a green TestPyPI upload says nothing
about whether the real one authenticates.

## What would kill it

A registry with a retraction that restores the name and the version -- then
attempt and success have comparable reversal costs and the guard should move.
Yanking is not that: a yanked version stays taken. A pre-release channel is not
that either, unless the same registration governs both, which is precisely what
TestPyPI is not.
