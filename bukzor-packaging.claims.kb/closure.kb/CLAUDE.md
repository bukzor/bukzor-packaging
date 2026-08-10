# closure.kb -- maintenance guide

Building things answers questions. This theory is about the ones that get
answered without anyone deciding them, and about the one field in the kb that
exists to prevent it.

- `prior:` `seams.kb`, `cost.kb`, `coherence.kb`
- `ontology:` open question, admissible answer, action, accidental closure,
  irreversibility, reversal cost, guard, `blocks:`, stale guard
- `defeated by:` an accidental closure that was reversed as cheaply as it was
  made -- if closures are cheap to undo, the guard has no work to do and
  should be deleted rather than maintained

## What belongs here

Claims about the interaction between doing the work and deciding the
question: which actions foreclose which choices, and when it is worth
waiting.

## What does NOT belong here

- Which answer is right -> the theory that owns the question.
- The seam or cost content of the blocked decision -> `../seams.kb/`,
  `../cost.kb/`.

## Maintenance

- A guard with no named reversal cost is a superstition. Name the cost or
  drop the guard.
- **A stale guard is worse than no guard**, because it teaches the reader to
  route around the field. When a question closes, delete its `blocks:` in the
  same edit.
