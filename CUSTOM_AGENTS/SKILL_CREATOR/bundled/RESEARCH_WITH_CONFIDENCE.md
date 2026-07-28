<!-- STAMPED COPY — do not edit.
     Source:      CUSTOM_SKILLS/RESEARCH_WITH_CONFIDENCE/SKILL.md
     Taken:       2026-07-28
     Canonical:   edit the source and rerun .claude/scripts/sync_bundles.py
-->

---
name: RESEARCH_WITH_CONFIDENCE
description: Marks every fact with how well it is actually known — verified, seen, recalled, or inferred — and forbids inventing a specific. Use whenever gathering facts, reading documentation, checking a source, or stating a URL, price, limit, version, date or coverage figure. Use before describing how any tool, API or platform behaves. Use when a check was blocked rather than answered, and whenever a claim is about to be built on.
---

# Research with confidence

**What changes because of this skill:** without it, a plausible URL, limit or
price recalled from memory gets stated as if it were checked — and that fails
silently, late, after work has been built on it. With it, every claim carries how
well it is known, and a gap is reported as a gap instead of being filled.

**Covers:** how facts are gathered and how confidently they are stated.
**Leaves out:** whether finished work actually works — that is verification, a
different job. Also how numbers are written into repository prose, which belongs
with the repository's own standards.

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
worse than stating the specific alone, because the reasoning around it makes it
look examined.

## 3. A blocked check is not a negative result

If the environment refused the request, the network failed, the page needed a
login, or a tool was unavailable — that says **nothing** about the thing being
checked. Report it as blocked, name what blocked it, and leave the question open.

Collapsing "I could not check" into "it is not there" produces confident wrong
conclusions that look like findings. The two are opposites: one is an absence of
evidence about the world, the other is evidence about the world.

## 4. Report the hole instead of filling it

When something could not be established, say so, say why, and say what it would
take. A named hole is a task. A filled hole is a bug with a long fuse.

This includes partial answers. "Three of the five fields are documented; the other
two I could not find" is a useful result. Quietly describing all five as though
they were equally established is not.

## 5. Check the free option before the paid one, and check whether it exists

Before building something, look for whether it already exists and is maintained.
Before paying, look for the free path. Finding a published artefact that already
does the job is often the single highest-value hour available, and it is
frequently skipped because building feels more like progress than searching does.

## 6. A measurement keeps its number; a description should not

A number that came from one moment stays true forever **if it carries where and
when it came from**: "the run of 2026-07-24 cost $7.14 for about four thousand
companies" is permanently accurate. The same number written into a description of
what something *is* goes stale silently and starts contradicting its neighbours:
"the dataset has 4,040 rows" is wrong after the next rebuild.

So: measurements are dated and keep their precision. Descriptions say "several
thousand" and let the running system report the exact figure.

## 7. End with what you would do

Research exists to support a decision, and marks alone do not make one. A report
scrupulously honest about every fact and silent about what to do with them hands
the entire judgement back untouched — which is the failure mode this discipline
invites, because carefulness feels like completion.

Finish with three lines:

- **What I would do on this evidence** — the recommendation, plainly.
- **What it rests on** — which of the marked facts it actually depends on.
- **What would change it** — the single check that would most move the answer.

The third line is the one that pays. It turns an open question into a task with a
known cost, so the gap stops being a permanent asterisk and becomes something
someone can go and close.

When the evidence genuinely does not support a recommendation, **that is the
recommendation** — say it outright rather than leaving it to be inferred from a
wall of qualified facts.

---

## Owner preferences

- **Confidence marks are expected, not optional.** They were added to the working
  contract after a source study in which the sandbox silently blocked several
  checks; the marks are what made the resulting report usable.
- **An admitted gap is never held against you. A fabricated specific is.** Say "I
  do not know" plainly rather than producing something plausible.
- **When a platform's behaviour matters to a decision, read the documentation
  before arguing from it** — not after the argument has been made. This rule
  exists because the opposite happened: an architecture was proposed on a recalled
  belief about how skills are discovered, and the documentation contradicted it.
- Depth of explanation by default is the result and what it means for the owner,
  not the internals. Go deeper when asked.

---

## Provenance

Maturity: **L3 measured** · Since: 2026-07-28 · Sources: the owner's
`AI_INSTRUCTIONS` §7a, and §8 of his `living-project` skill.

The only artifact in the library carrying evidence rather than an assertion. Two
sessions that had not written it were given the same real research task — one with
this folder and told only to follow it, one with nothing. Both reports ran to
roughly 350 lines. The one with the skill carried **sixty-odd confidence marks
distributed through the body**; the baseline carried **one**.

The difference was not honesty — the baseline was honest — but its *granularity*.
The baseline put its caution in one global caveat, which tells a reader the whole
report is equally shaky and gives no way to tell the solid parts from the
secondhand ones. The marked report lets a reader build on what was verified and go
check what was not. Every network route to the source was blocked in both runs, so
this also exercised the rule that a blocked check is not a negative result: both
respected it, and the marked run additionally said what it had verified *about* —
the contents of third-party code, not the behaviour of the API.

### Changelog

- **2026-07-28 — created.** Extracted as the first skill in the library because it
  is small, sharp and applies to almost every task. §6 (measurements versus
  descriptions) was pulled in from `AI_INSTRUCTIONS` §10, where it sat among
  repository rules although it is a rule about stating facts.
- **2026-07-28 — what "verified" means when the thing cannot be reached (§1).**
  From the cold read: the session invented a `verified (file contents)` mark for
  itself, because in a blocked environment it could only confirm what a
  third-party repository contained, never that the API worked. It closed the gap
  unprompted; the next session might not. Now stated — name the object of the
  verification, not just its level.
- **2026-07-28 — end with what you would do (§7).** Also from the cold read, and
  the more serious of the two. The two sessions reached **opposite** operational
  conclusions from the same absence of direct evidence — one said the API was down
  and to build against the bulk file, the other treated the same signal as routine
  maintenance. Neither could check. Per-fact honesty was excellent and the bottom
  line was left for the reader to assemble. Research exists to serve a decision,
  so the skill now requires one, plus the single check that would change it.

### Considered and turned down

- **2026-07-28 — a formal trigger-test file** (`evals/triggers.md` with phrases
  that must and must not fire the skill). Dropped before it was written: trigger
  tests prove a description auto-fires, and this library is delivered by
  repository access and by sending folders, where routing is explicit. What needs
  proving instead is that a session reading the folder cold does the right thing.
