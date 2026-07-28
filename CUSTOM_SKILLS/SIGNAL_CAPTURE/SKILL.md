---
name: SIGNAL_CAPTURE
description: Records observations about how the work is going into a SIGNALS.md file, so they can later improve the skill library instead of being forgotten. Use in every project, continuously. Use the moment the owner corrects you, when something takes more exchanges than it should have, when something goes unusually well, when you explain the same thing twice, when a task arrives that no skill covers, or when a claim of yours turns out to be wrong. Use at the close of a phase to offer a short review.
---

# Signal capture

**What changes because of this skill:** without it, everything learned about *how*
to work with this owner evaporates when the session ends, and the same friction
recurs in the next project. With it, those moments land in a file while they are
still exact, and the skill library improves from evidence rather than from
someone's memory of a bad afternoon.

**Covers:** noticing and recording observations about the collaboration itself,
and offering a review when enough have piled up.
**Leaves out:** deciding what any of it should change. That judgement belongs to
the review, where the owner rules — writing a signal is not proposing a fix.

---

## 1. What a signal is

A **raw observation about how the work went**, written when it happened.

Rawness is the point. A signal is not a decision, not a fix, and not a rule. If
every remark became a rule immediately, the guidance would fill with noise and
start contradicting itself within a month. A signal is material; it becomes a
change later, if the owner says so.

This means you record things you disagree with, and things whose implication you
cannot see yet. Judging on the way in defeats the mechanism.

## 2. The six kinds

| Kind | What it is |
| --- | --- |
| `correction` | the owner corrected a behaviour of yours |
| `friction` | something took more exchanges than it should have |
| `worked` | something went unusually well — the kind most often lost |
| `repeat` | the same thing got explained or worked out twice |
| `gap` | a task arrived that no available method covered |
| `caught` | you asserted something and it turned out to be wrong |

`worked` deserves attention because nobody thinks to write it down. Frustration
announces itself; a thing that went smoothly just goes smoothly. But the library
needs to know what to keep as much as what to change, and a method nobody recorded
as working is a method that gets quietly dropped in the next revision.

## 3. The record

Append to `SIGNALS.md` — in the project's agent-facing folder if it has one,
otherwise at the root.

```markdown
## <date> · <kind> · <target, or "none">
What happened: one or two sentences.
Verbatim: "<the owner's own words, quoted exactly>"
Candidate: the rule this might become.
Confidence: how strongly this is evidenced.
```

**Quote exactly, never paraphrase.** A month later your paraphrase will have
drifted toward what you think he meant; the quote will still be what he said. This
is the single most important line in the record, and it is the one most tempting
to smooth over.

Where the signal came from you rather than him — friction you noticed, a gap you
hit — say so in place of the quote.

Keep it to five lines and under a minute. A heavier format does not get used, and
a signal that goes unwritten is worth nothing however well it would have been
formatted.

## 4. When to write

**In the moment, not in a batch at the end.** Detail decays fast, and the exact
wording is most of the value. Writing the file is a side action — mention it in
one clause and carry on; it is not worth interrupting the work to announce.

Do not record every exchange. The test is whether it says something about **how to
work**, not about the task. "The API returned 403" is a fact about the task.
"Three attempts went by before I said the check was blocked rather than negative"
is a signal.

## 5. Offering a review

At the close of a phase, when a project ends, or when signals have piled up, offer
one — briefly, and take no for an answer:

> There are N signals recorded since <date>: mostly about <theme>. Worth a review
> pass, or keep going?

If yes, the review happens in the skill library, not here. Nothing in this file
decides what changes.

**Do not run a survey unprompted, and do not ask after every task.** The value of
these questions collapses if they arrive often enough to become furniture. A
phase boundary is a natural moment; the end of a small task is not.

## 6. After a review

Signals that have been processed can be cleared from `SIGNALS.md` — their
permanent record lives in the library, in the changelog of whatever they changed.
Leave anything not yet processed exactly as it is.

---

## Owner preferences

- **He explicitly asked for this mechanism**, and named the two functions he wants
  from it: periodic extraction of what is worth keeping from ordinary work, and
  being asked review questions *with options offered* rather than open-ended ones.
  A survey that asks "what should I improve?" gets a worse answer than one that
  proposes three candidates and asks which is right.
- **He also wants proposals for entirely new skills and agents**, with the
  reasoning: why it should exist, and what functions it should own. Record those
  as `gap` signals rather than acting on them.
- **His own observations outrank yours.** When he says something landed badly or
  well, that is the highest-quality signal available — record it verbatim and
  immediately.
- **Do not attach the file to the conversation.** He reads it where it lives.

---

## Provenance

Maturity: **L0 draft** · Since: 2026-07-28 · Sources: designed with the owner
while building the skill library; the six kinds and the record format come from
`FACTORY_PHILOSOPHY.md` §6, which this skill implements in the field.

This is the companion half of `SKILL_CREATOR`. This skill is the ears and travels
into every project; the agent is the judgement and stays in the library. They were
split because an agent cannot observe a conversation it is not part of — a
subagent is invoked, does its work in its own context, and returns. There is no
mechanism by which one watches you work, and a design that assumed otherwise would
have failed on contact.

### Changelog

- **2026-07-28 — created.** Written alongside `SKILL_CREATOR`, from the owner's
  requirement that the library improve from ordinary work rather than from
  dedicated sessions.

### Considered and turned down

- **2026-07-28 — a `Stop` hook prompting for a signal after every turn.**
  Maximum capture, and rejected: it would fire after "fix that typo" as readily as
  after a real correction, and a prompt that cries wolf gets ignored within a day.
  A `SessionStart` hook that counts unprocessed signals is installed instead — see
  `references/INSTALL.md`. Revisit if signals turn out to be getting missed.
