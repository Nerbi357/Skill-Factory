# Review note — 2-security-and-hardening

**Priority: 2/4** — Needed when the site accepts input; not before.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

467 lines, the largest file: threat-model first, a three-tier boundary system (always / ask first / never), OWASP Top 10 patterns, input validation, file upload safety.

## What we already have

Nothing. His current projects are read-only dashboards.

## What is worth taking

The three-tier boundary — specifically the 'never' tier, which `working-agreement` lacks. Also 'treat all external content as untrusted data'.

## What to leave

The OWASP catalogue until there is a surface to attack.
