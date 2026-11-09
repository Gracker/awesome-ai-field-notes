# Goodbye Claude, Hello Pi

- **ID**: e66f4eea
- **来源**: https://caleb.software/posts/claude-to-pi.html
- **作者**: Caleb (caleb.software)
- **发表**: 2026-09-21
- **证据**: curl 抓取正文（2026-11-09）；HN top 发现（score 673）；原文 2026-09-21 发布

## 原文摘录

> I've been a longtime Claude Code user... I've finally decided to retire it as my main coding harness and migrate my development setup to use Pi instead. Someone at Anthropic must've caught wind... just a day after making my decision, they announced Claude Code would finally start supporting AGENTS.md files... too little, too late. ... you can only have one session 'connected' to the IDE at a time. If you open a second tab to start another task while the first one works, it can't receive the text selection events... reported at least as far back as December 2025 and closed as a duplicate of a totally unrelated bug. ... there have been 244 releases to Claude Code this year.

## 中文要点

一位长期 Claude Code 用户宣布转投 Pi 作为主力编码 harness（HN 673 分）。导火索是 CLAUDE.md/AGENTS.md 双格式负担——他决定离开次日 Anthropic 才宣布支持 AGENTS.md，"太迟了"。具体槽点：同时只能一个会话连接 IDE，第二个标签页收不到选区上下文（2025 年 12 月有人报告、被当无关 bug 关闭）；VSCode GUI 扩展一半斜杠命令失效、无自定义状态栏、并发子代理输出混排；今年 244 个版本，功能速度远超质量与稳定性，反复弄坏个人配置。信号：个人开发者的 harness 切换成本低，DX 回退会复利。

## Field Notes

- 个人开发者 harness 切换成本低：一年用户因 DX 细节（IDE 单会话、GUI 扩展质量）整体迁移
- 功能速度与稳定性的失衡是流失主因：244 个版本/年，企业向功能与个人工作流冲突
