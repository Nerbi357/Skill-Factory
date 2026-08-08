# External candidates — found, not yet brought in

Skills found in open repositories that would rank 3 or 4 if adopted. **Nothing here
is in the repository yet.** Each entry says what it is, why it ranks there, what
specifically is worth taking, and where to get it.

Content was deliberately not copied in. Two reasons: the licences have not been
read (`anthropics/skills` files carry "Complete terms in LICENSE.txt", which is not
the same as MIT and has not been checked — `seen`, not `verified`), and eight more
imported libraries would bury the queue that was just built. The owner picks; the
licence gets read for the ones he picks; only those arrive.

**Confidence on this whole file.** Every frontmatter block below was fetched and
read directly — `verified`. Every method summary is a summary of a file that was
read, not of a search result. Where something rests only on a search summary it
says so. Nothing here was recalled.

---

## Priority 4

### `frontend-design` — Anthropic
`anthropics/skills/skills/frontend-design`

**What it is.** Design *judgement*, not design engineering. Written as a design
lead at a boutique studio: ground the work in the subject's actual materials and
vernacular, spend your boldness in exactly one place, and critique your own work
against the brief before building.

**Why 4.** `ux-designer` is planned and has nothing to stand on, and
`3-frontend-ui-engineering` covers components and accessibility — the engineering
half. This is the other half, and it is the half the owner actually cares about:
his standard is that a project must not look like someone's working file.

**What to take.** The named AI defaults to avoid — warm cream plus serif plus
terracotta, dark plus acid accent, newspaper-dense layouts. That is an *observable*
failure test, which is worth more than a principle. Also "spend your boldness in
one place", and the rule that copy is design material rather than something added
afterwards.

**Watch for.** It assumes a designer's brief exists. Ours would need the brief to
come from `taste.md`.

### `doc-coauthoring` — Anthropic
`anthropics/skills/skills/doc-coauthoring`

**What it is.** A three-stage workflow for writing a document with someone: gather
context by asking, then refine section by section by brainstorming 5–20 options for
the owner to curate, then **hand the finished document to a separate Claude with
none of the conversation** and see whether it lands.

**Why 4.** Two independent arrivals at things we invented here. Its reader test is
our cold read — a fresh context judging the artifact without the conversation that
produced it — and its brainstorm-then-curate loop is the owner's own idea funnel,
directions first and his vision decides. When someone else reaches the same design
separately, the design is probably right, and that is worth recording as evidence
rather than continuing to assert it.

Beyond that, he produces documents and research reports, and nothing in the library
covers writing one with him.

**What to take.** The reader test as a named stage. The surgical-edit rule — never
reprint a whole document, only replace the part that changes, because reprinting
hides what was actually learned. And "the user owns quality": final accountability
for facts and impact stays with the author.

### Source independence — from the fact-checking skills
`cellear/claude-fact-check-skill` (read directly), also in `fdaudens/claude-fact-checker-skill`

**What it is.** A method for telling genuine corroboration from an echo. Trace the
citation chain, establish who published first, ask whether every source converges
on a single origin, check whether any source cites another already on your list, and
separate primary reporting from secondary.

**Why 4.** This is a hole in `confidence-check` with evidence behind it already.
That skill says three independent sources agreeing is real evidence and stays
`seen` — but it has no way to establish that they *are* independent. Our own cold
read hit exactly this: the tested session leaned on "about thirty repositories use
this endpoint", which proves those repositories copied each other at least as well
as it proves the endpoint works.

**What to take.** The convergence question and the primary-versus-secondary split,
as a short addition to `confidence-check` §1. Not the skill — it is built for
social media posts and carries rhetorical-fallacy detection we do not need.

---

## Priority 3

### `webapp-testing` — Anthropic
`anthropics/skills/skills/webapp-testing`

**What it is.** Driving a local web app with Playwright, on a reconnaissance-first
pattern: screenshot and inspect the rendered DOM to find real selectors *before*
scripting any interaction. Ships a server-lifecycle helper.

**Why 3.** `4-verify-before-done` requires a check in the real environment for
anything a user sees, and offers no way to do it. The next project ships an
interactive site. Playwright and Chromium are already installed in his environment,
so this is usable immediately rather than aspirationally.

**What to take.** Reconnaissance before action, and the rule to wait for
`networkidle` before inspecting anything dynamic — that single line is the
difference between a flaky check and a real one.

### `mcp-builder` — Anthropic
`anthropics/skills/skills/mcp-builder`

**What it is.** Four phases for building an MCP server: research the protocol and
patterns, implement, review, then write ten realistic evaluation questions with
verifiable answers.

