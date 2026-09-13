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

Второй вид дубля — не фраза, а frontmatter: заглушка агента в `.claude/agents/`
несёт копию полей из его `AGENT.md`, и реестр агентов показывает устаревшее
описание молча. Такие пары сравниваются целиком, поле в поле, и объявлять текст
здесь не нужно.

Выход: список файлов и фраз, которых больше нет, и разошедшихся полей; код 1,
если список не пуст.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAIRS = {
    "метод фаз": [
        ("PROJECT_MEMORY.md", "Закрытая теряет шаги, а цель заменяется описанием."),
        ("PROJECT_MEMORY.md", "называет конкретную работу и конкретный результат, а не описывает состояние"),
        ("PROJECT_MEMORY.md", "Замороженная фаза не меняется."),
        ("skills/project-context/SKILL.md", "закрытая теряет их и оставляет одни решения"),
        ("skills/project-context/SKILL.md", "называет конкретную работу и её результат, а не описывает состояние"),
        ("skills/project-context/SKILL.md", "Закрытая фаза не переписывается"),
        ("PROJECT_PHILOSOPHY.md", "Работа идёт фазами."),
        ("PROJECT_PHILOSOPHY.md", "закрывается обеими сторонами"),
    ],
    "проводка": [
        ("PROJECT_MEMORY.md", "кто что читает: какой агент какие скиллы потребляет"),
        ("agents/skill-master/AGENT.md", "кто что читает: какой агент какие скиллы потребляет"),
        ("agents/skill-master/README.md", "кто что читает: какой агент какие скиллы потребляет"),
    ],
    # «объясняй почему» — про правило без записанного рассуждения. Строка о теле
    # коммита в разделе о гигиене `git-repo-structure` («каждый объясняет почему в
    # своём теле») в пару не входит: она о коммите, а не о правиле.
    "объясняй почему": [
        ("skills/skill-anatomy/SKILL.md", "Голый императив можно только исполнить или проигнорировать."),
        ("skills/agent-readable/SKILL.md", "Голый императив исполняется или игнорируется"),
        ("skills/project-context/SKILL.md", "решение без рассуждения можно только исполнить или проигнорировать"),
    ],
    # «механизм против манеры» — чем решают, вправе ли строка лежать в скилле.
    # Памяти в паре нет: её половина «Взаимодействие» отвечает на другой вопрос —
    # кто вправе менять манеру, а не где манера живёт.
    "механизм против манеры": [
        ("skills/skill-anatomy/SKILL.md", "Скилл целиком состоит из метода."),
        ("skills/project-context/SKILL.md", "это метод, и он входит в скилл"),
        ("agents/skill-master/AGENT.md", "живёт в рабочем соглашении памяти проекта"),
        ("agents/skill-master/JUDGEMENT.md", "а скилл состоит из метода целиком"),
    ],
    "форма секции работы агента": [
        ("skills/skill-anatomy/SKILL.md", "Секции работ внутри `AGENT.md` имеют свою форму"),
        ("skills/agent-readable/SKILL.md", "Секция работы в файле агента"),
    ],
    "ссылка называет свой файл": [
        ("PROJECT_PHILOSOPHY.md", "Перекрёстная ссылка называет свой файл, каждый раз."),
        ("PROJECT_PHILOSOPHY.md", "На номер раздела чужого файла не ссылаются вовсе — называют правило словами."),
        ("agents/skill-master/AGENT.md", "Называй файл полностью, а место внутри — словами."),
    ],
    "один вопрос на файл": [
        ("PROJECT_PHILOSOPHY.md", "У каждого файла один вопрос."),
        ("skills/git-repo-structure/SKILL.md", "Один документ на одну работу."),
        ("skills/git-repo-structure/references/FINAL_PASS.md", "Никакие два документа не отвечают на один вопрос."),
        ("agents/skill-master/JUDGEMENT.md", "Два документа, отвечающих на один вопрос."),
    ],
    "пересечение по вопросу": [
        ("PROJECT_MEMORY.md", "Пересечение судится по вопросу, а не по моменту."),
        ("agents/skill-master/AGENT.md", "по вопросу, на который каждый отвечает, а не по событию"),
        ("agents/skill-master/AGENT.md", "Пересечение — про вопрос, на который скилл отвечает"),
        ("skills/skill-anatomy/SKILL.md", "Пересечение соседей нормально; объединение двух методов — нет."),
    ],
    "реестр отклонённого": [
        ("PROJECT_MEMORY.md", "возвращается в разбор только с новым сигналом за ним"),
        ("PROJECT_PHILOSOPHY.md", "возвращается в разбор только с новым сигналом за ним"),
        ("agents/skill-master/AGENT.md", "Отклонённое не возвращается без нового сигнала"),
    ],
}


COPIES = [
    (".claude/agents/skill-master.md", "agents/skill-master/AGENT.md",
     ("name", "description", "tools")),
]


def squash(text):
    return re.sub(r"\s+", " ", text)


def field(text, key):
    """Значение поля frontmatter — или None, если поля нет."""
    if not text.startswith("---"):
        return None
    block = text.partition("---")[2].partition("\n---")[0]
    match = re.search(rf"^{key}:\s*(.+?)(?=^\w[\w-]*:|\Z)", block, re.S | re.M)
    return squash(match.group(1)).strip() if match else None


def copies():
    """Расхождения frontmatter между заглушкой и её источником."""
    diverged = []
    for stub, source, keys in COPIES:
        texts = {}
        for rel in (stub, source):
            path = os.path.join(ROOT, rel)
            texts[rel] = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if texts[stub] is None or texts[source] is None:
            diverged.append((stub, "файла нет"))
            continue
        for key in keys:
            if field(texts[stub], key) != field(texts[source], key):
                diverged.append((stub, f"поле {key} разошлось с {source}"))
    return diverged


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
    diverged = copies()
    if missing or diverged:
        for name, rel, phrase in missing:
            print(f"{name}: {rel} больше не несёт «{phrase}»")
        for rel, what in diverged:
            print(f"копия frontmatter: {rel} — {what}")
        print(f"разошедшихся редакций: {len(missing) + len(diverged)}")
        return 1
    fields = sum(len(keys) for _, _, keys in COPIES)
    print(f"объявленные редакции на месте: {sum(len(v) for v in PAIRS.values())} фраз в "
          f"{len(PAIRS)} правилах; копии frontmatter сходятся: {fields} поля")
    return 0


if __name__ == "__main__":
    sys.exit(main())
