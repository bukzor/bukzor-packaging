---
label: QTEST
standing: agent
why:
    - ../cost.kb/the-testable-set-is-a-threshold-not-a-property.md
    - ../cost.kb/cheap-tools-pin-drifting-facts.md
    - ../cost.kb/the-site-discount-is-language-relative.md
---

# Which Teeny Scripts Are Worth Testing?

**As experienced** (bukzor, 2026-08-09): *"a few are inherently inseparable
-- those belong in bukzor/dotfiles, esp if they're teeny, 'untestable'. But
if we're being real, there's no such thing as untestable. There's only 'not
worth testing', which is a cost/benefit judgement."*

**Well-posed:** for which *t* does *b*(*t*) > *c*(*t*) at the current site,
and how does the set move when the site changes?

**What the difference reveals:** the experienced question treats testability
as a **property of the tool**; the posed one makes it a **relation between a
tool and a site**. The user's own second sentence performs the correction
mid-thought -- which is why this reframing is his and not the ledger's. What
the ledger adds is the consequence: since the answer is a relation, *no
verdict here is durable*, and every "not worth it" in the kb is a dated
measurement that expires when `bukzor-tools` changes.

## Settled: the threshold, and the direction of the error

- `../cost.kb/the-testable-set-is-a-threshold-not-a-property.md` -- the
  worth-testing set is a sublevel set, monotone in the site. "Untestable" is
  never a reason; "*b* < *c*, here are both numbers" is.
- `../cost.kb/cheap-tools-pin-drifting-facts.md` -- the usual intuition is
  wrong about *b*, not just about *c*. Small tools encode other people's
  interfaces, which drift and fail silently. `claude-plan` is one line, was
  broken for months, and nobody knew.
- `../cost.kb/the-site-discount-is-language-relative.md` -- in `bukzor-tools`
  a Python doctest costs one line, so *c* ≈ 0 and nearly everything Python
  clears the bar. Bash gets no such discount.

Concretely: **the site already moved, so the back catalogue of "too small to
test" verdicts is void.** That is the substantive answer, and it is why the
12-line `claude-slug` is a package with doctests rather than a shim.

## Residue

- The numbers are guesses in minutes, unvalidated. `claude-slug`'s port was
  estimated at an hour; nobody has done it, so the estimate has never been
  scored. One measured port would calibrate every other estimate here.
- Bash's *c* is still high and nobody has tried the cheap fix -- a shellcheck
  hook plus a pytest wrapper that shells out. Until someone does, thirteen of
  sixteen tools sit above the threshold for a reason that is a *site* defect,
  not a property of the tools.
