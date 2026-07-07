AAIF Content Fetcher Report
Generated: 2026-07-07T04:20+08:00 (Asia/Shanghai)

=== STATISTICS ===
Total Entries: 1116 (preserved; no entries added/removed)
Active Entries: 881
High-Quality Active Entries (quality_score >= 4): 178
High-Quality Active with Content File on Disk: 178
High-Quality Active without Content File: 0
Content Files on Disk: 1275 (root content/)

=== ANALYSIS ===
No new article bodies required fetching this run. All 178 active
entries with quality_score >= 4 already have a canonical
content markdown file on disk (`content/{id}.md` lookup per
skill rule).

Strict candidate set per skill (status=active, qs>=4, missing
content/{id}.md): 0 entries. Skill rule: at most 5 per run.

Note: 4 entries (`ai-code-gen-benchmark-2026-06-09`, `adbd50c1`,
`ccconn_001`, `androi_001`) have a `local_path` that points to a
non-default location (Cubox/..., 每日论文精读（AI）/...,
content/discovery/...), but each one already has a canonical
content/{id}.md on disk, so they are not strict candidates.

=== CANDIDATES PROCESSED ===
0 entries fetched (no strict candidates).

=== CHANGES THIS RUN ===
- `dist/`: regenerated via `python3 scripts/generate-site.py`
  (640 display cards, 562 content pages, 7 channels).
- `metadata/stats.json`: timestamp refreshed by generate-site
  (2026-07-06 23:41 -> 2026-07-07 04:20).
- `data/entries.json`: untouched by this cron (entry count, list,
  and dict shape unchanged from HEAD; total_entries ==
  len(entries) == 1116).
- No `content/*.md` files written or modified by this cron.
- Working tree: 1 file changed (`metadata/stats.json`).

=== VALIDATION ===
✓ entries.json parses as dict with 'entries' list
  (len(entries)=1116 == total_entries=1116)
✓ Entry count stable (1116 vs HEAD 1116); no accidental reductions
✓ Active high-score coverage: 178/178 present on disk
✓ generate-site.py ran successfully (640 cards, 562 pages)
✓ No git push (content-fetcher mode per skill: Do not push)

=== SUMMARY ===
Content fetcher completed successfully with no work to perform. All
canonical content markdown files for active high-quality entries
already exist on disk. The static site was regenerated to refresh
the build timestamp; no entries.json writes or content creates were
required.
