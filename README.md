# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [GLM-5.3-Flash: Frontier Intelligence, Flash Cost](https://z.ai/blog/glm-5.3-flash) ⭐4 · 2026-08-26 — GLM-5.3-Flash：320B 总参/18B 激活+稀疏线性混合注意力，约 1/10 价格逼近 Claude Opus 4.8；曾以 ox-alpha 匿名盲测登顶当周人气
- [The AI Hater's Manifesto](https://www.wheresyoured.at/the-ai-haters-manifesto) ⭐4 · 2026-08-25 — AI 批评侧的基准文本：论据不是直觉而是社会投入的对照与亲身实验的失败样本，做 AI 产业分析时这是必须能反驳（或引用）
- [Hardening the Override Flag: 包管理器危险开关的防御设计](https://nesbitt.io/2026/08/25/hardening-the-override-flag.html) ⭐4 · 2026-08-25 — Andrew Nesbitt 梳理过去几年包管理器与 CLI 工具里危险开关的防御设计把 rmaptpipcargopacmanGoNixHomebrewDockergitCeph 摆到一张表里...
- [Foot Guns for Sale](https://idiallo.com/blog/foot-gun-for-sale) ⭐4 · 2026-08-25 — 去中心化/本地推理路线的一个清醒样本：不喊口号，用 IDE 切换无感与外设逆向实例说明集中式叙事的裂缝在哪里
- [StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments](https://arxiv.org/abs/2608.24804) ⭐4 · 2026-08-25 — StarHarness：权重固定只靠分层搜索进化环境专属 harness（prompt/工具/技能/子智能体/循环配置），企业基准性能提升 20-35 个百分点并可跨模型族迁移
- [SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL](https://arxiv.org/abs/2608.24870) ⭐4 · 2026-08-25 — SPO++：发现单流策略优化中轨迹白化与 token-mean actor loss 的度量错配，用动作 token 度量标准化修复，异步 agentic RL 效率提升
- [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2608.24876) ⭐4 · 2026-08-25 — Recuris：工作记忆与经验记忆耦合形成有边界的递归记忆演化循环，10 模型 x 4 长程基准中 35/37 配对成功率提升
- [Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows](https://arxiv.org/abs/2608.24842) ⭐4 · 2026-08-25 — 读到了不等于用上了：长上下文金融分析存在检索-整合鸿沟，无关上下文涨到 128K token 后风险披露对投资判断的影响只剩噪声
- [The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams](https://arxiv.org/abs/2608.23541) ⭐5 · 2026-08-24 — ICML 2026：多智能体互看完整解会让提案一轮内趋同；独立生成再共享对的信息，才是等预算下的默认最优
- [SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564) ⭐5 · 2026-08-24 — 整仓迁移三阶段评测：8 个前沿模型 520 次运行仅 5.4% 全通过，最好的 claude-opus-5 也只有 47.0/100

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 260 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 312 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 169 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 80 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 105 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 76 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2009
- 公开展示卡片: 1139
- 有全文内容: 1050
- 最近 7 天信号: 144
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-memory`, `security`, `multi-agent`, `google`, `claude-code`, `coding-agent`, `agent-security`, `coding-agents`, `llm`, `llm-agents`, `mcp`, `open-source`, `agents`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
