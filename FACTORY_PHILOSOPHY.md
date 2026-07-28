# FACTORY PHILOSOPHY

**What this file is.** The operating contract for this repository. It is written
for the agent that maintains the factory and for the owner who reviews it — not
for a visitor. Introductions live in `README.md`; this file assumes you already
know what a skill is.

**How to use it.** Read it first, before any skill or agent file, in any session
that touches this repository. It says *how* the factory is run. `INDEX.md` says
*what* is currently in it.

**The reconstruction clause.** This file must be sufficient on its own. Given an
empty repository, a pile of skill folders and this file, an agent has to be able
to rebuild the entire operating logic — structure, mechanisms, review loop,
delivery — without asking. §12 is the checklist that keeps that promise honest.
Any change to how the factory works that is not written here is a change that
will be lost.

---

## 0. If you read nothing else

The factory exists to remove the need to explain the same thing twice. Anything
explained twice belongs in a skill. Skills are the default; an agent is only
justified when isolation, parallelism, independence, a different permission
profile, or a separate trigger is the actual point. Every artifact folder must
work alone when sent to another chat. Nothing enters this repository without a
statement of what changes in behaviour because of it. Observations are captured
raw and become changes only at review, where the owner rules. Rejected proposals
are kept with their reason. A rule that never fires gets deleted.

---

## 1. What this repository is

A working library of methods, owned by one person, that grows from real use.

Three properties define it, and every decision below follows from them:

**It is never finished.** There is no release, no "done" state, no final version.
The measure of health is not how many skills exist but whether the last month
produced changes traceable to real work.

**It is the only place to look.** The long-term goal is that nothing needed has
to be fetched from another repository or a third-party author. External material
is starting material, never canon — see §10.

**The owner reviews it by hand.** This is a hard constraint on form, not a
preference. It means: short files, stable section order, readable diffs, no
generated walls of text in files meant for human reading, and every change
explainable in one line.

---

## 2. Skill or agent — the decision

### Definitions

A **skill** is a method. It is read by whoever is already working, enters their
context, and changes how they work. It has no context, tools or model of its own.
Anyone can use it: the main thread, an agent, another chat, a person.

An **agent** is a worker. It runs in its own context window with its own tool
allowlist and possibly its own model. It is not read — it is delegated to, and it
returns a report. The caller never sees its intermediate work.

> A skill changes **how** the work is done. An agent changes **who** does it.

### The five tests

Write a skill by default. Promote to an agent only if at least one is true:

1. **Context isolation is the point.** The work generates far more noise than
   conclusion — reading forty files to answer one question. The agent absorbs the
   noise elsewhere.
2. **Parallelism is needed.** Several instances at once, on independent pieces.
3. **Adversarial independence is needed.** The checker must not have seen how the
   thing was built. A reviewer who read the reasoning is already contaminated by
   it; this is the only way to buy a genuinely fresh look.
4. **A different permission or model profile.** Read-only, cheaper model, a
   narrower tool set.
5. **A separate trigger.** It fires on an event or a boundary, not on the current
   task.

None of them true means it is a skill. There is no sixth reason.

### The law

> **Agents consume skills. Skills never consume agents.**

An agent whose file carries three hundred lines of method is a skill wearing a
costume. A good agent file is short: who it is, when it activates, which skills it
reads, what its output must contain, what it must not touch. The method stays in
the skills, where everything else can reach it.

### Commands are a third form, not a third thing

A command is a skill with `disable-model-invocation: true` — invocable by the
owner, never by the model on its own. Use it for anything with side effects or
where timing is the owner's call. `COMMANDS.md` is the human-facing register of
what exists; the skill files are the implementation.

---

## 3. Anatomy

### Skill folder

```
<skill-name>/
├── SKILL.md          required — frontmatter + method + provenance
├── references/       loaded on demand, not upfront
├── scripts/          executable, for anything deterministic and repeated
├── assets/           templates, files used in output
└── evals/
    └── triggers.md   phrases that must fire it, near-misses that must not
```

### Agent folder

```
<AGENT-NAME>/
├── AGENT.md          a valid agent file: copy it and it works
├── README.md         how to install it into a project or another chat
├── bundled/          stamped copies of the skills it needs
└── <its own state>   e.g. taste.md — knowledge the agent accumulates
```

`bundled/` exists because §3's self-containment rule outranks avoiding
duplication. Every copy carries a stamp naming its source and the date it was
taken. The canonical file lives in `CUSTOM_SKILLS/`; the copy is derived and is
never edited in place. If a copy needs a change, change the canon and re-stamp.

### Frontmatter

Keep it to what is used. `name` and `description` always; the rest only when it
does something.

`description` is the trigger, not a label. The model sees only name and
description before deciding whether to open the skill — the body is invisible
until then. Write it as *what it does plus when to reach for it*, key case first.

