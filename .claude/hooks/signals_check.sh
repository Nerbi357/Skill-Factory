#!/usr/bin/env bash
# Хук SessionStart: напоминает сессии, что этот проект ведёт журнал сигналов, и
# говорит, сколько записей ждёт, когда их накопилось достаточно.
#
# Тихий по устройству. Он печатает одну короткую строку в начале сессии и больше
# ничего, никогда. Если ничего не находит — молчит, а не гадает.
#
# Установка: см. ../references/INSTALL.md
set -uo pipefail

THRESHOLD="${SIGNALS_THRESHOLD:-20}"

# Журнал лежит в корне проекта, на виду.
if [ -f "SIGNALS.md" ]; then
  SIGNALS_FILE="SIGNALS.md"
fi

if [ -z "${SIGNALS_FILE:-}" ]; then
  context="Этот проект ведёт журнал сигналов о том, как идёт работа. SIGNALS.md пока нет — создай SIGNALS.md в корне проекта в первый раз, когда что-то будет стоить записи, следуя скиллу signal-capture."
else
  # grep -c печатает счётчик даже когда он ноль, но выходит с ненулевым кодом при
  # отсутствии совпадений — поэтому запасной путь не должен подмешать второе число.
  count=$(grep -c '^## [0-9]' "$SIGNALS_FILE" 2>/dev/null || true)
  count=${count:-0}
  context="Этот проект ведёт журнал сигналов в $SIGNALS_FILE, записей в нём: $count. Продолжай записывать по скиллу signal-capture."
  if [ "$count" -ge "$THRESHOLD" ]; then
    context="$context Неразобранных сигналов $count, это на пороге $THRESHOLD или выше — предложи владельцу проход разбора на ближайшей естественной границе, один раз, и прими «нет» за ответ."
  fi
fi

# Выдаём как additionalContext, чтобы дошло до модели, а не до терминала.
if command -v jq >/dev/null 2>&1; then
  jq -n --arg c "$context" \
    '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$c}}'
else
  # jq может отсутствовать; экранируем руками, а не роняем сессию.
  escaped=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g')
  printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$escaped"
fi

exit 0
