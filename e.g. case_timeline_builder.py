#!/usr/bin/env python3
"""
case_timeline_builder.py
Converts raw case event notes (JSON) into a formatted chronological timeline.

Usage:
    python case_timeline_builder.py notes.json --gap-hours 72 -o timeline.md

Input format (notes.json) — SYNTHETIC EXAMPLE:
[
  {"date": "2026-03-02T14:00", "note": "Account opened online."},
  {"date": "2026-02-28T09:15", "note": "Customer called support re: login issue."},
  {"date": "2026-03-10T11:30", "note": "First outbound wire requested."}
]
"""

import json
import argparse
from datetime import datetime


def load_events(path):
    with open(path, "r") as f:
        data = json.load(f)
    events = []
    for e in data:
        events.append({
            "dt": datetime.fromisoformat(e["date"]),
            "note": e["note"].strip()
        })
    return sorted(events, key=lambda x: x["dt"])


def build_timeline(events, gap_hours):
    lines = ["# Case Timeline", ""]
    prev = None
    for i, e in enumerate(events, start=1):
        stamp = e["dt"].strftime("%Y-%m-%d %H:%M")
        lines.append(f"**{i}. {stamp}** — {e['note']}")
        if prev:
            gap = (e["dt"] - prev).total_seconds() / 3600
            if gap >= gap_hours:
                lines.append(f"   > ⚠️ Gap of {gap:.1f} hours since previous entry — verify nothing missing.")
        lines.append("")
        prev = e["dt"]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Build a chronological case timeline from raw notes.")
    ap.add_argument("input", help="Path to JSON file of events")
    ap.add_argument("--gap-hours", type=float, default=48.0,
                     help="Flag gaps between entries larger than this many hours (default: 48)")
    ap.add_argument("-o", "--output", default="timeline.md", help="Output Markdown file")
    args = ap.parse_args()

    events = load_events(args.input)
    timeline_md = build_timeline(events, args.gap_hours)

    with open(args.output, "w") as f:
        f.write(timeline_md)

    print(f"Timeline written to {args.output} ({len(events)} events)")


if __name__ == "__main__":
    main()
