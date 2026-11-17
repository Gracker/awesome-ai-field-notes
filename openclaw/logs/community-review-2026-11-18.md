# Community Review 2026-11-18

Mode: community-review (aaif-intake-pipeline). Baseline: 3361 entries (worktree = HEAD = origin/main), 2663 active. Pre-run dirty state: README/stats.json/openclaw-README regen + 8 untracked content files (preserved, see below).

## Scans (all active entries)

- Placeholder titles (`^[0-9a-fA-F]{6,12}$` or title==id): 0
- Same-URL active pairs (www/apex folded, full path+query preserved): 0
- Same-title active groups: 10 - all the known healthy bidirectionally-linked pairs (matches 2026-11-11 review / 2026-11-16 dedup)
- Related-edge audit (active side, incl. missing-target check): 2 one-way links found -> both repaired; 0 missing targets
- local_path audit: 125 flagged pointers, none repairable this run: majority point at the entry's own future `content/{id}.md` (correct content-fetcher target, not yet fetched); remainder is the carried 2026-06 vault-era set (no own content file, no grounding per 2026-11-04 rule)
- Entries added since 2026-11-11 review: 140; 0 placeholder titles, 0 bad authors, 0 bad scores, 1 missing summary_en (repaired below)
- Pre-run untracked `content/*.md` x8 (1c7b50d3 2b05f373 3f6c8be7 4c496f27 661c8f9b e4173937 ead89649 f2b25f29): all referenced by `data/entries.json` at HEAD, non-empty (4.1-5.2 KB) - preserved and committed with this run

## Fixed

- One-way `related` links made bidirectional: archived 5c0a9ebf (alibaba/OpenSandbox x_post) now links back to active 3bb5b3b2 (OpenSandbox GitHub entry); archived 212008af (Scaling Managed Agents x_post) now links back to active b80aa957 (Claude Code Projects entry).
- b2b95a0d (manateelazycat Antigravity CLI X post, added 2026-11-16): summary_en backfilled (662 chars, under the 900 cap) from its own grounded summary_zh + local content-file walkthrough; no source fabrication.
- Count unchanged: 3361 before/after; total_entries synced by save_entries_data(); pair symmetry verified on round-trip reload.

## Flagged for review (no changes made)

- Carried from 2026-11-11: 16 June-2026 legacy broken local_path pointers (no grounding), bare-homepage URLs kept as legit project/site subjects, 141 active no-summary June-2026 crawl-era entries.

## Validation

- `scripts/validate-schema.py`: exit 0 (legacy summary_zh warnings only, pre-existing)
- `scripts/generate-site.py`: OK, 2585 display cards / 2464 content pages (flat vs pre-run - metadata-only change, expected)
- Count: worktree = HEAD = origin/main = 3361 after push

## Changed files

- data/entries.json (2 related back-links, 1 summary_en)
- content/{1c7b50d3,2b05f373,3f6c8be7,4c496f27,661c8f9b,e4173937,ead89649,f2b25f29}.md (8 pre-run referenced content files, committed)
- metadata/stats.json, README.md, openclaw/README.md (regen)
- openclaw/logs/community-review-2026-11-18.md (this report)
