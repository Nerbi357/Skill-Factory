# PROJECT MEMORY

The factory's working memory: where the work stands, what has been decided, and
the technical notes that do not belong on the showcase. `README.md` shows what
this is; this file records where it is going. It is updated as part of ordinary
work, through the same pull requests as everything else — and it is the **only
handshake between sessions**: any session, in any chat, resumes the project by
reading this file.

---

## How the work runs

The owner, one working session, and — for special cases — an outside look:

- **The owner rules.** Every change to what is in force arrives as a pull
  request; his merge is acceptance, his close is rejection. He also declares
  phase closes — nothing else does.
- **The working session does everything else**: it holds the phase gates with
  the owner, builds the phase's work as reviewable pull requests, criticises
  the plan against what actually happened, and keeps this file current. Any
  capable session takes the role by reading this file; the working prompt is
  below. It starts by reading this file and ends by updating "Where things
  stand" in the same pull request as its work.
- **An outside look** is a deliberately fresh session with none of the working
  context, called only for the special cases queued below — a stuck
  disagreement, a constitution change, a plan overturned, a session judging
  its own earlier work, or a periodic independent audit. Its independence is
  the point (philosophy §2, test 3). Its prompt is also below.

**Phase gates.** Each phase opens with every decision it will implement put to
the owner in one pass — options with a recommendation (philosophy §9). Once
ruled, the decisions are recorded under the phase below and are not reopened
mid-task; if reality contradicts a ruling, the working session says so and
re-asks rather than silently deviating.

**Pull requests.** One meaningful change per PR; mechanical churn in separate
commits from meaning; commit subjects per philosophy §8. The open-PR cap is
**2**: at the cap, improve what is open instead of adding to the pile. Nobody
merges their own PR.

**Versions.** A phase closed by the owner gets a git tag (scheme below). Tags
mark states; there is no release ceremony before v1.0.

---

## Where things stand

- **Phase 0 — foundation repairs: in force.** Pull request #1 merged.
- **The review zone is stocked.** Pull request #2 merged: the vendored bundle
  broken into one folder per artifact, thirteen further candidates imported with
  their licences checked individually, and a `REVIEW_NOTE.md` in every folder
  carrying a priority from 0 to 4 that also leads the folder name. Forty methods
  and six workers now wait for a verdict.
- **This plan was written on a branch that forked before #2** and was carried
  across by hand rather than merged — merging it would have deleted the review
  zone. The branch is gone; nothing else on it was worth keeping.
- **Phase 1 — the commands: gate held 2026-08-04**, rulings recorded under the
  phase below. One question from that gate is still open and blocks building:
  whether the five factory commands earn their place at all.
- **Open, not blocking:** how many branches the work uses. The recommendation is
  one short-lived branch per pull request, cut from `main` and deleted on merge —
  `main` is the only branch the owner reads or edits. It becomes a standing
  decision once he rules.

---

## The plan

The idea-line across the phases: **mechanise** the loop (1), **protect** it
with guardrails (2), **absorb** everything already written (3), **connect** it
to real work (4), then **let it grow** on its own fuel (5). Later phases are
direction, not commitment — each gets its gate when its turn comes.

### Phase 1 — the commands (→ v0.2)

**Goal:** the loop stops being prose. All seven commands in `COMMANDS.md`
exist, are invocable in this repository, and have each survived one cold run on
real material.

**Builds:** the seven commands as skills with
`disable-model-invocation: true` — canonical folders in `skills/`, wired into
`.claude/skills/` so slash-invocation works here; `skill-creator` installed
into `.claude/agents/` so the factory can delegate to its own maintainer;
statuses in `COMMANDS.md` flipped to *built* as each lands.

**Decisions at the gate:** confirm the open-PR cap (2 proposed); symlink
versus copy for the `.claude/skills/` wiring — verified against the platform
documentation first, not recalled; the interview scripts of `factory-new` and
`factory-review` (what they ask, in what order); whether `signal` and
`skills-for` ship with install notes for foreign projects.

**Order of work:** `signal` and `skills-for` first (small, travelling), then
`factory-mine`, `factory-new`, `factory-review`, `factory-test`, and
`factory-loop` last — it composes the others.

**Acceptance:** each command cold-run once on real material — `factory-mine`
on `grilling`, `skills-for` on a real task description, `factory-test` on one
in-force skill — and the run's verdict recorded in the PR that flips its
status.

**Risks here:** commands swelling into methods (the law: agents consume
skills — a command file stays about a page, method lives in skills); platform
frontmatter surprises (check the documentation first; update the dated box in
philosophy §3 if figures moved).

**Gate rulings, 2026-08-04.**