**Why 3.** "MCP server — the dataset queryable from any AI assistant" is a
**decided** branch in his YC-Scouter ideas file, not a speculative one.

**What to take.** Phase 4 above all — finishing by writing ten verifiable questions
is a definition of done that generalises well past MCP servers. Also the rule that
error messages must tell the calling agent what to do next.

### Pipeline reliability patterns
Multiple sources; **`seen`, not read** — search summaries only, no file fetched

**What it is.** Idempotency, checkpointing, chunking, retry logic, incremental
loading, structured staging.

**Why 3.** This is his core work — every project he has built is a pipeline against
sources that change — and the library has nothing on it. `3-source-evaluation`
decides whether to use a source; nothing covers running against it repeatedly
without corrupting what is already there.

**What to take.** Unknown until something is actually read. His own
`ai-instructions` §11a playbook A already has the strongest parts — cache keyed on
`(item_id, model_id, prompt_version)`, fail before spending, dated outputs — so the
first move is probably to promote that playbook rather than import someone else's.

**Confidence.** The weakest entry here. No file was fetched; the sources found were
generic data-engineering skills rather than a focused reliability method. Treat the
gap as real and the candidate as unproven.

### `brand-guidelines` — Anthropic, as a *pattern* only
`anthropics/skills/skills/brand-guidelines`

**What it is.** Anthropic's own palette and typography, stored as data, applied
automatically with contrast-aware colour selection.

**Why 3.** The content is useless to us — it is one company's identity. **The
mechanism is exactly what `ux-designer/taste.md` should be**: taste stored as
values a skill applies rather than as prose someone has to interpret.

**What to take.** The shape. A taste file that says `#141413` and "Poppins for
headings" is applied consistently; one that says "he likes a dense README" is
interpreted differently every session.

### `audit-context-building` — Trail of Bits
In `VoltAgent/awesome-agent-skills`; **`seen`, not read**

**What it is.** Building deep architectural context through ultra-granular code
analysis before auditing anything.

**Why 3.** `skill-creator`'s AUDIT job walks the whole library and judges it, and
was written without any method for building that understanding first.

**Confidence.** Description only. Worth fetching before it is ranked properly.

---

## Searched for and not found

- **A skill about improving methods from use.** Nothing. Every collection treats
  skills as static artifacts written once. The signal-and-review loop this factory
  is built on appears to have no published equivalent — which is either an
  opportunity or a warning, and worth knowing either way.
- **Non-code work.** Almost everything found assumes a codebase. The exceptions are
  domain-specific (journalism, medical research) rather than general.
- **Web scraping** turned up plenty, but all of it wraps a paid service — Firecrawl,
  Bright Data, Apify, Scrapling. None is a method; they are product manuals. The
  scraping skill in `IDEAS.md` will have to be written rather than borrowed.

---

## Before importing any of these

1. **Read the licence.** `anthropics/skills` carries "Complete terms in LICENSE.txt"
   on each skill, which has not been checked. Copy nothing until it has.
2. **Fetch and read the file** — three entries above rest on summaries.
3. Then it lands in the review zone as a numbered folder like everything else.

