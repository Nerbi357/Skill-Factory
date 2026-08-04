# Review note — 4-test-driven-development

**Priority: 4/4** — The largest concrete gap in the library, against the owner's strongest stated request.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

398 lines: the red-green-refactor cycle, a Prove-It pattern for bug fixes (write the test that reproduces it first), the test pyramid with a resource model, and a long section on writing tests that fail for the right reason — test state not interactions, real implementations over mocks, DAMP over DRY.

## What we already have

`verify-before-done` (draft) says work must be proved to function but contains no method for writing the proof. It is a standard with no technique behind it.

## What is worth taking

The Prove-It pattern above all — a bug fix that starts with a failing reproduction is exactly the owner's 'proof not assertion'. Also 'test state, not interactions' and 'prefer real implementations over mocks', both of which prevent the suite that passes while the product is broken.

## What to leave

The test-pyramid taxonomy and the resource model are heavier than his projects need. The language-specific sections assume a web stack.
