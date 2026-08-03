# skill-creator

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
cp AGENT.md .claude/agents/skill-creator.md
```

The agent expects `bundled/` beside it, so copy that too and keep the relative
path intact — or point it at the library's own copy if the session can reach the
repository.

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
5. The agent applies what you accepted. What you rejected is closed with the
   pull request — the files keep no record, and if the same idea ever returns
   you simply say no again.

---

## What it will not do

It will never delete anything. Retiring an artifact needs you to say so outright —
the agent reports and recommends, and merging two weak skills into one strong one
is what it will suggest first.

It will not invent a signal to justify a proposal, or touch anything outside
the library.

If a review finds that nothing should change, it says so. That is a real result,
and it is the outcome the agent is most likely to be tempted away from.

---

## Its companion

`skills/signal-capture/` is the other half. It travels into every project
and records the observations this agent later reads.

They are separate because an agent cannot watch a conversation it is not part of.
A subagent is invoked, works in its own context, and returns; nothing about it
observes you working. The skill is the ears and goes where the work happens, the
agent is the judgement and stays with the library.
