# OpenClaw Task: Obsidian 数据全量扫描入库

## 目标
扫描 Obsidian 知识库中所有 AI 相关的 Markdown 文件，提取为 entries.json 条目。

## 仓库路径
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/`

## Obsidian 根目录
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/`

## 扫描范围（按优先级）

### P0 — 高密度 AI 目录（必扫）
| 目录 | 文件数 | 特征 |
|------|--------|------|
| `X 文章/` | ~188 | X/Twitter 抓取，标题含项目名，source_type=x_post |
| `DeepResearch/` | ~12+ | PDF+MD 调研报告，高质量，source_type=article |
| `论文/` | ~120 | AI 论文笔记，source_type=paper |
| `调研/` | ~303 | 调研文档，source_type=article |
| `Claude/` | ~13 | Claude 相关，source_type=article |
| `Claude Code 文档/` | ~28 | Claude Code 文档，source_type=article |
| `AutoResearchClaw研究/` | ~12 | 研究素材，source_type=article |

### P1 — 需过滤的混合目录
| 目录 | 总文件 | AI 相关估计 | 策略 |
|------|--------|-------------|------|
| `Cubox/` | ~4402 | ~3556 | 关键词预筛 + 内容评分，只取 ≥3 分 |
| `OpenClaw定时任务/` | ~1189 | ~800 | OpenClaw 相关，归类 agent-os / coding-ai |
| `性能优化日报/` | ~31 | ~5 | 仅取 AI×Android 交叉内容 |

### P2 — 跳过
- `Android/`、`Android-Internal-Wiki/`、`AndroidWeekly/` → Android 专属
- `小说工坊/`、`Ebook/`、`个人项目/`、`人生管理/` → 非技术
- `每日想法/` → 个人笔记

## 执行流程

### Phase 1: 文件发现与预筛
1. `find` 列出目标目录所有 `.md` 文件
2. 读取每个文件前 500 字符（标题 + 摘要）
3. 跳过明确非 AI 内容（纯 Android 性能、Flutter、人生管理等）

### Phase 2: 信息提取
```python
{
  "title": "从文件名或第一行 # 标题提取",
  "url": "从正文中的第一个 URL 提取",
  "category": "匹配 metadata/categories.json",
  "tags": ["从标题和内容提取关键词"],
  "source_type": "根据目录和内容推断",
  "language": "zh | en | both",
  "one_liner": "判断性一句话（标记 openclaw 待审核）",
  "quality_score": "1-5",
}
```

### Phase 3: 去重与写入
1. URL 精确去重
2. 标题相似度 > 0.85 去重
3. 写入 `data/entries.json`
4. 运行 `python3 scripts/validate-schema.py`

### Phase 4: 生成站点 + 提交
```bash
python3 scripts/generate-site.py
git add -A && git commit -m "[openclaw] intake: scan <目录名> — N entries added" && git push origin main
```

## 分类映射关键词
| 关键词 | 分类 |
|--------|------|
| Claude, GPT, Gemini, 大模型 | models-providers/* |
| LangChain, CrewAI, Agent 框架 | agent-frameworks/* |
| MCP, A2A, ACP | agent-protocols/* |
| OpenClaw, AIOS, 手机 AI | agent-os/* |
| Cursor, Claude Code, Aider | coding-ai/* |
| benchmark, 评测, Arena | benchmarks-evals/* |
| RAG, 向量, 知识库 | rag-knowledge/* |
| vLLM, Ollama, 推理, 量化 | inference-serving/* |
| LoRA, 微调, RLHF | finetuning-training/* |
| prompt, 系统提示 | prompt-engineering/* |
| 图像/视频生成, Sora | multimodal-ai/* |
| ChatGPT, Perplexity, AI 搜索 | ai-products/* |
| 融资, 估值, 战略 | industry-strategy/* |
| 论文, arxiv, 综述 | research-papers/* |
| 教程, 入门, 最佳实践 | tutorials-learning/* |

## 质量评分
| 信号 | 加分 |
|------|------|
| 深度技术分析（>3000字） | +2 |
| 有代码/架构图 | +1 |
| 原创观点 | +1 |
| 权威来源 | +1 |
| 二手整理 | -1 |
| 过时（>1年） | -1 |

## 约束
- 单次扫描 ≤ 200 条（防超时）
- 按目录分批，每批完成后 git commit + push
- Cubox 单独一轮（量大）
- one_liner 标记 `one_liner_author: "openclaw"` 待人工审核
- score ≥ 4 标记待人工确认
