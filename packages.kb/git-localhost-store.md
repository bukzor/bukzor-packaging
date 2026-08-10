---
status: proposed
home: bukzor-tools
language: bash
---

# git-localhost-store

Relocates `.git` to a central store and leaves a symlink, so naive tools
that resolve `.git/HEAD` by path keep working. Currently at
`~/.local/share/git-localhost-store/`, tracked in the dotfiles repo.

## Why it graduates

It fails all three dotfiles tests at once, and AUDIENCE decisively (see
`../criteria.kb/graduation-from-dotfiles.md`):

- 49 files tracked in the dotfiles repo, including `README.md` (6.5KB),
  `CLAUDE.md` (8.2KB), `TESTING.md`, four ADRs under `docs/adr/`, a
  devlog, and its own `.claude/todo.kb/`. That apparatus *is* a project.
- Knowledge worth testing: hook recursion capping via
  `GIT_LOCALHOST_STORE_ACTIVE`, ref recovery merge, the gitfile→symlink
  layout migration that has its own ADR.
- Audience: anyone whose filesystem is slow or sync-hostile. Nothing about
  it is bukzor's config, yet it rides along to every dotfiles clone.

Shape: `bin/git-localhost-store` (162 lines bash), `lib/init` (27),
`template-repo/hooks/`, and two bash test scripts
(`test-empty-commit`, `test-reference-transaction`).

## Feasibility, and the catch

`bukzor-tools` can ship bash today with no new toolchain -- verified. But a
`shared-scripts` payload is **not** re-exported by the meta-package, and the
meta install fails outright when it has no entry points of its own. So a
bash `git-localhost-store` arrives via `uv tool install
./packages/git-localhost-store` only, breaking the repo's one-install
promise. See `../mechanics.kb/bash-ships-via-shared-scripts.md`.

Unlike `claude-slug`, porting is not the escape hatch: 162 lines of git
plumbing, hooks that must be shell, and two bash test scripts. The options
are per-package install (acceptable, mildly inconsistent) or a Python
trampoline entry point in the meta-package that `execv`s the shared script
(untested, and the meta currently declares it has no code via
`bypass-selection = true`).

This is the strongest remaining argument for giving it its own repo instead.

## Dependency

`bin/claude-path` at line 33: `ENCODED="$(claude-path "$WORK_DIR")"`,
reached by absolute symlink into `~/bin`. Must become a dependency on
`claude-slug`.

The encoding cannot simply be replaced with a local one: store directories
already exist under `~/.local/state/git-localhost-store/repos/` using it
(e.g. `-home-bukzor-tmp-test--git--localhost`), so changing the encoding
orphans every relocated repo. The dependency is pinned by data on disk.

## Costs not yet paid

- **shellcheck hook** -- `bukzor-tools/.pre-commit-config.yaml` has five
  hooks (pyupgrade, isort, black, pyright, pytest), none for shell.
- **bash tests won't run under pytest.** Either a pytest wrapper that
  shells out, or convert them. This is the one real integration cost, and
  it's the reason to land `claude-slug` first as the cheap bash trial.
- Whether `uv tool install bukzor-tools` should put a git tool on every
  machine. Probably yes -- but it's a distribution decision, so name it.

## Objection considered and rejected

"It has a repo's apparatus, so give it a repo." That's the `bukzor-tools`
README's own first sentence in reverse: 189 lines of shell is "too small
for their own repos". A repo would cost a CI workflow, a release workflow,
and a PyPI decision for a tool that gets one commit a quarter.
