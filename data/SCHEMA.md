# entries.json Schema v2.0

## 字段定义

```json
{
  "id": "string (8位 nanoid)",
  
  "title": "string — 文章/项目标题，从文件名或 # 标题提取，不捏造",
  "url": "string — 原文链接，从文件元数据头提取（来源链接、原文链接等）",
  
  "source": {
    "platform": "string — 来源平台（x/twitter, cubox, arxiv, github, blog, newsletter, youtube, manual）",
    "author": "string — 原作者（从元数据头提取，无则 null）",
    "original_date": "string — 原文发布日期（YYYY-MM-DD，从元数据头提取）"
  },
  
  "category": "string — 站点顶层分类（models/agents/coding/infra/industry/learning），历史二级分类会在站点生成时映射到顶层分类",
  "tags": ["string — 关键词标签"],
  "source_type": "enum: github | paper | article | x_post | newsletter | video | product | dataset（历史 tweet 视为 x_post 兼容别名）",
  "language": "enum: en | zh | both — 原文语言",
  
  "summary_zh": "string — 中文摘要（100-300字，基于正文提取核心观点，禁止捏造）",
  "summary_en": "string | null — 英文摘要（仅 language=en 或 both 时填写，从正文提取）",
  
  "one_liner": "string — 一句话中文点评（判断性语句，如'目前最实用的XXX'，必须基于内容得出）",
  "one_liner_author": "enum: gracker | openclaw | community-pending — 谁写的点评",
  
  "quality_score": "int 1-5",
  "status": "enum: active | archived | deprecated | score-pending — score-pending 表示待人工评分",
  
  "local_path": "string — Obsidian 中的相对路径（如 'X 文章/04-06-xxx.md'），可定位本地备份",
  "images": ["string — 正文中的图片 URL 列表（从 ![](url) 提取）"],
  
  "added_date": "YYYY-MM-DD",
  "updated_date": "YYYY-MM-DD | null",
  
  "github_stars": "number | null（仅 github 类型）",
  "related": ["string — 关联条目 id"]
}
```

## 字段来源规则（禁止捏造）

| 字段 | 提取规则 |
|------|----------|
| title | 优先文件第一行 `# 标题`，其次文件名去掉日期前缀 |
| url | 从 YAML frontmatter 或元数据区的 `原文链接`/`url`/`链接` 字段提取 |
| source.platform | 从元数据区的 `来源` 字段推断，或根据目录名（X 文章→x, Cubox→cubox, 论文→arxiv） |
| source.author | 从元数据区的 `作者` 字段提取 |
| source.original_date | 从元数据区的 `日期`/`发表时间` 字段提取 |
| summary_zh | **从正文内容提取核心观点，100-300字，不捏造不推断** |
| summary_en | 仅英文原文，从正文提取英文摘要 |
| one_liner | 基于内容得出，不凭空判断。不确定时标记 `one_liner_author: "openclaw"` 待审核 |
| local_path | 相对于 Obsidian 根目录的路径 |
| images | 正则提取 `!\[.*?\]\((https?://[^)]+)\)` 中的 URL |
| tags | 从正文标题、YAML tags、内容关键词提取，≤8 个 |

## 双语摘要规则

当 `language = "en"` 或 `"both"` 时：
- `summary_zh`: 中文翻译摘要（基于原文内容翻译，保留技术术语英文）
- `summary_en`: 英文原文摘要（从正文直接提取，不翻译）

当 `language = "zh"` 时：
- `summary_zh`: 中文摘要
- `summary_en`: null

## 质量评分依据（必须基于内容实际判断）

| 分数 | 判断依据 |
|------|----------|
| 5 | 里程碑级：改变了行业认知或实践（如 Transformer 原始论文、MCP 规范发布） |
| 4 | 高质量原创：有独到洞察/完整实现/深度分析（>3000字 + 原创观点 + 数据支撑） |
| 3 | 有参考价值：信息准确，但缺少独特视角（二手整理、教程、入门指南） |
| 2 | 浅层介绍：内容泛泛，仅做补充参考 |
| 1 | 过时或低质量：仅存档 |

## 提取不出来的字段

如果某字段无法从文件中提取：
- `url`: 设为 null，备注 "原文链接缺失"
- `source.author`: 设为 null
- `source.original_date`: 设为 null
- `summary_zh`: 如果正文内容太少（<50字），设为 "内容过短，待补充"
- `images`: 空数组

**禁止：** 为缺失字段编造内容。宁可留空也不捏造。
