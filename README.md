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
COMMANDS.md             every command you can run by hand
FACTORY_PHILOSOPHY.md   the rules the library obeys, for maintaining it
PROJECT_MEMORY.md       where the work stands — the plan, decisions, technical notes
IDEAS.md                ideas for future skills and agents
skills/                 the methods, in force
agents/                 the workers, in force
to_review/              raw material — not in force
```

Those carry everything. `.claude/` holds settings, hooks and scripts that make
maintenance faster — delete it and you lose automation, never meaning.

**The two zones matter.** What sits in `skills/` and `agents/` has been approved
and is used; it is what gets improved. `to_review/` holds drafts, work borrowed
from elsewhere, and rules evicted from a skill they did not belong in — that is
what we improve *with*. **Nothing in `to_review/` is ever loaded into real
work.** Borrowed material is never promoted whole: it is taken apart into its
smallest usable ideas, and those ideas extend, merge into, or seed what is in
force.

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


### In the review zone — raw material, not in force

Drafts, borrowed work, and rules evicted from a skill they did not belong in. Nothing here is loaded during real work.


**Methods:** [`0-code-simplification`](to_review/skills/0-code-simplification), [`0-deprecation-and-migration`](to_review/skills/0-deprecation-and-migration), [`1-algorithmic-art`](to_review/skills/1-algorithmic-art), [`1-api-and-interface-design`](to_review/skills/1-api-and-interface-design), [`1-browser-testing-with-devtools`](to_review/skills/1-browser-testing-with-devtools), [`1-canvas-design`](to_review/skills/1-canvas-design), [`1-ci-cd-and-automation`](to_review/skills/1-ci-cd-and-automation), [`1-documentation-and-adrs`](to_review/skills/1-documentation-and-adrs), [`1-observability-and-instrumentation`](to_review/skills/1-observability-and-instrumentation), [`1-performance-optimization`](to_review/skills/1-performance-optimization), [`1-shipping-and-launch`](to_review/skills/1-shipping-and-launch), [`2-code-review-and-quality`](to_review/skills/2-code-review-and-quality), [`2-context-engineering`](to_review/skills/2-context-engineering), [`2-git-workflow-and-versioning`](to_review/skills/2-git-workflow-and-versioning), [`2-grilling`](to_review/skills/2-grilling), [`2-idea-refine`](to_review/skills/2-idea-refine), [`2-incremental-implementation`](to_review/skills/2-incremental-implementation), [`2-research-conduct`](to_review/skills/2-research-conduct), [`2-security-and-hardening`](to_review/skills/2-security-and-hardening), [`2-spec-driven-development`](to_review/skills/2-spec-driven-development), [`2-web-artifacts-builder`](to_review/skills/2-web-artifacts-builder), [`3-debugging-and-error-recovery`](to_review/skills/3-debugging-and-error-recovery), [`3-frontend-ui-engineering`](to_review/skills/3-frontend-ui-engineering), [`3-impeccable`](to_review/skills/3-impeccable), [`3-interview-me`](to_review/skills/3-interview-me), [`3-karpathy-guidelines`](to_review/skills/3-karpathy-guidelines), [`3-living-project`](to_review/skills/3-living-project), [`3-planning-and-task-breakdown`](to_review/skills/3-planning-and-task-breakdown), [`3-source-driven-development`](to_review/skills/3-source-driven-development), [`3-source-evaluation`](to_review/skills/3-source-evaluation), [`3-theme-factory`](to_review/skills/3-theme-factory), [`3-using-agent-skills`](to_review/skills/3-using-agent-skills), [`4-doubt-driven-development`](to_review/skills/4-doubt-driven-development), [`4-frontend-design`](to_review/skills/4-frontend-design), [`4-sp-dispatching-parallel-agents`](to_review/skills/4-sp-dispatching-parallel-agents), [`4-sp-subagent-driven-development`](to_review/skills/4-sp-subagent-driven-development), [`4-sp-writing-skills`](to_review/skills/4-sp-writing-skills), [`4-test-driven-development`](to_review/skills/4-test-driven-development), [`4-verify-before-done`](to_review/skills/4-verify-before-done), [`4-working-agreement`](to_review/skills/4-working-agreement), [`agent-skills-general.md`](to_review/skills/agent-skills-general.md), [`candidates-external.md`](to_review/skills/candidates-external.md), [`evicted-principles.md`](to_review/skills/evicted-principles.md)


**Workers:** [`1-security-auditor`](to_review/agents/1-security-auditor), [`2-code-reviewer`](to_review/agents/2-code-reviewer), [`2-test-engineer`](to_review/agents/2-test-engineer), [`3-source-scout`](to_review/agents/3-source-scout), [`3-understand-anything`](to_review/agents/3-understand-anything), [`3-web-performance-auditor`](to_review/agents/3-web-performance-auditor)

<!-- CATALOGUE:END -->

---

## For whoever maintains this

Read `FACTORY_PHILOSOPHY.md` before touching anything — it is the operating
contract, and it assumes you already know what a skill is. `PROJECT_MEMORY.md`
says where the work currently stands and what has been decided; this README does
not.
