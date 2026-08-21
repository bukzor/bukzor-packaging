---
label: QNAME
standing: agent
why:
    - ../seams.kb/a-cluster-is-legitimate-when-no-member-is-isolated.md
    - ../seams.kb/a-cluster-may-be-seamed-latently.md
    - ../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md
---

# Does the `claude-` Prefix Name a Package?

**As experienced** (bukzor, 2026-08-09): *"If we want to capture the full
range of `~/bin/claude-*` we might want a `claude-code-tools` as well? not
sure on that."*

**Well-posed:** is there a set *S* ⊆ `~/bin/claude-*`, not covered by an
existing package, such that *G*[*S*] has no isolated vertex?

**What the difference reveals:** the experienced question asks for *coverage
of a name*; the posed question asks about a *graph*. That substitution is the
error `../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md`
names, and it is not a pedantic upgrade -- the two questions have different
answers. "Capture the full range" presumes the range is a thing to be
captured. It isn't.

## Settled: no

Sixteen scripts sharing a prefix decompose into 1 seamed cluster, 3 latent,
1 dead, 1 relic, 1 unsettled -- five or six destinations, none of them "the
`claude-*` tools". Eight of the sixteen are isolated in *G* even under a
textual over-approximation of calling.

The felt need behind the question is real, though, and it has an answer that
is not a package: **`bukzor-tools` is already the thing that makes a family
of unrelated commands installable as one unit.** That is what a meta-package
is -- entry-point re-export plus dependencies, no code of its own. A
`claude-code-tools` package would be the same bundling done a second time,
one level down, and would additionally have to answer which of the five
destinations it was overriding.

## Residue

- `claude-jsonl-summarize` (63 lines) is still unread and unassigned. It has
  one edge (to `claude-jsonl-to-log`) and the `session-jsonl` artifact, so it
  is almost certainly an archeology member -- but *almost certainly* is what
  the levels theory forbids acting on.
- `claude-fork` and `claude-export` have no artifact in common with anything
  (`../seams.kb/a-cluster-may-be-seamed-latently.md`). "Stay in dotfiles" is
  the reading; nobody has read them closely enough to sign it.
