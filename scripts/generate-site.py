#!/usr/bin/env python3
"""
generate-site.py — 从 entries.json 生成 VitePress 站点

用法: python3 scripts/generate-site.py
读取: data/entries.json, metadata/categories.json
输出: site-src/ 下的 index.md + 各分类 .md
"""

import json, os, sys, html as html_mod
from datetime import datetime, timedelta
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
META_DIR = BASE_DIR / "metadata"
SRC_DIR = BASE_DIR / "site-src"
README_PATH = BASE_DIR / "README.md"
STATS_PATH = META_DIR / "stats.json"

def esc(text):
    """Escape HTML special chars in user content"""
    return html_mod.escape(str(text)) if text else ""

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

# === VitePress sidebar config ===
def build_sidebar():
    lines = [
        "import { defineConfig } from 'vitepress'",
        "",
        "export default defineConfig({",
        "  title: 'AI Field Notes',",
        "  description: 'AI 领域精选资源导航 — 有观点、有评分、每日自动更新',",
        "  lang: 'zh-CN',",
        "  head: [",
        "    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],",
        "  ],",
        "  themeConfig: {",
        "    logo: '/favicon.svg',",
        "    nav: [",
        "      { text: 'GitHub', link: 'https://github.com/Gracker/awesome-ai-field-notes' },",
        "    ],",
        "    sidebar: [",
        "      { text: '首页', link: '/' },",
    ]
    for key, info in categories.items():
        count = cat_counter.get(key, 0)
        lines.append("      { text: '%s %s (%s)', link: '/%s' }," % (info['icon'], info['name_zh'], count, key))
    lines.extend([
        "    ],",
        "    search: { provider: 'local' },",
        "    socialLinks: [",
        "      { icon: 'github', link: 'https://github.com/Gracker/awesome-ai-field-notes' },",
        "    ],",
        "    footer: { message: '由 OpenClaw 每日自动维护' },",
        "  },",
        "  srcDir: '.',",
        "  outDir: '../dist',",
        "  cleanUrls: true,",
        "})",
        "",
    ])
    return "\n".join(lines)

config_path = SRC_DIR / ".vitepress" / "config.ts"
config_path.parent.mkdir(exist_ok=True)
config_path.write_text(build_sidebar(), encoding="utf-8")

# === Favicon ===
favicon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><text y="28" font-size="28">⚡</text></svg>'
pub_dir = SRC_DIR / "public"
pub_dir.mkdir(exist_ok=True)
(pub_dir / "favicon.svg").write_text(favicon, encoding="utf-8")

# === Entry formatting (pure Markdown, no HTML) ===
def fmt_entry(e):
    """Format as a Markdown list item with inline metadata"""
    title = esc(e["title"])
    url = e.get("url") or "#"
    one_liner = esc(e.get("one_liner", ""))
    score = e.get("quality_score", 0)
    gh_stars = e.get("github_stars")
    stars_str = " ⭐{:,}".format(gh_stars) if gh_stars else ""
    lang = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "")
    source = e.get("source") or {}
    author = esc(source.get("author", ""))
    author_str = " by @{}".format(author) if author else ""
    summary = e.get("summary_zh", "") or e.get("summary_en", "")
    summary = esc(summary)
    
    lines = [
        "### [{}]({}){}".format(title, url, stars_str),
        "**{}**{} · ⭐{} {}/5 · {}".format(one_liner, author_str, "⭐" * score, score, lang),
    ]
    if summary:
        lines.append("")
        lines.append("> {}".format(summary))
    tags = [esc(t) for t in e.get("tags", [])[:6]]
    if tags:
        lines.append("")
        lines.append("{}".format(" ".join("`{}`".format(t) for t in tags)))
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

def fmt_list_item(e):
    title = esc(e["title"])
    url = e.get("url") or "#"
    one_liner = esc(e.get("one_liner", ""))
    score = e.get("quality_score", 0)
    lang = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "")
    return "- [{}]({}) — {} {} {} {}/5".format(title, url, one_liner, "⭐" * score, lang, score)

# === Homepage ===
top10 = sorted(active, key=lambda x: (-x.get("quality_score", 0), x.get("github_stars", 0) or 0))[:10]

home = [
    "---",
    "layout: home",
    "",
    "hero:",
    "  name: AI Field Notes",
    "  text: AI 领域精选资源导航",
    "  tagline: 有观点 · 有评分 · 每日自动更新 · {} 条".format(stats['total_entries']),
    "  actions:",
    "    - theme: brand",
    "      text: 浏览全部",
    "      link: /models",
    "    - theme: alt",
    "      text: GitHub",
    "      link: https://github.com/Gracker/awesome-ai-field-notes",
    "",
    "features:",
]
for key, info in categories.items():
    count = cat_counter.get(key, 0)
    home.append("  - title: '{} {}'".format(info['icon'], info['name_zh']))
    home.append("    details: '{} · {} 条'".format(info.get('desc', ''), count))
    home.append("    link: /{}".format(key))
home.append("---")
home.append("")

(SRC_DIR / "index.md").write_text("\n".join(home), encoding="utf-8")

# === Category pages ===
for key, info in categories.items():
    cat_entries = sorted(
        [e for e in active if e.get("category") == key],
        key=lambda x: (-x.get("quality_score", 0), x.get("added_date", ""))
    )
    
    page = [
        "# {} {}".format(info['icon'], info['name_zh']),
        "",
        "{} — 共 **{}** 条活跃资源".format(info.get('desc', ''), len(cat_entries)),
        "",
    ]
    
    if not cat_entries:
        page.append("_暂无条目_")
    else:
        for e in cat_entries:
            page.append(fmt_entry(e))
    
    (SRC_DIR / "{}.md".format(key)).write_text("\n".join(page), encoding="utf-8")

# === 仓库 README.md ===
readme = [
    "# AI Field Notes",
    "",
    "> AI 领域精选资源导航 — 有观点、有评分、每日自动更新。608 条，中英双语。",
    "",
    "## ⭐ 精选 Top 10",
    "",
]
for e in top10:
    title = esc(e["title"])
    url = e.get("url") or "#"
    one_liner = esc(e.get("one_liner", ""))
    readme.append("- [{}]({}) — {}".format(title, url, one_liner))
readme.extend(["", "## 分类导航", "", "| 分类 | 数量 | 说明 |", "|------|------|------|"])
for key, info in categories.items():
    count = cat_counter.get(key, 0)
    readme.append("| {} {} | {} | {} |".format(info['icon'], info['name_zh'], count, info.get('desc', '')))
readme.extend([
    "",
    "## 评分标准",
    "",
    "⭐⭐⭐⭐⭐ 必读 | ⭐⭐⭐⭐ 优秀 | ⭐⭐⭐ 值得一看 | ≤2 仅存档不展示",
    "",
    "## 数据",
    "",
    "- 在线站点：[godofgpt.com](https://godofgpt.com/)",
    "- 结构化数据：[`data/entries.json`](data/entries.json)（Agent 可直接消费）",
    "- 贡献资源：开 [Issue](../../issues/new/choose)",
    "",
    "由 [OpenClaw](https://github.com/openclaw/openclaw) 每日自动维护 — 采集、去重、分类、评分、死链检测、站点生成，全流程无人值守。",
    "",
    "License: [CC BY-NC-SA 4.0](LICENSE)",
])
README_PATH.write_text("\n".join(readme), encoding="utf-8")

print("✅ 站点生成完成: {} 条目, {} 活跃, {} 本周新增".format(stats['total_entries'], stats['active_entries'], stats['this_week_added']))
