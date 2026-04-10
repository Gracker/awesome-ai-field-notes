# 知识图谱

Knowledge Graphs — 2 条活跃资源

### [用 LLM + Obsidian 构建个人知识库：基于 Karpathy 的"LLM Knowledge Bases"工作流](https://x.com/yanhua1010/status/2039966047378583815) 
by @yanhua1010 (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**将 Karpathy 的 LLM 知识库方法论落地到 Obsidian，类比 CI/CD 的增量编译**

基于 Karpathy 的 LLM Knowledge Bases 工作流，将知识库管理类比为 CI/CD：原始资料→编译产物→运行时输出三层分离。用 Obsidian + Claude Code 实现三层目录结构：raw/（摄取）、wiki/（编译成品）、平台目录（发布）。三个摄取入口（Web Clipper、Podwise、手动剪藏），编译环节包含逐篇摘要、概念抽取、索引更新。强调增量编译和质量保障。
 `obsidian` `llm` `knowledge-base` `karpathy` `compile` `ci-cd`

---
### [LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595) 
by @Andrej Karpathy (2026-04-05) | ⭐⭐⭐⭐ 4/5 | 🌐

**Karpathy 的 LLM 知识库工作流：把 raw data 编译成 wiki，用 Obsidian 查看，不需要 fancy RAG。**

Karpathy 分享他用 LLM 构建个人知识库的工作流：raw/ 目录存放原始文档，LLM 增量"编译"成 .md wiki（含摘要、反向链接、概念分类文章）；用 Obsidian 作为 IDE 前端查看原始数据、编译产物和可视化；wiki 达到约 100 篇文章/40 万字后，可以直接向 LLM agent 提问复杂问题。关键发现：不需要 fancy RAG，LLM 自己会维护索引文件和文档摘要。输出形式包括 Markdown 文件、幻灯片（Marp 格式）、matplotlib 图像。还会用 LLM 做 wiki 健康检查（不一致数据、缺失数据、新文章候选）。
 `LLM` `知识库` `Obsidian` `Markdown` `RAG` `个人知识管理`

---