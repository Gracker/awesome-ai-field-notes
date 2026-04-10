# 贡献规范

## OpenClaw 操作规范

### Commit Message 格式

```
[openclaw] <type>: <描述>
```

Type 类型：
- `intake` — 新增条目入库
- `update` — 更新条目（stars/状态/评分）
- `archive` — 归档条目
- `remove` — 移除条目
- `meta` — 更新元数据（stats/categories/changelog）
- `site` — 重新生成站点

示例：
```
[openclaw] intake: 新增 3 条 agent-frameworks 条目
[openclaw] update: 刷新 15 个 GitHub 项目 stars
[openclaw] archive: 5 条 180 天时效归档
```

### entries.json 操作规则

1. **只操作 `data/entries.json`**，其他文件均为派生
2. 去重：URL 精确匹配 + 标题相似度 > 0.85 视为重复
3. 分类：根据 title + content 自动匹配二级分类，置信度 < 0.7 标记 `category: "uncategorized"`
4. one_liner：**必须是判断性语句**（如"目前最实用的多 Agent 编排框架"），非描述性语句
5. quality_score：OpenClaw 可生成候选分数，但 **≥ 4 分的必须人工确认**

### 维护规则

- GitHub 项目：每周刷新 stars，archived 项目 → `status: "deprecated"`
- 死链：连续 3 次 HTTP 检测失效 → 移除
- 时效归档：`source_type: article | x_post` 且 `added_date > 180 天` 且 `score ≤ 3` → `status: "archived"`

## 社区贡献指南

### 可以做的

- 提交新条目（通过 Issue 模板）
- 修正事实性错误
- 提交更好的 one_liner（需审核）
- 报告死链

### 不能做的

- 直接修改 quality_score
- 直接修改 status
- 直接修改 category（可建议）

### Issue 模板

**新条目提交** 请包含：
- 标题和 URL
- 建议分类（可选）
- 一句话推荐理由（可选，会作为 one_liner 候选）

**纠错** 请包含：
- 条目 ID 或 URL
- 错误描述
- 正确信息（附来源）

## Review 时效

- 新条目入库：48 小时内完成分类和初步评分
- 社区 Issue：7 天内响应
- one_liner 审核入库条目：每周批量处理
