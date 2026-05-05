# MCP-Flow: 自动构建大规模 MCP 工具数据集，让 0.6B 模型在工具调用上超越 GPT-4o


- **来源**：arxiv
- **作者**：TikTok & 上海交大联合研究
- **原文链接**：https://arxiv.org/abs/2510.24284
- **日期**：2025-10

---

MCP-Flow 提出全自动 pipeline，从 6 个 MCP 市场自动抓取服务器配置，通过 Slot-Fill Revision + WizardLM Evolution 两阶段数据增强，产出 68733 对 instruction-function call（1166 服务器、11536 工具）。实验表明：GPT-4o 在 10 工具场景下 AST 仅 58.8%，100 工具时 Groq-8B AST 跌至 3%；而 MCP-Flow-Qwen3-0.6B 在同场景下 AST 达 81.2%，全面超越所有大模型。用 MCP-Flow 做 RAG 检索增强后，GPT-4o 在 GAIA 任务上成功率 +17%，步数减少 32%。

## English Summary

MCP-Flow proposes a fully automated pipeline to scrape MCP server configs from 6 markets, augment data via Slot-Fill Revision + WizardLM Evolution, producing 68,733 instruction-function call pairs across 1,166 servers and 11,536 tools. Experiments show GPT-4o achieves only 58.8% AST accuracy with 10 tools; Groq-8B drops to 3% at 100 tools. MCP-Flow-Qwen3-0.6B achieves 81.2% AST, surpassing all large models. Using MCP-Flow for RAG retrieval augmentation, GPT-4o's GAIA task success rate improves by 17% with 32% fewer steps.