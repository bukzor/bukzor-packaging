---
label: HOME
standing: agent
why:
    - a-cluster-is-legitimate-when-no-member-is-isolated.md
verify: ../seams.py --index
---

# A Tool Has at Most One Home

Carrier: the disposition map *d*, sending a tool to the package that owns
it, or to `dotfiles`, or to `retired`. Law:

> ***d* is single-valued.** No tool appears in two `packages.kb/` member
> lists, and `dispositions.md` is the graph of *d* -- the disjoint union of
> the member lists plus the unclaimed tools with their reasons.

Single-valuedness is not bookkeeping hygiene. It is what forces contention
to be *stated*. Two clusters that both want a tool have discovered a real
question about where the seam runs; letting both list it lets the question
go unasked, and then the first build to touch the tool answers it
irreversibly (`../closure.kb/building-closes-open-questions-by-accident.md`).

So the law comes with a discipline: **contention is recorded as a refactor
item, never as a duplicated member line.** The refactor's `blocks:` names
the clusters that must wait.

## Smallest instance

`claude-jsonl-display` is wanted by two candidates. `claude-code-archeology`
wants it because it renders archived `~/.claude/projects/*.jsonl`;
`claude-stream` wants it because `claude-print-verbose` pipes live
stream-json into it. Both cases are good.

What the ledger's own files do: `dispositions.md:19` carries exactly one
row for it (`claude-code-archeology`), `claude-stream.md` argues for it in
prose under "Boundary" without listing it as a member, and
`refactors.kb/display-renders-two-schemas.md` carries
`blocks: [claude-code-archeology, claude-stream]`. *d* stayed single-valued
and the question stayed open. That is the pattern working.

The alternative -- listing it under both -- would have read as a harmless
overlap, and the first `git mv` into either package would have silently
decided whether an archeology package handles live streams.

## What would kill it

A member genuinely shared by two packages with no leaf between them, which
in Python means a namespace package or a vendored copy. Vendoring is
`two-implementations-are-one-node-only-after-merging.md` and fails for the
reasons given there; namespace packages would make *d* multi-valued by
design and are worth considering only if the leaf-extraction cost
(`a-shared-leaf-resolves-contention.md`) is ever measured and found high.
