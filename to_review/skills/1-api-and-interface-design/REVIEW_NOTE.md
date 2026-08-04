# Review note — 1-api-and-interface-design

**Priority: 1/4** — Only if v2 exposes an API or an MCP server.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

294 lines: contract first, Hyrum's Law, the one-version rule, consistent error semantics, validate at boundaries, prefer addition over modification.

## What we already have

Nothing.

## What is worth taking

'Prefer addition over modification' and validating at boundaries — both apply to a data schema, not just an API.

## What to leave

REST and TypeScript specifics.
