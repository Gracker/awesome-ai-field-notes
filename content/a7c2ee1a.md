# Storing the Gemma 4 K=V Cache Once: Exact Global-KV Memory Savings in a Paged Serving Engine with Unchanged Attention Kernels

- Source: https://arxiv.org/abs/2611.23035
- Author: unknown
- Published: 2026-11-17
- Intake: 2026-11-19 evening (daily-intake-evening, openclaw)
- Evidence: /Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/OpenClaw定时任务/论文流水线/2026-11-19-论文流水线.md

## 中文摘要
Gemma 4 31B 的全局注意力层里 K 和 V 实为同一行数据：value 是归一化 key 投影，key 只在四分之一维度转 RoPE，但开源 serving 引擎仍各存完整 key/value。作者只存一行 640 值（实数运算精确无损），让未改动的 paged attention kernel 经两个重叠跨步视图分别读作 key/value cache。vLLM 原型输出与逐位仿真一致，32K-64K token 时每请求稳态解码 KV 内存降到 1/1.34-1.40，16K prompt 每步解码吞吐 1.38 倍；代价是 eager 单步慢 4-9%。

## English Summary
In Gemma 4 31B's global attention layers, K and V are the same underlying row: value is the normalized key projection, key is the value scaled by a fixed weight with RoPE on a quarter of its dimensions. Checked open serving engines still store full separate K and V (1,024 values per KV head and token). The paper stores one 640-value row, exact in real arithmetic, and an unchanged paged-attention kernel reads it as key and value caches through two overlapping strided views. In a vLLM prototype with the 16-bit 31B model, outputs are bit-identical to emulated stock arithmetic (2 of 432 final answers differ, within run noise); steady per-request decode KV memory falls 1.34-1.40x at 32K-64K tokens, and decode throughput rises 1.38x for a 16K prompt on a dual-A100 setup, at 4-9% slower eager single steps with equal batch.

## Abstract (arXiv)
In the global attention layers of Gemma 4 31B, the value is the normalized key projection, and the key is the value scaled by a fixed weight, with rotary position encoding on one quarter of its dimensions. The Gemma 4 report states that this design reduces the global KV cache by up to 37.5%, but the open serving engines that we checked still store a full key and a full value: 1,024 values per KV head and token. We store one 640-value row instead, exact in real arithmetic, and an unchanged paged attention kernel reads it through two overlapping strided views as its key cache and its value cache. In a vLLM prototype with the 16-bit 31B model, the outputs are bit-identical to an emulation of the same arithmetic on the stock cache, 2 of 432 final answers differ from the stock engine (within its run-to-run noise), and the steady decode KV memory per request falls by a factor of 1.34 to 1.40 at 32K to 64K tokens. On a prefill/decode pair of two A100 GPUs with NIXL transfer and CPU offload, a decode engine with a full 15 GiB pool ran 1.38 times the stock decode tokens per step for 16K-token prompts (repeated to 0.06%) and 1.24 times for 8K-token prompts; a model of the vLLM block pool predicted both ratios to within 1% (the engine was 0.7% to 0.9% higher) and matched the change between them. The eager decode throughput rose by 1.30 and 1.11 times, and on this path the compact engine gave the same output tokens as the emulation for 8 prompts at batch 1. The run-time prototype makes an eager step 4% to 9% slower at equal batch, and the method does not yet stack with an 8-bit KV cache at the default scale.
