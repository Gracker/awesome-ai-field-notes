#!/usr/bin/env python3
"""
import-entries.py — 从 CSV/JSON 批量导入条目到 entries.json

用法:
  python3 scripts/import-entries.py input.csv
  python3 scripts/import-entries.py input.json
  python3 scripts/import-entries.py input.jsonl

CSV 格式要求（表头）:
  title, url, category, tags, source_type, language, one_liner, quality_score

JSON/JSONL 格式: 每条与 entries.json entry schema 一致（id 可选，自动生成）
"""

import json
import csv
import sys
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
ENTRIES_PATH = BASE_DIR / "data" / "entries.json"

def generate_id():
    """生成 8 位简易 ID"""
    import random, string
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))

def load_categories():
    with open(BASE_DIR / "metadata" / "categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_valid_categories(cats):
    valid = set()
    for cat_key, cat_info in cats.items():
        for child_key in cat_info.get("children", {}):
            valid.add(f"{cat_key}/{child_key}")
    return valid

def load_existing_entries():
    if ENTRIES_PATH.exists():
        with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, data.get("entries", [])
    return {"version": "1.0.0", "last_updated": "", "entries": []}, []

def dedup_check(entries, url, title):
    """检查是否重复"""
    for e in entries:
        if e.get("url") == url:
            return True
        # 简单标题相似度
        if e.get("title", "").lower() == title.lower():
            return True
    return False

def import_csv(filepath, entries):
    added = 0
    skipped = 0
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get("url", "").strip()
            title = row.get("title", "").strip()
            if not url or not title:
                skipped += 1
                continue
            if dedup_check(entries, url, title):
                skipped += 1
                continue
            
            tags = [t.strip() for t in row.get("tags", "").split(",") if t.strip()]
            
            entry = {
                "id": generate_id(),
                "title": title,
                "url": url,
                "category": row.get("category", "uncategorized").strip(),
                "tags": tags,
                "source_type": row.get("source_type", "article").strip(),
                "language": row.get("language", "en").strip(),
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "updated_date": None,
                "one_liner": row.get("one_liner", "").strip(),
                "quality_score": int(row.get("quality_score", 3)),
                "status": "active",
                "github_stars": None,
                "related": [],
            }
            entries.append(entry)
            added += 1
    
    return added, skipped

def import_json(filepath, entries):
    added = 0
    skipped = 0
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    if content.startswith("["):
        items = json.loads(content)
    else:
        # JSONL
        items = [json.loads(line) for line in content.split("\n") if line.strip()]
    
    for item in items:
        url = item.get("url", "").strip()
        title = item.get("title", "").strip()
        if not url or not title:
            skipped += 1
            continue
        if dedup_check(entries, url, title):
            skipped += 1
            continue
        
        # 保留原有字段，补充默认值
        entry = {
            "id": item.get("id", generate_id()),
            "title": title,
            "url": url,
            "category": item.get("category", "uncategorized"),
            "tags": item.get("tags", []),
            "source_type": item.get("source_type", "article"),
            "language": item.get("language", "en"),
            "added_date": item.get("added_date", datetime.now().strftime("%Y-%m-%d")),
            "updated_date": item.get("updated_date", None),
            "one_liner": item.get("one_liner", ""),
            "quality_score": item.get("quality_score", 3),
            "status": item.get("status", "active"),
            "github_stars": item.get("github_stars", None),
            "related": item.get("related", []),
        }
        entries.append(entry)
        added += 1
    
    return added, skipped

def main():
    if len(sys.argv) < 2:
        print("用法: python3 scripts/import-entries.py <input.csv|json|jsonl>")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"❌ 文件不存在: {filepath}")
        sys.exit(1)
    
    data, entries = load_existing_entries()
    
    suffix = filepath.suffix.lower()
    print(f"📥 导入 {filepath.name} (当前 {len(entries)} 条)...")
    
    if suffix == ".csv":
        added, skipped = import_csv(filepath, entries)
    elif suffix in (".json", ".jsonl"):
        added, skipped = import_json(filepath, entries)
    else:
        print(f"❌ 不支持的格式: {suffix}")
        sys.exit(1)
    
    data["entries"] = entries
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 导入完成: +{added} 新增, {skipped} 跳过(重复/缺失), 共 {len(entries)} 条")

if __name__ == "__main__":
    main()
