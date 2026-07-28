# SKILL_CREATOR

The agent that maintains the skill library: it turns accumulated observations into
proposed changes, drafts new skills and agents to the library's standard, audits
what is already there, and says which skills a given task should load.

It reads, judges and writes. It does not talk to you — the session that calls it
does that. The division is deliberate and explained in `AGENT.md`.

---

## What it is for

| Job | You ask for | You get back |
| --- | --- | --- |
| **Review** | signals turned into changes | proposals with their evidence, plus a survey drafted for you to answer |
| **Route** | which skills fit this task | required, optional, and explicitly *do not load* |
| **Create** | a new skill or agent from a settled brief | the artifact, after checking it does not already exist |
| **Audit** | the state of the library | overlaps, drift, and a recommended move for anything that looks dead |

---

## Installing it

### Into a Claude Code project

```bash
mkdir -p .claude/agents
cp AGENT.md .claude/agents/SKILL_CREATOR.md
```

The agent expects `bundled/` beside it, so copy that too and keep the relative
path intact — or point it at the library's own copy if the session can reach the
repository.

*(Unverified: whether Claude Code accepts an agent whose `name` is uppercase. The
documentation states no constraint either way and this has not been run yet. If it
fails to load, rename the `name` field to `skill-creator` and keep the folder name
as it is — the folder is for you to read, the field is for the loader.)*

### Into any other chat

Send this whole folder. It carries everything it needs: the agent definition and
stamped copies of the library rules it works from. Then say:

> Act as the agent defined in `AGENT.md`. Read `bundled/FACTORY_PHILOSOPHY.md`
> first. I want a <review / route / create / audit> pass; here is the material.

---

## Running a review

The loop this exists for. Five steps, and you are in the middle of three of them:

1. Bring the `SIGNALS.md` from whatever project produced it.
2. The agent groups the signals and drafts proposals with their evidence.
3. **It hands you a survey.** Each proposal comes as options with a
   recommendation, phrased to answer in a line.
4. You rule.
5. The agent applies what you accepted and writes what you rejected into the
   artifact's provenance block, with your reason in your words.

Step five matters as much as the others. A rejection recorded without its reason
gets proposed again by the next session that has the same idea; recorded with it,
it becomes a marker showing where a boundary was drawn on purpose.

---

## What it will not do

It will never delete anything. Retiring an artifact needs you to say so outright —
the agent reports and recommends, and merging two weak skills into one strong one
is what it will suggest first.

It will not promote a maturity level on its own, invent a signal to justify a
proposal, or touch anything outside the library.

If a review finds that nothing should change, it says so. That is a real result,
and it is the outcome the agent is most likely to be tempted away from.

---

## Its companion

`CUSTOM_SKILLS/SIGNAL_CAPTURE/` is the other half. It travels into every project
and records the observations this agent later reads.

They are separate because an agent cannot watch a conversation it is not part of.
A subagent is invoked, works in its own context, and returns; nothing about it
observes you working. The skill is the ears and goes where the work happens, the
agent is the judgement and stays with the library.

---

## Provenance

Maturity: **L0 draft** · Since: 2026-07-28

Built third, after the first four skills, so that its review job had real material
to be designed against. Two of the signals it was designed to handle came from an
actual cold-read test rather than from invented examples.

### Changelog

- **2026-07-28 — created.** Scoped to four jobs, with the survey deliberately left
  to the calling session.

### Considered and turned down

- **2026-07-28 — having the agent conduct the survey itself.** It is what the
  owner originally described. Dropped once the mechanics were clear: a subagent
  returns a result rather than holding a conversation, and a background one asking
  questions is worse than useless. The agent drafts the survey and the calling
  session delivers it, which keeps the intent and drops the impossible part.
- **2026-07-28 — preloading the library's skills via the `skills:` frontmatter
  field.** It works when the skills are discoverable, and this library is
  deliberately not on a discovery path. A missing skill is skipped with only a
  debug-log warning, so the failure would be silent. Reading the stamped copies in
  `bundled/` is explicit and works in every delivery path.
