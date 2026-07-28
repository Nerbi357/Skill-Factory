#!/usr/bin/env bash
# SessionStart hook: remind the session that this project keeps a signal log, and
# say how many entries are waiting when enough have piled up.
#
# Quiet by design. It prints one short line at the start of a session and nothing
# else, ever. If it cannot find anything it stays silent rather than guessing.
#
# Install: see ../references/INSTALL.md
set -uo pipefail

THRESHOLD="${SIGNALS_THRESHOLD:-10}"

# Look where a project would plausibly keep it, nearest first.
for candidate in \
  "AI_USAGE/SIGNALS.md" \
  "docs/SIGNALS.md" \
  "SIGNALS.md"
do
  if [ -f "$candidate" ]; then
    SIGNALS_FILE="$candidate"
    break
  fi
done

if [ -z "${SIGNALS_FILE:-}" ]; then
  context="This project keeps a signal log of how the work goes. No SIGNALS.md exists yet — create one at the project root the first time something is worth recording, following the SIGNAL_CAPTURE skill."
else
  count=$(grep -c '^## [0-9]' "$SIGNALS_FILE" 2>/dev/null || echo 0)
  context="This project keeps a signal log at $SIGNALS_FILE with $count entries. Keep recording per the SIGNAL_CAPTURE skill."
  if [ "$count" -ge "$THRESHOLD" ]; then
    context="$context There are $count unprocessed signals, at or past the threshold of $THRESHOLD — offer the owner a review pass at the next natural boundary, once, and take no for an answer."
  fi
fi

# Emit as additionalContext so it reaches the model rather than the terminal.
if command -v jq >/dev/null 2>&1; then
  jq -n --arg c "$context" \
    '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$c}}'
else
  # jq is not guaranteed to exist; escape by hand rather than fail the session.
  escaped=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g')
  printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$escaped"
fi

exit 0
