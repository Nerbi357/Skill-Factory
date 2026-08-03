<!-- STAMPED COPY — do not edit.
     Source:      skills/confidence-check/SKILL.md
     Taken:       2026-08-03
     Canonical:   edit the source and rerun .claude/scripts/sync_bundles.py
-->

---
name: confidence-check
description: Marks every fact with how well it is actually known — verified, seen, recalled, or inferred — and forbids inventing a specific. Use whenever stating a URL, price, limit, version, date, field name or coverage figure. Use before describing how any tool, API or platform behaves. Use when a check was blocked rather than answered, and whenever a claim is about to be built on.
---

# Confidence check

**What changes because of this skill:** without it, a plausible URL, limit or
price recalled from memory gets stated as if it were checked — and that fails
silently, late, after work has been built on it. With it, every claim carries how
well it is known, and a gap is reported as a gap instead of being filled.

**Covers:** one thing only — how well a stated fact is actually known, and how to
say so.
**Leaves out:** how to conduct research, what to conclude from it, and how to
shape a report. Those are separate jobs. This skill applies to a single claim, one
claim at a time, wherever claims are made.

---

## 1. Every fact carries its confidence

Four marks. Use them out loud, in the sentence itself, not in a footnote nobody
reads:

| Mark | Means |
| --- | --- |
| **verified** | you fetched it, ran it, or read it in the source just now |
| **seen** | you saw it somewhere credible but did not confirm it yourself |
| **recalled** | it comes from memory or training, unchecked |
| **inferred** | you worked it out; it is reasoning, not observation |

Mixing these silently is how work ends up resting on something plausible that was
never true. The mark costs three words and saves the class of failure that is
hardest to trace, because a wrong fact stated confidently gets built on before
anyone thinks to doubt it.

The mark matters in proportion to what depends on the fact. A passing aside needs
none. **Anything that will be built on carries one.**

### When the thing itself cannot be reached

Often it cannot: the network is blocked, the service is down, the page wants a
login. The mark then attaches to **what you actually did check**, and says so.

*Verified that this repository's code contains that URL* is a different claim from
*verified that the URL works*. Both are honest; only one of them is about the
thing you were asked about. Collapsing them is how a report full of honest-looking
marks still misleads, because the reader assumes the mark refers to the claim
rather than to its shadow.

So name the object, not just the level: "verified — the file contains this string"
beats a bare "verified". And three independent third-party sources agreeing is
real evidence worth reporting as such — it is still `seen`, because none of them
was the thing itself.

## 2. Never invent a specific

A URL, a price, a rate limit, a version number, a date, a field name, a coverage
figure — recalled from memory and presented as checked — is worse than an admitted
gap. An admitted gap gets checked. A confident fabrication gets used.

This is the rule that most often has to be applied against your own fluency: the
specific will arrive in your head feeling exactly as certain as a real one. That
feeling is not evidence. If you cannot say where it came from, it is `recalled`,
and if it matters, go and check it.

**Check before you argue from it.** Building an argument on a recalled specific is
worse than stating the specific alone, because the reasoning around it makes the
specific look examined.

## 3. A blocked check is not a negative result

If the environment refused the request, the network failed, the page needed a
login, or a tool was unavailable — that says **nothing** about the thing being
checked. Report it as blocked, name what blocked it, and leave the question open.

Collapsing "I could not check" into "it is not there" produces confident wrong
conclusions that look like findings. The two are opposites: one is an absence of
evidence about the world, the other is evidence about the world.

## 4. Report the hole instead of filling it

When something could not be established, say so, say why, and say what it would
take to close it. A named hole is a task. A filled hole is a bug with a long fuse.

This includes partial answers. "Three of the five fields are documented; the other
two I could not find" is a useful result. Quietly describing all five as though
they were equally established is not.

## 5. A number without its date will go stale

A measurement is a fact about one moment. It stays true forever **if it carries
where and when it came from** — "the run of 2026-07-24 cost $7.14" is permanently
accurate. Strip the date and the same number silently becomes false the next time
anything changes, without ever being marked as doubtful.

So a figure that can drift is stated with its moment attached, or not stated as a
fact at all. This is a confidence rule, not a formatting one: an undated number is
a claim whose confidence decays invisibly, which is the one failure this skill
exists to prevent.

---

## Owner preferences

- **Confidence marks are expected, not optional.** They entered the working
  contract after a source study in which the sandbox silently blocked several
  checks; the marks are what made the resulting report usable.
- **An admitted gap is never held against you. A fabricated specific is.** Say "I
  do not know" plainly rather than producing something plausible.
- **When a platform's behaviour matters to a decision, read the documentation
  before arguing from it** — not after the argument has been made. This rule
  exists because the opposite happened: an architecture was proposed on a recalled
  belief about how skills are discovered, and the documentation contradicted it.
