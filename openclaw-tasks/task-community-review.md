# OpenClaw Task: 社区审核 (Community Review)

## 目标
检查 GitHub Issues，处理社区提交的新资源和纠错请求。

## 仓库路径
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/`

## 执行频率
每日 14:00

## 执行流程

### Step 1: 拉取 Issues
通过 GitHub API 或 `gh` CLI 获取未处理的 Issues：
```bash
gh issue list --repo Gracker/awesome-ai-field-notes --state open --label new-entry
gh issue list --repo Gracker/awesome-ai-field-notes --state open --label correction
```

### Step 2: 处理新资源 (label: new-entry)
对每个新资源 Issue：
1. 提取标题、URL、建议分类
2. 执行去重检查（URL + 标题相似度）
3. 如果不重复：
   - 自动分类（匹配 categories.json）
   - 生成 one_liner 候选（基于 Issue 中的推荐理由）
   - 评分候选（默认 3 分，需人工确认）
   - 写入 entries.json，`one_liner_author: "community-pending"`
4. 在 Issue 中回复处理结果
5. 关闭 Issue

### Step 3: 处理纠错 (label: correction)
对每个纠错 Issue：
1. 验证报告的问题（死链/分类错误/评分异议）
2. 如果是死链 → 运行 check-links.py 确认 → archived
3. 如果是分类错误 → 重新分类 → 更新 entries.json
4. 如果是评分异议 → 标记 `score_review_pending: true`，待人工确认
5. 在 Issue 中回复处理结果
6. 关闭 Issue

### Step 4: 提交
```bash
git add -A
git commit -m "[openclaw] community: process N issues — M entries added, K fixed"
git push origin main
```

## Issue 回复模板

### 新资源已收录
```
✅ 已收录为条目 #XXXX
- 分类: {category}
- 评分候选: {score}/5（待确认）
- one_liner: "{one_liner}"

感谢贡献！评分和点评将经过人工审核后最终确定。
```

### 新资源重复
```
⚠️ 该资源已存在于条目 #XXXX
- 原条目: [{title}]({url})
- 如认为不同，请说明差异，我们会重新评估。
```

### 纠错已修复
```
✅ 已修复
- 问题: {问题描述}
- 处理: {处理方式}
- 变更: {具体变更}
```

## 约束
- 不自动关闭超过 24h 未处理的 Issue（先处理再关）
- 评分异议 **不自动修改** score，只标记待审核
- 社区提交的 one_liner 默认待人工审核
- 每日最多处理 20 个 Issue
