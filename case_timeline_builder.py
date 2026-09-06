#!/usr/bin/env python3
"""
case_timeline_builder.py
Converts raw case event notes (JSON) into a formatted chronological timeline.

Live demo: https://biancabcarlson.github.io/Case-Timeline-Builder/

Usage:
    python case_timeline_builder.py notes.json --gap-hours 72 -o timeline.md

Input format (notes.json) — SYNTHETIC EXAMPLE:
[
  {"date": "2026-08-28T18:41", "note": "Password reset requested via self-service portal."},
  {"date": "2026-08-30T00:18", "note": "Two-factor method changed from SMS to email."},
  {"date": "2026-08-30T00:24", "note": "Login succeeded from a foreign IP shortly after the 2FA change."},
  {"date": "2026-08-31T09:40", "note": "New external payee added to account."},
  {"date": "2026-08-31T10:15", "note": "Outbound withdrawal request submitted to the new payee."}
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
