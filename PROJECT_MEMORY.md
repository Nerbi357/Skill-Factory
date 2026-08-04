# PROJECT MEMORY

The factory's working memory: where the work stands, what has been decided, and
the technical notes that do not belong on the showcase. `README.md` shows what
this is; this file records where it is going. It is updated as part of ordinary
work, through the same pull requests as everything else.

---

## Where things stand

- **Phase 0 — foundation repairs: built**, delivered as one pull request whose
  every change the owner approved in conversation on 2026-08-03.
- **The review zone is stocked.** Work from a parallel session was carried over
  and rebuilt in this repository's shape: the vendored bundle decomposed into one
  folder per artifact, thirteen further candidates imported with their licences
  checked, and a `REVIEW_NOTE.md` in every folder. Forty-three methods and six
  workers now wait for a verdict.
- **Phase 1 — the commands: next.** Its decisions are put to the owner at its
  gate before anything is built.

---

## The plan

Each phase opens with its decisions put to the owner in one pass; nothing in a
phase is built before he rules. Later phases are direction, not commitment.

**Phase 1 — the commands.** Build the seven registered in `COMMANDS.md`
(`factory-new`, `factory-review`, `factory-mine`, `factory-test`,
`factory-loop`, `signal`, `skills-for`) as skills with
`disable-model-invocation: true`: canonical folders in `skills/`, made
invocable in this repository, the agent installed for delegation. Acceptance:
a cold run of each command on real material — `factory-mine` on `grilling` is
the natural first test.

**Phase 2 — guardrails.** CI on every pull request: the catalogue check, the
bundle check, an anatomy lint (frontmatter, difference sentence, scope lines,
no history in files), a link check. Optionally a manual `workflow_dispatch`
entry so the loop can be started from the repository page.

**Phase 3 — mining the sources.** `/factory-mine` over the two original files
in the root, then down the review queue in priority order — the fours first,
each folder's `REVIEW_NOTE.md` saying what to take before the file is opened.
When the two originals are mined out they move into `to_review/` or leave — on
the owner's word.

**Phase 4 — real projects.** `signal-capture` installed into working
repositories, the donor list below filled in, the first real reviews run on
accumulated signals.

**Phase 5 — grows from `IDEAS.md`.** The researcher agent, the orchestration
skill, the rest — each pulled out when its "revisit when" comes true. Scheduled
automation of the loop belongs here too, when manual mode starts to feel slow.

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
- **Open-PR cap: 2** — proposed default, to confirm or change at the Phase 1
  gate. At the cap the loop improves open pull requests instead of adding more.

---

## How we evaluate

Reported at every phase close, and whenever the owner asks. Four numbers and one
question. "Nothing to change" is a valid finding; manufacturing findings is not.

1. **In force** — how many skills and agents are approved and usable. This should
   grow slowly. Fast growth here is a warning, not an achievement.
2. **Loaded in real work since the last close** — how many of them a project
   actually pulled in. The number that matters most: a library nothing loads is
   decoration, however well written.
3. **Changes traceable to a signal** — of the edits made since the last close, how
   many came from a recorded observation rather than from someone's opinion. This
   is whether the loop is real.
4. **Queue depth** — how many items sit in `to_review/` awaiting a verdict. Rising
   while the first number holds still means intake is outrunning judgement.

**The question:** *what did you have to explain to me this period that a skill
should already have covered?* No number finds a gap; only this does, and its
answer is usually the next skill.

## Risk register

Named risks with the early signs to watch. At every phase close, say which signs
are **actually observed** — not which are conceivable.

| Risk | Early sign |
| --- | --- |
| The library grows faster than it is used | queue depth rises while nothing new is loaded in real work |
| Rules accumulate from opinion, not evidence | changes with no signal behind them; number 3 falling |
| Skills bloat past what survives a long session | any in-force skill approaching the compaction ceiling; sections restating a neighbour |
| The loop never actually runs | no `SIGNALS.md` in any working repository; the donor list still empty after Phase 4 |
| The agent judges its own case | proposals that conveniently remove a constraint on the agent; own work graded without an outside look |
| Borrowed material gets adopted whole | a `to_review/` folder reaching `skills/` unchanged |
| The factory becomes the project | months of library work with no project the better for it |

## For the outside look

Where the session is the interested party, its judgement is queued here instead of
acted on. Cleared by the owner, or by a session that did not make the call.

- **The priority digits on `to_review/` folder names.** This session chose the
  ranking and then wrote the notes that justify it. Both the scale and the
  individual placements deserve an outside eye.
- **The review notes themselves.** Each says what we already have that covers the
  ground — written by the session that also wrote much of what is being compared
  against.
- **Which upstream skills were called duplicates.** Eleven of `superpowers`'
  fourteen were left out as already covered. That call was made by the author of
  the things they supposedly duplicate.

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
- **Every `to_review/` folder carries a `REVIEW_NOTE.md`**: a priority from 0 to 4,
  what the thing is, what we already have covering the ground, what is worth taking
  and what to leave. The priority is also the first character of the folder name,
  so a plain listing sorts into a queue — ascending, so 0 comes first and 4 last.
  Read the note before the file.
- **Licences are per skill, not per repository.** `anthropics/skills` proves it:
  its design skills carry Apache 2.0, its document skills (`pptx`, `docx`, `pdf`,
  `xlsx`) carry Anthropic proprietary terms that forbid copies outside their own
  services. Nothing from those is in this repository. Check `LICENSE.txt` in the
  individual folder before copying anything, every time.
- **`to_review/skills/candidates-external.md`** holds eight further candidates
  found but deliberately not imported — licence unread, or too large to bring in
  without burying the queue. Each says what it is and what to take from it.
