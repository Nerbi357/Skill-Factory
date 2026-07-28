#!/usr/bin/env python3
"""Rewrite the catalogue block in README.md from the artifact files themselves.

Convenience only. Deleting this script costs the automation and nothing else:
the catalogue it writes is plain prose that stays readable and editable in the
README, and the artifacts it reads are the source of truth either way.

Usage:  python3 .claude/scripts/build_catalogue.py [--check]

--check exits 1 if the README is out of date instead of rewriting it.
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

MATURITY = {
    "L0": "draft",
    "L1": "used",
    "L2": "tested",
    "L3": "measured",
    "L4": "proven",
}


def frontmatter_description(text: str) -> str:
    """First sentence of the description field, or '' if there is none."""
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


def maturity(text: str) -> str:
    """The level from the provenance block, as 'L1 used'."""
    match = re.search(r"^Maturity:\s*\**\s*(L[0-4])", text, re.M)
    if not match:
        return "unstated"
    level = match.group(1)
    return f"{level} {MATURITY[level]}"


def collect(folder: str, entrypoint: str) -> list[tuple[str, str, str]]:
    directory = ROOT / folder
    if not directory.is_dir():
        return []
    rows = []
    for path in sorted(directory.iterdir()):
        artifact = path / entrypoint
        if not artifact.is_file():
            continue
        text = artifact.read_text(encoding="utf-8")
        rows.append((path.name, frontmatter_description(text), maturity(text)))
    return rows


def table(rows: list[tuple[str, str, str]], folder: str, empty: str) -> str:
    if not rows:
        return f"*{empty}*\n"
    lines = ["| | What it does | Maturity |", "| --- | --- | --- |"]
    for name, description, level in rows:
        lines.append(f"| [`{name}`]({folder}/{name}/) | {description} | {level} |")
    return "\n".join(lines) + "\n"


def build() -> str:
    skills = collect("CUSTOM_SKILLS", "SKILL.md")
    agents = collect("CUSTOM_AGENTS", "AGENT.md")
    parts = [
        "### Skills\n",
        table(skills, "CUSTOM_SKILLS", "No skills yet."),
        "\n### Agents\n",
        table(agents, "CUSTOM_AGENTS", "No agents yet."),
    ]
    return "\n" + "\n".join(parts)


def splice(readme: str, catalogue: str) -> str:
    start = readme.find(START)
    end = readme.find(END)
    if start == -1 or end == -1:
        sys.exit(f"error: catalogue markers not found in {README}")
    head_end = readme.find("-->", start) + len("-->")
    return readme[:head_end] + catalogue + "\n" + readme[end:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    current = README.read_text(encoding="utf-8")
    updated = splice(current, build())

    if current == updated:
        print("catalogue is current")
        return 0
    if args.check:
        print("catalogue is out of date: run build_catalogue.py")
        return 1
    README.write_text(updated, encoding="utf-8")
    print("catalogue rewritten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
