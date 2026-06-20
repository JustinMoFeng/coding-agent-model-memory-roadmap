#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "content" / "reference" / "templates" / "experiment-log.md"
EXPERIMENTS = ROOT / "content" / "experiments"


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s)
    return s.strip("-")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/new_experiment.py <slug>", file=sys.stderr)
        return 2

    EXPERIMENTS.mkdir(parents=True, exist_ok=True)
    slug = slugify(sys.argv[1])
    target = EXPERIMENTS / f"{slug}.md"
    if target.exists():
        print(f"exists: {target}", file=sys.stderr)
        return 1

    body = TEMPLATE.read_text(encoding="utf-8")
    frontmatter = (
        "---\n"
        "type: experiment\n"
        f"slug: {slug}\n"
        "status: planned\n"
        "tags: []\n"
        f"created: {date.today().isoformat()}\n"
        "---\n\n"
    )
    target.write_text(frontmatter + body, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
