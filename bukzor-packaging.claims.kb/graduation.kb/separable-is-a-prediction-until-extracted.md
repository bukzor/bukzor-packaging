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

## The confirmed instance

`claude_code_archeology` -- `claude-search`, `claude-inventory`,
`claude-branch-list`, `claude-branch-extract` plus seven library modules --
was predicted separable and then extracted. Result: 43 doctests pass, four
commands smoke-tested live, and the dotfiles copies deleted. The prediction
was right, and it is worth *nothing* as evidence for the next one; what it
establishes is the rate at which such predictions get confirmed, which is
now 1 for 1 out of a plan of five.

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
status than `claude-slug`'s, whose port is mechanical.

Recording both as "separable" flattens that difference, which is the
concrete reason this claim earns its file.

## What would kill it

A cheap, reliable proxy for separability -- an import-graph check, say, that
a tool references nothing under `~/.config` or `~/.local/share`. Worth
building if the extraction rate ever gets high enough to amortize it; today
the population is 16 tools and the proxy would cost more than the
extractions it would triage
(`../cost.kb/cost-splits-into-site-and-item.md`).
