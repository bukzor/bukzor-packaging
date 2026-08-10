# Refactors -- re-seaming for packagability

One proposal per file: a decomposition or re-seaming that would make tools
more generic, more testable, or more packagable. Frontmatter per
`../refactors.jsonschema.yaml`.

This collection answers standing questions 2 and 3 from `../README.md`:
is there a decomposition that helps, and are the current seams the right
ones?

## What belongs here

- An extraction that gives two tools a shared core.
- A merge of two implementations of one idea.
- A boundary question between two candidate packages, where the answer
  changes what each package is.

## What does NOT belong here

- A cluster's membership argument -> `../packages.kb/`.
- Deleting a tool. That's a disposition, not a re-seaming ->
  `../dispositions.md`.
- Work that improves a tool without changing a seam. Real, but not this
  kb's subject.

## Maintenance

`blocks:` is load-bearing -- a candidate package listed there should not be
built until this resolves, because building it decides the question by
accident. Keep the list accurate or delete it; a stale `blocks:` is worse
than none.

State what would settle the question, concretely enough to act on. A
proposal that ends in "we should think about this" hasn't been written yet.
