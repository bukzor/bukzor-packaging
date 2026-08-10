# Graduation from dotfiles

`bukzor-tools`' own README states the line, and it is the right one:

> Dotfiles hold glue -- wrappers and shims that only make sense beside my
> config. These are programs: they carry knowledge worth testing, grow
> subcommands, and shouldn't ride along to every machine that clones my
> dotfiles.

Three tests, and they are **not** symmetric:

> graduate ⟺ AUDIENCE ∧ (KNOWLEDGE ∨ SUBCOMMANDS)

- **KNOWLEDGE** -- carries knowledge worth testing: reverse-engineered
  upstream behavior, a non-obvious algorithm, a format fact.
- **SUBCOMMANDS** -- grows them: has flags, modes, or a family of siblings
  that should share a core.
- **AUDIENCE** -- shouldn't ride along: would be unwelcome or irrelevant on
  a machine that merely wants bukzor's shell config.

AUDIENCE is necessary; the other two are jointly sufficient given it. An
earlier version of this file said "any one is sufficient" *and* "when they
disagree, AUDIENCE decides", which cannot both hold -- a tool with KNOWLEDGE
and no AUDIENCE would both graduate and stay. The conjunctive rule fits every
settled call, including the one that discriminates the readings (`claude-s`
has KNOWLEDGE, lacks AUDIENCE, stays).

AUDIENCE is the test most often skipped, and it is the sharpest. Apparatus is
its own evidence: a tool with a README, a TESTING.md, ADRs and a todo.kb
has already declared itself a project. If that apparatus is inside the
dotfiles repo, the repo is carrying a project as cargo.

## Counter-pressure

The rule reads as a filter on *tools*, but KNOWLEDGE and SUBCOMMANDS are
properties of code while AUDIENCE is a property of people. A tool can have
both code properties and still belong in dotfiles because its audience is
exactly one config -- `claude-s`' flag choices are arguably this. When they
disagree AUDIENCE decides, because packaging is a distribution decision
before it is a code decision -- which is what makes it necessary rather than
merely weighty.
