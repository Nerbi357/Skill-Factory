<!-- STAMPED COPY — do not edit.
     Source:      FACTORY_PHILOSOPHY.md
     Taken:       2026-08-04
     Canonical:   edit the source and rerun .claude/scripts/sync_bundles.py
-->

# FACTORY PHILOSOPHY

**What this file is.** The operating contract for this repository. It is written
for the agent that maintains the factory and for the owner who reviews it — not
for a visitor. Introductions live in `README.md`; this file assumes you already
know what a skill is.

**How to use it.** Read it first, before any skill or agent file, in any session
that touches this repository. It says *how* the factory is run. `README.md` says
*what* is currently in it; `PROJECT_MEMORY.md` says where the work stands.

**The reconstruction clause.** This file must be sufficient on its own. Given an
empty repository, a pile of skill folders and this file, an agent has to be able
to rebuild the entire operating logic — structure, mechanisms, review loop,
delivery — without asking. §11 is the checklist that keeps that promise honest.
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
raw and become changes only at review, where the owner rules — in practice, by
merging or closing a pull request. Files carry no history: what a thing *is*
lives in the file, what *happened to it* lives in git and the pull-request
archive. Weak skills are merged into strong ones or rewritten, never quietly
deleted. Everything needed to understand, use or edit the factory lives in the
root files and the artifact folders — nowhere else. Nothing in `to_review/` is
ever loaded into real work.

---

## 1. What this repository is

A working library of methods, owned by one person, that grows from real use.

Three properties define it, and every decision below follows from them:

**It is never finished.** There is no release, no "done" state, no final version.
The measure of health is not how many skills exist but whether the last month
produced changes traceable to real work.

**It is the only place to look.** The long-term goal is that nothing needed has
to be fetched from another repository or a third-party author. External material
is starting material, never canon — see §9.

**The owner reviews it by hand.** This is a hard constraint on form, not a
preference. It means: short files, stable section order, readable diffs, no
generated walls of text in files meant for human reading, and every change
explainable in one line. Nothing reaches the in-force zones except through a
change the owner has seen — which is what pull requests are for.

### The surfaces

Everything the factory is, does and knows must be reachable from these places,
and nowhere else:

```
README.md            the showcase — what this is, how to use it, the catalogue
COMMANDS.md          every command, what it does, when to reach for it
PROJECT_MEMORY.md    the working memory — the plan, standing decisions, technical notes
IDEAS.md             ideas for future skills, agents, and how they would connect
skills/              the methods, in force
agents/              the workers, in force
to_review/           raw material — not in force
```

Plus this file, which states the principles the rest obey. The split among the
root files is deliberate: `README.md` stays a clean showcase with no roadmap and
no technical notes; everything about where the project is going and how it is
run day to day lives in `PROJECT_MEMORY.md`; a thought that might one day become
an artifact lives in `IDEAS.md`, so it is never lost and never mistaken for a
plan.

No logic, no rule, no computed value and no piece of the mechanism may live
anywhere else. If understanding how something works requires opening a file not
listed above, the design is wrong — move it into one of these or into this file.

`.claude/` is the workshop: hooks, scripts, working state. It exists so the
maintaining agent works faster, and it holds **nothing the factory depends on
being understood**. The test is blunt and worth applying literally:

> **Delete `.claude/` entirely. The owner, any other project and any fresh
> session must still be able to read, understand, use and edit every skill and
> agent. Only automation is lost, never meaning.**

That test is also what keeps the factory portable. A skill that needs a script in
`.claude/` to make sense cannot be sent to another chat, which contradicts §3.

### The two zones

What is in force lives in `skills/` and `agents/`. What is not lives in one
place:

```
skills/              in force — approved, in use, audited, improved
agents/              in force
to_review/skills/    raw material — drafts and borrowed methods
to_review/agents/    raw material — drafts and borrowed workers
```

`to_review/` also holds parked files that belong to no single artifact, such as
`evicted-principles.md` — rules removed from a skill they did not belong in,
waiting to be claimed.

