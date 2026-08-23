# Claudette: Make Claude stop talking like a BuzzFeed article (NoBuzz)

- **ID**: 0dbbd03a
- **原文链接**: https://github.com/adnanakil/nobuzz/blob/main/README.md
- **作者**: adnanakil (GitHub)
- **日期**: 2026-08
- **分类**: coding
- **来源类型**: article
- **标签**: claude-code, skill, agent-tools, hackernews
- **质量评分**: 4/5
- **抓取时间**: 2026-08-23T12:30:00Z

---

## 中文导读

NoBuzz 是一个 Claude Code 技能 `/debuzz`（作者戏称 "Claudette"，又强调绝对不叫这个名字）：把 Claude 的上一条回复原封不动交给 Google Antigravity CLI（`agy`）里的 Gemini，翻译成正常人说话的英语，并逐字打印译文——因为让 Claude 自己"润色"译文，恰恰会把要删掉的腔调重新带回来。提供 colleague / manager / director 三种受众模式，曾登上 HN 首页（346 points / 232 comments，条目元数据）。

## 为什么值得关注

它回应的是 prompt 工程解决不了的问题：Claude 是好工程师，但说话像"给自己的 PR 做 TED 演讲"——什么都是 load-bearing assumption，什么都有第三点 kicker。这个技能承认提示词治不了根，改用诚实的工程手段：跨模型去腔调 + 逐字输出。Before/After 对比很典型：从"the retry logic isn't just a nice-to-have — it's the load-bearing assumption of the entire sync pipeline"变成"The sync pipeline's retry logic has three bugs. `syncQueue.ts:142` swallows `ETIMEDOUT` instead of re-queuing the job..."。对写作 agent 工具链的人来说，"verbatim 打印 + 明确标注的降级路径"是可复用的设计模式。

Grounding: 以下要点全部来自 GitHub README 原文：安装方式（`git clone` + `cp -r nobuzz/debuzz ~/.claude/skills/`）、依赖（Claude Code + Antigravity CLI，`agy` 需完成 Google Sign-In）、模式表（colleague 默认保留全部文件路径与代码块；manager 砍到约三分之一长度、无代码；director 三到五句话）、工作机制（写临时文件后 `agy -p "$(cat <file>)"`，因 agy headless 模式不读 stdin；agy 出错时直接显示真实错误，Claude 自己的重写只作为明确标注的 fallback）、MIT 许可证。HN 数据来自条目元数据。

## 关键信息

- 项目: adnanakil/nobuzz（MIT License）
- 形态: Claude Code skill，用法 `/debuzz [mode] [text]`；不带参数时翻译 Claude 的上一条回复，也响应 "say that in normal english" 这类自然语句
- 依赖: Antigravity CLI (`agy`)，安装后需运行一次完成 Google 登录
- 三种模式: colleague（默认，同内容、代码与路径完整、零表演）/ manager（发生了什么、为什么重要、下一步）/ director（3-5 句：结果、影响、诉求）
- 热度: HN 首页 346 points / 232 comments（条目元数据）

## English Summary

NoBuzz ships a Claude Code skill, `/debuzz`, that hands Claude's previous response to Gemini via Google's Antigravity CLI and prints the plain-English translation verbatim — because letting Claude tidy its own translation reintroduces the buzz. It offers colleague/manager/director audience modes, shows real `agy` errors instead of hiding them, and falls back to a clearly labeled Claude rewrite only when the CLI fails.

## 原文要点摘录

> Claudette is our solution to Claude being a great engineer with one incurable condition: it talks like it's delivering a TED talk about its own pull request.

> This skill accepts that no amount of prompting fully cures this, and does the honest thing instead: it hands the response to a different model... Claudette has pinky promised to print Antigravity's translation verbatim, because letting Claude "tidy up" the translation reintroduces exactly the voice being removed.

> **After (`/debuzz`, colleague mode):** The sync pipeline's retry logic has three bugs. `syncQueue.ts:142` swallows `ETIMEDOUT` instead of re-queuing the job. The backoff caps at 2 seconds, which is too low for mobile networks.

## Obsidian Notes

- 内容由 `opencli web read` 抓取 GitHub README 全文生成（2026-08-23）。
- 中文导读与价值判断锚定在 README 原文的机制描述、安装/依赖、模式表与 before/after 示例上；HN 数据引自条目已有摘要，未新增未经证实的细节。