| Field | Use |
| --- | --- |
| `name` | defaults to the folder name |
| `description` | what it does **and when to use it** |
| `when_to_use` | extra trigger phrases |
| `disable-model-invocation: true` | makes it a command |
| `user-invocable: false` | background knowledge, not an action |
| `allowed-tools` | pre-approved tools for the invoking turn |

Status, version and origin do **not** go in frontmatter. They go in the
provenance block at the end of `SKILL.md`, where the owner reads them in the same
pass as the method, and where no environment can reject them for being unknown
keys.

### Hard constraints that shape how skills are written

These are properties of the runtime, verified against the Claude Code
documentation on 2026-07-28. They are the difference between a skill that works
in a long session and one that quietly stops working.

- **A skill is read once and stays in context; it is not re-read on later turns.**
  So write standing rules that hold for the rest of the session, not a one-time
  procedure. "From here on, mark every fact" survives; "step 1, step 2, step 3"
  decays.
- **After compaction only the first ~5,000 tokens of each skill are carried
  forward, with ~25,000 tokens shared across all of them.** So keep bodies well
  under that, and push depth into `references/`. A long skill loses its tail
  silently in exactly the long sessions where it matters most.
- **The listing of all skill descriptions has a budget of roughly 1% of the
  context window, and `description` + `when_to_use` is capped at 1,536
  characters.** When the library grows, descriptions get truncated and the
  keywords that would have triggered the skill are what gets cut. Front-load the
  key case. This is also why routing (§8) matters more as the library grows.
- **`.claude/skills/<name>` may be a symlink** to a folder elsewhere on disk, and
  Claude Code follows it. That is how the factory gets auto-discovery without
  duplicating files.
- **`--add-dir` loads `.claude/skills/` from the added directory**, unlike other
  configuration.
- **Cloud and web sessions read `.claude/skills/` from the cloned repository** and
  do not see a personal skills directory on any machine.
- **`context: fork` runs a skill in a subagent**, with the skill body as the
  prompt. It is the bridge between the two forms, useful when a method needs
  isolation but does not deserve an identity.

### The two layers

Every skill separates the general method from this owner's preferences. The
method is written so anyone could use it; the preferences sit in their own clearly
marked section. This costs a little in the writing and buys two things: the skill
can be handed to someone else without a rewrite, and the owner can see exactly
which rules are his taste rather than engineering fact — which is what makes them
reviewable.

### Self-containment

A skill or agent folder must work when sent alone into a chat that has nothing
else. No references to sibling folders, no assumed repository, no "see the other
skill" without saying what that skill contains. Cross-references are allowed as
*recommendations* ("if the task also involves X, `<skill>` covers it"), never as
dependencies.

---

## 4. The maturity ladder

Stated in the provenance block of every skill and agent. Its purpose is that a
glance separates what is battle-tested from what is an experiment.

| Level | Name | What proves it |
| --- | --- | --- |
| L0 | `draft` | written, never used in real work |
| L1 | `used` | applied in real work at least once, the owner confirmed it helped |
| L2 | `tested` | has `evals/triggers.md`: 3–5 phrases that must fire it, 2–3 near-misses that must not, and both verified |
| L3 | `measured` | one real task run with and without it, the difference described |
| L4 | `proven` | used across two or more projects and survived at least one revision driven by real feedback |

Nothing is born above L0. Nothing claims a level it cannot evidence. A skill that
sits at L0 for a long time is a candidate for deletion, not for promotion.

---

## 5. When a skill is allowed to exist

Four gates. A candidate that fails any of them is not written.

**The difference test.** State in one sentence what changes in behaviour with the
skill and without it. If that sentence cannot be written, the skill is decoration.
This sentence is mandatory in every `SKILL.md` and is the first thing to re-check
when revising one.

**One skill, one job.** If the description needs "and" to cover two unrelated
jobs, it is two skills. Overlap between neighbours is normal; a skill that is a
union of two methods is not.

**It must be reachable.** A skill nobody and nothing will ever route to is dead on
arrival. Either the description carries the words the owner would naturally use,
or `INDEX.md` and routing put it in front of the right task.

**It must be able to die.** Every skill is written knowing it can be deleted.
A rule that has not fired in a long stretch of real work, or that the owner has
overridden repeatedly, is removed — not softened, not qualified. Removal is
recorded with the reason, so nobody re-adds it blind. A library nothing is ever
removed from stops being read.

---

## 6. Signals

A **signal** is a raw observation about how the work went, recorded when it
happened. It is not a decision and not a fix.

The rawness is the point. If every remark became a rule immediately, the skills
would fill with noise and contradict each other within a month. A signal is
material; it becomes a change only at review, where the owner rules.

### The six types

