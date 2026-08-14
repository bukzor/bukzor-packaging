# bukzor-packaging — todo

The kb records decisions; this records the work those decisions named but
nobody has done. Every line here is priced in a claim file, so the argument
lives there and only the action lives here.

- [ ] Apply the R4 benefit-unit ruling, once bukzor closes N (the gate's
      payback bound; 26 ≈ one year proposed). Ruled 2026-08-13: benefit in
      SWEh per 2 weeks (`benefit-2w`; optional ISO-8601 `horizon`
      sub-attribute, default P2W), gate is payback `c/benefit-2w ≤ N` with c
      from TERMS inflated per INFLATE, rank divides by c never timebox.
      Application: TERMS/QUOTIENT declarations + a benefit column in
      `dispositions.md`; plus `Skill(llm-subtask)`'s schema (shared skill,
      bukzor approval). Full state: `requirements.md` R4 and
      `~/.claude/sessions.kb/penguin.kb/bukzor-packaging-r4-ruling-and-reset-question.md`.
- [~] bukzor rules: keep or reset the 2026-08-12..13 theory work (baseline
      `5db0ce4`; everything since is prose in this repo, checks clean). Both
      live sessions froze 2026-08-13T16:30 pending re-orientation. A wholesale
      reset discards three bukzor rulings -- the R1-R6 requirements spec, the
      SWEh benefit unit, INFLATE's recorded decline; unsigned claims can be
      dropped per-file instead (`grep -rH '^standing:' bukzor-packaging.claims.kb/`).
- [ ] bukzor re-reads QUOTIENT
      (`bukzor-packaging.claims.kb/genesis.kb/a-tool-is-worth-building-when-benefit-over-cost-exceeds-one.md`):
      commit `995763c` rewrote this user-signed claim's argument (Smith's rule
      for the sequencing regime, replacing an optimality claim that was false
      under a budget; conclusion unchanged) without re-ratification. Re-sign
      or downgrade the standing.
- [ ] Advertise `claude-export` where its audience will meet it: a line in
      `~/.claude/CLAUDE.md` under the Bash conventions, since it is the only way to
      make an environment variable survive between `Bash()` calls. Verified working
      2026-08-11; never invoked before that by anyone, because nothing tells an
      agent it exists. Then re-disposition it out of `unsettled`.
- [ ] Rule on `claude-plan`, whose retirement is **reopened**: its recorded reason
      ("no such alias in current `claude --help`") is false — `claude
      --model=opusplan` is accepted and starts a session. What survives is zero
      attested invocation. Still installed, so `retirement.py` exits 1 either way
      until the row is settled and carried out.
- [ ] Settle the five newly-visible unattested tools. The temporal cut took
      "no invocation attested" from 1 of 20 to **8 of 20**; two are shipped-package
      console scripts and one is `claude-export`, leaving `claude-jsonl-path`,
      `claude-jsonl-summarize`, `claude-jsonl-to-log`, `claude-s` and `claude-plan`.
      Four already have package homes decided on *seam* grounds — their zero use is
      new information about whether those members should ship at all.
      Measurement: `case-study.kb/the-unseamed-cluster-was-not-the-unused-one.md`.
- [ ] Measure the `claude-path` port with `hyperfine`, against the retired
      perl/bash pair. The premise shrank on 2026-08-10: `git-localhost-store`
      shipped as a package that imports `claude_code_slug` in-process, so it no
      longer spends a subprocess per hook firing across ~50 repositories. What
      is left to price is the standalone `claude-path`/`claude-slug` command,
      and the relocator's own interpreter start on every `git commit`.
      Asserted negligible, never measured — see
      `bukzor-packaging.claims.kb/composition.kb/a-process-boundary-is-a-serialization-boundary.md`
      and `cost.kb/an-estimate-omits-the-cutover.md`.
- [ ] Make the thin-main discipline true: five renames and three extractions,
      enumerated by `bukzor-packaging.claims.kb/composition.py --adapters`.
      Until then the composition laws are design rules, not descriptions.
- [ ] Settle `claude-jsonl-summarize`, which `seams.py --index` now warns about:
      it is filed `unsettled` while calling `claude-jsonl-to-log`, a member of
      shipped `claude-code-archeology`. Either it joins the package or the edge
      becomes a declared dependency; `unsettled` records neither.
- [ ] Finish or retract archeology's partial ship: `claude-jsonl-path`,
      `claude-jsonl-cwd`, `claude-jsonl-display`, `claude-jsonl-to-log` and
      `claude-uncolor` are planned members still sitting in `~/bin`, and `~/bin`
      is first on PATH.

## Later

Uncommitted; surfaced by sweeps, never nagged. Three gaps the 2026-08-11
formalization named and did not fill.

- [ ] Say which of `levels.kb/`'s claims are sound in which direction. `MONOTONE`
      says a soundness direction exists only for a predicate monotone in the
      approximated quantity, and the level claims were written before that rule
      existed, so none of them states one.
- [ ] Give `levels.kb/audience-is-not-in-the-files.md` a mechanism. It says
      the audience decides and does not say how one is reached — which is exactly
      the hole `claude-export` fell into: right audience, no channel.
- [ ] Measure `CHURN`: P(a claim still covers its subject) as a function of
      interface churn, from `git log` on the tools' own files. It is the missing
      term in every retention argument here, and it is a measurement, not a
      judgment — so it is cheap and nobody has taken it.
