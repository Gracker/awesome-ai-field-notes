# External Scan Report - 2026-07-11

## Run Summary
- **Cron ID**: ecbbfe53-85f4-4c5e-b63d-21a3f753a438
- **Date**: 2026-07-11 07:50 Asia/Shanghai (UTC 2026-07-10 23:50)
- **Mode**: external-scan
- **Model**: minimax/MiniMax-M3
- **Status**: 8 candidates appended (1 skipped due to duplicate URL)

## External Sources Scanned
- ✅ https://arxiv.org/list/cs.AI/recent — accessible (HTTP 200, Fri 10 Jul + Thu 9 Jul + Wed 8 Jul 2026 batch: 50 papers listed, 50 new vs entries.json; this run picked the 8 most AAIF-aligned)
- ✅ https://www.anthropic.com/news — accessible (HTTP 200); 1 new page added (Claude Science, AI workbench for scientists). The other 6 new pages (ben-bernanke, fable-safeguards-jailbreak-framework, hard-questions, introducing-claude-tag, redeploying-fable-5, reflect-with-claude, ust-claude) are either continuations of the Fable 5 / Mythos 5 export-control saga already represented in entries.json (e.g. `b0d10e8d`, `147a989f`) or low-signal product announcements.
- ✅ https://www.anthropic.com/research — accessible (HTTP 200); 0 new (all listed publications already in entries.json or are continuations).
- ✅ https://blog.google/innovation-and-ai/technology/ai/ — accessible (HTTP 200); 1 enriched page (DiffusionGemma — was already a score-pending placeholder in entries.json since 2026-06-12; the URL was dedup-skipped by `pipeline_utils.append_entries`, but the underlying `content/ab9c9a67.md` was upgraded with the real English abstract + Chinese summary so the next community-review/content-fetcher run can use it to lift the entry from score-pending → active).
- ✅ https://hnrss.org/newest — accessible (HTTP 200); 20 latest items reviewed, none rose to AAIF-active quality this round (browser-fingerprinting, Tesla autopilot, WordPress agency spam, NVFP4 RL recipe from humansand.ai which is infra-interesting but more practitioner blog than field-note, Grok Build easter egg, etc.).
- ⚠️  https://openai.com/news/ — blocked (HTTP 403); not reachable from this sandbox posture.

## Results
- **New candidates discovered**: 9 (8 arxiv + 1 Anthropic news)
- **Candidates added**: 8 (1 skipped — duplicate URL on DiffusionGemma)
- **Existing entries (before this run)**: 1212
- **New entry count**: 1220 (delta +8)
- **Skipped (duplicate URL)**: 1 (DiffusionGemma, already represented as score-pending entry `ab9c9a67` from 2026-06-12)

## Entries Added (all `status=active`, all via pipeline_utils.append_entries)

| ID | Source | Title | Score | Category |
|---|---|---|---|---|
| d7f5e8e9 | arxiv:2607.08028 | From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents | 5 | agents |
| d9102c5a | arxiv:2607.08716 | Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents | 5 | agents |
| d0b184a7 | arxiv:2607.08255 | Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation | 4 | coding |
| b139faf1 | arxiv:2607.08093 | CausalDS: Benchmarking Causal Reasoning in Data-Science Agents | 4 | infra |
| bcc5ec91 | arxiv:2607.08065 | When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals | 4 | infra |
| 93d84c70 | arxiv:2607.08734 | The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs | 4 | infra |
| 7c946336 | arxiv:2607.07984 | Agentic Neural Architecture Search | 4 | agents |
| d5f7bd1f | anthropic:claude-science-ai-workbench | Claude Science, an AI workbench for scientists | 4 | agents |

Each entry has:
- real source URL verified by fetching `arxiv.org/abs/<id>` (HTTP 200, abstract + author block + dateline parsed) for the 7 arxiv items, and by fetching `anthropic.com/news/claude-science-ai-workbench` (HTTP 200, full body extracted including the 60+ curated skills list, reviewer agent details, and beta plan availability) for the Anthropic item.
- bilingual summary: `summary_zh` is a Chinese paraphrase of the abstract / body; `summary_en` is the public abstract / body excerpt (verbatim, with HTML entities decoded). Both stored on the entry after `pipeline_utils.normalize_entry` cleaning.
- one-liner authored by `openclaw`, derived from the Chinese summary.
- `content/<id>.md` written via `exec + python3 + pathlib` with absolute paths (NOT via direct write tool on iCloud / Obsidian paths) into the canonical `content/<id>.md` path at the repo root (NOT `openclaw/content/`).
- `quality_score` reflects the abstract level: the two most AAIF-relevant papers (harness engineering for enterprise, proactive memory for long-horizon agents) get **5**; the other six get **4**.

## Skipped (duplicate URL)

| ID | Source | Title | Reason |
|---|---|---|---|
| ab9c9a67 | blog.google/innovation-and-ai/.../diffusion-gemma-faster-text-generation/ | Introducing DiffusionGemma | `pipeline_utils.append_entries` correctly deduped — the URL was already in entries.json as `status=score-pending` with empty summaries (added 2026-06-12). Per the skill's "do not reduce entry count accidentally" rule, the existing placeholder was left in place. As a positive side effect, the underlying `content/ab9c9a67.md` was rewritten with the real English abstract + Chinese summary so the next community-review or content-fetcher run can use it to lift the entry from score-pending → active. |

