---
label: GRAD
standing: agent
why:
    - ../levels.kb/audience-is-not-in-the-files.md
    - ../cost.kb/the-testable-set-is-a-threshold-not-a-property.md
---

# Graduation Needs Audience and Either Code Test

`criteria.kb/graduation-from-dotfiles.md` states three tests -- KNOWLEDGE
(worth testing), SUBCOMMANDS (grows them), AUDIENCE (shouldn't ride along) --
and then says two incompatible things about them: "any one is sufficient", and
"when the tests disagree, AUDIENCE decides". Both cannot hold. If any one
suffices, a tool with KNOWLEDGE and no AUDIENCE graduates; if AUDIENCE
decides, it stays.

The rule the data actually follows:

> **graduate(*t*) ⟺ AUDIENCE(*t*) ∧ ( KNOWLEDGE(*t*) ∨ SUBCOMMANDS(*t*) )**

AUDIENCE is **necessary**; the other two are jointly sufficient *given* it.
The three tests are not symmetric and never were, because KNOWLEDGE and
SUBCOMMANDS are properties of code while AUDIENCE is a property of people --
the asymmetry `../levels.kb/audience-is-not-in-the-files.md` predicts.

The tests are named, not numbered, for a reason that showed up immediately:
"3 decides" is unreadable at a glance and unauditable in a diff, while
"AUDIENCE decides" is the claim itself.

## Checked against every settled call

| tool | KNOWLEDGE | SUBCOMMANDS | AUDIENCE | rule says | recorded |
|---|---|---|---|---|---|
| `git-localhost-store` | ✓ git internals | ✓ ADRs, modes | ✓ any sync-hostile fs | graduate | graduate |
| `claude-jsonl-display` | ✓ record schema | ✓ ~50 renderers | ✓ anyone reading transcripts | graduate | graduate |
| `claude-s` | ✓ flag family | ~ debug levels | ✗ one harness's needs | **stay** | stay |
| `claude-plan` | ✗ | ✗ | ✗ | retire | retire |

`claude-s` is the case that discriminates the two readings: under "any one is
sufficient" it graduates on KNOWLEDGE, and the kb's own counter-pressure
paragraph says it stays. The conjunctive rule gets it right without an
exception clause -- which is the argument for the correction.

What the table cannot do is discriminate this rule from **AUDIENCE alone**:
every settled row agrees with plain AUDIENCE too, because no settled call has
AUDIENCE ✓ with both code tests ✗. The (KNOWLEDGE ∨ SUBCOMMANDS) conjunct has
therefore never changed a decision -- by this ledger's own bar it is
conjecture, waiting on a tool with a real audience and neither code test. If
such a tool graduates anyway, the conjunct is dead weight; if it stays home,
the conjunct earned its place.

## What it costs

The rule is **not decidable from the files**. Its necessary conjunct is L3,
so no amount of reading answers it (`../levels.kb/audience-is-not-in-the-files.md`).
Two consequences worth accepting deliberately:

- Every graduation call is a ruling, so claims here carry `agent` or `user`
  standing, never `bare`. A `verify:` here would be a lie about what was
  computed.
- The cheap tests cannot be used as a shortcut. KNOWLEDGE and SUBCOMMANDS
  together predict nothing on their own; that is precisely the trap
  `../levels.kb/the-name-abstraction-may-narrow-but-never-decide.md` names,
  one level up.

## The residue this exposes

AUDIENCE for `claude-open-tasks-list` is genuinely open, and the reason is
interesting: its audience is "anyone whose repos carry `.claude/todo.md`",
which is a convention defined by `Skill(llm-subtask)` -- a published skill,
not a personal preference. If that convention counts as upstream, the tool
graduates on KNOWLEDGE ∧ AUDIENCE; if it counts as bukzor's own habit, it
stays. **Nothing in the tool decides this; the skill's readership does.**

## What would kill it

A graduation that came out right while failing AUDIENCE -- a tool with no
audience beyond one config that was nonetheless worth packaging, for reuse
across the author's own machines, say. That would demote it from gate to
tiebreaker, and
would make the decision computable, which would be a considerable
simplification. `claude-s` is the standing test case: if it is ever packaged
and that turns out well, this claim is wrong.

The second conjunct has its own, cheaper defeater, stated above: any settled
call that separates it from plain AUDIENCE, in either direction.
