---
name: LIVING_PROJECT
description: Shapes a project as a strong trunk with many well-finished branches, built wide before deep, so new methods, sources and formats attach later without rewriting what exists. Use from the first message of any project that will run for weeks or months and keep growing, that must serve several audiences at once, or whose final shape the owner does not yet know. Use when an existing project has stalled, sprawled, or stopped generating new options. Triggers on "build this wide", "leave room for more branches", "make it a living project", "I want to be proud of this".
---

# Living project

**What changes because of this skill:** without it, a project goes deep on its
first idea and then has to be rewritten to admit the second — the eleventh method
needs a schema change, the fortieth question needs new code. With it, the trunk is
built so that a new branch is an insert rather than a migration, and the project
keeps producing options instead of running out of them.

**Covers:** the shape of a long-lived project — its architecture, how work is
sequenced, where ideas are kept, and what makes it reproducible and presentable.
**Leaves out:** how facts are checked and stated, which is its own skill; the
appearance of the repository itself, which is another; and the moment-to-moment
division of decisions between owner and agent.

Use it from the first message. Retrofitting this shape is expensive — that is the
whole point of it.

---

## 1. The prime rule

> **Build wide before you build deep. Every step must make the next step cheaper.**

Before building anything, ask what it will be reused for. A step that has to be
undone or rewritten to add the next branch was the wrong step. The test of the
architecture is not elegance — it is whether a new method, source, audience or
output can be added later while touching almost nothing that already exists.

Corollary: **do not go deep on the first idea.** The first idea is rarely the best
one, and depth taken early forecloses branches that were still cheap.

## 2. The eight principles

1. **A strong trunk with many well-finished branches.** Not one deep result.
2. **New branches attach without surgery.** Design for that before it is needed.
3. **A branch that fails is still a branch.** If ten approaches do not combine into
   one, that is ten small studies, each written up honestly. A cleanly measured
   negative result is part of the deliverable, not an embarrassment.
4. **Write down what you are not doing.** Everything considered and deferred goes
   into an ideas file with the reason. The point is not tidiness — the project
   should always have a **visible menu of what could come next**.
5. **Judged by several audiences at once.** A finished project should work
   simultaneously as material for a write-up, a portfolio piece, something a
   non-specialist can play with, something worth arguing about with a colleague,
   and something the owner understands end to end. When a choice serves one and
   costs another, say so and let the owner choose.
6. **Established methods are the floor, not the goal.** They belong in the project
   as baselines, so anything new has something to beat. But a project whose
   contribution is "I ran the standard method" is not the goal — push every phase
   for at least one thing genuinely new or under-explored.
7. **Keep proposing.** At the end of every phase, bring new branches. A project
   that stops generating options is finished whether or not it is done.
8. **The owner's interest is a success criterion**, ranked alongside the technical
   ones. If a direction is correct but boring, say it is boring and offer the
   version of it that is not.

## 3. The architecture that makes branching cheap

Adapt the layer names; keep the property.

**Layers with stable interfaces.** Break the work into a few layers where each one
only knows the layer below it. A new idea then attaches at exactly one layer and
touches nothing else:

```
sources      →  what came in, exactly as it came in, plus provenance
normalised   →  cleaned and given a common shape
derived      →  everything computed from the normalised layer
joined       →  the derived layer aligned with whatever it is related to
questions    →  one declarative record per question asked
presentation →  reads the questions layer, never the layer below it
```

**Two properties do almost all the work:**

- **The derived layer is long, not wide.** Key it by *what produced the value*:
  `(item_id, method_id, dimension, value)`. Then **adding the eleventh method is an
  insert, not a code change** — no new column, no migration, no downstream edits. A
  wide table with one column per method forces a schema change for every new idea,
  and that friction is exactly what stops projects from going wide.
- **A question is a config, not code.** Represent each question or experiment as a
  declarative record — which inputs, which target, which subset, which validation —
  that a single runner executes into a standardised result. Then **the fortieth
  question is a config file**, and results are comparable by construction because
  they all came out of the same runner.

**Presentation reads results, never internals.** Charts, reports and interfaces
consume the questions layer. Rebuilding a method then never breaks a figure, and a
figure never quietly depends on a model's internal state.

