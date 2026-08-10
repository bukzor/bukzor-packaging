---
label: AUDIENCE
standing: agent
why:
    - observation-comes-in-four-levels.md
---

# Audience Is Not in the Files

L3 -- who besides the author would want this -- is not definable from L0,
L1, or L2. No amount of reading the code answers it, because the answer is
a fact about other people's situations.

Two consequences, and they are the reason this claim is worth its file:

**A tool that names your home directory may still be separable.**
`claude-inventory` says `~/.claude/projects` throughout and is fully
separable, because that path belongs to Claude Code rather than to the
author. `claude-plan` names `--model=opusplan --permission-mode=plan` and is
not, because those are preferences. The textual signal is identical; the
audience differs.

**The decisive test cannot be automated, and its claims are therefore
`user`-signed.** Everything the seam and cost theories do can in principle
be computed. The graduation decision cannot
(`../graduation.kb/graduation-needs-audience-and-either-code-test.md`), so
its standing is a ruling and not a check. A ledger that marked it `bare`
would be claiming a computation it cannot exhibit.

## Smallest instance

`claude-s` (21 lines) passes L2 -- it encodes which flag set makes Claude
Code emit a machine-readable stream, a fact that has already drifted. It
plausibly fails L3: the flags encode one harness's needs. Nothing in the
file distinguishes those two readings; only knowing who else drives Claude
Code as a subprocess does.

## What would kill it

A proxy for audience that is computable and holds up: download counts,
inbound links, a dependency graph across other people's repos. For tools
that have never left one machine there is no such signal by construction --
which is exactly the population this ledger is about.
