---
label: AMORTIZE
standing: bare
authority: >-
    mechanics.kb/bash-ships-via-shared-scripts.md -- two hatchling probes
    run 2026-08-10, one passing and one failing outright
why:
    - cost-splits-into-site-and-item.md
---

# The Site Discount Is Language Relative

*F* did not fall for everything. `bukzor-tools` is a uv/hatchling workspace,
and the discount it provides is a **Python** discount:

| | Python member | bash member |
|---|---|---|
| entry point | `[project.scripts]` | `shared-scripts` payload |
| direct install shims it | yes | yes |
| meta-package re-exports it | yes | **no -- install fails** |
| importable by a sibling | yes | no; shell out or nothing |
| test harness | doctests, already configured | none; no shellcheck hook either |

The third row is the one that decides things, and it is not a soft cost. A
meta-package whose only would-be executable comes from a dependency's
`shared-scripts` payload does not merely omit the command:

```
No executables are provided by package `metapkg`; removing tool
error: Failed to install entrypoints for `metapkg`
```

So `uv tool install bukzor-tools` -- the repo's one-install promise -- cannot
carry bash. For a bash tool, *F* is not 15 minutes; it is 15 minutes plus a
broken promise, or a shellcheck hook plus a pytest-shells-out wrapper plus a
Python trampoline nobody has tested.

## Smallest instance

`claude-slug`, 12 lines of `perl -CSD -pe 's/[^A-Za-z0-9]/-/g'`. The
disposition is **port to Python, do not ship the bash** -- and that was
decided by this mechanic, not by taste. As Python it gets four properties at
once: a console script, meta-package re-export, an importable function
`claude_code_archeology` can call instead of documenting the encoding in
prose, and a doctest. The port is faithful: `perl -CSD` makes the
substitution per *character*, which is what `re.sub` on a `str` does.

## Why this matters beyond one tool

Nine of the sixteen `~/bin/claude-*` scripts are bash. If the discount were
language-neutral, the clustering question would be settled by seams alone.
It is not, so every bash cluster faces a third option that a Python cluster
never does -- **port, don't move** -- and the port cost belongs in *m*(*t*),
where it competes.

That is also the honest reading of the theory's own `defeated by:` line.
*F* did fall, by an order of magnitude, for the Python case; the defeater
survives in one corner, and the corner is named rather than hidden.

## What would kill it

A tested Python trampoline in the meta-package that `execv`s a shared
script. Then bash re-exports, the third row flips, and *F* is
language-neutral again -- at the price of the meta-package owning code, which
it currently declares it does not (`bypass-selection = true`). Nobody has
tried it; that is acceptance debt, not a refutation.
