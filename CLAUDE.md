--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
git-caution: personal
---

# bukzor packaging kb

The deliverable is a theory of how and why ad-hoc work becomes packages --
corpus-independent: an agent could run it against any population and act on
its verdicts without re-deriving them. `~/bin` is the first test corpus, not
the subject; a wrong disposition is evidence against a claim before it is a
filing error. Coverage is graded against `requirements.md` -- what the job
needs -- before any audit of what the files contain.

The theory is `bukzor-packaging.claims.md` and its `.kb/`. How it was built --
transferable claims about doing a formalization cheaply, none of them about
packaging -- is `docs/dev/formalization.claims.kb/`. **Read that before
starting a formalization, not after.**

Collections -- the test corpus and its working notes:

- `criteria.kb/` -- the judgment rules a clustering call is made against
- `packages.kb/` -- one file per candidate package, existing or proposed
- `refactors.kb/` -- re-seamings that would make tools package or test better
- `mechanics.kb/` -- verified facts about how packaging behaves here

Root files: `README.md` (synthesis + the standing questions), `requirements.md`
(what the theory's job needs, and how far it gets), `scope.md` (what's in
scope, what's authorship-gated), `dispositions.md` (the index: every tool in
scope and where it currently lands).

## Maintenance

- **Evidence for a claim about the corpus is a path and a line, or a command
  and its output.** "Looks like glue" is not evidence; opening the file is.
  This kb exists partly because grading tools by filename produced two wrong
  calls in one paragraph (see `criteria.kb/seams-over-name-prefixes.md`).
  The one question this rule cannot answer is theory coverage -- a missing
  term has no path; that grading is `requirements.md`.
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
