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

## The encoding is frozen, and the port must not improve it

The encoding changed once already, around 2026-07-05, when a rewrite of
`~/bin/claude-path` delegated to the then-new `claude-slug`. Old:
`-` → `--`, `/` → `-`, dots verbatim. New: every non-alnum → one `-`. That
rewrite sat **uncommitted for five weeks** and was tracked 2026-08-10
(`c879ca1`, `d983aad` in dotfiles) after the check below reported that a fresh
clone would still get the old encoder. Written up in
`~/.claude/sessions.kb/penguin/claude-path-encoding-change-orphans-stores.md`;
migrating the affected stores was priced and **declined**, and GLS's own
`.claude/todo.md` carries the reconciliation item.

Measured 2026-08-10 across worktrees under `~/repo`, `~/claude`, `~/.claude`,
`~/empty`, `~/trash`: **53 relocated worktrees, 19 keys matching today's
encoder, 31 carrying the legacy encoding, 3 keyed under a path the workdir has
since left.** Nothing is broken today, because GLS exits at `[ -L .git ]`
(line 41) before it would recompute -- so the encoding is consulted only when a
store is *created or recovered*.

Preconditions for this package, not polish:

- **port faithfully to today's encoder and stop there.** The encoding is
  frozen; "fixing" it a second time would orphan the 19 that currently agree.
- **preserve the early exit.** A packaged `claude-path` that eagerly recomputes
  keys converts 34 dormant mismatches into 34 empty stores -- the failure the
  session note calls "the system's whole purpose failing quietly".
- **ship the check with the encoder.** Walk worktrees, re-derive, report. A
  working prototype is `coherence.py --derived` in the claims directory; its
  job is to bound a decision already taken, not to reopen it.
- **retire the other two implementations, don't just add a third.** `--shadow`
  counts three independent tracked implementations today. A package that leaves
  `bukzor-agent-skills/bin/claude-slug` and `claude-workspace-merge:15` in place
  makes it four.

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

- `~/bin/claude-workspace-merge:15` -- a second implementation, inlined as
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
