# AGENTS.md — Drop-in senior engineer behavior spec for coding agents

GitHub: https://github.com/TheRealSeanDonahoe/agents-md
Stars: 525 (截至 2026-04-27)
License: MIT

## 核心理念

One file. Every coding agent starts behaving like a senior engineer.

Drop it into any repo. Claude Code, Codex, Cursor, Gemini CLI, Aider, Windsurf, Copilot, and Devin all read it on their own. No plugins. No config. No setup rituals.

## 行为改变对比

| Before | After |
| --- | --- |
| "You're absolutely right!" → reverts working code | Agent pushes back when you're wrong |
| 200 lines when 50 would do | Simplest diff that solves the problem |
| Reformats whole file while fixing a typo | Every changed line traces to your request |
| Claims "done" on code that doesn't run | Writes verification first, runs it, then reports |
| Silently guesses between two interpretations | Surfaces the ambiguity, asks once |
| Ignores half your rules because file is too long | Tight by design. ~200 lines. Rules stay loaded. |

## 两个可编辑区域，其余不动

**Section 10 — Project context**: Stack, commands, layout. Fill the TODO once. Five minutes.

**Section 11 — Project Learnings**: Starts empty. Every time the agent gets something wrong, one line gets added. This is the section that compounds.

## 理论基础

- Sean Donahoe's IJFW principles — it just f*cking works
- Andrej Karpathy's four principles on LLM coding failure modes
- Boris Cherny's public Claude Code workflow — reactive pruning, keep it tight
- Anthropic's official Claude Code best practices
- The AGENTS.md open standard (Linux Foundation / Agentic AI Foundation)

## 为什么是 AGENTS.md 而非 CLAUDE.md

AGENTS.md 是 Linux Foundation Agentic AI Foundation 维护的跨工具开放标准。Codex, Cursor, Windsurf, Copilot, Aider, Devin, Amp, opencode 和 RooCode 原生读取它。Claude Code 读取 CLAUDE.md，Gemini CLI 读取 GEMINI.md。通过符号链接三合一。

## 安装方式

```bash
curl -o AGENTS.md https://raw.githubusercontent.com/TheRealSeanDonahoe/agents-md/main/AGENTS.md
ln -s AGENTS.md CLAUDE.md  # macOS/Linux
ln -s AGENTS.md GEMINI.md  # macOS/Linux
```

> 备注：原文抓取自 GitHub README。
