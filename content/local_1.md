# AGENTS.md — Obsidian Vault 宪法

> 本文件是 AI Agent 在此 Vault 中工作的最高行为准则。每次会话必读。

## 你在帮谁
- **高爷**，Android 性能优化工程师，MTK 成都
- 方向：AI 应用专家 + Android 系统开发专家 + X 大 V
- 详见 workspace MEMORY.md 和 USER.md

## Vault 结构规范

### 三层目录铁律
| 层 | 目录 | 规则 |
|---|------|------|
| 📥 原料 | `Cubox/`、`Personal-Knowlodge/source/`、`source/`、`DeepResearch/` | **内容只读**。允许添加 tag 元数据（front matter），不改正文 |
| 📋 摘要 | `调研/`、`论文/`、`X 文章/`、`公众号文章/`、`Android/`、`Codex/` | AI 结构化编译产物，可读写 |
| 💎 沉淀 | `知识库/`、`Android-Internal-Wiki/` | 高质量知识结晶，可读写 |
| ⚙️ 系统 | `OpenClaw定时任务/`、`小说工坊/`、`工作记录/`、`每日想法/` | 元数据/日志，cron 落盘 |

### 原始素材内容永远不变。知识是编译出来的，不是堆出来的。

## Tag 规范

### 标准 Taxonomy
参见 `/Users/gracker/.openclaw/workspace/tasks/okb/tag-taxonomy.json`

### 规则
- 每个文件：1-2 domain + 0-1 subdomain + 1 type + 0-1 source
- 全小写，连字符连接（`android`、`llm-agent`、`rss-tech`）
- 必须来自 taxonomy，禁止自造 tag
- 旧 tag 通过 legacy_map 自动转换

### 三个元文件
| 文件 | 用途 | 规则 |
|------|------|------|
| `AGENTS.md` | AI 行为宪法 | 每次会话必读 |
| `index.md` | 全局 TLDR 索引 | 每篇重要笔记一行 TLDR，先扫 index 再深读 |
| `log.md` | 操作日志 | 只增不减，统一前缀 `## ingest/compile/lint/query | 标题` |

## AI 工作流

### Ingest（编译原料）
- OKB-知识编译 cron 自动执行：每天从原料层挑 5-8 篇生成摘要
- 手动触发时：一次一篇，讨论 takeaway → 生成摘要 → 更新 index + log

### Query（沉淀知识）
- 高质量回答存为 `知识库/` 下的文件
- 探索结果累积，不一次性消费

### Lint（健康检查）
- OKB-知识库Lint cron 每周执行：矛盾/孤儿/破损链接/过时内容
- 发现矛盾标注 `⚠️ 矛盾`，不默默覆盖

## 防腐蚀铁律

1. **重要断言必须有来源链接**。无来源 = 猜测，标注 `[待验证]`。
2. **新旧冲突时，报 diff，不默默覆盖**。标注 `⚠️ 矛盾：新说X，旧说Y`。
3. **区分"原文事实"和"推论"**。原文事实写 `[来源]`，推论写 `[推断]`。
4. **不编造论文/链接/数据**。搜索失败就报错停止。
5. **摘要必须基于原文**。禁止凭标题空编。

## 文件操作规则

- **严禁 write/edit 写 iCloud 路径**，统一 `exec + python3 + pathlib + 绝对路径`
- 落盘路径：`exec + python3 -c "from pathlib import Path; ..."`
- 文件命名：`YYYY-MM-DD-主题名.md`
- 编码：UTF-8，换行：LF

## OKB Cron 任务
| 任务 | 频率 | 时间 | 模型 | 投递群 |
|------|------|------|------|--------|
| OKB-Tag补全 | 每天 | 03:00 | minimax | Action |
| OKB-知识编译 | 每天 | 03:30 | minimax | 知识库 |
| OKB-索引维护 | 每天 | 04:00 | minimax | 静默 |
| OKB-知识库Lint | 每周日 | 04:30 | minimax | Action |
| OKB-GraphUpdate | 每周日 | 05:00 | minimax | Action |

## Graphify 知识图谱
- **工具**：graphify（已安装），Python 解释器：`/Users/gracker/.local/pipx/venvs/graphifyy/bin/python3`
- **触发**：手动 `/graphify <path>` 或 OKB-GraphUpdate cron
- **已建图谱**：`调研/graphify-out/`（3704 nodes, 6829 edges, 210 communities）
- **产物**：`graphify-out/GRAPH_REPORT.md`（AI 查询入口）+ `graphify-out/graph.json`（持久图谱）
- **查询**：AI 回答架构/关联问题时，先读 GRAPH_REPORT.md 再决定深读哪些文件
