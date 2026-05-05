#!/usr/bin/env python3
"""
weekly-dedup.py — AAIF 周去重脚本
执行：URL硬去重、标题软去重
输出：去重报告到 logs/
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from pipeline_utils import normalized_url_key, project_root

BASE_DIR = project_root()
ENTRIES_PATH = BASE_DIR / "data" / "entries.json"
LOGS_DIR = BASE_DIR / "logs"

TODAY = datetime.now().strftime("%Y-%m-%d")

def load_entries():
    with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_entries(data):
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def normalize_url(url):
    """归一化URL：去尾斜杠、去utm/ref参数"""
    shared = normalized_url_key(url)
    if shared:
        return shared
    if not url:
        return url
    parsed = urlparse(url)
    # Remove utm_* and ref params
    if parsed.query:
        params = parse_qs(parsed.query, keep_blank_values=True)
        filtered = {k: v for k, v in params.items() 
                    if not k.startswith('utm_') and k != 'ref'}
        new_query = urlencode(filtered, doseq=True)
    else:
        new_query = ""
    
    # Remove trailing slash from path
    path = parsed.path.rstrip('/')
    if not path:
        path = '/'
    
    # Lowercase netloc
    netloc = parsed.netloc.lower()
    
    return urlunparse((parsed.scheme, netloc, path, parsed.params, new_query, ''))

def title_similarity(t1, t2):
    """简单标题相似度：字符级 Jaccard"""
    if not t1 or not t2:
        return 0.0
    # Normalize
    t1n = re.sub(r'[\s\-–—_]', '', t1.lower())
    t2n = re.sub(r'[\s\-–—_]', '', t2.lower())
    if t1n == t2n:
        return 1.0
    # Bigram Jaccard
    def bigrams(s):
        return set(s[i:i+2] for i in range(len(s)-1))
    b1, b2 = bigrams(t1n), bigrams(t2n)
    if not b1 or not b2:
        return 0.0
    return len(b1 & b2) / len(b1 | b2)

def main():
    print(f"🔍 AAIF 周去重 · {TODAY}")
    print("=" * 50)
    
    data = load_entries()
    entries = data["entries"]
    active = [e for e in entries if e.get("status") == "active"]
    print(f"📊 当前 {len(active)} active 条目")
    
    # ─── Hard dedup: URL exact + normalized ───
    print("\n🔗 Step 1: URL 硬去重...")
    url_map = {}  # normalized_url -> entry
    exact_dupes = []
    norm_dupes = []
    auto_archived = 0
    
    for e in active:
        url = e.get("url")
        if not url:
            continue
        
        norm = normalize_url(url)
        
        # Exact match first
        exact_key = url.rstrip('/')
        if exact_key in url_map:
            other = url_map[exact_key]
            # Keep higher score
            if (e.get("quality_score", 0) <= other.get("quality_score", 0) - 2):
                e["status"] = "archived"
                auto_archived += 1
                exact_dupes.append({
                    "kept": {"id": other["id"], "title": other.get("title","")[:50], "score": other.get("quality_score")},
                    "removed": {"id": e["id"], "title": e.get("title","")[:50], "score": e.get("quality_score")},
                    "type": "exact"
                })
            elif (other.get("quality_score", 0) <= e.get("quality_score", 0) - 2):
                other["status"] = "archived"
                auto_archived += 1
                exact_dupes.append({
                    "kept": {"id": e["id"], "title": e.get("title","")[:50], "score": e.get("quality_score")},
                    "removed": {"id": other["id"], "title": other.get("title","")[:50], "score": other.get("quality_score")},
                    "type": "exact"
                })
            continue
        
        # Normalized match
        if norm in url_map:
            other = url_map[norm]
            if (e.get("quality_score", 0) <= other.get("quality_score", 0) - 2):
                e["status"] = "archived"
                auto_archived += 1
                norm_dupes.append({
                    "kept": {"id": other["id"], "title": other.get("title","")[:50], "score": other.get("quality_score")},
                    "removed": {"id": e["id"], "title": e.get("title","")[:50], "score": e.get("quality_score")},
                    "type": "normalized"
                })
            elif (other.get("quality_score", 0) <= e.get("quality_score", 0) - 2):
                other["status"] = "archived"
                auto_archived += 1
                norm_dupes.append({
                    "kept": {"id": e["id"], "title": e.get("title","")[:50], "score": e.get("quality_score")},
                    "removed": {"id": other["id"], "title": other.get("title","")[:50], "score": other.get("quality_score")},
                    "type": "normalized"
                })
            continue
        
        url_map[exact_key] = e
        url_map[norm] = e
    
    total_hard = len(exact_dupes) + len(norm_dupes)
    print(f"   精确重复: {len(exact_dupes)} 对")
    print(f"   归一化重复: {len(norm_dupes)} 对")
    print(f"   自动归档: {auto_archived} 条")
    
    # ─── Soft dedup: Title similarity ───
    print("\n📝 Step 2: 标题软去重 (相似度>0.85)...")
    # Group by category
    cat_entries = defaultdict(list)
    for e in entries:
        if e.get("status") != "active":
            continue
        cat_entries[e.get("category", "uncategorized")].append(e)
    
    soft_dupes = []
    for cat, cat_list in cat_entries.items():
        for i in range(len(cat_list)):
            for j in range(i+1, len(cat_list)):
                sim = title_similarity(cat_list[i].get("title",""), cat_list[j].get("title",""))
                if sim > 0.85:
                    soft_dupes.append({
                        "entry1": {"id": cat_list[i]["id"], "title": cat_list[i].get("title","")[:60], "score": cat_list[i].get("quality_score")},
                        "entry2": {"id": cat_list[j]["id"], "title": cat_list[j].get("title","")[:60], "score": cat_list[j].get("quality_score")},
                        "similarity": round(sim, 3),
                        "category": cat
                    })
    
    print(f"   高相似标题: {len(soft_dupes)} 对")
    for sd in soft_dupes[:5]:
        print(f"   - {sd['similarity']}: \"{sd['entry1']['title']}\" vs \"{sd['entry2']['title']}\"")
    
    # ─── Cross-category dedup ───
    print("\n🔀 Step 3: 跨分类检测...")
    # Find entries with same URL base but different categories
    cross_cat = []
    url_cat_map = {}
    for e in entries:
        if e.get("status") != "active":
            continue
        url = e.get("url")
        if not url:
            continue
        norm = normalize_url(url)
        if norm in url_cat_map and url_cat_map[norm]["category"] != e.get("category"):
            cross_cat.append({
                "id": e["id"],
                "title": e.get("title","")[:50],
                "category": e.get("category"),
                "vs_id": url_cat_map[norm]["id"],
                "vs_category": url_cat_map[norm]["category"],
                "url": norm[:80]
            })
        else:
            url_cat_map[norm] = {"id": e["id"], "category": e.get("category")}
    
    print(f"   跨分类疑似: {len(cross_cat)} 条")
    
    # Save
    data["last_updated"] = TODAY
    save_entries(data)
    
    # Generate report
    report = f"""# 去重报告 · {TODAY}

