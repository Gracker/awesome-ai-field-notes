# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code) ⭐5 · 2026-11-11 — DeepMind AlphaProof Code 形式化验证 Signal 协议代码：600 万行 Lean，四周完成
- [PSA: Fable on Pro consumes limits about 4x faster than Opus](https://www.reddit.com/r/ClaudeCode/comments/1xt1eo1/psa_for_pro_users_trying_fable_this_week_it_uses) ⭐3 · 2026-11-11 — Pro 试 Fable 额度消耗约 4x Opus：per-token 便宜不等于任务账单便宜
- [Nous Research raises ~$90M at ~$1.2B valuation narrative](https://www.wsj.com/pro/venture-capital/nous-research-scores-90-million-to-bring-open-source-ai-assistant-to-enterprises-516f9208) ⭐3 · 2026-11-11 — Nous Research 融资约 $90M（估值叙事 $1.2B），Hermes 转向企业扩张
- [Claude Code sent an Urgent push at 5:46 AM: background agent friction](https://www.reddit.com/r/ClaudeCode/comments/1xsp90d/at_546_am_i_get_anurgent_message_on_my_phone_from) ⭐3 · 2026-11-11 — 凌晨 5:46 收到 Claude Code Urgent 推送：后台 agent 的打扰边界
- [Cursor Projects is now multiplayer](https://cursor.com/blog/projects-multiplayer) ⭐5 · 2026-11-10 — Cursor Projects 多人化：共享任务板 + 团队 context + 跨队友 agent 消息（untrusted）
- [llama-modchip: CPU-First Inference for 284B & 30B MoE Models on 16-64 GB RAM](https://github.com/synchopate/llama-modchip) ⭐4 · 2026-11-10 — llama-modchip 是一组 ggml/llama.
- [MCP Apps bring full-screen interactive connectors to Claude](https://x.com/ClaudeDevs/status/2120227980672901180) ⭐4 · 2026-11-10 — MCP Apps 全屏化：SaaS UI 进对话，白名单即开，自建 public preview
- [Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins](https://www.latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins) ⭐4 · 2026-11-10 — Fable 5.2 复盘：榜上回顶，但任务账单 +31%max effort 反而掉分
- [Claude full reset: one free reset across all models and limits](https://x.com/ClaudeDevs/status/2120275296637321476) ⭐4 · 2026-11-10 — Claude 全量重置：Pro/Max/Ultra/Team 每人一次全模型全限额，12-10 截止
- [Claude Code v2.1.322 adds fast mode on Vertex](https://github.com/anthropics/claude-code/releases/tag/v2.1.322) ⭐3 · 2026-11-10 — Claude Code 2.1.322：Vertex 三区域 fast mode，拒绝则回落标准速度

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 510 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 692 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 368 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 220 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 265 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 147 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3221
- 公开展示卡片: 2446
- 有全文内容: 2330
- 最近 7 天信号: 170
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agent-security`, `coding-agents`, `security`, `agents`, `agent-memory`, `coding-agent`, `kv-cache`, `open-weights`, `mcp`, `agent-safety`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
