# bukzor-packaging — todo

The kb records decisions; this records the work those decisions named but
nobody has done. Every line here is priced in a claim file, so the argument
lives there and only the action lives here.

- [ ] Carry out `claude-plan`'s retirement. Dispositioned **retire (settled)**
      2026-08-10 and still installed in `~/bin`, which is the whole of
      `retirement.kb/the-forecast-discount-cuts-both-ways.md`'s evidence that the
      action is the bottleneck rather than the verdict. `retirement.py` exits 1
      until it goes.
- [ ] Fire the gate on `claude-export`: 86 lines, `unsettled`, and the only tool
      of twenty with **no attested invocation** in 298 session logs or bukzor's
      shell history. Either name a caller the logs cannot see — a hook, another
      checkout — or delete it. Priced in
      `retirement.kb/deletion-is-a-candidate-action-like-any-other.md`.
- [ ] Name the benefit kind for `claude-fork`, `claude-workspace-merge` and
      `claude-export`. Measured recurrence rules out friction for all three, and
      they are the same three members of the cluster killed for having no seam;
      `REUSE` can carry a tool alone but nobody has claimed it for these.
      Measurement: `case-study.kb/the-unseamed-cluster-is-also-the-unused-one.md`.
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
