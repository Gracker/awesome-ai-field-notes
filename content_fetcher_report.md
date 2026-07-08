# AAIF Content Fetcher Report

Generated: 2026-07-08T20:33+08:00 (Asia/Shanghai)

## STATISTICS

- Total Entries: 1163 (preserved; entries.json untouched by this cron)
- Tier-1 active q>=4 missing-content candidates: 0
- Tier-2 fallback q>=3 missing-content candidates: 64
- Tier used: 2 (fallback q>=3 most-recent)
- Files written this run: 2

## ARTIFACTS

Wrote 2 content files via `exec + python3 + pathlib` with absolute paths:

| ID | Title | URL | Source | Bytes |
|---|---|---|---|---|
| `14667f46` | Show HN: Smart model routing directly in Claude, Codex  | <https://github.com/workweave/router> | GitHub raw README@master 200 via urllib (24170 bytes) | 18665 |
| `7a48d6db` | Ultrasound imaging of the brain | <https://alephneuro.com/blog/ultrasound-brain> | HTTP 200 via urllib | 6237 |

**Skipped (3)**:
- `fb435a03` — HTTP 403 or too small (0b)
- `1ae317c0` — HTTP 403 or too small (0b)
- `2b6976f9` — HTTP 403 or too small (0b)

## VALIDATION

- ✓ entries.json parses as dict (`len(entries) == 1163 == total_entries == 1163`).
- ✓ entries.json NOT modified by this cron (content-fetcher mode).
- ✓ Written files non-empty (>= 2KB each, all 2 files).
- ✓ No git push (content-fetcher mode per skill: Do not push).

## SUMMARY

Content fetcher ran successfully. Wrote 2 content file(s) at tier 2, regenerated the static site, did not modify entries.json, and did not push.
