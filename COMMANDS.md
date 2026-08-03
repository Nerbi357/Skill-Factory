# COMMANDS

Everything you can run by hand, what it does, and when it is worth reaching for.

A command here is an ordinary skill carrying `disable-model-invocation: true` —
you can invoke it, the model cannot invoke it on its own. That restriction is the
point: regenerating a catalogue, rewriting a skill or opening a review are all
things whose timing should be yours, not a model's guess that the moment looks
right.

Three of these live in the factory. Two travel with the skills into whatever
project you are working in, which is why they are listed here rather than only in
that project's own documentation.

**Status** says whether the command exists yet. Nothing below is implemented; the
design is written first so you can argue with it before it is built.

| Command | Where it runs | Status |
| --- | --- | --- |
| `/factory-new` | the factory | planned |
| `/factory-review` | the factory | planned |
| `/factory-mine` | the factory | planned |
| `/signal` | any project | planned |
| `/skills-for` | any project | planned |

---

## `/factory-new`

**Creates a new skill or agent.**

Runs the interview first — what the thing is for, what changes in behaviour
because of it, where its boundary sits against its neighbours — and only then
writes a file. The interview is not ceremony: most bad skills are bad because they
were written before anyone could say what they would change.

Before writing anything it checks whether an existing skill is the same job seen
from a different angle, and says so if it is. One strong skill beats two that each
half-cover the ground.

It also applies the skill-or-agent test rather than taking your word for which one
you asked for. If you ask for an agent and the work needs none of context
isolation, parallelism, adversarial independence, a different permission profile
or its own trigger, it will say so and propose a skill instead — with the
reasoning, so you can overrule it.

Ends by regenerating the catalogue in `README.md`.

**Reach for it when:** you have explained the same approach twice, a task arrived
that nothing covers, or you want a rough placeholder now that will be reshaped
later.

---

## `/factory-review`

**Turns accumulated observations into changes to the skills.**

This is the loop the whole repository exists to run. Five steps:

1. Reads the signals — from the `SIGNALS.md` of whatever project produced them.
2. Groups them. The same observation arriving from three places is one strong
   candidate, not three weak ones.
3. Proposes: which skill, what changes, which signals it came from, how confident
   the evidence makes it. A proposal with no signal behind it is labelled as an
   opinion rather than dressed up as evidence.
4. **Asks you.** Each proposal comes as options with a recommendation. This is the
   survey — the point of the review, not a formality wrapped around it.
5. Applies what you accepted. What you turned down is simply not applied — the
   closed pull request keeps the discussion, and if the same idea ever returns
   you say no again.

**Reach for it when:** a phase or a project closes, or when the signal count has
been climbing and you want the pile turned into something.

---

## `/factory-mine`

**Gets the value out of borrowed work and into what is actually in force.**

Point it at something in `to_review/skills/` or
`to_review/agents/` — a skill written by someone else, a draft, a rule
evicted from a file it did not belong in.

It never promotes a file whole. Adopting someone else's artifact entire imports
their assumptions along with their good ideas, and the assumptions are invisible
precisely because they arrived bundled with something that works. Instead it takes
the thing apart into its smallest usable pieces, checks each against what is
already in force, and proposes only what survives — extending a named skill,
merging two, or seeding a new one where nothing fits.

It also reports what it left behind and why. A piece nobody ever claims is itself
a result: the idea was weaker than it looked.

**Reach for it when:** you have dropped something into a review folder and want to
know what in it is worth having.

---

## `/signal`

**Records an observation of yours, in your words, right now.**

The companion skill records what the model notices. This command records what
**you** notice — and those are the higher-quality signals, because the model
cannot see its own blind spots. "That was worse than usual", "you started coding
before asking again", "that table was exactly right" are all things only you can
report.

```
/signal you started implementing before asking what it was for
```

Writes a dated entry into `SIGNALS.md` at the project root, with your words quoted
exactly, plus the surrounding context. The verbatim quote is not decoration: a
month later a paraphrase will have drifted and the quote will not.

**Reach for it when:** something lands well or badly and you do not want to stop
and discuss it. One line, then carry on.

---

## `/skills-for`

**Says which skills to load for the task in front of you.**

```
/skills-for building a scraper for a source that keeps changing shape
```

Returns a prescription, not a list:

```
Required:    <skills, in the order to read them>
Optional:    <skills, with the condition that would make them worth loading>
Do not load: <skills, with the reason>
```

The last line does the most work. It keeps context free and stops two skills from
imposing conflicting rules on the same task.

**Reach for it when:** you start work in a project and want the right subset
loaded, rather than everything or whatever the model happens to notice. It matters
more the larger the library gets — descriptions compete for a shared budget, so
past a certain size the model stops reliably seeing what is available and explicit
routing takes over.

---

## Naming

Commands are lowercase-with-hyphens, like every artifact: a command is a skill,
and a skill's folder, frontmatter `name` and invocation are the same string, so
the register and the invocations match by construction.
