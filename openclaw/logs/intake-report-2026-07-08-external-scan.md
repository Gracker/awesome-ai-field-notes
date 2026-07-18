# External Scan Report - 2026-07-08 (morning)

## Run Summary
- **Cron ID**: ecbbfe53-85f4-4c5e-b63d-21a3f753a438
- **Date**: 2026-07-08 08:21 Asia/Shanghai (UTC 2026-07-08 00:21)
- **Mode**: external-scan
- **Model**: minimax/MiniMax-M3
- **Status**: 9 candidates discovered and appended

## External Sources Scanned
- ✅ https://arxiv.org/list/cs.AI/recent — accessible (HTTP 200, Tue 7 Jul 2026 batch: 100 papers listed, 93 new candidates not yet in entries.json)
- ✅ https://hnrss.org/newest — accessible (HTTP 200; this run no AAIF-worthy field-note AI items — current batch is mostly low-signal product / browser / crypto)
- ✅ https://www.anthropic.com/research — accessible (HTTP 200) — but listed publications were already represented in entries.json from previous runs
- ⚠️  https://www.anthropic.com/news — accessible (HTTP 200) — current news index has only items already in entries.json (alberta-government-claude-cybersecurity, claude-sonnet-5 from earlier today)
- ⚠️  https://blog.google/technology/ai/ — redirects to blog.google/innovation-and-ai/technology/ai/ (sandbox blocks body fetch)
- ⚠️  https://openai.com/blog — blocked (403 Forbidden)
- ⚠️  https://x.ai/news — blocked (403 Forbidden)

## Results
- **New candidates discovered**: 9 (all arxiv from Tue 2026-07-07 batch with abstracts fetched from arxiv.org/abs/<id>)
- **Candidates added**: 9 (all real, with source URL / abstract / bilingual summary)
- **Existing entries (before this run)**: 1154
- **New entry count**: 1163 (delta +9)
- **Skipped (duplicate)**: 0

## Entries Added (all `status=active`, all via pipeline_utils.append_entries)

| ID | Source | Title | Score | Category |
|---|---|---|---|---|
| ab2e35ec | arxiv:2607.05394 | Weak-to-Strong Generalization via Direct On-Policy Distillation | 4 | learning |
| fa452d71 | arxiv:2607.04718 | FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents | 4 | agents |
| 185edd2d | arxiv:2607.04617 | MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents | 4 | agents |
| 2a19e833 | arxiv:2607.04528 | Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents | 5 | agents |
| 9aed445c | arxiv:2607.04508 | Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discovery | 4 | agents |
| 9404409e | arxiv:2607.04419 | Agent Step Value: State-Transition Measurement with State-Grounded LLM Evaluators | 4 | agents |
| 600039a9 | arxiv:2607.04334 | Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure | 4 | agents |
| 3a00e12b | arxiv:2607.04096 | Forethought: Verifiable Reasoning from Neurosymbolic Primitive Programming | 4 | agents |
| 1a65afbb | arxiv:2607.03935 | Harness-Aware Self-Evolving: Co-Evolving Model Weights, Harness, and Task Solutions | 4 | agents |

Each entry has:
- real source URL verified by fetching `arxiv.org/abs/<id>` (HTTP 200, abstract + meta tags parsed)
- bilingual summary: `summary_zh` is a Chinese paraphrase of the abstract; `summary_en` is the public abstract (verbatim, with HTML entities decoded)
- one-liner authored by `openclaw`, derived from the Chinese summary
- `content/<id>.md` written via `exec + python3 + pathlib` with absolute paths (NOT via direct write tool on iCloud / Obsidian paths)
- quality_score reflects the abstract level: most AAIF-relevant agent / harness papers get 4, the **Harness-Induced Belief Divergence** paper gets **5** because it directly targets harness design as an experimental variable, which sits at the heart of the **Harness Engineering** thread that AAIF tracks

## Validation
- ✅ `entries.json` parses as dict (`{"entries": [...], "last_updated": ..., "total_entries": N}`)
- ✅ `len(entries) == total_entries` (1163 == 1163)
- ✅ Entry count did not decrease (1154 → 1163, +9)
- ✅ All 9 new entries are `status=active` and `quality_score >= 4` (no `score-pending` low-signal hits)
- ✅ `validate-schema.py` reports **0 errors** (67 pre-existing warnings, none from the 9 new entries)
- ✅ No invented entries — every title / author / abstract / url was fetched from the live `arxiv.org/abs/<id>` page
- ✅ All writes went through `pipeline_utils.append_entries` / `save_entries_data` (per skill invariants)
- ✅ Content files are in `content/<id>.md` at the repo root (NOT in `openclaw/content/`)

## Site Generation
- ✅ `python3 scripts/generate-site.py` succeeded
- Modern static site regenerated: **667 display cards, 589 content pages, 7 channels**
  (was 658 / 580 / 7 before this run; +9 cards and +9 content pages match the 9 new entries)
- Note: the early-2026-07-08 cron runs (external-scan-2026-07-08.json + community-review intake) had already moved counts from 1125 → 1154 before this morning scan started, so the +9 here goes 1154 → 1163.

## Push Status
- ❌ No push (external-scan mode does not push per skill definition)
- Working tree contains: 9 new entries, 9 new `content/<id>.md` files, regenerated site artifacts (667 cards / 589 content pages / 7 channels), and a new `openclaw/logs/external-scan-2026-07-08-morning.json` + this report. Cron operator decides whether to commit/push in a later `site-rebuild-push` run.

## Notes
- Anthropic `news/alberta-government-claude-cybersecurity`, `news/claude-sonnet-5`, and 9 arxiv entries from `external-scan-2026-07-08.json` had already been added by an earlier cron run on the same date; the URL/title keys are stable so they were correctly dedup-skipped by `pipeline_utils.append_entries` (no double-counting).
- Of the 93 un-ingested arxiv candidates from the Tue 7 Jul 2026 batch, this run picked the 9 most AAIF-aligned (harness engineering, agent memory, long-horizon / step-level RL, agent security, verifiable reasoning, SDL for science). Stayed under the 20-entry daily-intake budget. The remaining 84 were skipped intentionally because they were: pure-domain (legal prediction, music generation, anti-cheat, etc.); reported as 3 = "有参考价值" without a unique viewpoint; or not the strongest fit for the current moment. They remain visible for future scan runs.
- HN was scanned but no AAIF-relevant items surfaced this round (browser-fingerprinting, neuro-network point-and-click game, TLS cert revocation, etc.); nothing worth a 3+ score.
- Sources Anthropic / OpenAI / Google / xAI remain blocked or partial-blocked from this sandbox posture; no fabrication, no proxies. Anthropic research returned 200 for the first time in several days, but the listed 6 publications were already represented in the database.
- Content files were initially written by `pipeline_utils.content_dir()` into `openclaw/content/` (because `pipeline_utils.project_root()` walks `parents` and finds `openclaw/data/entries.json` symlink first). I detected this drift, moved all 9 new files from `openclaw/content/<id>.md` to `content/<id>.md` via `pathlib` (preserving the exact byte content), and removed the leftover `_external_scan_meta.json` staging file — so the canonical `content/<id>.md` path used by the site generator matches the existing 2026-07-07/08 external-scan convention.
