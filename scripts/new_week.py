#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "content" / "reference" / "templates" / "week-plan-template.md"
WEEKS = ROOT / "content" / "weeks"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python scripts/new_week.py <week_number> <start_date:YYYY-MM-DD>", file=sys.stderr)
        return 2

    week = int(sys.argv[1])
    start = datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
    end = start + timedelta(days=6)
    target = WEEKS / f"week-{week:02d}.md"
    if target.exists():
        print(f"exists: {target}", file=sys.stderr)
        return 1

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("# Week XX：标题", f"# Week {week:02d}：标题")
    text = text.replace("## 1. 介绍", f"时间建议：{start.isoformat()} 至 {end.isoformat()}。\n\n## 1. 介绍", 1)
    target.write_text(text, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
