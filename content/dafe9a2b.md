# The Economic Benefit of Refactoring (Thoughtworks/Martin Fowler)

> Source: https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html
> Author: Giles Edwards-Alexander
> Date: 2026-07-30

## Summary (Chinese)

在纯 agent 写出的约 15 万行应用上，大文件拆开后同类改动输入 token 掉 83%。省的不是代码量，是 agent 成功定位到最小相关文件集合的概率。实验设计精巧：每次重构后用全新 agent 执行完全相同的 prompt，避免了人类工程师的学习效应。Claude 不擅长自己规划重构，关键步骤靠人引导。

## Summary (English)

On a ~150K LOC app written entirely by agents, splitting large files reduced input tokens for similar changes by 83%. The savings come not from code reduction but from agent successfully locating the minimal relevant file set. Experiment design: fresh agent executes identical prompt after each refactoring step, eliminating human learning effects. Claude doesn't self-plan refactoring well; key steps need human guidance.

## One-liner

大文件拆开后同类改动输入 token 掉 83%，省的是定位成本

---

*Imported from Obsidian digest notes on 2026-08-01. Content grounded in fetched source metadata via opencli.*
