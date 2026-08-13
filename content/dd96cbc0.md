# Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models

> Source: https://arxiv.org/abs/2608.10824
> Author: Zhijie Wu, Kento Kawaharazuka, Kei Okada
> Original date: 2026-08-11
> Added by: AAIF daily-intake-evening 2026-08-13

## 摘要
Gated VLA-Cache 针对 Vision-Language-Action 模型复用 KV cache 的可靠性问题，引入 top-2 action token logit margin 作为零成本置信信号：margin 低于阈值就失效 cache 触发 full recompute。OpenVLA / OpenVLA-OFT 在 LIBERO-Goal / Long 上恢复 100% 精度损失，同时保留约 80% compute savings。

## English Summary
Vision-Language-Action(VLA) models map camera images and language instructions directly to motor commands through a single autoregressive transformer. In real-time control, they still spend substantial compute recomputing key-value(KV) representations for visual tokens that barely change across neighboring frames. Recent work such as VLA-Cache reduces that cost by reusing KV states for visually static patches, but its policy relies only on observation-space heuristics and does not account for the model's own uncertainty. We propose Gated VLA-Cache, a lightweight, training-free extension that augments visual-similarity caching with neural introspection. The method monitors the logit margin between the top two predicted action tokens, a zero-cost confidence signal available during decoding. When the margin drops below a threshold, the cache is invalidated and a full recompute is triggered. Evaluated on four LIBERO benchmark suites with both OpenVLA and OpenVLA-OFT, Gated VLA-Cache improves reliability when blind caching hurts. On LIBERO-Goal and LIBERO-Long, it recovers over 100% of the lost accuracy while retaining 80% of the compute savings.

## 入库理由
- quality_score: 4
- category: infra
- tags: vla, kv-cache, on-device-ai, robotics, inference-optimization
- one_liner: Gated VLA-Cache 用动作置信度决定是否复用 KV cache，在省算力与可靠性之间加门控。

## Obsidian evidence excerpt
```markdown
-08-13/`

## 今日论文速报

今天 arXiv recent 覆盖 `cs.AI / cs.CL / cs.LG / cs.CV / cs.RO / cs.MA` 六个分类共 254 篇去重提交。本轮最有信号的方向是 **Agent 记忆与自演化基础设施**——多条线从不同角度在做同一件事：把"retrieve-only"换成"compile + skill + provenance"。`SkillZip / Muscle Memory / GeoForge / MAP-Graph / EvoMem` 形成今天的"memory 范式切换"主线；`Self-Evolving GUI Grounding` + `SPIEval` 把这条主线拉到 GUI/移动端；`ReRound / Gated VLA-Cache` 提供 on-device 推理的量化与缓存路径。安全侧一条新的攻击面：`Trajectory Backdoor Attack` 直接攻击 self-evolving skill 的可信演化管道。

1. **SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure** — arXiv:2608.11079。把 self-evolving agent 累积的 skill 当成"typed contract"——名字/描述/工作流/工具契约/输出字段/例外规则——用 typed minimum description-length 目标一次性压缩：重复规则 state once at scope，重复动作序列 factor into shared procedure，例外保留为 explicit exceptions。Zip-on-Write 模式支持 incremental 演化不重放任务。压缩率高、保留 unique rare rules by construction。
   来源：https://arxiv.org/abs/2608.11079

2. **Muscle Memory for Agents: Compile not Merely Retrieve** — arXiv:2608.08995。主张把"反复出现的用户意图"编译成 purpose-built specialist agent，而不是 retrieve-then-orchestrate。Harvest→Analyze→Augment→Evaluate 四阶段管线，从对话历史中分别挖出 behavioral pattern 和 task pattern，发出的 specialist 配 two-stage trigger matching。90 held-out scenario 上 specialist 触发时 88.9% 胜率，+2.05 personalisation gain，accuracy 损失仅 -0.28（1-4 scale）。
   来源：https://arxiv.org/abs/2608.08995

3. **GeoForge: Non-Parametric Self-Evolving Agents for Earth-Observation Reasoning** — arXiv:2608.10494。Training-free self-evolving 框架，把完成的轨迹压成结构化 nonparametric execution state——Workflow Graph Memory（全局操作顺序）+ Action-Level Experiences（局部纠错）+ Adapted Skill SOP（程序与数据约束）。执行、蒸馏、复用三段循环里 backbone LLM 不变。多个 geospatial benchmark 上同时拉高 task accuracy 和 tool-use trajectory quality。
   来源：https://arxiv.org/abs/2608.10494

4. **MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows** — arXiv:2608.10509。把 agent、source、memory、claim、action 全部建模成 typed execution graph：lineage tracing + permission-ineligible record exclusion + semantic similarity × multiplicative path trust reranking + risk-sensitive action gate。2,700 合成任务上 94.96% task success / 72.70% exact decision accuracy / 90.22% clea
```

## arXiv metadata / abstract
- arXiv id: 2608.10824
- authors: Zhijie Wu, Kento Kawaharazuka, Kei Okada
- published: 2026-08-11
- updated: 2026-08-11
- categories: cs.RO, cs.CV
- PDF: https://arxiv.org/pdf/2608.10824v1

Vision-Language-Action(VLA) models map camera images and language instructions directly to motor commands through a single autoregressive transformer. In real-time control, they still spend substantial compute recomputing key-value(KV) representations for visual tokens that barely change across neighboring frames. Recent work such as VLA-Cache reduces that cost by reusing KV states for visually static patches, but its policy relies only on observation-space heuristics and does not account for the model's own uncertainty. We propose Gated VLA-Cache, a lightweight, training-free extension that augments visual-similarity caching with neural introspection. The method monitors the logit margin between the top two predicted action tokens, a zero-cost confidence signal available during decoding. When the margin drops below a threshold, the cache is invalidated and a full recompute is triggered. Evaluated on four LIBERO benchmark suites with both OpenVLA and OpenVLA-OFT, Gated VLA-Cache improves reliability when blind caching hurts. On LIBERO-Goal and LIBERO-Long, it recovers over 100% of the lost accuracy while retaining 80% of the compute savings.
