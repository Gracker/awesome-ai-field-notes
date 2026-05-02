# OpenClaw Task: 社区内容自动处理（全自动）

## 目标
自动处理社区提交的 Issue（新条目/纠错），合并到 `data/entries.json`。

## 仓库路径
`/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/`

## 执行频率
每日 14:00

## 规则
- **全自动**：分类、评分、点评全部由 OpenClaw 完成，无需人工确认
- `one_liner_author` 统一为 `"openclaw"`
- 社区不能直接修改 score/status/category（由 OpenClaw 自动判定）

## 执行流程

### Step 1: 拉取 Issues
```bash
gh issue list --repo Gracker/awesome-ai-field-notes --state open --label new-entry
gh issue list --repo Gracker/awesome-ai-field-notes --state open --label correction
```

### Step 2: 处理新资源 (label: new-entry)
1. 提取标题、URL、建议分类
2. 执行去重检查（URL + 标题相似度）
3. 如果不重复：
   - 自动分类（匹配 categories.json）
   - 自动评分 + 生成 one_liner（`one_liner_author: "openclaw"`）
   - 写入 `data/entries.json`
   - 保存正文或占位摘要到 `content/<id>.md`
4. 在 Issue 中回复处理结果
5. 关闭 Issue

### Step 3: 处理纠错 (label: correction)
1. 验证报告的问题（死链/分类错误/评分异议）
2. 如果是死链 → 运行 check-links.py 确认 → archived
3. 如果是分类错误 → 自动重新分类
4. 如果是评分异议 → 基于内容自动重新评分
5. 在 Issue 中回复处理结果
6. 关闭 Issue

### Step 4: 提交
```bash
python3 scripts/validate-schema.py
npm run build
git add -A
git commit -m "[openclaw] community: process N issues — M entries added, K fixed"
git push origin main
```

## Issue 回复模板

### 新资源已收录
```
✅ 已收录为条目 #XXXX
- 分类: {category}
- 评分: {score}/5
- one_liner: "{one_liner}"

感谢贡献！
```

### 纠错已修复
```
✅ 已修复
- 问题: {问题描述}
- 处理: {处理方式}
- 变更: {具体变更}
```

## 约束
- 每日最多处理 20 个 Issue
- 不自动关闭超过 24h 未处理的 Issue（先处理再关）
- 日期字段只能写 `YYYY-MM-DD` 或 `null`，禁止写“今天/昨天/今日/昨日/today/yesterday”等相对时间
- 不手写 `site-src/` 页面；`site-src/entry/` 是 ignored 构建产物，不要强行提交
