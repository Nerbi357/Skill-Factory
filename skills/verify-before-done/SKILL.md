---
name: verify-before-done
description: Forbids calling anything finished without evidence that it works, and requires a deliberate attempt to break it first. Use before saying a task is done, before closing a phase, before any push, and whenever a change touches something a user sees, something that stores data, or a run that produces a dataset. Use when reporting a result — a number, not an assurance.
---

# Verify before done

**What changes because of this skill:** without it, "done" means the code was
written and nothing obviously broke, and the owner is the one who finds the
problems. With it, "done" means something was measured and something was
deliberately attacked, and the report carries the number rather than the
assurance.

**Covers:** proving that finished work actually works, and hunting for what is
broken before the owner finds it — for a single piece of work, and for everything
accumulated by a phase boundary.
**Leaves out:** how confidently a *fact* is stated — that is `confidence-check`,
which marks a claim about the world as verified, seen, recalled or inferred. This
skill is about claims from your own work. It also leaves out everything else that
happens at a phase close — the review offer, the choice of what comes next — and
keeps only the technical pass.

---

## 1. Proof, not assertion

Three shapes an evidence sentence takes:

> "The suite is green, 47 tests." · "1.06 s → 0.40 s on the real dataset." · "The
> note reached storage and survived a reload."

Those are evidence. **"I checked it" is not**, and neither is "it should work now".
The difference is whether the reader could disagree with you: a number can be
argued with, a reassurance can only be believed or not.

State the evidence in the same message as the claim. Evidence that arrives only
when challenged reads as something found afterwards.

**Say what you did not check.** A step deliberately skipped is a normal part of a
report — the environment was unavailable, the case was out of scope, the fixture
would have cost an hour. A step silently skipped turns the whole report into a
guess, because the reader cannot tell which claims were tested and which were
assumed. Name the gap and what would close it.

## 2. The standard scales with what is at risk

| What changed | What "done" requires |
| --- | --- |
| An internal utility | tests pass, and they cover what changed |
| Anything a user sees | the above, plus a check in the real environment against real data |
| Anything that stores data | the above, plus a deliberate attempt to lose or corrupt it |
| Anything about speed or size | a before and after measurement, on real data |
| A run that produces data | a count and a shape check against what a complete run produces |

The rows are cumulative. A change matching more than one takes the union of what
they ask for, and the order is a hierarchy rather than a list of alternatives.

The user-facing row is where most failures hide: unit tests cannot see a button
covered by another element, an empty state that renders as a blank page, or a
message that says `undefined`. A test suite passing is evidence about the code,
not about the thing the user meets.

When the real environment cannot be reached — no network, no credentials, no
sandbox that resembles production — that is a **blocked check, not a passed one**.
Say which row you could not satisfy and what would satisfy it. Substituting a
lesser check and calling the row met is the failure this row exists to prevent.

The data row exists because a half-finished run does not look broken. It leaves a
file of the right kind, with the right columns, in the right place — only smaller,
and nothing in it says so. So the evidence is the count set against what a full
run produces, plus the tail: the last row, the latest date, the inputs that
yielded nothing at all. **An exit code of zero is the weakest claim available
about a data run**, because the most common failure is one that ends politely.

**The standard does not bend when meeting it costs more than the change did.**
That is not an unfortunate side effect of the rule; it is the rule. A verification
budget that is the first thing dropped under time pressure buys nothing, because
the occasions when it is dropped are exactly the occasions that produce the
failures.

## 3. Try to break it before saying it works

Verification can only find what you thought to assert. Attack finds what you did
not — which is why they are separate acts, and why the second is the one that gets
skipped.

Before declaring anything finished, spend real effort trying to make it fail. The
vectors are the assumptions the change makes about its input, its environment and
its ordering: name those, then violate each one. Duplicate keys, empty values, a
value of zero, a name with a quote in it, a dead network, a partially-written
file, a source that changed shape, a visitor who should not have access, the same
action twice — those are what the method produces, not the method itself.

**Reproduce every candidate finding before fixing it.** A fix aimed at something
you never actually saw fail is a change with no evidence behind it, and it usually
leaves the real fault in place. A finding you cannot reproduce is not discarded —
record it with the conditions you tried, and say so in the report. An unreproduced
finding is a named hole, and naming it is what lets someone else close it.

**Sort by blast radius, not by ease of fixing.** The natural order is
easiest-first, which is exactly backwards: it spends the attention on what matters
least while it is still fresh.

## 4. What to do with what you find

Finding it is never the question. A problem you found is better than the same
problem found by the owner, whatever its size. The only question is whether
repairing it is a judgement call.

**Not a judgement call — fix it, then report.** The fault is unambiguous and the
repair has one obvious form: a crash, data being lost, the wrong person let in, a
dead link, an off-by-one in behaviour already agreed. Asking first buys nothing
here, and where the damage is live it costs.

**A judgement call — bring it and ask.** The fault is real but the repair encodes
a decision: which of two behaviours is correct, what the empty case should show,
whether the slow path is worth restructuring. Deciding one of those alone delivers
a change nobody requested in the same breath as one that was, and the diff does
not distinguish them.

Urgency overrides the second rule and nothing else. If a judgement call cannot
wait, make the smallest version that stops the damage, and say in the same message
that it was yours and how to reverse it.

## 5. A change that did not work is reported, not kept

If a change did not achieve its goal, **report the numbers and propose reverting**.
Do not keep it because it was work. "Measured 1.06 s → 1.12 s, i.e. no effect, and
it costs the ability to edit in bulk — reverting" is a good outcome; the same
change quietly retained is not.

This is a measured failure, not an absent measurement. A check the environment
refused to run says nothing at all and is reported as blocked — that distinction
belongs to `confidence-check`, which marks how well a claim is known.

This is also the honest end of an optimisation: intuition about what is slow is
wrong often enough that the measurement, not the reasoning, decides.

## 6. Suspect your own check first

When a check disappoints, the reflex is to doubt the code. Doubt the harness
first: a test asserting the wrong thing, a fixture that never loaded, a mock that
swallowed the call, a comparison against stale output. The order pays because it
is asymmetric — confirming the harness is cheap, and chasing a fault that was
never in the code is not.

## 7. At a boundary, verify the whole, not the change

Everything above governs one piece of work. At the close of a phase the unit
becomes everything that accumulated inside it: run the tests and the linters over
all of it, confirm the dependencies are still the ones you think they are, and
follow the documentation links. Report what needs attention rather than silently
fixing it all.

It is a separate pass because regressions live between pieces, not inside them.
Each change was verified against itself; nothing so far has asked whether they
still work together, and the boundary is the last moment when that answer is
cheap.

---

## Owner preferences

- **This is his strongest stated request:** check your own work, and find the
  problems before he does. In his own terms — he would rather hear about three
  things you found and fixed than discover one himself. It governs what reaches
  him, not what you may decide alone; §4 draws that line.
- **Screenshots are not required.** Numbers and plain statements are enough.
