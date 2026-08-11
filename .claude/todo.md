# bukzor-packaging — todo

The kb records decisions; this records the work those decisions named but
nobody has done. Every line here is priced in a claim file, so the argument
lives there and only the action lives here.

- [ ] Measure the `claude-path` port with `hyperfine`, against the retired
      perl/bash pair. `git-localhost-store` invokes it once per hook firing in
      ~50 repositories, so an interpreter start may have made every `git commit`
      slower. Asserted negligible, never measured — see
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
- [ ] Declare the encoder in `git-localhost-store` —
      `refactors.kb/declare-the-encoder-in-git-localhost-store.md`, blocked on
      packaging the consumer.
