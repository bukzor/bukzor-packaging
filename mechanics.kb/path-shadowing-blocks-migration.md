# ~/bin shadows ~/.local/bin, so a migration isn't done until the old file is deleted

Verified 2026-08-09 during the `claude-code-archeology` move.

`$PATH` puts `/home/bukzor/bin` **before** `/home/bukzor/.local/bin`. Since
`uv tool install` shims into `~/.local/bin`, a newly packaged command is
shadowed by its own predecessor in `~/bin` until that file is removed.

The failure this causes is quiet: the new package installs successfully,
`command -v` looks plausible to a careless reader, and every invocation
keeps running the old code. A test suite passing against the package while
the shell runs the old script is the worst version of this.

Migration order that avoids it:

1. package and install
2. `git rm` the old wrapper(s)
3. `hash -r`, then `command -v NAME` and confirm it resolves under
   `~/.local/bin`
4. run the command against real data -- not just `--help`

Step 3 is the one that gets skipped. `hash -r` matters because bash caches
the old path within the session, so even after deletion the shell may report
"no such file" or keep executing a stale inode.

## Corollary for graduations specifically

While both copies exist, the two can silently diverge, and the surviving
one is whichever `$PATH` finds -- not whichever is newer or better tested.
Keep the overlap window short: delete in the same session as the install,
which also means committing the deletion rather than leaving it staged.
