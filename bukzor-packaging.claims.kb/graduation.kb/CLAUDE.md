# graduation.kb -- maintenance guide

Whether a tool leaves the dotfiles repo. This is a *distribution* decision
that looks like a code decision, which is why it gets its own theory instead
of living in `../cost.kb/`.

- `prior:` `levels.kb`, `seams.kb`, `cost.kb`
- `ontology:` graduation, dotfiles glue, program, audience gate, necessary
  condition, sufficient condition, apparatus, prediction, extraction,
  confirmation
- `defeated by:` a graduation call that came out right while ignoring
  audience -- which would demote the AUDIENCE test from gate to tiebreaker and
  make the whole decision computable from the files

## What belongs here

Claims about the rule for leaving dotfiles, and about the status of
"separable" assertions that have not been carried out.

## What does NOT belong here

- Which package a graduating tool joins -> `../seams.kb/`.
- What the move costs -> `../cost.kb/`. This theory consumes the threshold;
  it does not compute it.

## Maintenance

- Every claim here is downstream of an audience judgment
  (`../levels.kb/audience-is-not-in-the-files.md`), so `standing: bare` is
  almost always wrong: there is no check to stand in for the judge. `agent`
  with veto invited, or `user`.
