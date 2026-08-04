# Review note — 2-context-engineering

**Priority: 2/4** — Argues with the factory's own design rather than extending it.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

289 lines: a five-level context hierarchy — rules files, specs, source files, error output, conversation management — plus packing strategies.

## What we already have

This whole repository is an answer to the same question. Reading it is a check on our design, not a source of parts.

## What is worth taking

Level 5, conversation management, is the one part we have not thought about: what to do when a session gets long.

## What to leave

Most of it. Their rules-file format is CLAUDE.md-shaped; ours is a skill library.
