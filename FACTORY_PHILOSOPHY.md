# FACTORY PHILOSOPHY

**What this file is.** The operating contract for this repository. It is written
for the agent that maintains the factory and for the owner who reviews it — not
for a visitor. Introductions live in `README.md`; this file assumes you already
know what a skill is.

**How to use it.** Read it first, before any skill or agent file, in any session
that touches this repository. It says *how* the factory is run. `README.md` says
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
are kept with their reason. Weak skills are merged into strong ones or rewritten,
never quietly deleted. Everything needed to understand, use or edit the factory
lives in `README.md`, `COMMANDS.md` and the two artifact folders — nowhere else.

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

### The four surfaces

Everything the factory is, does and knows must be reachable from four places:

```
README.md          what this is, how to use it, and what is currently in it
COMMANDS.md        every command, what it does, when to reach for it
CUSTOM_SKILLS/     the methods
CUSTOM_AGENTS/     the workers
```

Plus this file, which states the principles those four obey.

No logic, no rule, no computed value and no piece of the mechanism may live
anywhere else. If understanding how something works requires opening a fifth
file, the design is wrong — move it into one of the four or into this file.

`.claude/` is the workshop: hooks, scripts, the signal inbox, working state.
It exists so the maintaining agent works faster, and it holds **nothing the
factory depends on being understood**. The test is blunt and worth applying
literally:

> **Delete `.claude/` entirely. The owner, any other project and any fresh
> session must still be able to read, understand, use and edit every skill and
> agent. Only automation is lost, never meaning.**

That test is also what keeps the factory portable. A skill that needs a script in
`.claude/` to make sense cannot be sent to another chat, which contradicts §3.

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
<SKILL_NAME>/
├── SKILL.md          required — frontmatter + method + provenance
├── references/       loaded on demand, not upfront
├── scripts/          executable, for anything deterministic and repeated
└── assets/           templates, files used in output
```

Every `SKILL.md` states its **scope** in two lines: what it covers, and what it
deliberately leaves to a named neighbour. Boundaries written down are what stop
two skills from imposing conflicting rules on the same task, and they are the
first thing to check when a skill starts feeling like it does too much.

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

### The provenance block

Every skill and agent ends with one, and it carries the whole history of that
artifact — because §6 puts the history in the file that holds the method, not in
a store somewhere else.

```markdown
## Provenance

Maturity: <L0–L4> · Since: <date> · Sources: <where the method came from>

### Changelog
- **<date> — <what changed>.** Why, and the signal it came from.