**Refresh is incremental and idempotent.** Re-running months later must extend the
work, not rebuild it, and must not corrupt it if interrupted. Record provenance
with everything: where it came from, when it was fetched, and a content hash.

## 4. How the work is sequenced

**Plan epochs, not tasks.** An epoch is a coherent stage producing something
demonstrable. Tasks appear only when their epoch opens — a detailed task list
written months early is a work of fiction.

For each epoch state three things: **what must be agreed before it starts** (these
are the real decision points), **what it produces**, and **what it deliberately
leaves out**.

```
E0  Foundation ....... architecture, layout, the reproducibility contract
E1  The trunk ........ the whole pipeline end to end, at deliberately naive settings
E2  Do it properly ... the corrections that make the naive version defensible
E3+ Branches ......... deliberately unordered
En  Finish ........... write-up, release, polish
```

**Epochs after the trunk are deliberately unordered.** Once E0–E2 stand, branches
attach independently and get built in whatever order is most interesting at the
time. **Choose the next branch; do not work through a queue.**

**Build the deliberately naive version first, and report its failure.** The
simplest end-to-end version usually does not work. Run it anyway, publish that it
did not, and use the failure to motivate everything after it. It is the honest
opening of any write-up, it proves the pipeline works before the modelling starts,
and it stops the project from mistaking complexity for progress.

**Order decisions by how much depends on the answer**, and say which are blocking.
Ask the blocking ones early and plainly; decide the rest yourself and say so.

**Identify what cannot be done retroactively, and start it immediately.** Every
project has a few — recording something that only exists going forward,
snapshotting a source that will change, capturing a baseline before an
intervention. They are usually cheap and always impossible to recover later. Find
them in the first hour.

## 5. Two tiers of idea, delivered at different moments

Separate them explicitly and never mix them into one list.

| Tier | What it is | When to raise it |
| --- | --- | --- |
| **Actionable now** | doable within the next three to five steps; makes current work better or cheaper | **inline**, in the message it occurred to you |
| **Idea-level branch** | a new method, angle, audience or format | **at the close of a phase or branch**, when there is room to choose |

Raising branch-level ideas mid-work is noise. Raising them at a boundary is often
the most valuable thing produced in a whole session. Both tiers live in the ideas
file with a status: open, proposed, decided, or set aside with the reason.

**The ideas file keeps its rejections, with the owner's reasoning.** A well-argued
rejection records where a boundary was drawn deliberately, and stops the same
proposal being made blind by the next session.

## 6. The reproducibility contract

**Treat the repository as a chain of checkpoints.** After every meaningful step,
phase or decision, the owner must be able to reproduce the result **from the
repository alone**, on their own machine, without the agent's working environment.

Concretely: the executable path is **visible and runnable**, not hidden in a
shell history; every artefact lands in a **declared folder**, decided in advance;
the environment is **pinned**; anything needing a key or costing money is
**isolated and labelled**; a step that genuinely cannot be re-run is **said to be
so, out loud, with the reason**.

**Where the logic lives — the rule that settles the "notebooks versus library"
argument.** Put **infrastructure** in the importable, tested library: fetching,
parsing, storage, plumbing. Nobody wants to read it, everybody wants it to behave
identically everywhere. Put **everything contestable** in the visible, executable
narrative: how a thing is defined, how a sample is chosen, what is assumed, how a
result is validated.

> **The test: if a decision can be argued with on the merits, it is visible. If it
> is merely "this must be done correctly", it is in the library.**

**Commit the fragile inputs, rebuild the stable ones.** Anything a source might
change or remove gets committed. Anything reliably re-fetchable is re-fetched.
Never delete produced output — dated outputs are an archive.

## 7. The product layer is first-class

If the project has any audience beyond the owner, the visible layer is not a
garnish added at the end. Design it early even if it is built late.

**The bar: it must read as a finished product, not as the output of a working
file.** Someone arriving with no context should understand within twenty seconds
what it shows and want to touch something. If it looks like a dashboard someone
built for themselves, it has failed.

**Interesting, not merely informative.** The test: does a person *do* something,
get a result they did not expect, and want another go? Output that is merely
correct fails this test. Interaction that changes what someone believes passes it.

**Honesty is a constraint, not a disclaimer.** If the work produces estimates,
anything returning a number to a user must make unmistakable what that number is
and is not. Uncertainty belongs in the design, not hidden behind it. A demo that
quietly overclaims is worse than no demo.

