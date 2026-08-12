# bukzor-packaging — todo

The kb records decisions; this records the work those decisions named but
nobody has done. Every line here is priced in a claim file, so the argument
lives there and only the action lives here.

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
