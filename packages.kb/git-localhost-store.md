---
status: shipped
home: bukzor-tools
language: mixed
---

# git-localhost-store

Relocates `.git` to a central store and leaves a symlink, so naive tools
that resolve `.git/HEAD` by path keep working. Shipped 2026-08-10 as
`bukzor-tools/packages/git-localhost-store`, out of the dotfiles repo.

## Why it graduated

It failed all three dotfiles tests at once, and AUDIENCE decisively (see
`../criteria.kb/graduation-from-dotfiles.md`):

- 49 files tracked in the dotfiles repo, including `README.md` (6.5KB),
  `CLAUDE.md` (8.2KB), `TESTING.md`, four ADRs under `docs/adr/`, a
  devlog, and its own `.claude/todo.kb/`. That apparatus *is* a project.
- Knowledge worth testing: hook recursion capping via
  `GIT_LOCALHOST_STORE_ACTIVE`, ref recovery merge, the gitfile→symlink
  layout migration that has its own ADR.
- Audience: anyone whose filesystem is slow or sync-hostile. Nothing about
  it is bukzor's config, yet it rode along to every dotfiles clone.

## The seam that was chosen

Not the one this file predicted. The catch recorded here was that a
`shared-scripts` payload is not re-exported by the meta-package
(`../mechanics.kb/bash-ships-via-shared-scripts.md`), so a bash tool
arrives via per-package install only, breaking the repo's one-install
promise. Porting looked like the expensive escape: 162 lines of git
plumbing, hooks that must be shell.

Grading it by *what each line decides* dissolved that. One line chooses a
store; the rest drive git. `cli.py` (Python, an entry point like any
other) imports `claude_code_slug`, computes the store, and `execve`s
`relocate.sh` with the workdir and store as arguments. `relocate.sh` stays
bash and computes no paths. `hook.sh` stays shell because git copies it.
The meta-package re-exports the console scripts the ordinary way, so
`shared-scripts` never entered it.

See `../refactors.kb/declare-the-encoder-in-git-localhost-store.md` for
why the encoder had to be *imported* and not merely installed.

## What packaging had to preserve

`${XDG_DATA_HOME:-$HOME/.local/share}/git-localhost-store/bin/git-localhost-store`
is baked into ~3000 hook files already on disk, copied at init time and
never re-read. A wheel lands in a venv, which is not a place git looks. So
the distribution carries a second entry point,
`git-localhost-store-install`, which writes the git template and aims that
one public path at whichever venv the package landed in. That indirection
is what lets a release change the relocator under repos initialized in
2025 -- with no sweep of the ~1000 existing stores.

The encoding is pinned by the same data: store directories exist under
`~/.local/state/git-localhost-store/repos/` named by it, so changing it
orphans repos rather than renaming them.

## Costs paid, and one not

- **bash tests**: dropped, not converted. `cli_test.py` replaces them,
  driving real git through real hooks with every XDG path and the git
  config redirected into `tmp_path`. The bash scripts wrote to `/tmp` and
  to the *real* store.
- **shellcheck hook**: still not in `bukzor-tools/.pre-commit-config.yaml`.
  The two shell files are checked by hand. Real gap.
- **Distribution**: `uv tool install bukzor-tools` now puts a git tool on
  every machine, and its hooks do nothing until
  `git-localhost-store-install` runs. Deliberate: installing is not
  arming.

## Objection considered and rejected

"It has a repo's apparatus, so give it a repo." That's the `bukzor-tools`
README's own first sentence in reverse: 189 lines of shell is "too small
for their own repos". A repo would cost a CI workflow, a release workflow,
and a PyPI decision for a tool that gets one commit a quarter. Graduation
stays available -- the packages are independently buildable.
