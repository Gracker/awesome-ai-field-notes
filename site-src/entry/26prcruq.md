---
title: 'GitHub - steipete/CodexBar: Show usage stats for OpenAI Codex and Claude Code, without having to login.'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# GitHub - steipete/CodexBar: Show usage stats for OpenAI Codex and Claude Code, without having to login.

> Claude Code 编程工具相关实践与技巧

🔗 [原文链接](https://github.com/steipete/CodexBar) | 🌐 | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-04-10

`mcp` `copilot` `[]` `cursor` `openai` `codex` `gemini` `claude`

---

# CodexBar: 显示 OpenAI Codex 和 Claude Code 使用情况的 macOS 菜单栏应用

## English

Tiny macOS 14+ menu bar app that keeps your Codex, Claude, Cursor, Gemini, Antigravity, Droid (Factory), Copilot, z.ai, Kiro, Vertex AI, Augment, Amp, JetBrains AI, OpenRouter, Perplexity, and Abacus AI limits visible (session + weekly where available) and shows when each window resets. One status item per provider (or Merge Icons mode with a provider switcher and optional Overview tab); enable what you use from Settings. No Dock icon, minimal UI, dynamic bar icons in the menu bar.

- macOS 14+ (Sonoma)

Download: [https://github.com/steipete/CodexBar/releases](https://github.com/steipete/CodexBar/releases)

brew install --cask steipete/tap/codexbar

brew install steipete/tap/codexbar

Or download CodexBarCLI-v`tag`-linux-`arch`.tar.gz from GitHub Releases.
Linux support via Omarchy: community Waybar module and TUI, driven by the codexbar executable.

- Open Settings → Providers and enable what you use.

- Install/sign in to the provider sources you rely on (e.g. codex, claude, gemini, browser cookies, or OAuth; Antigravity requires the Antigravity app running).

- Optional: Settings → Providers → Codex → OpenAI cookies (Automatic or Manual) to add dashboard extras.

- [Codex](/steipete/CodexBar/blob/main/docs/codex.md) — Local Codex CLI RPC (+ PTY fallback) and optional OpenAI web dashboard extras.

- [Claude](/steipete/CodexBar/blob/main/docs/claude.md) — OAuth API or browser cookies (+ CLI PTY fallback); session + weekly usage.

- [Cursor](/steipete/CodexBar/blob/main/docs/cursor.md) — Browser session cookies for plan + usage + billing resets.

- [Gemini](/steipete/CodexBar/blob/main/docs/gemini.md) — OAuth-backed quota API using Gemini CLI credentials (no browser cookies).

- [Antigravity](/steipete/CodexBar/blob/main/docs/antigravity.md) — Local language server probe (experimental); no external auth.

- [Droid](/steipete/CodexBar/blob/main/docs/factory.md) — Browser cookies + WorkOS token flows for Factory usage + billing.

- [Copilot](/steipete/CodexBar/blob/main/docs/copilot.md) — GitHub device flow + Copilot internal usage API.

- [z.ai](/steipete/CodexBar/blob/main/docs/zai.md) — API token (Keychain) for quota + MCP windows.

- [Kimi](/steipete/CodexBar/blob/main/docs/kimi.md) — Auth token (JWT from kimi-auth cookie) for weekly quota + 5‑hour rate limit.

- [Kimi K2](/steipete/CodexBar/blob/main/docs/kimi-k2.md) — API key for credit-based usage totals.

- [Kiro](/steipete/CodexBar/blob/main/docs/kiro.md) — CLI-based usage via kiro-cli /usage command; monthly credits + bonus credits.

- [Vertex AI](/steipete/CodexBar/blob/main/docs/vertexai.md) — Google Cloud gcloud OAuth with token cost tracking from local Claude logs.

- [Augment](/steipete/CodexBar/blob/main/docs/augment.md) — Browser cookie-based authentication with automatic session keepalive; credits tracking and usage monitoring.

- [Amp](/steipete/CodexBar/blob/main/docs/amp.md) — Browser cookie-based authentication with Amp Free usage tracking.

- [JetBrains AI](/steipete/CodexBar/blob/main/docs/jetbrains.md) — Local XML-based quota from JetBrains IDE configuration; monthly credits tracking.

- [OpenRouter](/steipete/CodexBar/blob/main/docs/openrouter.md) — API token for credit-based usage tracking across multiple AI providers.

- [Abacus AI](/steipete/CodexBar/blob/main/docs/abacus.md) — Browser cookie auth for ChatLLM/RouteLLM compute credit tracking.

- Open to new providers: [provider authoring guide](/steipete/CodexBar/blob/main/docs/provider.md).

The menu bar icon is a tiny two-bar meter:

- Top bar: 5‑hour/session window. If weekly is missing/exhausted and credits are available, it becomes a thicker credits bar.

- Bottom bar: weekly window (hairline).

- Errors/stale data dim the icon; status overlays indicate incidents.

- Multi-provider menu bar with per-provider toggles (Settings → Providers).

- Session + weekly meters with reset countdowns.

- Optional Codex web dashboard enrichments (code review remaining, usage breakdown, credits history).

- Local cost-usage scan for Codex + Claude (last 30 days).

- Provider status polling with incident badges in the menu and icon overlay.

- Merge Icons mode to combine providers into one status item + switcher, with an optional Overview tab for up to three providers.

- Refresh cadence presets (manual, 1m, 2m, 5m, 15m).

- Bundled CLI (codexbar) for scripts and CI (including codexbar cost --provider codex|claude for local cost usage); Linux CLI builds available.

- WidgetKit widget mirrors the menu card snapshot.

- Privacy-first: on-device parsing by default; browser cookies are opt-in and reused (no passwords stored).

Wondering if CodexBar scans your disk? It doesn't crawl your filesystem; it reads a small set of known locations (browser cookies/local storage, local JSONL logs) when the related features are enabled. See the discussion and audit notes in [issue #12](https://github.com/steipete/CodexBar/issues/12).

- Full Disk Access (optional): only required to read Safari cookies/local storage for web-based providers (Codex web, Claude web, Cursor, Droid/Factory). If you don't grant it, use Chrome/Firefox cookies or CLI-only sources instead.

- Keychain access (prompted by macOS):

Chrome cookie import needs the "Chrome Safe Storage" key to decrypt cookies.

- Claude OAuth credentials (written by the Claude CLI) are read from Keychain when present.

- z.ai API token is stored in Keychain from Preferences → Providers; Copilot stores its API token in Keychain during device flow.

- How do I prevent those keychain alerts?

Open Keychain Access.app → login keychain → search the item (e.g., "Claude Code-credentials").

- Open the item → Access Control → add CodexBar.app under "Always allow access by these applications".

- Prefer adding just CodexBar (avoid "Allow all applications" unless you want it wide open).

- Relaunch CodexBar after saving.

- Reference screenshot: /steipete/CodexBar/blob/main/docs/keychain-allow.png

- How to do the same for the browser?

Find the browser's "Safe Storage" key (e.g., "Chrome Safe Storage", "Brave Safe Storage", "Firefox", "Microsoft Edge Safe Storage").

- Open the item → Access Control → add CodexBar.app under "Always allow access by these applications".

- This removes the prompt when CodexBar decrypts cookies for that browser.

- Files & Folders prompts (folder/volume access): CodexBar launches provider CLIs (codex/claude/gemini/antigravity). If those CLIs read a project directory or external drive, macOS may ask CodexBar for that folder/volume (e.g., Desktop or an external volume). This is driven by the CLI's working directory, not background disk scanning.

- What we do not request: no Screen Recording, Accessibility, or Automation permissions; no passwords are stored (browser cookies are reused when you opt in).

- Providers overview: [docs/providers.md](/steipete/CodexBar/blob/main/docs/providers.md)

- Provider authoring: [docs/provider.md](/steipete/CodexBar/blob/main/docs/provider.md)

- Issue labeling guide: [docs/ISSUE_LABELING.md](/steipete/CodexBar/blob/main/docs/ISSUE_LABELING.md)

- UI & icon notes: [docs/ui.md](/steipete/CodexBar/blob/main/docs/ui.md)

- CLI reference: [docs/cli.md](/steipete/CodexBar/blob/main/docs/cli.md)

- Architecture: [docs/architecture.md](/steipete/CodexBar/blob/main/docs/architecture.md)

- Refresh loop: [docs/refresh-loop.md](/steipete/CodexBar/blob/main/docs/refresh-loop.md)

- Status polling: [docs/status.md](/steipete/CodexBar/blob/main/docs/status.md)

- Sparkle updates: [docs/sparkle.md](/steipete/CodexBar/blob/main/docs/sparkle.md)

- Release checklist: [docs/RELEASING.md](/steipete/CodexBar/blob/main/docs/RELEASING.md)

- Clone the repo and open it in Xcode or run the scripts directly.

- Launch once, then toggle providers in Settings → Providers.

- Install/sign in to provider sources you rely on (CLIs, browser cookies, or OAuth).

- Optional: set OpenAI cookies (Automatic or Manual) for Codex dashboard extras.

swift build -c release # or debug for development
./Scripts/package_app.sh # builds CodexBar.app in-place
CODEXBAR_SIGNING=adhoc ./Scripts/package_app.sh # ad-hoc signing (no Apple Developer account)
open CodexBar.app

Dev loop:

./Scripts/compile_and_run.sh

- ✂️ [Trimmy](https://github.com/steipete/Trimmy) — "Paste once, run once." Flatten multi-line shell snippets so they paste and run.

- 🧳 [MCPorter](https://mcporter.dev) — TypeScript toolkit + CLI for Model Context Protocol servers.

- 🧿 [oracle](https://askoracle.dev) — Ask the oracle when you're stuck. Invoke GPT-5 Pro with a custom context and files.

- [Win-CodexBar](https://github.com/Finesssee/Win-CodexBar)

Inspired by [ccusage](https://github.com/ryoppippi/ccusage) (MIT), specifically the cost usage tracking.

MIT • Peter Steinberger ([steipete](https://twitter.com/steipete))

## 中文

这是一个微小的 macOS 14+ 菜单栏应用，让您的 Codex、Claude、Cursor、Gemini、Antigravity、Droid (Factory)、Copilot、z.ai、Kiro、Vertex AI、Augment、Amp、JetBrains AI、OpenRouter、Perplexity 和 Abacus AI 限制保持可见（会话 + 周，如适用），并显示每个窗口何时重置。每个提供商一个状态项（或合并图标模式，带提供商切换器和可选的概览标签）；从设置中启用您使用的内容。无 Dock 图标，最简 UI，菜单栏中动态条形图标。

- macOS 14+ (Sonoma)

下载：[https://github.com/steipete/CodexBar/releases](https://github.com/steipete/CodexBar/releases)

brew install --cask steipete/tap/codexbar

brew install steipete/tap/codexbar

或者从 GitHub Releases 下载 CodexBarCLI-v`tag`-linux-`arch`.tar.gz。
通过 Omarchy 支持 Linux：社区 Waybar 模块和 TUI，由 codexbar 可执行文件驱动。

- 打开设置 → 提供商，启用您使用的内容。

- 安装/登录您依赖的提供商源（例如 codex、claude、gemini、浏览器 cookie 或 OAuth；Antigravity 需要 Antigravity 应用正在运行）。

- 可选：设置 → 提供商 → Codex → OpenAI cookie（自动或手动）以添加仪表板附加功能。

- [Codex](/steipete/CodexBar/blob/main/docs/codex.md) — 本地 Codex CLI RPC（+ PTY 回退）和可选的 OpenAI 网络仪表板附加功能。

- [Claude](/steipete/CodexBar/blob/main/docs/claude.md) — OAuth API 或浏览器 cookie（+ CLI PTY 回退）；会话 + 周使用量。

- [Cursor](/steipete/CodexBar/blob/main/docs/cursor.md) — 浏览器会话 cookie，用于计划 + 使用 + 计费重置。

- [Gemini](/steipete/CodexBar/blob/main/docs/gemini.md) — 基于OAuth的配额 API，使用 Gemini CLI 凭据（无浏览器 cookie）。

- [Antigravity](/steipete/CodexBar/blob/main/docs/antigravity.md) — 本地语言服务器探测（实验性）；无外部身份验证。

- [Droid](/steipete/CodexBar/blob/main/docs/factory.md) — 浏览器 cookie + WorkOS 令牌流，用于 Factory 使用 + 计费。

- [Copilot](/steipete/CodexBar/blob/main/docs/copilot.md) — GitHub 设备流 + Copilot 内部使用 API。

- [z.ai](/steipete/CodexBar/blob/main/docs/zai.md) — API 令牌（钥匙串），用于配额 + MCP 窗口。

- [Kimi](/steipete/CodexBar/blob/main/docs/kimi.md) — 身份验证令牌（来自 kimi-auth cookie 的 JWT），用于周配额 + 5 小时速率限制。

- [Kimi K2](/steipete/CodexBar/blob/main/docs/kimi-k2.md) — 基于 API 密钥的积分总额。

- [Kiro](/steipete/CodexBar/blob/main/docs/kiro.md) — 基于 CLI 的使用量，通过 kiro-cli /usage 命令；月度积分 + 奖励积分。

- [Vertex AI](/steipete/CodexBar/blob/main/docs/vertexai.md) — Google Cloud gcloud OAuth，从本地 Claude 日志跟踪令牌成本。

- [Augment](/steipete/CodexBar/blob/main/docs/augment.md) — 基于浏览器 cookie 的身份验证，自动保持会话活跃；积分跟踪和使用监控。

- [Amp](/steipete/CodexBar/blob/main/docs/amp.md) — 基于浏览器 cookie 的身份验证，Amp Free 使用量跟踪。

- [JetBrains AI](/steipete/CodexBar/blob/main/docs/jetbrains.md) — 基于 JetBrains IDE 配置的本地 XML 配额；月度积分跟踪。

- [OpenRouter](/steipete/CodexBar/blob/main/docs/openrouter.md) — API 令牌，用于跨多个 AI 提供商的基于积分的使用量跟踪。

- [Abacus AI](/steipete/CodexBar/blob/main/docs/abacus.md) — 浏览器 cookie 身份验证，用于 ChatLLM/RouteLLM 计算积分跟踪。

- 接受新的提供商：[提供商编写指南](/steipete/CodexBar/blob/main/docs/provider.md)。

菜单栏图标是一个微小的双条计量器：

- 顶部条：5小时/会话窗口。如果周窗口缺失/耗尽且积分可用，它会变成更粗的积分条。

- 底部条：周窗口（细线）。

- 错误/过期数据会淡化图标；状态覆盖显示事件。

- 多提供商菜单栏，每个提供商都有切换（设置 → 提供商）。

- 会话 + 周计量器，带重置倒计时。

- 可选的 Codex 网络仪表板增强功能（代码审查剩余、使用情况分解、积分历史）。

- Codex + Claude 的本地成本使用量扫描（最近30天）。

- 提供商状态轮询，菜单和图标覆盖中的事件徽章。

- 合并图标模式将提供商合并为一个状态项 + 切换器，可选的概览标签支持最多三个提供商。

- 刷新节奏预设（手动、1分钟、2分钟、5分钟、15分钟）。

- 捆绑的 CLI（codexbar）用于脚本和 CI（包括 codexbar cost --provider codex|claude 的本地成本使用）；提供 Linux CLI 构建。

- WidgetKit 小部件镜像菜单卡片快照。

- 隐私优先：默认设备解析；浏览器 cookie 是可选的并重复使用（不存储密码）。

想知道 CodexBar 是否扫描您的磁盘吗？它不会爬取您的文件系统；它在相关功能启用时读取少量已知位置（浏览器 cookie/本地存储、本地 JSONL 日志）。请参阅 [issue #12](https://github.com/steipete/CodexBar/issues/12) 中的讨论和审计说明。

- 完整磁盘访问（可选）：仅需要读取基于网络的提供商（Codex 网络、Claude 网络、Cursor、Droid/Factory）的 Safari cookie/本地存储。如果您不授予此权限，请使用 Chrome/Firefox cookie 或仅 CLI 来源。

- 钥匙串访问（由 macOS 提示）：

Chrome cookie 导入需要"Chrome 安全存储"密钥来解密 cookie。

- Claude OAuth 凭据（由 Claude CLI 写入）在存在时从钥匙串读取。

- z.ai API 令牌从偏好设置 → 提供商存储在钥匙串中；Copilot 在设备流期间将其 API 令牌存储在钥匙串中。

- 如何防止那些钥匙串警报？

打开钥匙串访问应用 → 登录钥匙串 → 搜索项目（例如，"Claude Code-credentials"）。

- 打开项目 → 访问控制 → 在"始终允许这些应用程序访问"下添加 CodexBar.app。

- 优先添加仅 CodexBar（避免"允许所有应用程序"，除非您希望完全开放）。

- 保存后重新启动 CodexBar。

- 参考截图：/steipete/CodexBar/blob/main/docs/keychain-allow.png

- 如何对浏览器执行相同操作？

找到浏览器的"安全存储"密钥（例如，"Chrome 安全存储"、"Brave 安全存储"、"Firefox"、"Microsoft Edge 安全存储"）。

- 打开项目 → 访问控制 → 在"始终允许这些应用程序访问"下添加 CodexBar.app。

- 这会删除 CodexBar 解密该浏览器 cookie 时的提示。

- 文件和文件夹提示（文件夹/卷访问）：CodexBar 启动提供商 CLI（codex/claude/gemini/antigravity）。如果这些 CLI 读取项目目录或外部驱动器，macOS 可能会要求 CodexBar 访问该文件夹/卷（例如，桌面或外部卷）。这由 CLI 的工作目录驱动，而不是后台磁盘扫描。

- 我们不请求的内容：无屏幕录制、辅助功能或自动化权限；不存储密码（浏览器 cookie 在您选择时重复使用）。

- 提供商概览：[docs/providers.md](/steipete/CodexBar/blob/main/docs/providers.md)

- 提供商编写：[docs/provider.md](/steipete/CodexBar/blob/main/docs/provider.md)

- 问题标签指南：[docs/ISSUE_LABELING.md](/steipete/CodexBar/blob/main/docs/ISSUE_LABELING.md)

- UI 和图标说明：[docs/ui.md](/steipete/CodexBar/blob/main/docs/ui.md)

- CLI 参考：[docs/cli.md](/steipete/CodexBar/blob/main/docs/cli.md)

- 架构：[docs/architecture.md](/steipete/CodexBar/blob/main/docs/architecture.md)

- 刷新循环：[docs/refresh-loop.md](/steipete/CodexBar/blob/main/docs/refresh-loop.md)

- 状态轮询：[docs/status.md](/steipete/CodexBar/blob/main/docs/status.md)

- Sparkle 更新：[docs/sparkle.md](/steipete/CodexBar/blob/main/docs/sparkle.md)

- 发布清单：[docs/RELEASING.md](/steipete/CodexBar/blob/main/docs/RELEASING.md)

- 克隆仓库并在 Xcode 中打开或直接运行脚本。

- 启动一次，然后在设置 → 提供商中切换提供商。

- 安装/登录您依赖的提供商源（CLI、浏览器 cookie 或 OAuth）。

- 可选：设置 OpenAI cookie（自动或手动）以获得 Codex 仪表板附加功能。

swift build -c release # 或 debug 用于开发
./Scripts/package_app.sh # 在原位构建 CodexBar.app
CODEXBAR_SIGNING=adhoc ./Scripts/package_app.sh # ad-hoc 签名（无 Apple 开发者账户）
open CodexBar.app

开发循环：

./Scripts/compile_and_run.sh

- ✂️ [Trimmy](https://github.com/steipete/Trimmy) — "粘贴一次，运行一次。"展平多行 shell 代码片段，以便粘贴和运行。

- 🧳 [MCPorter](https://mcporter.dev) — 用于模型上下文协议服务器的 TypeScript 工具包 + CLI。

- 🧿 [oracle](https://askoracle.dev) — 当您遇到困难时询问神谕。使用自定义上下文和文件调用 GPT-5 Pro。

- [Win-CodexBar](https://github.com/Finesssee/Win-CodexBar)

灵感来自 [ccusage](https://github.com/ryoppippi/ccusage)（MIT），特别是成本使用量跟踪。

MIT • Peter Steinberger ([steipete](https://twitter.com/steipete))
