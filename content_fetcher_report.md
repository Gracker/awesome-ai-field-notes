AAIF Content Fetcher Report
Generated: 2026-07-05T20:20:12+08:00 (Asia/Shanghai)

=== STATISTICS ===
Total Entries: 1469 (preserved; no entries added/removed)
Active Entries: 1207
High-Quality Active Entries (quality_score >= 4): 181
High-Quality Active with Content File on Disk: 181
High-Quality Active without Content File: 0
Content Files on Disk: 1262

=== ANALYSIS ===
No new article bodies required fetching this run. All 181
active entries with quality_score >= 4 already have a canonical
content markdown file on disk. File lookup matches both
`data/entries.json` `id` (`<id>.md`) and the entry's `local_path`
basename against the on-disk `content/` directory.

=== CANDIDATES PROCESSED ===
0 entries fetched (no strict candidates). Skill rule: at most 5 per run.

=== CHANGES THIS RUN ===
- `dist/`: regenerated via `python3 scripts/generate-site.py`
  (1262 content pages, identical to HEAD).
- `metadata/stats.json`: timestamp refreshed by generate-site.
- `data/entries.json`: untouched by this cron (entry count, list,
  and dict shape unchanged from HEAD; total_entries ==
  len(entries) == 1469).
- No `content/*.md` files written or modified.
- Working tree contains only the `metadata/stats.json` and
  `content_fetcher_report.md` refresh.

=== VALIDATION ===
✓ entries.json parses as dict with 'entries' list
  (len(entries)=1469 == total_entries=1469)
✓ Entry count stable (1469 vs HEAD); no accidental reductions
✓ Active high-score coverage: 181/181 present on disk
✓ generate-site.py ran successfully (dist/ unchanged vs HEAD)
✓ No git push (content-fetcher mode per skill: Do not push)

=== SUMMARY ===
Content fetcher completed successfully with no work to perform. All
canonical content markdown files for active high-quality entries
already exist on disk. The static site was regenerated to refresh
the build timestamp; no entries.json writes or content creates were
required.
