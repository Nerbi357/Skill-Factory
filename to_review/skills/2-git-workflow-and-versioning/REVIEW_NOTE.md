# Review note — 2-git-workflow-and-versioning

**Priority: 2/4** — Overlaps git-repo-structure on one side and covers ground ours does not on the other.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

355 lines: trunk-based development, atomic commits, branch naming, worktrees, a save-point pattern, pre-commit hygiene, handling generated files, using git to debug.

## What we already have

`git-repo-structure` covers structure, naming and appearance. It touches branching only in one bullet.

## What is worth taking

The save-point pattern and using git bisect as a debugging tool. Both are techniques ours does not have.

## What to leave

Their commit-message convention conflicts with his, which is deliberate and stronger — his is written for the file listing.
