# Review note — 2-web-artifacts-builder

**Priority: 2/4** — Useful only if the interactive site is built as a single-file artifact, which is not the current plan.

*Not in force. This note is a proposal; the verdict is the owner's.*

**Licence: Apache 2.0** — copying and reworking is permitted; attribution and a change notice must travel with any derivative.

## What it is

73 lines plus scripts. Builds elaborate multi-component HTML artifacts with React, Tailwind and shadcn/ui bundled into one self-contained file, for claude.ai artifacts specifically.

## What we already have

Nothing. The existing dashboard is Streamlit.

## What is worth taking

One line worth stealing regardless: it warns against 'excessive centered layouts, purple gradients, uniform rounded corners, and Inter font' — another observable list of defaults to avoid, alongside the one in `4-frontend-design`.

## What to leave

Most of it, unless the site becomes an artifact. **It also tells the agent not to test before delivering, which directly contradicts `4-verify-before-done`** — worth noting as a real conflict rather than a nuance.
