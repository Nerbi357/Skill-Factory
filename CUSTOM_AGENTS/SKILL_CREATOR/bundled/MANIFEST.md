# Bundled

Stamped copies of what this agent needs, so the folder works when sent somewhere
on its own. **Do not edit anything in here.** Edit the source and run
`.claude/scripts/sync_bundles.py`, which rewrites these from the canonical files
and re-stamps them.

Declared as `` `destination` <- `source` ``; the sync script reads these lines.

- `FACTORY_PHILOSOPHY.md` <- `FACTORY_PHILOSOPHY.md`
- `RESEARCH_WITH_CONFIDENCE.md` <- `CUSTOM_SKILLS/RESEARCH_WITH_CONFIDENCE/SKILL.md`

## Why these two

The philosophy holds every rule an artifact must obey — the anatomy, the maturity
ladder, the gates, the review loop. Without it the agent can read the library but
cannot judge it against anything.

`RESEARCH_WITH_CONFIDENCE` is here because the agent's core act is weighing how
well a proposal is evidenced, and that skill is how this library separates a
claim backed by three independent signals from one backed by an impression.
