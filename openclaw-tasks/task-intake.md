# OpenClaw Task: 存量阶段 — 日常入库 (Intake)

## 前置条件
初始化阶段完成（Phase 1-3 全部完成）。

## 目标
增量发现新的 AI 内容，完整提取后写入 entries.json。

## 执行频率
每日 08:00 + 20:00

## 与初始化阶段的核心区别
初始化 scan：批量暴力提取，不分类不评分
存量 intake：增量逐条处理，**完整提取（来源+摘要+图片+本地路径）+ 分类 + 评分**

## 执行流程

### Phase 1: 信息发现
- 检查 `intake/` 目录待处理素材
- 扫描 Obsidian 中最近 24h 新增/修改的 AI 相关 .md 文件
- RSS / Newsletter 抓取（如有配置）

### Phase 2: 完整提取（严格从文件提取，禁止捏造）
读取 `data/SCHEMA.md` 获取字段定义，对每个候选：

1. **元数据提取**：title / url / source(platform, author, original_date)
2. **内容提取**：summary_zh（100-300字）+ summary_en（英文原文时）
3. **图片提取**：正则 `!\[.*?\]\((https?://[^)]+)\)`
4. **本地路径**：`local_path` 相对 Obsidian 根

### Phase 3: 分类 + 评分
- 根据 title + summary_zh + tags 自动匹配分类
- 根据 SCHEMA.md 评分依据给出 quality_score
- 生成 one_liner 候选

### Phase 4: 去重 + 写入
- URL 精确去重
- 标题相似度 > 0.85 去重
- 写入 entries.json
- `one_liner_author: "openclaw"`（全自动点评）

### Phase 5: 验证 + 提交
```bash
python3 scripts/validate-schema.py
python3 scripts/generate-site.py
git add -A
git commit -m "[openclaw] intake: daily — N entries added"
git push origin main
```

## 约束
- 单次 ≤ 20 条
- 不修改已有条目的 score/one_liner（除非人工指示）
- 提取不到的字段设为 null，不编造
- 英文原文必须提供中英双语摘要
