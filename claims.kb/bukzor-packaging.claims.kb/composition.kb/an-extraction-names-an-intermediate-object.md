---
label: FACTOR
standing: agent
why:
    - tools-are-the-arrows-not-the-objects.md
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
---

# An Extraction Names an Intermediate Object

Carrier: one tool whose body computes two things in sequence. Law:

> **A latent seam is a composite that factors through an object the system does
> not name.** Extracting is naming it. The factorization is already there; the
> only decision is whether the intermediate value gets a name, and at which
> level -- a function, a module, or a separate command.

This is what `../seams.kb/a-cluster-may-be-seamed-latently.md` was reaching for.
That claim says a seam can exist without appearing as an edge, which reads as a
hedge -- "trust me, it's in there". Under `PIPE` it is a statement with content:
the edge is missing because no **object** is named, and an unnamed object is
exactly what a reference graph cannot see. `LATENT` stops being a judgment call
and becomes a question with a witness: *name the type of the value in the
middle.* If you can, the seam is real. If you cannot, it is not latent, it is
absent.

## Smallest instance

`claude-path` before the port ran path normalization and character encoding in
one perl pipeline. The port named the object between them: `normalize()` returns
a normalized path, `slug()` encodes one. Two functions, one new type, and the
`LATENT` verdict discharged -- `claude-path` now *imports* where it used to
`exec` its sibling.

The same factorization can be realized at two different levels, and the choice
is a cost question rather than a design one. `claude-uncolor` is
`uuid -> filesystem effect`, and its intermediate object -- a decolored `jsonl`
stream -- is named: `uncolor-jsonl` is a **separate command**. Identical
factorization, realized as two processes instead of two functions. Which
realization is right is decided by
`a-process-boundary-is-a-serialization-boundary.md`, not here -- and the answer
turns on the process boundary rather than the package one, which is a
distinction that file had to draw before it could be stated.

## What it settles upstream

`../questions.kb/which-recurring-actions-should-become-a-tool.md` asks, in its
well-posed form, for "a frequent contiguous subsequence whose intermediate
outputs are consumed only within the subsequence." **That is this law, stated
over a log instead of over a file.** Consumed-only-within means the intermediate
object is internal to the subsequence; a tool is earned by giving it a name.
The question's own complaint -- that *G* is undefined on a log -- is unaffected:
this says what to look for, not how to enumerate it.

## What would kill it

An extraction that is clearly worth doing and names no new object: splitting a
long function into halves with the same domain and codomain, or hoisting a
helper that returns the same type it took. Those are real and common; the claim
survives only because it is about *seams*, not about tidiness. If the
extractions that pay off here turn out mostly to be of that kind, `LATENT` was
a heuristic after all and this file should say so.
