# OpenClaw Task: 存量阶段 — 周维护 (Maintain)

## 前置条件
初始化阶段完成。

## 目标
维护 entries.json 数据质量。

## 执行频率
每周一 02:00

## 执行流程

### 1. GitHub Stars 刷新
```bash
GITHUB_TOKEN=<token> python3 openclaw/scripts/refresh-stars.py
```

### 2. 时效归档
- `source_type` 为 article 或 x_post
- `added_date` > 180 天
- `quality_score ≤ 3`
→ `status: "archived"`

### 3. 本地路径校验
- 检查所有 active 条目的 `local_path` 是否在 Obsidian 中存在
- 不存在的标记 `local_path_valid: false`（不删除条目）

### 4. 图片校验（抽样）
- 随机抽 20 条含 images 的条目
- HTTP HEAD 检测图片 URL 是否可访问
- 失效的标记但保留

### 5. 统计 + 提交
```bash
npm run build
git add -A
git commit -m "[openclaw] maintain: weekly — N stars refreshed, M archived"
git push origin main
```
