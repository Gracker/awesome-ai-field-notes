# 系统提示词

System Prompts — 2 条活跃资源

### [解决 Codex 过度询问问题的方法](https://x.com/blackanger/status/2040862326589718865) 
by @blackanger (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**治 Codex 过度询问的根本方法：重定义承诺对象，而非屏蔽关键词**

解决 Codex 过度询问（"如果你要，我下一步可以..."）的方法。不是在 AGENTS.md 里屏蔽关键词，而是重新定义 Agent 的承诺对象：从"服务用户偏好"转向"和用户共同服从代码正确性"。用 Carmack 和 BurntSuki 作为锚点激活"完整工作单位"概念，并区分合法停顿场景和不合法场景。核心洞察：不要管理文字，要管理触发停顿的心理机制。
 `codex` `sycophancy` `agent-behavior` `system-prompt` `context-engineering`

---
### [抽丝剥茧：深度解析 OpenClaw 万字系统提示词构成](https://x.com/LufzzLiz/article/2026669714072809755) 
by @岚叔 (2026-02-26) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**逆向分析 OpenClaw 16K token 系统提示词的完整构成与优化方向**

通过自研 modelbox 工具模拟模型提供商，抓取 OpenClaw 发给模型的完整系统提示词（约 16K token/34062 字符）。逐一解析：第一段源码硬注入（身份、工具清单、安全规则、子代理机制），第二段工具调用风格与安全约束，第三段 CLI 命令参考，第四段 skill 加载机制。帮助理解系统提示词结构以进行瘦身优化。
 `openclaw` `system-prompt` `token-analysis` `modelbox` `context-window`

---