# OpenClaw Task: 去重扫描 (Dedup)

## 目标
检测 entries.json 内部及新增条目的重复，保持数据干净。

## 仓库路径
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/`

## 执行频率
每周日 03:00

## 去重规则

### 硬去重（自动处理）
- **URL 精确匹配**：同 URL 视为重复，保留 score 更高的条目
- **URL 归一化**：去掉尾部 `/`、`?ref=xxx`、`utm_*` 参数后比较

### 软去重（标记待人工）
- **标题相似度 > 0.85**：同分类内标题高度相似，标记 `related` 互相关联
- **跨分类疑似重复**：同一项目出现在不同分类（如 GitHub 项目同时被归为 coding-ai 和 agent-frameworks），保留最匹配的分类

### 处理流程
1. 加载 `data/entries.json`
2. 对所有 active 条目执行 URL 归一化 + 比较
3. 对同分类条目执行标题相似度计算
4. 输出去重报告到 `logs/dedup-report-YYYY-MM-DD.md`
5. 硬去重自动处理（低分条目 → archived）
6. 软去重写入报告，等待人工确认

## 去重报告格式
```markdown
# 去重报告 · YYYY-MM-DD

## 自动处理
- URL 重复: N 对 → 保留高分，低分归档
- URL 归一化重复: N 对 → 已合并

## 待人工确认
- [ ] 标题相似 #entry1 vs #entry2: "标题A" / "标题B"
- [ ] 跨分类重复 #entry3: 同时出现在 coding-ai 和 agent-frameworks
```

## 约束
- 硬去重仅处理 score 差距 ≥ 2 的对（避免误删高质量条目）
- score 相近的重复对只标记不自动处理
- 去重后运行 `python3 scripts/validate-schema.py`
- 去重后运行 `python3 scripts/generate-site.py`
- 提交：`[openclaw] dedup: weekly dedup scan — N merged, M flagged`
