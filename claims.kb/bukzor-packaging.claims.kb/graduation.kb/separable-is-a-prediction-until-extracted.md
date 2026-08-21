---
label: PREDICT
standing: agent
why:
    - graduation-needs-audience-and-either-code-test.md
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
---

# Separable Is a Prediction Until Extracted

"Separable" is not an observation. It is a forecast that an extraction would
succeed, and the only thing that settles it is the extraction. Until then it
should be recorded with its status, exactly as the criteria file says of
itself: *"'Separable' is cheap to assert and expensive to verify... Until
then it is a prediction. Record it as one."*

The same shape appears one theory over. A **latent** seam
(`../seams.kb/a-cluster-may-be-seamed-latently.md`) is the prediction that a
refactor will realize an edge; a **separable** tool is the prediction that a
move will not drag context with it. Both are debts denominated in work not
yet done, and both are discharged the same way: by doing it and reporting
what happened.

## The confirmed instances

`claude_code_archeology` -- `claude-search`, `claude-inventory`,
`claude-branch-list`, `claude-branch-extract` plus seven library modules --
was predicted separable and then extracted. Result: 43 doctests pass, four
commands smoke-tested live, and the dotfiles copies deleted.

`claude-code-slug`, shipped 2026-08-10, is the second -- and the first whose
prediction this ledger made rather than recorded. It was called **mechanical**,
and the port bears that out where it counts: 26 differential cases plus all 53
live worktree paths, zero disagreements, and `--derived` byte-identical before
and after. No key moved.

But "mechanical" was wrong in a way worth keeping. The file predicted **one**
silent-drift risk (`Path.resolve()` versus `normpath`, which would follow
symlinks); the port found **two**, the second being that `logical_cwd()` must
prefer `$PWD` over `os.getcwd()` for exactly the same reason from the other
side. Two hazards in a 23-line port, one of them invisible until someone wrote
it.

So the rate is 2 for 2 out of a plan of five, and the honest reading of the
second is that extraction is not merely *confirmation* -- it is where the
remaining hazards are found. A prediction of "mechanical" is a prediction about
effort, never about completeness.

## The instance with evidence against it

`claude-open-tasks-list` is asserted separable on the strength of a real
algorithm (effective mtime, worktree dedup). But its twin disagrees with it
about **where to look**: two `ROOTS` lists, differing by `~/claude`, 14 task
files visible to one and not the other
(`../seams.kb/two-implementations-are-one-node-only-after-merging.md`). An
extraction has to pick one, and *neither is obviously right* -- the union
changes one tool's output, the intersection changes the other's.

So this prediction is not merely unverified; the extraction is known to
require a decision that no one has made. That is a different and worse
status than `claude-code-slug`'s was -- and the difference held up: the
mechanical one shipped in an hour, and this one still has an undecided `ROOTS`.

Recording both as "separable" flattens that difference, which is the
concrete reason this claim earns its file.

## What would kill it

A cheap, reliable proxy for separability -- an import-graph check, say, that
a tool references nothing under `~/.config` or `~/.local/share`. Worth
building if the extraction rate ever gets high enough to amortize it; today
the population is 16 tools and the proxy would cost more than the
extractions it would triage
(`../cost.kb/cost-splits-into-site-and-item.md`).
