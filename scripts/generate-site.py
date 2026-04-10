#!/usr/bin/env python3
"""
generate-site.py — 从 entries.json 生成 mdbook 站点

用法: python3 scripts/generate-site.py
读取: data/entries.json, metadata/categories.json
输出: src/ 下的 SUMMARY.md + 各分类 .md 文件, README.md 统计摘要
"""

import json
import os
import sys
from datetime import datetime, timedelta
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
META_DIR = BASE_DIR / "metadata"
SRC_DIR = BASE_DIR / "site-src"
README_PATH = BASE_DIR / "README.md"
STATS_PATH = META_DIR / "stats.json"

# 加载数据
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

entries_data = load_json(DATA_DIR / "entries.json")
categories = load_json(META_DIR / "categories.json")

entries = entries_data.get("entries", [])

# 过滤活跃 + 高分
active_entries = [e for e in entries if e.get("status") == "active" and e.get("quality_score", 0) >= 3]

# 计算统计
now = datetime.now()
week_ago = (now - timedelta(days=7)).strftime("%Y-%m-%d")
this_week = [e for e in entries if e.get("added_date", "") >= week_ago]

cat_counter = Counter()
source_counter = Counter()
lang_counter = Counter()

for e in entries:
    cat = e.get("category", "uncategorized")
    top_cat = cat.split("/")[0] if "/" in cat else cat
    cat_counter[top_cat] += 1
    source_counter[e.get("source_type", "unknown")] += 1
    lang_counter[e.get("language", "unknown")] += 1

# 写入 stats.json
stats = {
    "total_entries": len(entries),
    "active_entries": len([e for e in entries if e.get("status") == "active"]),
    "archived_entries": len([e for e in entries if e.get("status") == "archived"]),
    "this_week_added": len(this_week),
    "category_distribution": dict(cat_counter.most_common()),
    "source_type_distribution": dict(source_counter.most_common()),
    "language_distribution": dict(lang_counter.most_common()),
    "last_updated": now.strftime("%Y-%m-%d %H:%M"),
}
STATS_PATH.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

# 生成 mdbook site-src
SRC_DIR.mkdir(exist_ok=True)

# 生成 SUMMARY.md
summary_lines = ["# Summary", "", "- [首页](README.md)", "- [分类总览](overview.md)", ""]
for cat_key, cat_info in categories.items():
    summary_lines.append(f"- [{cat_info['icon']} {cat_info['name_zh']}]({cat_key}/README.md)")
    for child_key, child_info in cat_info.get("children", {}).items():
        child_path = f"{cat_key}/{child_key}.md"
        summary_lines.append(f"  - [{child_info['name_zh']}]({child_path})")
    summary_lines.append("")

(SRC_DIR / "SUMMARY.md").write_text("\n".join(summary_lines), encoding="utf-8")

# 生成首页
def score_badge(score):
    stars = "⭐" * score
    return f"{stars} {score}/5" if score >= 3 else f"{score}/5"

def format_entry(e):
    title = e["title"]
    url = e.get("url") or "#"
    one_liner = e.get("one_liner", "")
    score = e.get("quality_score", 0)
    stars_str = f" ⭐{e['github_stars']:,}" if e.get("github_stars") else ""
    tags = " ".join(f"`{t}`" for t in e.get("tags", [])[:5])
    tag_str = f" {tags}" if tags else ""
    lang_badge = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "🌍")
    source = e.get("source") or {}
    author = source.get("author", "")
    author_str = f" by @{author}" if author else ""
    
    line = f"- [{title}]({url}){author_str} — {one_liner}{stars_str}{tag_str} {lang_badge}"
    return line

def format_entry_detail(e):
    """生成详细条目（含摘要），用于子分类页面"""
    title = e["title"]
    url = e.get("url") or "#"
    one_liner = e.get("one_liner", "")
    score = e.get("quality_score", 0)
    summary = e.get("summary_zh", "")
    stars_str = f" ⭐{e['github_stars']:,}" if e.get("github_stars") else ""
    tags = " ".join(f"`{t}`" for t in e.get("tags", [])[:8])
    tag_str = f" {tags}" if tags else ""
    lang_badge = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "🌍")
    source = e.get("source") or {}
    author = source.get("author", "")
    orig_date = source.get("original_date", "")
    author_str = f"by @{author}" if author else ""
    date_str = f" ({orig_date})" if orig_date else ""
    
    lines = [
        f"### [{title}]({url}) {stars_str}",
        f"{author_str}{date_str} | {'⭐' * score} {score}/5 | {lang_badge}",
        f"",
        f"**{one_liner}**",
        f"",
        summary,
        f"{tag_str}",
        f"",
    ]
    return "\n".join(lines)

