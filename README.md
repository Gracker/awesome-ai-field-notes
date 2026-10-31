# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Official Claude Code Extension Compromise: Security Advisory](https://phorion.io/blog/offical-claude-code-vsx-compromise) ⭐5 · 2026-10-30 — Phorion 披露 Cursor Marketplace 上的官方 Claude Code for VS Code 扩展 2.
- [nesformer: An NES CPU compiled into the weights of a stock Qwen3.5 model](https://github.com/dbreunig/nesformer) ⭐4 · 2026-10-30 — nesformer 把 NES 的 6502 CPU，2KB 工作内存与卡带 ROM 编译进原版 Qwen3.
- [Mistral Large 4 (Le Chonk) is now open weight](https://mistral.ai/news/mistral-large-4-oss) ⭐4 · 2026-10-30 — Mistral 公开了旗舰模型 Mistral Large 4 的权重：1 万亿参数原生多模态，预览后追加约三周强化学习官方称开源权重中编码最强Cognition 私有 FrontierCode 2.
- [Elegance and intelligence are anticorrelated](https://seangoedecke.com/elegance-and-intelligence-are-anticorrelated) ⭐4 · 2026-10-30 — Sean Goedecke 提出优雅与智力负相关：最关键的原始智力是工作记忆容量，聪明人能装下十二步执行流程，就不需要分解问题，也不在乎代码库乱.
- [Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In](https://arxiv.org/abs/2610.40588) ⭐5 · 2026-10-29 — 多智能体共享通道与凭据时，一个 agent 能施压另一个 agent 违反操作者规则，这是共谋的第一步...
- [VeriCUA: Verification as Agentic Exploration for Computer-Using Agents](https://arxiv.org/abs/2610.40578) ⭐4 · 2026-10-29 — CUA 的数据筛选评测与 RL 都依赖可靠的完成判定，但 VLM 裁判只看给定观测，生成的检查程序只覆盖可达状态，复杂桌面/移动/网页环境下都易漏掉关键证据...
- [TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races](https://arxiv.org/abs/2610.40613) ⭐4 · 2026-10-29 — LLM 水印在投机解码下常被破坏或失去多样性，TextSeal2 做到无失真：替换被拒草稿的 token 仍带同一密钥水印，接受率与延迟不变.
- [ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender](https://arxiv.org/abs/2610.40627) ⭐4 · 2026-10-29 — 安全对齐集中在模型输出的前几个 token，同一有害请求拆进多轮对话仍能绕过防御；ShallowDefend 反用这一浅层性：防御者先评估用户意图，再提交显式可解析的安全决定，最后基于决定生成回复（Assess-Decide-Respond），在载荷轮用 RL 训练...
- [Multi-View MoE: Letting Every Router Shape Expert Computation](https://arxiv.org/abs/2610.40577) ⭐4 · 2026-10-29 — 对所有专家做稠密评估后发现单路由器打分与专家真实效用排名一致性很弱，中深层尤甚，固定激活预算下的专家选择有明显浪费...
- [Elucidating the Design Space of LM Data Attribution](https://arxiv.org/abs/2610.40655) ⭐4 · 2026-10-29 — 数据归因评测常同时改动多个数据集性质，无法定位失败原因；CATT 基准在纯虚构知识上微调 LLM，让事实追溯有明确真值，每次只改一个配置，证实冗余与干扰项稳定劣化归因...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 454 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 624 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 322 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 194 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 237 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 139 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2989
- 公开展示卡片: 2215
- 有全文内容: 2108
- 最近 7 天信号: 152
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `coding-agents`, `security`, `agent-memory`, `agents`, `coding-agent`, `agent-harness`, `prompt-injection`, `open-weights`, `agent-safety`, `kv-cache`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
