#!/usr/bin/env python3
"""Переписывает блок каталога в README.md по самим файлам артефактов.

Только удобство. Удаление этого скрипта стоит автоматики и больше ничего:
каталог, который он пишет, — обычная проза, остающаяся читаемой и правимой в
README, а артефакты, которые он читает, и так являются источником истины.

Запуск:  python3 .claude/scripts/build_catalogue.py [--check]

--check выходит с кодом 1, если README устарел, вместо того чтобы переписывать его.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

START = "<!-- CATALOGUE:START"
END = "<!-- CATALOGUE:END -->"

def frontmatter_description(text: str) -> str:
    """Первое предложение поля description, или '', если его нет."""
    if not text.startswith("---"):
        return ""
    _, _, rest = text.partition("---")
    block, _, _ = rest.partition("\n---")
    match = re.search(r"^description:\s*(.+?)(?=^\w[\w-]*:|\Z)", block, re.S | re.M)
    if not match:
        return ""
    joined = " ".join(match.group(1).split())
    sentence, _, _ = joined.partition(". ")
    return sentence.rstrip(".") + "."


def collect(folder: str, entrypoint: str) -> list[tuple[str, str]]:
    """Строка на каждую папку артефакта: её имя и первое предложение описания,
    прочитанное из frontmatter точки входа."""
    directory = ROOT / folder
    if not directory.is_dir():
        return []
    rows = []
    for path in sorted(directory.iterdir()):
        artifact = path / entrypoint
        if not artifact.is_file():
            continue
        text = artifact.read_text(encoding="utf-8")
        rows.append((path.name, frontmatter_description(text)))
    return rows


def table(rows: list[tuple[str, str]], folder: str, empty: str) -> str:
    if not rows:
        return f"*{empty}*\n"
    lines = ["| | Что делает |", "| --- | --- |"]
    for name, description in rows:
        lines.append(f"| [`{name}`]({folder}/{name}/) | {description} |")
    return "\n".join(lines) + "\n"


def build() -> str:
    """Только то, что в силе. Зона разбора — рабочий материал, и её место в
    PROJECT_MEMORY.md, а не на титульной странице: очередь неодобренных черновиков
    на витрине сообщает посетителю, что работа не закончена."""
    return "\n" + "\n".join([
        "### Скиллы\n",
        table(collect("skills", "SKILL.md"), "skills", "Скиллов пока нет."),
        "\n### Агенты\n",
        table(collect("agents", "AGENT.md"), "agents", "Агентов пока нет."),
    ])


def splice(readme: str, catalogue: str) -> str:
    start = readme.find(START)
    end = readme.find(END)
    if start == -1 or end == -1:
        sys.exit(f"ошибка: маркеры каталога не найдены в {README}")
    head_end = readme.find("-->", start) + len("-->")
    return readme[:head_end] + catalogue + "\n" + readme[end:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    current = README.read_text(encoding="utf-8")
    updated = splice(current, build())

    if current == updated:
        print("каталог актуален")
        return 0
    if args.check:
        print("каталог устарел: запусти build_catalogue.py")
        return 1
    README.write_text(updated, encoding="utf-8")
    print("каталог переписан")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
