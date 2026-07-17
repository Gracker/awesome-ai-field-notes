# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Experience Memory Graph: One-Shot Error Correction for Agents](https://arxiv.org/abs/2607.13884) ⭐5 · 2026-07-15 — Experience Memory Graph (EMG) 把 agent failure recovery 重写为图匹配问题：训练阶段把失败探索轨迹与成功专家轨迹都转为有向"动作决策图"...
- [CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems](https://arxiv.org/abs/2607.13716) ⭐5 · 2026-07-15 — CAVA (Canonical Action Verification and Attestation) 在 Proof-Carrying Agent Actions (PCAA) 之下定义稳定的"运行期规范动作对象"：把本地 coding hookSDK tool浏览器自动化m...
- [Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliabilit...](https://arxiv.org/abs/2607.13918) ⭐4 · 2026-07-15 — 该论文给出 LLM harness 串行验证门的最简相关理论：用 de Finetti 潜变量 ~ G 刻画每个 gate 对生成器自身错误的假阳性率，得到精确级联后验 _k = _0 ln m_k（m_k 为 G 的 k 阶矩）...
- [Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code](https://arxiv.org/abs/2607.13921) ⭐4 · 2026-07-15 — Generative Compilation 是首个在 LLM 生成过程中就拿到编译器反馈的方法：核心机制 sealor 把部分程序轻量语法引导地补完为完整程序，让现成编译器可诊断设计上保证"可能被补完的部分程序永不被拒"...
- [Early Adoption of Agentic Coding Tools by GitHub Projects](https://arxiv.org/abs/2607.14037) ⭐4 · 2026-07-15 — 基于 2,361 个热门 GitHub 仓库 25,264 条 agentic PR 的实证分析...
- [Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](https://arxiv.org/abs/2607.14004) ⭐4 · 2026-07-15 — 该文首次系统提出"agent 优化器是否会随时间复合收益"的 continual-learning 评测：在 Terminal-Bench 2.
- [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705) ⭐4 · 2026-07-15 — AgentCompass 是一套面向 LLM-based agent 的开源轻量可扩展的统一评测基础设施，核心抽象是 Benchmark / Harness / Environment 三件独立可替换的组件...
- [Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents](https://arxiv.org/abs/2607.13157) ⭐5 · 2026-07-14 — Oracle Agent Memory 把"agent memory"明确为长时程 Agent 的系统工程问题，主张用 Oracle Database 作为原生 memory substrate.
- [Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable](https://arxiv.org/abs/2607.13285) ⭐5 · 2026-07-14 — 该论文提出 Harness Handbook 框架，把传统以文件/模块组织的 agent harness 代码库自动合成为以"行为"为单位的可读可定位可编辑的索引.
- [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) ⭐4 · 2026-07-14 — Self-Improvements in Modern Agentic Systems综述把现代 self-improving agents 框为"把经验转化为累积能力增益"的适应系统.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 232 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 167 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 91 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 24 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 47 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 39 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 139 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1402
- 公开展示卡片: 739
- 有全文内容: 661
- 最近 7 天信号: 92
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `agent`, `2026`, `multi-agent`, `claude-code`, `benchmark`, `gemini`, `open-source`, `enterprise`, `harness`, `workflow`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
