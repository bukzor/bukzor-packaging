#!/usr/bin/env python3
"""Check the retirement laws of retirement.kb/ against what this machine recorded.

Deletion is an action with a quotient of its own: the maintenance toll it avoids
over the benefit it forfeits. Both terms are recurrence counts, and two
populations here have been recording them all along -- every Bash call the
harness has made (`~/.claude/projects/**/*.jsonl`) and every command bukzor typed
(`~/.bash_history`). Neither had been read until this check.

Usage: retirement.py [--observed]

  --observed  per tool: how often it was named, invoked, and edited

Two measures, and the interesting thing is that the sound one is useless:

  named    the name anywhere in a command line. **Over**-approximates use, so a
           count of zero would be the sound direction for a deletion -- and it
           is zero for nothing, because studying twenty tools types their names
           twenty times. An over-approximation is polluted by its own analyst.
  called   the name in command position, past pipes and env assignments.
           **Under**-approximates: `xargs claude-slug` and a name inside a
           heredoc both miss. So a positive count is sound and a zero is not.

The verdict therefore rests on the unsound direction, deliberately, and says so:
zero attested invocations is a *candidate*, never a decision. What neither
population sees is a caller that is not a shell this machine logged -- a git
hook, a cron entry, another checkout. `git-localhost-store` calls `claude-path`
on every commit in ~50 repositories, and if that were the only caller the tool
would read as dead here. `SUBSUME` rests on the reference graph for that reason.

`touch` is the toll side, and under-approximates worse than `called` does: most
of the real charge is a sweep that never names the file -- an `ls ~/bin`, a
directory-wide grep, a tab completion. It is reported because TOLL claims the
charge is per encounter, and this is the only encounter kind with a record.

Both terms were polluted by this study, and in the same direction: formalizing
twenty tools typed their names (inflating `named`) and edited their files
(inflating `touch`), which made the ratio's bias *ambiguous* rather than
conservative -- worse than a known direction. Hence the temporal cut. Agent log
events dated on or after STUDY are dropped, because stratifying by a timestamp
uses something the analyst cannot influence, while stratifying by topic would
drop real uses along with the mentions and manufacture the zeros this check hunts.

The cut was not a precaution. Auditing whether the one unattested tool still works
meant *running* it, which erased the finding: "no invocation attested" went to zero
of twenty because its auditor became its first caller. The residual weakness is
narrow and statable -- a tool whose use began after 2026-08-09 reads as unused --
and `~/.bash_history` is exempt because bash records no times, so bukzor's own
invocations are counted entire and are the corpus this cut does not reach.

Exits nonzero while a tool has no attested invocation and no disposition, while
a tool dispositioned `retire` is still installed, or while a settled decision in
the index has no terms recorded beside it.
"""

from __future__ import annotations

import collections
import dataclasses
import json
import pathlib
import re
import sys
import typing
from collections.abc import Iterable, Iterator, Mapping

from composition import population
from seams import clusters

LOGS = pathlib.Path.home() / ".claude" / "projects"
HISTORY = pathlib.Path.home() / ".bash_history"
BIN = pathlib.Path.home() / "bin"
INDEX = pathlib.Path(__file__).resolve().parent.parent / "dispositions.md"
TERMS = "## Decision terms"
# The day the packaging census opened. Agent activity from here on is this
# study's own, so it is cut: see the docstring.
STUDY = "2026-08-09"

# Every point in a command line where a new command can start.
BREAKS = re.compile(r"\$\(|[|;&\n()`]")
ASSIGN = re.compile(r"^\w+=")
NAMED = re.compile(r"claude-[a-z][a-z0-9-]*")
# A bare tool name and nothing else: the heredoc lines and prose that reach
# command position otherwise arrive as `claude-path",` and `claude-slug's`.
TOKEN = re.compile(r"^claude-[a-z][a-z0-9-]*$")
NAME = re.compile(r"^`([\w./-]+)`$")

Event = tuple[str, str, str]


@dataclasses.dataclass
class Tally:
    """What the recorded populations attest about one tool.

    Agent and shell counts stay apart because they answer to different people:
    a tool can live entirely on bukzor's recurrence with none of the harness's,
    and `claude-jsonl-display` does.
    """

    named: int = 0
    shell: int = 0
    called: int = 0
    touched: int = 0
    last: str = ""


def fields(value: object) -> Mapping[str, object]:
    """A JSON object's fields, or none -- a log line is untyped by nature."""
    if isinstance(value, dict):
        return typing.cast(Mapping[str, object], value)
    return {}


def head(piece: str) -> str:
    """The command word of one command position, past any env assignments."""
    for word in piece.split():
        if not ASSIGN.match(word):
            return word.rsplit("/", 1)[-1]
    return ""


def called(text: str) -> set[str]:
    """Tool names in command position. Under-approximate, so a hit is sound."""
    heads = (head(piece) for piece in BREAKS.split(text))
    return {name for name in heads if TOKEN.match(name)}


def named(text: str) -> set[str]:
    """Tool names anywhere. Over-approximate, so only a zero would be sound."""
    return set(NAMED.findall(text))


