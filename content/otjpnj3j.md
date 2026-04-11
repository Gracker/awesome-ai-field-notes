# 搞懂缓存机制，从Gemma4到Claude Code省80%Token

从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。

## 核心概念

- **KV 缓存**：Transformer 注意力机制中的 Key/Value 缓存
- **Decoder-only 架构**：可以缓存历史 token 的 KV
- **Claude Code 缓存实现**：Anthropic 的精密缓存工程
- **Token 优化**：同样的套餐多撑 3-5 倍

## 实验方法

从本地 Gemma 4 实验出发，通过实际测试验证 KV 缓存的效果。

## 关键发现

理解缓存机制后，可以显著提升 token 使用效率。
