# IDEAS

Ideas for future skills, agents, and the connections between them. This is the
menu of what the library could grow next — not a roadmap (`PROJECT_MEMORY.md`
holds the plan) and not raw material (`to_review/` holds that). An entry leaves
this file by becoming a draft the owner rules on, or by being dropped when he
says no.

Five lines each: what it is, why it would earn its place, where it came from,
and what would make it worth picking up.

---

## researcher — a general research agent

What: `source-scout` generalised. Consumes `research-conduct` +
`source-evaluation` + `confidence-check`; modes: evaluate a source, find a
fact, survey the options.
Why: research is noisy (context isolation) and parallelises across sources —
two of the five agent tests.
From: the owner, 2026-08-03 — "variant (a) now, and we will definitely return
to (b) once more relevant skills exist."
Revisit when: `research-conduct` and `source-evaluation` are in force.

## phase-discipline — what a phase is and when it is closed

What: a skill defining a phase, its boundary, and what happens there — the full
technical pass, the review offer, the next branches.
Why: the phase close is the factory's "meaning" trigger for reviews, currently
declared by the owner with no method behind it. The technical pass now lives in
`verify-before-done` §7; what remains unowned is the ceremony around it — the
review offer, and the choice of what comes next.
From: the owner, 2026-08-03 — "we will come back to it when we understand what
else this skill is for."
Revisit when: phase closes have happened a few times and the pattern is visible.

## agent-orchestration — the catalogue of multi-agent shapes

What: fan-out, adversarial panel, judge panel, loop-until-dry, completeness
critic, clean-room replication — when each pays and when it wastes money.
Why: the strongest unmined material in the repository; `living-project` cut its
agent catalogue down and promised it a skill of its own.
From: `SKILL (1).md` §9, flagged during the Phase 0 survey.
Revisit when: the sources are mined (Phase 3).

## idea-funnel — how a proposal is shaped before it is decided

What: the funnel from raw idea to decidable options — what to expand, what to
kill, how to present the choice.
Why: `working-agreement` explicitly leaves this to a named skill that does not
exist yet.
From: `AI_INSTRUCTIONS (1).md`, via the `working-agreement` scope line.
Revisit when: the sources are mined (Phase 3).

## ux-designer — the agent that judges what a person meets first

What: checks the repository page, the README, a site, an error message, an
empty state against the skills that define what finished looks like;
accumulates the owner's taste rather than guessing it.
Why: the visible surface is part of every deliverable, and no artifact owns it.
From: the owner's original roadmap.
Revisit when: `git-repo-structure` has survived real use and a web surface
exists to judge.

## critic — the agent that argues against the project

What: called at a phase close or whenever the owner wants it, it reads the
constitution, the plan and what is in force, and reports what is at risk — what
could break, what is quietly rotting, which decision looks worse now than when
it was made. It rules on nothing and changes nothing; it hands back a list.
Why: adversarial independence is the one agent test a working session cannot
pass on its own work (philosophy §2, test 3). That job exists today as a queue
in `PROJECT_MEMORY.md` that the owner carries to a fresh chat by hand.
From: the owner, 2026-08-04 — "an agent called from time to time that
criticises the project: where the risks are, what the problems are, what could
break."
Revisit when: enough is built to criticise. A critic pointed at plans reports on
plans, which is the cheapest criticism there is — so after Phase 2, or the first
time the outside-look queue has more lines than the owner wants to carry.

## idea-generator — the agent that argues for what is missing

What: the critic's mirror. Same material, opposite question — what could be done
differently, where the library could extend, which skills are missing and which
connections between them are unbuilt. Its output lands in this file as
candidates with a revisit condition each, never as drafts.
Why: divergent generation is a different job from building, and a session deep
in a phase generates near the work in front of it. The risk is the reason for
the constraint: an idea generator produces plausible volume, and volume is what
this repository is built to resist — so nothing it emits reaches `skills/`
without going the ordinary way, through a draft and a pull request.
From: the owner, 2026-08-04 — "and another one, the reverse: it advises what
could be done differently, how the project could be extended."
Revisit when: this file stops growing on its own. Every entry here came out of a
real conversation, which is better fuel than generation — the day new entries
stop arriving is the day generation is worth paying for.

## fact-checker — freshness split out of the audit

What: a dedicated skill or command for re-verifying dated facts, if they ever
multiply.
Why: today the in-force zones hold roughly a dozen perishable facts, so
freshness is one audit sub-pass; a data-heavy library would outgrow that.
From: the owner, 2026-08-03, asking where fact upkeep should live.
Revisit when: an audit reports the freshness pass taking longer than the rest
of the audit combined.

## synthetic test rigs — deliberately broken fixtures for factory-test

What: purpose-built traps (a cluttered repository for `git-repo-structure`, a
conversation with planted signals for `signal-capture`) as a third source of
test tasks.
Why: cheap and reproducible where real tasks are expensive — but weaker
evidence, so parked rather than adopted.
From: the owner, 2026-08-03 — "let's leave synthetic runs to think about."
Revisit when: `factory-test` exists and real-task supply becomes the
bottleneck.

## the commands — deterministic handles for what already works

What: the seven designs in `COMMANDS.md` built as skills carrying
`disable-model-invocation: true` — five factory jobs, plus `/signal` and
`/skills-for`, which travel into working projects.
Why: a command buys a trigger nobody can forget and nobody can fire by accident.
`/signal` in particular has to be manual by nature — its whole job is recording
the owner's words at the moment he chooses. What a command does not buy is
capability: every job below is already reachable through `agents/skill-creator`
and a sentence, which is how this repository has actually been run.
From: the owner, 2026-08-04 — "let's not write commands for now; mark it as a
development point and we will come back to it."
Revisit when: the base is built and the library begins maintaining itself — or
earlier, if the same job gets described in words three times and the description
drifts on each telling.

## scheduled loop — automation of the maintenance iteration

What: the loop on a schedule (a cloud routine or cron) instead of by hand, with
push notification of each result.
Why: removes the owner as the bottleneck for upkeep — but only worth it once
the manual loop has proven the iteration shape.
From: the owner, 2026-08-03 — "a good idea, keep it, but for the future; for
now only on my request."
Revisit when: manual `/factory-loop` runs feel routine and the owner tires of
starting them.

## workflow-dispatch entry — starting the loop from the repository page

What: a GitHub Actions button that runs one loop iteration in CI and opens the
pull request.
Why: a manual trigger that needs no session at all; shares infrastructure with
Phase 2's checks.
From: the Phase 0 survey of loop-trigger options.
Revisit when: Phase 2 sets up CI.
