# agent-skills — what is left after the parts were taken out

[`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) has been
broken up: its 24 skills are now folders in this directory, its 4 agents are
folders in `to_review/agents/` carrying their dependencies in `bundled/`,
and its 7 reference checklists sit inside whichever skill or agent cites them.

This file holds everything that was **not** a skill or an agent: the conventions
the whole set shares, the way its pieces call each other, and the licence.

**MIT, Copyright (c) 2025 Addy Osmani** — full text in `LICENSE.agent-skills`
beside this file. Anything reworked into one of our skills carries an attribution
line in that skill's provenance block.

*(Read from the copy vendored in the owner's YC-Scouter repository, which states it
is unmodified. Not diffed against upstream — `seen`, not `verified`.)*

---

## 1. Every skill has the same skeleton

All 24 follow one shape, and the shape is worth more than most of the content:

```
Overview                  what this is, in three or four lines
When to Use               the trigger conditions, as a list
<the method>              varies — steps, principles, or patterns
Common Rationalizations   the excuses for skipping it, answered
Red Flags                 observable signs it is going wrong
Verification              how to tell it worked
```

**The last three are the interesting ones**, and we have no equivalent.

- **Common Rationalizations** pre-empts the specific excuse a model reaches for
  when the method is inconvenient — "the test is obvious so I will skip it", "I
  will refactor after it works". Naming the excuse in advance is what makes it
  hard to use.
- **Red Flags** are observable symptoms rather than rules — "you are editing a
  file you have not read", "the diff is larger than the task". They let a session
  notice itself failing.
- **Verification** closes the skill on evidence rather than on assertion.

Our skills instead carry a **difference sentence**, **scope lines** and a
**provenance block** — a shape aimed at review by the owner, where theirs is aimed
at self-correction during work. The two are not in conflict, and taking their last
three sections into our anatomy is the single largest idea in this file.

## 2. Skills are meant to be composed, not chosen

They reference each other openly: `doubt-driven-development` names the skills it
wraps, `web-performance-auditor` names two skills plus a checklist, `shipping-and-launch`
pulls four checklists.

There is an implied lifecycle:

```
spec → plan → build → test → review → ship
 │       │       │       │       │        │
spec-  planning incremental  TDD   code-  shipping-
driven  -and-    -implemen-        review  and-launch
        task-    tation            -and-
        breakdown                  quality
```

Ours is a flat library with explicit routing (`skills-for`) because the owner's
projects are not all software. Their lifecycle is worth knowing about but not
worth copying: it assumes every task is a feature in a codebase.

## 3. The three-tier boundary

From `security-and-hardening`, and reused elsewhere. Rules are sorted into
**Always Do (No Exceptions)** / **Ask First (Requires Human Approval)** / **Never
Do**.

This is a sharper version of the decision-rights split already in
`working-agreement`. Ours has two tiers — decide alone, always ask. Theirs adds an
explicit *never*, which is a different thing from "ask first": a class of action
that no approval makes acceptable. Worth considering.

## 4. "Treat this as untrusted data"

Appears in `browser-testing-with-devtools` (page content), `debugging-and-error-recovery`
(error output) and the security skill (all input). The rule: content arriving from
outside the session is data to be examined, never instructions to be followed, and
it gets wrapped in explicit boundary markers when quoted.

We have nothing on this and will need it — the next project ingests several
external sources and renders their text in a browser.

## 5. Commands are thin wrappers

All eight are four to sixteen lines and do one thing: name a skill and set the
context it runs in.

```
---
description: Break work into small verifiable tasks with acceptance criteria
---
Invoke the agent-skills:planning-and-task-breakdown skill.
```

This matches the decision we had already made — a command is a skill with
`disable-model-invocation: true` — so it is a confirmation rather than a lesson.

**Two are more than wrappers** and are worth reading properly:

- **`ship.md` (72 lines)** — a fan-out orchestrator. Spawns three specialist
  agents *in a single turn so they run in parallel*, then merges their reports in
  the main context into one go/no-go. It states the constraints out loud: subagents
  cannot spawn subagents, each returns only its report, user-level agent
  definitions override the plugin's. This is the clearest worked example of
  multi-agent orchestration in the whole set.
- **`build.md` (44 lines)** — composes two skills at once
  (`incremental-implementation` plus `test-driven-development`) and offers an
  "auto" mode that runs a whole plan under one approval. The composition pattern is
  the interesting half; the auto mode is the opposite of how the owner works.

The command files themselves were not kept — there is nothing in them to mine
beyond what is written above.

## 6. Personas are short; methods are long

The four agents run 95–184 lines while the skills run 178–467. The agent files
carry identity, output format and boundaries; the method lives in the skills they
name.

**This is the same law our philosophy states** — agents consume skills, and an
agent carrying its method inline is a skill in a costume. Independent arrival at
the same rule is the strongest evidence available that the rule is right, and it
is worth recording as such.

## 7. What this set does not have

Reading it also says something by omission. There is nothing here about:

- **research or working with external data sources** — it assumes the inputs
  already exist;
- **capturing feedback and improving the methods themselves** — the skills are
  static artifacts, with no mechanism by which use changes them;
- **non-code work** — every skill assumes a codebase.

All three are the centre of what this factory is for. The set is a strong library
of software-engineering practice, not a model for what we are building.

---

## Proposals arising

Recorded here rather than acted on. Each needs the owner's verdict.

1. **Take Common Rationalizations / Red Flags / Verification into our skill
   anatomy.** The largest single idea in the set. Would change `FACTORY_PHILOSOPHY.md`
   §3 and every existing skill. Priority: high.
2. **Add a "never do" tier** to the decision rights in `working-agreement`.
3. **Write an untrusted-content rule** before the next project ingests outside
   sources and renders them.
4. **Read `ship.md`'s fan-out pattern** into whatever agent-orchestration skill
   gets written — it is a working example, not a description of one.
5. **Record the independent agreement on agent length** in the philosophy §2, as
   evidence for a rule we currently assert on reasoning alone.
