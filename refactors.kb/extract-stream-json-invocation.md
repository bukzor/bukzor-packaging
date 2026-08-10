---
status: proposed
blocks: [claude-stream]
---

# Extract the stream-json invocation

`claude-print-verbose` and `claude-s` each hardcode a flag set whose job is
"make Claude Code emit a machine-readable stream". The flags are
version-sensitive and the two scripts already disagree about them.

## The extraction

`--input-format` accepts `text` (default) or `stream-json`, per
`claude --help`, so one parameterized core covers both callers:

```
core:                 claude --print --output-format=stream-json --input-format=$MODE "$@"
claude-print-verbose: core MODE=text        | claude-jsonl-display
claude-s:             core MODE=stream-json --include-partial-messages --replay-user-messages
```

What the core owns: the flag set, and the knowledge of which flags require
which others. `claude --help` documents four flags as "only works with
`--output-format=stream-json`" (`--include-partial-messages`,
`--include-hook-events`, `--forward-subagent-text`, and `--input-format`'s
stream-json mode), plus several as "only works with `--print`". Those
constraints are exactly what a single tested surface should enforce.

## The disagreement it would settle

`--verbose` was once required alongside `--print --output-format=stream-json`.
This version's `--help` no longer says so. `claude-print-verbose` passes it
unconditionally; `claude-s` passes it only at `DEBUG>=2`. One of them is
carrying a stale workaround and neither knows which -- an upstream-behavior
fact with no test, which is the highest-value kind here (see
`../criteria.kb/testability-is-cost-benefit.md`).

## What would settle it

A single invocation at each `MODE`, recording whether stream-json output
arrives without `--verbose` on the current version. Cheap, decisive, and it
turns the core's flag list from folklore into a pinned fact.

## Objection

Two 20-line bash scripts don't obviously need a shared core; the extraction
adds a third file. The answer is that the third file is the only one that
would be *tested*, and it's where the version drift lands. If that argument
fails, the fallback is smaller and still worth it: make `claude-s` and
`claude-print-verbose` agree about `--verbose`, and write down why.
