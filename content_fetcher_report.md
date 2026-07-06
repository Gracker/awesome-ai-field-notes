AAIF Content Fetcher Report
Generated: 2026-07-06T04:21+08:00 (Asia/Shanghai)

=== STATISTICS ===
Total Entries: 1109 (preserved; no entries added/removed)
Active Entries: 876
High-Quality Active Entries (quality_score >= 4): 176
High-Quality Active with Content File on Disk: 176
High-Quality Active without Content File: 0
Content Files on Disk: 1272 (root content/ + openclaw/content/)

=== ANALYSIS ===
No new article bodies required fetching this run. All 176 active
entries with quality_score >= 4 already have a canonical
content markdown file on disk. File lookup matches both
`data/entries.json` `id` (`<id>.md`) and the entry's `local_path`
basename against the on-disk content/ directory (root + openclaw/).

Strict candidate set per skill (status=active, qs>=4, missing content):
0 entries. Skill rule: at most 5 per run.

=== CANDIDATES PROCESSED ===
0 entries fetched (no strict candidates).

=== CHANGES THIS RUN ===
- `dist/`: regenerated via `python3 scripts/generate-site.py`
  (635 display cards, 557 content pages, 7 channels).
- `metadata/stats.json`: timestamp refreshed by generate-site
  (2026-07-06 02:02 -> 2026-07-06 04:23).
- `data/entries.json`: untouched by this cron (entry count, list,
  and dict shape unchanged from HEAD; total_entries ==
  len(entries) == 1109).
- No `content/*.md` files written or modified.
- Working tree: 1 file changed (`metadata/stats.json`).

=== VALIDATION ===
✓ entries.json parses as dict with 'entries' list
  (len(entries)=1109 == total_entries=1109)
✓ Entry count stable (1109 vs HEAD); no accidental reductions
✓ Active high-score coverage: 176/176 present on disk
✓ generate-site.py ran successfully (635 cards, 557 pages)
✓ No git push (content-fetcher mode per skill: Do not push)

=== SUMMARY ===
Content fetcher completed successfully with no work to perform. All
canonical content markdown files for active high-quality entries
already exist on disk. The static site was regenerated to refresh
the build timestamp; no entries.json writes or content creates were
required.
