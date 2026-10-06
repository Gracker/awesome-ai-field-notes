# Research: Qwen3.8 27B addition in words

> Intake entry · 2026-10-06 · awesome-ai-field-notes

- **URL**: https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/
- **Source**: blog · Simon Willison · 2026-10-04
- **Category**: models
- **Tags**: evaluation, reasoning, quantization, local-models, benchmark
- **Quality Score**: 4

## 中文导读

两年前 Colin Frasier 用 GPT-4o 做过“把加法答案写成英文单词”的实验，正确率随位数增长崩塌。Simon Willison 在 DGX Spark 上用本地量化 Qwen3.8-27B-Q4_K_M 复刻，并把实验做成完全可控：13×13 位数组合、每格 30 个固定样本、共 5070 题、禁用推理。

结果分两层。禁用推理时数字正确率 23.57%（1195/5070），1-3 位数 97.04%，10-13 位数跌到 6.44%，但格式合规率高达 96.17%——模型几乎总在输出合法英文单词，只是算错。打开 medium 推理后只跑 169 题试点（每格 1 采样，每格非 100% 即 0%），167 题正确，热图几乎全蓝；推理 trace 显示模型把数位对齐、从右往左逐位相加并标注进位。结论：本地 27B 量化模型在没有任何工具调用的情况下，能靠链式推理跨过“把大数和写成英文单词”的组合障碍——reasoning_effort 是这类约束型任务的实际开关，而不是模型本身“会不会算术”。

## 为什么值得关注

## 关键信息

- 硬件/模型：DGX Spark · Qwen3.8-27B-Q4_K_M.gguf（本地量化）
- 设置：13×13 位数网格 × 30 固定对 = 5070 题（禁用推理）；medium reasoning 试点 169 题（每格 1 采样）
- 无推理：23.57%（1195/5070）；1-3 位数 97.04% → 10-13 位数 6.44%；格式合规 96.17%
- medium reasoning：167/169 正确，热图几乎全蓝
- 推理 trace：数位对齐、右到左逐位相加、进位标注（报告 gist 含完整 trace）
- 原实验：Colin Frasier（Bluesky，GPT-4o，两年前）
- 复现材料：github.com/simonw/research/tree/main/qwen38-addition-in-words

## One-liner

关推理 23.57%、开推理 167/169：把 reasoning_effort 当约束任务的实际开关用

## English Summary

Simon Willison replicated Colin Frasier's GPT-4o experiment on a DGX Spark with locally quantized Qwen3.8-27B-Q4_K_M: add two positive integers, answer solely in English words. 5,070 reasoning-disabled cases: 23.57% numeric accuracy (97.04% at 1-3 digits, 6.44% at 10-13 digits) despite 96.17% format compliance. A 169-case medium-reasoning pilot scored 167/169, traces showing column-aligned right-to-left addition with carries. Chain-of-thought alone clears the compositional barrier; reasoning_effort is the practical switch for constraint tasks.

## 原文摘录（节选）

A benchmark tested whether the local `Qwen3.8-27B-Q4_K_M.gguf` model could add positive integers and express exact results solely in English words, using 5,070 reasoning-disabled cases and a paired 169-case comparison with medium reasoning. Without reasoning, it achieved 23.57% numeric accuracy, with performance dropping from 97.04% for one- to three-digit operands to 6.44% for ten- to thirteen-digit operands, despite 96.17% format compliance.

[reasoning trace] "Wait, let me redo this more carefully. 4,299,366,105,622 + 6,088,794,067,970. Let me align them: [...] Adding from right to left: Position 1 (units): 2 + 0 = 2. Position 2 (tens): 2 + 7 = 9. Position 3 (hundreds): 6 + 9 = 15, write 5, carry 1."

It got the right answer in 167 out of 169 attempts, and since these were one-shot I'm confident a second run would produce different results here.

热图：![no-reasoning](https://static.simonwillison.net/static/2026/qwen-words-no-reasoning.webp) · ![reasoning](https://static.simonwillison.net/static/2026/qwen-words-reasoning.png) · ![GPT-4o 原实验](https://static.simonwillison.net/static/2026/colin-frasier-grid.webp)

---

> 注：原文全文于 2026-10-06 由 AK-RSS digest 证据抓取留存（evidence-2026-10-06/02，6299 bytes），数字均经全文核对。
