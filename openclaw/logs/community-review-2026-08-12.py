#!/usr/bin/env python3
"""
Community Review 2026-08-12 — archive 2 clear junk duplicates.

Both target entries are score-pending with hash-like titles that match an
existing active entry on the same canonical URL. The active copies have real
titles, summaries, and content files. Archiving the score-pending copies keeps
the entry count constant, preserves the URL via the active copy, and connects
the two via the `related` field for traceability.

Conservative path required by the skill: prefer metadata fixes over deletion;
never reduce entry count.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes").resolve()
sys.path.insert(0, str(REPO / "openclaw" / "scripts"))

from pipeline_utils import load_entries_data, save_entries_data  # noqa: E402

ENTRIES = REPO / "data" / "entries.json"


def main() -> None:
    data = load_entries_data(ENTRIES)
    before_count = len(data["entries"])
    before_total = data.get("total_entries")

    # Active canonical IDs that the score-pending junk entries duplicate.
    pairs = [
        ("b3802f09", "60d9c4aa", "https://www.anthropic.com/research/automated-alignment-researchers"),
        ("145978a6", "hermex_001", "https://x.com/PMbackttfuture/status/2047562135987741009"),
    ]

    by_id = {e["id"]: e for e in data["entries"]}
    archived = []
    for junk_id, active_id, url in pairs:
        junk = by_id.get(junk_id)
        active = by_id.get(active_id)
        if junk is None or active is None:
            print(f"SKIP {junk_id}/{active_id}: entry not found")
            continue
        if junk.get("status") == "archived":
            print(f"SKIP {junk_id}: already archived")
            continue
        if (junk.get("url") or "") != url or (active.get("url") or "") != url:
            print(f"SKIP {junk_id}: URL drift (junk={junk.get('url')!r}, active={active.get('url')!r})")
            continue
        # Cross-link via related.
        related_junk = list(junk.get("related") or [])
        if active_id not in related_junk:
            related_junk.append(active_id)
        junk["related"] = related_junk

        related_active = list(active.get("related") or [])
        if junk_id not in related_active:
            related_active.append(junk_id)
        active["related"] = related_active

        junk["status"] = "archived"
        junk["updated_date"] = "2026-08-12"
        archived.append((junk_id, active_id))

    save_entries_data(data, ENTRIES)
    after_count = len(data["entries"])
    after_total = data.get("total_entries")

    print(f"Before: {before_count} entries (total_entries={before_total})")
    print(f"After:  {after_count} entries (total_entries={after_total})")
    print(f"Archived score-pending duplicates: {len(archived)}")
    for j, a in archived:
        print(f"  {j} -> archived (linked to active {a})")
    assert after_count == before_count, "entry count must not decrease"
    assert after_total == before_count, "total_entries must equal len(entries)"


if __name__ == "__main__":
    main()
