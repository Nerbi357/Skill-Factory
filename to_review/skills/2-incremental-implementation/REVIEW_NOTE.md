# Review note — 2-incremental-implementation

**Priority: 2/4** — Useful method with no home in the library yet.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

249 lines: vertical slices, keep it compilable at every step, feature flags for incomplete work, safe defaults, rollback-friendly changes. Ships an increment checklist.

## What we already have

Nothing covers how to build in steps.

## What is worth taking

'Keep it compilable' and 'one thing at a time' generalise beyond code. The Rule 0 simplicity-first framing is good.

## What to leave

Feature flags and rollback patterns assume a deployed service.
