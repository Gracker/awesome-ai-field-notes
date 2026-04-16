## Pi: The Minimal Agent Within OpenClaw

### English

**Author**: Armin Ronacher
**Published**: 2026-01-31
**Source**: <https://lucumr.pocoo.org/2026/1/31/pi/>

If you haven't been living under a rock, you will have noticed this week that a project of my friend Peter went viral on the internet. It went by many names. The most recent one is OpenClaw but in the news you might have encountered it as ClawdBot or MoltBot depending on when you read about it. It is an agent connected to a communication channel of your choice that just runs code.

What you might be less familiar with is that what's under the hood of OpenClaw is a little coding agent called Pi. And Pi happens to be, at this point, the coding agent that I use almost exclusively.

Pi is written by Mario Zechner and unlike Peter, who aims for "sci-fi with a touch of madness," Mario is very grounded. Despite the differences in approach, both OpenClaw and Pi follow the same idea: LLMs are really good at writing and running code, so embrace this.

### What is Pi?

Pi is a coding agent. And there are many coding agents. Really, I think you can pick effectively anyone off the shelf at this point and you will be able to experience what it's like to do agentic programming.

Pi is interesting to me because of two main reasons:

- **First of all, it has a tiny core.** It has the shortest system prompt of any agent that I'm aware of and it only has four tools: Read, Write, Edit, Bash.
- **The second thing is that it makes up for its tiny core by providing an extension system** that also allows extensions to persist state into sessions, which is incredibly powerful.

A little bonus: Pi itself is written like excellent software. It doesn't flicker, it doesn't consume a lot of memory, it doesn't randomly break, it is very reliable and it is written by someone who takes great care of what goes into the software.

Pi also is a collection of little components that you can build your own agent on top. That's how OpenClaw is built, and that's also how I built my own little Telegram bot and how Mario built his mom.

### What's Not In Pi

The most obvious omission is support for MCP. There is no MCP support in it. While you could build an extension for it, you can also do what OpenClaw does to support MCP which is to use mcporter. mcporter exposes MCP calls via a CLI interface or TypeScript bindings.

This is not a lazy omission. This is from the philosophy of how Pi works. Pi's entire idea is that if you want the agent to do something that it doesn't do yet, you don't go and download an extension or a skill or something like this. **You ask the agent to extend itself.** It celebrates the idea of code writing and running code.

### Agents Built for Agents Building Agents

When you look at what Pi and by extension OpenClaw are doing, there is an example of software that is malleable like clay. Pi's underlying AI SDK is written so that a session can really contain many different messages from many different model providers. It recognizes that the portability of sessions is somewhat limited between model providers.

In addition to the model messages it maintains custom messages in the session files which can be used by extensions to store state. Because this system exists and extension state can also be persisted to disk, it has built-in hot reloading so that the agent can write code, reload, test it and go in a loop until your extension actually is functional.

Even better: **sessions in Pi are trees.** You can branch and navigate within a session which opens up all kinds of interesting opportunities such as enabling workflows for making a side-quest to fix a broken agent tool without wasting context in the main session.

### Tools Outside The Context

An extension in Pi can register a tool to be available to the LLM to call. But for the most part all of what I'm adding to my agent are either skills or TUI extensions to make working with the agent more enjoyable.

Beyond slash commands, Pi extensions can render custom TUI components directly in the terminal: spinners, progress bars, interactive file pickers, data tables, preview panes. The TUI is flexible enough that Mario proved you can run Doom in it.

### Extensions

- **`/answer`** — reads the agent's last response, extracts all questions, and reformats them into a nice input box
- **`/todos`** — brings up all items stored in `.pi/todos` as markdown files; both the agent and I can manipulate them
- **`/review`** — branches into a fresh review context, get findings, then bring fixes back to the main session
- **`/control`** — lets one Pi agent send prompts to another; a simple multi-agent system
- **`/files`** — lists all files changed or referenced in the session

### Software Building Software

The point of it mostly is that none of this was written by me, it was created by the agent to my specifications. I told Pi to make an extension and it did. There is no MCP, there are no community skills, nothing. Don't get me wrong, I use tons of skills. But they are hand-crafted by my agent and not downloaded from anywhere.

Part of the fascination that working with a minimal agent like Pi gave me is that it makes you live that idea of using software that builds more software. That taken to the extreme is when you remove the UI and output and connect it to your chat. That's what OpenClaw does and given its tremendous growth, I really feel more and more that this is going to become our future in one way or another.

---

### 中文

**Pi：OpenClaw 中的极简 Agent**

**作者**: Armin Ronacher
**发布**: 2026-01-31

如果你不是住在岩石下面，本周你一定注意到我朋友 Peter 的一个项目在网上火了。它有过很多名字，最近叫 OpenClaw，但新闻里你可能见过 ClawdBot 或 MoltBot。它是一个连接到你选择的通信渠道的 agent，核心就是运行代码。

你可能不太熟悉的是，OpenClaw 引擎之下是一个叫 Pi 的小型编程 agent。而 Pi 恰恰是目前我几乎排他性使用的编程 agent。

Pi 由 Mario Zechner 编写，与追求"带点疯狂的科幻感"的 Peter 不同，Mario 非常务实。尽管方法不同，OpenClaw 和 Pi 遵循相同的理念：LLM 擅长写代码和运行代码，那就拥抱这一点。

### 什么是 Pi？

Pi 是一个编程 agent。现在编程 agent 很多，基本上你随便拿一个都能体验到 agentic programming 是什么感觉。

Pi 让我感兴趣主要有两个原因：

- **首先，它的核心极小。** 它的系统提示词是我见过所有 agent 中最短的，只有四个工具：Read、Write、Edit、Bash。
- **其次，它用扩展系统弥补了核心的精简。** 扩展还能将状态持久化到会话中，这非常强大。

额外的好处：Pi 本身就像优秀的软件一样编写。不闪烁、不消耗大量内存、不会随机崩溃，非常可靠。

Pi 也是一组小组件，你可以在其上构建自己的 agent。OpenClaw 就是这么构建的，我的 Telegram bot 和 Mario 的 mom 也是。

### Pi 中没有什么

最明显的缺失是 MCP 支持。这并非偷懒，而是来自 Pi 的哲学：如果你想让 agent 做它还不会做的事，不是去下载扩展或技能，而是**让 agent 自己扩展自己**。它崇尚的是写代码和运行代码的理念。

### 为构建 Agent 的 Agent 而构建的 Agent

Pi 和 OpenClaw 展示了一种像粘土一样可塑的软件。Pi 的底层 AI SDK 被设计为会话可以包含来自不同模型提供商的多种消息。它还维护会话文件中的自定义消息，供扩展存储状态。

由于这个系统和扩展状态可以持久化到磁盘，它内置了热重载——agent 可以写代码、重载、测试并循环直到扩展真正可用。**Pi 的会话是树结构**，你可以分支和导航，比如在不浪费主会话上下文的情况下去修复一个坏掉的工具。

### 软件构建软件

最重要的是，这些都不是我写的，都是由 agent 按照我的规格创建的。我告诉 Pi 做一个扩展，它就做了。没有 MCP，没有社区技能，什么都没有。我确实用了很多技能，但它们都是由我的 agent 手工制作的，不是从哪里下载的。

与 Pi 这样的极简 agent 合作的迷人之处在于，它让你真正体验"软件构建软件"的理念。推向极致就是去掉 UI 和输出，连接到你的聊天——这就是 OpenClaw 做的事。考虑到它的巨大增长，我越来越觉得这将以某种方式成为我们的未来。
