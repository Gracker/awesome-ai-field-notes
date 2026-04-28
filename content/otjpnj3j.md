# Claude Code 缓存深度指南：如何让 Pro/Max 套餐多干 3-5 倍活

> 作者: @MinLiBuilds
> 原文链接: https://x.com/MinLiBuilds/status/2041178722230030384
> 评分: 5 | 平台: x.com | 语言: zh

---

## 核心原理

多轮对话中"慢"的部分不是 AI 在思考，而是重新处理完整历史。Claude 使用 KV 缓存技术，将历史 token 的 Keys + Values 存储在内存中。首次消息后跳过了 90%+ 输入的重计算，速度提升 100 倍，成本也大幅下降。

## 省钱核心机制

一个长 session 复用缓存，只有新内容按全价计算。新 session 或中途变更（切换工具、换模型、编辑 CLAUDE.md）会导致缓存失效，强制全量重处理，prompt prepare 阶段会很贵。

命中缓存后，input 价格是原来的 10%。

## 实操技巧

1. **尽量一个 session 做完一件事**：避免频繁 new session 或 /clear
2. **提前配好一切**：CLAUDE.md、MCP 工具、模型选择提前配好，不要中途修改
3. **用 /btw 插问题**：长任务用 /btw 插问题，不要开新窗口
4. **续命 TTL**：下班前半小时不要切模型，午饭前发一句"ok"续命 TTL（Pro/Max 1h 缓存）
5. **少用 sub-agent**：sub-agent 成本高，能用 Grep/Glob 工具就别起 agent

## Compact 的坑

小于 100K 时基本别用 compact，虽然官方做了 caching 优化，但仍然会触发 prepare prompt 开销。宁可让 session 自然长一点，缓存命中更划算。session 超过一兆，Claude 会自动 compact。

## 续命技巧

用 `/loop` 指令可以续命缓存，2 小时内的循环是赚的。

## 缓存清除策略

高峰期建议使用 TTL 租约机制而非 LRU，可以提高缓存命中率。虽然会提高缓存写入成本，但能提高缓存命中率。

> 网络一定要好，网络有问题时经常重试很重要。

---

*💬 1511 likes | 305 retweets | 中文推文thread精华整理*