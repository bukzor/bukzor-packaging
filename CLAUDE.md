--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# bukzor packaging kb

A standing question, not a project: which of bukzor's ad-hoc tools should
become packages, clustered how, and along which seams. `bukzor-tools`
lowered the per-package cost enough that the answer changes -- this kb
tracks the re-evaluation as it happens, tool by tool.

Collections:

- `criteria.kb/` -- the judgment rules a clustering call is made against
- `packages.kb/` -- one file per candidate package, existing or proposed
- `refactors.kb/` -- re-seamings that would make tools package or test better
- `mechanics.kb/` -- verified facts about how packaging behaves here

Root files: `README.md` (synthesis + the standing questions), `scope.md`
(what's in scope, what's authorship-gated), `dispositions.md` (the index:
every tool in scope and where it currently lands).

## Maintenance

- **Evidence is a path and a line, or a command and its output.** "Looks
  like glue" is not evidence; opening the file is. This kb exists partly
  because grading tools by filename produced two wrong calls in one
  paragraph (see `criteria.kb/seams-over-name-prefixes.md`).
- **A tool appears in exactly one `packages.kb/` file.** If two clusters
  both want it, that contest is a `refactors.kb/` item about the seam --
  not a duplicated member line.
- **`dispositions.md` is the index and must stay in sync.** Every tool
  named in a `packages.kb/` member list appears there; so does every
  tool that no package claims, with its reason.
- **A `packages.kb/` entry records why these members belong together.**
  A member list without that rationale is a name-prefix cluster.
- **Shipped candidates keep their files.** Status becomes `shipped`; the
  file becomes the record of which seam was chosen and what it cost.
- Estimates here are cost/benefit claims. Write the estimate down, not
  just the conclusion, so a later reader can attack the estimate.
- **Root `.md` files carry no frontmatter, deliberately.** This project's
  root is itself a `.kb`, so `bin/llm.kb-validate` reads its root files as
  collection items and demands a sibling `bukzor-packaging.jsonschema.yaml`
  that cannot live inside the repo. They're synthesis files; `last-updated`
  is what git already tracks. Don't add it back.
