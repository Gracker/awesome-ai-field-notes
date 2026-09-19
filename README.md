# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [OWASP Agent Memory Guard：针对 agent 记忆中毒的运行时防御项目上线](https://github.com/OWASP/www-project-agent-memory-guard) ⭐4 · 2026-09-19 — OWASP Agent Memory Guard 上线：运行时拦住上下文重置后的记忆中毒，PyPI 双包可用
- [Package Management 周报 09-19：Rust 社工攻防YARD 文档生成执行边界Podman/CVE-2025-11395](https://nesbitt.io/2026/09/19/this-week-in-package-management.html) ⭐4 · 2026-09-19 — Nesbitt 包管周报：Rust 社工攻防 + rubygems 文档生成也是执行边界实证
- [Doctorow Textured：LLM 统计平滑隐藏了意识参与才是产出意外的唯一条件](https://pluralistic.net/2026/09/18/surprise) ⭐4 · 2026-09-18 — Doctorow：LLM 只能平整，意外在纹理里，验证意识参与才是产出下一个意外的唯一条件
- [Dan Abramov 用 frontier 模型反正 Conway refinement 推论 (4 周 / 40B token / ~$40k)](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture) ⭐4 · 2026-09-18 — 前 React 核心用 frontier 模型 + Lean 隐闭环了 50 年老推论：40B token ~$40k 三周
- [Claude Code 2.1.277 原生读 AGENTS.md：无 CLAUDE.md 时回退到跨 harness 文件](https://x.com/trq212/status/2101009392611278961) ⭐4 · 2026-09-18 — Claude Code 2.1.277 原生读 AGENTS.md：有 CLAUDE.md 时仍只听 CLAUDE，无才回退
- [ChatGPT 插件多账号上线：开发者可退回 MCP profile tool 打标](https://x.com/mxstbr/status/2100966048132718786) ⭐4 · 2026-09-18 — ChatGPT 多账号插件上线：开发者退回 MCP profile tool 让 ChatGPT 给账号打标
- [Anthropic 与 Accenture 联手嵌入式评测：合计 1B USD / 5 年](https://www.anthropic.com/news/accenture-embedded-evaluation) ⭐4 · 2026-09-18 — Anthropic + Accenture 5 年各投 10 亿美元：评测者从交卷式转为驻场嵌入
- [stealthprint Case Study: union-alpha 指纹分析](https://github.com/majiayu000/stealthprint/blob/main/docs/case-union-alpha.zh-CN.md) ⭐5 · 2026-09-17 — stealth 模型匿名挡不住 token 级取证：词表视觉塔计费公式工具调用语义三层指纹把候选名单缩到个位数，黑盒也能验明正身
- [SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic...](https://arxiv.org/abs/2609.19705) ⭐4 · 2026-09-17 — 15 个学术金融交易 agent 全军覆没：80% 鲁棒性不达标，100% 有安全漏洞
- [分享一个大幅节省Codex额度的邪修方法，不要浪费了你的ChatGPT Pro会员](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647686431&idx=1&sn=c1bfba7e0b5b7cf995e444daf79861a4) ⭐3 · 2026-09-17 — 规划用网页版 GPT-6 Pro实施用 Codex：把生产数据封装成只读 MCP 挂进网页插件，用上下文可见性和额度的入口差省下一个量级的成本

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 325 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 422 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 236 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 116 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 149 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 102 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2364
- 公开展示卡片: 1488
- 有全文内容: 1396
- 最近 7 天信号: 116
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `claude-code`, `agent-security`, `multi-agent`, `security`, `agent-memory`, `coding-agent`, `agents`, `field-note`, `open-source`, `coding-agents`, `google`, `codex`, `agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
