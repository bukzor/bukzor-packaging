# Graduation from dotfiles

`bukzor-tools`' own README states the line, and it is the right one:

> Dotfiles hold glue -- wrappers and shims that only make sense beside my
> config. These are programs: they carry knowledge worth testing, grow
> subcommands, and shouldn't ride along to every machine that clones my
> dotfiles.

Three tests, and they are independent. Any one is sufficient:

1. **Knowledge worth testing** -- reverse-engineered upstream behavior,
   a non-obvious algorithm, a format fact.
2. **Grows subcommands** -- has flags, modes, or a family of siblings that
   should share a core.
3. **Shouldn't ride along** -- would be unwelcome or irrelevant on a
   machine that merely wants bukzor's shell config.

Test 3 is the one most often skipped, and it is the sharpest. Apparatus is
its own evidence: a tool with a README, a TESTING.md, ADRs and a todo.kb
has already declared itself a project. If that apparatus is inside the
dotfiles repo, the repo is carrying a project as cargo.

## Counter-pressure

The rule reads as a filter on *tools*, but tests 1 and 2 are properties of
code while test 3 is a property of *audience*. A tool can pass 1 and 2 and
still belong in dotfiles because its audience is exactly one config --
`claude-s`' flag choices are arguably this. When the tests disagree, 3
decides, because packaging is a distribution decision before it is a code
decision.
