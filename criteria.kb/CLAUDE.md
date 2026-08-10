# Criteria -- the rules a clustering call is made against

One judgment rule per file. These are the standards `packages.kb/` and
`refactors.kb/` entries are argued against, so an entry that cites no
criterion is probably an unexamined preference.

## What belongs here

- A rule that decides between two defensible options.
- A rule that names a failure mode precisely enough to catch it in the
  act, ideally with the instance that produced it.

## What does NOT belong here

- Verified technical behavior (how `uv tool install` treats a payload)
  -> `../mechanics.kb/`. Criteria are contestable; mechanics are testable.
- A specific tool's fate -> `../packages.kb/` or `../dispositions.md`.

## Maintenance

State the rule, then the strongest objection to it. A criterion with no
recorded counter-pressure tends to get applied past its range -- which is
how the graduation rule got used to justify leaving a 49-file tool with
its own ADRs inside dotfiles.
