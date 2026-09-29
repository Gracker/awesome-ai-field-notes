[跳转到主要内容](#main-content) [ZhiJun Blog](/)

* [博客](/posts)
* [周报](/briefs)
* [Wiki](/wiki)
* [标签](/tags)
* [跑步](/running)
* [聚合](/feeds)
* [关于](/about)

[首页](/)/[博客](/posts)

# 让Claude 和 Codex 告诉我需要哪些工具才能更快地运行

4 分钟阅读·

2026-03-30

最近看到一篇文章《[Claude Code told me what tools it needs to work faster. Oh boy I was missing so many things.](https://sderosiaux.substack.com/p/claude-code-told-me-what-tools-it)》。作者通过一次让 **Claude Code** 自查环境的实验，整理出 **ripgrep、fd、fzf、DuckDB、git-delta、xh、watchexec、just、semgrep** 等能显著提升 AI 编码助手效率的工具，并指出：**提升效果不只靠改 prompt，还要把 AI 当成需要「趁手 CLI」的协作者。**

出于好奇，我分别向 **Codex** 和 **Claude** 提了同一个问题：

> **为了有效地帮助我解决问题，您还缺少哪些工具？请分析已安装的软件、缺失的软件、损坏的软件和冗余的软件，并按对您帮助我的能力的影响程度排序。**

下面是我的记录与取舍。

## Codex

我向 Codex 提问：

![我向 Codex 提问](https://cos.zhijun.io/images/what-tools-it-needs-for-claude-codex/01.webp)

它的回答：

![Codex回答](https://cos.zhijun.io/images/what-tools-it-needs-for-claude-codex/02.webp)

我让 Codex 整理成报告，其中 **缺失项**大致如下。

**P0**

| 工具 | 说明 |
| --- | --- |
| `gh` | GitHub CLI，影响 PR、issue、release、workflow 等 |
| `psql` | PostgreSQL 客户端，影响连库与 SQL 验证 |
| `gradle` | Gradle 项目构建与依赖检查 |

**P1**

| 工具 | 说明 |
| --- | --- |
| `redis-cli` / `mysql` | 缓存与关系库排查 |
| `poetry` | Python 若用 Poetry 管理依赖 |
| `deno` | 仅 Deno 项目明显相关 |
| `playwright` | 浏览器自动化脚本通道 |

**我的取舍**：本地开发多用 **Docker** 跑数据库与中间件，因此**不会**在本机装 `psql` / `redis-cli` / `mysql` 等；**Gradle** 不常用，也未装。唯一打算补的是 **`gh`**。按 Codex 的提示，我还删掉了一部分冗余版本软件。

## Claude

我向 Claude 提问：

![我向 Claude 提问](https://cos.zhijun.io/images/what-tools-it-needs-for-claude-codex/03.webp)

Claude 给出的**最小修复清单**（截图）：

![Claude 给出的最小修复清单](https://cos.zhijun.io/images/what-tools-it-needs-for-claude-codex/04.webp)

**我的决策**：

* **`gh`、Gradle**：可以安装（Gradle 若项目需要再装）。
* **`kubectl`**：本机不用，可卸。
* **Docker**：编排用 **OrbStack**，不装 Docker Desktop。

按提示执行的大致步骤如下（请按需裁剪；**不要盲目照抄 `brew untap` 等**，除非你清楚含义）：

Terminal window

```
echo "=== 1. 安装 Xcode CLI Tools ==="

xcode-select --install

echo "=== 2. 安装缺失的关键工具 ==="

brew install gh

echo "=== 3. 配置语言环境（若使用 Rust）==="

rustup default stable

echo "=== 4. 清理 Homebrew（按需）==="

brew untap homebrew/bundle   # 仅在你确认需要时

brew link certifi

brew link kubernetes-cli

brew cleanup --prune 30

echo "=== 5. 更新包 ==="

brew update && brew upgrade
```

## 补齐「现代 CLI」

参考同一篇英文文章，Claude **一开始没有**主动列出 **ripgrep、fd、fzf、DuckDB、xh、git-delta** 等。我让它对照原文再分析：

![对照原文再分析](https://cos.zhijun.io/images/what-tools-it-needs-for-claude-codex/05.webp)

之后 Claude 按类别整理了**已安装 / 建议安装 / Shell 集成**，核心表格如下（节选）。

**文件搜索与导航**：`fd`、`ripgrep`、`fzf` —— AI 少在路径和搜索上犯错。

**输出增强**：`bat`、`git-delta`、`eza` —— 读文件、看 diff、列目录更清晰。

**数据处理**：`jq`、`yq`、`duckdb` —— JSON/YAML/轻量 SQL。

**HTTP**：`xh`（以及可选 `httpie`）。

**代码质量**：`semgrep`。

**自动化**：`just`、`watchexec`。

**文本**：`sd`。

**推荐再装**（按需）：`tldr`、`procs`、`bottom`、**Nushell** 等。

### Shell 集成（示例）

**fzf**（若用 Homebrew 安装）：

~/.zshrc

```
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# 或执行: /opt/homebrew/opt/fzf/install
```

**just** 的 zsh 补全（不要用 fish 的 `psub` 语法）：

~/.zshrc

```
eval "$(just --completions zsh)"
```

**eza / bat** 别名可放在 `~/.zshrc` 或统一的 `~/.aliases` 里，与 dotfiles 保持一致即可。

### 项目级示例

**justfile**（我把以前的 go-task 迁到 just，按需保留）：

```
test:

cargo test

build:

cargo build

dev:

watchexec -e rs,toml cargo run
```

**semgrep** 规则示例仅作演示，实际项目需按语言与框架调整。

### 使用频率（主观）

| 频率 | 工具 |
| --- | --- |
| 每日 | `fd`、`rg`、`fzf`、`bat`、`jq` |
| 每周 | `xh`、`just`、`duckdb`、`semgrep` |
| 偶尔 | `sd`、`watchexec`、`yq` |

更多用法可参考《[命令行四件套：fd/rg/fzf/bat](https://atbug.com/cli-essentials-fd-rg-fzf-bat/)》。

## dotfiles 与 Brewfile

我有一份 macOS 重装后的初始化配置 **[dotfiles](https://github.com/zhijunio/dotfiles)**（私有仓库时以本地为准），并让 Claude 按**已装软件**对齐 **Brewfile**。

![让 Claude 按已装软件对齐 Brewfile](https://cos.zhijun.io/images/what-tools-it-needs-for-claude-codex/06.webp)

成文时的结构大致是：**Taps**（如 **`sdkman/tap`**、`tw93/tap`；注意拼写是 **sdk** 不是 sak）→ **命令行 brew**（可先集中一块 **「开发工具」**，如 `gh`、`fnm`、`uv`、`pandoc`；其余如 `fd`、`ripgrep`、`fzf`、`bat`、`just`、`xh` 等）→ **图形 cask**（编辑器、浏览器、OrbStack、Kaku、cc-switch 等）。**完整列表与注释以仓库内最新 `Brewfile` 为准**，避免博文与仓库长期漂移；安装方式：`brew bundle install`。

## 小结

1. **Codex** 更偏「缺什么数据库/构建客户端」，和你在本机是否用容器跑服务强相关；**Claude** 在追问后更能对齐「文章里那套 AI 友好 CLI」。
2. **共同点**：**`gh`** 对 GitHub 工作流帮助大，值得装。
3. **fd / rg / fzf / bat** 这类工具，投入小、和 AI 读仓库、跑命令的习惯契合度高，适合写进 **Brewfile** 长期维护。
4. 自动化脚本里的 **`brew untap`**、**`rustup`** 等，只在你真实需要时执行；**容器编排**用 OrbStack 即可，不必重复装 Docker Desktop。

* [ai](/tags/ai)
* [tools](/tags/tools)

### 订阅与分享

订阅文章

### 订阅更新，不错过后续文章

直接通过 RSS 和 Telegram 订阅本站更新。

[订阅 RSS](/rss.xml)  [关注 Telegram](https://t.me/zhijunio)

分享文章

### 如果这篇有帮助，可以顺手转发

直接分享给同事、朋友，或者发到你的社交平台。

[分享到 X](https://x.com/intent/tweet?text=%E8%AE%A9Claude%20%E5%92%8C%20Codex%20%E5%91%8A%E8%AF%89%E6%88%91%E9%9C%80%E8%A6%81%E5%93%AA%E4%BA%9B%E5%B7%A5%E5%85%B7%E6%89%8D%E8%83%BD%E6%9B%B4%E5%BF%AB%E5%9C%B0%E8%BF%90%E8%A1%8C%20%7C%20ZhiJun%20Blog&url=https%3A%2F%2Fblog.zhijun.io%2Fposts%2Fwhat-tools-it-needs-for-claude-codex)  [分享到 Telegram](https://t.me/share/url?url=https%3A%2F%2Fblog.zhijun.io%2Fposts%2Fwhat-tools-it-needs-for-claude-codex&text=%E8%AE%A9Claude%20%E5%92%8C%20Codex%20%E5%91%8A%E8%AF%89%E6%88%91%E9%9C%80%E8%A6%81%E5%93%AA%E4%BA%9B%E5%B7%A5%E5%85%B7%E6%89%8D%E8%83%BD%E6%9B%B4%E5%BF%AB%E5%9C%B0%E8%BF%90%E8%A1%8C%20%7C%20ZhiJun%20Blog)  [邮件分享](/cdn-cgi/l/email-protection#9ca3efe9fef6f9ffe8a1b9d9a4b9ddd9b9dda5dff0fde9f8f9b9aeacb9d9a9b9a5aeb9a4dfb9aeacdff3f8f9e4b9aeacb9d9a9b9a5adb9a4ddb9d9a4b9dddab9a4a5b9d9aab9a4a4b9a5adb9d9a5b9a5dfb9a4acb9d9a4b9ddaab9a4adb9d9a9b9a5afb9ddddb9d9a8b9deddb9a5deb9d9a9b9deabb9dda9b9d9a9b9a4a9b9deabb9d9aab9a4a5b9a4d8b9d9a4b9a4afb9ded8b9d9aab9a5deb9dea8b9d9a9b9dedab9dddeb9d9a9b9a5dfb9deacb9d9a4b9dedab9a5acb9d9a4b9ddadb9a4dfb9aeacb9abdfb9aeacc6f4f5d6e9f2b9aeacdef0f3fbbafdf1eca7fef3f8e5a1b9d9a4b9ddd9b9dda5b9aeacdff0fde9f8f9b9aeacdff3f8f9b9aeacb9d9a8b9dea4b9a4d9b9aeacdff3f8f9e4b9aeacb9d9a4b9a4abb9ddddb9d9aab9a5dab9dda9b9d9aab9a5dfb9dddfb9d9aab9a5dfb9deddb9d9a9b9dedfb9a4acb9d9a9b9a4dab9a5adb9d9abb9a4d9b9dddab9d9a9b9ddaeb9a4afb9d9dab9dedfb9a5ddb9d9a9b9dddab9dea5b9d9aab9dddab9a5a8b9d9a8b9deddb9a4dfb9d9a4b9a4acb9a4a9b9d9abb9dedeb9a5a5b9d9a9b9a4abb9deddb9d9abb9a5ddb9a4a8b9d9abb9dedfb9deddb9d9a9b9dda8b9deadb9d9a9b9deabb9dda9b9d9a9b9a4a9b9deabb9d9aab9dea4b9a4a9b9d9a9b9a4d8b9a5a9b9d9dab9dedfb9a4dfb9d9a9b9dea5b9deaab9d9a4b9ddadb9dda9b9d9a5b9ded8b9a5acb9aeaceef5ecfbeef9ecb9d9afb9a4acb9a4adfaf8b9d9afb9a4acb9a4adfae6fab9aeacb9d9abb9ddd8b9a4a5b9d9a8b9dea4b9a4d9b9aeacddd5b9aeacb9d9a9b9a4d8b9a4dab9d9a8b9ded8b9a5dfb9d9abb9a5deb9dea4b9d9a9b9a4a9b9deafb9d9abb9a5ddb9a4a8b9aeacdfd0d5b9aeacb9d9a9b9deabb9dda9b9d9a9b9a4a9b9deabb9d9a5b9a5afb9ded9b9d9afb9a4acb9a4aeb9acddb9acddf4e8e8ecefb9afddb9aedab9aedafef0f3fbb2e6f4f5f6e9f2b2f5f3b9aedaecf3efe8efb9aedaebf4fde8b1e8f3f3f0efb1f5e8b1f2f9f9f8efb1faf3eeb1fff0fde9f8f9b1fff3f8f9e4)

### 相关文章

ai / tools

[从 Vim 到 AI：开发工具这些年](/posts/programming-tools-evolution-timeline)

按年代梳理编辑器、IDE、云原生到 Copilot 与 Cursor：一张时间线看懂工具链怎么变。个人整理，方便收藏对照。

ai / openclaw / hermes

[2026-04-12｜OpenClaw 迁移到 Hermes](/briefs/20260412-week-review)

本周记录：将 OpenClaw 迁移到 Hermes Agent、博客评论系统从 Artalk 切换到 Giscus、发表 5 篇技术博文与 10 篇公众号文章…

ai / openclaw

[普通人如何用小龙虾记日记](/posts/how-to-use-xiaolongxia-diary)

用 OpenClaw 小龙虾轻松记日记，无需打开 App、不用排版整理，随手发送即可自动按日期归档。适合普通人的碎片化记录方法。

ai / spring-ai / skillsjars

[SkillsJars：用 Maven 依赖管理 AI Agent Skills](/posts/skillsjars-quickstart)

介绍 SkillsJars 是什么、如何使用（AI 代码助手和 Spring AI）以及如何创建和发布 SkillsJars。

ai

[2026-04-05｜AI 翻译英文文章](/briefs/20260405-week-review)

本篇博客介绍最近一周（2026-03-30 ～ 2026-04-05）的记录与思考。 摘要

tools

[Obsidian 的 CEO 是如何做知识管理的](/posts/how-obsidian-ceo-does-knowledge-management)

根据 Steph Ango（kepano）《How I use Obsidian》等文整理的用法笔记：库结构、Bases、内链与分形日记、模板属性、评分与发稿，…

 [2026-03-29｜翻译技能迭代、重启公众号](/briefs/20260329-week-review)  [IntelliJ IDEA 2026.1，真正有用的只有这 5 个变化](/posts/intellij-idea-2026-1)

---

© 2026 ZhiJun. All rights reserved.