| Type | What it is |
| --- | --- |
| `correction` | the owner corrected a behaviour |
| `friction` | something took more exchanges than it should have |
| `worked` | something went unusually well — the type most often lost |
| `repeat` | the same thing was explained or figured out twice |
| `gap` | a task arrived with no skill covering it |
| `caught` | a claim was asserted and turned out to be wrong |

### The record

```markdown
## <date> · <type> · <target skill or "none">
What happened: one or two sentences.
Verbatim: "<the owner's own words, quoted exactly>"
Candidate: the rule this might become.
Confidence: how strongly this is evidenced.
```

Five lines, written in under a minute — anything heavier does not get written at
all. The verbatim quote is not optional: a month later a paraphrase will have
drifted and the quote will not.

### Where they live and how they travel

Signals are generated in the working project, so `SIGNALS.md` lives there, next to
the work. They reach the factory two ways: the owner brings the file into a
factory session, or — when a session holds both repositories — the signal is
committed straight to `.claude/SIGNALS/`. The second is only enabled after the
first has been in use long enough to show what a good signal looks like;
automating the capture of noise just produces more noise.

### What triggers a review

Two triggers, split along the same line as everything else in this file:

- **Count** — a hook counts unprocessed signals at session start and says so once
  the threshold is crossed. Counting is a machine's job and machines do it
  reliably.
- **Meaning** — the close of a phase or a project. That is a semantic moment; the
  `phase-discipline` skill declares it because no event can.

---

## 7. Review — turning signals into changes

Five steps. This is the loop the whole repository exists to run.

1. **Read** every unprocessed signal.
2. **Group.** The same observation arriving from three places is one candidate
   with strong evidence, not three weak ones.
3. **Propose.** For each candidate state: which skill, what changes, which signals
   it came from, and how confident the evidence makes you. A proposal without a
   signal behind it is an opinion — say so explicitly rather than dressing it up.
4. **Ask.** Put the proposals to the owner as options with a recommendation, not
   as a fait accompli. This is the survey; it is the point of the review, not a
   formality around it.
5. **Apply.** Accepted changes go into the skills with a changelog line. Rejected
   ones are recorded in `.claude/DECISIONS/` **with the owner's reason**, so the
   same proposal is never made blind twice. A well-argued rejection often says
   more about what the skill should be than the acceptance would have.

### Judging a proposed change

Prefer the change that generalises. The signals are a handful of examples; the
skill will run hundreds of times. A rule that fixes exactly the observed case and
nothing adjacent is overfitting, and it makes the file longer without making it
better.

Prefer removal to qualification. When a rule misfires, the reflex is to add an
exception. Two exceptions on one rule means the rule was wrong; rewrite it or
delete it.

Explain why, not just what. A rule whose reasoning is written is a rule that can
be applied to a situation nobody anticipated. A bare imperative can only be obeyed
or ignored.

Length is a cost. Every line added to a skill dilutes the rest of it and eats the
compaction budget from §3. Adding a rule means being able to say what it is worth.

---

## 8. Delivery

How a skill gets from the factory into work. Ranked by what the owner actually
uses.

| Path | How | When |
| --- | --- | --- |
| **Repository access** | the factory is available to the session; the model reads `INDEX.md` and loads what it needs | the default, works everywhere including web sessions |
| **Folder into a chat** | the folder is pasted or uploaded alone | environments with no repository access |
| **Copy into a project** | the folder is committed to the project's `.claude/skills/` | when a skill is needed permanently; required for cloud sessions |
| **`--add-dir`** | the factory's `.claude/skills/` loads automatically | local Claude Code |

The first two are the ones in use, and both have the same consequence: **nothing
is auto-discovered**. The model learns the factory exists only because it was
pointed at it. Two things carry that weight:

**`INDEX.md` is the entry point.** Generated from the artifact files, never
written by hand — a hand-maintained index goes stale and then lies, which is worse
than not having one. It lists every skill and agent with its one-line description
and maturity level, and it stays short enough to read in one pass.

**The bootstrap prompt** is kept ready to paste, in `README.md`. It tells a fresh
session where the factory is, to read `INDEX.md` first, and to load only what the
task needs.

### Routing

Routing is what keeps the library usable as it grows past the point where
descriptions fit in context (§3). The output of routing is a prescription, not a
list:

```
Required:    <skills, in reading order>
Optional:    <skills, with the condition that would make them worth loading>
Do not load: <skills, with the reason>
```

The last line does the most work. It saves context and prevents two skills from
imposing conflicting rules on the same task.

---

## 9. Repository standards

**A minimal root.** Folders, plus only the files that must be there. A new file
goes into a folder.

**Names.** Folders a human opens are CAPS (`CUSTOM_SKILLS/`, `CUSTOM_AGENTS/`).
Service folders are lowercase or dot-prefixed. Skills are lowercase-hyphenated and
named for the job (`repo-finished-look`), not for a category. Agents are
CAPS_UNDERSCORED and named for a role (`SKILL_CREATOR`, `UX_DESIGNER`).

