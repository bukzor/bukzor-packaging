# Separable is not the same as separate

The tools were written with effort spent on factoring them apart from
bukzor's own idiosyncrasies. That effort mostly succeeded, which produces
three populations, not two:

- **separate** -- already stands alone; nothing to do
- **separable** -- factored well enough that extraction is mechanical, but
  still sitting in `~/bin` or inside the dotfiles repo
- **inseparable** -- genuinely about bukzor's config; extraction makes it
  worse, not better

The middle population is the whole subject of this kb, and it is easy to
misread as inseparable because *location* looks like *nature*. A script in
`~/bin` that hardcodes `~/.claude` looks personal; if what it hardcodes is
a path Claude Code defines rather than one bukzor chose, it is separable.

The test is not "does it mention my home directory" but **would anyone
else with the same upstream tool want this behavior**. `claude-inventory`
mentions `~/.claude/projects` throughout and is fully separable, because
that path is Claude Code's, not bukzor's. `claude-plan` names
`--model=opusplan --permission-mode=plan`, which is a preference, and is
therefore inseparable -- or, as it turned out, retirable.

## Counter-pressure

"Separable" is cheap to assert and expensive to verify; the honest
signal is whether the extraction has actually been attempted. Until then
it is a prediction. Record it as one.
