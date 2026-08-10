---
label: FRICTION
standing: agent
authority: >-
    the framing is bukzor's -- "lower activation energy/friction on
    past-and-ongoing activities"; the decomposition into a per-invocation
    barrier times a recurrence count is this claim's own
why:
    - predicted-use-is-discounted-by-two-thirds.md
---

# Friction Is Paid Per Invocation

The first benefit kind, and the one a CLI is *for*.

Carrier: an action performed repeatedly. Activation energy is the barrier
crossed **every time** it is performed -- recalling the flags, composing the
pipeline, looking up where the file lives. Law:

> *b*<sub>friction</sub> = recurrence × Δ(activation energy)

Two consequences follow from the shape alone, before any estimate:

- **A tool does not need to add capability.** Lowering the barrier on
  something already possible is the entire benefit. "You can already do that
  with `jq`" is not an objection; it is a restatement of the premise.
- **Recurrence multiplies, so it can zero the product.** A large per-use
  saving on something done once is worth nothing, and this is the benefit kind
  most often claimed on a candidate that has no recurrence to multiply by.

## Smallest instance

`claude-s`, 21 lines, and the reason it survives every attempt to dismiss it.
It adds no capability -- every flag it sets can be typed. What it removes is a
flag family that has to be recalled correctly on each invocation, several times
a day. High recurrence, small Δ, and the product is the only argument it needs.

Note what this does *not* settle: `claude-s` still fails
`../graduation.kb/graduation-needs-audience-and-either-code-test.md` on
AUDIENCE and stays in dotfiles. Genesis and graduation are different
questions, and this is the tool that shows they can disagree -- worth
existing, not worth packaging.

## The proxy nobody has run

Recurrence is countable here and has not been counted. Every Bash call this
harness has ever made is recorded in `~/.claude/projects/*/*.jsonl`, and
`claude_code_archeology` reads that format. Until someone runs it, every
friction estimate in this kb is a recollection of how often something feels
done -- which is the estimate this claim is most exposed to being wrong about.
See `../questions.kb/which-recurring-actions-should-become-a-tool.md`.

## What would kill it

A tool whose value is real and *falls* with use -- something worth building
for a single crossing of the barrier, like a one-time migration. Those exist,
and they are the case where this benefit kind should not be reached for at
all: their numerator is `REUSE` or nothing.