**Language.** Everything in the repository is English. Conversation with the owner
is in the language he is using.

**Generated versus written.** `INDEX.md` is generated. Everything else is written
and reviewed by hand. A generated file says so in its first line and is never
edited directly.

**Commit subjects are part of the repository's face.** The file listing prints the
last subject that touched each file, so those lines are read far more often than
the diffs beneath them. One short sentence, plain words, capitalised, no trailing
period, no prefixes or ticket codes, ideally under fifty characters. Detail goes in
the body.

**One document per job.** Two documents answering the same question get merged.

**Every change is reviewable.** No commit mixes a mechanical reformat with a
change of meaning — the owner cannot review the second when it is buried in the
first.

---

## 10. Working with the owner inside this repository

The owner's own working contract governs the conversation. This section covers
only what is specific to the factory.

**Decide alone:** wording of a method already agreed in substance, file and
section ordering, splitting an over-long skill into a skill plus references,
generating the index, fixing an outright error in a skill.

**Always ask:** creating a new skill or agent, deleting one, changing what a skill
is *for*, promoting a maturity level, anything that changes this file.

**External material is starting material, never canon.** Skills written by others
are read as drafts of an idea — worth studying for what they got right and wrong,
never adopted because they are established. Where an external skill and the
owner's stated preference disagree, the owner wins without discussion. The
long-term direction is that everything borrowed is replaced by something written
here.

**Never invent a specific.** A path, a field name, a limit or a behaviour of the
platform recalled from memory and stated as fact is worse than an admitted gap,
because it fails silently and late. Check it, or mark it unchecked. The technical
constraints in §3 carry the date they were verified for exactly this reason.

**The owner's boredom is a signal.** A direction that is correct but tedious will
not survive contact with real use. Say it is tedious and offer the version that
is not.

---

## 11. Anti-patterns

- An agent that carries its method inline instead of reading a skill.
- A skill that cannot state what changes in behaviour because of it.
- A rule added because it sounded right, with no signal behind it.
- Fixing the exact observed case instead of the class it belongs to.
- Softening a misfiring rule with a second exception instead of rewriting it.
- A skill so long that compaction eats its tail in the sessions that need it most.
- A hand-maintained index.
- A library nothing is ever deleted from.
- Treating a borrowed skill as a standard.
- Recording a rejected proposal without its reason — it will be proposed again.
- Turning every remark into a rule the moment it is made.
- Two documents that answer the same question.

---

## 12. Reconstruction

If this file arrives in an empty repository together with a set of skills, rebuild
in this order. Everything needed is above; this is the assembly sequence.

1. **Create the shape.** `CUSTOM_SKILLS/`, `CUSTOM_AGENTS/`, `.claude/` with
   `SIGNALS/`, `DECISIONS/` and `STATE.md`. Root files: `README.md`,
   `FACTORY_PHILOSOPHY.md`, `COMMANDS.md`, `INDEX.md`.
2. **Normalise the skills** into the anatomy of §3: frontmatter, the difference
   sentence, the two layers, a provenance block with a maturity level from §4.
   Anything that cannot pass the gates in §5 is quarantined, not silently kept.
3. **Wire the index.** A script that reads every artifact and writes `INDEX.md`,
   plus a `PostToolUse` hook on writes under the artifact folders so it stays
   current without anyone remembering.
4. **Wire the signals.** The companion skill that records them, the record format
   from §6, and a `SessionStart` hook that counts unprocessed signals and says so
   past the threshold.
5. **Restore the commands** listed in `COMMANDS.md` as skills with
   `disable-model-invocation: true`.
6. **Write the bootstrap prompt** into `README.md` per §8.
7. **Ask the owner what is missing.** Reconstruction from a file is reconstruction
   of the mechanism, not of the judgement that shaped it. State plainly what was
   rebuilt and what was inferred.

---

## 13. Changelog

- **2026-07-28 — created.** Written with the owner from two sources: his portable
  `AI_INSTRUCTIONS` and his `living-project` skill, both kept in the repository as
  material still being mined. Decisions made in the founding conversation and
  encoded here: skills are the default and agents need one of five tests (§2);
  agent folders carry stamped copies rather than pointers, because
  self-containment outranks avoiding duplication (§3); skills are written in two
  layers so they can be handed on (§3); maturity is stated, not assumed (§4);
  signals are captured raw and only become changes at review (§6–7); rejections
  are recorded with reasons (§7); external skills are drafts, never standards
  (§10). The runtime constraints in §3 were read from the Claude Code
  documentation on this date rather than recalled — the same session had already
  produced one wrong architectural claim made from memory, which is the signal
  that rule came from.
