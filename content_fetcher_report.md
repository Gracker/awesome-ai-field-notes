# AAIF Content Fetcher Report

Generated: 2026-07-16T04:19+08:00 (Asia/Shanghai) · cron 0701a96e (AAIF hourly, 5-entry batch)

## SCAN

- `entries.json` parses as dict via `pipeline_utils.load_entries_data()`; `len(entries)=1392 == total_entries=1392`; `last_updated=2026-07-15`.
- Content directory holds 1382 `.md` files (recursive under `<repo>/content/`).
- Status distribution: {'active': 970, 'score-pending': 422}.
- Active quality distribution: {2: 2, 3: 702, 4: 175, 5: 91}.
- Tier-1 candidates (`status=active` AND `quality_score>=4` AND no content file ≥200 B): **0**.
  - Match logic: content exists iff `content/{id}.md` is present (≥200 bytes) OR `Path(local_path)` exists (≥200 bytes, case-insensitive id fallback).
  - All 266 active q≥4 entries already have a non-trivial content file.

## FETCH

- No tier-1 candidates this run -> 0 entries fetched, 0 `<repo>/content/{id}.md` writes.
- No `exec + python3 + pathlib` writes to `<repo>/content/` were necessary.
- Did **not** git push (cron rule + skill content-fetcher mode).

## SITE GENERATION

- `python3 scripts/generate-site.py` executed successfully (compatibility wrapper -> `openclaw/scripts/generate-modern-site.py`).
- Output: 729 display cards, 651 content pages, 7 channels.
- Working-tree change: `M metadata/stats.json` only (`last_updated` 2026-07-15 20:19 -> 2026-07-16 04:19). `data/entries.json` and `content/` untouched by this run.

## VALIDATION (per skill invariants)

- OK: `entries.json` is a dict with `entries` list and `total_entries`.
- OK: `len(entries) == total_entries == 1392`; `last_updated=2026-07-15`.
- OK: Entry count did not decrease (cron does not mutate `entries.json`; HEAD `4545480` reports 1392, working tree matches).
- OK: Site generation succeeded; non-deterministic build only touched `metadata/stats.json` (timestamp).
- OK: No content file writes occurred (correctly, since no candidates).
- OK: Push: NONE. Cron rule and skill both say "Do not git push" in content-fetcher mode.

## STATUS

No-op fetch (tier-1 empty). entries.json preserved, no `content/` writes, site regenerated, push skipped per cron rule.
