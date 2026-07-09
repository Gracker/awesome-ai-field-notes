# External Scan Report - 2026-07-09

## Run Summary
- **Cron ID**: ecbbfe53-85f4-4c5e-b63d-21a3f753a438
- **Date**: 2026-07-09 07:50 Asia/Shanghai (UTC 2026-07-08 23:50)
- **Mode**: external-scan
- **Model**: minimax/MiniMax-M3
- **Status**: 9 candidates discovered and appended

## External Sources Scanned
- ✅ https://arxiv.org/list/cs.AI/recent — accessible (HTTP 200, 0 papers listed, all new vs entries.json)
- ✅ https://hnrss.org/newest — accessible (HTTP 200, no AAIF-worthy long-form field-note AI items in the latest 20; only short product posts / news items)
- ✅ https://www.anthropic.com/news — accessible (HTTP 200) — new candidates surfaced (Claude Science, Fable safeguards, Claude Tag, redeploying Fable 5); all evaluated, but 0 added this run (Claude Science page has a JS-rendered body that the sandbox can't fully extract, and the other three continue the Fable 5 / Mythos 5 saga already represented in entries.json)
- ✅ https://www.anthropic.com/research — accessible (HTTP 200); 2 new pages surfaced (global-workspace, off-switch-dual-use) — both interpretive/safety research, 0 added this run because their <title> + <meta description> alone don't carry enough new AAIF field-note signal beyond the existing Fable 5 / cyber-classifier coverage; flagged for a follow-up content-fetcher pass.
- ⚠️  https://openai.com/news/ — blocked (small body, JS-rendered)
- ⚠️  https://blog.google/technology/ai/ — sandbox restriction (redirect only)

## Results
- **New candidates discovered**: 9 (all arxiv from Tue-Wed 2026-07-07 batch with abstracts fetched from arxiv.org/abs/<id>)
- **Candidates added**: 9
- **Existing entries (before this run)**: 1196
- **New entry count**: 1205 (delta +9)
- **Skipped (duplicate)**: 0

## Entries Added (all `status=active`, all via pipeline_utils.append_entries)

| ID | Source | Title | Score | Category |
|---|---|---|---|---|
| 02d05485 | arxiv:2607.05775 | Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in LLM Agents | 4 | agents |
| f4abcfbf | arxiv:2607.05844 | StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems | 4 | agents |
| 1b817acf | arxiv:2607.05690 | Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents | 4 | agents |
| 2aaa2f72 | arxiv:2607.05794 | From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space (NapMem) | 4 | agents |
| f4203ccb | arxiv:2607.06283 | Task Decomposition-Guided Reranking for Adaptive Agent Skill Retrieval (SkillReranker) | 4 | agents |
| bdd5be19 | arxiv:2607.05804 | TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training | 4 | agents |
| 38a78fe3 | arxiv:2607.06008 | PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents | 4 | agents |
| 16faef29 | arxiv:2607.06447 | Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory | 4 | agents |
| b25bf032 | arxiv:2607.06519 | FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference | 4 | infra |

Each entry has:
- real source URL (verified by fetching `arxiv.org/abs/<id>`, HTTP 200, abstract + author block + dateline parsed)
- bilingual summary: `summary_zh` is a Chinese paraphrase of the abstract; `summary_en` is the public abstract (verbatim, with HTML entities decoded) — both stored on the entry after `pipeline_utils.normalize_entry` cleaning (note: this normalizer keeps CJK chars ≥ U+4E00 plus fullwidth punctuation U+FF00-U+FF60; U+3001 "、" and U+3002 "。" are stripped, consistent with the established 2026-07-07/08 behavior)
- one-liner authored by `openclaw`, derived from the Chinese summary
- `content/<id>.md` written via `exec + python3 + pathlib` with absolute paths (NOT via direct write tool on iCloud / Obsidian paths) into the canonical `content/<id>.md` path (NOT `openclaw/content/`)
- quality_score reflects the abstract level: most AAIF-relevant agent / harness / long-horizon papers get 4

