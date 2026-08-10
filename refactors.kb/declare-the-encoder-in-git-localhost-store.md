---
status: proposed
---

# Declare the encoder in git-localhost-store

`git-localhost-store` line 33 is `ENCODED="$(claude-path "$WORK_DIR")"`. Since
2026-08-10 that command comes from the `claude-code-slug` package, and nothing
anywhere says so. The edge is real, load-bearing on data already on disk, and
undeclared.

## Why it is not done already

There is nowhere to write it. A dependency is declared in a `pyproject.toml`,
and `git-localhost-store` has none -- it is 189 lines of shell tracked in the
dotfiles repo. **This refactor is blocked on packaging its consumer**
(`../packages.kb/git-localhost-store.md`), which has its own unpaid costs: a
shellcheck hook, bash tests that will not run under pytest, and the
`shared-scripts` re-export problem.

Retargeting the symlink in its `bin/` was the only move available on ship day,
and it fixes a smaller thing than it appears to: that directory is on PATH only
when the test harness prepends it, so the symlink pins the *tests*.

## What would settle it

`packages/git-localhost-store/pyproject.toml` carrying
`dependencies = ["claude-code-slug"]` plus a `[tool.uv.sources]` workspace row.
Then `uv tool install ./packages/git-localhost-store` provisions `claude-path`
into the same environment as the hook, and the dependency is versioned, declared,
and checkable.

## The part that does not follow, and is the reason to write this down

**A declared dependency fixes provisioning, not selection.** The hook still says
`claude-path`, so PATH still decides which `claude-path` answers -- and the first
entry on this machine's PATH is `~/bin`, the directory the encoder was just
deleted from. Declaring the dependency guarantees that *a* correct encoder is
installed; it does not guarantee it is the one that runs.

That is the coherence cube again
(`../bukzor-packaging.claims.kb/coherence.kb/two-live-implementations-are-resolved-by-search-order.md`):
provenance and resolution are independent, and bash can only buy the first.
Three ways to buy the second, in increasing cost:

- **call it by resolved path.** The hook computes its own location already; a
  sibling-of-`$0` lookup binds to the installed environment. Cheap, and swaps
  PATH order for "whoever moves the file" -- a better mechanism, not a declared
  one.
- **pin in the hook's own template.** `template-repo/hooks/` is generated at
  install time, so it could bake an absolute path. Machine-specific by
  construction, which is the defect the symlink already has.
- **port the hook to Python** and `import claude_code_slug`. The only option
  that makes resolution declared, and rejected on its own merits in
  `../packages.kb/git-localhost-store.md`: 162 lines of git plumbing, and hooks
  that must be shell.

Recommendation: declare the dependency and take the resolved-path lookup. It
leaves one mechanism in place instead of two and stops depending on the order of
a user's PATH, which is the property actually at issue.
