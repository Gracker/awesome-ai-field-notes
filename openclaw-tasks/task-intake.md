# OpenClaw Task: 数据入库 (Intake)

## 目标
从 RSS / X / Newsletter / 研究素材中提取有价值条目，写入 `data/entries.json`。

## 执行流程

### Phase 1: 信息源扫描
- 检查 `intake/` 目录是否有待处理素材
- 扫描 Obsidian 知识库中最近 24h 的 AI 相关内容
- 检查本地收藏/书签中的新增内容

### Phase 2: 入库判断
对每个候选条目执行：
1. **去重**: URL 精确匹配 entries.json + 标题相似度 > 0.85
2. **分类**: 根据 title + content 匹配 `metadata/categories.json` 中的二级分类
   - 置信度 ≥ 0.7 → 自动分类
   - 置信度 < 0.7 → `category: "uncategorized"`
3. **评分**: 根据内容质量给出 1-5 分候选
4. **one_liner**: 生成一句话点评候选（必须是判断性语句）

### Phase 3: 写入
- 更新 `data/entries.json`
- 新增条目默认 `status: "active"`
- GitHub 项目: 尝试获取 stars（调用 refresh-stars.py 逻辑）
- 运行 `python3 scripts/validate-schema.py` 确保合规

### Phase 4: 日志
- 在 `logs/` 下写入当日入库日志
- 更新 `metadata/stats.json`

## 约束
- 不修改已有条目的 quality_score（除非人工明确指示）
- one_liner 是核心壁垒，生成候选后需标记待人工审核
- GitHub 项目 stars 为 null 时标记待刷新
- 单次入库不超过 20 条（避免数据质量下降）
