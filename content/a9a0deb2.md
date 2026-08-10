---
id: a9a0deb2
title: "Addy Osmani 2026 LLM coding workflow: spec-first, chunked, human-supervised"
url: https://x.com/yibie/status/2085536770758996033
source: {"platform": "x", "author": "@yibie (Addy Osmani)", "original_date": "2026-08-10"}
quality_score: 5
tags: ["llm-coding", "workflow", "software-engineering", "spec-driven", "code-review"]
fetched_at: 2026-08-10T15:30:00+08:00
fetch_method: opencli twitter thread + archived X article
---

# Addy Osmani 2026 LLM coding workflow

> Source: https://x.com/yibie/status/2085536770758996033
> Author: @yibie (translating Addy Osmani's original)

## Summary

Google engineering lead Addy Osmani shares his 2026 LLM coding workflow: treat the model as a powerful pair programmer that needs clear direction, context, and supervision rather than autonomous judgment. Key principles: (1) spec before code -- brainstorm requirements with AI into a spec.md, then generate a step-by-step plan; (2) break work into small iterations -- one function, one bug, one feature at a time; (3) provide full context -- show relevant code, constraints, documentation; (4) choose the right model per task, switch when stuck; (5) never blindly trust output -- test and review everything; (6) commit frequently with clear messages as save points; (7) customize AI behavior with rules files (CLAUDE.md, GEMINI.md) and examples; (8) leverage CI/CD and automated testing as amplifiers. Core thesis: classic software engineering disciplines become more important, not less, when AI writes half your code.

## 摘要中文

Google 工程主管 Addy Osmani 分享 2026 年 LLM 编码工作流：先写规格再写代码，把任务拆成小块，提供充分上下文，选对模型，永不盲信 AI 输出，频繁提交当存档点，用规则文件定制 AI 行为，以 CI/CD 和自动化测试作为放大器。核心论点：经典软件工程纪律在 AI 写一半代码时不是过时了，而是更重要了。

> Evidence: Obsidian archived at `X 文章/2026-08-10-1200-yibie-Addy Osmani 的 2026 L.md`
