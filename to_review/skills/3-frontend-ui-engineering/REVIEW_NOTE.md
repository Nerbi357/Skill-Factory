# Review note — 3-frontend-ui-engineering

**Priority: 3/4** — The next project ships an interactive site and ux-designer has nothing to stand on.

*Not in force. This note is a proposal; the verdict is the owner's.*

## What it is

328 lines: component architecture, state management, and a long design-system section including an explicit 'avoid the AI aesthetic' passage on spacing, typography and colour. WCAG 2.1 AA accessibility. Meaningful empty and error states.

## What we already have

`git-repo-structure` covers the repository as a surface and explicitly defers the web half. Nothing covers it yet.

## What is worth taking

'Avoid the AI aesthetic' and 'meaningful empty and error states' — both are exactly the owner's standard that a product must not look like someone's working file. The accessibility checklist travels with it.

## What to leave

React-specific component patterns, unless the site is built in React.
