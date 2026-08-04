# Review note — 4-doubt-driven-development

**Priority: 4/4** — Writes out the method behind our third agent test, which we assert but never describe.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

243 lines: every non-trivial decision is extracted into its smallest reviewable unit and handed to a fresh context told to attack it. Five steps — CLAIM, EXTRACT, DOUBT, RECONCILE, STOP — with an explicit bound so it does not recurse forever.

## What we already have

`FACTORY_PHILOSOPHY.md` §2 says adversarial independence justifies an agent, and stops there. We have the principle and no procedure.

## What is worth taking

The whole five-step loop, especially STOP — a bounded review rather than recursion is the part everyone gets wrong. Also 'extract the smallest reviewable unit', which is what makes a fresh-context review affordable at all.

## What to leave

Its framing assumes code. The loop generalises to any decision; the examples do not.
