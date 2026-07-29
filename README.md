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
README.md                   you are here — what this is, how to use it, what it holds
COMMANDS.md                 every command you can run by hand
FACTORY_PHILOSOPHY.md       the rules the library obeys, for maintaining it
CUSTOM_SKILLS/              the methods, in force
CUSTOM_AGENTS/              the workers, in force
CUSTOM_SKILLS_TO_REVIEW/    raw material — not in force
CUSTOM_AGENTS_TO_REVIEW/    raw material — not in force
```

Those carry everything. `.claude/` holds settings, hooks and scripts that make
maintenance faster — delete it and you lose automation, never meaning.

**The two zones matter.** What sits in `CUSTOM_SKILLS/` and `CUSTOM_AGENTS/` has
been approved and is used; it is what gets improved. The `_TO_REVIEW` folders hold
drafts, work borrowed from elsewhere, and rules evicted from a skill they did not
belong in — that is what we improve *with*. **Nothing in a review folder is ever
loaded into real work.** Borrowed material is never promoted whole: it is taken
apart into its smallest usable ideas, and those ideas extend, merge into, or seed
what is in force.

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
> **Ignore anything under `CUSTOM_SKILLS_TO_REVIEW/` or `CUSTOM_AGENTS_TO_REVIEW/`**
> unless I point you at it: that is raw material, not approved for use.
>
> While we work, keep a `SIGNALS.md` at the root of this project. Record anything
> worth remembering about *how* we worked: a correction I made, friction that cost
> extra exchanges or a rediscovery, something that went unusually well, a task no
> skill covered, or a claim of yours that turned out wrong. Quote me exactly rather
> than paraphrasing. I process those later, in the library.

If the session cannot reach the repository, send the skill folder itself — it
carries everything it needs.

---

## The catalogue

<!-- CATALOGUE:START — generated from the artifact files; edit the artifacts, not this block -->
### Skills

| | What it does | Maturity |
| --- | --- | --- |
| [`CONFIDENCE_CHECK`](CUSTOM_SKILLS/CONFIDENCE_CHECK/) | Marks every fact with how well it is actually known — verified, seen, recalled, or inferred — and forbids inventing a specific. | L3 measured |
| [`GIT_REPO_STRUCTURE`](CUSTOM_SKILLS/GIT_REPO_STRUCTURE/) | Keeps a repository structured and named so it reads as a finished product rather than someone's working desk. | L0 draft |
| [`SIGNAL_CAPTURE`](CUSTOM_SKILLS/SIGNAL_CAPTURE/) | Records observations about how the work is going into a SIGNALS.md file, so they can later improve the skill library instead of being forgotten. | L0 draft |


### Agents

| | What it does | Maturity |
| --- | --- | --- |
| [`SKILL_CREATOR`](CUSTOM_AGENTS/SKILL_CREATOR/) | Maintains the skill library — turns accumulated signals into proposed changes, drafts new skills and agents to the library's standard, mines borrowed work for usable parts, audits what exists for overlap and drift, and says which skills a given task should load. | L0 draft |


### In the review zone — raw material, not in force

Drafts, borrowed work, and rules evicted from a skill they did not belong in. Nothing here is loaded during real work.


**Skills:** [`EVICTED_PRINCIPLES.md`](CUSTOM_SKILLS_TO_REVIEW/EVICTED_PRINCIPLES.md), [`GRILLING`](CUSTOM_SKILLS_TO_REVIEW/GRILLING), [`LIVING_PROJECT`](CUSTOM_SKILLS_TO_REVIEW/LIVING_PROJECT), [`RESEARCH_CONDUCT`](CUSTOM_SKILLS_TO_REVIEW/RESEARCH_CONDUCT), [`SOURCE_EVALUATION`](CUSTOM_SKILLS_TO_REVIEW/SOURCE_EVALUATION), [`VERIFY_BEFORE_DONE`](CUSTOM_SKILLS_TO_REVIEW/VERIFY_BEFORE_DONE), [`WORKING_AGREEMENT`](CUSTOM_SKILLS_TO_REVIEW/WORKING_AGREEMENT)


**Agents:** [`SOURCE_SCOUT`](CUSTOM_AGENTS_TO_REVIEW/SOURCE_SCOUT)

<!-- CATALOGUE:END -->

---

## What is next

The visible roadmap. Entries leave this list only by being built or by being
turned down with a reason.

**Phase 1 — the constitution.** Done. `FACTORY_PHILOSOPHY.md` states how the
library is run: the skill-or-agent test, the shape every artifact takes, the
maturity ladder, and the loop that turns observations into changes.

**Phase 2 — the first skills.** Done. Extracted from two large instruction files
the owner had already written. Three were approved into force; `WORKING_AGREEMENT`
and `LIVING_PROJECT` went to the review zone pending his decision on them.
`CONFIDENCE_CHECK` reached `L3 measured` after a paired cold-read test and was
then narrowed to a single job.

**Phase 3 — `SKILL_CREATOR`.** Done. The agent that turns accumulated signals into
proposed changes, drafts new artifacts, audits the library, and routes skills to a
task. It drafts the review survey but does not conduct it — a subagent returns a
result rather than holding a conversation. Its companion `SIGNAL_CAPTURE` travels
into every project and records the observations it later reads.

Neither has been run in anger yet. The first real review is what will show whether
the signal format survives contact with a working session.

**Phase 4 — more skills, then more agents.** In progress. Three drafts are in the
review zone awaiting the owner's verdict: `SOURCE_EVALUATION`, `RESEARCH_CONDUCT`
and `VERIFY_BEFORE_DONE`. Alongside them, a borrowed library of 24 skills, 4 agents
and 7 checklists has been brought in for mining — triaged, not yet read. The next
project is YC-Scouter v2: several accelerators instead of one, official data, and
an interactive site.

**Phase 5 — `UX_DESIGNER`.** Checks what a person meets first — the repository
page, the README, a site, an error message, an empty state — against the skills
that define what finished looks like. Accumulates the owner's taste rather than
guessing at it.

**After that.** Revisions driven by real use. There is no final state; the measure
of health is whether the last month produced changes traceable to real work.

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
