---
label: REUSE
standing: agent
authority: >-
    bukzor 2026-08-10 names this as the third, separate kind: "a
    expenditure-leveraging mechanism in making deep research, today's deep
    understanding reusable tomorrow (once most of it's paged out)"
why:
    - friction-is-paid-per-invocation.md
    - ../cost.kb/cheap-tools-pin-drifting-facts.md
---

# Understanding Earns a Tool When Re-Deriving Costs More Than Recalling

The third benefit kind, and the one that justifies tools with almost no
recurrence.

Carrier: an understanding established at real expense -- a reverse-engineered
format, a measured behavior, a decision and its reasons. The premise is that
it **pages out**: the expenditure was real and the retention is not. Law:

> *b*<sub>reuse</sub> = P(needed again) × (re-derivation cost − recall cost)

The artifact does not have to be code. Prose recalls, a test asserts, a
function executes -- ascending in reliability and in what they cost to build.
The choice among them is `QUOTIENT` again, on a smaller scale.

## Why it is separate from friction, sharply

`FRICTION` multiplies by recurrence, so it goes to zero on a rarely used tool.
This one does not: P(needed again) can be low while the difference term is
enormous, and the product still clears the bar. A tool invoked twice a year
can be obviously worth building, and reaching for the frequency argument and
finding it absent proves nothing.

## Smallest instance

`claude-slug`, 12 lines, and one fact: Claude Code maps every
non-`[A-Za-z0-9]` character in a project path to exactly one `-`, with no run
squeezing and no case folding. Establishing that took reading Claude Code's
behavior. Re-deriving it means doing that again; recalling it means running the
command. Recurrence is near zero -- the encoder is consulted only when a store
is created or recovered -- and the tool is still the highest-ranked candidate
in the kb.

The counter-case in the same file is the point: `claude_code_archeology`
documents the same fact **in prose** because it cannot import a bash script.
Prose is the cheapest artifact on the ladder and the least reliable, and it has
already permitted the divergence that
`../coherence.kb/two-live-implementations-are-resolved-by-search-order.md`
measures. Choosing prose is choosing a lower recall cost and a higher chance of
being wrong.

## The trap this names

`../cost.kb/cheap-tools-pin-drifting-facts.md` is this benefit kind applied to
a fact that *moves*: pinning an upstream behavior in a test converts silent
drift into a failing check. Read together, the two claims say the same thing
from opposite ends -- understanding decays whether or not the world does, and
the artifact is what stops both.

## What would kill it

Understanding that is cheap to re-derive. If the fact is one web search or one
`--help` away, the difference term is near zero and the tool is waste no matter
how expensive the *original* discovery felt. Sunk cost is the failure mode
here, and the test that catches it is honest: ask what re-deriving costs
**today**, not what deriving cost then.
