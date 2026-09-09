#!/usr/bin/env bash
# Число, которое печатает хук сигналов, равно числу записей в SIGNALS.md.
# Записи считаются по форме заголовка — «## <метка> · <дата> · <вид> · <тема>», —
# а не по тому же образцу, что у хука: иначе оба ошибутся одинаково и молча.
set -uo pipefail
cd "$(dirname "$0")/../.."

hook=$(bash skills/signal-capture/scripts/signals_check.sh 2>/dev/null | grep -o 'записей в нём: [0-9]*' | grep -o '[0-9]*$')
hook=${hook:-нет}
real=$(grep -cE '^## [^ ]+ · [0-9]{4}-[0-9]{2}-[0-9]{2} · ' SIGNALS.md 2>/dev/null || true)
real=${real:-0}

if [ "$hook" != "$real" ]; then
  echo "хук считает: $hook, записей по форме заголовка: $real"
  exit 1
fi
echo "счётчик сигналов сходится: $real"