# 生成 overview.md
overview_lines = [
    "# 分类总览",
    "",
    f"**最后更新**: {now.strftime('%Y-%m-%d %H:%M')}",
    "",
    "## 📊 统计",
    "",
    f"| 指标 | 数值 |",
    f"|------|------|",
    f"| 总条目数 | {stats['total_entries']} |",
    f"| 活跃条目 | {stats['active_entries']} |",
    f"| 本周新增 | {stats['this_week_added']} |",
    f"| 分类覆盖 | {len(cat_counter)} / {len(categories)} |",
    "",
]

if stats["category_distribution"]:
    overview_lines.append("### 分类分布")
    overview_lines.append("")
    for cat, count in sorted(stats["category_distribution"].items(), key=lambda x: -x[1]):
        name = categories.get(cat, {}).get("name_zh", cat)
        overview_lines.append(f"- **{name}**: {count} 条")
    overview_lines.append("")

if stats["source_type_distribution"]:
    overview_lines.append("### 来源分布")
    overview_lines.append("")
    for src, count in sorted(stats["source_type_distribution"].items(), key=lambda x: -x[1]):
        overview_lines.append(f"- **{src}**: {count} 条")
    overview_lines.append("")

(SRC_DIR / "overview.md").write_text("\n".join(overview_lines), encoding="utf-8")

# 生成各分类页面
for cat_key, cat_info in categories.items():
    cat_dir = SRC_DIR / cat_key
    cat_dir.mkdir(exist_ok=True)
    
    # 分类首页
    cat_entries = [e for e in active_entries if e.get("category", "").startswith(cat_key + "/")]
    
    cat_lines = [
        f"# {cat_info['icon']} {cat_info['name_zh']}",
        "",
        f"{cat_info['name']} — 共 {len(cat_entries)} 条活跃资源",
        "",
    ]
    
    for child_key, child_info in cat_info.get("children", {}).items():
        child_cat = f"{cat_key}/{child_key}"
        child_entries = [e for e in cat_entries if e.get("category") == child_cat]
        child_entries.sort(key=lambda x: (-x.get("quality_score", 0), x.get("added_date", "")))
        
        cat_lines.append(f"## {child_info['name_zh']} ({len(child_entries)})")
        cat_lines.append("")
        
        if not child_entries:
            cat_lines.append("_暂无条目_")
        else:
            for e in child_entries:
                cat_lines.append(format_entry(e))
        cat_lines.append("")
    
    (cat_dir / "README.md").write_text("\n".join(cat_lines), encoding="utf-8")
    
    # 子分类独立页面
    for child_key, child_info in cat_info.get("children", {}).items():
        child_cat = f"{cat_key}/{child_key}"
        child_entries = [e for e in active_entries if e.get("category") == child_cat]
        child_entries.sort(key=lambda x: (-x.get("quality_score", 0), x.get("added_date", "")))
        
        child_lines = [
            f"# {child_info['name_zh']}",
            "",
            f"{child_info['name']} — {len(child_entries)} 条活跃资源",
            "",
        ]
        
        if not child_entries:
            child_lines.append("_暂无条目_")
        else:
            for e in child_entries:
                child_lines.append(format_entry_detail(e))
                child_lines.append("---")
        
        (cat_dir / f"{child_key}.md").write_text("\n".join(child_lines), encoding="utf-8")

