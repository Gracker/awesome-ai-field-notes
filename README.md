# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [dots3-note-prev: 280B MoE 多模态长上下文 agent 底座（Apache-2.0）](https://huggingface.co/dots-studio/dots3-note-prev) ⭐4 · 2026-08-15 — 280B MoE/16B active/512K 上下文的开源多模态 agent 底座：工程字段已坐实，TEMPO 方法论还停在 X 宣布层
- [OpenSandbox: Secure, Fast, and Extensible Sandbox runtime for AI agents](https://github.com/opensandbox-group/OpenSandbox) ⭐4 · 2026-08-15 — 开源可自托管的 agent sandbox 平台：K8s 调度 + gVisor/Kata/Firecracker 分级隔离 + Credential Vault 不把真密钥给 workload
- [GLM-5.3: Frontier Coding with Emergent Cyber Capabilities](https://z.ai/blog/glm-5.3) ⭐5 · 2026-08-14 — GLM-5.3: Frontier Coding with Emergent Cyber Capabilities
- [Capital formation: Going legit means going mainstream（DMCA 1201 豁免流程批判）](https://pluralistic.net/2026/08/14/one-chokable-throat) ⭐5 · 2026-08-14 — 对做第三方 app store / 第三方维修 / 平台竞争政策讨论的读者，这是一篇框架级文章：把 2026 年仍在进行的政策争论接到 1998 年立法源头，并
- [droidrun/mobile-harness：给 AI agent 的真机控制 Markdown harness（非 runtime）](https://github.com/droidrun/mobile-harness) ⭐4 · 2026-08-14 — 真机 agent 控制面分层的直接素材：探索层用 harness回归层用脚本证据层用 Perfetto这是把agent 开真机从安利帖变成可执行选型
- [DecryptAds：把广告供应链拆开给你看（ads.txt/sellers.json 交叉透视）](https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out) ⭐4 · 2026-08-14 — 不是再讲一遍广告在追踪你，而是给出一个能立刻查任何站点的工具 + 一组可复述的供应链安全事实，做反 malvertising / 供应链安全的工程师可直接上
- [Agent 限流状态机：额度是编排状态，不是模型属性](https://godofgpt.com/entry/2f4b0c1d/) ⭐4 · 2026-08-14 — overnight 长程任务的实用框架：启动写 task_id/goal/checkpoint_path/quota_mode，每工具环刷新 checkpoin
- [Agent 与人类协作三原则：授权分桶外显可解释性静默抑制](https://godofgpt.com/entry/3cb2c509/) ⭐3 · 2026-08-14 — Harness 运行时之外的另一层：runtime 解agent 自己怎么不崩，协作纪律解人与 agent 的边界三段式摘要与静默抑制可直接落到现有
- [Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐4 · 2026-08-13 — Qwen3.8-27B-FP8
- [Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding](https://arxiv.org/abs/2608.11095) ⭐4 · 2026-08-13 — Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 275 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 258 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 138 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 55 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 73 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 51 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 154 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1825
- 公开展示卡片: 1004
- 有全文内容: 908
- 最近 7 天信号: 116
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `arxiv`, `research`, `benchmark`, `evaluation`, `openai`, `attention`, `google`, `anthropic`, `security`, `coding-agent`, `agent-security`, `claude-code`, `agent-memory`, `coding-agents`, `optimization`, `multi-agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