**Nothing in `to_review/` is ever loaded into real work.** That is the whole
distinction, and it is absolute. Routing never returns one. A session following
the library does not read one unless it was explicitly asked to.

The two zones are not "good" and "bad" — they play different parts in the same
mechanism:

- **In force is what gets improved.** Signals, the owner's judgement, and material
  mined from the review zone all land here. The audit watches only these.
- **The review zone is what we improve *with*.** Skills written by other people,
  half-formed drafts, principles evicted from a file they did not belong in,
  ideas worth keeping but not yet placed.

The move from one zone to the other is **the owner's, always**, and it is not a
file move. Borrowed work is never promoted wholesale: it is taken apart into its
smallest usable ideas, and those ideas are fitted into what already exists —
extending a skill, merging two, or seeding a new one where nothing fits. What is
left behind stays where it is.

That is deliberate. Adopting someone else's file whole imports their assumptions
along with their good ideas, and the assumptions are invisible precisely because
they came bundled with something that worked.

An entry in the review zone that nothing ever claims is itself a result: the idea
was weaker than it looked, and saying so is worth more than keeping it in view
forever.

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
where timing is the owner's call. `COMMANDS.md` is the human-facing register;
the skill files are the implementation.

A command buys a trigger, never a capability. Anything it would do is reachable
by asking for it, so the form earns its file only where the trigger itself
matters — where the model must not fire it, or where nothing in the session
shares the context needed to ask well. Where that is not true, the command is a
second name for something that already exists.

---

## 3. Anatomy

### Skill folder

```
<skill-name>/
├── SKILL.md          required — frontmatter + method
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
<agent-name>/
├── AGENT.md          a valid agent file: copy it and it works
├── README.md         how to install it into a project or another chat
├── bundled/          stamped copies of the skills it needs
└── <its own state>   e.g. taste.md — knowledge the agent accumulates
```

`bundled/` exists because §3's self-containment rule outranks avoiding
duplication. Every copy carries a stamp naming its source and the date it was
taken. The canonical file lives in `skills/`; the copy is derived and is never
edited in place. If a copy needs a change, change the canon and re-stamp.

### Frontmatter

Keep it to what is used. `name` and `description` always; the rest only when it
does something.

`description` is the trigger, not a label. The model sees only name and
description before deciding whether to open the skill — the body is invisible
until then. Write it as *what it does plus when to reach for it*, key case first.

| Field | Use |
| --- | --- |
| `name` | equals the folder name |
| `description` | what it does **and when to use it** |
| `when_to_use` | extra trigger phrases |
| `disable-model-invocation: true` | makes it a command |
| `user-invocable: false` | background knowledge, not an action |
| `allowed-tools` | pre-approved tools for the invoking turn |

### Files carry no history

A skill or agent file holds the method and nothing else about itself: no
changelog, no status, no version, no record of what was once proposed and turned
down. Changes are applied directly. What a thing *is* lives in the file; what
*happened to it* lives in git and the pull-request archive, which record every
change and every rejection without costing the files a line.

The one exception is a draft in `to_review/`, which may end with an
**`## Open questions for the owner`** section: the unresolved boundary questions
its author had no right to settle. That section is the agenda for the interview
that decides the draft's fate, and it is removed at promotion — by then the
questions have answers.

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
also why explicit routing (§7) matters more the larger the library gets.

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

## 4. When a skill is allowed to exist

Four gates. A candidate that fails any of them is not written.

**The difference test.** State in one sentence what changes in behaviour with the
skill and without it. If that sentence cannot be written, the skill is decoration.
This sentence is mandatory in every `SKILL.md` and is the first thing to re-check
when revising one.

**One skill, one task or one principle** — even when the principle is large and
fundamental. Size is not the test; coherence is. A long skill about one thing is
healthy. A short one carrying two unrelated rules is not, however tidy it looks.

If the description needs "and" to join two jobs that do not depend on each other,
it is two skills. Overlap between neighbours is normal; a union of two methods is
not.

