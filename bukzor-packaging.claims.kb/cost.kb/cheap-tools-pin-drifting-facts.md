---
label: DRIFT
standing: agent
why:
    - the-testable-set-is-a-threshold-not-a-property.md
verify: >-
    claude --help | grep -q -- opusplan && echo 'PRESENT -- claim dead' || echo
    'opusplan: gone from claude --help; the fact claude-plan encoded has drifted'
---

# Cheap Tools Pin Drifting Facts

Benefit is not proportional to size. A tool's *b*(*t*) tracks the *fact it
encodes*, not the lines it takes to encode it:

> *b*(*t*) ≈ drift rate of the encoded fact × cost of failing silently

Both factors are large exactly where line count is small. A wrapper's whole
content is a claim about someone else's interface -- the flag that exists,
the alias that resolves, the path that is stable. Those are the facts that
move without telling you, and a wrapper that has gone wrong usually still
runs.

So the intuition that small tools are not worth testing is not merely a bad
estimate of *c* (which is
`the-testable-set-is-a-threshold-not-a-property.md`); it is backwards about
*b*.

## Smallest instance

`claude-plan`, one line, no shebang:
`claude --model=opusplan --permission-mode=plan`. There is no `opusplan`
alias in the current `claude --help` -- the model aliases are `fable`,
`opus`, `sonnet`. The tool has been broken for months and nobody noticed,
because nothing asserted the alias. One doctest-sized check against
`claude --help` would have failed the day it changed.

Its disposition is **retire**, not "port with a test" -- the underlying
workflow is gone too. But it is the exhibit, because it is simultaneously
the smallest tool in scope and the one that suffered the most expensive
failure mode available: silent.

## The live case

`claude-s`, 21 lines, encodes which flag combination makes Claude Code emit
a machine-readable stream. That family has **already drifted once**:
`--verbose` used to be required alongside
`--print --output-format=stream-json`, and the current help no longer says
so. `claude-print-verbose` passes it, `claude-s` does not, and neither knows
which is right. Two tools disagreeing about an upstream fact is a test
waiting to be written, and it is the reason
`refactors.kb/extract-stream-json-invocation.md` is worth doing beyond
tidiness -- the extracted core is the one place that fact can be asserted.

## What would kill it

A cheap tool encoding a fact that cannot drift -- pure computation over a
frozen spec. `claude-slug` is close (the encoding is upstream's and has been
stable), but it is not an argument against this claim: its *b* comes from
the *cost* factor instead, since a silent change to the encoding orphans
data on disk. Both factors have to be small for the intuition to hold, and
in this population neither usually is.
