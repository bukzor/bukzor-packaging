# Packaging bukzor's ad-hoc tools

## The standing questions

Asked of any tool, any time, not just when packaging is the task:

1. What clustering of ad-hoc tools would make them packagable? (A
   cost/benefit claim, highly cost-sensitive -- and `bukzor-tools`
   existing already lowered the cost.)
2. Is there a decomposition of a current tool that would make it more
   generic, more packagable, or more testable?
3. Are the candidate clusters well served by their **current** seams, or
   would things package and test better after refactoring along a
   different seam?
4. As work happens: is any recurring *clustering of actions* worth
   **com**posing into a new tool or tool-suite?

Question 4 is the one that generates new entries here. The first three
are re-asked of entries that already exist.

## Where it stands

`bukzor-tools` holds three shipped packages; `claude-code-archeology` is
the first that was a graduation rather than a new build. `~/bin/claude-*`
is the working front: 16 scripts, of which 3 are true config aliases, 1
is a relic, and the rest carry testable knowledge that is currently
untested.

Read `dispositions.md` first -- it is the index, and it answers "what
about X?" without opening a collection.

The live disagreement worth knowing about: whether
`claude-code-archeology` is scoped to *transcripts on disk* or to *Claude
Code record streams, live or archived*. `claude-jsonl-display` renders
both, so absorbing it decides the question by accident unless it's
decided on purpose. See `refactors.kb/display-renders-two-schemas.md`.
