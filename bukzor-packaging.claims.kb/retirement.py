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

Exits nonzero while a tool has no attested invocation and no disposition, or
while a tool dispositioned `retire` is still installed.
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

# Every point in a command line where a new command can start.
BREAKS = re.compile(r"\$\(|[|;&\n()`]")
ASSIGN = re.compile(r"^\w+=")
NAMED = re.compile(r"claude-[a-z][a-z0-9-]*")
# A bare tool name and nothing else: the heredoc lines and prose that reach
# command position otherwise arrive as `claude-path",` and `claude-slug's`.
TOKEN = re.compile(r"^claude-[a-z][a-z0-9-]*$")

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
    """Every Bash command and file target the harness has recorded."""
    for path in sorted(LOGS.glob("**/*.jsonl")):
        with path.open(errors="replace") as lines:
            for line in lines:
                if '"tool_use"' in line:
                    yield from line_events(line)


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
    print(f"attested    {logs} session logs + ~/.bash_history")

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

    undecided = [name for name in dead if name not in retiring]
    if undecided or stayed:
        print(
            "\nNeither block is a verdict on its own. An unlogged caller is"
            "\ninvisible here, so PRUNE wants a reference search before a"
            "\ndeletion -- but an undecided row and an undone retirement are"
            "\nboth states RATCHET says the index should not hold for long."
        )
    return 1 if undecided or stayed else 0


def main(argv: list[str]) -> int:
    if argv and argv[0] not in ("--observed",):
        print(__doc__, file=sys.stderr)
        return 2
    return check(observed=bool(argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
