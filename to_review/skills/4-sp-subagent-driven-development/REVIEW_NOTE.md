# Review note — 4-sp-subagent-driven-development

**Priority: 4/4** — The orchestration method we listed as a gap, written out with working prompts.

*Not in force. This note is a proposal; the verdict is the owner's.*

**Licence: MIT** — copying and reworking is permitted with attribution.

## What it is

503 lines plus three prompt files — an implementer prompt, a task-reviewer prompt, and a re-review prompt — and scripts. A two-stage review workflow where work is done by one subagent and reviewed by another that did not do it.

## What we already have

`FACTORY_PHILOSOPHY.md` §2 says adversarial independence justifies an agent and stops there. `skill-creator` was written without any orchestration method behind it.

## What is worth taking

The three prompt files are the valuable part: they are the actual briefs, not descriptions of briefs. Our philosophy says every brief needs five things; these are worked examples to check that against. The two-stage pattern — implement, then review by someone who did not implement — is exactly our third agent test in practice.

## What to leave

The scripts, until we know what they assume about the environment.
