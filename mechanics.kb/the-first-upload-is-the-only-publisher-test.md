# Only the upload tests a *new* project's publisher

Verified 2026-08-10 publishing `git-localhost-store 0.1.0` from
`bukzor-tools`, where `claude-code-slug` was already registered on the same
workflow.

The `workflow_dispatch` rehearsal in `release-pypi.yml` mints an OIDC token
and calls it proof that the publisher accepts us. The request is:

```sh
curl -sS -X POST https://pypi.org/_/oidc/mint-token -d "{\"token\": \"$jwt\"}"
```

**No project name is in it.** PyPI answers for the identity
`(owner, repo, workflow, environment)`, and one registered project is enough
to mint. So the dispatch came back green for `git-localhost-store` while that
project had no publisher at all, and the tagged run then failed at upload:

```
400 Non-user identities cannot create new projects. This was probably caused
by successfully using a pending publisher but specifying the project name
incorrectly (either in the publisher or in your project's metadata).
```

That message is also misleading -- nothing was misspelled; the pending
publisher simply did not exist.

## Which is cheap, so publish and find out

Registering the pending publisher and then `gh run rerun <run-id>` published
it. **The tag did not need to move**: rerun replays the same ref, so a bounced
first upload burns nothing -- not the version, not the tag, not the name.

For a first release, then: review the metadata before tagging (it is
immutable), and let the upload itself answer the publisher question. The
rehearsal still earns its keep for everything upstream of the upload -- the
build, the tag/version agreement -- and for confirming a *second* package on
an already-working workflow, which is the case where the token really is
scoped to something you have.

See `trusted-publishing-pins-the-workflow-filename.md` for what the grant
binds, and
`../bukzor-packaging.claims.kb/closure.kb/only-a-successful-publish-is-irreversible.md`
for the guard-placement claim this is the smallest instance of.