# 生成 mdbook README (site 首页)
site_readme = [
    "# AI Field Notes",
    "",
    "> AI 领域精选资源导航 — 有观点、有评分、可被 Agent 消费",
    "",
    f"**总条目**: {stats['total_entries']} | **本周新增**: {stats['this_week_added']} | **更新时间**: {now.strftime('%Y-%m-%d')}",
    "",
    "## 质量评分标准",
    "",
    "| 分数 | 含义 |",
    "|------|------|",
    "| ⭐⭐⭐⭐⭐ | 必读 — 里程碑级内容 |",
    "| ⭐⭐⭐⭐ | 优秀 — 有独到洞察 |",
    "| ⭐⭐⭐ | 值得一看 — 有参考价值 |",
    "",
    "## 快速导航",
    "",
]

for cat_key, cat_info in categories.items():
    count = sum(1 for e in active_entries if e.get("category", "").startswith(cat_key + "/"))
    site_readme.append(f"- [{cat_info['icon']} {cat_info['name_zh']} ({count})]({cat_key}/README.md)")

site_readme.extend([
    "",
    "---",
    "",
    f"*数据存储在 [entries.json](../data/entries.json)，由 [OpenClaw](https://github.com/openclaw/openclaw) 每日自动更新。*",
])

(SRC_DIR / "README.md").write_text("\n".join(site_readme), encoding="utf-8")

def update_readme_summary(stats, categories, active_entries, now):
    """更新仓库根 README.md 的统计部分"""
    readme = README_PATH.read_text(encoding="utf-8")
    
    marker_start = "<!-- AUTO-GENERATED: 由 generate-site.py 从 entries.json 渲染，勿手动编辑 -->"
    marker_end = "<!-- /AUTO-GENERATED -->"
    
    if marker_start not in readme:
        print("Warning: README.md 中缺少 AUTO-GENERATED 标记", file=sys.stderr)
        return
    
    idx_start = readme.index(marker_start) + len(marker_start)
    idx_end = readme.index(marker_end)
    
    gen_lines = [
        "",
        f"📊 **{stats['total_entries']}** 条资源 | **{stats['this_week_added']}** 条本周新增 | 更新: {now.strftime('%Y-%m-%d')}",
        "",
        "| 分类 | 活跃数 | 分类 | 活跃数 |",
        "|------|--------|------|--------|",
    ]
    
    cat_keys = list(categories.keys())
    for i in range(0, len(cat_keys), 2):
        left = cat_keys[i]
        right = cat_keys[i + 1] if i + 1 < len(cat_keys) else None
        
        left_info = categories[left]
        left_count = sum(1 for e in active_entries if e.get("category", "").startswith(left + "/"))
        left_str = f"| {left_info['icon']} {left_info['name_zh']} | {left_count} |"
        
        if right:
            right_info = categories[right]
            right_count = sum(1 for e in active_entries if e.get("category", "").startswith(right + "/"))
            right_str = f" {right_info['icon']} {right_info['name_zh']} | {right_count} |"
        else:
            right_str = " | |"
        
        gen_lines.append(left_str + right_str)
    
    gen_lines.append("")
    
    # Top 10 精选
    top10 = sorted(active_entries, key=lambda x: (-x.get("quality_score", 0), x.get("github_stars", 0) or 0))[:10]
    if top10:
        gen_lines.append("### ⭐ 本周精选 Top 10")
        gen_lines.append("")
        for e in top10:
            gen_lines.append(format_entry(e))
        gen_lines.append("")
    
    gen_block = "\n".join(gen_lines)
    
    new_readme = readme[:idx_start] + gen_block + readme[idx_end:]
    README_PATH.write_text(new_readme, encoding="utf-8")

# 更新仓库 README 统计摘要
update_readme_summary(stats, categories, active_entries, now)

# 生成 book.toml
book_toml = """[book]
title = "AI Field Notes"
description = "AI 领域精选资源导航 — 有观点、有评分、可被 Agent 消费"
language = "zh"
src = "site-src"

[build]
build-dir = "book"

[output.html]
default-theme = "light"
git-repository-url = "https://github.com/Gracker/awesome-ai-field-notes"
edit-url-template = "https://github.com/Gracker/awesome-ai-field-notes/edit/main/{path}"
"""

(BASE_DIR / "book.toml").write_text(book_toml, encoding="utf-8")

print(f"✅ 站点生成完成: {stats['total_entries']} 条目, {stats['active_entries']} 活跃, {stats['this_week_added']} 本周新增")
