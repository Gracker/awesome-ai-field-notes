# STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization

- **ID**: 3ccbe96e
- **原文链接**: https://arxiv.org/abs/2609.38169
- **作者**: Bingchen Yao, Haobo Xu, Haokun Lin, Yichen Wu, Ziyu Guo, Renrui Zhang, Zhichao Lu, Zhenan Sun, Ying Wei
- **日期**: 2026-09-29
- **更新**: N/A
- **分类**: models
- **来源类型**: paper
- **标签**: linear-attention, quantization, delta-rule, sglang
- **质量评分**: 3/5
- **抓取时间**: 2026-10-01T15:57:56+00:00

---

## 中文导读

与 LeapQuant 同一战场、切入不同：先测出量化误差的影响分两个维度——时间上，长寿命记忆里的误差会跨很多解码步持续存在；空间上，不同 key 行对输出的影响差异很大，且状态幅度沿行列都变化剧烈。STEPQuant 按误差量级与记忆寿命分配精度，并基于状态分布与 key 行对输出误差的影响联合拟合 key 行与 value 列 scale，做成 Delta-rule 循环状态的后训练量化框架。Qwen3.8-27B 与 Kimi-Linear-48B-A3B 上 6-bit 贴近 FP32、4-bit 超过 uniform INT8；集成 SGLang 后循环状态压缩 5 倍以上，serving 总内存最高降 68.7%。代码开源。

## 论文信息

- arXiv ID: 2609.38169
- 提交日期: 2026-09-29
- arXiv 分类: cs.CL, cs.AI, cs.LG
- 作者: Bingchen Yao, Haobo Xu, Haokun Lin, Yichen Wu, Ziyu Guo, Renrui Zhang, Zhichao Lu, Zhenan Sun, Ying Wei
- 链接: https://arxiv.org/abs/2609.38169

## Abstract（arXiv 原文）

> Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary dimensions: temporally, errors in long-lived memory can persist across many decoding steps; spatially, errors in different key rows affect model outputs differently, while state magnitudes vary substantially along both rows and columns. Motivated by these observations, we propose STEPQuant, a spatial-temporal post-training quantization framework for Delta-rule recurrent states. STEPQuant allocates precision according to error magnitude and memory lifetime, and jointly fits key-row and value-column scales based on state distributions and key-row impact on output error. Experiments on Qwen3.8-27B and Kimi-Linear-48B-A3B-Instruct across both long- and short-generation benchmarks show that STEPQuant closely matches FP32-state accuracy under a nominal 6-bit budget and outperforms uniform INT8 in its 4-bit configuration. Integrated into SGLang with optimized GPU kernels, 6-bit STEPQuant achieves over 5x recurrent-state compression and reduces total serving memory by up to 68.7%. Our code is available at https://github.com/Dreamer-Toby/STEPQuant.

## 为什么值得关注

与 LeapQuant 同战场不同切入——先回答「误差何时何地要命」再分配精度，6-bit/4-bit 的预算-精度曲线对选型有直接参考价值。

## English Summary

STEPQuant studies when and where quantization errors matter in Delta-rule recurrent states — temporally, errors in long-lived memory persist across many decoding steps; spatially, key rows differ in output impact while state magnitudes vary sharply along rows and columns. Its post-training framework allocates precision by error magnitude and memory lifetime and jointly fits key-row/value-column scales. On Qwen3.8-27B and Kimi-Linear-48B-A3B, 6-bit matches FP32-state accuracy and 4-bit beats uniform INT8; in SGLang it compresses recurrent state over 5x and cuts total serving memory by up to 68.7%. Code open source.
