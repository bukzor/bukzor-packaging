---
status: proposed
home: bukzor-tools
language: bash
---

# claude-stream

Driving `claude --print` programmatically, and rendering what comes back.
The cluster bukzor spotted by noticing `claude-print-verbose` is tightly
coupled to `claude-jsonl-display`.

Members:

- `~/bin/claude-print-verbose` (20 lines) --
  `claude --print --verbose --output-format stream-json | claude-jsonl-display`
- `~/bin/claude-s` (21 lines) -- `claude --print --input-format=stream-json
  --output-format=stream-json --include-partial-messages
  --replay-user-messages`, with `--verbose`/`--debug` added at `DEBUG>=2`/`>=4`

## Seam

Both know the same drifting fact: **which flag combination makes Claude
Code emit a machine-readable stream in this version.** That family is
larger than either script uses -- `claude --help` also offers
`--include-hook-events` and `--forward-subagent-text`, each documented as
"only works with `--output-format=stream-json`" -- and it has already
drifted once: `--verbose` used to be required alongside
`--print --output-format=stream-json`, and this version's help no longer
says so. `claude-print-verbose` passes it; `claude-s` doesn't. Neither
knows which of them is right, which is exactly the fact worth testing.

## Is claude-s the core of claude-print-verbose?

**No, not as written** -- they differ in *direction*, not in depth:

|                | `claude-s`                  | `claude-print-verbose` |
| -------------- | --------------------------- | ---------------------- |
| prompt arrives | stdin, stream-json envelopes | argv                   |
| output         | raw stream-json on stdout   | rendered by `-display` |
| partials       | `--include-partial-messages` | no                     |
| replay         | `--replay-user-messages`     | no                     |

`--replay-user-messages` only means anything when messages are being fed
in, so `claude-s` is a *harness for driving Claude Code as a subprocess*.
Adopting it as the core would force stream-json input on
`claude-print-verbose`, changing its calling contract from
`claude-print-verbose "prompt"` to writing a JSON envelope on stdin. That's
a regression, not a refactor.

**But there is a shared core, one level down.** `--input-format` takes
`text` (default) or `stream-json`, so the invocation parameterizes cleanly:

- core: `claude --print --output-format=stream-json --input-format=MODE …`
- `claude-print-verbose` = core with `MODE=text`, piped to the renderer
- `claude-s` = core with `MODE=stream-json` plus the partial/replay flags

See `../refactors.kb/extract-stream-json-invocation.md`.

## Boundary with claude-code-archeology

Unresolved, and the two packages meet here: the renderer
(`claude-jsonl-display`) consumes *both* live stream-json and archived
session JSONL. Whichever package owns it inherits the other's schema. See
`../refactors.kb/display-renders-two-schemas.md`. If that resolves toward
"one renderer, both schemas", `claude-stream` may collapse into a couple of
commands inside `claude-code-archeology` instead of standing alone -- which
would be a fine outcome, arrived at deliberately.
