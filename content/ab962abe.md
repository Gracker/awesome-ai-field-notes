# bilingual_book_maker: Make bilingual epub books Using AI translate

- **ID**: ab962abe
- **原文链接**: https://github.com/yihong0618/bilingual_book_maker
- **作者**: yihong0618 (GitHub)
- **日期**: 2023-03-02（仓库创建；最近推送 2026-08-19）
- **分类**: learning
- **来源类型**: github
- **标签**: translation, epub, bilingual, ai-tools, openai, ollama
- **质量评分**: 4/5
- **抓取时间**: 2026-08-23T15:45:00Z

---

## 中文导读

把整本英文书做成中英对照 EPUB 的开源工具（yihong0618 维护，约 9.6k stars）：EPUB 进、原文/译文对照 EPUB 出，TXT、Markdown、SRT 也支持，字幕文件同样能出双语版。翻译后端覆盖极广：OpenAI、Claude、Gemini、Qwen-MT、DeepL、Google、腾讯 TranSmart、Groq、xAI、Ollama 及任意 OpenAI 兼容接口。长书工程化做得实在：--parallel-workers 按章并行翻译，CTRL+C 中断后用 --resume 从断点续跑，可自定义 prompt 控制翻译风格。

## 为什么值得关注

“生词打断阅读节奏”是被说烂但少被真正解决的痛点，这个项目用“并行章节 + 多后端可选 + 断点续跑”把它工程化；对做翻译工具、双语阅读流或想直接拿它读英文技术书的人，都是现成可用的基础设施。

## 关键信息

- 仓库：yihong0618/bilingual_book_maker（2023-03 创建；9597 stars、最近推送 2026-08-19 @2026-08-23 实测）
- 输入/输出：EPUB / TXT / Markdown / SRT → 双语对照文件
- 后端：OpenAI / Claude / Gemini / Qwen-MT / DeepL / Google / 腾讯 TranSmart / Groq / xAI / Ollama / OpenAI 兼容接口
- 工程特性：--parallel-workers 章级并行、--resume 断点续跑、自定义 prompt、临时双语文件防中断丢失
- 自带测试书：test_books/animal_farm.epub

## English Summary

An open-source tool (yihong0618, ~9.6k stars) that produces bilingual EPUBs: EPUB in, aligned original/translation out; TXT, Markdown and SRT also supported. Backends include OpenAI, Claude, Gemini, Qwen-MT, DeepL, Google, Tencent TranSmart, Groq, xAI, Ollama and any OpenAI-compatible endpoint. --parallel-workers parallelizes chapters, --resume recovers from CTRL+C interruptions, and custom prompts control style.

## 原文要点摘录

> Built-in routes include OpenAI presets and arbitrary OpenAI-compatible model IDs, current Claude choices, Gemini, Qwen-MT, Groq, xAI, OrcaRouter, DeepL, Google, Caiyun, and Tencent TranSmart.

> Use --parallel-workers to process EPUB chapters or Markdown batches/sections in parallel.

> Use --resume option to manually resume the process after an interruption.

## Obsidian Notes

- 内容由 opencli web read 抓取 GitHub README 生成（2026-08-23）。
- 候选来源：X 书签消化 2026-08-23（@Ryrenz 推荐，评分 7.5）；后端列表、并行与断点续跑特性锚定 README 原文，stars 数为 GitHub API 当日实测。
