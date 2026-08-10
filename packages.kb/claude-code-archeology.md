---
status: shipped
home: bukzor-tools
language: python
---

# claude-code-archeology

Shipped 2026-08-09 (`bukzor-tools` f6c2700, dotfiles f155f32) -- the first
graduation rather than a new build, so it's the reference for what a move
costs.

Commands: `claude-search`, `claude-inventory`, `claude-branch-list`,
`claude-branch-extract`. Library: `claude_code_archeology.{session,tree,
format_short,branch_list,branch_extract,inventory,search}`.

## Seam

Everything here needs the parent/child forest model in `session.py`. That
shared model is the seam, and it's load-bearing: `branch_list` and
`branch_extract` are unbuildable without it, and `inventory`/`search` both
depend on `is_user_text` to tell a typed prompt from a tool result.

## Pending members

Per `../dispositions.md`: `claude-jsonl-display`, `claude-jsonl-cwd`,
`claude-jsonl-path`, `claude-jsonl-to-log`, `claude-uncolor`. Blocked on
`../refactors.kb/display-renders-two-schemas.md`, which decides whether
this package is about *files on disk* or *record streams generally*.

## What the move actually cost

Useful as a cost estimate for the next graduation:

- pyright strict found 17 errors the old `~/lib/pythonpath` config didn't;
  root causes were bare `field(default_factory=list)` and isinstance-
  narrowing an unannotated `Any` into `Unknown`. Resolved with a
  `JsonValue` union so the runtime guards stay necessary *and* protective.
- one latent `IndexError` surfaced in `_label_tool_use` (a `Bash` tool_use
  whose input lacks `command`).
- shebang/`--doctest` hack per module deleted; `uv run pytest` with
  `--doctest-modules` replaced it. 43 tests.
- `$PATH` puts `~/bin` before `~/.local/bin`, so the old wrappers shadowed
  the new shims until deleted -- see
  `../mechanics.kb/path-shadowing-blocks-migration.md`.

Net: about one working session, most of it spent on strict typing rather
than on the move.

## Dependency

Should depend on `claude-slug` once that exists, replacing the prose
warning in `session.cwd()`'s docstring with a real import.
