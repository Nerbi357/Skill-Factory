# PROJECT MEMORY

The factory's working memory: where the work stands, what has been decided, and
the technical notes that do not belong on the showcase. `README.md` shows what
this is; this file records where it is going. It is updated as part of ordinary
work, through the same pull requests as everything else.

---

## Where things stand

- **Phase 0 — foundation repairs: built**, delivered as one pull request whose
  every change the owner approved in conversation on 2026-08-03.
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
in the root, then over `to_review/skills/agent-skills-upstream/` piece by
piece, following its own triage table. When the two originals are mined out
they move into `to_review/` or leave — on the owner's word.

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
