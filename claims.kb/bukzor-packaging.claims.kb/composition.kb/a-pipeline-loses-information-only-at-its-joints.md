---
label: ROUNDTRIP
standing: agent
why:
    - tools-are-the-arrows-not-the-objects.md
    - a-streaming-filter-is-a-monoid-homomorphism.md
---

# A Pipeline Loses Information Only at Its Joints

Carrier: a command modelled as `main = render ∘ f ∘ parse`, with *f* the pure
core. Then `a | b` computes

> `render_b ∘ f_b ∘ (parse_b ∘ render_a) ∘ f_a ∘ parse_a`

against the pure composite `f_b ∘ f_a`. Law:

> **The two agree exactly when `parse_b ∘ render_a = id`.** The wire format must
> be a **retraction**: every type a retract of its encoding, `dec ∘ enc = id`.
> The shell is a *lax* functor from pure functions to commands, and the whole of
> the laxity sits at the joints.

That is a strong, cheap result: to trust a pipeline, you do not have to reason
about the pipeline. You check one round-trip property per format, and
composition takes care of the rest.

## Three corollaries, in descending obviousness

**Only one direction is needed.** `enc ∘ dec = id` is a different and usually
false demand -- two encodings can denote one value -- so what is wanted is a
retraction, not an isomorphism. Capnp's *canonical form* is precisely the tool
for the rare case where equality of encodings must be equality of values, and
asking for it by default is over-buying.

**The check is generatable.** `dec(enc(x)) == x` over generated values is one
property test per schema, mechanical from the schema itself. Of everything the
capnproto direction could bring, this is the first thing to build, because it
converts the law above from an assumption into CI.

**The law is scoped by `STREAM`.** For non-homomorphic tools the composite can
depend on interleaving and buffer boundaries rather than only on values -- a
fold that flushes on a timer, anything that reads a TTY. On that part of the
category the joints are not the only source of loss, and this claim's defeater
is already realized there. The homomorphic subcategory is where it holds.

## Smallest instance: an encoder with no `dec`, on purpose

The store-key encoding maps *every* non-alphanumeric character to one `-`. It is
not injective, so it has no left inverse, and no discipline can give it one.
`claude-code-archeology` documents that it must never *invert* the encoding, and
that prose is the whole safety mechanism.

Read through this law, that stops being a caveat and becomes a placement rule:
**a non-injective encoding belongs at the end of a pipe, never in the middle.**
A store key is a terminal object -- something to name a directory with, not
something a downstream tool can parse.

The second instance says the same thing from the other side. `claude-jsonl-display`
renders ANSI that nothing parses back; `uncolor-jsonl` is an attempted `dec` and
is lossy by construction, since the colors are gone. So `display` is terminal
too, and the census agreeing -- a FILTER with nothing downstream of it -- is
evidence rather than coincidence.

## What would kill it

Information lost in a pipeline whose every joint round-trips faithfully. Beyond
the timing case already conceded, a candidate would be a joint that loses
*identity* while preserving value: two records that encode to the same bytes and
must stay distinguishable downstream. If that shows up in the capnp family, the
law needs the retraction stated on a richer object than the message type.
