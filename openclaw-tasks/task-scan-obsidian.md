# OpenClaw Task: Phase 1 批量搬运（提取结构）

## 目标
从 Obsidian 扫描所有 AI 相关 .md 文件，**只提取结构化元数据**，不做分类/评分/点评。
提取内容必须来自文件本身，禁止捏造。

## 仓库路径
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/`
## Obsidian 根
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/`

## Schema 参考
读取 `data/SCHEMA.md` 了解完整字段定义和提取规则。

## 批次策略（每批 ≤60 条，防超时）

### Batch 1: X 文章（~188 → 分 4 批）
- offset 0-60, 61-120, 121-180, 181+
- 元数据区格式固定：`来源`/`原文链接`/`作者`/`日期`

### Batch 2: 论文（~120 → 分 2 批）
- 子目录结构：`论文/AI-YYYY-MM-DD-主题/02-翻译.md` 等
- 优先取 `03-精读.md`（最完整），其次 `02-翻译.md`

### Batch 3: 调研（~303 → 分 6 批）
- 多个子目录，每个子目录可能有多个 .md
- 优先取报告文件（通常文件名含"报告"、"调研"、"对比"）

### Batch 4: DeepResearch + Claude 系列 + AutoResearch（~60 → 1 批）
- DeepResearch/、Claude/、Claude Code 文档/、AutoResearchClaw研究/

### Batch 5+: Cubox（~3556 → 分 60 批，每批 60）
- 量大质杂，先用关键词预筛（AI/LLM/GPT/Agent/大模型/模型/训练/微调/RAG/提示词/benchmark）
- 不命中的直接跳过

## 每批执行流程

### Step 1: 文件发现
```bash
find <目录> -name "*.md" | head -60 | tail -60  # 按 offset 分批
```

### Step 2: AI 相关预筛
读取前 300 字符，检查是否包含 AI 相关关键词。
跳过明确非 AI：纯 Android 性能优化、Flutter、人生管理、投资理财、产品推荐（非技术）。

### Step 3: 结构提取（严格从文件提取，禁止捏造）

```python
entry = {
    "id": generate_id(),
    "title": 从 # 标题或文件名提取,
    "url": 从元数据头提取（原文链接/url/链接）,  # 提取不到设为 null
    "source": {
        "platform": 从来源字段或目录名推断,
        "author": 从作者字段提取,  # 提取不到设为 null
        "original_date": 从日期/发表时间字段提取,  # 提取不到设为 null
    },
    "category": "uncategorized",  # Phase 1 不分类
    "tags": 从 YAML tags + 内容关键词提取（≤8 个）,
    "source_type": 根据目录和内容推断,
    "language": 根据内容语言判断,
    "summary_zh": 从正文提取核心观点（100-300字）,  # 内容<50字则 "内容过短，待补充"
    "summary_en": 英文原文时提取英文摘要,  # 中文原文设为 null
    "one_liner": "待人工点评",  # Phase 1 不写点评
    "one_liner_author": "openclaw",
    "quality_score": 3,  # Phase 1 统一默认 3，待 Phase 3 重新评分
    "status": "score-pending",  # 标记待评分
    "local_path": 相对 Obsidian 根的路径,
    "images": 从 ![](url) 正则提取,
    "added_date": today,
    "updated_date": null,
    "github_stars": null,
    "related": [],
}
```

### Step 4: 去重 + 写入
- URL 精确去重
- 标题精确去重
- 追加到 entries.json

### Step 5: 验证 + 提交
```bash
python3 scripts/validate-schema.py
python3 scripts/generate-site.py
git add -A
git commit -m "[openclaw] scan: <目录名> batch N — X entries added"
git push origin main
```

### Step 6: 更新进度
更新 `logs/scan-progress.json`：
```json
{
  "scanned_dirs": ["X 文章"],
  "current_batch": "X 文章 batch 2/4",
  "total_scanned": 120,
  "total_imported": 95,
  "total_skipped": 25,
  "last_scan": "2026-04-10 13:00"
}
```

## 关键约束
- **禁止捏造**：提取不到的字段设为 null，不编造
- **摘要必须来自正文**：读文件内容后提取核心观点，不凭标题猜测
- **图片只提取 URL**：不下载不处理
- **每批完成后必须 git commit + push**：防止丢失进度
- **Cubox 的图片域名**：`image.cubox.pro` 可能已失效，标记但不删除

## 跳过规则（不提取）
- 文件内容 < 50 字符
- 纯 Android 性能优化（无 AI 关键词）
- 个人日记/想法/待办
- 重复文件（同一内容不同日期的 X 抓取，保留最新）
