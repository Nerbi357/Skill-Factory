# Review note — 1-observability-and-instrumentation

**Priority: 1/4** — For when something runs unattended in production.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

203 lines: define 'working' before instrumenting, pick the right signal per question, structured logging, metrics, tracing, alerting, verify the telemetry itself.

## What we already have

Nothing.

## What is worth taking

'Define working before instrumenting' and 'verify the telemetry itself' — the second is our own suspect-your-own-check rule in another domain.

## What to leave

The tracing and metrics stacks.
