# OpenClaw Task: Phase 3 批量评分（全自动）

## 前置条件
Phase 2 完成大部分分类，entries.json 中条目已有 category。

## 目标
为所有 `status: "score-pending"` 的条目全自动评分 + 生成 one_liner。

## 规则
- **全自动**：评分、点评、分类全部由 OpenClaw 完成，无需人工确认
- `one_liner_author` 统一为 `"openclaw"`
- `quality_score ≤ 2` → `status: "archived"` 自动归档

## 执行策略
按一级分类逐批处理（每批 ≤50 条）：

1. 从 entries.json 筛选 `status == "score-pending"` 的条目
2. 读取每条的完整 `summary_zh` + `title` + `tags` + `source_type`
3. 基于内容实际质量评分（参考 SCHEMA.md 中的评分依据）
4. 生成 one_liner（判断性语句，基于内容得出）
5. 更新条目：
   - `quality_score`: 1-5
   - `one_liner`: 判断性点评
   - `one_liner_author`: "openclaw"
   - `status`: "active"（score ≥ 3）或 "archived"（score < 3）

## 每批完成后
```bash
python3 scripts/validate-schema.py
npm run build
git commit -m "[openclaw] score: <分类名> — M scored, K archived"
git push origin main
```

## 完成通知
当所有批次完成后，在 Telegram 通知高爷：
- 总入库数
- 分类分布统计
- 站点已自动生成