- **Where the executable folders live:** in `skills/`, alongside the methods.
  `COMMANDS.md` stays the human-facing register — it describes; it cannot
  execute, since one file cannot be seven skills. The catalogue splits the two
  by the `disable-model-invocation` flag, which is machine-readable.
- **A command names what it drives in one line** — `factory-mine` says
  "delegate to `agents/skill-creator`, job MINE" — rather than nesting inside
  the artifact it drives. Nesting would take it off the discovery path, and
  three of the commands point at the same agent.
- **Wiring:** symlinks from `.claude/skills/<name>` into `skills/<name>`.
  Documented as supported and `core.symlinks` is on; **unverified in the
  owner's cloud environment**, so it is the first thing tested. Copies are the
  fallback.
- **Cold runs:** two clean subagents — a candidate given only the skill folder
  and a task, a judge given the candidate's output and the skill's difference
  sentence. Paired when the difference needs showing rather than asserting, with
  the metric declared before the run. Default agent type `general-purpose`; when
  a target project's `CLAUDE.md` overlaps the skill under test, use `Explore` or
  record in the verdict that the run was not fully cold. Worth it when a skill
  is new, heavily revised, or doubted — not for a wording fix.
- **Open-PR cap: 2**, confirmed.
- **`signal` and `skills-for` ship with install notes**; `signal` travels
  alongside `signal-capture`, since they are the manual and automatic halves of
  one mechanism. `skills-for` reads the catalogue from the factory's `README.md`
  when the repository is reachable, and says so plainly when it is not.

**Open, and blocking the build:** *do the five factory commands earn their
place?* This whole repository has been run for weeks with none of them — every
mine, review and structural decision happened by a session reading
`PROJECT_MEMORY.md` and the owner saying what to do. `signal` and `skills-for`
are different: they run in foreign projects where no shared context exists, and
a short deterministic handle is worth having. The owner rules before anything
is built.

### Phase 2 — the guardrails (→ v0.3)

**Goal:** the invariants hold without anyone remembering them.

**Builds:** CI on every pull request — catalogue check, bundle-stamp check, an
anatomy lint (new script in `.claude/scripts/`: frontmatter name equals
folder, difference sentence present, scope lines present, no history sections,
internal links resolve), all deterministic and offline. Optionally a
`workflow_dispatch` entry so a loop iteration can be started from the
repository page.

**Decisions at the gate:** what the lint enforces on drafts (recommendation:
only the review-zone banner and the open-questions section); whether red CI
blocks merging (recommendation: yes).

**Risks here:** flaky checks teach the owner to ignore red — so no network, no
timing, no model calls in CI; a lint that ossifies prose — lint structure,
never style.

**Acceptance:** a PR with a deliberately broken catalogue fails visibly; a
clean one passes green.

### Phase 3 — the mining (→ v0.4)

**Goal:** nothing valuable is left unmined; the two originals leave the root.

**Steps:** `/factory-mine` over `AI_INSTRUCTIONS (1).md` (expected seeds: the
idea funnel, phase material, the team-of-agents section) and over
`SKILL (1).md` §9 (the agent-orchestration catalogue — the strongest unmined
material in the repository). Then the originals move to `to_review/` or leave,
on the owner's word. Then `to_review/skills/agent-skills-upstream/`, following
its own triage table — one file or small group per iteration, each a PR.

**Decisions at the gate:** attribution wording for mined ideas; the promotion
interviews — whether `working-agreement`, `living-project`, and the three
drafts enter force, using their own open-questions sections as the agenda;
mining order beyond the triage table.

**Risks here:** a flood of mining PRs (the cap holds; one mining PR at a
time); taste dilution — **owner-preference sections are never edited by
mining**, only by the owner's own signals; the vendored copy was never diffed
against upstream (fine — ideas are mined, not text).

**Acceptance:** the root holds only the six declared files; every triage-table
row resolved — taken or left, with the reason in its PR.

### Phase 4 — real use (→ v0.5)

**Goal:** the loop feeds on reality instead of on the library itself.

**Steps:** install `signal-capture` (and its hook) into the first working
project; fill the donor list below; run the first `/factory-review` over a
real `SIGNALS.md`; run `/factory-test` with a real task from that project;
start each working session there with `/skills-for`.

**Decisions at the gate:** the donor list; the signal threshold per project;
how often reviews run.

