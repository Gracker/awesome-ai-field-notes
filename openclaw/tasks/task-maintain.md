# OpenClaw Task: 存量阶段 — 周维护 (Maintain)

## 前置条件
初始化阶段完成。

## 目标
维护 `data/entries.json` 数据质量。

## 执行频率
每周一 02:00

## 执行流程

### 1. GitHub Stars 刷新
```bash
GITHUB_TOKEN=<token> python3 openclaw/scripts/refresh-stars.py
```

### 2. 可读性门禁
- 运行 `openclaw/scripts/weekly-maintain.py` 时会先检查 active 条目
- 低信号占位、非 AI 内容、无可读摘要/one_liner 的条目 → `score-pending`
- `quality_score` 会降到 ≤2，避免进入首页和频道页

### 3. 时效归档
- `source_type` 为 article 或 x_post
- `added_date` > 180 天
- `quality_score ≤ 3`
→ `status: "archived"`

### 4. 本地路径校验
- 检查所有 active 条目的 `local_path` 是否在 Obsidian 中存在
- 不存在的标记 `local_path_valid: false`（不删除条目）

### 5. 图片校验（抽样）
- 随机抽 20 条含 images 的条目
- HTTP HEAD 检测图片 URL 是否可访问
- 失效的标记但保留

### 5. 统计 + 提交
```bash
python3 scripts/validate-schema.py
npm run build
git add -A
git commit -m "[openclaw] maintain: weekly — N stars refreshed, M archived"
git push origin main
```

## 约束
- 日期字段只能写 `YYYY-MM-DD` 或 `null`，禁止写“今天/昨天/本周/today/yesterday”等相对时间
- 不手写 `site-src/` 页面，生产站输出只能来自 `npm run build` 生成的 `dist/`
- 不强行提交 `dist/`
