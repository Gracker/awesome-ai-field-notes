# Community Review 2026-11-25

Mode: community-review (aaif-intake-pipeline). Baseline: 3500 entries (worktree = HEAD = origin/main), 2802 active. Pre-run dirty state: metadata/stats.json churn only.

## Scans (all active entries)

- Placeholder titles (`^[0-9a-fA-F]{6,12}$` or title==id): 0
- Same-URL active pairs (www/apex folded, full path+query preserved): 0
- Same-title active groups: 12 — all fully bidirectionally linked pairs with distinct source URLs/perspectives; kept per distinct-source rule, no merges
- Related-edge audit (direction + missing-target check): 0 one-way links, 0 missing targets
- local_path audit: 0 fixable; 126 carry (own future `content/{id}.md` targets + carried 2026-06 vault-era set, per 2026-11-04 rule)
- Entries added since 2026-11-18 review: 116; 0 bad `one_liner_author`, 0 over-900 summaries, 0 low-quality actives, 0 malformed/junk URLs, 0 missing content files for q>=4
- Recent active entries missing `summary_en`: 3 → all backfilled below (grounded by own summary_zh + non-empty content files)

## Fixed

- `summary_en` backfills grounded in each entry's own summary_zh/content file (no source fabrication), measured 695 / 831 / 746 chars (all under the 900 cap), count 3500 unchanged, round-trip reload verified:
  - a11a6232 (Jake Wharton Kotlin 2026 JetBrains interview, Juejin translation)
  - 0cd766e6 (Gracker local agent-practice note: skill admission validation via GRASP / Assay / SkillAxe / Skill-V)
  - d6312fa3 (@mylifcc Fable 5.2 as Claude Code advisor, weekly-limit measurement)

## Flagged for review (no changes)

- Carried from prior reviews: WeChat cross-title canonical collision (yzi1wbrv / z1jgz9it), verify-page chrome (z8jjvpnw), 16 June-2026 legacy broken local_path pointers, 141 active no-summary June-2026 crawl-era entries — all unchanged from 2026-11-18.
- The 12 same-title groups stay as distinct-source pairs (simonwillison commentary vs original source, X post vs blog announcement, GitHub repo vs docs site, WeChat vs baoyu translation, etc.) — all fully linked via `related`.

## Validation

- `scripts/validate-schema.py`: exit 0 (legacy summary_zh warnings only, pre-existing)
- `scripts/generate-site.py`: OK, 2724 display cards / 2602 content pages (flat vs pre-run — metadata-only change, expected)
- Count: worktree = HEAD = origin/main = 3500 after push

## Changed files

- data/entries.json (3 summary_en backfills)
- metadata/stats.json, README.md, openclaw/README.md (regen)
- openclaw/logs/community-review-2026-11-25.md (this report)
