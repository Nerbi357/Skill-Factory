# Review note — 4-sp-dispatching-parallel-agents

**Priority: 4/4** — Short, and aimed squarely at the one thing our agent design has never been tested on.

*Not in force. This note is a proposal; the verdict is the owner's.*

**Licence: MIT** — copying and reworking is permitted with attribution.

## What it is

167 lines from `obra/superpowers` on running several agents at once: when parallelism pays, how to split work so agents do not collide, and how to merge what comes back.

## What we already have

Nothing. `living-project` names two moments that justify a large parallel run and gives no method for running one.

## What is worth taking

Whatever it says about splitting work without collisions. This is the gap between 'parallelism is a reason to use an agent' and knowing how to actually do it.

## What to leave

Judge after reading — it is short enough that it may be thinner than it looks.
