# Anthropic 复盘 Claude Code 质量下降根因：三个互不相关的变更

---

**英文原文：**

Over the past month, we've been looking into reports that Claude's responses have worsened for some users. We've traced these reports to three separate changes that affected Claude Code, the Claude Agent SDK, and Claude Cowork. The API was not impacted. All three issues have now been resolved as of April 20 (v2.1.116).

**中文翻译：**

过去一个月，我们一直在调查有关 Claude 对某些用户响应质量下降的报告。我们将这些报告追溯到三个独立的变化，它们分别影响了 Claude Code、Claude Agent SDK 和 Claude Cowork。API 本身未受影响。截至 4 月 20 日（v2.1.116），所有三个问题均已解决。

---

**英文原文：**

After investigation, we identified three different issues:

- **On March 4**, we changed Claude Code's default reasoning effort from high to medium to reduce the very long latency some users were seeing in high mode. This was the wrong tradeoff. We reverted this change on April 7 after users told us they'd prefer to default to higher intelligence and opt into lower effort for simple tasks.
- **On March 26**, we shipped a change to clear Claude's older thinking from sessions that had been idle for over an hour. A bug caused this to keep happening every turn for the rest of the session instead of just once, which made Claude seem forgetful and repetitive. We fixed it on April 10.
- **On April 16**, we added a system prompt instruction to reduce verbosity. In combination with other prompt changes, it hurt coding quality and was reverted on April 20.

**中文翻译：**

经过调查，我们确认了三个不同的问题：

- **3 月 4 日**，我们将 Claude Code 的默认推理 effort 从 high 改为 medium，以减少部分用户在 high 模式下遇到的过长延迟。这是一个错误的权衡。在用户反馈他们宁愿默认更高智能、主动选择低 effort 处理简单任务后，我们于 4 月 7 日撤销了这一更改。
- **3 月 26 日**，我们推送了一项更改，用于清除空闲超过一小时的会话中 Claude 的旧思维。A bug 导致这在会话剩余的每轮中都持续发生，而非仅发生一次，这让 Claude 显得健忘和重复。我们于 4 月 10 日修复了此问题。
- **4 月 16 日**，我们添加了一条系统提示指令来减少冗长。结合其他提示更改，这损害了代码质量，并于 4 月 20 日被撤销。

---

**英文原文：**

## A caching optimization that dropped prior reasoning

On March 26, we shipped what was meant to be an efficiency improvement to this feature. The design should have been simple: if a session has been idle for more than an hour, we could reduce users' cost of resuming that session by clearing old thinking sections.

**中文翻译：**

## 一个清除先前推理的缓存优化

3 月 26 日，我们推送了本应是此功能的效率改进。设计本应很简单：如果会话空闲超过一小时，我们可以通过清除旧的思维部分来降低用户恢复会话的成本。

---

**英文原文：**

The implementation had a bug. Instead of clearing thinking history once, it cleared it on every turn for the rest of the session. After a session crossed the idle threshold once, each request for the rest of that process told the API to keep only the most recent block of reasoning and discard everything before it. This compounded: if you sent a follow-up message while Claude was in the middle of a tool use, that started a new turn under the broken flag, so even the reasoning from the current turn was dropped.

**中文翻译：**

实现中有一个 bug。它没有只清除一次思维历史，而是在会话剩余的每一轮中都持续清除。一旦会话跨过空闲阈值，该进程剩余的每个请求都告诉 API 只保留最近的推理块并丢弃之前的所有内容。这产生了叠加效应：如果你在 Claude 正在使用工具时发送了后续消息，这会在错误标志下开启新的一轮，因此连当前轮的推理也被丢弃了。

---

**英文原文：**

As part of the investigation, we back-tested Code Review against the offending pull requests using Opus 4.7. When provided the code repositories necessary to gather complete context, Opus 4.7 found the bug, while Opus 4.6 didn't. We fixed this bug on April 10 in v2.1.101.

**中文翻译：**

作为调查的一部分，我们使用 Opus 4.7 对有问题的 Pull Request 进行 Code Review 回测。当提供收集完整上下文所需的代码仓库时， Opus 4.7 发现了这个 bug，而 Opus 4.6 没有。我们于 4 月 10 日在 v2.1.101 中修复了这个 bug。

---

**英文原文：**

## A system prompt change to reduce verbosity

A few weeks before we released Opus 4.7, we started tuning Claude Code in preparation. One addition to the system prompt caused an outsized effect on intelligence in Claude Code: "Length limits: keep text between tool calls to ≤25 words. Keep final responses to ≤100 words unless the task requires more detail."

**中文翻译：**

## 一条减少冗长的系统提示更改

在我们发布 Opus 4.7 的几周前，我们开始为 Opus 4.7 调整 Claude Code。系统提示中的一处增加对 Claude Code 的智能产生了过度影响："长度限制：工具调用之间的文本保持在 25 个词以内。最终回复保持在 100 个词以内，除非任务需要更多细节。"

---

**英文原文：**

As part of this investigation, we ran more ablations using a broader set of evaluations. One of these evaluations showed a 3% drop for both Opus 4.6 and 4.7. We immediately reverted the prompt as part of the April 20 release.

**中文翻译：**

作为此次调查的一部分，我们使用更广泛的评估集进行了更多的消融实验。其中一项评估显示 Opus 4.6 和 4.7 均下降了 3%。我们随 4 月 20 日的版本立即撤销了该提示。

---

**英文原文：**

## Going forward

We are going to do several things differently to avoid these issues: we'll ensure that a larger share of internal staff use the exact public build of Claude Code; and we'll make improvements to our Code Review tool that we use internally, and ship this improved version to customers.

**中文翻译：**

## 展望未来

我们将采取若干不同措施来避免此类问题：我们将确保更多内部员工使用与外部完全一致的 Claude Code 公共版本；我们还将改进内部使用的 Code Review 工具，并将其改进版本交付给客户。
