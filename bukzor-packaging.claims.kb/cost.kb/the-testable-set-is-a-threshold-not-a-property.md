---
label: THRESHOLD
standing: user
authority: >-
    bukzor, 2026-08-09: "if we're being real, there's no such thing as
    untestable. There's only 'not worth testing', which is a cost/benefit
    judgement, requires estimating cost and benefit. If we reduce the
    incremental cost to near zero (imaginable, but currently not the case)
    then near all things, even teeny stuff, becomes testable."
why:
    - cost-splits-into-site-and-item.md
---

# The Testable Set Is a Threshold, Not a Property

"Untestable" names no property of a tool. Every tool has a marginal test
cost *c*(*t*) and a marginal benefit *b*(*t*), and the worth-testing set is

> *T*(*c*) = { *t* : *b*(*t*) > *c*(*t*) }

which is **monotone in the site**: lower the incremental cost and *T* only
grows. It is a sublevel set, not a predicate, and it has no stable
membership -- the same tool moves in and out as the site changes without
anyone editing the tool.

Consequences for how this kb may argue:

- **"Too small to test" is never a reason.** It is a claim that *b* < *c*,
  and it must be written as one, with both numbers.
- **A `not worth it` verdict expires** when the site changes. It is a dated
  measurement, not a finding.
- **Nothing is exempt by kind.** Wrappers, aliases, and one-liners are all
  in *T* at a low enough *c*.

## Smallest instance

`claude-slug`, 12 lines. By size, the paradigm of "not worth testing". As a
Python function its marginal test cost is *one doctest line*, and what that
line pins is a reverse-engineered encoding that live data on disk already
depends on -- `~/.local/state/git-localhost-store/repos/` names are built
from it, so a change to the encoding orphans stores. *b* ≫ *c* by a wide
margin, at 12 lines.

The site is what made that true. In `bukzor-tools`, pytest runs with
`addopts = "--doctest-modules"`, so a doctest *is* a test with no harness,
no file, and no registration: *c* is one line. In `~/bin` the same assertion
needs a test file, a runner, and a way to import a shebang script -- tens of
minutes. Same tool, same benefit, opposite verdict.

## What would kill it

A tool with *b* = 0 -- knowledge-free, so no test could fail informatively.
`claude-plan` (one line, no shebang, `--model=opusplan
--permission-mode=plan`) is the closest candidate in the data, and it does
not qualify: a test asserting the alias exists would have *caught its death
months ago* (`cheap-tools-pin-drifting-facts.md`). Its *b* was not zero; it
was unclaimed.
