# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [当我们聊 Agent OS 时，我们聊些什么](https://mp.weixin.qq.com/s?__biz=MzkzNTk2MDUxMg%3D%3D&mid=2247484348&idx=1&sn=cbf6bd580b44738c6f501f9ffd6383bb&chksm=c3f5eb56a9d66370fc52075887c47735629523dabdbc4cac41a5b90fe09da491d20fd3c16c15) ⭐4 · 2026-07-26 — Agent OS 的核心不是更强聊天框，而是围绕记忆技能权限和数据编织的系统层
- [Bringing PyTorch Monarch to AMD GPUs: Single-Controller Distributed Training on ROCm](https://pytorch.org/blog/bringing-pytorch-monarch-to-amd-gpus-single-controller-distributed-training-on-rocm) ⭐4 · 2026-07-26 — 大模型训练基础设施开始把 GPU 和节点故障当成常态来设计恢复路径
- [Open-weight AI is having its Kubernetes moment. Let's not ruin it.](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment) ⭐5 · 2026-07-25 — 开放权重模型正在成为 AI 基础设施的中立底座，竞争重点会转向运行时和生态
- [Open source software distribution may be rewritten by coding agents](http://antirez.com/news/170) ⭐4 · 2026-07-24 — AI coding 让软件分发从交付静态成品，转向交付可被 Agent 安全改造的模板和边界
- [LLMs reward expertise](https://seangoedecke.com/llms-reward-expertise) ⭐4 · 2026-07-24 — LLM 让人人变成泛化手，但真正上限来自领域专家的判断力
- [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535) ⭐4 · 2026-07-23 — 百万 token 上下文下，draft 模型的 KV 成本已经从小优化变成推理系统瓶颈
- [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557) ⭐4 · 2026-07-23 — Agent 训练正在从离线任务转向真实 harness 内的轨迹工具和容器化 rollout
- [Can a MUD evaluate LLMs? CrucibleBench](https://cruciblebench.ai/) ⭐4 · 2026-07-23 — 把 MUD 变成 LLM 行为显微镜：小环境也能暴露幻觉动作和对话循环
- [The Subprime Data Center Crisis](https://www.wheresyoured.at/the-subprime-data-center-crisis) ⭐4 · 2026-07-23 — 判断 AI 数据中心风险，要看 SPV偿债覆盖和客户集中度，而不只看算力需求
- [The Arguments Against Open Source AI are Very Bad](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad) ⭐4 · 2026-07-23 — Open-weight AI 的核心争论不是意识形态口号，而是底层组件开放会如何改变创业成本和产业控制权

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 228 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 145 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 86 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 24 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 46 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 34 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1531
- 公开展示卡片: 713
- 有全文内容: 621
- 最近 7 天信号: 69
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `arxiv`, `google`, `anthropic`, `benchmark`, `evaluation`, `optimization`, `2026`, `claude-code`, `gemini`, `agent`, `digest`, `codex`, `coding-agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
