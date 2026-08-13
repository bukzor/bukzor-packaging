---
label: STREAM
standing: agent
why:
    - tools-are-the-arrows-not-the-objects.md
    - ../cost.kb/cost-splits-into-site-and-item.md
verify: ../composition.py --adapters
---

# A Streaming Filter Is a Monoid Homomorphism

Carrier: sequences of messages under concatenation -- a monoid, with `++` and
the empty stream. Operations: a filter is a map from streams to streams. Law:

> A filter *f* **streams** when it is a monoid homomorphism:
> *f*(*xs* ++ *ys*) = *f*(*xs*) ++ *f*(*ys*). Homomorphisms compose, contain
> the identity, and so form a **wide subcategory** of `PIPE` -- same objects,
> fewer arrows. Everything else is a **fold**: it must see the whole stream
> before it can emit.

Two structural consequences, both of them practical:

- **The streaming prefix of a pipeline is everything before its first fold.**
  A fold precomposed with a homomorphism is a fold; a fold *post*composed with
  anything is still a fold. So the rule is to move folds right. What the fold's
  position sets is the pipeline's *latency* profile -- when output can begin.
  Its **memory** profile is set by the earliest *unbounded-state* stage, and
  the two come apart: dedup streams (prefix-monotone, below) and still holds
  every distinct item. An earlier revision said memory was set by the earliest
  fold; the tool this file already cites disproves it.
- **Adjacent homomorphisms fuse.** Replacing `a | b` by one arrow computing
  *f*<sub>*b*</sub> ∘ *f*<sub>*a*</sub> is licensed by the law, and it elides
  one serialization round trip and one process. This is the only argument for
  "fewer, larger tools" in this ledger that comes from mathematics rather than
  from taste, and it is narrow: it licenses fusing *homomorphisms*, nothing else.

## Homomorphism is sufficient, not necessary

The converse is false and it matters. `claude-open-tasks-list` deduplicates
task lines: it streams fine, and it is **not** a homomorphism, because a
duplicate spanning the split point survives in *f*(*xs*) ++ *f*(*ys*) and dies
in *f*(*xs* ++ *ys*).

The general property is weaker: *f* is **prefix-monotone** -- extending the
input only extends the output, so *f* can be computed incrementally. Every
homomorphism is prefix-monotone; `uniq` is prefix-monotone and not a
homomorphism. A homomorphism on a free monoid is determined by its action on
single messages -- it *is* `concatMap`, stateless per message -- while
prefix-monotone tools carry state, bounded (`uniq`, one message of lookback) or
unbounded (dedup, one entry per distinct item).
Prefix-monotonicity is the honest characterization of streaming;
the homomorphism law is the **decidable special case**, the one a property test
can check by splitting an input at every position. That is why the discipline
worth adopting is *declare which one you are*, not *be a homomorphism*.

## The monoid is a property of the framing, not of the tool

On raw bytes this law is unstatable: bytes concatenate, but almost no filter
respects that concatenation, because splitting a byte stream mid-record is
meaningless. Line-oriented tools are homomorphisms on the *line* monoid -- and
that monoid exists only in the reader's head, recovered by scanning for `\n`
and defeated by an embedded newline.

**A framed message stream makes the monoid explicit, and that is what makes the
law testable.** This is the formal content of the capnproto direction: not speed
and not schemas, but that `++` becomes an operation on the data rather than a
convention about the bytes. Without framing, `f(xs ++ ys) = f(xs) ++ f(ys)` is
a statement about a monoid the format merely implies.

## Standing, honestly

`composition.py --adapters` finds **one** FILTER among 20 tools. This law
therefore ranges over a population of one, and calling it a description of
bukzor's tools would be false. It is a **design rule for the family not yet
written**, filed now because the cheapest moment to fix a calling convention is
before there are callers -- and because it identifies the one property that a
capnp family should be required to declare per tool.

## What would kill it

A tool in the capnp family that is a homomorphism on its declared message type
and still cannot be run streamwise -- which would mean the framing is lying
about where records end. Or, more likely and more interesting: the FILTER count
stays at one, tools keep taking paths, and the pipe category never acquires
enough arrows for fusion to matter. Then this file is premature rather than
wrong, and `an-adapter-is-where-the-environment-leaks-in.md` is where the work
actually was.
