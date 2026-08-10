# bukzor-tools can ship bash today

Verified 2026-08-10. This removes the main objection to `git-localhost-store`
and `claude-slug` joining a Python workspace.

`bukzor-tools` is a uv/hatchling workspace and its README anticipates other
*language toolchains* ("a pnpm workspace goes in when the first one lands"),
which reads as though bash has no path in. It does: hatchling's
`shared-scripts` puts arbitrary executables in the wheel's scripts dir, and
`uv tool install` shims them like any entry point.

## The probe

`~/trash/shared-scripts-probe/` (kept; gitignored via `/trash/`).

```toml
[tool.hatch.build.targets.wheel.shared-scripts]
"bash-bin/probe-bash" = "probe-bash"
```

The mapping value must be non-empty -- `"bash-bin" = ""` fails with
`Path for source 'bash-bin' ... cannot be an empty string`. Map each file
explicitly.

Results:

- `uv build` -> `probepkg-0.1.0.data/scripts/probe-bash` in the wheel
- `uv tool install .` -> "Installed 1 executable: probe-bash"
- `~/.local/bin/probe-bash -> ~/.local/share/uv/tools/probepkg/bin/probe-bash`
- running `probe-bash` printed `probe-bash-ran`

No entry point, no Python trampoline, no new toolchain -- **for a directly
installed package.** The limit is below.

## What still isn't free

- `bukzor-tools/.pre-commit-config.yaml` has no shellcheck hook. A bash
  member should add one; the cost is shared across all bash members, so
  the first one to land pays it.
- `[tool.pytest.ini_options] addopts = "--doctest-modules"` means the test
  suite is doctests, which reach no bash. Bash tests need either a pytest
  wrapper that shells out or conversion.
## The meta-package cannot re-export a bash payload

Tested 2026-08-10, and it's a hard no. A `metapkg` depending on `probepkg`
(whose only executable is the `shared-scripts` bash file):

```
+ probepkg==0.1.0 (from file:///home/bukzor/trash/shared-scripts-probe)
No executables are provided by package `metapkg`; removing tool
error: Failed to install entrypoints for `metapkg`
```

`uv tool install` shims a package's own entry points only, and a
`shared-scripts` payload is not an entry point -- so it is invisible to the
`[project.scripts]` re-export trick that makes `uv tool install bukzor-tools`
yield every command. It didn't merely omit the script; the meta-package
install *failed outright* for having no executables of its own.

Consequences for any bash member of `bukzor-tools`:

- it ships only via `uv tool install ./packages/NAME`, not via the
  meta-package -- a break in the repo's one-install promise
- or the meta-package grows a Python trampoline entry point that `execv`s
  the shared script (untested; requires the meta to have code, which it
  currently declares it doesn't via `bypass-selection = true`)
- **or the tool stops being bash.** For anything small enough to port, this
  is the better answer, and it's what turned `claude-slug` from a bash
  package into a Python one.

## What still isn't free (for genuine bash members)

- `bukzor-tools/.pre-commit-config.yaml` has no shellcheck hook. The first
  bash member pays for it; the cost is shared thereafter.
- `[tool.pytest.ini_options] addopts = "--doctest-modules"` means the suite
  is doctests, which reach no bash. Bash tests need a pytest wrapper that
  shells out, or conversion.
