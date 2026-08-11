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
| `claude-slug`            | 12  | **`claude-code-slug`** (shipped) | ported to Python, deleted from `~/bin`; now a console script      |
| `claude-path`            | 23  | **`claude-code-slug`** (shipped) | same package; GLS imports `path_slug` rather than resolving a name |
| `claude-jsonl-path`      | 3   | `claude-code-archeology`   | consumer, not a copy: `claude-path` + the projects-dir location        |
| `claude-jsonl-cwd`       | 19  | `claude-code-archeology`   | already reimplemented as `session.Session.cwd()`, doctested            |
| `claude-jsonl-display`   | 714 | `claude-code-archeology`   | duplicates `format_short`'s block walking; see the two-schemas seam    |
| `claude-jsonl-to-log`    | 25  | `claude-code-archeology`   | thin driver over `-display`; likely a flag, not a command              |
| `claude-uncolor`         | 16  | `claude-code-archeology`   | repairs session files in place; transcript-domain, and destructive     |
| `claude-print-verbose`   | 20  | `claude-stream`            | tightly coupled to `-display`; pipes into it                           |
| `claude-s`               | 21  | `claude-stream`            | same flag family, opposite direction (stream-json *in*)                |
| `claude-open-tasks`      | 198 | `claude-open-tasks`        | PEP-723 python, real algorithm, overlaps its sibling                   |
| `claude-open-tasks-list` | 212 | `claude-open-tasks`        | worktree dedup by effective mtime -- testable knowledge, untested      |
| `claude-fork`            | 42  | unsettled                  | ex-`claude-session-lifecycle`, rejected; shares nothing with either sibling |
| `claude-workspace-merge` | 120 | unsettled                  | inline copy retired -- now calls `claude-path`; still unclustered       |
| `claude-export`          | 86  | unsettled                  | ex-cluster; `~/.claude/shell-snapshots` is a subsystem of its own      |
| `claude-jsonl-summarize` | 63  | unsettled                  | not yet read closely                                                   |
| `claude-plan`            | 1   | **retire** (settled)       | `--model=opusplan`; no such alias in current `claude --help`, and the file has no shebang |

Config aliases that stay in `dotfiles`: none of the above except by
argument. `claude-s` and `claude-print-verbose` were originally filed as
launcher aliases and moved out of that group once read -- the only
survivor of that reading is `claude-plan`, which is being retired instead.

## Elsewhere

| tool                 | disposition                | why                                                            |
| -------------------- | -------------------------- | -------------------------------------------------------------- |
| `git-localhost-store` | **`git-localhost-store`** (shipped) | general git tool that rode along in dotfiles; has its own ADRs |
| `bukzor/work-stuff`   | gated                     | mixed authorship -- see `scope.md`                             |

## Decision terms

Every **bold** disposition above is a decision that weighed something against
something. This records the two terms as estimated *at the time*: `for` is
`QUOTIENT`'s numerator and `against` its denominator, whichever direction the
action pointed. A verdict without its terms constrains no exchange rate, and the
numbers are not recoverable afterwards -- see
`docs/dev/formalization.claims.kb/record-the-terms-of-a-decision-not-only-its-verdict.md`.

A `--` with a reason **is** a record: it says the term was never estimated, which
makes the decision degenerate rather than undocumented. `retirement.py` fails
while a bold row above has no row here.

| decision | for | against | when |
| --- | --- | --- | --- |
| `claude-plan` retire | one line in a cold corner: the toll is a rounding error, and the argument was never about its size | zero -- `--model=opusplan` is not a flag value `claude` offers, so there is no benefit left to forfeit | 2026-08-10 |
