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
declared by the owner with no method behind it; two drafts already point rules
at this skill.
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
