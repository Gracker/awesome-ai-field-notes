# AI开发工具链完整方案推荐

- **来源**：X/Twitter
- **原文链接**：https://x.com/RookieRicardoR/status/2044630408894271549
- **作者**：RookieRicardoR
- **日期**：2026-04-17
- **抓取时间**：2026-04-17 12:03

---

Claude Agent Sdk 依然是最快方案，可以通过子进程设置环境变量的方式，兼容所有支持 Claude 协议的模型，比如 GLM、Minimax 之类的，换言之，Claude Code 能支持的用它也都能支持。

Openai 系的模型可以看看 Openai Agent Sdk 或者 Vercel AI SDK，或者直接用整套的 Pi-mono。

上面讲的都是底层，上层是 CLI or 桌面端事件，一般叫做 Runtime，可以用 assistant-ui + 配套的 tools ui。

这个库包装了一层模型时间到 UI 的完整事件流和完整 UI 组件，也可以只用的它的 Runtime 做事件流，自己做 UI 组件，但是这里面的 UI 组件还挺漂亮的。

完整的开源方案，我推荐藏师傅（虽然他把我屏蔽了）的 CodePilot。

宝玉老师推荐的 Craft 也不错。

数据库推荐直接上 better sqlite + F5，记忆层可以单独做可插拔设计，无论是用外部组件还是直接 markdown 都可以。
