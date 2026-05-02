# OpenClaw Task: 变更日志 (Changelog)

## 目标
生成 CHANGELOG.md，记录本周 `data/entries.json` 的所有变更。

## 仓库路径
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/`

## 执行频率
每周日 04:00（在 dedup 之后运行）

## 执行流程

### Step 1: 对比变更
对比本周 `data/entries.json` 与上周 git 快照的差异：
- **新增条目**：本周 added_date 的条目
- **归档条目**：status 变为 archived 的条目
- **评分变更**：quality_score 发生变化的条目
- **分类变更**：category 发生变化的条目

### Step 2: 分类统计
```markdown
## 分类变更分布
| 分类 | 新增 | 归档 | 评分调整 |
|------|------|------|----------|
| agent-frameworks | +5 | -2 | 1 |
| coding-ai | +3 | 0 | 2 |
```

### Step 3: 生成 CHANGELOG.md
追加到仓库根 CHANGELOG.md（保留最近 12 周，更早的归档）：

```markdown
# Changelog

## 2026-04-06 ~ 2026-04-12

### 📈 新增 (N)
- [标题](url) — agent-frameworks/orchestration ⭐4
- ...

### 📦 归档 (N)
- [标题](url) — 时效归档（180天+score≤3）
- ...

### ✏️ 评分调整 (N)
- [标题](url) — 3→4（补充了深度分析）
- ...

### 📊 统计
- 总条目: XXX → XXX (+N)
- 活跃条目: XXX → XXX (+N)
- 本周最高分新增: [标题](url) ⭐5
```

### Step 4: 提交
```bash
git add CHANGELOG.md
git commit -m "[openclaw] changelog: weekly changelog 2026-WXX"
git push origin main
```

## 约束
- 只记录 active/archived 状态变更，不记录 deprecated
- 评分变更需标注原因（来源：dedup/人工/自动）
- CHANGELOG.md 超过 12 周时，将最早的周归档到 `archive/changelog/`
- 周期范围必须写绝对日期，例如 `2026-05-02 ~ 2026-05-08`，不要写“本周/上周/今天/昨天”
