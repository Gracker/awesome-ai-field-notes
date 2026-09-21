# Two techniques for working with System One models

- **ID**: aa617abc
- **原文链接**: https://seangoedecke.com/two-techniques-for-working-with-system-one-models
- **作者**: Sean Goedecke
- **日期**: 2026-09-18
- **分类**: agents
- **来源类型**: article
- **标签**: system-one-models, jev, tiered-goals, tournament-sampling, llm-decision-loop
- **质量评分**: 4/5
- **抓取时间**: 2026-09-21T23:30Z

---

## 中文摘要

Goedecke 9 月 18 日实战心得，给 Jev 这类 System One 决策模型两点技巧tiered goals：Qwen3-8B 跑 Doom 实验里 200ms 一 pass 太碎，模型只会按住 shoot 键乱撞；改成 10s 战略目标 / 5s 战术目标 / 1s 动作目标分层之后行为立刻像人tournament sampling：Jev 单次只能塞 255 候选，Wikiracing 一千多条链接灌不进去；改成两段，先 100 选 top再 top 选 top，模型只做相对判断就绕开绝对评分不准的问题原文给出 baseballscientific americanamateur astronomysun 三跳的具体路径示例

## English Abstract

Goedecke's September 18 hands-on post on Jev-style System One decision models offers two practical techniques. Tiered goals: a Qwen3-8B Doom agent running a 200ms decision loop just spammed the shoot key; switching to a 10s strategic / 5s tactical / 1s action split immediately produced human-like behavior. Tournament sampling: Jev's 255-candidate ceiling is too tight for Wikiracing's thousand-plus links, so he runs a two-stage prune-first-then-pick top-k where the model only does relative judgment, side-stepping absolute-score weakness. The post includes a worked three-hop path (baseball scientific american amateur astronomy sun).

## 为什么值得关注

Jev 实战 2 招：tiered goals 解决反应过快乱撞tournament sampling 解决 255 候选天花板

## Obsidian 证据摘要

> 来源: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-09-21-AK-RSS-Digest（89源精选）.md + 对应 evidence-2026-09-21 文件
