---
title: "2026-06-09 · AI 代码生成与评测基准"
date: 2026-06-09
topic: AI
original_author: "每日论文精读（AI）"
source_platform: "manual"
original_url: null
---

# 2026-06-09 · AI 代码生成与评测基准

> 今日关键词：**"AI code generation evaluation benchmark"**（索引 2/24）。
> 核心叙事：**经典基准 → 有效性危机 → 新一代基准 → 不确定性新工具 → 工程落地清单**。

## 一、TL;DR

1. **代码基准正经历"有效性危机"** — HumanEval 严重污染，SWE-Bench Verified 也出现 76% 文件命中 vs 53% 域外的记忆迹象。([SWE-Bench Illusion, 2025](https://arxiv.org/abs/2506.12286))
2. **新一代基准主动反污染：长时程 + 持续更新 + 私域仓库** — [SWE-Bench Pro](https://arxiv.org/abs/2509.16941)（1,865 × 41 商业仓库）、[SWE-bench-Live](https://arxiv.org/abs/2505.23419)（季度更新 + 自动 pipeline）、[LiveCodeBench Pro](https://arxiv.org/abs/2506.11928)（Olympiad 级，hard 0% pass@1 无工具）。
3. **评测指标也要升级** — `pass rate` 之外还需 `retry-free coverage`（差距 17.8 pp）+ **functional entropy**（11/15 AUROC 第一）作为「是否接受生成」的二次过滤。

## 二、四大奠基基准

| 基准 | 出处 | 关键贡献 | 已知局限 |
|------|------|----------|----------|
| [HumanEval](https://arxiv.org/abs/2107.03374) | OpenAI / Codex, 2021 | 164 题 + `pass@k` | 严重污染；单函数 |
| [SWE-bench](https://arxiv.org/abs/2310.06770) | Princeton, ICLR 2024 | 2,294 issue 修复 + 隐藏测试 | 12 仓库；开始被记住 |
| [LiveCodeBench](https://arxiv.org/abs/2403.07974) | MIT/UCB/Cornell/CMU, 2024 | 持续更新 + **release-aware** | 仅竞赛题 |
| [BigCodeBench](https://arxiv.org/abs/2406.15877) | BigCode, NeurIPS 2024 | 1,140 × 7 域 × 139 库 | 评测贵；非 agentic loop |

## 三、2025–2026 新一代基准

| 基准 | 关键词 | 数字 |
|------|--------|------|
| [SWE-Bench Pro](https://arxiv.org/abs/2509.16941) | 企业级长时程 | 1,865 题 / 41 仓库 / commercial split |
| [SWE-bench-Live](https://arxiv.org/abs/2505.23419) | 持续更新 | 1,319 题 / 93 仓库 / 自动化 pipeline |
| [LiveCodeBench Pro](https://arxiv.org/abs/2506.11928) | Olympiad 级 | hard 0% pass@1（无工具） |
| [Asuka-Bench](https://arxiv.org/abs/2606.05920) | 多轮 Web 开发 | 50 题 / 3 轮后最强 52% |
| [CodegenBench](https://arxiv.org/abs/2606.04023) | HPC 跨架构 | x86 正常 / 专用架构 5–10× 慢 |
| [SWE-InfraBench](https://arxiv.org/abs/2606.05249) | IaC (AWS CDK) | Sonnet 3.7 34% / R1 24% |

## 四、稳定性与 UQ 新方法

- **[Accuracy, Stability, and Repeated-Run Reliability](https://arxiv.org/abs/2606.00920)**：16,000 次评测证明 `pass rate` 高估 `retry-free coverage` 17.8 pp，**中段模型排名会反转**。
- **[Functional Entropy](https://arxiv.org/abs/2605.28500)**：用 LLM 判功能等价代替 NLI，AUROC 11/15 第一 —— 可直接接入生产代码 agent 的二次过滤。

## 五、对 AI 工程实践的整合建议

> 受众：**AI 从业者 / 开发者**；目标：**AI 工程实践**。

### 选型时该问的 5 个问题
1. 有没有报 release-aware / held-out 协议？
2. 有没有报告 retry-free coverage？
3. 测的是 single-turn 还是 multi-turn？
4. 测的是"实现"还是"算法推理"？
5. 测的是不是工业代码（IaC / 嵌入式 / 私有库）？

### 内部代码 Agent 的最小可行栈
```
Pass@1..5 → Functional Entropy 过滤 → Retry-free Coverage 评估
                    ↑                       ↓
                反馈循环 + 季度 Live 复评 ←─┘
```

### 三个反直觉提示
- **别再追 HumanEval 数字了**（95%+ 之后边际信息量近 0）。
- **5 次重跑比 5 道新题更有价值**（稳定性比广度更敏感）。
- **让 agent 看反馈 + 让评测看 agent 用反馈**（Asuka-Bench 范式）。

## 六、精选论文清单（10 篇）

### 奠基经典（2021–2024）
1. [HumanEval (Codex)](https://arxiv.org/abs/2107.03374) — 1.1
2. [SWE-bench](https://arxiv.org/abs/2310.06770) — 1.2
3. [LiveCodeBench](https://arxiv.org/abs/2403.07974) — 1.3
4. [BigCodeBench](https://arxiv.org/abs/2406.15877) — 1.4

### 基准有效性危机（2025）
5. [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286) — 2.1
6. [Accuracy, Stability, Repeated-Run Reliability](https://arxiv.org/abs/2606.00920) — 2.2

### 新一代基准（2025–2026）
7. [SWE-Bench Pro](https://arxiv.org/abs/2509.16941) — 3.1
8. [SWE-bench-Live](https://arxiv.org/abs/2505.23419) — 3.2
9. [LiveCodeBench Pro](https://arxiv.org/abs/2506.11928) — 3.3
10. [Asuka-Bench](https://arxiv.org/abs/2606.05920) — 3.4
11. [CodegenBench](https://arxiv.org/abs/2606.04023) — 3.5
12. [SWE-InfraBench](https://arxiv.org/abs/2606.05249) — 3.6

### 方法论
13. [Functional Entropy](https://arxiv.org/abs/2605.28500) — 4.1

## 七、明天预告
**2026-06-10 · Query Index 3 · "retrieval augmented generation RAG"** — 经典 RAG、Agentic RAG、GraphRAG、长上下文 vs RAG 之争、RGB / RAGAS / HotpotQA 评测、2025–2026 RAG 工程化。

---
*This content was automatically extracted and processed by OpenClaw daily intake pipeline*
