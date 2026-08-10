---
status: shipped
home: bukzor-tools
language: python
---

# claude-code-slug

**Shipped 2026-08-10** as `claude-code-slug` in `bukzor-tools` (`aa7535b`),
module `claude_code_slug`: `slug()`, `normalize()`, `path_slug()`,
`logical_cwd()`. The smallest package in the plan, the one two others depend
on, and the first to be built on this kb's reasoning rather than filed by it.

Members, **ported not moved**, then deleted from `~/bin` (`922d325`):

- `~/bin/claude-slug` (12 lines) -- `perl -CSD -pe 's/[^A-Za-z0-9]/-/g'`
- `~/bin/claude-path` (23 lines) -- path normalization, then delegate

## The name, settled

The file's own open question was whether to name the dist for `claude-slug`
(the smaller file), `claude-path` (the command most callers want), or the
subject. **The subject won: the package is the encoding, and the two commands
are two views of it, neither name covering the other.** Same call
`claude-code-archeology` makes, which is the argument for consistency rather
than for either command.

The instruction "don't settle this by which file is smaller" survived contact,
which is the only reason it was written down.

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
  counted three independent tracked implementations. **Two retired:** dotfiles'
  pair deleted (`922d325`), and `claude-workspace-merge`'s inline
  `claudepath()` now calls `claude-path` (`b8559b5`). One remains and is
  another repo's call -- `bukzor-agent-skills` vendors `bin/claude-slug` and
  four skill scripts invoke it by explicit relative path so the repo works
  standalone. The check stays red at 2 on purpose.

All four were met. The record of *how* is below, kept because a precondition
that turns out to be unnecessary is as informative as one that binds.

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

**A third way to get it wrong, found during the port and not predicted here:**
`logical_cwd()` must prefer `$PWD` over `os.getcwd()`. A shell keeps the
symlinks you walked through; `getcwd` resolves them. Taking the resolved
answer would give one directory two store keys depending on how the caller
arrived -- the same failure as `Path.resolve()`, reached from the other side.
Both are pinned by tests now. Two of the three silent-drift risks in a
23-line port were invisible until someone wrote it, which is the honest
argument for porting early rather than analyzing longer.

## Faithfulness, evidenced

The port was required to be faithful, and "faithful" was checked rather than
asserted: 26 differential cases bash-versus-python (unicode, empty string,
bare dashes, dotted segments, nonexistent paths), plus both implementations run
over all 53 live relocated worktree paths. **Zero disagreements.**
`coherence.py --derived` after the migration is byte-identical to before --
53 worktrees, 19/31/3, 1012 store directories. **No key moved**, which is the
whole point of freezing the encoding.

## Duplication it collapsed

- `~/bin/claude-workspace-merge:15` -- a second implementation, inlined as a
  `claudepath()` bash function. **Retired**: calls `claude-path` now.
- `~/bin/claude-jsonl-path` -- a consumer, correct then and still correct.
- `claude_code_archeology.session.cwd()` -- documented the fact in prose
  because it could not import it. It can now, which is the dependency edge the
  whole exercise was for.

## Cost, estimated versus actual

The estimate was "a `pyproject.toml`, two entry points, a meta-package row, a
README row, and the port itself -- call it an hour." **Actual: about an hour for
that list, and the list was incomplete.**

What it missed: retargeting `git-localhost-store`'s symlink. GLS runs
`claude-path` at line 33 on *every* hook firing, before the `[ -L .git ]` exit,
so a dangling symlink does not fail a test -- it fails `git commit` in roughly
50 repositories. That step was load-bearing and unbudgeted.

The lesson generalizes and is filed as one: an estimate covering the artifact
can omit the *installation*, and the omitted part is the part that touches
everything already depending on the old arrangement. See
`../bukzor-packaging.claims.kb/cost.kb/`.
