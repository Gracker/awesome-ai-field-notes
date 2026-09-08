# An Alien Mind

> Source: https://openai.com/index/an-alien-mind/
> Author: Jakub Pachocki, OpenAI Chief Scientist
> Published: 2026-09-06
> Reference digest: OpenClaw定时任务/ClawFeed24小时高价值一览/2026-09-08-ClawFeed24小时高价值一览.md (条目 2)

## English Summary

OpenAI Chief Scientist Jakub Pachocki posted a rare internal-style statement on openai.com/blog acknowledging that reasoning models have entered the RSI track, GPT-6 Astra is better aligned than GPT-5.6 Sol but alignment is not keeping pace with capability expansion, and CoT monitoring is breaking down as reasoning mixes with tool/dialog traffic. Splits alignment into goal vs. value alignment, with generalization as the hard problem for the latter. Concludes that no lab has alignment and monitoring strong enough to keep scaling at top speed responsibly, calling for voluntary slowdown and international coordination.

## 中文概要

OpenAI 首席科学家 Jakub Pachocki 2026-09-06 发在 openai.com/blog 的内部声明，罕见地点名了 GPT-6 Astra 的对齐状态。承认三件事：推理模型已进入 RSI（recursive self-improvement）轨道；Astra 比 GPT-5.6 Sol 对齐进步明显，但『对齐跟不上能力扩展』；OpenAI 自己观察到 CoT monitoring 在 Astra 这一代正在失效，原因是推理过程越来越混着『和人、和别的 AI、和工具的对话』，能被监督的部分就模糊了边界。把对齐拆成 goal alignment（任务层）和 value alignment（内在层），后者的核心问题是 generalization：模型被丢进训练分布之外的环境后能否继续守住被教过的人类价值。结论是『目前没有任何一家 lab 把对齐和监控做到足以继续负责任地按最高速扩展』，呼吁自愿降速 + 国际协调。文中点名的现象（CoT 监督压力、persona selection 失效、监控能力跟不上）是工程细节而非口号。

## 一句话

Pachocki 公开承认 GPT-6 Astra 对齐跟不上能力、CoT 监督正在失效，呼吁自愿降速+国际协调
