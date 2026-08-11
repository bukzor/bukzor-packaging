# bukzor-packaging — todo

The kb records decisions; this records the work those decisions named but
nobody has done. Every line here is priced in a claim file, so the argument
lives there and only the action lives here.

- [ ] Ratify or veto `INFLATE`
      (`bukzor-packaging.claims.kb/genesis.kb/a-predicted-cost-is-inflated-by-the-same-coefficient.md`).
      It changes the build gate — a purely speculative action goes from needing
      3:1 to needing 9:1 — and it currently stands `agent`. The sign is defensible
      from `FORECAST`'s own argument; the magnitude is symmetry, not evidence.
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
