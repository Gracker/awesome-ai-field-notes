# Cursor 常用提示词手册

> 发布时间: 2024-12-29
> 原文链接: https://baoyu.io/translations/cursor-prompt-manual

---

原文：[Cursor Prompting HandBook](https://twitter-thread.com/t/1873417505550868647)

Cursor 提示手册： 🧵

1.  "修复错误"（Fix Errors）提示

有些时候，像 Sonnet 3.5 这样的 AI 模型会忽略一些重要细节，导致一连串的错误。

可以使用下面的提示来解决这个问题。它将帮助 AI 分析错误的核心原因，然后一步步制定修复计划。

```markdown
@page.tsx I got this error:

Use Chain of thought reasoning to find the core issue of this error, then create a step by step plan to fix the error.
```

2.  "新功能"（New feature）提示

当你成功执行完一个组件后，需要再次指引 AI 查阅文档，让它了解下一个组件的工作范围。

根据以下说明，要求 AI 在执行之前先写一份实现方案。标注相关文档，当 AI 阅读完成后，可能会向你提问。回答它的问题，然后让它执行。

这一做法能避免一半关于每个组件的"幻觉"问题（hallucinations）。

```markdown
Great. Header looks good.

Now we move to "x" section. Refer to @frontend-guidelines.md to understand the scope of work for this feature.

Before implementation if you need more clarification or have any questions, ask me!
```

3.  响应结构（Response structure）

该结构用于通知 AI：我当前的任务完成了，需要继续下一个任务。

1. 提供更新："Header 菜单现在已经完美居中。"
2. 提供下一个任务："现在我们需要一个登录（sign in）和注册（sign up）按钮。"
3. 标注正确的文档："查看 @（文档名称），并解释你将如何实现这些需求。"

```markdown
Header menu is now aligned in center perfectly.

Now we need a sign in and sign up buttons.

Check @frontend-guidelines.md and explain how you will implement this.
```

4.  progress.md 文件

使用这个提示来跟踪所有的工作进度。它可以为 AI 提供上下文，避免重复错误。

"在每个已完成步骤的最后，将你的工作日志记录到 @Progress.md 文件里。

包括以下问题并分步回答，且不要遗漏任何信息：我们实现了哪些功能？我们遇到了哪些错误？我们是如何解决这些错误的？"

5.  project-status.md 文件

AI 应该在上次的工作进度基础上继续。这个文件能帮助 AI 记录工作日志，了解哪些已经完成，哪些还没做。

"在本次会话结束时，将你的工作日志记录到 @project-status.md 文件里。

首先查看 @progress.md 文件，了解我们在本次会话中已经实现了哪些功能。

然后写一份详细的会话报告，为下一次工作会话提供上下文。"

6.  Cursor Agent Hack

Cursor Agent 有时候会做得过头，乱改代码库。

"阅读 @（文档名称）中的说明，以了解本功能的工作范围。

使用链式思考（chain of thought）推理来制定分步实现计划。

确保解释此功能的每个部分是如何运作的，并提供宏观级别的细节。

将内容分解成详细的编号步骤。"

通过这样做，你可以获得一份 AI 即将实现的计划，进而核对所有要求是否一致，并确认是否批准。

这能解决 Cursor Agent 所做的多余编辑。

7.  附件文档

建立一个名为 "Documentation" 或 "Instructions" 的文件夹，把所有核心文档都放进去：

- Project Requirements Doc (PRD)
- App Flow Doc
- Frontend Guidelines Doc
- Backend Structure Doc
- Tech Stack Doc
- File Structure Doc

你可以使用 01 模型，但需要在提示上多加注意（否则可能会有很多无用的内容和段落）。

最好的办法是使用 @CodeGuide 来生成这些文档。我已经为你自动化了这个流程，可以在 20-30 分钟内获得所有所需文档，混合使用 Sonnet 3.5、o1-preview 和 GPT4o 来创建文档。通常，如果仅依靠 ChatGPT，这些文档的阅读、精修、迭代总共需要 7-8 个小时的工作量。