**Sequencing that works:** find the piece that needs only the earliest artefacts
and build it first — it gives the project something visible and satisfying long
before the substance is finished. Prefer **static-first**: precompute and serve
plain data, so there is no server to attack and no bill to pay. Add anything live
only when it earns its place, and only after a hostile-input pass.

## 8. Parallel work, at the two moments it pays

**Two moments justify a large parallel run:** discovery — mapping the option space
at the start — and adversarial audit — attacking a finished piece. Everything else
is usually faster as one focused pass.

**Never delegate:** conceptual decisions, the project's narrative, or anything
where the owner's judgement is the input.

**Read reports as evidence, not truth.** Agents are confidently wrong in the same
ways you are, and parallel agents share the session's budgets, network policy and
rate limits — a wide fan-out can leave later agents unable to verify anything.

*(The full catalogue of roles and orchestration shapes becomes its own skill once
there is real experience to write it from. What is here is only what a long-lived
project specifically needs.)*

## 9. Versions, and the closing of a phase

**Ship versions like successive revisions of a paper**, each extending the previous
baseline rather than replacing it. Tag them. Keep a changelog a stranger can read.

**A branch is done when** it has a stated goal, a demonstrable result, tests or
checks covering what it introduced, an honest account of what went in and what was
deliberately postponed, and the owner's approval.

**At every phase boundary:** run the full technical pass; attack the work
deliberately before calling it finished; report what needs attention; and bring the
next set of branches.

**The ideas file stays even in the finished state.** It is the visible roadmap of
what could come next, and it is part of what makes a project look alive rather
than abandoned.

## 10. Anti-patterns

- Going deep on the first idea before the project has gone wide.
- Building a step that must be rewritten to add the next branch.
- A wide table with one column per method — the schema change that quietly stops
  the project from growing.
- Many started branches and none finished. Breadth is the goal; **unfinished**
  breadth is the failure mode. Every branch gets a definition of done before it
  starts.
- Losing an idea because there was no place to put it.
- Hiding a negative result instead of publishing it.
- Calling something reproducible without reproducing it from a clean state.
- Adding a ninth idea when the useful move is to attack the eight that exist.
- Treating the visible layer as decoration to be added at the end.

---

## Owner preferences

- **He works as an inverted pyramid**: widest set of possibilities first, narrowing
  as understanding sharpens, never rebuilding a step from scratch. This skill is
  that habit applied to a whole project rather than to a single decision.
- **A project that stops generating options is over.** He ranks "what could come
  next" as part of the deliverable, which is why the ideas file survives into the
  finished state rather than being cleaned away.
- **He would rather hear that a direction is boring than build it.** Interest is a
  real success criterion for him, not a soft one.
- **Default assumption about purpose**, until told otherwise: an
  educational-professional project that could be attached to a CV or become
  material for an article. Ask at the start anyway — why this project, who besides
  him will see it, what "this went well" would look like.

---

## Provenance

Maturity: **L1 used** · Since: 2026-07-28 · Sources: the owner's own
`living-project` skill, written during his YC-Scouter project and used there.

Maturity is L1 rather than L0 because the method predates this library and shaped
a real project; it has not yet passed a cold read in this form.

### Changelog

- **2026-07-28 — adopted into the library.** Content is the owner's, restructured
  to the factory's anatomy: difference sentence, scope lines, owner preferences
  separated from the general method, provenance block.
- **2026-07-28 — deduplicated.** The original §8 (research and verification
  discipline) was removed entirely; it is now `RESEARCH_WITH_CONFIDENCE`, which
  says the same things at more length. The original §9 (using agents) was cut from
  a full catalogue of roles and orchestration shapes down to the two points a
  long-lived project specifically needs, because the catalogue duplicated
  `AI_INSTRUCTIONS` §8 almost line for line and deserves to be its own skill.

### Considered and turned down

- **2026-07-28 — splitting this into four skills** (architecture, sequencing,
  reproducibility, product layer). Each section is substantial enough to stand
  alone. Kept as one because the sections only make sense together: the
  architecture exists to serve the sequencing, and both exist to make the product
  layer cheap. Split it if the file becomes hard to load, not because it is long.
