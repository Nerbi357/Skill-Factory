# Skill Factory

**A working library of methods for AI agents, built from real use and never
finished.**

Every skill here started as something that had to be explained twice. Rather than
explain it a third time, it was written down, given a boundary, and put where any
session can read it. The library grows from actual work: observations are captured
while a project runs, and turned into changes to these files at review — every one
of them through a pull request the owner rules on.

Nothing in here is borrowed as a standard. Where an outside method and the owner's
own preference disagree, the preference wins — that is what makes these files
useful rather than generic.

---

## What is in here

```
README.md               you are here — what this is, how to use it, the catalogue
COMMANDS.md             the manual entry points, designed but not built
FACTORY_PHILOSOPHY.md   the rules the library obeys, for maintaining it
PROJECT_MEMORY.md       where the work stands — the plan, decisions, technical notes
IDEAS.md                ideas for future skills and agents
SIGNALS.md              observations about the work here, waiting to be processed
skills/                 the methods, in force
agents/                 the workers, in force
to_review/              raw material — not in force, never loaded into work
archive/                spent material — reference only, never loaded into work
```

Those carry everything. `.claude/` holds settings, hooks and scripts that make
maintenance faster — delete it and you lose automation, never meaning.

**Skills** are methods. A session reads one and works differently because of it.
**Agents** are workers with their own context, delegated to and reporting back.
The dividing line, and why it matters, is in `FACTORY_PHILOSOPHY.md` §2.

Every folder is self-contained. Send one into a chat that has nothing else and it
works.

---

## Using it in a project

Paste this at the start of a session, with the library available to it:

> My skill library is at `Nerbi357/Skill-Factory`. Read its `README.md` first —
> the catalogue lists every skill and agent with a one-line description. Load
> only what this task actually needs, and tell me what you loaded. If you are
> unsure which apply, describe the task back to me and ask.
>
> Skills are in `skills/`, agents in `agents/`. Each folder is self-contained —
> read the whole folder, not just `SKILL.md`, before using it. **Ignore anything
> under `to_review/`** unless I point you at it: that is raw material, not
> approved for use.
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

| | What it does |
| --- | --- |
| [`confidence-check`](skills/confidence-check/) | Marks every fact with how well it is actually known — verified, seen, recalled, or inferred — and forbids inventing a specific. |
| [`git-repo-structure`](skills/git-repo-structure/) | Keeps a repository structured and named so it reads as a finished product rather than someone's working desk. |
| [`signal-capture`](skills/signal-capture/) | Records observations about how the work is going into a SIGNALS.md file, so they can later improve the skill library instead of being forgotten. |


### Agents

| | What it does |
| --- | --- |
| [`skill-creator`](agents/skill-creator/) | Maintains the skill library — turns accumulated signals into proposed changes, drafts new skills and agents to the library's standard, mines borrowed work for usable parts, audits what exists for overlap and drift, and says which skills a given task should load. |

<!-- CATALOGUE:END -->

---

## For whoever maintains this

Read `FACTORY_PHILOSOPHY.md` before touching anything — it is the operating
contract, and it assumes you already know what a skill is. `PROJECT_MEMORY.md`
says where the work currently stands and what has been decided; this README does
not.
