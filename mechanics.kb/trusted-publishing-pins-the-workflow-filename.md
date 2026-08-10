# PyPI trusted publishing pins the workflow filename

Verified 2026-08-10 while publishing `claude-code-slug 0.1.0`.

A PyPI trusted publisher is registered against a *repository, environment and
workflow filename*, and the OIDC claim GitHub mints carries that filename. PyPI
honors **no rename redirect**: rename the workflow after registering and the
next release fails to authenticate.

So the workflow file is the unit of authorization. Two consequences for this
workspace:

- **One registry per workflow file.** `release-pypi.yml`, not `release.yml` --
  a second registry (a private index, a container registry) gets its own file
  rather than another job in this one, because a job cannot hold fewer
  privileges than the file it lives in. This is bukzor's own written policy in
  `template.python-project/docs/dev/technical-policy.kb/least-privilege-grants.md`,
  and the first draft here violated it.
- **Rename before registering, never after.** Cheap in that order, a failed
  release in the other.

The distribution is *not* part of the grant: it rides in the tag
(`<dist>-v<version>`), so one workflow file releases every member of the
workspace and each member needs its own publisher registration. The file names
the registry; the tag names the package.

## The rehearsal this enables

`workflow_dispatch` on the same file, building a chosen member and skipping the
upload, mints a token at `pypi.org/_/oidc/mint-token`. That is the only way to
prove the registration works before burning a version, because TestPyPI's
publisher is a separate registration on a separate index. Filed as a claim in
`../bukzor-packaging.claims.kb/closure.kb/only-a-successful-publish-is-irreversible.md`.