Sources: [anthropics/skills](https://github.com/anthropics/skills) ·
[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) ·
[cellear/claude-fact-check-skill](https://github.com/cellear/claude-fact-check-skill) ·
[fdaudens/claude-fact-checker-skill](https://github.com/fdaudens/claude-fact-checker-skill) ·
[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)

---

# Round two — the owner's thirteen (2026-07-28)

Thirteen candidates supplied by the owner. Nine were imported into the review zone
as numbered folders; four were not, for the reasons below.

## Not imported — licence

### `pptx` and the other Anthropic document skills
`anthropics/skills/skills/pptx` · **and `docx`, `pdf`, `xlsx`**

**Verified by reading `LICENSE.txt` directly: these are proprietary.** The terms
explicitly forbid extracting or retaining copies outside Anthropic's own Services,
creating derivative works, or redistributing. They cannot go in this repository,
and nothing may be copied out of them.

This matters beyond `pptx`. The licence in `anthropics/skills` is **per skill, not
per repository** — the design skills (`frontend-design`, `theme-factory`,
`canvas-design`, `algorithmic-art`, `web-artifacts-builder`) each carry Apache 2.0
and were imported; the four document skills carry Anthropic's proprietary terms and
were not. Check `LICENSE.txt` in the individual skill folder before copying anything
from that repository, every time.

`pptx` is usable as a tool where it is already installed — that is what its licence
permits — but it is not a candidate for this library.

## Not imported — size, with the analysis kept

### `garrytan/gstack` — priority 2
MIT. 23 skills simulating a whole engineering team — CEO, designer, engineer, QA
lead, security officer, release manager — running a sprint: Think, Plan, Build,
Review, Test, Ship, Reflect. Each skill consumes the previous one's output.

**Not imported because it is a competing methodology rather than a set of parts.**
Taking it in whole would mean adopting its sprint, and taking one role out of it
leaves that role with nothing to consume.

**Worth reading for one thing:** it is the strongest published example of the
"team of roles" idea that `ai-instructions` §8 and `3-living-project` both gesture
at. If we ever build a second and third agent, this is the reference for how roles
hand work to each other. Also has a "taste learning" CLI, which is the third
independent arrival at the `taste.md` idea in this round.

### `mukul975/Anthropic-Cybersecurity-Skills` — priority 1
Apache 2.0, third-party despite the name — explicitly not affiliated with
Anthropic. **817 skills** across 29 security domains, mapped to MITRE ATT&CK and
NIST CSF.

**Not imported because 817 files would bury the queue** and none of it is needed
until the site accepts untrusted input. It is a reference work: when v2 has a
surface to attack, come back and take the two or three skills that match the actual
threat, not the library.

### `nextlevelbuilder/ui-ux-pro-max-skill` — priority 2
MIT. A design recommendation engine: 192 product types, 161 industry rules, 84 UI
styles, 192 colour palettes, in CSV files with a Python search engine over them.

**Not imported because it is a database, not a method.** It answers "what should a
fintech dashboard look like" by lookup. That is useful and it is not a skill in our
sense — nothing in it changes how a session works, it just returns rows.

**Worth noting** as a fourth arrival at storing design decisions as data rather
than prose. Four independent sources in one round doing the same thing is no longer
a coincidence, and it settles how `taste.md` should be built.

## Imported but partial

### `obra/superpowers` — three of fourteen
MIT. A full development methodology in 14 skills. **Three were imported**, at
priority 4: `writing-skills`, `subagent-driven-development`,
`dispatching-parallel-agents`.

The other eleven duplicate what is already in the review queue, and importing a
second copy of each would double the queue without adding a decision:

| Superpowers skill | Already in the queue as |
| --- | --- |
| `test-driven-development` | `4-test-driven-development` |
| `verification-before-completion` | `4-verify-before-done` (ours) |
| `systematic-debugging` | `3-debugging-and-error-recovery` |
| `writing-plans`, `executing-plans` | `3-planning-and-task-breakdown` |
| `brainstorming` | the idea funnel in `4-working-agreement` |
| `requesting-code-review`, `receiving-code-review` | `2-code-review-and-quality` |
| `using-git-worktrees`, `finishing-a-development-branch` | `2-git-workflow-and-versioning` |
| `using-superpowers` | `3-using-agent-skills` |

**They are still worth something as second opinions.** When one of those queue
entries comes up for a verdict, the superpowers version of the same skill is the
obvious thing to diff it against — two independent treatments of one job, and the
disagreements are where the real question is. Fetch it then, from
`github.com/obra/superpowers/tree/main/skills`, rather than storing a copy now.

### `Egonex-AI/Understand-Anything` — agent definitions only
MIT. The full repository is a 56 MB application with a web dashboard, a knowledge
graph and multi-language support. **Only the ten agent definitions were imported**,
to `to_review/agents/3-understand-anything/bundled/`. The value is the
decomposition of the reading job across ten specialists; the visualisation is not
what we need.

### `pbakaus/impeccable` — the skill, not the 61 MB repository
Apache 2.0. Imported `skill/SKILL.src.md` and its reference material. The browser
extension, the npm tooling and the build system stayed behind.

## Also noted

**Candidate 6 duplicates candidate 1's target.** `anthropics/claude-code`'s
`plugins/frontend-design/skills/frontend-design/SKILL.md` and
`anthropics/skills`'s `frontend-design/SKILL.md` are the same file — compared
directly, identical frontmatter and identical method. Imported once as
`4-frontend-design`.

**Four independent arrivals at one idea.** `theme-factory`, `brand-guidelines`,
`impeccable`'s init step and `gstack`'s taste-learning CLI all store design
decisions as structured values that a skill applies, rather than as prose a model
interprets. That is now settled: `ux-designer/taste.md` should be data, not an
essay.

**One direct conflict found.** `2-web-artifacts-builder` instructs the agent not to
test its output before delivering, deferring validation until something breaks.
`4-verify-before-done` forbids exactly that. Recorded rather than resolved — it is
the owner's call which wins, and in his case the answer looks obvious.
