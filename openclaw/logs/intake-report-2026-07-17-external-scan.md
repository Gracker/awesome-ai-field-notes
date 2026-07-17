# External Scan Report - 2026-07-17

## Run Summary
- **Cron ID**: ecbbfe53-85f4-4c5e-b63d-21a3f753a438
- **Date**: 2026-07-17 07:50 Asia/Shanghai (UTC 2026-07-16 23:50)
- **Mode**: external-scan
- **Model**: minimax/MiniMax-M3
- **Status**: 10 candidates appended (0 skipped)

## External Sources Scanned
- ✅ https://arxiv.org/list/cs.AI/recent — accessible (HTTP 200, 50 papers listed; 2026-07-15/16/17 batch; all 50 new vs entries.json; 10 picked)
- ✅ https://www.anthropic.com/news — accessible (HTTP 200); 6 new pages (ben-bernanke, claude-for-teachers, fable-safeguards-jailbreak-framework, hard-questions, redeploying-fable-5, reflect-with-claude, ust-claude), all continuations of the Fable 5 / Mythos saga, case studies, or low-density announcements → 0 added this run
- ✅ https://www.anthropic.com/research — accessible (HTTP 200); 4 new pages (claude-plays-robotics, global-workspace, off-switch-dual-use, claude-values-models-languages), all niche (robotics eval, interpretability, alignment, societal-impacts) → 0 added this run; flagged for follow-up content-fetcher
- ✅ https://blog.google/innovation-and-ai/technology/ai/ — accessible (HTTP 200); 2 actually-new pages (firesat-satellites, gemini-southeast-asia-report-2026) — both not AAIF-core (regional satellite/fire detection, regional AI adoption report) → 0 added this run. All other visible surface already in entries.json under normalized URL keys.
- ✅ https://hnrss.org/newest — accessible (HTTP 200); 20 items reviewed (Xiaomi 38B world model, AegisDB agent memory, Kimi K3 vs GPT 5.6 briefcase, AI Data Centers & Wealth concentration, etc.) → 0 added (all low density)

## Results
- **New candidates discovered**: 10 (all arxiv)
- **Candidates added**: 10
- **Existing entries (before this run)**: 1392
- **New entry count**: 1402 (delta +10)
- **Skipped (duplicate)**: 0

## Entries Added (all `status=active`, all via pipeline_utils.append_entries)

| ID | Source | Title | Score | Category |
|---|---|---|---|---|
| 2607.13285 | arxiv:2607.13285 | Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable | 5 | agents (normalized from agents/frameworks) |
| 2607.13157 | arxiv:2607.13157 | Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents | 5 | agents |
| 2607.13716 | arxiv:2607.13716 | CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems | 5 | agents |
| 2607.13884 | arxiv:2607.13884 | Experience Memory Graph: One-Shot Error Correction for Agents | 5 | agents |
| 2607.14004 | arxiv:2607.14004 | Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0 | 4 | agents |
| 2607.13705 | arxiv:2607.13705 | AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities | 4 | agents |
| 2607.14037 | arxiv:2607.14037 | Early Adoption of Agentic Coding Tools by GitHub Projects | 4 | coding |
| 2607.13918 | arxiv:2607.13918 | Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliability, and Blind-Spot Ceilings | 4 | agents |
| 2607.13104 | arxiv:2607.13104 | Self-Improvements in Modern Agentic Systems: A Survey | 4 | learning |
| 2607.13921 | arxiv:2607.13921 | Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code | 4 | coding |

Each entry has:
- real source URL verified by fetching `arxiv.org/abs/<id>` (HTTP 200, abstract + author block + dateline parsed)
- bilingual summary: `summary_zh` is a Chinese paraphrase of the abstract / body; `summary_en` is the public abstract verbatim (with HTML entities decoded). Both stored on the entry after `pipeline_utils.normalize_entry` cleaning.
- one-liner authored by `openclaw`, derived from the Chinese summary.
- `content/<id>.md` written via `exec + python3 + pathlib` with absolute paths (NOT via direct write tool on iCloud / Obsidian paths) into the canonical `content/<id>.md` path at the repo root.
- `quality_score` reflects the abstract level: the four most AAIF-thread-anchored entries (Harness Handbook, Oracle Agent Memory, CAVA, Experience Memory Graph) get **5**; the other six get **4**.

