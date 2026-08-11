--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-claims)
    - Skill(llm-claims-kb)
---

# bukzor-packaging claims -- maintenance guide

The formal account of the kb one directory up: which claims the packaging
decisions rest on, who signed each, and what would overturn it. The kb holds
the working notes; this holds the load-bearing structure.

Entry point: `../bukzor-packaging.claims.md` -- the poset and the picture.

## Filing rule

**A claim goes in the earliest theory whose ontology -- its own plus its
priors' -- admits every word the claim needs.** If you must borrow vocabulary
from a downstream theory to state it, either it belongs downstream, or the
upstream theory is missing a term and should gain it deliberately.

**Rules upstream, measurements in `case-study.kb/`.** A theory file states a law
and names one smallest instance in a sentence or two; the population, the
transcript, and the date belong in a case study that carries the `verify:`. The
test: if a paragraph would need rewriting when a script is edited, it is an
exhibit and it is in the wrong file. This split exists because the first draft
welded them together, and a reader could not tell which sentences would survive
a change of machine.

## Standing conventions

The schema says a certified claim's standing is `bare` -- the check stands
where a judge would. That needs one distinction this ledger uses constantly:

- **`bare` + `verify:`** -- the check certifies *the claim*. `PROXY`, `TWIN`,
  `DERIVED`, `SHADOW`, `AMORTIZE`.
- **`agent`/`user` + `verify:`** -- the claim is a *law*, and the check only
  evaluates the data the law ranges over. `SEAM` and `LATENT` are judgments
  about what makes a package; `seams.py` reports which clusters currently
  pass. Running it cannot certify the law.
- **never `bare` in `graduation.kb/`** -- its necessary conjunct is L3, so no
  check exists that could stand in for the judge
  (`levels.kb/audience-is-not-in-the-files.md`).

**The tell that this stopped being a theory:** if every file's honest standing
is `user`, the ledger has become a manual -- a record of preferences with no
structure that could be wrong. Watch the ratio.

## Code lives in files, not in frontmatter

A `verify:` is a *command*, never a program. Each theory's checks live beside
its collection as `<theory>.py` (or `<theory>.d/` if one file stops being
enough) -- `seams.py` next to `seams.kb/`, `coherence.py` next to
`coherence.kb/`.

This is not formatting preference. Code in a YAML scalar cannot be run by
hand, formatted, type-checked, or reviewed as a diff; the checks here are
`black`-clean and `pyright`-clean because they are files. A claim whose
`verify:` grew past one line has a script waiting to be written.

## Method

`../docs/dev/formalization.claims.kb/` holds what building this ledger taught
about building ledgers -- the population bar, why the check gets written before
the claims are done, which direction of a heuristic's verdicts is sound, and how
an exchange rate is elicited rather than measured. It is deliberately free of
subject matter, so it is the cheaper thing to read first.

## Maintenance

- After adding or renaming claims, run `bin/llm.claims-graph` from
  `Skill(llm-claims-kb)` against this directory. It lints dangling `why:`
  targets, cycles, and claims that never joined the graph.

- Run every check before believing any number in here. They are cheap and two
  of them currently exit nonzero *on purpose* -- that is the finding, not a
  broken script.
- When a claim is overturned, edit the file. The `-` lines in the git diff are
  the strikethrough; do not delete the file and do not renumber anything.
- Claims cite the kb above by relative path, e.g. into `../packages.kb/`. Those are
  one-way: the kb should not depend on the ledger, so that it stays usable
  without it.
