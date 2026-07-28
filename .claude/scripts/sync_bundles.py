#!/usr/bin/env python3
"""Refresh the stamped copies in every agent's bundled/ folder.

Agent folders must work when sent somewhere alone, so each one carries copies of
what it needs rather than pointers into the library. Copies drift, so they are
generated here and stamped with their source and date instead of being edited.

Each agent declares what it needs in bundled/MANIFEST.md, as lines of the form:

    - `<destination file>` <- `<source path relative to the repo root>`

Convenience only. Deleting this script costs the refresh; the copies it wrote stay
readable and the agents keep working.

Usage:  python3 .claude/scripts/sync_bundles.py [--check] [--date YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / "CUSTOM_AGENTS"

ENTRY = re.compile(r"^\s*-\s+`([^`]+)`\s*<-\s*`([^`]+)`\s*$", re.M)

STAMP = """<!-- STAMPED COPY — do not edit.
     Source:      {source}
     Taken:       {date}
     Canonical:   edit the source and rerun .claude/scripts/sync_bundles.py
-->

"""


def stamped(source: str, date: str, body: str) -> str:
    return STAMP.format(source=source, date=date) + body


def sync(date: str, check: bool) -> int:
    if not AGENTS.is_dir():
        print("no CUSTOM_AGENTS directory; nothing to do")
        return 0

    stale: list[str] = []
    written = 0

    for manifest in sorted(AGENTS.glob("*/bundled/MANIFEST.md")):
        bundled = manifest.parent
        entries = ENTRY.findall(manifest.read_text(encoding="utf-8"))
        if not entries:
            print(f"warning: {manifest.relative_to(ROOT)} declares nothing")
            continue

        for destination, source in entries:
            src = ROOT / source
            if not src.is_file():
                print(f"error: {source} does not exist (wanted by {manifest.relative_to(ROOT)})")
                return 2

            dst = bundled / destination
            want = stamped(source, date, src.read_text(encoding="utf-8"))
            have = dst.read_text(encoding="utf-8") if dst.is_file() else None

            # Compare the body only: a re-run on an unchanged source must not
            # churn the date and produce a diff that means nothing.
            if have is not None and have.split("-->\n\n", 1)[-1] == src.read_text(encoding="utf-8"):
                continue

            if check:
                stale.append(str(dst.relative_to(ROOT)))
                continue

            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(want, encoding="utf-8")
            print(f"stamped {dst.relative_to(ROOT)}  <-  {source}")
            written += 1

    if check:
        if stale:
            print("stale bundled copies:")
            for path in stale:
                print(f"  {path}")
            print("run sync_bundles.py")
            return 1
        print("bundled copies are current")
        return 0

    print(f"{written} file(s) refreshed" if written else "bundled copies were already current")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--date", default=datetime.date.today().isoformat())
    args = parser.parse_args()
    return sync(args.date, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
