# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Introducing Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐4 · 2026-10-24 — Kimi K3.1 Pro：最强 3T 级开源权重模型，1M 上下文；开源版主动清除网络攻击数据，攻击能力被刻意压到前沿之下
- [Claude Duet: proactive agent research preview powered by Opus 5.5](https://claude.com/product/claude-duet) ⭐4 · 2026-10-23 — Claude Duet 研究预览：早晨简报加消息派活，云端自己持续干活，敏感操作先审批，Opus 5.5 驱动
- [TorchTPU: PyTorch backend for Google TPUs (google-pytorch/torch_tpu)](https://github.com/google-pytorch/torch_tpu) ⭐3 · 2026-10-23 — Google 官方开源 PyTorch TPU 后端：ATen kernel 加 XLA 编译缓存加 torch.compile，训练/推理栈开源竞争再加一子
- [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650) ⭐4 · 2026-10-22 — 证据缺失让"每句都真"的代理照样执行禁令动作：300 对任务的可执行基准测安全边界与证据恢复，十模型差异显著
- [Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](https://arxiv.org/abs/2610.31639) ⭐4 · 2026-10-22 — CoT 解释可能是事后合理化：把推理拆成隔离上下文的 DAG每节点只看因果父节点，因果敏感度 +12~21pp
- [Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent L...](https://arxiv.org/abs/2610.31280) ⭐4 · 2026-10-22 — 多代理管线收益归因：F1 提升主要来自专门化提示而非类型化契约，但类型化状态能在边界拦住越界输出避免晚失败丢数据
- [BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing](https://arxiv.org/abs/2610.31633) ⭐4 · 2026-10-22 — 循环模型推理内存线性增长的解法：随机深度预训练 + KV 缓存跨深度共享，命中率 +31%p90 TTFT 降 84%
- [Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](https://arxiv.org/abs/2610.31461) ⭐4 · 2026-10-22 — 编码代理的技能粒度应当运行时路由：宏失败自动回退微级恢复，技能库从检索资源升级为可控执行抽象
- [Introducing 1Password for Agents](https://1password.com/blog/1password-for-ai-agents) ⭐4 · 2026-10-22 — 1Password for Agents：代理登录时向密码库请求凭据用户批准后由 1Password 直接代填，密码不进代理上下文
- [智能体手机加速爆发？换机困境端侧AI与下一代入口之争](https://mp.weixin.qq.com/s?__biz=MzA4NjUwNTI0OA%3D%3D&mid=2247500542&idx=1&sn=e8e3fde608787b50549a4985e457c186) ⭐3 · 2026-10-22 — 换机周期 4348 个月才是厂商押注智能体手机的真正推力，Agent 是下一轮换机的新故事

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 431 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 582 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 308 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 185 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 220 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 133 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2876
- 公开展示卡片: 2148
- 有全文内容: 2037
- 最近 7 天信号: 118
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `agent-safety`, `kv-cache`, `prompt-injection`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
