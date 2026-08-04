---
name: verify-before-done
description: Forbids calling anything finished without evidence that it works, and requires a deliberate attempt to break it first. Use before saying a task is done, before closing a phase, before any push, and whenever a change touches something a user sees or something that stores data. Use when reporting a result — a number, not an assurance.
---

> **DRAFT — in the review zone, not in force.** Extracted from what the owner
> called his strongest request. Held back from the first wave because it overlaps
> `confidence-check` and a future skill about phases, and that boundary needs his
> ruling before it goes into force.

# Verify before done

**What changes because of this skill:** without it, "done" means the code was
written and nothing obviously broke, and problems reach the owner before they reach
anyone else. With it, "done" means something was measured and something was
deliberately attacked, and the report carries the number rather than the assurance.

**Covers:** proving that finished work actually works, and hunting for what is
broken before the owner finds it.
**Leaves out:** how confidently a *fact* is stated — that is `confidence-check`,
which is about claims from the world. This skill is about claims from your own
work. Also the ceremony of closing a phase, which is a separate job.

---

## 1. Proof, not assertion

> "The suite is green, 47 tests." · "1.06 s → 0.40 s on the real dataset." · "The
> note reached storage and survived a reload."

Those are evidence. **"I checked it" is not**, and neither is "it should work now".
The difference is whether the reader could disagree with you: a number can be
argued with, a reassurance can only be believed or not.

State the evidence in the same message as the claim. Evidence that arrives only
when challenged reads as something found afterwards.

## 2. The standard scales with what is at risk

| What changed | What "done" requires |
| --- | --- |
| An internal utility | tests pass, and they cover what changed |
| Anything a user sees | the above, plus a check in the real environment against real data |
| Anything that stores data | the above, plus a deliberate attempt to lose or corrupt it |
| Anything about speed or size | a before and after measurement, on real data |

The middle row is where most failures hide: unit tests cannot see a button covered
by another element, an empty state that renders as a blank page, or a message that
says `undefined`. A test suite passing is evidence about the code, not about the
thing the user meets.

**This standard holds even when it triples the time.** That is the owner's explicit
instruction, and it is the whole point — the cost is the mechanism, not a side
effect of it.

## 3. Try to break it before saying it works

Verification confirms; attack discovers. They find different things, and only the
second finds the ones that matter.

Before declaring anything finished, spend real effort trying to make it fail:
duplicate keys, empty values, a value of zero, a name with a quote in it, a dead
network, a partially-written file, a source that changed shape, a visitor who
should not have access, the same action twice.

**Reproduce every candidate finding before fixing it.** A fix aimed at something
you never actually saw fail is a change with no evidence behind it, and it usually
leaves the real fault in place.

**Sort by blast radius, not by ease of fixing.** The natural order is
easiest-first, which is exactly backwards: it spends the attention on what matters
least while it is still fresh.

## 4. What to do with what you find

**Critical** — data loss, a crash, anything letting the wrong person in: fix it
immediately, report afterwards.

**Everything else**: bring it as a list and ask. A medium-severity finding fixed
without asking is a change the owner did not request, arriving in the same breath
as one he did.

## 5. A negative result is a result

If a change did not achieve its goal, **report the numbers and propose reverting**.
Do not keep it because it was work. "Measured 1.06 s → 1.12 s, i.e. no effect, and
it costs the ability to edit in bulk — reverting" is a good outcome; the same
change quietly retained is not.

This is also the honest end of an optimisation: intuition about what is slow is
wrong often enough that the measurement, not the reasoning, decides.

## 6. Suspect your own check first

When a check disappoints, the reflex is to doubt the code. Doubt the harness first:
a test asserting the wrong thing, a fixture that never loaded, a mock that swallowed
the call, a comparison against stale output. Blaming the tooling before verifying
the test has cost more time than any other habit on this list.

---

## Owner preferences

- **This is his strongest stated request** — check your own work, and find the
  problems before he does. Phrased in his own terms: he would rather hear about
  three things you found and fixed than discover one himself.
- **Screenshots are not required.** Numbers and plain statements are enough.
- **Report what was skipped.** A step deliberately not run is fine; a step silently
  not run is not.
- **At every phase boundary, run the full pass** — tests, linters, dependency
  freshness, broken documentation links — and report what needs attention.

---

## Open questions for the owner

**Where does the phase boundary belong?** The last owner preference — the full technical
pass at every phase boundary — is about phases, not about verification. It is here
because there is nowhere else yet. When a phase skill exists it should move, and
this skill should say only what "done" requires for one piece of work.

**Is §6 (suspect your own check) part of this skill or part of debugging?** It fires
during verification, which is why it is here, but it is really a rule about
diagnosing a surprise. If a debugging skill is ever written it has a claim on it.

**Does the table in §2 need a row for data pipelines?** The next project rebuilds
one, and "a run that produces a dataset" fits none of the four rows cleanly — the
risk there is silent partial success, which no existing row catches.
