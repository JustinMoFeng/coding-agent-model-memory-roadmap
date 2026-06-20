#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "content" / "reference" / "templates" / "week-plan-template.md"
WEEKS = ROOT / "content" / "weeks"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python scripts/new_week.py <start_date:YYYY-MM-DD> <title>", file=sys.stderr)
        return 2

    start = datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
    title = sys.argv[2]
    end = start + timedelta(days=6)
    week_dir = WEEKS / start.isoformat()
    index = week_dir / "index.md"
    if week_dir.exists():
        print(f"exists: {week_dir}", file=sys.stderr)
        return 1

    week_dir.mkdir(parents=True)
    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("# YYYY-MM-DD 至 YYYY-MM-DD：标题", f"# {start.isoformat()} 至 {end.isoformat()}：{title}")
    text = text.replace("时间建议：YYYY-MM-DD 至 YYYY-MM-DD。", f"时间建议：{start.isoformat()} 至 {end.isoformat()}。")
    index.write_text(text, encoding="utf-8")

    day_template = ROOT / "content" / "reference" / "templates" / "daily-log-template.md"
    day_text = day_template.read_text(encoding="utf-8")
    for i in range(7):
        day = start + timedelta(days=i)
        (week_dir / f"{day.isoformat()}.md").write_text(day_text.replace("# YYYY-MM-DD", f"# {day.isoformat()}"), encoding="utf-8")

    print(index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