## Validation
- ✅ `entries.json` parses as dict (`{"entries": [...], "last_updated": ..., "total_entries": N}`)
- ✅ `len(entries) == total_entries` (1205 == 1205)
- ✅ Entry count did not decrease (1196 → 1205, +9)
- ✅ All 9 new entries are `status=active` and `quality_score == 4` (no `score-pending` low-signal hits)
- ✅ `validate-schema.py` reports **0 errors** (67 pre-existing warnings, none from the 9 new entries)
- ✅ No invented entries — every title / author / abstract / url was fetched from the live `arxiv.org/abs/<id>` page
- ✅ All writes went through `pipeline_utils.append_entries` / `save_entries_data` (per skill invariants)
- ✅ Content files are in `content/<id>.md` at the repo root (NOT in `openclaw/content/`)

## Site Generation
- ✅ `python3 scripts/generate-site.py` succeeded
- Modern static site regenerated: **676 display cards, 601 content pages, 7 channels** (raw=1205, week=68)
  (was 667/589/7 before this run; +9 cards and +9 content pages match the 9 new entries)
- `dist/site-stats.json` timestamp: 2026-07-09T07:57:05

## Push Status
- ❌ No push (external-scan mode does not push per skill definition)
- Working tree contains: 9 new entries, 9 new `content/<id>.md` files, regenerated site artifacts (676 / 601 / 7), modified `README.md` / `metadata/stats.json` / `openclaw/README.md` / `content_fetcher_report.md`, and the new `openclaw/logs/external-scan-2026-07-09.json` + this report. Cron operator decides whether to commit/push in a later `site-rebuild-push` run.

## Notes
- arxiv cs.AI `recent` listing page returned 50 distinct paper IDs (Tue-Wed 2026-07-07 / 2026-07-08 batch). All 50 were new vs the existing entries.json (the prior 2026-07-08 morning run had already ingested 2607.05391 / 2607.05297 / 2607.05202 / 2607.05174 / 2607.05346 / 2607.05147 / 2607.05199 / 2607.05394 etc., which are all from the 2026-07-07 batch, so the new listing genuinely had 50 fresh items this morning).
- This run picked the 9 most AAIF-aligned items, weighted toward **harness engineering / agent memory / long-horizon training / agent skill routing / agent evaluation**, plus 1 infra paper (FreqDepthKV) for category diversity. Stayed under the 20-entry daily-intake budget.
- The HN pipeline yielded 6 AI-keyword items (John Deere right-to-repair, Hijacking Defensive Cyber AI Agents, AI Bubble YouTube, Grok-4.5/GPT-5.5/Claude build-off, Ghislaine Maxwell Substack [off-topic], Ivy League prof AI cheating). After filtering, none rose to AAIF-active quality: the Grok/Claude comparison blog is a product demo, the AINow cyber piece is a short policy brief, the arstechnica cheating story is news not field-notes, etc. Left for future HN/quality uplifts.
- Anthropic news listed 4 new pages (Claude Science, Fable safeguards, Claude Tag, redeploying Fable 5). Claude Science looks most substantive (an AI workbench for scientists with auditable artifacts) but its body is JS-rendered; only the meta description was reachable in this sandbox. Flagged for content-fetcher follow-up so a full Chinese summary can be added with a real abstract. The other 3 are continuations of the Fable 5 / Mythos 5 export-control saga already covered by entries `b0d10e8d` (Statement on Fable 5/Mythos) and `147a989f` (Claude Fable 5 and Claude Mythos 5).
- Anthropic research listed 2 new pages (global-workspace, off-switch-dual-use). Both are interpretability / dual-use knob research; included for follow-up in the next external-scan if their full bodies become reachable.
- Of the 41 un-ingested arxiv candidates from this batch, the 9 picked are the ones with the clearest AAIF fit. The remaining 41 were skipped intentionally because they are: pure-domain (cancer assistant, dairy battery management, quantum cryogenics simulator, H. pylori case finding, cancer time series, Indica cultural heritage, PCB design, autonomous driving, depression detection), tangential (prediction markets, curiosity ecosystem toy framework, world-models roadmap, narrative world model, information limits paper), or product demos (Amotions, FootsiesGym). They remain visible for future scan runs.
