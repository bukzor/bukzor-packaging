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
| `claude-fork`            | 42  | unsettled                  | a four-flag `exec claude --resume --fork-session --worktree N --name N`; the value is the recorded gotcha, not the flags -- `REUSE`, not friction |
| `claude-workspace-merge` | 120 | unsettled                  | inline copy retired -- now calls `claude-path`; still unclustered       |
| `claude-export`          | 86  | unsettled                  | **verified working 2026-08-11**: appends `export` to this session's shell snapshot, found via `/proc/self/stat` -> `ps --sid`. Audience is *agents*, and no `CLAUDE.md` mentions it -- zero use is zero discoverability |
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
| `claude-slug` + `claude-path` port | three implementations of one encoding down to one; GLS imports the encoder in-process instead of forking a subprocess on every hook firing in ~50 repos; 26 differential cases and 53 live paths agree, no key moved | estimated "a `pyproject.toml`, two entry points, a meta-package row, a README row, and the port itself -- call it an hour"; actual about an hour **plus two unbudgeted steps**: install had to precede deletion or `git commit` breaks, and `bin/`'s symlink needed retargeting (`packages.kb/claude-code-slug.md:158`) | 2026-08-10 |
| `git-localhost-store` graduation | failed all three dotfiles tests, AUDIENCE decisively: 49 tracked files including four ADRs, knowledge worth testing (hook recursion cap, ref recovery, layout migration), and an audience of anyone whose filesystem is slow (`packages.kb/git-localhost-store.md:13`) | bash tests dropped rather than converted; shellcheck hook still not wired, two shell files checked by hand; a git tool now lands on every machine, inert until `-install` runs (`:62`) | 2026-08-10 |
| `claude-plan` retire | one line in a cold corner: the toll is a rounding error, and the argument was never about its size | **the recorded reason does not hold** -- `claude --model=opusplan` is accepted and starts a session (probed 2026-08-11), so the flag value is not dead. What survives is zero attested invocation in 299 session logs and `~/.bash_history`. Reopened; awaiting a ruling | 2026-08-10 |

**Neither of the first two rows carves an exchange rate.** The cost side has a
number ("an hour"); the benefit side has no unit at all. So both decisions are
degenerate in `ELICIT`'s sense even though the record was fuller than the index
suggested -- the missing quantity is a *benefit in comparable units*, and no
amount of better filing produces one.
