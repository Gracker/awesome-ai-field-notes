---
title: 'Anthropic 今天发了一个新产品，可能会让一批做 AI 智能体基础设施的团队失业'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# Anthropic 今天发了一个新产品，可能会让一批做 AI 智能体基础设施的团队失业

> 中文深度解析 Claude Managed Agents 的产品定位、架构设计与企业案例

🔗 [原文链接](https://x.com/dotey/status/2042017036931305667) | @dotey | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-06

`claude` `managed-agents` `anthropic` `enterprise` `agent-infrastructure`

---

# Anthropic 今天发了一个新产品，可能会让一批做 AI 智能体基础设施的团队失业


https://t.co/b0FvxN8sLs

新時代的大廠開始圈地，打造護城河了：賣token->賣服務->賣基建

AWS 只賣算力。
你的產品缺什麼基礎設施，AWS 說了不算。
Anthropic 不一樣。
它一邊賣 agent 基礎設施，一邊決定 Claude 還需要多少 harness。
所以像 LangChain、CrewAI 這類第三方 Agent 基建團隊，處境會越來越被動。
他們今天替模型補上的能力，明天可能就被 Claude 自己升級掉。

Notion 讓用戶在工作區裡直接把編碼、做 PPT、整理表格這些活扔給 Claude，幾十個任務並行跑，整個團隊在同一個輸出上協作。

將來有一天，人們回頭看，也許會發現 Anthropic 推出 Managed Agents，對 Agent 產業的意義，和當年 AWS 推出 EC2 對云计算的意義一樣深远。

EC2 改變的，不只是服務器部署方式，而是把原本沉重、緩慢、依賴人工管理"寵物"的物理算力，變成了可以通過 API 按需獲取、彈性擴展"牛群"的公共能力。

現在，Managed Agents 正在對 Agent 做類似的事。它把原本需要團隊自己拼裝和維護的編排循環、工具調用、會話管理、沙箱、重試和運行時，收斂成一個可直接調用的托管層。開發者不再需要反覆搭底座，而是把重心放到真正創造價值的部分: 業務工作流、領域上下文、工具接口、權限邊界，以及與 Agent 的協作方式。

如果說 EC2 把計算資源變成了公共基礎設施，那麼 Managed Agents 可能正在把 Agent Runtime變成新的公共基礎設施。
