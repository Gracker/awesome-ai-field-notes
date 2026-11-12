# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code) ⭐5 · 2026-11-11 — DeepMind AlphaProof Code 形式化验证 Signal 协议代码：600 万行 Lean，四周完成
- [Gemini Decisions API: Fast, calibrated multimodal decisions](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api) ⭐5 · 2026-11-11 — Google 推出 Gemini Decisions API，由新模型 gemini-decision-1 驱动，面向封闭集决策原语：工具选择策略检查模型路由上下文分级单次多模态输入（文本/图像/音频/视频/PDF...
- [United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights) ⭐4 · 2026-11-11 — 美联航宣布禁止第三方个人 AI agent 代旅客订票：共享账户凭证（含支付信息）会暴露敏感数据可能造成误购改账户或误用里程，且 agent 代办值机等操作可能违反联邦规定（如行李需旅客本人当面确认无违禁品）美联航在自有数字平台并经旅行社与聚合渠道限制未授权 AI agent.
- [PSA: Fable on Pro consumes limits about 4x faster than Opus](https://www.reddit.com/r/ClaudeCode/comments/1xt1eo1/psa_for_pro_users_trying_fable_this_week_it_uses) ⭐3 · 2026-11-11 — Pro 试 Fable 额度消耗约 4x Opus：per-token 便宜不等于任务账单便宜
- [Nous Research raises ~$90M at ~$1.2B valuation narrative](https://www.wsj.com/pro/venture-capital/nous-research-scores-90-million-to-bring-open-source-ai-assistant-to-enterprises-516f9208) ⭐3 · 2026-11-11 — Nous Research 融资约 $90M（估值叙事 $1.2B），Hermes 转向企业扩张
- [Claude Code sent an Urgent push at 5:46 AM: background agent friction](https://www.reddit.com/r/ClaudeCode/comments/1xsp90d/at_546_am_i_get_anurgent_message_on_my_phone_from) ⭐3 · 2026-11-11 — 凌晨 5:46 收到 Claude Code Urgent 推送：后台 agent 的打扰边界
- [Cursor Projects is now multiplayer](https://cursor.com/blog/projects-multiplayer) ⭐5 · 2026-11-10 — Cursor Projects 多人化：共享任务板 + 团队 context + 跨队友 agent 消息（untrusted）
- [llama-modchip: CPU-First Inference for 284B & 30B MoE Models on 16-64 GB RAM](https://github.com/synchopate/llama-modchip) ⭐4 · 2026-11-10 — llama-modchip 是一组 ggml/llama.
- [MCP Apps bring full-screen interactive connectors to Claude](https://x.com/ClaudeDevs/status/2120227980672901180) ⭐4 · 2026-11-10 — MCP Apps 全屏化：SaaS UI 进对话，白名单即开，自建 public preview
- [Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins](https://www.latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins) ⭐4 · 2026-11-10 — Fable 5.2 复盘：榜上回顶，但任务账单 +31%max effort 反而掉分

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 514 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 695 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 368 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 222 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 266 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 147 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3231
- 公开展示卡片: 2456
- 有全文内容: 2330
- 最近 7 天信号: 180
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agent-security`, `coding-agents`, `agents`, `security`, `agent-memory`, `coding-agent`, `agent-harness`, `kv-cache`, `open-weights`, `mcp`, `agent-safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
