---
label: CASETWINS
standing: bare
why:
    - ../seams.kb/two-implementations-are-one-node-only-after-merging.md
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
verify: ../seams.py --twins
---

# The Open-Tasks Twins Already Disagree

Population: `~/bin/claude-open-tasks` (198 lines) and
`~/bin/claude-open-tasks-list` (212 lines). Measured 2026-08-10.

Neither names the other; both scan the filesystem for open-task markdown. The
duplicated knowledge, function by function:

| the fact | `claude-open-tasks` | `claude-open-tasks-list` |
|---|---|---|
| where to look | `ROOTS`, `scan()` | `ROOTS`, `list_candidates()` |
| what counts as a task file | `matches()` | `existence_is_signal()` |
| how to read a status | `parse_status()` | `frontmatter_status()` |
| which statuses are closed | *nothing* | `SKIP_STATUSES`, `KNOWN_STATUSES` |

## Three observable disagreements

- **`ROOTS` disagree.** `claude-open-tasks` scans `~/repo` and `~/.claude`;
  `claude-open-tasks-list` also scans `~/claude`. **14 task files under
  `~/claude/` are invisible to one twin and listed by the other** -- and one of
  the projects in that tree is this ledger.
- **The status regex is byte-identical** (`^status:\s*(\S+)`, `re.MULTILINE`)
  and reached differently: one requires a real `---` frontmatter block first,
  the other searches the first 30 lines. A file with `status: done` in its
  prose head and no frontmatter is closed for one twin and open for the other.
- **Only one validates.** `claude-open-tasks-list` warns on an unrecognized
  status; `claude-open-tasks` silently treats it as data.

Same knowledge, two encodings, three disagreements. No refactor has to be
argued for: the answers already differ, so at most one is right.

## Why this is the uncomfortable one

`claude-open-tasks` reads as the most natural cluster in the whole plan -- two
commands, one domain, obviously belong together -- and it is the one carrying a
live inconsistency. A latent verdict is therefore a finding of *risk*, not of
cohesion, and the merge is a precondition for the package rather than a cleanup
afterward.

The `ROOTS` question is genuinely undecided -- union or intersection, and each
choice changes one tool's output -- and per
`../closure.kb/a-guard-names-a-reversal-cost.md` it still earns no `blocks:`:
reversal is a one-line edit to a tuple with no released surface. Merge first,
argue in the review.

## What would make this stale

Merging them, which is the point. Also any edit to either `ROOTS` -- the count
of 14 is a function of what is currently under `~/claude/`, so re-run rather
than cite.
