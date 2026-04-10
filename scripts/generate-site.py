#!/usr/bin/env python3
"""
generate-site.py — 从 entries.json 生成 mdbook 站点 + README
扁平分类模式：6 个顶层分类，无子分类
"""

import json, os, sys
from datetime import datetime, timedelta
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
META_DIR = BASE_DIR / "metadata"
SRC_DIR = BASE_DIR / "site-src"
README_PATH = BASE_DIR / "README.md"
STATS_PATH = META_DIR / "stats.json"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

entries_data = load_json(DATA_DIR / "entries.json")
categories = load_json(META_DIR / "categories.json")
entries = entries_data.get("entries", [])
active = [e for e in entries if e.get("status") == "active" and e.get("quality_score", 0) >= 3]

now = datetime.now()
week_ago = (now - timedelta(days=7)).strftime("%Y-%m-%d")
this_week = [e for e in entries if e.get("added_date", "") >= week_ago]

# Stats
cat_counter = Counter(e.get("category", "uncategorized") for e in entries)
source_counter = Counter(e.get("source_type", "unknown") for e in entries)
stats = {
    "total_entries": len(entries),
    "active_entries": len([e for e in entries if e.get("status") == "active"]),
    "archived_entries": len([e for e in entries if e.get("status") == "archived"]),
    "this_week_added": len(this_week),
    "category_distribution": dict(cat_counter.most_common()),
    "source_type_distribution": dict(source_counter.most_common()),
    "last_updated": now.strftime("%Y-%m-%d %H:%M"),
}
STATS_PATH.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

# === mdbook site ===
SRC_DIR.mkdir(exist_ok=True)

def fmt_entry(e):
    title = e["title"]
    url = e.get("url") or "#"
    one_liner = e.get("one_liner", "")
    stars = f" ⭐{e['github_stars']:,}" if e.get("github_stars") else ""
    tags = " ".join(f"`{t}`" for t in e.get("tags", [])[:5])
    tag_str = f" {tags}" if tags else ""
    lang = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "")
    source = e.get("source") or {}
    author = source.get("author", "")
    author_str = f" by @{author}" if author else ""
    return f"- [{title}]({url}){author_str} — {one_liner}{stars}{tag_str} {lang}"

def fmt_detail(e):
    title = e["title"]
    url = e.get("url") or "#"
    one_liner = e.get("one_liner", "")
    score = e.get("quality_score", 0)
    summary = e.get("summary_zh", "") or e.get("summary_en", "")
    stars = f" ⭐{e['github_stars']:,}" if e.get("github_stars") else ""
    tags = " ".join(f"`{t}`" for t in e.get("tags", [])[:8])
    tag_str = f" {tags}" if tags else ""
    lang = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "")
    source = e.get("source") or {}
    author = source.get("author", "")
    orig_date = source.get("original_date", "")
    author_str = f"by @{author}" if author else ""
    date_str = f" ({orig_date})" if orig_date else ""
    return (
        f"### [{title}]({url}) {stars}\n"
        f"{author_str}{date_str} | {'⭐' * score} {score}/5 | {lang}\n\n"
        f"**{one_liner}**\n\n"
        f"{summary}\n\n"
        f"{tag_str}\n"
    )

# SUMMARY.md
summary = ["# Summary", "", "- [首页](README.md)", ""]
for key, info in categories.items():
    count = cat_counter.get(key, 0)
    summary.append(f"- [{info['icon']} {info['name_zh']} ({count})]({key}/README.md)")
summary.append("")
(SRC_DIR / "SUMMARY.md").write_text("\n".join(summary), encoding="utf-8")