## Validation
- ✅ `entries.json` parses as dict (`{"entries": [...], "last_updated": ..., "total_entries": N}`)
- ✅ `len(entries) == total_entries` (1402 == 1402)
- ✅ Entry count did not decrease (1392 → 1402, +10)
- ✅ All 10 new entries are `status=active` and `quality_score >= 4` (no `score-pending` low-signal hits)
- ✅ `validate-schema.py` reports **0 errors**, 67 pre-existing warnings (none from the 10 new entries — warnings are all from earlier batches on `platform=industry/personal_blog/openai/hackernews` and short `summary_zh` on legacy entries)
- ✅ No invented entries — every title / author / abstract / url was fetched from the live `arxiv.org/abs/<id>` page
- ✅ All writes went through `pipeline_utils.load_entries_data` / `append_entries` / `save_entries_data` (per skill invariants)
- ✅ Content files are in `content/<id>.md` at the repo root (NOT in `openclaw/content/`)

## Site Generation
- ✅ `python3 scripts/generate-site.py` succeeded
- Modern static site regenerated: **739 display cards, 661 content pages, 7 channels** (was 729/651/7 before this run; +10 cards and +10 content pages match the 10 new entries)
- `dist/site-stats.json` timestamp: 2026-07-17T07:55:50.284173

## Push Status
- ❌ No push (external-scan mode does not push per skill definition)
- Working tree contains: 10 new entries, 10 new `content/<id>.md` files, regenerated site artifacts (739 / 661 / 7), modified `README.md` / `data/entries.json` / `metadata/stats.json` / `openclaw/README.md` / `content_fetcher_report.md`, and the new `openclaw/logs/external-scan-2026-07-17.json` + this report. Cron operator decides whether to commit/push in a later `site-rebuild-push` run.

