# AGENTS.md — Drop-in senior engineer behavior spec for coding agents

- **ID**: agentsm_001
- **原文链接**: https://github.com/TheRealSeanDonahoe/agents-md
- **作者**: TheRealSeanDonahoe / FerroxLabs（已迁移）
- **平台**: GitHub
- **分类**: coding-agents/best-practices
- **标签**: coding-agent, claude-code, cursor, gemini-cli, best-practices, prompt-engineering, agents-md
- **质量评分**: 4/5
- **抓取时间**: 2026-07-02T12:24:35
- **抓取方式**: opencli web read

---

## 用一行文件让所有编程 Agent 停止「过度热情」和「阿谀奉承」，强制进入工程验证循环

---

## English (Original)

[![Sean Donahoe's AGENTS.md — Smarter Operating Instructions for Coding Agents](https://github.com/FerroxLabs/agents-md/releases/download/v0.1.0/hero.png)](https://github.com/FerroxLabs/agents-md/releases/download/v0.1.0/hero.png)

**One file. Every coding agent starts behaving like a senior engineer.**

Drop it into any repo. Claude Code, Codex, Cursor, Gemini CLI, Aider, Windsurf, Copilot, and Devin all read it on their own. No plugins. No config. No setup rituals.

It just works.

This is the tool and the core operating discipline we run on every project at Ferrox Labs. One file, every agent, every repo.

* * *

## Install

[](#install)

### The easy way — hand it to your agent

[](#the-easy-way--hand-it-to-your-agent)

Open Claude Code, Codex, Cursor, or any coding agent in your project root. Paste this:

> Install [https://github.com/FerroxLabs/agents-md](https://github.com/FerroxLabs/agents-md) into this project.
>
> 1.  Fetch `https://raw.githubusercontent.com/FerroxLabs/agents-md/main/AGENTS.md` and save it as `./AGENTS.md` at the project root. If `AGENTS.md` already exists, stop and show me the diff before overwriting.
> 2.  Symlink `CLAUDE.md` and `GEMINI.md` to `AGENTS.md` so Claude Code and Gemini CLI read the same file. Use the right command for my OS (`ln -s` on macOS/Linux, `New-Item -ItemType SymbolicLink` on Windows). If symlinks fail, fall back to copying the file. If `CLAUDE.md` or `GEMINI.md` already exist with content, do not overwrite — prepend `@AGENTS.md` as the first line and leave the rest intact.
> 3.  Open the new `AGENTS.md`, find section 10 (Project context), and fill in only what you can verify by reading this codebase: stack, build/test/lint commands from `package.json`, `pyproject.toml`, `Cargo.toml`, or `Makefile`, and source/test directory layout. Leave anything you can't confirm as `TODO`.
> 4.  Do not touch section 11 — it stays empty by design.
> 5.  When done, tell me to restart this session so the file loads.

Restart the session. You're done.

### The manual way

[](#the-manual-way)

```shell
curl -o AGENTS.md https://raw.githubusercontent.com/FerroxLabs/agents-md/main/AGENTS.md
```

Codex, Cursor, Aider, Windsurf, Copilot, Devin, Amp, opencode, and RooCode read `AGENTS.md` on their own. Nothing else to do.

Claude Code and Gemini CLI look for their own filenames, so symlink:

**macOS / Linux**

```shell
ln -s AGENTS.md CLAUDE.md
ln -s AGENTS.md GEMINI.md
```

**Windows** (PowerShell, run as admin or with Developer Mode on)

```powershell
New-Item -ItemType SymbolicLink -Path CLAUDE.md -Target AGENTS.md
New-Item -ItemType SymbolicLink -Path GEMINI.md -Target AGENTS.md
```

If symlinks aren't available, copy the file instead — you'll just need to re-copy when you update `AGENTS.md`:

```powershell
Copy-Item AGENTS.md CLAUDE.md; Copy-Item AGENTS.md GEMINI.md
```

Open a session. You're done.

* * *

## What changes immediately

[](#what-changes-immediately)

| Before | After |
| --- | --- |
| _"You're absolutely right!"_ → reverts working code | Agent pushes back when you're wrong |
| 200 lines when 50 would do | Simplest diff that solves the problem |
| Reformats your whole file while fixing a typo | Every changed line traces to your request |
| Claims "done" on code that doesn't run | Writes verification first, runs it, then reports |
| Silently guesses between two interpretations | Surfaces the ambiguity, asks once |
| Ignores half your rules because the file is too long | Tight by design. ~200 lines. Rules stay loaded. |

* * *

## Two sections you edit. Everything else you leave alone.

[](#two-sections-you-edit-everything-else-you-leave-alone)

**Section 10 — Project context.** Stack, commands, layout, forbidden areas. Fill the `TODO`s once. Five minutes.

**Section 11 — Project Learnings.** Starts empty. Every time the agent gets something wrong, one line gets added. The agent itself adds the line when you correct it — you don't babysit the file.

This is the section that compounds. Boris Cherny, the creator of Claude Code, runs his team's version at around 100 learnings accumulated over months. His file is a trained reflex, not a manifesto.

Sections 0–9 are the behavioral scaffold. Don't touch them unless you have a specific reason.

* * *

## When your AGENTS.md outgrows one file

[](#when-your-agentsmd-outgrows-one-file)

Rare. But it happens on large codebases. Read the docs before you shard — most people don't need to:

-   **Claude Code:** use `@path/to/file.md` imports inside `CLAUDE.md`, or drop topic-scoped rules into `.claude/rules/*.md` with `paths:` frontmatter so they only load when Claude touches matching files. Claude Code also writes its own memory automatically — don't reinvent it.
-   **Cursor:** use `.cursor/rules/*.mdc` with path scoping for the same reason.
-   **Everyone else:** one `AGENTS.md` is still the right answer.

The goal is fewer tokens loaded per session, not more files for their own sake.

* * *

## Why `AGENTS.md` and not `CLAUDE.md`

[](#why-agentsmd-and-not-claudemd)

`AGENTS.md` is the [open cross-tool standard](https://agents.md/) stewarded by the Linux Foundation's Agentic AI Foundation. Codex, Cursor, Windsurf, Copilot, Aider, Devin, Amp, opencode, and RooCode read it natively. Claude Code reads `CLAUDE.md`. Gemini CLI reads `GEMINI.md`. Symlink all three and every agent reads the same file.

One source of truth. Stop maintaining three.

* * *

## What it's built on

[](#what-its-built-on)

-   Sean Donahoe's **IJFW** principles — _it just f\*cking works_: one install, zero ceremony, working code
-   Andrej Karpathy's [four principles](https://github.com/forrestchang/andrej-karpathy-skills) on LLM coding failure modes
-   Boris Cherny's public Claude Code workflow — reactive pruning, keep it tight
-   [Anthropic's official Claude Code best practices](https://code.claude.com/docs/en/best-practices)
-   The [AGENTS.md](https://agents.md/) open standard

* * *

## License

[](#license)

MIT. Fork it, rewrite it, ship it with your own name on it. That's the point.

* * *

If it saved you an hour, a ⭐ on the repo is how you say thanks.

---

## 中文摘要

`AGENTS.md` 是一份约 200 行的"高级工程师行为规范"文件，放到项目根目录即可让 Claude Code、Codex、Cursor、Gemini CLI、Aider、Windsurf、Copilot、Devin 等所有主流编程 Agent 自动以资深工程师方式工作，无需插件或额外配置。该项目原本位于 TheRealSeanDonahoe/agents-md，现已迁移到 FerroxLabs/agents-md。

**核心行为改变**（前后对比）：
- 之前是 "You're absolutely right!" → 改坏正在工作的代码；之后 Agent 会在用户犯错时主动反驳。
- 之前一个修复动辄 200 行；之后追求能解决问题的最小 diff。
- 之前改一个 typo 会顺手格式化整个文件；之后每一处改动都对应到用户请求。
- 之前声称"完成"但代码跑不通；之后先写验证、再运行、再报告。
- 之前两个含义间默默猜测；之后主动暴露歧义、只问一次。
- 之前规则太多加载不到一半；之后紧贴 200 行设计，规则全量生效。

**两段需要手动编辑，其余不要动**：
- **Section 10 — 项目上下文**：栈、命令、目录布局、禁区。把 TODO 填一次，五分钟搞定。
- **Section 11 — 项目经验积累**：初始为空。每次 Agent 犯错了加一行；Agent 自己加，你不需要手动维护。这一段是复利所在 —— Boris Cherny（Claude Code 作者）的团队版本运行数月后积累了约 100 条经验。

**与 CLAUDE.md 的关系**：`AGENTS.md` 是 Linux Foundation Agentic AI Foundation 维护的开放跨工具标准。Claude Code 读 `CLAUDE.md`、Gemini CLI 读 `GEMINI.md`，因此需要软链接或复制 `AGENTS.md` 到这两个文件，一个源头全 Agent 共享。

**理论基础**：融合 Karpathy 的 LLM 编程四大失败原则、Boris Cherny 公开的 Claude Code 工作流（响应式修剪、保持紧凑）、Anthropic 官方 Claude Code 最佳实践。

**License**：MIT。可以 fork、改写、署自己的名字发布 —— 这正是这个项目的目的。
