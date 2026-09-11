#!/usr/bin/env python3
"""Проверяет, что пути, названные в файлах в силе, существуют.

Сканирует README.md, PROJECT_PHILOSOPHY_CHECK.md, skills/**/*.md,
agents/**/*.md и .claude/**/*.md. Память, идеи и журнал сигналов не
сканируются: это история и личные заметки — они цитируют пути на момент
события, и красный прогон требовал бы править цитату. Временный план
пересборки называет пути до их создания.

Путём считается строка в обратных кавычках или в markdown-ссылке, которая
начинается с папки этого репозитория — skills/, agents/, .claude/, .github/ —
либо с папки внутри артефакта — references/, bundled/, scripts/, assets/ —
и не несёт плейсхолдера <…> или шаблона *. Пути внутри to_review/ и archive/
не проверяются: зоны не в силе. Папки bundled/ не сканируются: это штампованные
копии, канон проверяется у источника. Пути внутри артефакта проверяются только
из файлов самого артефакта; заглушка .claude/agents/<имя>.md читает их от
agents/<имя>/.

Выход: список неразрешённых путей; код 1, если список не пуст.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

REPO_PREFIXES = ("skills/", "agents/", ".claude/", ".github/")
ARTIFACT_PREFIXES = ("references/", "bundled/", "scripts/", "assets/")
SKIP_PREFIXES = ("to_review/", "archive/")
ROOT_FILES = {"README.md", "PROJECT_PHILOSOPHY_CHECK.md"}

BACKTICK = re.compile(r"`([^`\n]+)`")
MDLINK = re.compile(r"\]\(([^)\s]+)\)")


def candidates(text):
    for m in BACKTICK.finditer(text):
        yield m.group(1)
    for m in MDLINK.finditer(text):
        yield m.group(1)


def artifact_dir(path):
    """Папка артефакта для файла внутри skills/<x>/ или agents/<x>/, либо для
    заглушки .claude/agents/<x>.md; иначе None."""
    rel = os.path.relpath(path, ROOT).split(os.sep)
    if rel[0] in ("skills", "agents") and len(rel) > 2:
        return os.path.join(ROOT, rel[0], rel[1])
    if rel[:2] == [".claude", "agents"] and len(rel) == 3 and rel[2].endswith(".md"):
        return os.path.join(ROOT, "agents", rel[2][:-3])
    return None


def files_to_scan():
    for name in sorted(ROOT_FILES):
        p = os.path.join(ROOT, name)
        if os.path.exists(p):
            yield p
    for top in ("skills", "agents", ".claude"):
        for dirpath, _, names in os.walk(os.path.join(ROOT, top)):
            if os.path.basename(dirpath) == "bundled":
                continue  # штампованные копии: канон проверяется у источника
            for n in sorted(names):
                if n.endswith(".md"):
                    yield os.path.join(dirpath, n)


def classify(cand, scanning_file):
    """Возвращает список путей для проверки или None, если строка — не путь."""
    if any(ch in cand for ch in "<>*"):
        return None
    if cand.startswith(SKIP_PREFIXES):
        return None
    if cand.startswith(REPO_PREFIXES):
        return [os.path.join(ROOT, cand.rstrip("/"))]
    if cand.startswith(ARTIFACT_PREFIXES):
        base = artifact_dir(scanning_file)
        if base is None:
            return None  # общий разговор об анатомии, а не указатель
        return [os.path.join(base, cand.rstrip("/"))]
    return None


def main():
    missing = []
    for f in files_to_scan():
        text = open(f, encoding="utf-8").read()
        for cand in dict.fromkeys(candidates(text)):
            tries = classify(cand, f)
            if tries is None:
                continue
            if not any(os.path.lexists(t) for t in tries):
                missing.append((os.path.relpath(f, ROOT), cand))
    if missing:
        for f, c in missing:
            print(f"{f}: не разрешается `{c}`")
        print(f"неразрешённых путей: {len(missing)}")
        return 1
    print("ссылки разрешаются")
    return 0


if __name__ == "__main__":
    sys.exit(main())
