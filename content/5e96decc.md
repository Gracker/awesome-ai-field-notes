# Use the built-in GELU, don't roll your own!

- **ID**: 5e96decc
- **原文链接**: https://www.gilesthomas.com/2026/08/built-in-gelu
- **作者**: Giles Thomas
- **日期**: 2026-08-20
- **来源类型**: blog
- **标签**: pytorch, training, performance, gelu, tutorial
- **质量评分**: 3/5
- **抓取时间**: 2026-08-20T15:44:49Z

---

## 中文导读

同一份代码、同一张 RTX 3090 训练 GPT-2 small 风格模型，只把 Raschka 教材里手写的 GELU 换成 PyTorch 内置 nn.GELU()，吞吐从约 21,000 tokens/sec 涨到 25,000，提升 20%；tanh 与 exact 两种近似表现一致（25,134 对 25,142 tps）。12 层模型里 GELU 占了约 17% 训练时间。作者此前以为 JAX 比 PyTorch 快（24,000 对 21,000 tps），根因其实是手写 GELU 的 Python 层开销吃掉了 AMP 优势。Raschka 在 X 补充：坚持 tanh 近似是为了兼容 OpenAI 预训练权重。给 from-scratch 训练者一个零成本 20% 加速。

## 为什么值得关注

换掉手写 GELU 就白拿 20% 训练吞吐：from-scratch LLM 训练的低成本加速样本

## 原文摘录 (English Excerpt)

The headline numbers: the same code, training the same model on the same data, ran at about:

-   21,000 tokens per second using the hand-rolled GELU from [Sebastian Raschka](https://sebastianraschka.com/)'s book "[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)".
-   25,000 tokens per second using PyTorch's built-in GELU with no arguments.
-   25,000 tokens per second using the built-in GELU with `approximate="tanh"`, which uses the same maths as Raschka's version under the hood.

That's a 20% increase in throughput for both of the built-in versions -- definitely nothing to be sneezed at.

And what is particularly interesting is that there aren't that many GELUs going on -- it's a GPT-2 small-style model, with 12 layers. So that's 12 GELUs handling tensors shaped `(batch_size, seq_len, 4 * d_emb)`, which is `(6, 1024, 3072)` for my training setup. Given that the rest of the model is doing all of the normal full attention stuff for GPT-2, it's _really_ surprising that the GELUs alone must have been taking up so muc

## Obsidian 证据

- 来源 digest: AK RSS Digest 2026-08-20（2026-08-20，评分 8.2）
- 原文经 opencli web read / opencli arxiv paper 抓取核对，关键数字与摘要均锚定抓取内容。