# 各分类页面
for key, info in categories.items():
    cat_dir = SRC_DIR / key
    cat_dir.mkdir(exist_ok=True)
    cat_entries = sorted(
        [e for e in active if e.get("category") == key],
        key=lambda x: (-x.get("quality_score", 0), x.get("added_date", ""))
    )
    lines = [
        f"# {info['icon']} {info['name_zh']}",
        "",
        f"{info.get('desc', '')} — 共 {len(cat_entries)} 条活跃资源",
        "",
    ]
    if not cat_entries:
        lines.append("_暂无条目_")
    else:
        for e in cat_entries:
            lines.append(fmt_detail(e))
            lines.append("---")
            lines.append("")
    (cat_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")

# Site README
top10 = sorted(active, key=lambda x: (-x.get("quality_score", 0), x.get("github_stars", 0) or 0))[:10]
site_home = [
    "# AI Field Notes",
    "",
    "> AI 领域精选资源导航 — 有观点、有评分、每日自动更新",
    "",
    f"**{stats['total_entries']}** 条 | **{stats['this_week_added']}** 条本周新增 | {now.strftime('%Y-%m-%d')}",
    "",
    "## ⭐ 精选 Top 10",
    "",
]
for e in top10:
    site_home.append(fmt_entry(e))
site_home.extend(["", "## 分类导航", ""])
for key, info in categories.items():
    count = cat_counter.get(key, 0)
    site_home.append(f"- [{info['icon']} {info['name_zh']} ({count})]({key}/README.md) — {info.get('desc', '')}")
site_home.extend([
    "",
    "## 评分标准",
    "",
    "⭐⭐⭐⭐⭐ 必读 | ⭐⭐⭐⭐ 优秀 | ⭐⭐⭐ 值得一看 | ≤2 仅存档不展示",
    "",
    "---",
    "",
    f"*数据: [entries.json](../data/entries.json) · 由 [OpenClaw](https://github.com/openclaw/openclaw) 每日自动维护*",
])
(SRC_DIR / "README.md").write_text("\n".join(site_home), encoding="utf-8")

# === 仓库 README.md ===
readme_lines = [
    "# AI Field Notes",
    "",
    "> AI 领域精选资源导航 — 有观点、有评分、每日自动更新。608 条，中英双语。",
    "",
    "## ⭐ 本周精选",
    "",
]
for e in top10:
    title = e["title"]
    url = e.get("url") or "#"
    one_liner = e.get("one_liner", "")
    readme_lines.append(f"- [{title}]({url}) — {one_liner}")
readme_lines.extend(["", "## 分类导航", "", "| 分类 | 数量 | 说明 |", "|------|------|------|"])
for key, info in categories.items():
    count = cat_counter.get(key, 0)
    readme_lines.append(f"| {info['icon']} {info['name_zh']} | {count} | {info.get('desc', '')} |")
readme_lines.extend([
    "",
    "## 评分标准",
    "",
    "⭐⭐⭐⭐⭐ 必读 | ⭐⭐⭐⭐ 优秀 | ⭐⭐⭐ 值得一看 | ≤2 仅存档不展示",
    "",
    "## 数据",
    "",
    "- 结构化数据：[`data/entries.json`](data/entries.json)（Agent 可直接消费）",
    "- 在线站点：[mdbook 版](https://awesome-ai-field-notes.androidperformance.com/)",
    "- 贡献资源：开 [Issue](../../issues/new/choose)",
    "",
    "由 [OpenClaw](https://github.com/openclaw/openclaw) 每日自动维护 — 采集、去重、分类、评分、死链检测、站点生成，全流程无人值守。",
    "",
    "License: [CC BY-NC-SA 4.0](LICENSE)",
])
README_PATH.write_text("\n".join(readme_lines), encoding="utf-8")

# book.toml
(BASE_DIR / "book.toml").write_text(
    '[book]\n'
    'title = "AI Field Notes"\n'
    'description = "AI 领域精选资源导航"\n'
    'language = "zh"\n'
    'src = "site-src"\n\n'
    '[build]\nbuild-dir = "book"\n\n'
    '[output.html]\n'
    'default-theme = "light"\n'
    'git-repository-url = "https://github.com/Gracker/awesome-ai-field-notes"\n',
    encoding="utf-8"
)

print(f"✅ 站点生成完成: {stats['total_entries']} 条目, {stats['active_entries']} 活跃, {stats['this_week_added']} 本周新增")
