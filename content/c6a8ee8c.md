# If your repo has both AGENTS.md and CLAUDE.md, Claude Code may be ignoring AGENTS.md

- **ID**: c6a8ee8c
- **原文链接**: https://www.reddit.com/r/ChatGPTCoding/comments/1xtlwh6/if_your_repo_has_both_agentsmd_and_claudemd/
- **作者**: u/Nvmtag (r/ChatGPTCoding)
- **日期**: 2026-11-11
- **更新**: N/A
- **分类**: coding
- **来源类型**: article
- **标签**: claude-code, agents-md, claude-md, memory, instructions, reddit
- **质量评分**: 3/5
- **抓取时间**: 2026-11-13T15:45:09+00:00

---

## 中文导读

u/Nvmtag 在已有 AGENTS.md（Cursor/Codex 用）旁加了短 CLAUDE.md 后，Claude Code 会话看不到共享命令和 ask-first 清单。对照官方 memory 文档：默认只有在没有 CLAUDE.md/.claude/CLAUDE.md/CLAUDE.local.md 时才读 AGENTS.md。一行修复是在 CLAUDE.md 首行写 @AGENTS.md（真 import），「请也读一下 AGENTS.md」这类句子不算；用 /memory 或 /context all 验证两份文件都被加载。评论区补 symlink 与单源生成配置两种做法。

## 为什么值得关注

指令文件不会自动合并：CLAUDE.md 在场时 AGENTS.md 被跳过，@import 才是真引用——多工具共享规则要显式设计加载顺序。

中文导读与价值判断锚定在条目已有摘要与抓取到的原文/摘要、作者、日期与分类信息上；未补充源材料之外的实验细节。

## 关键信息

- 标题：If your repo has both AGENTS.md and CLAUDE.md, Claude Code may be ignoring AGENTS.md
- 作者：u/Nvmtag (r/ChatGPTCoding)
- 链接：https://www.reddit.com/r/ChatGPTCoding/comments/1xtlwh6/if_your_repo_has_both_agentsmd_and_claudemd/
- 发布时间：2026-11-11
- 关联标签：claude-code, agents-md, claude-md, memory, instructions, reddit

## English Summary

After adding a short CLAUDE.md beside an existing AGENTS.md used for Cursor and Codex, u/Nvmtag found Claude Code sessions no longer saw the shared commands and ask-first list. Claude Code's memory docs: by default AGENTS.md is read only when no CLAUDE.md, .claude/CLAUDE.md or CLAUDE.local.md exists in the working directory or above. The one-line fix is putting @AGENTS.md on line 1 of CLAUDE.md - an actual import; a sentence saying "please also read AGENTS.md" is not. Verify via /memory or /context all. Comments add symlink and generate-configs-from-one-rules-source alternatives.

## 原文摘录 / Evidence Excerpts

I tripped over this after adding a short `CLAUDE.md` next to an `AGENTS.md` I was already using for Cursor and Codex. Claude Code sessions stopped seeing the shared commands and the "ask first" list. The file was fine. It just wasn't being loaded.

Claude Code's memory docs (https://code.claude.com/docs/en/memory) say that, by default, it reads `AGENTS.md` only when there is no `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in the working directory or above it.

The one-line fix is to put `@AGENTS.md` on line 1 of `CLAUDE.md`. That's an actual import. A sentence that says "please also read AGENTS.md" is not — Claude only opens it if it decides to. Then run `/memory` or `/context all` and confirm both files show up.

Comment (u/Successful-Tax1306): another option, if you don't want to keep two files at all, is a symlink, so CLAUDE.md just points to AGENTS.md and every tool reads the same text.

---

## 证据来源

opencli web read 直接抓取原帖全文（2026-11-13）。社区热度：约 7 赞 8 评（last30days 2026-11-13 引擎窗）。
