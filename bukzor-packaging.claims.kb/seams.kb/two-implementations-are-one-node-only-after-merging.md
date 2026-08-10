---
label: TWIN
standing: bare
why:
    - a-cluster-is-legitimate-when-no-member-is-isolated.md
verify: ../seams.py --twins
---

# Two Implementations Are One Node Only After Merging

Duplication is not an edge. Two tools that implement the same knowledge
twice are two vertices of *G* with nothing between them, and *G* is right
about that: neither breaks when the other changes. They drift instead, which
is strictly worse than breaking, because breaking is observable.

This is why the promotion gate in
`a-cluster-is-legitimate-when-no-member-is-isolated.md` is stated on *G*.
A cluster of twins looks cohesive at every level a reader inspects -- same
domain, same artifact, same vocabulary -- and shares no line of code.

## Smallest instance

`claude-open-tasks` (198 lines) and `claude-open-tasks-list` (212 lines).
Neither names the other; both scan the filesystem for open-task markdown.
Their duplicated knowledge, function by function:

| the fact | `claude-open-tasks` | `claude-open-tasks-list` |
|---|---|---|
| where to look | `ROOTS`, `scan()` | `ROOTS`, `list_candidates()` |
| what counts as a task file | `matches()` | `existence_is_signal()` |
| how to read a status | `parse_status()` | `frontmatter_status()` |
| which statuses are closed | *nothing* | `SKIP_STATUSES`, `KNOWN_STATUSES` |

They have already drifted, and the drift is measurable:

- **`ROOTS` disagree.** `claude-open-tasks` scans `~/repo` and `~/.claude`;
  `claude-open-tasks-list` also scans `~/claude`. **14 task files under
  `~/claude/` are invisible to one twin and listed by the other** -- and one
  of the projects in that tree is this ledger.
- **The status regex is byte-identical** (`^status:\s*(\S+)`, `re.MULTILINE`)
  and reached differently: one requires a real `---` frontmatter block
  first, the other searches the first 30 lines. A file with `status: done` in
  its prose head and no frontmatter is closed for one twin and open for the
  other.
- **Only one validates.** `claude-open-tasks-list` warns on an unrecognized
  status; `claude-open-tasks` silently treats it as data.

Same knowledge, two encodings, three observable disagreements. No refactor
has to be argued for: the answers already differ, so at most one is right.

## What this costs the seam law

It means a latent verdict (`a-cluster-may-be-seamed-latently.md`) is a
finding of *risk*, not of cohesion. `claude-open-tasks` reads as the most
natural cluster in the whole plan -- two commands, one domain, obviously
belong together -- and it is the one carrying a live inconsistency. The
merge is a precondition for the package, not a cleanup afterward.

## What would kill it

Deliberate, tested duplication: two implementations kept apart on purpose
with a differential test asserting they agree. Then the test is the edge --
it references both, so *G* joins them through it -- and the law is satisfied
without a merge. Nothing in `~/bin` has such a test, which is why this claim
is worth writing down rather than assuming.
