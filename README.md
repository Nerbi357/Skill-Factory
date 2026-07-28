# Skill Factory

**A working library of methods for AI agents, built from real use and never
finished.**

Every skill here started as something that had to be explained twice. Rather than
explain it a third time, it was written down, given a boundary, and put where any
session can read it. The library grows from actual work: observations are captured
while a project runs, and turned into changes to these files at review.

Nothing in here is borrowed as a standard. Where an outside method and the owner's
own preference disagree, the preference wins — that is what makes these files
useful rather than generic.

---

## What is in here

```
README.md               you are here — what this is, how to use it, what it holds
COMMANDS.md             every command you can run by hand
FACTORY_PHILOSOPHY.md   the rules the library obeys, for maintaining it
CUSTOM_SKILLS/          the methods
CUSTOM_AGENTS/          the workers
```

Those five carry everything. `.claude/` holds settings, hooks and scripts that
make maintenance faster — delete it and you lose automation, never meaning.

**Skills** are methods. A session reads one and works differently because of it.
**Agents** are workers with their own context, delegated to and reporting back.
The dividing line, and why it matters, is in `FACTORY_PHILOSOPHY.md` §2.

Every folder is self-contained. Send one into a chat that has nothing else and it
works.

---

## Using it in a project

Paste this at the start of a session, with the library available to it:

> My skill library is at `Nerbi357/Skill-Factory`. Read its `README.md` first —
> the catalogue lists every skill and agent with a one-line description and how
> well tested each one is. Load only what this task actually needs, and tell me
> what you loaded. If you are unsure which apply, describe the task back to me and
> ask.
>
> Skills are in `CUSTOM_SKILLS/`, agents in `CUSTOM_AGENTS/`. Each folder is
> self-contained — read the whole folder, not just `SKILL.md`, before using it.
>
> While we work, keep a `SIGNALS.md` in this project. Record anything worth
> remembering about *how* we worked: a correction I made, friction that cost extra
> exchanges, something that went unusually well, a task no skill covered, or a
> claim of yours that turned out wrong. Quote me exactly rather than paraphrasing.
> I process those later, in the library.

If the session cannot reach the repository, send the skill folder itself — it
carries everything it needs.

---

## The catalogue

<!-- CATALOGUE:START — generated from the artifact files; edit the artifacts, not this block -->

*Nothing here yet.* The library is being built; the first skills land in the next
phase. See **What is next** below.

<!-- CATALOGUE:END -->

---

## What is next

The visible roadmap. Entries leave this list only by being built or by being
turned down with a reason.

**Phase 1 — the constitution.** Done. `FACTORY_PHILOSOPHY.md` states how the
library is run: the skill-or-agent test, the shape every artifact takes, the
maturity ladder, and the loop that turns observations into changes.

**Phase 2 — the first skills.** Four, extracted from two large instruction files
the owner had already written:

- `WORKING_AGREEMENT` — the order work goes in, who decides what, how risk and
  disagreement are raised.
- `RESEARCH_WITH_CONFIDENCE` — every fact carries how well it is known; never
  invent a specific; a blocked check is not a negative result.
- `REPO_FINISHED_LOOK` — what makes a repository read as a product rather than a
  workbench. Grows a web half later.
- `LIVING_PROJECT` — build wide before deep, so a new branch attaches without
  rewriting what exists.

**Phase 3 — `SKILL_CREATOR`.** The agent that reads accumulated signals, judges
what should change, runs the review survey, and routes the right skills to a task.
Ships with the companion skill that records signals while other work is happening.

**Phase 4 — `UX_DESIGNER`.** Checks what a person meets first — the repository
page, the README, a site, an error message, an empty state — against the skills
that define what finished looks like. Accumulates the owner's taste rather than
guessing at it.

**Phase 5 and after.** More skills, and revisions of these driven by real use.
There is no final state; the measure of health is whether the last month produced
changes traceable to real work.

---

## Still being mined

`AI_INSTRUCTIONS (1).md` and `SKILL (1).md` are the owner's originals, kept
deliberately. They are the source material the first skills are extracted from and
are consulted while that work continues. They leave when the owner says they are
redundant, not before.

---

## For whoever maintains this

Read `FACTORY_PHILOSOPHY.md` before touching anything. It is written for that job
and assumes you already know what a skill is; this README does not.
