---
status: done
---

# Declare the encoder in git-localhost-store

`git-localhost-store` needs a path encoder, and the store directories
already on disk are *named* by whichever one runs. Since 2026-08-10 a
correct one ships as `claude-code-slug`. The question this file settles is
not where it comes from but which one answers.

Settled 2026-08-10 by `packages/git-localhost-store` in `bukzor-tools`:
`pyproject.toml` declares `dependencies = ["claude-code-slug"]`, and
`cli.py` says `from claude_code_slug import path_slug`.

## The distinction that made it worth writing down

**A declared dependency fixes provisioning, not selection.** The old call
site was `ENCODED="$(claude-path "$WORK_DIR")"` -- a bare command, so PATH
decided, and the first entry on this machine's PATH is `~/bin`. Declaring
the dependency guarantees *a* correct encoder is installed; it does not
guarantee it is the one that runs. That is the coherence cube
(`../bukzor-packaging.claims.kb/coherence.kb/two-live-implementations-are-resolved-by-search-order.md`):
provenance and resolution are independent axes.

The failure mode is why it mattered: a wrong encoder does not error. It
names a *second* store for a repository that already has one, and the
commits carry on into a directory nobody looks in.

## What was chosen, over what this file first recommended

Three options were weighed here, and the recommendation was the cheapest:
a sibling-of-`$0` lookup in bash. Porting to Python was rejected on
volume -- "162 lines of git plumbing, and hooks that must be shell".

That rejection graded the tool as one artifact. Split by *what each line
decides*, the volume argument evaporates: exactly one line chooses a
store, and the other 161 drive git. So the seam went between them.
`cli.py` imports the encoder, computes the store, and `execve`s
`relocate.sh` with the workdir and store as arguments; `relocate.sh` stays
bash, computing no paths of its own. `hook.sh` is unchanged and still
shell, because git requires that.

An import cannot resolve to the wrong encoder -- it binds to the venv the
package was installed into. The sibling-of-`$0` lookup would have bought a
weaker property (whoever moves the file wins, instead of whoever ordered
PATH) for a comparable edit.

## What it cost

Less than the packaging entry predicted. The `shared-scripts`
re-export problem never came up: the entry points are Python, so the
meta-package re-exports them the ordinary way. No shellcheck pre-commit
hook was added -- `relocate.sh` and `hook.sh` are checked by hand, and
that gap is real.

The two bash test scripts were dropped rather than converted. Their
replacement, `cli_test.py`, drives real git through real hooks with every
XDG path and the git config redirected into `tmp_path` -- which the bash
scripts never did, and which is the property that matters when a test
failure would edit the repositories this tool exists to protect.
