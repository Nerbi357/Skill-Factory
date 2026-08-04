---
name: source-evaluation
description: Decides whether an external data source can be relied on before anything is built on it — what it actually provides, who it excludes, what it costs, and what its terms forbid. Use when a new source is being considered, when a coverage claim needs checking, when someone asks "can we get X for these companies", or before writing the first line of a parser.
---

> **DRAFT — in the review zone, not in force.** Written from a gap observed while
> planning, and from the owner's own `source-scout` agent, which already does much
> of this. His verdict decides whether this becomes a skill, folds into that agent,
> or is dropped. See the open questions at the bottom.

# Source evaluation

**What changes because of this skill:** without it, a source gets adopted because
its front page looks promising, and the exclusions, licence terms and real coverage
surface after a parser has been built on it. With it, the decision is made against
what the source actually provides, and a clean "this cannot do what we hoped" is
available as an outcome.

**Covers:** judging one external source before committing to it.
**Leaves out:** how confidently any individual fact is stated — that is
`confidence-check`, which this skill leans on throughout. Also how to build the
pipeline once the source is chosen.

---

## 1. Answer these before anything is built

Seven questions. A source is not evaluated until all seven have an answer, and
"unknown" is an answer as long as it says so.

1. **What does it actually provide** — the fields, not the marketing description.
2. **Whose records does it cover, and who is excluded?** The exclusion is usually
   the important half: one country only, filers only, companies with public code
   only, anything after 2015 only. A source with wonderful fields covering the
   wrong population is worse than no source, because the gap is invisible in the
   data itself.
3. **How is it accessed** — endpoint or bulk file, key needed, account needed.
4. **What are the limits** — rate limits, page sizes, whether a full download
   exists.
5. **What do the terms forbid** — commercial use, redistribution, attribution
   requirements. **Quote the restriction rather than summarising it.** A summary of
   a licence is an interpretation, and interpretations are what get projects into
   trouble.
6. **What could not be checked, and why.**
7. **What measurement would settle it** — the specific sample and the specific
   number that turns an estimate into a fact.

## 2. Coverage is measured, never estimated

Never report a coverage figure you did not measure. "About 80% of companies have a
website field" produced by impression is a fabricated statistic that will be quoted
back for months.

Say **unmeasured**, and describe the measurement that would settle it: take N
records, count how many carry the field non-empty, report the fraction with the
date. That is usually twenty minutes and it converts the largest unknown in any
source decision into a fact.

## 3. Check the free path first, and check whether it already exists

Before paying, look for the free route. Before building, look for whether someone
already publishes the thing — a maintained dataset usually beats a private
reimplementation, and finding one is often the single highest-value hour of a
project.

This is skipped more often than any other step, because searching does not feel
like progress the way building does.

## 4. Prefer primary sources, and do not attack the target

Official documentation beats a blog post about it. A third-party wrapper's README
is evidence about the wrapper, not about the source.

Do not hammer an endpoint to discover its rate limit — read the documented one. A
source that notices you probing is a source that may stop answering.

## 5. A clean negative is a result

If the honest answer is "this source cannot do what was hoped", say it in the first
line. It is a finding, it is cheaper now than after a parser exists, and it usually
points at what the real requirement was.

## 6. What to hand back

A short table — one row per question in §1 — plus the caveats. Every claim carries
its confidence mark. No preamble, no restatement of the brief.

---

## Owner preferences

- **Open sources only.** Never paywalled, and never a fact the source does not
  publish. This is a project rule, not a budget preference.
- **The exclusion matters more than the inclusion.** In his YC work the question
  that decided everything was not what the source held but what it left out —
  fields that never move, and companies that never appear.
- **A source decision is conceptual, not technical.** It changes what the project
  can claim, so it is his call, not one to be made while implementing.

---

## Open questions for the owner

**Is this a skill at all, or only an agent?** Evaluating a source generates a lot
of noise for one conclusion and can run in parallel across several sources — two of
the five tests, so the agent shape is justified. The argument for also having a
skill is that the *method* should be readable by whoever is working, not only
delegated: you often judge a source in passing without spinning up an agent.

Three ways this could go:

- **(A)** Keep both: this skill holds the method, `source-scout` reads it and adds
  isolation and parallelism. Consistent with "agents consume skills".
- **(B)** Agent only. Simpler, one file, but the method is then unavailable to
  anyone not delegating.
- **(C)** Skill only, drop the agent. Loses parallel evaluation of several sources,
  which is exactly what a multi-source project needs.

Leaning **(A)** — it is the pattern the philosophy already prescribes, and the next
project evaluates many sources at once.

**Where does the evicted "check the free path" rule live?** It was removed from
`confidence-check` as unrelated to how well a fact is known, and it appears here as
§3 — but it also already appears in `source-scout`. If (A) is chosen it belongs in
exactly one of them, and this skill is the natural home.
