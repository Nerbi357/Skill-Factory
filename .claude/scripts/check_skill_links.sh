#!/usr/bin/env bash
# Каждый скилл в силе подключён ссылкой из .claude/skills/, и каждая ссылка там
# ведёт на скилл в силе. Ссылка не создаётся вводом в силу — проверено 2026-08-19,
# когда три скилла из четырёх стояли без неё; с тех пор это считает машина.
set -uo pipefail
cd "$(dirname "$0")/../.."
bad=0
for d in skills/*/; do
  n=$(basename "$d")
  l=".claude/skills/$n"
  if [ ! -L "$l" ] || [ ! -f "$l/SKILL.md" ]; then
    echo "скилл без ссылки или ссылка не разрешается: $l"; bad=1
  fi
done
for l in .claude/skills/*; do
  [ -e "$l" ] || continue
  n=$(basename "$l")
  if [ ! -d "skills/$n" ]; then
    echo "ссылка без скилла в силе: $l"; bad=1
  fi
done
if [ "$bad" -eq 0 ]; then
  echo "каждый скилл подключён ссылкой: $(ls -d skills/*/ | wc -l | tr -d ' ')"
fi
exit "$bad"
