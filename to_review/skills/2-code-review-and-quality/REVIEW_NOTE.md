# Review note — 2-code-review-and-quality

**Priority: 2/4** — Feeds verify-before-done once that skill's shape is settled.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

396 lines: a five-axis review — correctness, readability, architecture, security, performance — with a process that reviews the tests before the implementation and verifies the verification.

## What we already have

`verify-before-done` covers proving your own work; this covers judging someone else's.

## What is worth taking

'Review the tests first' and 'verify the verification' — both attack the case where the check itself is wrong, which is a rule we already have in a weaker form.

## What to leave

The five axes are a code-specific frame.
