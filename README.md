# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Inte...](https://arxiv.org/abs/2607.08774) ⭐5 · 2026-07-13 — 把 inference-time control 抽象成第一类接口：固定模型下，结构化脚手架能系统性降低 LLM 失败率，reliability 不只是 scale 问题
- [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653) ⭐4 · 2026-07-13 — VEXAIoT 用检测 + 执行双智能体自动跑 IoT 渗透测试，OWASP IoT 场景 260 次执行 95% 成功率
- [TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Sys...](https://arxiv.org/abs/2607.09586) ⭐4 · 2026-07-13 — TrustX ARC 用 12 维量表给七类智能体 AI 系统风险分级，三层治理输出 + 编程助手专属扩展
- [Practical Source Code Recovery from Binary Functions Using Anchor-Based Retrieval and LLM Reason...](https://arxiv.org/abs/2607.09452) ⭐4 · 2026-07-13 — 用 anchor 检索 + LLM 重排从 stripped 二进制找回源码，tcpdump 上 95.2% 指令覆盖
- [OpenProver: Agentic and Interactive Theorem Proving with Lean 4](https://arxiv.org/abs/2607.09217) ⭐4 · 2026-07-13 — OpenProver 把 Planner-Worker-Verifier 搬到 Lean 4 自动定理证明上，开源 + 交互式人机协同搜索
- [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scalin...](https://arxiv.org/abs/2607.09153) ⭐4 · 2026-07-13 — KV-PRM 直接复用生成阶段的 KV cache，把 PRM 评分从 O(L) 降到 O(L)，长多智能体 TTS 提速 5000 倍
- [Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI](https://arxiv.org/abs/2607.09560) ⭐4 · 2026-07-13 — 用'词汇鸿沟'和'验证器鸿沟'刻画 AI 与开放式智能的距离，提出创新自主性阶梯与生成性表征变换
- [ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning](https://arxiv.org/abs/2607.09059) ⭐4 · 2026-07-13 — ARCANA 用感知-假设-符号执行-反思四智能体协作解 ARC-AGI-2，可微黑板 + 元控制器调度抽象变换任务
- [Pi Agent 配置指南：打造专属 AI 编程助手](https://godofgpt.com/entry/78c2e5c8/) ⭐3 · 2026-07-12 — 原文链接： 作者：ninthbit...
- [AI 职业建议](https://godofgpt.com/entry/ac240c5f/) ⭐3 · 2026-07-12 — 作者: AYi_AInotes 链接: 抓取时间: 2026-07-0...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 229 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 147 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 82 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 23 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 45 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 37 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 139 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1235
- 公开展示卡片: 702
- 有全文内容: 624
- 最近 7 天信号: 74
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `2026`, `multi-agent`, `claude-code`, `benchmark`, `gemini`, `enterprise`, `agent`, `digest`, `open-source`, `manual`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
