# Review note — 3-debugging-and-error-recovery

**Priority: 3/4** — His projects are pipelines against sources that change without warning; failure is the normal case.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

300 lines: a stop-the-line rule, then reproduce, localize, reduce, fix the root cause, guard against recurrence, verify end to end. Separate triage paths for test, build and runtime failures. Treats error output as untrusted data.

## What we already have

`verify-before-done` §6 says to suspect your own check first, and flags that it may belong to debugging instead. This is the file that settles that question.

## What is worth taking

'Reduce' as a named step — shrinking a failure to its smallest reproduction before fixing it. And the rule that a fix without a reproduction is a change with no evidence behind it.

## What to leave

The build-failure triage assumes a JS toolchain.
