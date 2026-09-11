#!/usr/bin/env python3
"""Проверяет, что правила с несколькими адресатами не разошлись молча.

У некоторых правил намеренно две-три редакции — в памяти проекта для сессии, в
`AGENT.md` для агента, в философии как принцип, в скилле для любого проекта.
Убрать редакцию нельзя: папка агента работает без памяти, а память не едет в
`bundled/`. Поэтому каждая редакция объявлена здесь опорной фразой, и проверка
краснеет, когда фраза исчезла: тот, кто переписал одну редакцию, обязан
перечитать остальные.

Сравнение — по фразе, дословно, с пробелами и переносами строк, сведёнными к
одному пробелу. Новая пара объявляется здесь же, когда решение о двух адресатах
принято владельцем.

Выход: список файлов и фраз, которых больше нет; код 1, если список не пуст.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAIRS = {
    "метод фаз": [
        ("PROJECT_MEMORY_CHECK.md", "Закрытая теряет шаги, а цель заменяется описанием."),
        ("PROJECT_MEMORY_CHECK.md", "называет конкретную работу и конкретный результат, а не описывает состояние"),
        ("PROJECT_MEMORY_CHECK.md", "Замороженная фаза не меняется."),
        ("skills/git-repo-structure/SKILL.md", "закрытая теряет их и оставляет одни решения"),
        ("skills/git-repo-structure/SKILL.md", "называет конкретную работу и её результат, а не описывает состояние"),
        ("skills/git-repo-structure/SKILL.md", "Закрытая фаза не переписывается"),
        ("PROJECT_PHILOSOPHY_CHECK.md", "Работа идёт фазами."),
        ("PROJECT_PHILOSOPHY_CHECK.md", "закрывается обеими сторонами"),
    ],
    "проводка": [
        ("PROJECT_MEMORY_CHECK.md", "кто что читает: какой агент какие скиллы потребляет"),
        ("agents/skill-master/AGENT.md", "кто что читает: какой агент какие скиллы потребляет"),
    ],
    "пересечение по вопросу": [
        ("PROJECT_MEMORY_CHECK.md", "Пересечение судится по вопросу, а не по моменту."),
        ("agents/skill-master/AGENT.md", "по вопросу, на который каждый отвечает, а не по событию"),
        ("agents/skill-master/AGENT.md", "Пересечение — про вопрос, на который скилл отвечает"),
        ("skills/skill-anatomy/SKILL.md", "Пересечение соседей нормально; объединение двух методов — нет."),
    ],
    "реестр отклонённого": [
        ("PROJECT_MEMORY_CHECK.md", "возвращается в разбор только с новым сигналом за ним"),
        ("PROJECT_PHILOSOPHY_CHECK.md", "возвращается в разбор только с новым сигналом за ним"),
        ("agents/skill-master/AGENT.md", "Отклонённое не возвращается без нового сигнала"),
    ],
}


def squash(text):
    return re.sub(r"\s+", " ", text)


def main():
    missing = []
    cache = {}
    for name, anchors in PAIRS.items():
        for rel, phrase in anchors:
            if rel not in cache:
                path = os.path.join(ROOT, rel)
                cache[rel] = squash(open(path, encoding="utf-8").read()) if os.path.exists(path) else None
            text = cache[rel]
            if text is None:
                missing.append((name, rel, "файла нет"))
            elif squash(phrase) not in text:
                missing.append((name, rel, phrase))
    if missing:
        for name, rel, phrase in missing:
            print(f"{name}: {rel} больше не несёт «{phrase}»")
        print(f"разошедшихся редакций: {len(missing)}")
        return 1
    print(f"объявленные редакции на месте: {sum(len(v) for v in PAIRS.values())} фраз в {len(PAIRS)} правилах")
    return 0


if __name__ == "__main__":
    sys.exit(main())
