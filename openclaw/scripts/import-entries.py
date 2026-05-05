#!/usr/bin/env python3
"""
import-entries.py — 从 CSV/JSON/JSONL 批量导入条目到 entries.json (v2 schema)

用法:
  python3 scripts/import-entries.py input.csv
  python3 scripts/import-entries.py input.json
  python3 scripts/import-entries.py input.jsonl

CSV 格式要求（表头）:
  title, url, platform, author, original_date, category, tags, source_type, language, summary_zh

JSON/JSONL 格式: 每条与 entries.json entry schema 一致（id 可选，自动生成）
"""

import json
import csv
import sys
from pathlib import Path
from pipeline_utils import append_entries, generate_entry_id, project_root, save_entries_data

BASE_DIR = project_root()
ENTRIES_PATH = BASE_DIR / "data" / "entries.json"

def generate_id():
    return generate_entry_id()

def load_existing_entries():
    if ENTRIES_PATH.exists():
        with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, data.get("entries", [])
    return {"version": "2.0.0", "schema_description": "", "last_updated": "", "entries": []}, []

def dedup_check(entries, url, title):
    if url and any(e.get("url") == url for e in entries):
        return True
    if any(e.get("title", "").lower() == title.lower() for e in entries):
        return True
    return False

def make_entry(**kwargs):
    """补全默认值的 entry 工厂"""
    return {
        "id": kwargs.get("id") or generate_entry_id(title=kwargs.get("title", ""), url=kwargs.get("url") or ""),
        "title": kwargs.get("title", ""),
        "url": kwargs.get("url") or None,
        "source": {
            "platform": kwargs.get("platform", "unknown"),
            "author": kwargs.get("author") or None,
            "original_date": kwargs.get("original_date") or None,
        },
        "category": kwargs.get("category", "uncategorized"),
        "tags": kwargs.get("tags", []),
        "source_type": kwargs.get("source_type", "article"),
        "language": kwargs.get("language", "en"),
        "summary_zh": kwargs.get("summary_zh", ""),
        "summary_en": kwargs.get("summary_en") or None,
        "one_liner": kwargs.get("one_liner", "待人工点评"),
        "one_liner_author": kwargs.get("one_liner_author", "openclaw"),
        "quality_score": kwargs.get("quality_score", 3),
        "status": kwargs.get("status", "score-pending"),
        "local_path": kwargs.get("local_path") or "",
        "images": kwargs.get("images", []),
        "added_date": kwargs.get("added_date"),
        "updated_date": kwargs.get("updated_date") or None,
        "github_stars": kwargs.get("github_stars") or None,
        "related": kwargs.get("related", []),
    }

def import_csv(filepath, entries):
    added, skipped = 0, 0
    pending = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get("url", "").strip()
            title = row.get("title", "").strip()
            if not title:
                skipped += 1; continue
            if dedup_check(entries, url, title):
                skipped += 1; continue
            tags = [t.strip() for t in row.get("tags", "").split(",") if t.strip()]
            entry = make_entry(
                title=title, url=url,
                platform=row.get("platform", "").strip() or "unknown",
                author=row.get("author", "").strip() or None,
                original_date=row.get("original_date", "").strip() or None,
                category=row.get("category", "uncategorized").strip(),
                tags=tags,
                source_type=row.get("source_type", "article").strip(),
                language=row.get("language", "en").strip(),
                summary_zh=row.get("summary_zh", "").strip(),
                summary_en=row.get("summary_en", "").strip() or None,
            )
            pending.append(entry)
    added_entries, skipped_entries = append_entries({"entries": entries}, pending)
    added += len(added_entries)
    skipped += len(skipped_entries)
    return added, skipped

def import_json(filepath, entries):
    added, skipped = 0, 0
    pending = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    items = json.loads(content) if content.startswith("[") else [json.loads(l) for l in content.split("\n") if l.strip()]
    
    for item in items:
        url = item.get("url", "")
        title = item.get("title", "")
        if not title:
            skipped += 1; continue
        if dedup_check(entries, url, title):
            skipped += 1; continue
        entry = make_entry(**item)
        pending.append(entry)
    added_entries, skipped_entries = append_entries({"entries": entries}, pending)
    added += len(added_entries)
    skipped += len(skipped_entries)
    return added, skipped

def main():
    if len(sys.argv) < 2:
        print("用法: python3 scripts/import-entries.py <input.csv|json|jsonl>")
        sys.exit(1)
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"❌ 文件不存在: {filepath}"); sys.exit(1)
    
    data, entries = load_existing_entries()
    suffix = filepath.suffix.lower()
    print(f"📥 导入 {filepath.name} (当前 {len(entries)} 条)...")
    
    if suffix == ".csv":
        added, skipped = import_csv(filepath, entries)
    elif suffix in (".json", ".jsonl"):
        added, skipped = import_json(filepath, entries)
    else:
        print(f"❌ 不支持的格式: {suffix}"); sys.exit(1)
    
    data["entries"] = entries
    save_entries_data(data, ENTRIES_PATH)
    
    print(f"✅ 导入完成: +{added} 新增, {skipped} 跳过, 共 {len(entries)} 条")

if __name__ == "__main__":
    main()
