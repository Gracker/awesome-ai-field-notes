AAIF Content Fetcher Report
Generated: 2026-07-04T04:20:55+08:00 (Asia/Shanghai)

=== STATISTICS ===
Total Entries: 1457 (was preserved; no entries added/removed)
Active Entries: 1195
High-Quality Active Entries (score >= 4): 179
High-Quality Active with Content File on Disk: 179
High-Quality Active without Content File: 0
Content Files on Disk: 1255

=== ANALYSIS ===
No new article bodies required fetching this run. All 179
active entries with quality_score >= 4 already have a content markdown file
on disk (matched case-insensitively against `data/entries.json` `id`/stem).
The single historical name mismatch — Andrew Ng tweet at
`content/AndrewYNg_20260611180217_002.md` — is present and accounted for.

=== CANDIDATES PROCESSED ===
0 entries fetched (no strict candidates). Skill rule: at most 5 per run.

=== CHANGES THIS RUN ===
- `dist/`: regenerated via `python3 scripts/generate-site.py`
  (639 display cards, 550 content pages, 7 channels — identical output to HEAD).
- `metadata/stats.json`: refreshed timestamp.
- `data/entries.json`: untouched by this cron (entry count, list, and dict
  shape unchanged from HEAD).
- No `content/*.md` files written or modified.

=== VALIDATION ===
✓ entries.json parses as dict with 'entries' list (len(entries)=1457 == total_entries=1457)
✓ Entry count stable (1457 vs HEAD); no accidental reductions
✓ Active high-score coverage: 179/179 present on disk
✓ generate-site.py ran successfully (no diff against HEAD in dist/)
✓ No git push (content-fetcher mode per skill: Do not push)

=== SUMMARY ===
Content fetcher completed successfully with no work to perform. All canonical
content markdown files for active high-quality entries already exist. The
static site was regenerated to refresh `lastmod` metadata; no entries.json
writes or content creates were required.
