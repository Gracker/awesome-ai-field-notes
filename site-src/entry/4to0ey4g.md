---
title: 'Investigating how Codex context compaction works'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# Investigating how Codex context compaction works

> AI 实践：Investigating how Codex context compacti

🔗 [原文链接](https://x.com/Kangwook_Lee/status/2028955292025962534) | @Kangwook_Lee |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`codex` `system-prompt` `context-management` `open-source`

---

## English

Investigating how Codex context compaction works:

Hard to say. Maybe the encrypted blob carries something more than what this simple experiment can reveal, e.g. something specific about how tool results are compacted and restored. But I didn't bother to test further.

The question asks why Codex CLI uses two entirely different compaction paths - local LLM for non-codex models, encrypted API for codex models - when the underlying prompts are nearly identical, and why encrypt the summary at all.

## 中文

探究 Codex 上下文压缩的原理：

这很难说。也许加密的数据包包含了这个简单实验无法揭示的更多信息，比如工具结果如何被压缩和恢复的具体细节。但我不费心进一步测试了。

问题询问为什么 Codex CLI 使用两种完全不同的压缩路径——对于非 Codex 模型使用本地 LLM，对于 Codex 模型使用加密 API——当底层提示几乎相同时，以及为什么要加密摘要。

这个分析揭示了 Codex 在处理不同模型时的差异化策略，以及对数据完整性和安全性的考虑。
