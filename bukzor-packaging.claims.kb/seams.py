#!/usr/bin/env python3
"""Check the seam laws of seams.kb/ against ~/bin and ../dispositions.md.

Two relations on tools:

- G  -- realized: `t` textually references `u`. Over-approximates calling.
- G+ -- latent: G plus an edge between tools touching the same artifact.

    G ⊆ G+, so a cluster connected in G is connected in G+.

Verdicts per cluster, from the disposition index:

    SEAMED   no isolated member in G           -- shippable as-is
    LATENT   isolated in G, not in G+          -- separable, not separate;
                                                  a refactor realizes the edge
    NONE     isolated in G+                    -- not a package under any
                                                  refactoring
    SINGLE   one member                        -- law vacuous, no siblings to
                                                  share with; decided by cost
    SHIPPED  status: shipped in packages.kb/   -- members have left ~/bin on
                                                  purpose; the graph is silent
                                                  and PATH answers instead

The SHIPPED case is not a convenience. A package that ships *deletes its
members from ~/bin*, so every relation here goes quiet and a graph verdict
computed over the absence reads NONE -- condemning the cluster for having
succeeded. Shipping moves the question from "do these files reference each
other" to "does the command exist and where does it come from", which is
`coherence.py --shadow`'s provenance check, not this one's.

Usage: seams.py [--edges] [--artifacts] [--isolated] [--index] [--twins]
       seams.py --cluster tool,tool,...

`--cluster` judges an arbitrary member set instead of the index, so a cluster
the index no longer carries -- a rejected one, say -- stays checkable.

Exits nonzero when a cluster earns NONE, when a shipped package's commands
are missing from PATH, when --index finds the disposition map multi-valued or
out of sync with ~/bin, or when --twins finds the open-tasks pair still
drifting.
"""

from __future__ import annotations

import collections
import pathlib
import re
import shutil
import sys

BIN = pathlib.Path.home() / "bin"
KB = pathlib.Path(__file__).resolve().parent.parent
INDEX = KB / "dispositions.md"
PACKAGES = KB / "packages.kb"

Edges = set[tuple[str, str]]

# An artifact is a schema or a data location two tools can share without
# sharing a line of code. The regex is the marker, not the definition.
ARTIFACTS = {
    "record-schema": r"parentUuid|toolUseResult|isSidechain|stream_event"
    r"|content_block|\bsessionId\b",
    "session-jsonl": r"\.claude/projects|\.jsonl",
    "stream-json": r"stream-json",
    "todo-markdown": r"todo\.kb|todo\.md|\[ \]",
    "worktree": r"worktree|git rev-parse",
    "shell-snapshots": r"shell-snapshots",
    "slug-encoding": r"A-Za-z0-9\]|claude-slug|claudepath",
}

# Dispositions in the index that are not candidate packages.
NOT_A_PACKAGE = ("retire", "unsettled", "dotfiles", "gated")

# Two implementations of one job, neither referencing the other.
TWINS = ("claude-open-tasks", "claude-open-tasks-list")

# Where a task file lives, relative to a scanned root.
TASK_GLOBS = (".claude/todo.md", ".claude/todo.kb/*.md")


def tools() -> dict[str, str]:
    return {p.name: p.read_text(errors="replace") for p in sorted(BIN.glob("claude-*"))}


def clusters() -> dict[str, list[str]]:
    rows = re.findall(
        r"^\| `([\w.-]+)` *\| *\d+ *\| *\**`?([\w.-]+)`?", INDEX.read_text(), re.M
    )
    out: dict[str, list[str]] = collections.defaultdict(list)
    for tool, pkg in rows:
        out[pkg].append(tool)
    return dict(out)


def frontmatter(path: pathlib.Path) -> str:
    found = re.match(r"^---\n(.*?)^---", path.read_text(), re.S | re.M)
    return found.group(1) if found else ""


def shipped() -> set[str]:
    """Packages whose members have left ~/bin, per packages.kb/ frontmatter."""
    return {
        path.stem
        for path in sorted(PACKAGES.glob("*.md"))
        if re.search(r"^status: shipped\s*$", frontmatter(path), re.M)
    }


def realized(src: dict[str, str]) -> set[tuple[str, str]]:
    return {
        (n, m)
        for n in src
        for m in src
        if m != n and re.search(r"\b" + re.escape(m) + r"\b", src[n])
    }


def incidence(src: dict[str, str]) -> dict[str, set[str]]:
    return {
        n: {a for a, r in ARTIFACTS.items() if re.search(r, t)} for n, t in src.items()
    }


def latent(src: dict[str, str]) -> set[tuple[str, str]]:
    inc = incidence(src)
    return realized(src) | {
        (n, m) for n in src for m in src if m != n and inc[n] & inc[m]
    }