**Risks here:** signals simply not written (the hook reminds at session start,
and the owner's own `/signal` entries are the highest-value fuel); reviews
postponed until signals go stale (the working session watches the age of the
oldest unprocessed signal).

**Acceptance:** one full cycle end to end — a signal recorded in a real
project, grouped into a proposal, delivered as a PR, merged, and the change
traceable back to the signal that caused it.

### Phase 5 — expansion (→ v1.0)

**Goal:** the library grows on its own fuel, and the owner's time shrinks to
merge-time.

**Content:** pulled from `IDEAS.md` as each entry's *revisit when* comes true —
the researcher agent, `phase-discipline`, `agent-orchestration`,
`ux-designer`, the scheduled loop. Nothing enters by default: every candidate
passes the gates of philosophy §4 at its own mini-gate.

**v1.0 is declared when:** a full month passes in which every change to
`skills/` and `agents/` traces to real work through the loop, and the owner
spent only review time.

---

## Versions

Tagged by the owner at phase closes. `vX.Y` — no ceremony, just the tag.

| Tag | Marks |
| --- | --- |
| v0.1 | foundation in force — pull request #1 merged |
| v0.2 | the commands built and cold-run |
| v0.3 | guardrails green on a deliberate failure |
| v0.4 | sources mined out, root minimal |
| v0.5 | first real cycle closed end to end |
| v1.0 | a month lived on real fuel alone |

---

## Standing decisions

Decided by the owner on 2026-08-03:

- **Everything reaches `skills/` and `agents/` through pull requests.** Merge is
  acceptance; close is rejection; a rejection leaves no trace in the files — if
  the same idea returns, the owner says no again.
- **The loop is manual.** `/factory-loop` (or a plain request) is the only
  trigger; nothing runs on a schedule. Automation is parked in `IDEAS.md`.
- **Files carry no history** — no changelogs, no provenance blocks, no maturity
  levels. Git and the pull-request archive are the record.
- **Test tasks are generated at run time**, from real project tasks or from
  signals. Nothing test-related is stored in skill folders; synthetic rigs are
  parked in `IDEAS.md`.
- **Freshness is an audit sub-pass**, not a separate artifact — revisit if the
  library ever accumulates data-heavy skills.
- **`source-scout` follows direction (a):** a thin agent consuming
  `source-evaluation` and `confidence-check`; the generalised researcher is
  parked in `IDEAS.md`.
- **The working model:** the owner rules; one working session builds,
  strategises and criticises; an independent outside session is called only
  for the special cases the working prompt names. This file is the only
  handshake between sessions.
- **Factory work does not keep a `SIGNALS.md`** — the factory stores no raw
  signals. A working session that notices friction writes one line under "For
  the outside look" instead, or fixes it within scope.
- **Versions are git tags on phase closes**, declared by the owner.
- **The two prompts below are canon.** Paste them; do not retype them from
  memory.

---

## The risk register

What can go wrong, how it announces itself, and what we do. The working
session re-reads this at every phase close, the outside look at every visit;
anything observed gets a line in the queue below.

| Risk | Early sign | Response |
| --- | --- | --- |
| The mechanism stays prose | commands still *planned* weeks after the gate | Phase 1 goes first; nothing else starts before it |
| Noise without fuel | proposals with no channel-source named | every PR names its channel; an empty iteration is a valid result |
| Meta-work crowds out real work | most merged PRs touch the factory, not the skills used in projects | the numbers below, at every phase close; rebalance at the next gate |
| PR queue outgrows the owner | open PRs older than a week | cap of 2 holds; executor improves open PRs instead of adding |
| Mining dilutes the owner's taste | edits touching owner-preference sections | those sections change only on the owner's own signals — never by mining |
| Skills bloat past compaction | a skill's tail stops being applied in long sessions | audit's compactness pass; split into references |
| Constitution drifts from practice | a rule quoted that no one actually follows | every gate starts by diffing practice against the philosophy |
| Context lost between chats | a session re-asks what is already ruled | this file is the handshake; executors read it first, update it last |
| Platform changes break mechanics | a hook or frontmatter field stops working | freshness pass re-verifies the dated box; fixes ride ordinary PRs |
| Forgotten branches and stale PRs | a branch older than its phase | one branch per piece of work; delete on merge; the PR page is the only queue |

---

## How we evaluate

At every phase close — and whenever the owner asks — the working session
reports four numbers and one question; an outside look re-checks them
independently at its visits:

1. Merged changes to `skills/` and `agents/` this month that trace to real
   work, versus meta-work on the factory itself.
2. Age of the oldest open pull request.
3. Age of the oldest unprocessed signal across donor projects (from Phase 4).
4. Length of the current empty-iteration streak of the loop.

And the question: **did anything get explained twice this month that no skill
covers?** A yes is the next skill; a chronic no with no real use happening
means the factory is idling, not succeeding.

---

## For the outside look

The queue of things the working session must not judge alone: a disagreement
with the owner that stays stuck, a proposed constitution change, a plan it
wants to overturn, a decision that would grade its own earlier work, anything
the owner wants a fresh eye on. One line each. The owner takes the list to an
independent session; each line is cleared by a ruling, a re-plan, or a move to
`IDEAS.md`.

*Empty.*

---

## The prompts

### The working prompt

Paste into the session that runs the factory — it builds, holds gates, and
criticises, all in one:

> You are the **working session** of the Skill Factory — its builder,
> strategist and critic in one. The owner rules; you do everything else. Your
> successor is another session with this same prompt: leave the repository so
> it can continue without you.
>
> **Start every session the same way.** Read `FACTORY_PHILOSOPHY.md` (the
> rules), then `PROJECT_MEMORY.md` (the plan, the standing decisions, the
> queue), then `COMMANDS.md`. Then say in one short message: where things
> stand, what you propose to do now — a gate, a piece of work, or a critique —
> and wait for my go.
>
> **Phase gates.** A phase starts only after its gate: put every decision the
> phase will implement to me in one pass, options with a recommendation, and
> record my rulings in `PROJECT_MEMORY.md` under the phase. Once ruled, do not
> reopen them; if reality contradicts a ruling, say so and re-ask — never
> silently deviate.
>
> **Building.** One well-scoped piece at a time, each landing as a pull
> request I can review in minutes: one meaningful change per PR, mechanical
> churn in commits separate from meaning, commit subjects per philosophy §8,
> open-PR cap of 2. Never merge your own PR — my merge is acceptance, my close
> is rejection, and a rejection leaves no trace in the files.
>
> **Deciding.** A technical choice that fits the agreed vision — make it, then
> say so in one line. A small scoped choice — ask me inline, options with a
> recommendation. What philosophy §9 reserves (creating, merging or retiring
> artifacts; changing the constitution; re-planning phases) — put to me at a
> gate, never mid-task. And when you are the interested party — you want to
> rewrite a rule that blocks you, overturn a plan you wrote, or grade your own
> earlier work — queue it under "For the outside look" instead of judging your
> own case.
>
> **Criticising.** At every phase close, and whenever I ask: report the four
> numbers and the one question from "How we evaluate"; re-read the risk
> register and say which early signs you actually observe; bring anything new
> worth building as `IDEAS.md` entries with a *revisit when*. "Nothing to
> change" is a valid finding; manufacturing findings is not.
>
> **Never:** hand-edit the generated catalogue block or the stamped copies in
> `bundled/`; load anything from `to_review/` into work; keep history in the
> files; keep a `SIGNALS.md` in the factory; build ahead of an unheld gate.
>
> **End every session the same way.** Run
> `.claude/scripts/build_catalogue.py --check` and
> `.claude/scripts/sync_bundles.py --check`; update "Where things stand" (and
> any new rulings) in `PROJECT_MEMORY.md` inside the same PR as the work;
> push; then report: what changed, what you verified, what you need from me.
>
> Talk to me in the language I use. Everything committed is English.

### The outside-look prompt

Paste into a fresh session — one with none of the working context — when the
queue has lines in it or a fresh audit is wanted:

> You are an **outside reviewer** of the Skill Factory, valuable precisely
> because you carry none of its working context. Read `FACTORY_PHILOSOPHY.md`,
> `PROJECT_MEMORY.md`, the open and recently closed pull requests, and the
> "For the outside look" queue.
>
> For each queued line: rule or recommend, with reasons the owner can act on
> in one line. Then criticise freely: where the plan and reality diverge,
> which risk-register signs are actually visible, what the working session
> cannot see because it built the thing. Check the four numbers from "How we
> evaluate" independently. Recommend; do not implement — your product is
> judgement, recorded in `PROJECT_MEMORY.md` through a pull request like
> everything else.
>
> Talk to me in the language I use. Everything committed is English.

---

## The review queue

There is no generated queue: the folder listing **is** the queue. Every folder
under `to_review/` leads with its priority digit, so a plain listing sorts into
one — ascending, so 0 comes first and 4 last. Each folder carries a
`REVIEW_NOTE.md`: what the thing is, what we already have covering the ground,
what is worth taking, what to leave. Read the note, then the file.

The verdict on each is one of: adopt as a new artifact, fold into a named
existing one, merge with another queue entry, or leave it with a reason.

---

## Technical notes

- **`AI_INSTRUCTIONS (1).md` and `SKILL (1).md`** stay in the root until their
  mining completes (Phase 3); then they move to `to_review/` or leave, on the
  owner's word. They are the only permitted departure from the minimal root.
- **Signal donors** — the working repositories whose `SIGNALS.md` the loop
  reads: *none yet; filled at Phase 4.*
- **Attribution for mined material** is settled at the `/factory-mine` design
  gate. The vendored library under `to_review/skills/agent-skills-upstream/`
  keeps its own MIT licence file regardless.
- **The signals hook threshold** defaults to twenty entries; it is set per
  project when the skill is installed.
