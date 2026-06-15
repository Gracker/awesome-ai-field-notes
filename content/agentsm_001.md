# AGENTS.md — Drop-in senior engineer behavior spec for coding agents

- **来源**：GitHub
- **原文链接**：https://github.com/TheRealSeanDonahoe/agents-md
- **作者**：TheRealSeanDonahoe
- **原始日期**：—
- **抓取时间**：2026-06-15
- **质量评分**：4
- **抓取方式**：opencli web read

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

## 中文摘要

AGENTS.md 是一个约 200 行的可放置于项目根目录的行为规范文件，让 Claude Code、Codex、Cursor、Gemini CLI 等编程 Agent 自动按高级工程师方式工作。核心改变：Agent 在用户犯错时主动反驳、只做最小必要修改、不擅自重构无关代码、先写验证再报告完成、遇到歧义主动询问。综合了 Karpathy 的四大 LLM 编程失败原则和 Boris Cherny 的 Claude Code 工作流，仅两个区域需要手动编辑（项目上下文 + 经验积累）。是 Linux Foundation Agentic AI Foundation 维护的跨工具开放标准。

## 中文翻译

**一个文件，让所有编程 Agent 立刻表现得像高级工程师。**

把它放进任意代码仓库根目录。Claude Code、Codex、Cursor、Gemini CLI、Aider、Windsurf、Copilot、Devin 都会自动读取它。无需插件、无需配置、无需仪式。

### 安装方式

**简单方法——交给你的 Agent 即可**：在 Claude Code、Codex、Cursor 或任何编程 Agent 中粘贴以下指令：

1. 抓取 https://raw.githubusercontent.com/FerroxLabs/agents-md/main/AGENTS.md 并保存为项目根的 ./AGENTS.md。如果已存在 AGENTS.md，先停下展示差异再覆盖。
2. 把 CLAUDE.md 和 GEMINI.md 软链到 AGENTS.md，让 Claude Code 与 Gemini CLI 读取同一文件（macOS/Linux 用 ln -s，Windows PowerShell 用 New-Item -ItemType SymbolicLink）。如果软链失败则改用复制。如果 CLAUDE.md/GEMINI.md 已存在，不要覆盖，而是在首行加 @AGENTS.md 引入即可。
3. 打开新的 AGENTS.md，找到第 10 节（Project context），只填你能从代码库中验证到的内容：技术栈、从 package.json / pyproject.toml / Cargo.toml / Makefile 读到的构建/测试/lint 命令、源码与测试目录布局。无法确认的留 TODO。
4. 不要动第 11 节——按设计它保持空白。
5. 完成后提示用户重启会话以加载文件。

**手动方式**：执行 curl -o AGENTS.md https://raw.githubusercontent.com/FerroxLabs/agents-md/main/AGENTS.md。Codex、Cursor、Aider、Windsurf、Copilot、Devin、Amp、opencode、RooCode 都会自动读取 AGENTS.md，无需其他操作。Claude Code 找 CLAUDE.md，Gemini CLI 找 GEMINI.md，所以把这三个文件名软链到同一份 AGENTS.md 即可。

### 立刻带来的改变

之前：用户说"您说得对！" 然后回滚正常工作的代码 / 用 200 行写 50 行能搞定的事 / 改一个 typo 时顺手重排整个文件 / 代码跑不起来却宣称完成 / 在两种解读间默默猜测 / 规则文件太长导致一半被忽略。

之后：Agent 会在你错的时候主动反驳 / 解决问题所需的最简 diff / 每一行变更都对应你的请求 / 先写验证 → 跑通 → 再回报 / 主动暴露歧义，只问一次 / 设计紧凑约 200 行，规则始终在上下文内。

### 只需要编辑两个章节

- 第 10 节 Project context：技术栈、命令、目录结构、禁区。把 TODO 一次性填好，五分钟。
- 第 11 节 Project Learnings：从空白开始。每次 Agent 出错时，Agent 自己加一行——你不必亲自维护。这是会复利的章节。Boris Cherny（Claude Code 作者）团队版本累积了约 100 条 learnings，多月沉淀后文件本身成了训练过的反射。

第 0–9 节是行为脚手架，除非有明确理由否则不要动。

### 何时拆分到多个文件

大型代码库偶尔需要拆分，但绝大多数项目不需要。Claude Code 用 @path/to/file.md 引入或 .claude/rules/*.md 配合 paths: frontmatter（只在匹配文件被触碰时加载）。Cursor 用 .cursor/rules/*.mdc。其他 Agent 一份 AGENTS.md 仍然够用。

### 为什么叫 AGENTS.md 而不是 CLAUDE.md

AGENTS.md 是 Linux Foundation 下 Agentic AI Foundation 维护的开放跨工具标准。Codex、Cursor、Windsurf、Copilot、Aider、Devin、Amp、opencode、RooCode 都原生读取。Claude Code 读 CLAUDE.md，Gemini CLI 读 GEMINI.md。三个文件名软链到同一份 AGENTS.md——单一信息源，告别维护三份文件。

### 设计依据

- Sean Donahoe 的 IJFW 原则（it just f*cking works）：一次安装、零仪式、能跑起来
- Andrej Karpathy 关于 LLM 编程失败的四条原则
- Boris Cherny 公开的 Claude Code 工作流——反应式精简、保持紧凑
- Anthropic 官方的 Claude Code 最佳实践
- AGENTS.md 开放标准

### 许可证

MIT。Fork、改写、以你的名义发布——这正是它的意义所在。

---

*本文件由 AAIF Content Fetcher 自动抓取并双语整理。原文版权归原作者所有。*
