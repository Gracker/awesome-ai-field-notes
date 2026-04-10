# OpenClaw Task: Phase 3 批量评分

## 前置条件
Phase 2 完成大部分分类，entries.json 中条目已有 category。

## 目标
为所有 `status: "score-pending"` 的条目重新评分 + 生成 one_liner 候选。

## 执行策略
按一级分类逐批处理（每批 ≤50 条，评分需要更多思考）：

1. 从 entries.json 筛选 `status == "score-pending"` 的条目
2. 读取每条的完整 `summary_zh` + `title` + `tags` + `source_type`
3. 基于内容实际质量评分（参考 SCHEMA.md 中的评分依据）
4. 生成 one_liner 候选（判断性语句，基于内容得出）
5. 更新条目：
   - `quality_score`: 1-5
   - `one_liner`: 判断性点评
   - `status`: "active"（score ≥ 3）或 "archived"（score < 3）

## 特殊处理
- `quality_score ≥ 4` → 标记 `one_liner_author: "openclaw-pending"` 待人工确认
- `quality_score = 3` → `one_liner_author: "openclaw"` 自动通过
- `quality_score ≤ 2` → `status: "archived"` 直接归档

## 每批完成后
```bash
python3 scripts/validate-schema.py
python3 scripts/generate-site.py
git commit -m "[openclaw] score: <分类名> — M scored, K archived"
git push origin main
```

## 人工审核触发
当所有批次完成后，在 Telegram 通知高爷：
- 总入库数
- 待人工确认的高分条目数（score ≥ 4）
- 分类分布统计
