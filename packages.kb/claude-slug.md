---
status: proposed
home: bukzor-tools
language: python
---

# claude-slug

The smallest useful package in the plan, and the one two others depend on.

Current members, to be **ported, not moved** (see below):

- `~/bin/claude-slug` (12 lines) -- `perl -CSD -pe 's/[^A-Za-z0-9]/-/g'`
- `~/bin/claude-path` (23 lines) -- path normalization, then delegate

## Seam

One reverse-engineered fact: Claude Code's `projects/<slug>/` naming maps
**every** non-`[A-Za-z0-9]` character to exactly one `-` -- no run
squeezing, no case folding. `claude-path` adds path semantics
(`realpath -Lm`, absolute vs relative); `claude-slug` deliberately has
none, so it's safe on titles.

The pair is a package rather than a helper because it has two unrelated
consumers that must not disagree:

- `git-localhost-store` names its store directories with it
- `claude-code-archeology` must never *invert* it, and documents why

## Why it can't stay ambient

`git-localhost-store` currently reaches it by absolute symlink:
`~/.local/share/git-localhost-store/bin/claude-path -> ~/bin/claude-path`.
That's an undeclared runtime dependency on `~/bin` being present, which
survives only because both live in one dotfiles repo. Package the consumer
and the symlink becomes a real dependency edge or a broken install.

Live evidence, captured while creating this kb: `git init` here triggered
GLS, which computed `-home-bukzor-claude-bukzor-packaging-kb` and relocated
`.git` there. The encoding is load-bearing for data already on disk.

## Port to Python, don't ship the bash

Decided by mechanics, not taste: a `shared-scripts` bash payload is
invisible to the meta-package re-export, so a bash `claude-slug` would not
arrive via `uv tool install bukzor-tools`, and
`claude_code_archeology` could not import it -- only shell out to a command
that might not be installed. See
`../mechanics.kb/bash-ships-via-shared-scripts.md`.

As Python it gets all four properties at once: a console entry point per
command, meta-package re-export, an importable function for archeology, and
doctests.

The port is faithful and shrinks the dependency set: `perl -CSD` sets
stdin/stdout to UTF-8 so the substitution is per *character*, which is what
`re.sub(r"[^A-Za-z0-9]", "-", s)` does on a `str`. Dropping perl is a bonus.

`claude-path`'s `realpath -Lm` semantics (normalize without resolving
symlinks, tolerate nonexistent paths) map to `os.path.normpath` on an
absolutized path -- **not** `Path.resolve()`, which follows symlinks. That
difference is worth a doctest, since getting it wrong silently changes which
store directory GLS picks for a symlinked worktree.

## Duplication it would collapse

- `~/bin/claude-workspace-merge:12` -- a second implementation, inlined as
  a `claudepath()` bash function
- `~/bin/claude-jsonl-path` -- a consumer (calls `claude-path`), correct
  today, one edit away from becoming a third copy
- `claude_code_archeology.session.cwd()` -- documents the fact in prose
  because it can't import it

## Cost

A `pyproject.toml`, two entry points, a meta-package row, a README row, and
the port itself -- call it an hour. No shellcheck hook needed, since nothing
here stays bash.

Open naming question: `claude-slug` is a command name and would be the dist
name, but the package's subject is *the encoding*, and `claude-path` is the
command most callers want. Don't settle this by which file is smaller.
