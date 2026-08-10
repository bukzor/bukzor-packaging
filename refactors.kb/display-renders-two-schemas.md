---
status: proposed
blocks: [claude-code-archeology, claude-stream]
---

# claude-jsonl-display renders two schemas

`~/bin/claude-jsonl-display` (714 lines, stdlib-only Python, ~50 `format_*`
functions) reads JSONL from stdin and renders a transcript. It is fed from
two different producers:

- **archived**: `~/.claude/projects/*/*.jsonl` records, via
  `claude-jsonl-to-log` or a shell redirect
- **live**: `claude --print --output-format stream-json`, via
  `claude-print-verbose` -- note its dedicated `format_stream_event`

Those are related but not identical schemas. Whichever package owns the
renderer inherits both.

## Why it blocks two candidates

- If `claude-code-archeology` absorbs it, that package silently stops being
  "transcripts on disk" and becomes "Claude Code records, live or
  archived". Defensible -- but it should be chosen, not discovered later
  when someone wonders why an archeology package handles live streams.
- If `claude-stream` owns it, then `claude-jsonl-to-log` (an archive tool)
  depends on a live-streaming package, which is backwards.

## The three resolutions

1. **One package, widened scope.** Renderer goes to
   `claude-code-archeology`, whose charter is rewritten to "Claude Code
   record streams, live or archived". `claude-stream` shrinks to the
   invocation core and its two commands, probably as members here too.
2. **Renderer as its own leaf**, depended on by both -- same shape as
   `claude-slug`. Cleanest dependency graph, one more package.
3. **Split the renderer** along the schema boundary. Almost certainly
   wrong: `format_*` functions overwhelmingly handle content blocks, which
   both schemas share, so the split would duplicate most of the file.

## What would settle it

Count how much of the 714 lines is schema-specific. `format_stream_event`
and `format_result` look live-only; `format_snapshot` and `format_summary`
look archive-only; the ~40 `format_*` attachment/content handlers look
shared. If shared dominates -- the likely finding -- resolution 3 dies and
the choice is 1 vs 2, which is then a taste call about package count
rather than an architecture question.

Do this before absorbing any `claude-jsonl-*` member into
`claude-code-archeology`, since the first absorption is what decides it.

## Related overlap

`claude-jsonl-display` duplicates `claude_code_archeology.format_short`'s
content-block walking. `format_short` is deliberately terse (~80-column
tree labels) and says so in its docstring, pointing at
`claude-jsonl-display` for full rendering. Two renderers at two verbosities
over one block model is a reasonable end state -- but they should share the
block walking, and today they don't.
