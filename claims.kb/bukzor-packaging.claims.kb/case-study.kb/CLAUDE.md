# case-study.kb -- maintenance guide

Where the instance lives. Everything upstream states a rule; a file here
states what happened when the rule met one particular pile of scripts on one
particular machine, with the measurement that says so.

- `prior:` every other theory -- `levels.kb`, `seams.kb`, `cost.kb`,
  `genesis.kb`, `composition.kb`, `coherence.kb`, `graduation.kb`,
  `closure.kb`, `retirement.kb`, `questions.kb`
- `ontology:` case, population, measurement, verdict, exhibit, date of
  measurement, the tool names themselves
- `defeated by:` nothing -- a case study is a record, not a conjecture. What
  can go wrong is that it stops being reproducible, and that is a bug in the
  check rather than a defeat of the claim

## Why this collection exists

The general theories were written with their exhibits welded in: every law
arrived carrying a table of `claude-*` verdicts, so a reader could not tell
which sentences would still be true next year on a different machine. That is
the failure this collection fixes. **Upstream claims are rules with an
example; files here are the examples with their measurements.**

The bar has to be met in *both* places and it is not the same bar. A rule
needs a carrier, operations, laws, one smallest instance, and its own
defeater. A case study needs a population, a date, a command, and its output.

## What belongs here

- The verdict on a specific cluster, with the check that produced it.
- A measurement over a specific population, with the date it was taken.
- Anything whose truth expires when the machine changes.

## What does NOT belong here

- The rule the case exhibits -> upstream. If a file here starts arguing for a
  law, the law belongs in a theory and this file should cite it.
- Working notes on a candidate package -> `../../packages.kb/`, one directory
  up and outside the ledger entirely. The distinction: that kb is where a
  decision gets made, this is where a measurement gets certified.

## Maintenance

- **One file per case, not a directory.** A case gets a `<slug>.kb/` of its own
  only when one file stops holding it, which has not happened yet.
- **Every file carries a `verify:` and a date.** A case study whose number
  cannot be reproduced is an anecdote, and this collection is the one place in
  the ledger where `standing: bare` should be the norm rather than the
  exception.
- When a case is acted on -- the cluster built, the drift migrated -- keep the
  file and record what the action was. It becomes the before-picture, which is
  the only thing that can tell a later reader whether the rule was any good.
