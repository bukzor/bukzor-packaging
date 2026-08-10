---
status: proposed
home: bukzor-tools
language: python
---

# claude-open-tasks

Aggregating open work across every project: `todo.md`, `todo.kb/`,
`todo.d/`, `sessions.kb/`, `CLAUDE.*Task*.md`.

Members, both Python, overlapping:

- `~/bin/claude-open-tasks` (198 lines) -- PEP-723 `uv run --script`
- `~/bin/claude-open-tasks-list` (212 lines) -- plain `python3`

## Seam

Not transcripts. These scan *todo conventions*, which makes their subject
`Skill(llm-subtask)`'s file formats, not `~/.claude/projects`. That's why
this is its own candidate rather than more members for
`claude-code-archeology`: nothing here would import `session.py`, and
nothing in archeology would import a todo parser.

The `claude-` prefix is the only thing tying them to the rest of
`~/bin/claude-*`, which is exactly the trap in
`../criteria.kb/seams-over-name-prefixes.md`.

## Knowledge worth testing

`claude-open-tasks-list`'s docstring states the non-obvious rule, and it is
currently untested prose:

> Effective mtime is the file's last-commit time when the file is clean,
> else filesystem mtime -- git checkout sets filesystem mtime to checkout
> time (not commit time), so a fresh sibling worktree would otherwise beat
> `main` on identical content.

That is a git-behavior fact plus a dedup policy. It has an obvious
doctestable shape and no test.

Also encoded: "for `todo.kb/`-style files, existence *is* the signal, so
emit the path unconditionally; if a `- [ ]` list happens to be present,
list those too." A convention worth pinning, since the kb conventions it
tracks keep evolving.

## Precondition

Two implementations of one tool must become one before packaging -- see
`../refactors.kb/dedup-open-tasks-implementations.md`. Packaging both would
ship the ambiguity.

Naming: `claude-` in the name is probably wrong once packaged, since the
subject is bukzor's todo conventions, not Claude Code. `open-tasks` reads
better and matches what it actually scans.
