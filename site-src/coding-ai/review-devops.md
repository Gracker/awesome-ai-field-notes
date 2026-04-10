# 代码审查与DevOps

Code Review & DevOps — 3 条活跃资源

### [Claude Code + Codex 双模型审查流程](https://x.com/runes_leo/status/2027269214524903892) 
by @Leo (2026-02-28) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**双模型代码审查：Opus 写、Codex 审，消除盲区**

写代码的模型永远不负责审自己的代码。Claude Code 跑 Opus 4.6 写完功能，通过 MCP 协议接入 Codex MCP Server 让 Codex 审查。审完列问题，回到 Opus 逐个修，循环到没新问题。原理：自己写的东西自己审永远有盲区，换一个不同思路的 AI 审你的 AI。成本多一轮对话的钱但省掉的返工时间远超。
 `claude-code` `codex` `code-review` `mcp` `dual-model`

---
### [从 MCP 到 SKILL：关于 Agent 扩展机制的思考](https://x.com/jolestar/status/2011461813767155828) 
by @jolestar (2026-03-01) | ⭐⭐⭐⭐ 4/5 | 🌍

**Agent 相关：从 MCP 到 SKILL：关于 Agent 扩展机制的思考**

从 MCP 到 SKILL：关于 Agent 扩展机制的思考
去年 MCP 爆火，大家一度有种感觉：只要把工具都接进来，AI Agent 就会“活”过来，像一个长了手脚的人，什么都能干。
如果把 LLM 看作大脑（智力引擎），tool call / function call 就像让它能指挥四肢：模型填参数，代码去执行，再把结果喂回去继续推理。
MCP（Model Context Protocol）把这套机制做成了“标准插头”：以前各家服务各自一套 SDK + API，你要给 Agent 封装工具，就得处理语言、依赖、鉴权、返回格式，复杂度会指数上升；MCP 的价值是把“接入”这件事工程化、标准化。
所以当时最乐观的推论很自然：只要 MCP 工具够多，Agent 就有无限多的手脚，什么都能干了。
但很快大家就撞墙了。
第一堵墙：容量瓶颈（上下文预算）
工具的定义本身要进入系统 prompt 或等价的工具上下文；工具越多，占用越多，留给“干活”的空间越少。
 `mcp` `agent` `prompt-engineering` `skill` `coding` `context-management` `github`

---
### [认知重建之后，步入Agentic Engineering的工程革命](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649801026&idx=1&sn=3e12f0888b3c232ed7218caf90df5f0a&chksm=bf4c0f3ab8ef6ca21c04e80f8bfce44dae41e5b6e72e1f523bbcf88da8f6d03e4f1056efb689&mpshare=1&scene=1&srcid=0331LA6BLBJmhKZPFBdhCoO4&sharer_shareinfo=91bd93888a0e7958e77c5a12d0cbd198&sharer_shareinfo_first=91bd93888a0e7958e77c5a12d0cbd198) 
 (2026-03-31) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 认知重建之后，步入Agentic Engineering的工程革命**

?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2Fj3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D0)


---