## Notes
- arxiv cs.AI `recent` listing page returned 50 distinct paper IDs (2026-07-15/16/17 batch). All 50 were new vs the existing entries.json (the prior 2026-07-15 external-scan run had ingested 2607.11388 / 2607.11357 / 2607.11346 / 2607.11197 / 2607.11185 / 2607.11172 / 2607.11138 / 2607.10878 / 2607.11307 / canadian-ai-research from the 2026-07-14/15 batch). After AAIF title prefilter and field-by-field AAIF-aligned selection, 10 were picked.
- **Score-5 cluster (harness / governance / memory)** is intentional this run — the four entries sit at the core of existing AAIF threads: 2607.13285 (Harness Handbook advances the harness-engineering thread next to Managed Agents and Prompts-to-Contracts); 2607.13157 (Oracle Agent Memory advances the agent-memory substrate thread next to MRMS, NapMem, Proactive Memory, OPSMem); 2607.13716 (CAVA advances the runtime-governance thread next to LOGOS and Formal-Hierarchical-Orchestration); 2607.13884 (Experience Memory Graph advances the one-shot / no-trial-and-error agent memory thread).
- **Score-4 cluster (eval / coding / synthesis)**: 2607.14004 (Do Agent Optimizers Compound?) gives the first systematic continual-learning eval of agent optimizers (RELAI-VCL 76.4% lifelong avg vs GEPA 66.0% / Meta Harness 64.6% / baseline 58.7% on Terminal-Bench 2.0) — a benchmark-plus-design-recipe combo; 2607.13705 (AgentCompass) is the open-source eval-infra substrate (Benchmark/Harness/Environment decoupling); 2607.14037 (Early Adoption of Agentic Coding Tools) gives the first large-scale empirical study of agentic coding PR adoption across 2,361 GitHub repos (25,264 PRs) with the headline finding that intensive adoption remains concentrated in a small subset of projects; 2607.13918 (Partially Correlated Verifier Cascades) gives the minimal theory of correlated gates and shows independence-based extrapolation underestimates failure by 20× at k=5 and ~3000× at k=10 — practical lever is decorrelation, not adding gates; 2607.13104 (Self-Improvements Survey) is the 2026 synthesis of the self-improving-agents thread (foundation model + scaffold + update operator); 2607.13921 (Generative Compilation) advances AI-assisted coding with a Lean-mechanized Rust sealor that brings compiler feedback into the generation loop.
- Of the 50 arxiv candidates surfaced this batch, the 10 picked are the most AAIF-aligned. The remaining 40 were intentionally skipped because they are: pure-domain (Earthquaker-AI RAG for primary-school earthquake education, ODE Discovery for Biological Systems, AI-accelerated Professional Upskilling, Wind and Solar Power Prediction, AI-Augmented Human Resource Management, Pancreatic Cancer Resectability, Multi-Expert Routing for Manchu OCR, Music-to-Dance Generation, HOI Detection in the Wild, Node Classification, EgoziAerial Studies, OriginBlame data provenance); business/industry-light (AI-Native Insurance for Agentic AI — closer to product than field-note; AI advice suppresses I-don't-know); theoretical/niche (AIMO Interpretability Challenge, CayleyR TopSpin puzzle, EZSMT Version 3, Theory-Level Autoformalization, Networked Intelligence context graphs, SPINE cyber-physical, Probabilistic Belnap FOL, Music-to-Dance); eval/benchmarks with limited AAIF lift (UESF-Bench embodied seeking/following, Set-shifting Harnessed Agents test, AI advice psychology study, Bot Adoption in OSS projects); or otherwise tangential (AI advice psychology, Generative Compilation is the exception; the others all stayed outside the core agents/coding/infra/learning triangles). The 10 picked stay under the 20-entry daily-intake budget while maximizing AAIF-thread advancement.
- Anthropic news listed 6 new pages this batch: bernanke-bernanke (Bernanke LTBT appointment — corporate governance, not field-note); claude-for-teachers (consumer edtech product — low AAIF density); fable-safeguards-jailbreak-framework (continuation of the Fable 5 saga already represented by `b0d10e8d` and `147a989f`); hard-questions (Anthropic PR about asking the public for hard questions — meta-announcement); redeploying-fable-5 (continuation, same thread); reflect-with-claude (consumer Reflect beta — product announcement, low AAIF density); ust-claude (case study of UST bringing Claude to physical AI factory work — useful as evidence but already covered by Managed Agents / Claude for Industry threads). None rose to AAIF-active quality this round.
- Anthropic research listed 4 new pages: claude-plays-robotics (Frontier Red Team eval of Claude on robot bodies — niche robotics evaluation); global-workspace (interpretability research on Claude's internal thoughts — interesting but pure interpretability, low AAIF density); off-switch-dual-use (alignment / AE Studio collab on controlling dual-use knowledge — niche alignment); claude-values-models-languages (300K conversation analysis across models and languages — societal impacts analysis, low AAIF-thread density). Flagged for follow-up content-fetcher / community-review passes if/when full body extraction becomes reliable.
- Google blog surface: most visible AI-related items (sundar-pichai-io-2026 = `b10a3315`, gemini-spark-updates-june-2026 = `c66e2703`, gemini-study-notebooks = `2e3f360d`, expanding-managed-agents-gemini-api = `f7eb2a86`, interactions-api-general-availability = `a89b1dbe`, diffusion-gemma-faster-text-generation = `ab9c9a67` score-pending, helping-communities-prepare-for-natural-disasters = `9d77f2d8`) are already represented in entries.json under normalized URL keys; the 2 actually-new ones (firesat-satellites, gemini-southeast-asia-report-2026) are not AAIF-core (satellite fire detection, regional AI adoption report).
- The HN pipeline yielded AI-keyword items but none rose to AAIF-active quality this round: Xiaomi 38B world model (press-release level), AegisDB self-hosted agent memory (single-developer C-binary hobby project — low signal), Kimi K3 vs GPT 5.6 briefcase eval (single benchmark update on a third-party eval page, will revisit if Kimi releases their own field-note), AI Data Centers & Wealth concentration (policy blog post). Left for future HN / quality uplifts.