def line_events(line: str) -> Iterator[Event]:
    record = fields(json.loads(line))
    stamp = str(record.get("timestamp", ""))[:10]
    content = fields(record.get("message")).get("content")
    if not isinstance(content, list):
        return
    for entry in typing.cast(list[object], content):
        block = fields(entry)
        if block.get("type") != "tool_use":
            continue
        args = fields(block.get("input"))
        command = args.get("command")
        target = args.get("file_path")
        if block.get("name") == "Bash" and isinstance(command, str):
            yield stamp, "bash", command
        elif isinstance(target, str):
            yield stamp, "file", target


def read_log_events() -> Iterator[Event]:
    """Harness Bash commands and file targets recorded *before* the study opened."""
    for path in sorted(LOGS.glob("**/*.jsonl")):
        with path.open(errors="replace") as lines:
            for line in lines:
                if '"tool_use"' in line:
                    yield from (e for e in line_events(line) if e[0] and e[0] < STUDY)


def read_shell_events() -> Iterator[Event]:
    """Every command bukzor typed. Undated: bash records times only on request."""
    if not HISTORY.exists():
        return
    for line in HISTORY.read_text(errors="replace").splitlines():
        if not line.startswith("#"):
            yield "", "shell", line


def tally(events: Iterable[Event]) -> dict[str, Tally]:
    rows: dict[str, Tally] = collections.defaultdict(Tally)
    for stamp, kind, payload in events:
        match kind:
            case "bash" | "shell":
                for name in named(payload):
                    row = rows[name]
                    row.named += 1 if kind == "bash" else 0
                    row.shell += 1 if kind == "shell" else 0
                    row.last = max(row.last, stamp)
                for name in called(payload):
                    rows[name].called += 1
            case "file":
                name = payload.rsplit("/", 1)[-1]
                if NAMED.fullmatch(name):
                    rows[name].touched += 1
            case _:
                raise AssertionError(kind)
    return dict(rows)


def uncalled(rows: Mapping[str, Tally], tools: Iterable[str]) -> list[str]:
    """Tools no recorded shell was seen to invoke -- `PRUNE`'s zero denominator."""
    return [name for name in sorted(tools) if not rows.get(name, Tally()).called]


def cells(line: str) -> list[str]:
    """One table row's cells, or none if the line is not a row."""
    if not line.startswith("|"):
        return []
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def unpriced() -> tuple[list[str], int]:
    """Settled decisions whose terms are not on record -- `TERMS`' obligation.

    The index marks a decision as made by bolding its *disposition*, which is the
    second-to-last cell in both of its tables (`why` is always last). Testing the
    whole row instead would count any bolded phrase in a `why` cell as a decision,
    which it did until an emphasised note in one tripped it. A decision is priced
    when the first cell of some row under the terms heading names it; an explicit
    `--` counts, because "never estimated" is a record and a degenerate decision
    is a finding.
    """
    head, _, terms = INDEX.read_text().partition(TERMS)
    rows = [cells(line) for line in head.splitlines()]
    decided = sorted(
        NAME.findall(row[0])[0]
        for row in rows
        if len(row) > 2 and NAME.match(row[0]) and "**" in row[-2]
    )
    priced = {
        word.strip("`")
        for row in map(cells, terms.splitlines())
        if row
        for word in row[0].split()
    }
    return [name for name in decided if name not in priced], len(decided)


def show_observed(rows: Mapping[str, Tally], tools: Iterable[str]) -> None:
    print(f"{'tool':<26}{'named':>7}{'shell':>7}{'called':>8}{'touch':>7}  last")
    for name in sorted(tools):
        row = rows.get(name, Tally())
        print(
            f"{name:<26}{row.named:>7}{row.shell:>7}{row.called:>8}{row.touched:>7}"
            f"  {row.last or '--'}"
        )


def check(observed: bool) -> int:
    tools = population()
    rows = tally([*read_log_events(), *read_shell_events()])
    retiring = set(clusters().get("retire", ()))

    logs = len(list(LOGS.glob("**/*.jsonl")))
    print(
        f"population  {len(tools)} tools on PATH; ~/bin holds {len(list(BIN.iterdir()))}"
    )
    print(f"attested    {logs} session logs, cut at {STUDY} + ~/.bash_history")

    if observed:
        print()
        show_observed(rows, tools)

    dead = uncalled(rows, tools)
    print(f"\nno invocation attested: {len(dead)} of {len(tools)}")
    for name in dead:
        row = rows.get(name, Tally())
        state = "retire" if name in retiring else "UNDECIDED"
        print(f"  {name:<26}named {row.named + row.shell:>4}x, never invoked  {state}")

    stayed = sorted(name for name in retiring if (BIN / name).exists())
    print(f"\ndispositioned retire, still installed: {', '.join(stayed) or 'none'}")

    silent, decided = unpriced()
    print(f"\nsettled decisions with no recorded terms: {len(silent)} of {decided}")
    for name in silent:
        print(f"  {name}")

    undecided = [name for name in dead if name not in retiring]
    if undecided or stayed:
        print(
            "\nNeither block is a verdict on its own. An unlogged caller is"
            "\ninvisible here, so PRUNE wants a reference search before a"
            "\ndeletion -- but an undecided row and an undone retirement are"
            "\nboth states RATCHET says the index should not hold for long."
        )
    return 1 if undecided or stayed or silent else 0


def main(argv: list[str]) -> int:
    if argv and argv[0] not in ("--observed",):
        print(__doc__, file=sys.stderr)
        return 2
    return check(observed=bool(argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
