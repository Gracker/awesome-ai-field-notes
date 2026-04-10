#!/usr/bin/env python3
"""
generate-site.py — 从 entries.json 生成 VitePress 站点
按日期分组，最新在前，格式统一
"""

import json, os, sys, html as html_mod
from datetime import datetime, timedelta
from collections import Counter, OrderedDict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
META_DIR = BASE_DIR / "metadata"
SRC_DIR = BASE_DIR / "site-src"
README_PATH = BASE_DIR / "README.md"
STATS_PATH = META_DIR / "stats.json"

def esc(text):
    return html_mod.escape(str(text)) if text else ""

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

entries_data = load_json(DATA_DIR / "entries.json")
categories = load_json(META_DIR / "categories.json")
entries = entries_data.get("entries", [])
active = [e for e in entries if e.get("status") == "active" and e.get("quality_score", 0) >= 3]

now = datetime.now()
today_str = now.strftime("%Y-%m-%d")
yesterday_str = (now - timedelta(days=1)).strftime("%Y-%m-%d")
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

# === VitePress config ===
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

# Favicon
favicon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><text y="28" font-size="28">⚡</text></svg>'
pub_dir = SRC_DIR / "public"
pub_dir.mkdir(exist_ok=True)
(pub_dir / "favicon.svg").write_text(favicon, encoding="utf-8")

# === Date helpers ===
def date_label(date_str):
    if not date_str:
        return None
    if date_str == today_str:
        return "今天"
    if date_str == yesterday_str:
        return "昨天"
    return None  # will use raw date as header

def date_sort_key(date_str):
    """For sorting: today=0, yesterday=1, then descending date"""
    if not date_str:
        return (999, "")
    if date_str == today_str:
        return (0, "")
    if date_str == yesterday_str:
        return (1, "")
    return (2, date_str)

# === Entry formatting ===
def fmt_entry(e):
    title = esc(e["title"])
    url = e.get("url") or "#"
    score = e.get("quality_score", 0)
    gh_stars = e.get("github_stars")
    stars_str = " ⭐{:,.0f}".format(gh_stars) if gh_stars else ""
    lang = "🇨🇳" if e.get("language") == "zh" else ("🌐" if e.get("language") == "en" else "")
    source = e.get("source") or {}
    author = esc(source.get("author", ""))
    added = e.get("added_date", "")

    # Body: prefer summary, fallback to one_liner
    summary = (e.get("summary_zh", "") or e.get("summary_en", "") or "").strip()
    one_liner = e.get("one_liner", "").strip()
    body = esc(summary) if len(summary) >= 20 else esc(one_liner)

    # Meta: author · score · date
    meta_parts = []
    if author:
        meta_parts.append("@{}".format(author))
    meta_parts.append("{}{} {}".format("⭐" * score, score, lang))
    if added:
        dl = date_label(added)
        meta_parts.append(dl if dl else added)
    meta_str = " · ".join(meta_parts)

    lines = [
        "### [{}]({}){}".format(title, url, stars_str),
        meta_str,
    ]
    if body:
        lines.append("")
        lines.append(body)
    tags = [esc(t) for t in e.get("tags", [])[:5]]
    if tags:
        lines.append("")
        lines.append(" ".join("`{}`".format(t) for t in tags))
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

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

# === Category pages (grouped by date) ===
for key, info in categories.items():
    cat_entries = [e for e in active if e.get("category") == key]
    
    if not cat_entries:
        page = [
            "# {} {}".format(info['icon'], info['name_zh']),
            "",
            "_暂无条目_",
        ]
    else:
        # Group by date, sort groups newest first
        groups = OrderedDict()
        for e in cat_entries:
            d = e.get("added_date", "") or "unknown"
            groups.setdefault(d, []).append(e)
        
        # Sort groups: today first, yesterday second, then descending date
        sorted_dates = sorted(groups.keys(), key=date_sort_key)
        
        page = [
            "# {} {}".format(info['icon'], info['name_zh']),
            "",
            "{} — 共 **{}** 条活跃资源".format(info.get('desc', ''), len(cat_entries)),
            "",
        ]
        
        for d in sorted_dates:
            label = date_label(d) or d
            group_entries = sorted(groups[d], key=lambda x: (-x.get("quality_score", 0), x.get("github_stars", 0) or 0))
            page.append("## 📅 {}".format(label))
            page.append("")
            for e in group_entries:
                page.append(fmt_entry(e))
    
    (SRC_DIR / "{}.md".format(key)).write_text("\n".join(page), encoding="utf-8")

# === README.md ===
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
