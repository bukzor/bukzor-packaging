# Scope

## In scope

Any bukzor-authored tool currently living somewhere that makes it hard to
test, hard to install, or hard to hand to someone else:

- `~/bin/*` -- the largest population; `claude-*` is the active front
- `~/lib/pythonpath/bukzor/*` -- what remains after the archeology move
- tools tracked inside the dotfiles repo but not *of* it, e.g.
  `~/.local/share/git-localhost-store/` (49 tracked files, its own README,
  CLAUDE.md, TESTING.md and four ADRs -- a repo's apparatus living in
  dotfiles)

## Authorship-gated: `bukzor/work-stuff`

There is a body of well-factored, packagable work under
`bukzor/work-stuff` that belongs under this umbrella eventually. It is
**mixed authorship**, and the parts bukzor did not write are out of
bounds.

Rule, per bukzor 2026-08-10: look only at what is clearly bukzor-authored
or a close match for something known to be bukzor-authored -- and prefer
not to look at all rather than guess. An agent that cannot establish
authorship from evidence should leave the file unread and say so, not
skim it and caveat.

Deliberately not inspected as of 2026-08-10. When it opens up, the first
deliverable is an authorship-evidence pass, not a clustering pass.

## Out of scope

- Tools whose whole purpose is bukzor's own config: they belong in
  dotfiles by the graduation rule, and pulling them out makes them worse.
  See `criteria.kb/graduation-from-dotfiles.md`.
- Repos that already stand alone. They graduated; this kb is about things
  that haven't.
