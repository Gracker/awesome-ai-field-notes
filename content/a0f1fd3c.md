---
id: a0f1fd3c
title: Tell Agents the Why, Not Just the How
url: https://seangoedecke.com/tell-agents-the-why/
source: seangoedecke.com 博客 + Obsidian AK-RSS-Digest
added_date: 2026-09-15
---

# Tell Agents the Why, Not Just the How

## 博客要点 (中文)

Sean Goedecke 2026-09-15 工程短文。把 spec 换成「目标 + 优先级」：现代模型错的时候不是看不懂，是猜错了用户的优先级，所以他写 agent prompt 时有意识地分配一半篇幅讲「我对 bug、可观测性、贴合既有代码、性能的相对权重」。样本：启动 Deckard（屏蔽 AI 生成内容的浏览器扩展）的 prompt——明确告诉模型这是个人项目、本机优先、希望 Runpod 跑长实验，模型主动挑 Gradient 模型替代他原本列的 EditLens，还建议走 native messaging。顺带埋了一条对「万能 prompt」内容的反对意见：花心思找黄金 prompt 是新时代的迷信。

## Key claims (English)

Sean Goedecke's 2026-09-15 engineering short reframes the agent spec as 'goals + priorities'. The failure mode of modern models is not misreading the prompt but guessing the user's priorities wrong — so he devotes half of every agent prompt to spelling out the relative weight he places on bugs, observability, fit-with-existing-code, and performance. He shares the prompt he used to launch Deckard (a browser extension that masks AI-generated content) as a worked sample: by labeling the project as personal, local-first, and preferring long-running experiments on Runpod, the model picked Gradient as a substitute for his originally listed EditLens and recommended going through native messaging. The piece also sneaks in an objection to 'universal prompts' — hunting for a golden prompt is a new-era superstition. Reads like an experienced person disassembling their own workbench, not a mystical post.

## Obsidian 证据摘录

> 「把 spec 换成『目标 + 优先级』。现代模型错的时候不是看不懂，是猜错了用户的优先级，所以他写 agent prompt 时有意识地分配一半篇幅讲『我对 bug、可观测性、贴合既有代码、性能的相对权重』。他贴出自己用来启动 Deckard（屏蔽 AI 生成内容的浏览器扩展）那一段 prompt 作样本……文章还顺带埋了一条对『万能 prompt』内容的反对意见：花心思找黄金 prompt 是新时代的迷信。」——OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-09-15-AK-RSS-Digest（89源精选）.md L37-39

## 链接

- 原文：https://seangoedecke.com/tell-agents-the-why/
- AK-RSS-Digest：OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-09-15-AK-RSS-Digest（89源精选）.md
