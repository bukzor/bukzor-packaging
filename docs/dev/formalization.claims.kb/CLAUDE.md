# formalization.claims.kb -- how the ledger above was built

Ten claims about *doing* a formalization, extracted from the one in
`../../../bukzor-packaging.claims.md` because none of them is about packaging.
They transfer; the ledger they came from does not.

- `prior:` `Skill(formalize)`'s bar -- an identification carries a carrier,
  operations, laws, one smallest instance drawn from the data, and the
  observation that would kill it
- `ontology:` instrument, population, corpus, over- and under-approximation,
  soundness direction, monotone predicate, exchange rate, elicitation, decision
  terms, predicted versus measured term, estimator, coverage, retrieval
  occasion, carrier choice, killed conjecture
- `defeated by:` a formalization that paid off while violating these -- most
  plausibly one where the theory was written first and the measurement only
  confirmed it, which would kill `INSTRUMENT` and weaken the rest

Read `a-structure-earns-its-keep-by-the-decision-it-changes.md` first. Five
claims are its consequences; two are its unstated premises, filed after the fact
because the bar it states cannot grade either of them -- `CARRIER` (the choice of
objects, which no count refutes) and `RETRIEVAL` (whether the claim reaches the
decision at all).

## Cheapest order of operations

The order that produced the ledger above, with the mistakes taken out.

Before step 1, name the objects -- the census is a census *of* them, so the choice
precedes everything here and no later step can check it (`CARRIER`). Spend real
effort on it and expect it to be the expensive error.

1. **Census the population before framing anything.** Twenty rows of "what is
   actually here" is worth more than any conjecture, and it is an hour.
2. **Build the cheapest instrument next, while the claims are still soft.** It
   will rewrite them -- that is the point, not a setback (`INSTRUMENT`).
3. **Conjecture past the comfortable ones.** The reach that fails is worth more
   than the safe pick that holds: the transposed category ("tools are the
   objects") died and its correction became a whole theory.
4. **Record what killed each conjecture.** The kills are the compressed form of
   everything the data said no to, and they are what stops the next agent from
   re-proposing them.
5. **State the population size next to every law.** A law with one instance is a
   conjecture with good manners; say so in the same paragraph.
6. **Turn each obligation into a failing check.** Prose has no encounter cost, so
   a prose obligation applies no pressure and will still be there next year.

## Maintenance

- **The graph lint takes the ledger root, which is `docs/dev/`, not this
  directory:** `bin/llm-claims-kb-graph docs/dev`. Pointed at this `.kb/` it asserts
  on finding no theory subdirectories -- this collection *is* the single theory,
  and its parent is the ledger.

- **A change to a check is a change to the theory.** `INSTRUMENT` makes the
  instrument a co-author of the claims, which means editing a measure edits what
  the law it certifies means. Commit the check with the claim it moves; "just
  fixing the script" is a silent amendment.

- **Every standing here is `agent` except where noted.** These are the agent's
  methodological calls and no one has ratified them; that is the honest state and
  also the collection's main weakness. Two carry a `verify:` that demonstrates
  the failure mode rather than certifying the law.
- **Keep the files short.** This collection is read at the *start* of work, so
  its token cost is paid before any of its value arrives. If a claim needs more
  than a screen, the instance belongs in the ledger it came from.
- **Do not import subject matter.** A claim mentioning a `claude-*` tool is
  drifting back into `../../../bukzor-packaging.claims.kb/`; cite it instead.