This gate is the one most often failed by accident, because a rule that is *true*
and *useful* and *happened to come up while writing* feels like it belongs. It
does not: skills are loaded selectively, and a rule filed under an unrelated
heading is a rule that will be absent when it is actually needed and present when
it is noise. The library's first eviction was exactly this — advice on checking
whether something already exists, sitting inside a skill about how confidently a
fact is known. Both good; unrelated.

**Evicting is not deleting.** A rule removed for sitting in the wrong file goes to
`to_review/skills/evicted-principles.md` with where it came from, why it was
moved, and where it might belong. It leaves that file by being folded into a
skill that genuinely wants it, or by seeding a new one.

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

## 5. Signals

A **signal** is a raw observation about how the work went, recorded when it
happened. It is not a decision and not a fix.

The rawness is the point. If every remark became a rule immediately, the skills
would fill with noise and contradict each other within a month. A signal is
material; it becomes a change only at review, where the owner rules.

### The five kinds

| Kind | What it is |
| --- | --- |
| `correction` | the owner corrected a behaviour |
| `friction` | something cost more than it should have — extra exchanges, a rediscovery, the same thing explained twice |
| `worked` | something went unusually well — the kind most often lost |
| `gap` | a task arrived with no skill covering it |
| `caught` | a claim was asserted and turned out to be wrong |

### The record

