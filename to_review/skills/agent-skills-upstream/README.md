# agent-skills — borrowed, for mining

A vendored copy of [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills):
24 skills, 4 specialist agents, 8 commands and 7 reference checklists.

**MIT licence, Copyright (c) 2025 Addy Osmani.** The full text is in `LICENSE`
beside this file and stays with any copy. Anything mined out of here and reworked
into our own skills carries an attribution line in that skill's provenance block —
not because the licence demands it for a rewritten idea, but because knowing where
a rule came from is the point of a provenance block.

**Nothing here is in force.** It sits in the review zone, is never loaded during
real work, and is not held to our standards. It is a construction kit.

It contains agent material as well as skills. It lives under the skills review
folder because it is one borrowed library, not because everything inside it is a
skill.

*(This copy was taken from the owner's YC-Scouter repository, which vendored it and
states it is unmodified. Not diffed against upstream — `seen`, not `verified`. Two
artifacts he wrote himself were removed from the copy: `living-project`, already in
our review zone, and the `source-scout` agent, moved to
`to_review/agents/source-scout/`.)*

---

## How this gets mined

Per `FACTORY_PHILOSOPHY.md` §1, borrowed work is never promoted whole. Each file
that earns attention is taken apart into its smallest usable ideas; each idea is
checked against what is already in force; only what survives is proposed, as an
extension to a named skill, a merge, or the seed of a new one. What is left behind
is reported with a reason.

One file at a time, in an order the owner sets. The table below is the triage that
sets it — a first pass over descriptions and sizes, not a reading of the contents.

---

## Triage

**Verdicts are proposals.** `open first` means the file most likely holds something
we lack. `compare` means we already cover the ground and the question is whether
their version is better. `later` means useful but not for the work in front of us.
`skip` means no visible claim on our library yet.

### Skills

| Skill | Size | Verdict | Why |
| --- | --- | --- | --- |
| `doubt-driven-development` | 243l | **open first** | Adversarial review by a fresh context is exactly our third agent test, written out as a method. Nothing of ours covers it. |
| `using-agent-skills` | 191l | **open first** | Their answer to the routing problem we solved with a catalogue and `skills-for`. Direct comparison of two designs for one job. |
| `test-driven-development` | 398l | **open first** | `verify-before-done` is a draft with no method for writing the tests themselves. Largest concrete gap. |
| `source-driven-development` | 194l | **open first** | "Ground every decision in official documentation" sits right against `confidence-check`. Either it sharpens it or it duplicates it — worth knowing which. |
| `frontend-ui-engineering` | 328l | **open first** | The next project ships an interactive site, and `ux-designer` has nothing to stand on yet. |
| `git-workflow-and-versioning` | 355l | compare | Overlaps `git-repo-structure`. Ours covers structure and appearance; theirs covers branching and releases, which ours only touches. |
| `interview-me` | 225l | compare | Same job as `grilling`, already in review. Compare the two before either is adopted. |
| `idea-refine` | 178l +4 files | compare | Overlaps the idea funnel inside `working-agreement`. Also the only one shipping scripts and reference files — worth seeing how they structure that. |
| `context-engineering` | 289l | compare | About configuring an agent's context, which is what this whole factory does. Likely to argue with our design rather than extend it. |
| `code-review-and-quality` | 396l | later | Feeds `verify-before-done` once its shape is settled. |
| `planning-and-task-breakdown` | 234l | later | For the phase skill we have not written. |
| `spec-driven-development` | 206l | later | For the project-bootstrap skill we have not written. |
| `incremental-implementation` | 249l | later | Method for building in steps; no home yet. |
| `debugging-and-error-recovery` | 300l | later | Has a claim on `verify-before-done` §6, which is flagged as possibly belonging to debugging. |
| `security-and-hardening` | 467l | later | When the site takes untrusted input. Largest file in the set. |
| `performance-optimization` | 350l | later | When there is something measured to be slow. |
| `observability-and-instrumentation` | 203l | later | When something runs in production unattended. |
| `shipping-and-launch` | 310l | later | When v2 actually ships. |
| `ci-cd-and-automation` | 390l | later | He already has working Actions; read when they need changing. |
| `documentation-and-adrs` | 288l | later | Recording decisions — partially covered by our provenance blocks. |
| `api-and-interface-design` | 294l | later | If v2 exposes an API or an MCP server. |
| `browser-testing-with-devtools` | 317l | later | Requires an MCP server we do not have. Read when we do. |
| `code-simplification` | 331l | skip | No current need. |
| `deprecation-and-migration` | 247l | skip | Nothing to deprecate yet. |

### Agents

| Agent | Size | Verdict | Why |
| --- | --- | --- | --- |
| `web-performance-auditor` | 184l | **open first** | Closest thing here to `ux-designer`, and the next project has a site to audit. |
| `code-reviewer` | 97l | compare | A short persona file — a useful check on whether our `skill-creator` is the right length. |
| `test-engineer` | 95l | later | With `test-driven-development`. |
| `security-auditor` | 112l | later | With `security-and-hardening`. |

### References

| Reference | Size | Verdict | Why |
| --- | --- | --- | --- |
| `orchestration-patterns.md` | 370l | **open first** | Agent orchestration was on our list and never written. Largest reference here. |
| `definition-of-done.md` | 67l | **open first** | Small, and directly aimed at `verify-before-done`'s central question. |
| `testing-patterns.md` | 235l | later | With `test-driven-development`. |
| `security-checklist.md` | 205l | later | With security. |
| `accessibility-checklist.md` | 160l | later | With the site. |
| `performance-checklist.md` | 153l | later | With performance. |
| `observability-checklist.md` | 91l | later | With observability. |

### Commands

All eight are thin wrappers — four to sixteen lines that invoke a skill by name.
Nothing to mine as content. What is worth taking is the **pattern**: a command that
does nothing but name a skill and set the context it runs in. Two of them,
`ship.md` (72l) and `build.md` (44l), are longer and compose several skills — those
two are worth reading when our own commands get built.

---

## Proposed order

Eight files, in three sittings. Each one produces a report and a list of proposed
changes; nothing moves without the owner's verdict.

1. **The gap sitting** — `doubt-driven-development`, `orchestration-patterns.md`.
   Both are about how agents check each other, which we designed by hand and never
   wrote down.
2. **The overlap sitting** — `using-agent-skills`, `source-driven-development`,
   `definition-of-done.md`. All three argue with something we already have; the
   output is either a sharpening or a confirmation that ours is better.
3. **The next-project sitting** — `test-driven-development`,
   `frontend-ui-engineering`, `web-performance-auditor`. All three feed work that
   is about to start.

The remaining sixteen stay here until something needs them. A file nobody ever
claims is itself a finding.
