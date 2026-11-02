# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Cursor marketplace compromise of Claude Code extension: official security notice](https://cursor.com/blog/claude-code-extension-security-notice) ⭐4 · 2026-11-02 — Cursor 官方公告确认：10 月 29 日 2:2713:35（太平洋时间）间，其市场上的 Anthropic.
- [Hermes 190 个 cron 任务复盘：看门狗时代结束，上下文预算成为新单点](https://godofgpt.com/entry/cb9c878c/) ⭐3 · 2026-11-01 — 对本机 190 个 Hermes cron 任务的复盘：127 个禁用任务里 101 个属于旧的五段式流水线（采集/成稿/发布/通知/看门狗），现已被 15 个单任务替代，18 个看门狗只剩 1 个启用合并消掉了交接失败面...
- [Google Project Suncatcher: first AI response from a data-center-class TPU in orbit](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-satellite-response) ⭐3 · 2026-11-01 — Google 轨道 TPU 卫星跑通首个 AI 响应：星上 Gemma 4 生成俳句下行回传，下一步验证热应力与辐射下的工作负载.
- [VOLTA-AUTODOXER: infostealer outsources victim appraisal to LLMs via OpenRouter](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer) ⭐4 · 2026-10-31 — Cisco Talos 披露 VOLTA-AUTODOXER：窃密木马偷完凭据后把序列化受害者档案 POST 给 OpenRouter，让模型以 forensic analyst 身份输出 WHAT THEY'RE WORTH 与 THEIR OPSEC.
- [Report from the Vatican](https://garymarcus.substack.com/p/report-from-the-vatican) ⭐4 · 2026-10-31 — Gary Marcus 记述在梵蒂冈见到教皇利奥十四世，转录其 AI 讲话五条主张（引 2026 年 5 月通谕Magnifica Humanitas编号）：AI 的未来没有被预先决定；机器无身体不经历体验（编号 99）...
- [Pluralistic: Formalities (31 Oct 2026)](https://pluralistic.net/2026/10/31/burn-berne) ⭐4 · 2026-10-31 — Cory Doctorow 论 AI 时代版权：版权只保护人类作者Feist 案确立版权奖励创意而非劳动；猴子自拍案确立非人无版权，算法比猴子更不是人.
- [Anthropic renames Max 20x to Ultra: 5-hour window dropped for weekly quota](https://www.anthropic.com/pricing) ⭐3 · 2026-10-31 — 订阅计量从 5 小时窗口转向周配额：Ultra 无 5 小时限制加 $200 API credits，跑长任务的 Claude Code 用户要按周折算用量
- [Official Claude Code Extension Compromise: Security Advisory](https://phorion.io/blog/offical-claude-code-vsx-compromise) ⭐5 · 2026-10-30 — Phorion 披露 Cursor Marketplace 上的官方 Claude Code for VS Code 扩展 2.
- [Black October for AI Developer Platforms](https://www.wiz.io/blog/black-october-for-ai-developer-platforms) ⭐5 · 2026-10-30 — 一个月 9 家 AI 平台被打的共同点：信任边界止步于环境变量加密存储，攻击者直接打平台侧解密路径第三方平台上的 AI key 应轮换
- [nesformer: An NES CPU compiled into the weights of a stock Qwen3.5 model](https://github.com/dbreunig/nesformer) ⭐4 · 2026-10-30 — nesformer 把 NES 的 6502 CPU，2KB 工作内存与卡带 ROM 编译进原版 Qwen3.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 462 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 641 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 327 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 197 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 243 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 139 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3028
- 公开展示卡片: 2254
- 有全文内容: 2138
- 最近 7 天信号: 122
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `coding-agents`, `security`, `agent-memory`, `agents`, `coding-agent`, `agent-safety`, `prompt-injection`, `agent-harness`, `open-weights`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