## 总览
- 活跃条目: {len(active)}
- 自动归档: {auto_archived}
- 待人工确认: {len(soft_dupes)} 对标题 + {len(cross_cat)} 条跨分类

## 自动处理

### URL 精确重复: {len(exact_dupes)} 对
"""
    if exact_dupes:
        report += "| 保留 | 分数 | 归档 | 分数 |\n|---|---|---|---|\n"
        for d in exact_dupes:
            report += f"| {d['kept']['title']} | {d['kept']['score']} | {d['removed']['title']} | {d['removed']['score']} |\n"
    
    report += f"\n### URL 归一化重复: {len(norm_dupes)} 对\n"
    if norm_dupes:
        report += "| 保留 | 分数 | 归档 | 分数 |\n|---|---|---|---|\n"
        for d in norm_dupes:
            report += f"| {d['kept']['title']} | {d['kept']['score']} | {d['removed']['title']} | {d['removed']['score']} |\n"
    
    report += f"\n## 待人工确认\n\n### 标题相似 (>{0.85}): {len(soft_dupes)} 对\n"
    if soft_dupes:
        report += "| #1 | 分数 | #2 | 分数 | 相似度 | 分类 |\n|---|---|---|---|---|---|\n"
        for sd in soft_dupes:
            report += f"| {sd['entry1']['title']} | {sd['entry1']['score']} | {sd['entry2']['title']} | {sd['entry2']['score']} | {sd['similarity']} | {sd['category']} |\n"
    
    report += f"\n### 跨分类重复: {len(cross_cat)} 条\n"
    if cross_cat:
        report += "| ID | 标题 | 分类 vs 分类 |\n|---|---|---|\n"
        for cc in cross_cat:
            report += f"| {cc['id']} | {cc['title']} | {cc['category']} vs {cc['vs_category']} |\n"
    
    report_path = LOGS_DIR / f"dedup-report-{TODAY}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n📝 报告: {report_path}")
    
    summary = f"hard_merged={total_hard}, auto_archived={auto_archived}, soft_flagged={len(soft_dupes)}, cross_cat={len(cross_cat)}"
    print(f"\n✅ 去重完成: {summary}")
    
    print(f"::DEDUP_SUMMARY::{json.dumps({
        'hard_dupes': total_hard,
        'auto_archived': auto_archived,
        'soft_flagged': len(soft_dupes),
        'cross_cat': len(cross_cat),
        'total_active': len(active)
    }, ensure_ascii=False)}")

if __name__ == "__main__":
    main()