## Validation
- ✅ `entries.json` parses as dict (`{"entries": [...], "last_updated": ..., "total_entries": N}`)
- ✅ `len(entries) == total_entries` (1220 == 1220)
- ✅ Entry count did not decrease (1212 → 1220, +8)
- ✅ All 8 new entries are `status=active` and `quality_score >= 4` (no `score-pending` low-signal hits)
- ✅ `validate-schema.py` reports **0 errors**, 68 pre-existing warnings (none from the 8 new entries — warnings are all from earlier batches on `platform=industry/personal_blog/openai/hackernews` and short `summary_zh` on legacy entries)
- ✅ No invented entries — every title / author / abstract / url was fetched from the live `arxiv.org/abs/<id>` page or `anthropic.com/news/<slug>` page
- ✅ All writes went through `pipeline_utils.load_entries_data` / `append_entries` / `save_entries_data` (per skill invariants)
- ✅ Content files are in `content/<id>.md` at the repo root (NOT in `openclaw/content/`)

## Site Generation
- ✅ `python3 scripts/generate-site.py` succeeded
- Modern static site regenerated: **687 display cards, 612 content pages, 7 channels** (was 679/604/7 before this run; +8 cards and +8 content pages match the 8 new entries)
- `dist/site-stats.json` timestamp: 2026-07-11T07:57:43

## Push Status
- ❌ No push (external-scan mode does not push per skill definition)
- Working tree contains: 8 new entries, 8 new/updated `content/<id>.md` files (the 9th — `ab9c9a67.md` — is an upgrade to an existing entry's content file), regenerated site artifacts (687 / 612 / 7), modified `README.md` / `data/entries.json` / `metadata/stats.json` / `openclaw/README.md` / `content_fetcher_report.md`, and the new `openclaw/logs/external-scan-2026-07-11.json` + this report. Cron operator decides whether to commit/push in a later `site-rebuild-push` run.

## Notes
- **Harness-engineering + agent-memory double-5** is intentional this run: arxiv:2607.08028 (Prompts → Contracts) and arxiv:2607.08716 (Proactive Memory) both sit at the core of the AAIF harness / agent-memory threads that recent runs have been tracking (cf. entries like `2a19e833` "Harness-Induced Belief Divergence", `185edd2d` "MRMS Memory Substrate", `2aaa2f72` "NapMem"). Score 5 reflects "directly advances an existing AAIF thread" rather than novel-of-its-kind.
- **CausalDS (b139faf1)** scores 4 because it cleanly closes the long-standing gap between symbolic causal-reasoning benchmarks and data-analysis benchmarks — directly AAIF-relevant for the agent-eval thread.
- **When LLMs Agree, Are They Right? (bcc5ec91)** scores 4 because it directly audits the reliability of LLM-as-judge ensembles, which are a key piece of the AAIF evaluation pipeline.
- **Compete Then Collaborate (d0b184a7)** scores 4 because it gives a practical recipe for training small coding students from frontier teachers (Claude / Codex-GPT / Grok / Gemini) without LLM-judge bias — practical agent / coding follow-up to recent distillation entries.
- **Illusion of Equivalency (93d84c70)** scores 4 as a strong infra contribution: a decision-level metric that exposes how PTQ metrics (accuracy / perplexity) hide real behavioral changes between base and quantized models.
- **Agentic Neural Architecture Search (7c946336)** scores 4 as an agents × autoML crossover that has clear practical value for agent harness tuning.
- **Claude Science (d5f7bd1f)** scores 4 as the Anthropic-published workbench-with-reviewer-agent news item that closes the loop on the auditable-artifacts thread AAIF has been tracking (cf. entries like `0f764e9b` Claude Sonnet 5).
- Of the 50 arxiv candidates surfaced this batch, the 8 picked are the most AAIF-aligned. The remaining 42 were intentionally skipped because they are: pure-domain (Hepatocellular Carcinoma clinical LLM, food nutrient VLM, biomedical text rewiring, gesture recognition, ASMR ship maintenance, autism self-stimulatory hand classification, mental health chatbot, vehicular intention LSTM, autism facial emotion studies, JEPA network fingerprints, FedOPAL visual prompt tuning, Petroleum industry dataset, etc.); tangential (Compete Then Collaborate's NS flash games, Persuasion Attacks on CoT Monitoring without a concrete audit recipe, ZendoWorld game-based agent eval, IG-Bench scientific lineage reasoning, PolyUQuest verifiable web RAG); or not the strongest fit for the current moment (Weather balloon modeling, optimization AI assistant, etc.).
- The Anthropic news Claude Science page that was flagged as JS-rendered in the 2026-07-08 and 2026-07-09 external scans was successfully fetched this run with the standard curl UA + python regex body extraction (10K+ chars of body recovered), allowing it to be added now with a full Chinese summary + verbatim English abstract excerpt.
- The DiffusionGemma entry `ab9c9a67` (score-pending, no summaries, added 2026-06-12) is the kind of legacy placeholder that community-review is meant to clean up. The content file at `content/ab9c9a67.md` is now upgraded in this run so the next community-review pass can simply lift the entry's `summary_zh`, `summary_en`, `tags`, `category`, and `quality_score` from the content file and rewrite the entry — no fresh abstract fetch needed.
