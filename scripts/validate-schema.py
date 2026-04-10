#!/usr/bin/env python3
"""
validate-schema.py — 校验 entries.json 结构合规

用法: python3 scripts/validate-schema.py [data/entries.json]
退出码: 0=通过, 1=有错误
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent

VALID_SOURCE_TYPES = {"github", "paper", "article", "x_post", "newsletter", "video", "product", "dataset"}
VALID_LANGUAGES = {"en", "zh", "both"}
VALID_STATUSES = {"active", "archived", "deprecated"}

def load_categories():
    with open(BASE_DIR / "metadata" / "categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_valid_categories(cats):
    valid = set()
    for cat_key, cat_info in cats.items():
        for child_key in cat_info.get("children", {}):
            valid.add(f"{cat_key}/{child_key}")
    valid.add("uncategorized")
    return valid

def validate_entries(filepath=None):
    if filepath is None:
        filepath = BASE_DIR / "data" / "entries.json"
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    entries = data.get("entries", [])
    cats = load_categories()
    valid_cats = get_valid_categories(cats)
    
    errors = []
    warnings = []
    seen_urls = set()
    seen_ids = set()
    
    for i, e in enumerate(entries):
        idx = f"[#{i}]"
        
        # Required fields
        for field in ["id", "title", "url", "category", "source_type", "added_date", "quality_score", "status"]:
            if field not in e:
                errors.append(f"{idx} 缺少必填字段: {field}")
        
        if "id" not in e:
            continue
        
        eid = e["id"]
        
        # ID unique
        if eid in seen_ids:
            errors.append(f"{idx} ID 重复: {eid}")
        seen_ids.add(eid)
        
        # ID format (nanoid 8位-ish, or any non-empty string)
        if len(eid) < 4:
            warnings.append(f"{idx} ID 过短: {eid}")
        
        # URL unique
        url = e.get("url", "")
        if url in seen_urls:
            errors.append(f"{idx} URL 重复: {url}")
        seen_urls.add(url)
        
        # source_type
        if e.get("source_type") not in VALID_SOURCE_TYPES:
            errors.append(f"{idx} 无效 source_type: {e.get('source_type')}")
        
        # language
        if e.get("language") not in VALID_LANGUAGES:
            errors.append(f"{idx} 无效 language: {e.get('language')}")
        
        # status
        if e.get("status") not in VALID_STATUSES:
            errors.append(f"{idx} 无效 status: {e.get('status')}")
        
        # quality_score
        score = e.get("quality_score")
        if not isinstance(score, int) or not (1 <= score <= 5):
            errors.append(f"{idx} quality_score 必须是 1-5 整数: {score}")
        
        # category
        if e.get("category") not in valid_cats:
            warnings.append(f"{idx} 未知分类: {e.get('category')}")
        
        # date format
        for date_field in ["added_date", "updated_date"]:
            val = e.get(date_field)
            if val is not None:
                try:
                    datetime.strptime(val, "%Y-%m-%d")
                except ValueError:
                    errors.append(f"{idx} {date_field} 格式错误: {val} (应为 YYYY-MM-DD)")
        
        # one_liner check (如果存在)
        one_liner = e.get("one_liner", "")
        if one_liner and len(one_liner) < 5:
            warnings.append(f"{idx} one_liner 过短: {one_liner[:50]}")
    
    # Summary
    print(f"📊 校验完成: {len(entries)} 条目, {len(errors)} 错误, {len(warnings)} 警告")
    
    if warnings:
        print(f"\n⚠️  警告 ({len(warnings)}):")
        for w in warnings[:20]:
            print(f"  - {w}")
        if len(warnings) > 20:
            print(f"  - ... 还有 {len(warnings) - 20} 条")
    
    if errors:
        print(f"\n❌ 错误 ({len(errors)}):")
        for err in errors[:30]:
            print(f"  - {err}")
        if len(errors) > 30:
            print(f"  - ... 还有 {len(errors) - 30} 条")
        return 1
    
    return 0

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(validate_entries(filepath))
