# AAIF Community Review - 2026-10-28

Mode: community-review (weekly maintenance). Pre-run gate: status=ready, count 2925.

## Pre-run worktree state (folded into this commit)

- 11 uncommitted entries (added_date 2026-10-27, author openclaw, q3-q5, all with
  non-empty content pages under canonical content/): 0e3c87a0 13b5d33b 198411f7
  1cca7ecd 1d91af75 4380b131 49a83108 84c9b463 ce5ce5fc dfe1a534 f028d80c.
  Prioritized for commit, not modified.
- 20 untracked content files, all referenced (case-insensitive stem match) by
  active entries and non-empty: the 11 above plus 9 backfills for entries already
  at HEAD (0fe639e3 1758535a 2325af33 5126c05b 61b19ab9 8f5707e9 cafe4eb2 d1a3b4fa
  d7b6b5fc). Committed as-is.

## Scan coverage (read-only first)

- Placeholder titles among ALL active (^[0-9a-fA-F]{6,12}$ or title==id): 1 hit,
  z8jjvpnw (verify-page chrome) - carried, no action per skill rule.
- Same-URL collisions among active via normalized_url_key(): 0 groups.
- www/apex fold (host www-stripped, full-URL key): 0 extra groups. Dedup sweeps hold.
- Same-title active pairs: 11 groups. 10 are legitimate dual-view pairs (different
  sources/perspectives: original vs commentary, repo vs docs, original vs
  translation) with bidirectional related already in place - kept, no action.
  GET probes: c7ae024c, miopc080 (kaggle 404 on HEAD only), 7af26c7f, 0ae5aa88
  are all HEAD-hostile but alive via GET - not stale, no action.
- Suspicious URLs among active (static assets, bare domains, multi-URL, CJK-in-URL):
  24 hits, resolved per-entry below.
- one_liner_author: all 2925 = openclaw (validator-clean).
- Low-quality recent additions since 2026-10-08: 42 active q3 entries, all with
  content and live URLs - normal tail of the score distribution, no action.
- Active entries missing content pages: 108 (standing content-fetcher pool, other mode).

## Actions taken (count 2925 -> 2925, unchanged)

1. ae1c0b14 archived (status+updated_date only): same-canonical twin of d74a7da1 -
   its /en/publication/ URL 302s to d74a7da1's /en/blog/ URL (curl-verified). Kept
   twin active with own content page; related already bidirectional; both q5, no
   score absorb.
2. chromdmcp url repaired: https://developers.chrome.com ->
   https://github.com/ChromeDevTools/chrome-devtools-mcp (own content file grounds
   the repo as source).
3. a70218bc url repaired: https://apertvs.ai/ -> https://www.apertus-ai.org/
   (typo domain; redirect target curl-verified 200, title matches Apertus model).
4. wpe1fck7 url repaired: img.way2solo.com avatar PNG (crawl artifact) ->
   https://www.w2solo.com/topics/6200 (web-search + own content grounding: same
   title, author vulgur, 2025-08-29).

Post-fix asserts: no same-URL active collisions introduced; repaired URLs owned by
exactly one entry each; round-trip reload verified all four edits.

## Carried flags (no action, week 7)

- z8jjvpnw placeholder title (content is verify-page chrome).
- yzi1wbrv / z1jgz9it WeChat cross-title canonical collision (no canonicalize/merge).

## Left as review candidates (not repaired, insufficient grounding)

- antautomd (url=anthropic.com bare; content pins the same bare URL; likely a
  translation of the auto-mode announcement already covered by 15e161b5/18b0dbee,
  but no URL-level evidence in own content).
- cvqqsf6n (huhuhang.com bare; content is a sspai crawl; sspai post URL not found
  by search - do not guess).
- jyt3fx2b (53ai.com bare; exact article path not captured in content).
- m56axpoa (api.openai.com is an API endpoint, no web root; content is a shortcuts
  tutorial, original article URL not grounded).
- p8k8rfur (claude.com bare; content has no original-article URL).
- l5c1k8rv (chatgpt-plus.github.io is genuinely the source; content matches; low
  value but correct - no repair).

## Validation

- entries.json dict shape intact; len(entries)==total_entries==2925.
- scripts/validate-schema.py + scripts/generate-site.py run after fixes (see commit).
- Count invariants: worktree 2925 >= HEAD 2914 = origin/main 2914 pre-push.
