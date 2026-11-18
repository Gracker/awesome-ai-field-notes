# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Introducing FrontierHarness Eval v1.1: 22 harnesses x 5 models, the best harness differs per mod...](https://runta.com/blog/introducing-frontierharness-eval-v1-1) ⭐4 · 2026-11-17 — Runta 与 Baseten 的最大规模 harness 榜单：83B token27,280 次 agent 运行，22 harness x 5 模型 x 62 任务 x 4 尝试.
- [Update on October 2026 security incident](https://fireworks.ai/security/bulletins/october-2026-security-incident-update) ⭐4 · 2026-11-16 — Fireworks 对 10 月 9 日首份公告的更新把影响面从存储密钥扩大：部分账号的账号与账单信息（地址发票余额...
- [When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents](https://arxiv.org/abs/2611.21577) ⭐4 · 2026-11-16 — MCP 让 agent 组合多台 server 的工具，但用于发现和选择的工具元数据并不绑定已验证的提供方身份论文把 tool-provider misbinding 形式化为攻击者控制的工具选择优化问题：攻击者只需另起一台 MCP server 发布精心构造的元数据...
- [SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents](https://arxiv.org/abs/2611.21541) ⭐4 · 2026-11-16 — SciResearch-Eval 用标准实验室问题（加热材料拟合热传导模拟器）考 agent 的科研判断：自己设计实验用可能欠分辨或物理错误的模拟器每个属性给出对齐真值的 95% 区间held-out 93 任务9 模型2,511 回合：程序性陷阱都能处理...
- [Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied Requests](https://arxiv.org/abs/2611.21545) ⭐4 · 2026-11-16 — LLM 越来越多地替规则系统写拒绝解释，但多条规则独立拒绝时，解释可以列出真实原因用户照着修完却仍被拒论文定义 recourse validity（照解释改动作能否翻转决定）并精确计算.
- [Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle](https://arxiv.org/abs/2611.21538) ⭐4 · 2026-11-16 — RLVR 继承 verifier 的一切错误：数学和代码之外 verifier 只是代理，与真实目标的距离从没被测过，reward 上涨分不清是真进步还是被 hack作者用 124,416 个上下文上的可执行授权策略构造能精确列出每个决策全部最小充分理由的过程级 oracle.
- [Latent Lattice Language Models](https://arxiv.org/abs/2611.21608) ⭐4 · 2026-11-16 — 不加深层数也不加循环步，而是增加模型同时维持的活跃计算状态数：Lattice of Latents 在每层加一条沿时间循环的水平 latent 流，与竖直残差流并行与 Transformer-SSM 混合架构不同，这些 latent 不是序列混合的内部记忆.
- [阿里发布 Qwen4-Max：2.4T 参数 / 1M 上下文 / 仅托管不开源](https://qwen.ai/blog?id=qwen4-max) ⭐3 · 2026-11-16 — 阿里 11 月 16 日上线 Qwen4-Max，仅在阿里云托管开放 API，不开源：2.
- [NVIDIA Allegedly Engineered Scarcity By Funding AI Startups To Buy Its GPUs](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) ⭐3 · 2026-11-16 — TechPowerUp 转述华尔街日报（经 Wccftech）报道：NVIDIA 被指通过投资 AI 创业公司再由后者采购 GPU 建数据中心的方式人为加剧本轮 GPU 与显存短缺，属循环融资式需求预支报道为指控性质...
- [All AI-generated code should be Open Source](https://jakub.jankiewicz.org/blog/ai-code-open-source) ⭐3 · 2026-11-16 — Jankiewicz 主张 AI 生成的代码都应开源：模型语料取自未经许可抓取的开源代码与按 CC 协议要求署名的 Stack Exchange 内容，把这份集体知识变成专有输出近乎许可证洗白.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 543 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 736 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 394 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 234 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 289 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 152 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3368
- 公开展示卡片: 2592
- 有全文内容: 2464
- 最近 7 天信号: 181
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `claude-code`, `anthropic`, `multi-agent`, `agents`, `agent-security`, `coding-agents`, `security`, `agent-memory`, `kv-cache`, `mcp`, `coding-agent`, `codex`, `open-weights`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
