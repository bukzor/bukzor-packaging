---
last-updated: 2026-08-10
---

# Dispositions

Index of tools in scope and where each currently lands. `dotfiles` means
staying put on purpose, not "not looked at yet". Every candidate name is a
file in `packages.kb/`.

## `~/bin/claude-*` (16 scripts, 2026-08-10)

| tool                     | loc | disposition                | why                                                                    |
| ------------------------ | --- | -------------------------- | ---------------------------------------------------------------------- |
| `claude-slug`            | 12  | `claude-slug`              | reverse-engineered encoding; a second implementation exists inline     |
| `claude-path`            | 23  | `claude-slug`              | path normalization over the same encoding; GLS depends on it           |
| `claude-jsonl-path`      | 3   | `claude-code-archeology`   | consumer, not a copy: `claude-path` + the projects-dir location        |
| `claude-jsonl-cwd`       | 19  | `claude-code-archeology`   | already reimplemented as `session.Session.cwd()`, doctested            |
| `claude-jsonl-display`   | 714 | `claude-code-archeology`   | duplicates `format_short`'s block walking; see the two-schemas seam    |
| `claude-jsonl-to-log`    | 25  | `claude-code-archeology`   | thin driver over `-display`; likely a flag, not a command              |
| `claude-uncolor`         | 16  | `claude-code-archeology`   | repairs session files in place; transcript-domain, and destructive     |
| `claude-print-verbose`   | 20  | `claude-stream`            | tightly coupled to `-display`; pipes into it                           |
| `claude-s`               | 21  | `claude-stream`            | same flag family, opposite direction (stream-json *in*)                |
| `claude-open-tasks`      | 198 | `claude-open-tasks`        | PEP-723 python, real algorithm, overlaps its sibling                   |
| `claude-open-tasks-list` | 212 | `claude-open-tasks`        | worktree dedup by effective mtime -- testable knowledge, untested      |
| `claude-fork`            | 42  | `claude-session-lifecycle` | speculative cluster; seam not yet argued                               |
| `claude-workspace-merge` | 120 | `claude-session-lifecycle` | speculative; also carries an inlined copy of the slug encoding         |
| `claude-export`          | 86  | `claude-session-lifecycle` | speculative; operates on `~/.claude/shell-snapshots`                   |
| `claude-jsonl-summarize` | 63  | unsettled                  | not yet read closely                                                   |
| `claude-plan`            | 1   | **retire** (settled)       | `--model=opusplan`; no such alias in current `claude --help`, and the file has no shebang |

Config aliases that stay in `dotfiles`: none of the above except by
argument. `claude-s` and `claude-print-verbose` were originally filed as
launcher aliases and moved out of that group once read -- the only
survivor of that reading is `claude-plan`, which is being retired instead.

## Elsewhere

| tool                 | disposition                | why                                                            |
| -------------------- | -------------------------- | -------------------------------------------------------------- |
| `git-localhost-store` | `git-localhost-store`     | general git tool riding along in dotfiles; has its own ADRs    |
| `bukzor/work-stuff`   | gated                     | mixed authorship -- see `scope.md`                             |
