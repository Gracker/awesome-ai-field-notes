# OpenClaw Task: Phase 2 批量分类

## 前置条件
Phase 1 全部批次完成，entries.json 中所有条目 status 为 "score-pending"。

## 目标
将所有 `category: "uncategorized"` 的条目自动分类到正确的二级分类。

## 执行策略
按一级分类逐批处理（每批 ≤100 条）：

1. 从 entries.json 筛选 `category == "uncategorized"` 的条目
2. 读取每条的 `title` + `summary_zh` + `tags`
3. 匹配 `metadata/categories.json` 中的二级分类
4. 置信度 ≥ 0.7 → 自动分类
5. 置信度 < 0.7 → 保持 uncategorized，标记待人工

## 分类关键词映射（参考）
见 task-scan-obsidian.md 中的映射表。

## 每批完成后
```bash
python3 scripts/validate-schema.py
git commit -m "[openclaw] classify: batch N — M entries classified, K uncategorized"
git push origin main
```
