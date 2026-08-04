# Review note — 3-understand-anything

**Priority: 3/4** — Ten agent definitions forming a pipeline that builds understanding of a codebase before acting on it.

*Not in force. This note is a proposal; the verdict is the owner's.*

**Licence: MIT** — copying and reworking is permitted with attribution.

## What it is

From `Egonex-AI`, MIT. A multi-agent pipeline: project-scanner discovers files and languages, file-analyzer extracts symbols into graph nodes, architecture-analyzer identifies layers, domain-analyzer extracts business domains, tour-builder generates a dependency-ordered walkthrough, graph-reviewer validates completeness. Only the agent definitions were imported — the full repository is a 56 MB application with a web dashboard.

## What we already have

`skill-creator`'s AUDIT job walks the library and judges it, with no method for building understanding first. Nothing else covers comprehending an unfamiliar codebase.

## What is worth taking

**The pipeline shape**: scan, analyse, then a reviewer whose only job is to check the result is complete. That last agent is the 'completeness critic' pattern and we have nothing like it. Also the tour-builder's ordering-by-dependency idea, which is how a phase plan should be ordered too.

## What to leave

The knowledge-graph machinery and the dashboard. The value here is the decomposition of the reading job, not the visualisation.
