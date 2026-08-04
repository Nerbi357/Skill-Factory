# Review note — 3-source-driven-development

**Priority: 3/4** — Sits directly against confidence-check — either it sharpens it or duplicates it.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

194 lines: detect the stack and its versions, fetch the official documentation, implement from documented patterns, cite the source in the code.

## What we already have

`confidence-check` requires reading documentation before arguing from it and marks every claim. This adds the step of *citing* the source in the artifact itself.

## What is worth taking

Citation in the output — a code comment naming the doc page it came from. That survives the session; a confidence mark in a chat message does not.

## What to leave

The stack-detection procedure is mechanical and specific to package managers.