def isolated(members: list[str], edges: set[tuple[str, str]]) -> list[str]:
    joined = {x for a, b in edges if a in members and b in members for x in (a, b)}
    return [m for m in members if m not in joined]


def check_index(src: dict[str, str]) -> int:
    """The disposition map is single-valued and covers exactly ~/bin/claude-*."""
    rows = re.findall(r"^\| `([\w.-]+)` *\|", INDEX.read_text(), re.M)
    dup = [t for t, n in collections.Counter(rows).items() if n > 1]
    unindexed = sorted(set(src) - set(rows))
    # Indexed rows are allowed to name no file in ~/bin when the tool never
    # lived there (`git-localhost-store`) or has shipped out of it -- a shipped
    # member is expected to be absent, and PATH is where it answers now.
    exempt = {"git-localhost-store"} | {
        m for pkg, ms in clusters().items() if pkg in shipped() for m in ms
    }
    absent = sorted(set(rows) - set(src) - exempt)
    print(f"duplicate rows:     {dup or 'none'}")
    print(f"unindexed:          {unindexed or 'none'}")
    print(f"indexed but absent: {absent or 'none'}")
    return 1 if dup or unindexed or absent else 0


def scanned_roots(source: str) -> set[str]:
    """The ~-relative roots a twin walks, read off its ROOTS assignment."""
    line = next(x for x in source.splitlines() if x.startswith("ROOTS"))
    return set(re.findall(r'Path\.home\(\) / "([^"]+)"', line))


def check_twins(src: dict[str, str]) -> int:
    """The twins duplicate knowledge, share no edge, and have already drifted."""
    a, b = TWINS
    roots = {t: scanned_roots(src[t]) for t in TWINS}
    for t in TWINS:
        print(f"{t:24} scans {' '.join(sorted(roots[t]))}")

    referenced = any(
        re.search(rf"\b{re.escape(y)}\b", src[x]) for x, y in ((a, b), (b, a))
    )
    print(f"{'edge between them':24} {'yes' if referenced else 'NO'}")

    drift = 0
    for root in sorted(roots[a] ^ roots[b]):
        blind = [t for t in TWINS if root not in roots[t]]
        seen = sum(len(list((pathlib.Path.home() / root).rglob(g))) for g in TASK_GLOBS)
        print(f"{'~/' + root:24} {seen} task files, invisible to {', '.join(blind)}")
        drift += seen

    status_re = {
        t: re.findall(r"^STATUS\w* = re\.compile\((.*)\)$", src[t], re.M) for t in TWINS
    }
    print(
        f"{'status regex':24} {'identical' if len(set(map(str, status_re.values()))) == 1 else 'differs'}"
    )
    return 1 if drift or not referenced else 0


def verdict(
    pkg: str, members: list[str], G: Edges, Gplus: Edges, ship: set[str] = frozenset()
) -> str:
    if pkg in ship:
        gone = [m for m in members if not shutil.which(m)]
        if gone:
            return f"BROKEN  {pkg}: shipped, but {', '.join(gone)} is not on PATH"
        return f"SHIPPED {pkg}: {', '.join(members)} on PATH, not in ~/bin"
    iso, iso_plus = isolated(members, G), isolated(members, Gplus)
    if len(members) == 1:
        return f"SINGLE  {pkg}"
    if not iso:
        return f"SEAMED  {pkg}"
    if not iso_plus:
        return f"LATENT  {pkg}: {', '.join(iso)} share artifacts, not code"
    return f"NONE    {pkg}: {', '.join(iso_plus)} share nothing with siblings"


def main(argv: list[str]) -> int:
    src = tools()
    G, Gplus = realized(src), latent(src)

    if "--index" in argv:
        return check_index(src)
    if "--twins" in argv:
        return check_twins(src)
    if "--cluster" in argv:
        members = argv[argv.index("--cluster") + 1].split(",")
        line = verdict("(given)", members, G, Gplus)
        print(line)
        return 1 if line.startswith("NONE") else 0
    if "--edges" in argv:
        for a, b in sorted(G):
            print(f"  {a} -> {b}")
    if "--isolated" in argv:
        print(f"  isolated in G: {', '.join(isolated(sorted(src), G))}")
    if "--artifacts" in argv:
        for n, arts in sorted(incidence(src).items()):
            print(f"  {n:26} {' '.join(sorted(arts)) or '-- none --'}")

    index, ship = clusters(), shipped()
    bad = 0
    for pkg, members in sorted(index.items()):
        if pkg in NOT_A_PACKAGE:
            print(f"--      {pkg}: {', '.join(members)}")
            continue
        line = verdict(pkg, members, G, Gplus, ship)
        print(line)
        bad += line.startswith(("NONE", "BROKEN"))

    unindexed = set(src) - {m for ms in index.values() for m in ms}
    if unindexed:
        print(f"UNINDEXED {', '.join(sorted(unindexed))}", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
