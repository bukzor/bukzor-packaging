---
label: ADAPTER
standing: user
authority: >-
    bukzor, 2026-08-10: "my own style is to have a very thin 'main' function in
    my scripts that adapts from a bona-fide function of the same name (as the
    script) to the cli calling convention. Perhaps you'd get a more beneficial
    theory if you presume such? Even where it's not literally true, it's a fair
    modelling, and for bukzor-owned scripts it should either be literally true
    or we can make it be so with minor work."
why:
    - tools-are-the-arrows-not-the-objects.md
    - ../cost.kb/the-testable-set-is-a-threshold-not-a-property.md
verify: ../composition.py --adapters
---

# An Adapter Is Where the Environment Leaks In

Carrier: a command as a pair -- a pure core *f*, and a `main` that adapts it to
the CLI calling convention. Law:

> **Every environmental dependency enters through the adapter.** argv, `$PWD`,
> the environment, the terminal, the locale, the clock, `PATH`. The core is a
> function of its arguments and nothing else, so it has a signature, and having
> a signature is what makes it an arrow in `PIPE`.

The presumption is bukzor's, granted above as a modelling license. Taking it
seriously is what makes `PIPE`, `STREAM` and `ROUNDTRIP` statable at all: an
arrow needs a domain and a codomain, and a script without a named core has
neither.

## The evidence points at the adapter, which is not where intuition points

Both real defects found while porting the store-key encoder were **adapter**
defects:

- `logical_cwd()` had to prefer `$PWD` over `os.getcwd()`, or one directory gets
  two store keys depending on how the caller arrived. A cwd leak.
- `perl -CSD` made the substitution per *character*; the naive port would have
  worked per byte. A locale leak.

Neither was in `slug()`, the part that looks like the algorithm. Two of three
silent-drift risks in a 23-line port lived in the six lines that talk to the
environment. **The adapter is small, boring, and where the bugs are** -- so it
is also where the tests belong, and a core that has been named can be tested
without any of that apparatus.

That is the link to `../cost.kb/the-testable-set-is-a-threshold-not-a-property.md`
and the answer this theory contributes to
`../questions.kb/which-teeny-scripts-are-worth-testing.md`: the marginal cost of
testing a small script is dominated by fixture setup, and fixture setup is
demanded by the adapter. Name the core and the core's tests need no fixture at
all, which moves the tool across the threshold without anyone deciding to
"invest in testing".

## How far the presumption is from true

`composition.py --adapters`, over the 20 `claude-*` commands on PATH:

- **1** names a core for its command (`slug`, in the package that shipped)
- **5** name one a rename away: `path_slug` under `claude-path`,
  `summarize_one` under `claude-jsonl-summarize`, `list_candidates` under
  `claude-open-tasks-list`, `merge_and_symlink` under `claude-workspace-merge`,
  and `claude-branch-extract`, whose core is `branch_records` although the check
  reports the earlier `belongs_to_branch` -- among equal word-overlaps the
  earliest wins, so a near-miss names *a* candidate, not the best one
- **3** effectful tools name no core at all: `claude-export`,
  `claude-jsonl-to-log`, `claude-uncolor`
- and one core is invisible to any name-based check: `claude-search`'s work is
  in `find()` and `scan()`, synonyms of the command rather than its name

The last row carries the real point. **The convention's value is not that a core
exists -- it is that a checker can find it.** A core named by a synonym is
structurally identical and formally useless: nothing can verify the discipline
holds, so nothing downstream can rely on it. The naming half of the convention
is the load-bearing half, which is the general claim in
`a-house-discipline-earns-its-keep-by-what-it-makes-checkable.md`.

Cost of making the presumption literally true, priced by the census: **five
renames and three extractions.** That is what "minor work" comes to, and it is
worth recording as a number because the laws downstream are design rules until
it is done.

## What would kill it

A tool whose logic *is* its effect sequence, where the split yields an empty
core -- `claude-fork`, `claude-workspace-merge`. Demanding a core there is cargo
cult, and the test is sharp: **if the core can return a plan the adapter then
executes, the split is real and `--dry-run` falls out for free; if the plan can
only be discovered by executing it, there is no core** and the tool is an
`unit -> unit` arrow by nature rather than by neglect.
