# OpenClaw Task: Phase 1 批量搬运（提取结构）

## 目标
从 Obsidian 扫描所有 AI 相关 .md 文件，**全自动提取**结构化元数据（分类+评分+点评+摘要）。
提取内容必须来自文件本身，禁止捏造。

## 仓库路径
`<仓库路径>/awesome-ai-field-notes/`
## Obsidian 根
`<Obsidian 根目录>/`

## Schema 参考
读取 `data/SCHEMA.md` 了解完整字段定义和提取规则。

## 规则
- **全自动**：提取、分类、评分、点评全部由 OpenClaw 完成，无需人工确认
- `one_liner_author` 统一为 `"openclaw"`
- Phase 1 直接产出完整条目（分类 + 评分 + one_liner + 摘要），不再分 Phase

## 批次策略（每批 ≤60 条，防超时）

### Batch 1: X 文章（~188 → 分 4 批）
### Batch 2: 论文（~120 → 分 2 批）
### Batch 3: 调研（~303 → 分 6 批）
### Batch 4: DeepResearch + Claude 系列 + AutoResearch（~60 → 1 批）
### Batch 5+: Cubox（~3556 → 分 60 批，每批 60）

## 每批执行流程

### Step 1: 文件发现
```bash
find <目录> -name "*.md" | head -60 | tail -60
```

### Step 2: AI 相关预筛
读取前 300 字符，检查是否包含 AI 相关关键词。
跳过明确非 AI：纯 Android 性能优化、Flutter、人生管理、投资理财、产品推荐（非技术）。

### Step 3: 完整提取（严格从文件提取，禁止捏造）

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
    "category": 自动匹配 metadata/categories.json,  # 直接分类
    "tags": 从 YAML tags + 内容关键词提取（≤8 个）,
    "source_type": 根据目录和内容推断,
    "language": 根据内容语言判断,
    "summary_zh": 从正文提取核心观点（100-300字）,
    "summary_en": 英文原文时提取英文摘要,
    "one_liner": 基于内容生成判断性点评,  # 直接生成
    "one_liner_author": "openclaw",  # 全自动
    "quality_score": 基于 SCHEMA.md 评分依据自动评分,  # 1-5
    "status": "active" if score >= 3 else "archived",
    "local_path": 相对 Obsidian 根的路径,
    "images": 从 ![](url) 正则提取,
    "added_date": "YYYY-MM-DD",  # 绝对日期，禁止 today/今天/昨天 等相对日期
    "updated_date": null,
    "github_stars": null,
    "related": [],
}
```

### Step 4: 去重 + 写入
- URL 精确去重
- 标题精确去重
- 追加到 `data/entries.json`，不要写根目录旧 `entries.json`

### Step 5: 验证 + 提交
```bash
python3 scripts/validate-schema.py
npm run build
git add -A
git commit -m "[openclaw] scan: <目录名> batch N — X entries added"
git push origin main
```

### Step 6: 更新进度
更新 `logs/scan-progress.json`。

## 关键约束
- **禁止捏造**：提取不到的字段设为 null，不编造
- 日期字段只能写 `YYYY-MM-DD` 或 `null`，禁止写“今天/昨天/今日/昨日/today/yesterday”等相对时间
- **摘要必须来自正文**：读文件内容后提取核心观点，不凭标题猜测
- 不手写 `site-src/` 页面；站点只能由 `npm run build` 生成
- **每批完成后必须 git commit + push**：防止丢失进度
- **Cubox 的图片域名**：`image.cubox.pro` 可能已失效，标记但不删除

## 跳过规则（不提取）
- 文件内容 < 50 字符
- 纯 Android 性能优化（无 AI 关键词）
- 个人日记/想法/待办
- 重复文件（同一内容不同日期的 X 抓取，保留最新）
