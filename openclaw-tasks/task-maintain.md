# OpenClaw Task: 数据维护 (Maintain)

## 目标
定期维护 entries.json 的数据质量。

## 执行频率
每周一 02:00（OpenClaw cron）

## 执行流程

### 1. GitHub Stars 刷新
```bash
GITHUB_TOKEN=<token> python3 scripts/refresh-stars.py
```

### 2. 时效归档
扫描所有 `status: "active"` 条目：
- `source_type` 为 `article` 或 `x_post`
- `added_date` 距今 > 180 天
- `quality_score ≤ 3`
→ 设置 `status: "archived"`

### 3. 分类修正
扫描 `category: "uncategorized"` 条目，尝试重新分类。

### 4. 统计更新
运行 `python3 scripts/generate-site.py` 更新 stats.json + README。

### 5. 日志
在 `logs/` 下写入维护日志，包含：
- 刷新了多少 stars
- 归档了多少条目
- 修正了多少分类

## 约束
- 归档操作需谨慎，只归档不删除
- deprecated 项目（GitHub archived）不自动恢复
