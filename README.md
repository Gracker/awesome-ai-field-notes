# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Android Bench 2.0: 以长周期任务拓展 AI 开发的技术前沿](https://mp.weixin.qq.com/s?__biz=Mzk0NDIwMTExNw%3D%3D&mid=2247598097&idx=1&sn=6b1da17515983d0b7be38b800903462d) ⭐4 · 2026-09-23 — Android Bench 2.0 以长周期任务（升级依赖从零构建应用跨平台移植）重塑 AI 编码评估，评分体系联动 Harbor
- [Can gzip be a language model?](https://nathan.rs/posts/gzip-lm) ⭐3 · 2026-09-23 — 只用 zlib + beam search 走出一个可生成 Shakespeare 体字的压缩机：语言模型是压缩机这一论点在字节层的反向工程实现
- [Unreal Agent: asynchronous tool-call harness cuts frontier-agent cost 40%](https://unreallabs.ai/blog/unreal-agent) ⭐4 · 2026-09-22 — Unreal Agent 用异步 in-progress 事件重塑 harness 生命周期，Terminal-Bench 与 Codex 并列 57.9% 但成本便宜 39%，DeepSWE 1.1 72.4% 低于 Codex 但贵于便宜 16%
- [Unfinished Work in Package Security](https://nesbitt.io/2026/09/22/unfinished-work-in-package-security.html) ⭐4 · 2026-09-22 — 2026 供应链安全年度总结：包管理器 release pipeline 本身就是一条独立攻击面，10 次审计中中招 6 次，agent 时代又多了生成代码身份的另一条路
- [Package Manager Threat Model, Revisited](https://nesbitt.io/2026/09/22/package-manager-threat-model-revisited.html) ⭐4 · 2026-09-22 — 四个月 126 份公告验证包管理器威胁模型：最危险的不是可 grep 的 CWE，而是两个特性在接缝处错配的信任假设
- [Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna) ⭐4 · 2026-09-22 — Opus 5.5 + GPT-6 Sol/Luna 同日发布：Luna 拉到 $0.10/M，Opus 5.5 cache read 降 60%，但 max 思维档画鹭鹄踩在 128k 输出上限上
- [Qwen-Image-2.1 Uncensored GGUF (abenzerps)](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF) ⭐3 · 2026-09-22 — Qwen-Image-2.1 全档 GGUF 上线：T2I 权重 + ComfyUI 配套件齐备，8GB 显存已能本地跑完整生图链
- [Are LLMs still surprisingly bad at some simple tasks?](https://shkspr.mobi/blog/2026/09/are-llms-still-surprisingly-bad-at-some-simple-tasks) ⭐3 · 2026-09-22 — 同一道题一年后全行业仍无模型满分：评测缺的不是更难的题，是这种有确定答案的简单靶子
- [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) ⭐4 · 2026-09-21 — RRSI：给 agent harness 递归自我进化加正则化，OOD benchmark 仍 +4.7 分，policy token 省 30%
- [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974) ⭐4 · 2026-09-21 — Harness-Zero：把专用 agent harness 蒸馏进权重，部署时不带 harness 反超带着的，任务成功率 23.3% 升至 44.3%

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 337 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 443 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 243 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 122 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 152 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 105 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2416
- 公开展示卡片: 1540
- 有全文内容: 1447
- 最近 7 天信号: 103
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `claude-code`, `agent-security`, `security`, `agent-memory`, `coding-agent`, `agents`, `coding-agents`, `google`, `agent`, `field-note`, `open-source`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