### Considered and turned down
- **<date> — <the proposal>.** The owner's reason, in his terms.
```

The last section is the one that pays off later. A rejected proposal without its
reason gets proposed again by the next session that has the same good idea; with
the reason, it is a boundary marker showing where the skill's edge was drawn
deliberately.

### Four properties of the runtime, and what they demand

These hold across models and platforms because they follow from how a context
window works, not from any one product's settings. The exact figures behind them
move; the shape does not. Figures live in the box below, dated — never inside the
rules themselves, so a changed limit never invalidates a principle.

**A skill is read once and stays; it is not re-read on later turns.** Write
standing rules that hold for the rest of the session, not a procedure to be
walked through. "From here on, mark every fact with its confidence" survives the
whole session; "step 1, step 2, step 3" is spent the moment it is read.

**Only the front of a skill is guaranteed to survive a long session.** When
context fills up it gets compacted, and what is carried forward is bounded. Put
the rules that must never be lost near the top and push depth into `references/`.
A long skill loses its tail silently, in exactly the long sessions where it
matters most.

**Descriptions compete for a shared budget.** Every skill's description sits in
context so the model knows the skill exists, and that listing is capped. As a
library grows, descriptions get truncated — and what gets cut is the tail, which
is where the triggering keywords usually are. Front-load the key case. This is
also why explicit routing (§8) matters more the larger the library gets.

**Isolation is available without a new identity.** A method that needs its own
context can be run as a forked subagent while remaining a skill. Reach for that
before inventing an agent; §2's five tests are about identity, not just about
isolation.

> **Measured on 2026-07-28, against the Claude Code documentation.** Re-check
> before relying on any figure; correct the box, not the rules above it.
> Compaction carries roughly the first 5,000 tokens of each invoked skill, with
> about 25,000 tokens shared across all of them. The skill listing is budgeted at
> roughly 1% of the context window, and `description` plus `when_to_use` is
> capped at 1,536 characters. `.claude/skills/<name>` may be a symlink and is
> followed. `--add-dir` loads `.claude/skills/` from the added directory. Cloud
> and web sessions read `.claude/skills/` from the cloned repository and see no
> personal skills directory. `context: fork` runs a skill in a subagent with the
> skill body as its prompt.

When a skill exists that governs how skills are written, this box moves into it,
where a stale number is corrected through the ordinary improvement loop instead of
by amending the constitution.

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
| L2 | `tested` | passed a cold read: a session that did not write it was given the folder and a real task, and behaved as intended |
| L3 | `measured` | one real task run with and without it, the difference described |
| L4 | `proven` | used across two or more projects and survived at least one revision driven by real feedback |

Nothing is born above L0. Nothing claims a level it cannot evidence.

L2 is the level that matters most here, because it tests the thing that actually
fails: not whether a skill is well written, but whether a session reading it cold
— with none of the conversation that produced it — does the right thing. That is
the real delivery condition (§8), so it is the real test.

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
or the catalogue and routing put it in front of the right task.

**It must be able to change shape.** A skill that stops earning its place is not
deleted — it is merged, rewritten or, only with the owner's explicit permission,
retired. Writing a skill speculatively is therefore fine: a rough skill that might
become useful is far cheaper to reshape later than to invent from nothing, and a
file that exists is a file the owner can react to.

### When a skill stops earning its place

Three moves, in order of preference. **Deletion is never one of them, and never
happens without the owner saying so.**

1. **Merge.** Two weak skills covering neighbouring ground become one strong one.
   This is the default and usually the right answer — the library gets shorter and
   each remaining file gets better, which is the opposite of what deletion
   achieves.
2. **Rewrite.** The job is real but the file is wrong. Keep the name and the
   place; replace the contents.
3. **Retire.** Only after the owner has been told, in these terms: why it looks
   dead, what already does its job, and which of the three moves is recommended.

The moment to raise this is an audit, never mid-task. Report it as a finding with
the evidence; the decision is the owner's. Silently removing a method he might
still want is worse than carrying a file that is doing nothing.

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

**`SIGNALS.md` lives in the working project, never in the factory.** Signals are
born where the work happens, so that is where they are written — alongside the
project's other agent material, or at its root if it keeps none.

**The factory stores no raw signals.** There is no inbox here, and that is
deliberate: an inbox would be a load-bearing store outside the four surfaces, and
the first thing to fail §1's deletion test. Review reads `SIGNALS.md` where it
lies and writes its outcomes straight into the skills.

**A processed signal leaves its trace in the skill it touched**, in that skill's
own provenance block — what changed, and what was proposed and turned down, each
with its reason. The history of a method belongs in the file that holds the
method; nowhere else does anyone reading that skill have to go looking. Decisions
about how the factory itself works are recorded in this file's changelog for the
same reason.

Once a signal has been processed it can be cleared from the project's
`SIGNALS.md`. Its permanent record already exists in the skill.

### What triggers a review

Two triggers, split along the same line as everything else in this file:

- **Count** — a hook in the working project counts unprocessed signals at session
  start and says so once the threshold is crossed. Counting is a machine's job and
  machines do it reliably. It fires where the signals are, which is also where the
  owner is when he would want to hear it.
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
   ones are written into the same provenance block **with the owner's reason**, so
   the same proposal is never made blind twice and so anyone opening the skill
   sees what was already considered. A well-argued rejection often says more about
   what the skill should be than the acceptance would have.

### Judging a proposed change

Prefer the change that generalises. The signals are a handful of examples; the
skill will run hundreds of times. A rule that fixes exactly the observed case and
nothing adjacent is overfitting, and it makes the file longer without making it
better.

Prefer rewriting a rule to qualifying it. When a rule inside a skill misfires,
the reflex is to add an exception. Two exceptions on one rule means the rule was
wrong: restate it so the exceptions become unnecessary. This is about the lines
inside a file — whole skills are handled by §5, where merging comes first and the
owner decides.

Prefer merging to adding. Before writing a new skill, check whether an existing
one is the same job seen from a different angle. One strong skill beats two that
each half-cover the ground, and the check costs a minute.

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
| **Repository access** | the factory is available to the session; the model reads `README.md` and loads what the task needs | the default, works everywhere including web sessions |
| **Folder into a chat** | the folder is pasted or uploaded alone | environments with no repository access |
| **Copy into a project** | the folder is committed to the project's `.claude/skills/` | when a skill is needed permanently; required for cloud sessions |
| **`--add-dir`** | the factory's `.claude/skills/` loads automatically | local Claude Code |

The first two are the ones in use, and both have the same consequence: **nothing
is auto-discovered**. The model learns the factory exists only because it was
pointed at it. Two things carry that weight:

**`README.md` is the entry point**, and it carries the catalogue. There is no
separate index file: a fifth root file would break §1, and a catalogue is exactly
what a reader arriving at the repository needs anyway. The catalogue lists every
skill and agent with its one-line description and maturity level, and stays short
enough to read in one pass.

It sits in a marked, generated block inside `README.md`, rebuilt from the artifact
files themselves and never edited by hand — a hand-maintained catalogue goes stale
and then lies, which is worse than not having one. The generator touches only what
is between the markers; everything else in the README is written and reviewed like
any other prose.

**The bootstrap prompt** is kept ready to paste, also in `README.md`. It tells a
fresh session where the factory is, to read the README first, and to load only
what the task needs.

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

**Names.** Everything a human opens is `CAPS_WITH_UNDERSCORES`: the two artifact
folders, every skill folder, every agent folder. Service folders stay lowercase or
dot-prefixed. A skill is named for its job (`REPO_FINISHED_LOOK`), an agent for
its role (`SKILL_CREATOR`, `UX_DESIGNER`); which is which is told by the folder it
sits in and by whether it holds `SKILL.md` or `AGENT.md`.

The consequence to know: a skill folder's name is also how it is invoked, so a
skill copied into a project answers to `/REPO_FINISHED_LOOK`. That is the accepted
cost of a listing the owner can read at a glance.

**Language.** Everything in the repository is English. Conversation with the owner
is in the language he is using.

**Generated versus written.** Exactly one thing is generated: the catalogue block
inside `README.md`, between its markers. Everything else in the repository is
written and reviewed by hand. Generated regions say so and are never edited
directly; the fix for a wrong catalogue is a fix to the artifact it was read from.

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
regenerating the catalogue, fixing an outright error in a skill.

**Always ask:** creating a new skill or agent, merging two, changing what a skill
is *for*, promoting a maturity level, anything that changes this file — and
retiring anything, which additionally requires the owner to say so outright (§5).

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
- A hand-maintained catalogue.
- Logic, a rule or a computed value that lives outside the four surfaces.
- A skill that cannot be understood without opening something in `.claude/`.
- Deleting a skill instead of merging or rewriting it, or deleting one at all
  without the owner's word.
- Treating a borrowed skill as a standard.
- Recording a rejected proposal without its reason — it will be proposed again.
- Keeping raw signals, decisions or any other store inside the factory.
- Turning every remark into a rule the moment it is made.
- Two documents that answer the same question.

---

## 12. Reconstruction

If this file arrives in an empty repository together with a set of skills, rebuild
in this order. Everything needed is above; this is the assembly sequence.

1. **Create the shape.** `CUSTOM_SKILLS/`, `CUSTOM_AGENTS/`, and `.claude/` for
   settings, hooks and scripts only. Root files: `README.md`,
   `FACTORY_PHILOSOPHY.md`, `COMMANDS.md`. No fourth root file, and no store of
   any kind under `.claude/` (§1).
2. **Normalise the skills** into the anatomy of §3: frontmatter, the difference
   sentence, the scope lines, the two layers, a provenance block with a maturity
   level from §4. Anything failing the gates in §5 is listed for the owner with a
   recommended move — never dropped.
3. **Wire the catalogue.** A script that reads every artifact and rewrites the
   marked block in `README.md`, plus a `PostToolUse` hook on writes under the
   artifact folders so it stays current without anyone remembering.
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
  (§10). The runtime properties in §3 were read from the Claude Code
  documentation on this date rather than recalled — the same session had already
  produced one wrong architectural claim made from memory, which is the signal
  that rule came from.
- **2026-07-28 — the four surfaces, and skills are reshaped rather than
  deleted.** Both from the owner, reviewing the first draft. He required that
  everything needed to understand, use or edit the factory be reachable from
  `README.md`, `COMMANDS.md` and the two artifact folders, with `.claude/` holding
  nothing load-bearing (§1) — which removed the separate index file in favour of a
  generated block in the README (§8). He also rejected the original "a skill must
  be able to die": nothing is deleted without his word, merging two weak skills
  into one strong one is preferred to removing either, and writing a skill
  speculatively is fine because reshaping a rough file is cheaper than inventing
  one (§5). He was right on both counts, and the second changes the character of
  the library — it accumulates and consolidates rather than pruning.
  Separately, he noticed that §3 stated platform figures inside its rules, where a
  changed limit would invalidate a principle; the figures now sit in a dated box
  and the rules are written without them. Skill folders were renamed to
  `CAPS_WITH_UNDERSCORES` to match agents (§9), and the trigger-test harness was
  dropped in favour of a cold-read test at L2 (§4) — with delivery happening by
  repository access and by folder, what needs proving is that a session reading a
  folder cold does the right thing, not that a description auto-fires.
- **2026-07-28 — the factory stores nothing raw.** The owner asked where the
  signal file would live, which exposed that the draft's `.claude/SIGNALS/` and
  `.claude/DECISIONS/` were stores outside the four surfaces and the first things
  to fail §1's own deletion test. Both are gone. `SIGNALS.md` now lives only in the
  working project where signals are born, and every processed signal leaves its
  trace — accepted or rejected — in the provenance block of the skill it touched
  (§3, §6, §7). `.claude/` is left holding settings, hooks and scripts, which is
  what makes the deletion test pass literally rather than approximately.
