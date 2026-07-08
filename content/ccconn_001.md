# cc-connect: Bridge local AI coding agents to messaging platforms

- **ID**: `ccconn_001`
- **Source URL**: https://github.com/chenhg5/cc-connect
- **Original Date**: 2026-06-28 (latest release v1.4.1)
- **Category**: agents/frameworks
- **Quality Score**: 4/5
- **Status**: active
- **Fetched**: 2026-07-08T12:19+08:00
- **Language**: en (with curated Chinese summary in entries.json)
- **GitHub**: ⭐ 13.7k stars · 🍴 1.3k forks · 📦 43 releases (latest v1.4.1, Jun 28 2026)

> Source: <https://github.com/chenhg5/cc-connect>
> Primary README pulled on 2026-07-08 via curl (HTTPS, 535,820 bytes).
> Repo: chenhg5/cc-connect (Go, MIT).

---

## English

Control your local AI agents from any chat app. Anywhere, anytime.
cc-connect bridges AI agents running on your machine to the messaging platforms you already use.
Code review, research, automation, data analysis — anything an AI agent can do,
now accessible from your phone, tablet, or any device with a chat app.
🆕 What’s New in v1.3.3
First stable of the 1.3.3 series — stabilizes beta.1 → beta.5 (≈ 235 PRs since v1.3.2) plus 7 post-beta fixes. Highlights:
New agents
— Devin CLI, Google Antigravity (
agy
), GitHub Copilot CLI as first-class agents (#672, #1123, #865). Hardened Cursor / OpenCode / Qoder / Kimi / Pi coverage.
Platform expansion
— QQ (OneBot) file send & receive (#323), QQ Bot inline keyboards (#1131), WeCom
SendFile
in WebSocket (#1199), Feishu audio + video native media (#1202), Slack Assistant API (#844), MAX webhook delivery (#818), DingTalk @mentions / richText / image / file inbound (#1188, #828, #1357), broader Weibo DM, WPS Xiezuo (金山协作).
Long-running turn hardening
— new
max_turn_time_mins
wall-clock cap with soft-stop + force-kill + auto-resume so a long bash / test command can no longer lock a session indefinitely (#1091).
New core commands
—
/timer
(one-shot delayed task),
/cancel
(interrupt current turn),
/ps
(replaces
/btw
, kept as alias),
cron add --silent
, agent-driven TTS.
Multi-user / permissions
— reply-to-unauthorized-IM-senders option,
@Bot/permit
≡
/permit
keyword matching, Bridge requires token when enabled.
Provider ecosystem
— NekoCode, VisionCoder, AIHubMix, MiniMax M3 presets; Claude Code 1M-context Opus +
append_system_prompt
+ PermissionRequest hooks; Codex
request_user_input
app-server events; configurable
shell
+ shell profile for
exec
.
Observability
— blackbox testing framework (P0/P1/P2 + config-switch matrix), CUJ test framework, provider-resume regression suite for codex/opencode/kimi, Pi context-usage reporter in reply footer.
⚠️
Behavior changes (action may be required)
: Telegram/Discord
progress_style
defaults to
compact
(set
legacy
to revert); QQ Bot default
intents
now include
INTERACTION_CREATE
(custom values must include
1<<26
); DingTalk
msgtype=file
inbound now reaches the agent; engine permission keywords are @mention-tolerant;
reset_on_idle_mins
defaults to 30 min; Bridge with no token configured refuses to start. See
changelogs/v1.3.3.md
for the full themed summary.
No breaking changes. Coming from a v1.3.3-beta.*, this is a small fix-only upgrade.
🧩 Platform feature snapshot
High-level view of what each
built-in platform
can do in cc-connect.
Legend
Symbol
Meaning
✅
Works in
stable
cc-connect with typical configuration
⚠️
Partial, needs extra config (e.g. speech / ASR), or limited by the vendor app or API
❌
Not supported or not applicable in practice
†
QQ (NapCat / OneBot)
— unofficial self-hosted bridge; behaviour depends on your NapCat / network setup.
Capability
Feishu
WPS Xiezuo
DingTalk
Telegram
Slack
Discord
LINE
WeCom
Weibo
Weixin
(personal)
QQ†
QQ Bot
Matrix
Text & slash commands
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
Markdown / cards
✅
✅
✅
✅
✅
✅
⚠️
⚠️
❌
✅
✅
✅
⚠️
Streaming / chunked replies
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
Images & files
✅
❌
✅
✅
✅
✅
⚠️
✅
❌
✅
✅
✅
✅
Voice / STT / TTS
⚠️
❌
⚠️
✅
⚠️
⚠️
❌
⚠️
❌
✅
⚠️
⚠️
❌
Private (DM)
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
Group / channel
✅
✅
✅
✅
✅
✅
⚠️
✅
❌
✅
✅
✅
✅
WeCom:
Webhook mode needs a
public URL
; long-connection / WS style setups often do not.
Voice row:
many platforms need
[speech]
/ TTS providers enabled in
config.toml
; values are a best-effort summary.
Per-platform setup:
Platform setup guides
below.
✨ Why cc-connect?
🤖 Universal Agent Support
10+ AI Agents
— Claude Code, Codex, Cursor Agent, Kimi CLI, Qoder CLI, Gemini CLI, OpenCode, iFlow CLI, Pi, Devin, Copilot — plus any agent that supports the
Agent Client Protocol (ACP)
. Use whichever fits your workflow, or all of them at once.
📱 Platform Flexibility
13 Chat Platforms
— Feishu, WPS Xiezuo, DingTalk, Slack, Telegram, Discord, WeChat Work, Weibo, LINE, QQ, QQ Bot (Official), Matrix, plus
Weixin (personal ilink)
for
personal WeChat
. Most platforms need
zero public IP
.
🔄 Multi-Agent Orchestration
Multi-Bot Relay
— Bind multiple bots in a group chat and let them communicate with each other. Ask Claude, get insights from Gemini — all in one conversation.
🎮 Complete Chat Control
Full Control from Chat
— Switch models (
/model
), tune reasoning (
/reasoning
), change permission modes (
/mode
), manage sessions, all via slash commands.
Directory Switching in Chat
— Change where the next session starts with
/dir <path>
(and
/cd <path>
as a compatibility alias), plus quick history jump via
/dir <number>
/
/dir -
.
🧠 Persistent Memory
Agent Memory
— Read and write agent instruction files (
/memory
) without touching the terminal.
⏰ Intelligent Scheduling
Scheduled Tasks
— Set up cron jobs in natural language.
"Every day at 6am, summarize GitHub trending"
just works.
🎤 Multimodal Support
Voice & Images
— Send voice messages or screenshots; cc-connect handles STT/TTS and multimodal forwarding.
📦 Multi-Project Architecture
Multi-Project
— One process, multiple projects, each with its own agent + platform combo.
🌍 Multilingual Interface
5 Languages
— Native support for English, Chinese (Simplified & Traditional), Japanese, and Spanish. Built-in i18n ensures everyone feels at home.
Left：Lark  |  Telegram  |  Right：Wechat
🚀 Quick Start
🤖 Install & Configure via AI Agent (Recommended)
The easiest way
— Send this to Claude Code or any AI coding agent, and it will handle the entire installation and configuration for you:
Follow https://raw.githubusercontent.com/chenhg5/cc-connect/refs/heads/main/INSTALL.md to install and configure cc-connect.
📦 Manual Install
Via npm:
npm install -g cc-connect
Via Homebrew (macOS / Linux):
brew install cc-connect
Download binary from
GitHub Releases
:
#
Linux amd64 - Stable
curl -L -o cc-connect https://github.com/chenhg5/cc-connect/releases/latest/download/cc-connect-linux-amd64
chmod +x cc-connect
sudo mv cc-connect /usr/local/bin/
Build from source (requires Go 1.22+):
git clone https://github.com/chenhg5/cc-connect.git
cd
cc-connect
make build
⚙️ Configure
💡 Tip: Use the Web UI to configure
— After installing, run
cc-connect web
to configure the web admin and open the dashboard in your browser. You can visually create projects, add platforms, manage providers, and chat with your agent — no need to manually edit TOML files.
Note:
cc-connect web
only configures and opens the browser — you still need to run
cc-connect
separately to start the service.
If you prefer manual configuration:
mkdir -p
~
/.cc-connect
cp config.example.toml
~
/.cc-connect/config.toml
vim
~
/.cc-connect/config.toml
Set
admin_from = "alice,bob"
in a project to allow those user IDs to run privileged commands such as
/dir
and
/shell
.
admin_from
must be placed under
[[projects]]
(not under
[projects.platforms.options]
). You can use
/whoami
or
/status
to get your current
User ID
.
When a user runs
/dir reset
, cc-connect restores the configured
work_dir
and clears the persisted override stored under
data_dir/projects/<project>.state.json
.
▶️
Run
./cc-connect
🔄 Upgrade
#
npm
npm install -g cc-connect
#
Homebrew
brew upgrade cc-connect
#
Binary self-update
cc-connect update
#
Stable
cc-connect update --pre
#
Include pre-releases
📊 Support Matrix
Component
Type
Status
Agent
Claude Code
✅ Supported
Agent
Codex (OpenAI)
✅ Supported
Agent
Cursor Agent
✅ Supported
Agent
Gemini CLI (Google)
✅ Supported
Agent
Qoder CLI
✅ Supported
Agent
OpenCode (Crush)
✅ Supported
Agent
iFlow CLI
✅ Supported
Agent
Kimi CLI (Moonshot)
✅ Supported
Agent
Pi (Cursor Background Agent)
✅ Supported
Agent
Copilot (GitHub)
✅ Supported
Agent
ACP (Agent Client Protocol)
✅ Any
ACP-compatible agent
Agent
Devin (Cognition)
✅ Supported (via ACP)
Agent
Goose (Block)
🔜 Planned
Agent
Aider
🔜 Planned
Platform
Feishu (Lark)
✅ WebSocket — no public IP needed
Platform
DingTalk
✅ Stream — no public IP needed
Platform
WPS Xiezuo
✅ WebSocket — no public IP needed
Platform
Telegram
✅ Long Polling — no public IP needed
Platform
Slack
✅ Socket Mode — no public IP needed
Platform
Discord
✅ Gateway — no public IP needed
Platform
Weibo
✅ WebSocket — no public IP needed
Platform
LINE
✅ Webhook — public URL required
Platform
WeChat Work
✅ WebSocket / Webhook
Platform
Weixin (personal, ilink)
✅— HTTP long polling — no public IP needed
Platform
QQ (NapCat/OneBot)
✅ WebSocket
Platform
QQ Bot (Official)
✅ WebSocket — no public IP needed
Platform
Matrix
✅ Long Polling (/sync) — no public IP needed
📖 Platform Setup Guides
Platform
Guide
Connection
Public IP?
Feishu (Lark)
docs/feishu.md
WebSocket
No
DingTalk
docs/dingtalk.md
Stream
No
WPS Xiezuo
docs/wps-xiezuo.md
WebSocket
No
Telegram
docs/telegram.md
Long Polling
No
Slack
docs/slack.md
Socket Mode
No
Discord
docs/discord.md
Gateway
No
Weibo
docs/weibo.md
WebSocket
No
WeChat Work
docs/wecom.md
WebSocket / Webhook
No (WS) / Yes (Webhook)
Weixin (personal)
docs/weixin.md
HTTP long polling (ilink)
No
QQ / QQ Bot
docs/qq.md
WebSocket
No
Matrix
docs/matrix.md
/sync (Long Polling)
No
🎯 Key Features
💬 Session Management
/new [name]       Start a new session
/list             List all sessions
/switch <id>      Switch session
/current          Show current session
/dir [path|reset] Show, switch, or reset work directory
Project configs rotate to a fresh session automatically after long inactivity. This prevents "context drift" where stale chat history (failed commands, debugging noise) is repeatedly re-ingested via
--continue
and starts to dominate the model's attention. The previous session is preserved and remains accessible via
/list
and
/switch
.
[[
projects
]]
reset_on_idle_mins
=
30
#
default when unset; set to 0 to disable
The default is
30 minutes
when unset. Set
reset_on_idle_mins = 0
to opt out and always continue the previous session.
🛡️ OS-User Isolation (
run_as_user
)
On Linux/macOS, a project can spawn its agent under a different Unix
user for OS-level file-system isolation from the supervisor user that
runs cc-connect. Currently supported by Claude Code.
[[
projects
]]
name
=
"
claude-sandboxed
"
run_as_user
=
"
partseeker-coder
"
run_as_env
= [
"
PGSSLROOTCERT
"
]
The target user needs passwordless sudo from the supervisor, no sudo
of its own, read+write on
work_dir
, and its own
~/.claude/settings.json
with whatever credentials the agent uses. If you authenticate via
claude.ai
OAuth, symlink the target user's
~/.claude/.credentials.json
to the supervisor's copy so token refresh stays in sync — see the
environment propagation checklist
for details. See
docs/usage.md
for the full setup.
Before starting cc-connect, audit the setup with:
cc-connect doctor user-isolation
This runs three go/no-go preflight gates and an isolation probe that
reports what the target user can and cannot read. cc-connect refuses to
start if any gate fails or if the probe detects a cross-user leak.
🔐 Permission Modes
/mode             Show available modes
/mode yolo        # Auto-approve all tools
/mode default     # Ask for each tool
🔄 Provider Management
/provider list              List providers
/provider switch <name>     Switch API provider at runtime
🤖 Model Selection
/model                      List available models (format: alias - model)
/model switch <alias>       Switch to model by alias
📂 Work Directory
/dir                         Show current work directory and history
/dir <path>                  Switch to a path (relative or absolute)
/dir <number>                Switch from history
/dir -                       Switch to previous directory
/cd <path>                   Compatibility alias for /dir <path>
⏰ Scheduled Tasks
/cron add 0 6
*
*
*
Summarize GitHub trending
📎 Agent Attachment Send-Back
When an agent generates a local screenshot, chart, PDF, bundle, or other file, it can send that attachment back to the current chat.
First release supports:
Feishu
Telegram
If your agent does not natively inject the system prompt, run this once in chat after upgrading:
/bind setup
or:
/cron setup
This refreshes the cc-connect instructions in the project memory file so the agent knows how to send attachments back.
You can control this feature globally in
config.toml
:
attachment_send
=
"
on
"
#
default: "on"; set to "off" to block image/file send-back
This switch is independent from the agent's
/mode
. It only controls
cc-connect send --image/--file
. Voice send-back uses the TTS config instead.
Examples:
cc-connect send --image /absolute/path/to/chart.png
cc-connect send --file /absolute/path/to/report.pdf
cc-connect send --file /absolute/path/to/report.pdf --image /absolute/path/to/chart.png
cc-connect send --tts
"
Hello from cc-connect
"
Notes:
Absolute paths are the safest option.
--image
and
--file
can both be repeated.
--tts
sends synthesized speech when the user asks for a voice reply.
attachment_send = "off"
disables only attachment send-back; ordinary text replies still work.
Attachments are capped at 50 MiB by default; configure with
max_attachment_size_mb
(or
CC_MAX_ATTACHMENT_SIZE_MB
env, same MiB unit).
This command is for generated attachments, not ordinary text replies.
📖
Full documentation:
docs/usage.md
📚 Documentation
Usage Guide
— Complete feature documentation
INSTALL.md
— AI-agent-friendly installation guide
config.example.toml
— Configuration template
CONTRIBUTING.md
— How to report issues and contribute pull requests
👥 Community
Discord
Telegram
☕ Support the Project
If cc-connect has been helpful to you, consider buying us a coffee! Your support helps us:
🛠️ Maintain and improve the project
📚 Write better documentation and tutorials
🐛 Fix bugs and add new features faster
☕ Keep the developers caffeinated
How to Donate
Buy Me a Coffee
:
https://buymeacoffee.com/cg33
WeChat Pay / Alipay
:
WeChat Pay
Alipay
Thank You, Donors! 🎉
We're grateful to everyone who has supported this project. Leave your GitHub username in the donation message if you'd like to be recognized here!
Avatar
GitHub Username
Date
@thx0701
2026-04-29
🤝 Commercial Cooperation
We accept the following commercial collaborations:
Enterprise Customization
: Custom deployment for internal AI tooling (Feishu, DingTalk, WeChat Work, Slack, etc.)
Technical Consulting
: AI agent integration and architecture design
Outsourcing Projects
: AI-related system development
Contact
:
Email
:
chg80333@gmail.com
|
WeChat
: mongorz |
Telegram
|
Discord
🙏 Contributors
⭐ Star History
📄 License
MIT License
Built with ❤️ by the cc-connect community
About
Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work). Chat with your AI dev assistant from anywhere — no public IP required for most platforms.
Resources
Readme
Contributing
Contributing
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
13.7k
stars
Watchers
26
watching
Forks
1.3k
forks
Report repository
Releases
43
v1.4.1
Latest
Jun 28, 2026
+ 42 releases
Sponsor this project
Uh oh!
There was an error while loading.
Please reload this page
.
ko-fi.com/
chg80333
buymeacoffee.com/
cg33
https://github.com/chenhg5/cc-connect/blob/main/docs/images/alipay.jpg?raw=true
https://raw.githubusercontent.com/chenhg5/cc-connect/refs/heads/main/docs/images/wechatpay.jpg
Packages
0
Uh oh!
There was an error while loading.
Please reload this page
.
Contributors
Uh oh!
There was an error while loading.
Please reload this page
.

### 中文摘要（来自 entries.json curated summary_zh）

> cc-connect 将本地 AI 编程 agent（Claude Code、Codex、Cursor Agent 等 10+ 种）桥接到 11 个主流聊天平台（飞书、钉钉、Telegram、Slack、Discord、微信等），实现从任意设备通过聊天控制本地 AI 编码助手。v1.3.0 新增 Web 管理界面、生命周期钩子、技能管理、个人微信支持等特性，支持 slash 命令切换模型、调整推理级别、管理会话目录和定时任务，无需公网 IP。

### One-liner（来自 entries.json curated one_liner）

> 当前最完整的本地编程 Agent 聊天平台桥接方案，零公网 IP 要求让移动端控制 AI 编码助手成为现实

---

## 中文（基于 README 的要点）

cc-connect 把本地运行的 AI 编程 agent（Claude Code、Codex、Cursor Agent、Kimi CLI、Qoder CLI、Gemini CLI、OpenCode、iFlow CLI、Pi、Devin、GitHub Copilot CLI 等 10+ 种，外加任何兼容 Agent Client Protocol / ACP 的 agent）桥接到 13 个常用聊天平台（飞书 / Lark、WPS 协作、钉钉、Telegram、Slack、Discord、LINE、企业微信、微博、QQ / NapCat / OneBot、QQ 官方 Bot、Matrix，以及个人微信 ilink）。大多数平台都不需要公网 IP（WebSocket / 长连接 / Long Polling 模式），只有 LINE 与企业微信 Webhook 模式需要公网 URL。

v1.3.3（稳定版，约 235 个 PR）带来：
- 新 agent：Devin CLI、Google Antigravity（`agy`）、GitHub Copilot CLI 成为一等公民；Cursor / OpenCode / Qoder / Kimi / Pi 兼容性强化。
- 平台扩展：QQ（OneBot）文件收发、QQ Bot 内联键盘、企业微信 WebSocket 发送文件、飞书音视频原生媒体、Slack Assistant API、DingTalk @提及 / 富文本 / 图片 / 文件入站、微博 DM、WPS 协作。
- 长任务稳健性：新增 `max_turn_time_mins`（软停止 + 强制 kill + 自动 resume），避免长时间 bash/test 锁定会话。
- 新核心命令：`/timer`、`/cancel`、`/ps`、`cron add --silent`、agent 驱动的 TTS。
- 多用户 / 权限：reply-to-unauthorized-IM-senders、`@Bot/permit`、`Bridge` 启用时强制 token。
- Provider 生态：NekoCode、VisionCoder、AIHubMix、MiniMax M3 presets；Claude Code 1M-context Opus + `append_system_prompt` + PermissionRequest hooks；Codex `request_user_input` 事件；可配置 `shell`。
- 可观测性：blackbox 测试框架（P0/P1/P2 + config-switch 矩阵）、CUJ 测试框架、provider-resume 回归套件、Pi context-usage reporter。

⚠️ 行为变更：Telegram / Discord `progress_style` 默认改为 `compact`（可用 `legacy` 还原）；QQ Bot 默认 `intents` 包含 `INTERACTION_CREATE`；DingTalk `msgtype=file` 入站可达 agent；`reset_on_idle_mins` 默认 30 分钟；未配置 token 时 Bridge 拒绝启动。

### 核心特性（README 摘录）

- **多 Agent 编排**：群聊里绑定多个 bot，Claude 与 Gemini 互相对话，共享上下文。
- **完整聊天控制**：`/model`、`/reasoning`、`/mode`、`/dir <path>`、`/cd <path>` 等 slash 命令全部可用。
- **持久记忆**：通过 `/memory` 直接读写 agent 的指令文件，无需打开终端。
- **智能调度**：自然语言创建 cron 任务（例如"每天 6 点汇总 GitHub trending"）。
- **多模态**：语音消息、截图自动 STT/TTS / 多模态转发。
- **多项目架构**：一个进程同时托管多个项目，每个项目独立 agent + 平台组合。
- **多语言界面**：英语、简体中文、繁体中文、日语、西班牙语原生支持。

### 安装与升级

```bash
# npm
npm install -g cc-connect

# Homebrew (macOS / Linux)
brew install cc-connect

# 二进制下载（Linux amd64）
curl -L -o cc-connect https://github.com/chenhg5/cc-connect/releases/latest/download/cc-connect-linux-amd64
chmod +x cc-connect
sudo mv cc-connect /usr/local/bin/

# 源码编译（Go 1.22+）
git clone https://github.com/chenhg5/cc-connect.git
cd cc-connect
make build

# 升级
cc-connect update           # 稳定版
cc-connect update --pre     # 包含 pre-release
```

也可以直接把 `INSTALL.md` 喂给 Claude Code / 任意 AI coding agent，让它自动完成安装与配置。Web 管理界面：`cc-connect web` 启动后浏览器配置，**仍需单独运行 `cc-connect`**。

### 支持矩阵（节选）

| 类型 | 项目 | 状态 |
|---|---|---|
| Agent | Claude Code / Codex / Cursor Agent / Gemini CLI / Qoder CLI / OpenCode / iFlow CLI / Kimi CLI / Pi / Copilot / Devin / ACP 兼容 | ✅ |
| Agent | Goose (Block) / Aider | 🔜 Planned |
| Platform | 飞书 (Lark) — WebSocket | ✅ 无需公网 IP |
| Platform | 钉钉 — Stream | ✅ 无需公网 IP |
| Platform | WPS 协作 — WebSocket | ✅ 无需公网 IP |
| Platform | Telegram — Long Polling | ✅ 无需公网 IP |
| Platform | Slack — Socket Mode | ✅ 无需公网 IP |
| Platform | Discord — Gateway | ✅ 无需公网 IP |
| Platform | 微博 — WebSocket | ✅ 无需公网 IP |
| Platform | LINE — Webhook | ✅ 需要公网 URL |
| Platform | 企业微信 — WebSocket / Webhook | ✅ WS 无需公网 / Webhook 需公网 |
| Platform | 个人微信 ilink — HTTP long polling | ✅ 无需公网 IP |
| Platform | QQ (NapCat / OneBot) — WebSocket | ✅ |
| Platform | QQ Bot 官方 — WebSocket | ✅ 无需公网 IP |
| Platform | Matrix — `/sync` Long Polling | ✅ 无需公网 IP |

### License

MIT License.