```markdown
## <date> · <kind> · <target skill or "none">
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
deliberate: an inbox would be a load-bearing store outside the surfaces, and the
first thing to fail §1's deletion test. Review reads `SIGNALS.md` where it lies
and writes its outcomes straight into the skills. Which projects to read is
configuration, and it lives in `PROJECT_MEMORY.md`.

Once a signal has been processed it can be cleared from the project's
`SIGNALS.md`. The change it produced is in the skill; the discussion that
produced it is in the pull request.

### What triggers a review

Two triggers, split along the same line as everything else in this file:

- **Count** — a hook in the working project counts unprocessed signals at session
  start and says so once the threshold is crossed. Counting is a machine's job and
  machines do it reliably. It fires where the signals are, which is also where the
  owner is when he would want to hear it.
- **Meaning** — the close of a phase or a project. That is a semantic moment, and
  it is the owner's to declare: he says the phase is over, or agrees it is when
  the session suggests so. No mechanism fires it for him.

---

## 6. Review — turning signals into changes

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
5. **Apply** what he accepted, directly — the diff is the record. What he turned
   down is simply not applied: the closed pull request keeps the discussion, and
   the files keep nothing. If the same idea returns one day, the owner says no
   again; that cost is accepted.

In practice the survey rides in a pull request. The diff is the proposal, the
description carries the options and the recommendation, the merge is the ruling,
and a close without merge is a rejection. Nothing reaches the in-force zones
except through that gate.

### Judging a proposed change

Prefer the change that generalises. The signals are a handful of examples; the
skill will run hundreds of times. A rule that fixes exactly the observed case and
nothing adjacent is overfitting, and it makes the file longer without making it
better.

Prefer rewriting a rule to qualifying it. When a rule inside a skill misfires,
the reflex is to add an exception. Two exceptions on one rule means the rule was
wrong: restate it so the exceptions become unnecessary. This is about the lines
inside a file — whole skills are handled by §4, where merging comes first and the
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

## 7. Delivery

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
separate index file: the catalogue is exactly what a reader arriving at the
repository needs anyway. It lists every skill and agent with its one-line
description, and stays short enough to read in one pass.

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

## 8. Repository standards

**A minimal root.** Folders, plus only the files that must be there: `README.md`,
`COMMANDS.md`, `FACTORY_PHILOSOPHY.md`, `PROJECT_MEMORY.md`, `IDEAS.md`, and
`LICENSE`. A new file goes into a folder. A temporary departure from this is
declared in `PROJECT_MEMORY.md` together with what ends it.

**Names.** One name everywhere: a folder, its frontmatter `name`, and the way it
is invoked are the same lowercase-with-hyphens string — `git-repo-structure` is
the folder, the `name`, and `/git-repo-structure`. This is the ecosystem's own
convention, so an artifact copied into any project's `.claude/skills/` looks
native there. A skill is named for its job (`git-repo-structure`), an agent for
its role (`skill-creator`); which is which is told by the folder it sits in and
by whether it holds `SKILL.md` or `AGENT.md`. Root files and platform-pinned
names (`README.md`, `LICENSE`, `SKILL.md`, `AGENT.md`) keep their conventional
forms.

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

## 9. Working with the owner inside this repository

The owner's own working contract governs the conversation. This section covers
only what is specific to the factory.

**Decide alone:** wording of a method already agreed in substance, file and
section ordering, splitting an over-long skill into a skill plus references,
regenerating the catalogue, fixing an outright error in a skill.

**Always ask:** creating a new skill or agent, merging two, changing what a skill
is *for*, anything that changes this file — and retiring anything, which
additionally requires the owner to say so outright (§4).

**Each phase of work opens with its decisions.** Before a phase starts, every
decision it will implement is put to the owner in one pass — options with a
recommendation — and nothing is built until he has ruled. This is the same shape
as the review survey, applied to the plan.

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

## 10. Anti-patterns

- An agent that carries its method inline instead of reading a skill.
- A skill that cannot state what changes in behaviour because of it.
- A rule added because it sounded right, with no signal behind it.
- Fixing the exact observed case instead of the class it belongs to.
- Softening a misfiring rule with a second exception instead of rewriting it.
- A skill so long that compaction eats its tail in the sessions that need it most.
- A hand-maintained catalogue.
- Logic, a rule or a computed value that lives outside the surfaces.
- A skill that cannot be understood without opening something in `.claude/`.
- Deleting a skill instead of merging or rewriting it, or deleting one at all
  without the owner's word.
- Treating a borrowed skill as a standard.
- Keeping raw signals, or any store the surfaces do not name, inside the factory.
- History creeping back into the files — a changelog line, a status field, a
  version number. Git already holds all of it.
- A change reaching `skills/` or `agents/` without passing through the owner.
- Adopting a borrowed skill whole instead of taking it apart for its usable ideas.
- Loading anything from `to_review/` into real work.
- Leaving a true, useful rule inside a skill it has nothing to do with.
- Turning every remark into a rule the moment it is made.
- Two documents that answer the same question.
- Losing an idea because there was no place to put it — `IDEAS.md` is the place.

---

## 11. Reconstruction

If this file arrives in an empty repository together with a set of skills, rebuild
in this order. Everything needed is above; this is the assembly sequence.

1. **Create the shape.** `skills/` and `agents/` for what is in force,
   `to_review/` with `skills/` and `agents/` inside for raw material, and
   `.claude/` for settings, hooks and scripts only. Root files: `README.md`,
   `COMMANDS.md`, `FACTORY_PHILOSOPHY.md`, `PROJECT_MEMORY.md`, `IDEAS.md`. No
   other root file, and no store of any kind under `.claude/` (§1).
2. **Normalise the skills** into the anatomy of §3: frontmatter, the difference
   sentence, the scope lines, the two layers, no history in the files. Anything
   failing the gates in §4 is listed for the owner with a recommended move —
   never dropped.
3. **Wire the catalogue.** A script that reads every artifact and rewrites the
   marked block in `README.md`, plus a `PostToolUse` hook on writes so it stays
   current without anyone remembering.
4. **Wire the signals.** The companion skill that records them, the record format
   from §5, and a `SessionStart` hook that counts unprocessed signals and says so
   past the threshold.
5. **Restore whatever `COMMANDS.md` marks as built** — as skills with
   `disable-model-invocation: true`. A design in that file that was never built
   is not rebuilt here; it stays a design.
6. **Write the bootstrap prompt** into `README.md` per §7.
7. **Ask the owner what is missing.** Reconstruction from a file is reconstruction
   of the mechanism, not of the judgement that shaped it. State plainly what was
   rebuilt and what was inferred.
