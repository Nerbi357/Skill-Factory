#!/usr/bin/env python3
"""Обновляет штампованные копии в папке bundled/ каждого агента.

Папки агентов обязаны работать, будучи отправленными куда-то в одиночку, поэтому
каждая несёт копии нужного, а не указатели в библиотеку. Копии дрейфуют, поэтому
они генерируются здесь и штампуются источником и датой, а не правятся руками.

Каждый агент объявляет нужное ему в bundled/MANIFEST.md строками вида:

    - `<файл назначения>` <- `<путь к источнику от корня репозитория>`

Только удобство. Удаление этого скрипта стоит обновления; написанные им копии
остаются читаемыми, и агенты продолжают работать.

Запуск:  python3 .claude/scripts/sync_bundles.py [--check] [--date YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / "agents"

ENTRY = re.compile(r"^\s*-\s+`([^`]+)`\s*<-\s*`([^`]+)`\s*$", re.M)

STAMP = """<!-- ШТАМПОВАННАЯ КОПИЯ — не править.
     Источник:  {source}
     Снято:     {date}
     Канон:     правь источник и перезапусти .claude/scripts/sync_bundles.py
-->

"""


def stamped(source: str, date: str, body: str) -> str:
    return STAMP.format(source=source, date=date) + body


def sync(date: str, check: bool) -> int:
    if not AGENTS.is_dir():
        print("папки agents нет; делать нечего")
        return 0

    stale: list[str] = []
    written = 0

    for manifest in sorted(AGENTS.glob("*/bundled/MANIFEST.md")):
        bundled = manifest.parent
        entries = ENTRY.findall(manifest.read_text(encoding="utf-8"))
        if not entries:
            print(f"предупреждение: {manifest.relative_to(ROOT)} ничего не объявляет")
            continue

        for destination, source in entries:
            src = ROOT / source
            if not src.is_file():
                print(f"ошибка: {source} не существует (запрошен из {manifest.relative_to(ROOT)})")
                return 2

            dst = bundled / destination
            want = stamped(source, date, src.read_text(encoding="utf-8"))
            have = dst.read_text(encoding="utf-8") if dst.is_file() else None

            # Сравниваем только тело: повторный запуск на неизменившемся источнике
            # не должен трогать дату и производить дифф, который ничего не значит.
            if have is not None and have.split("-->\n\n", 1)[-1] == src.read_text(encoding="utf-8"):
                continue

            if check:
                stale.append(str(dst.relative_to(ROOT)))
                continue

            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(want, encoding="utf-8")
            print(f"проштамповано {dst.relative_to(ROOT)}  <-  {source}")
            written += 1

    if check:
        if stale:
            print("устаревшие копии в bundled:")
            for path in stale:
                print(f"  {path}")
            print("запусти sync_bundles.py")
            return 1
        print("копии в bundled актуальны")
        return 0

    print(f"обновлено файлов: {written}" if written else "копии в bundled и так были актуальны")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--date", default=datetime.date.today().isoformat())
    args = parser.parse_args()
    return sync(args.date, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
