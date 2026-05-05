#!/usr/bin/env python3
"""
validate-schema.py — 校验 entries.json v2.0 结构合规

用法: python3 scripts/validate-schema.py [data/entries.json]
退出码: 0=通过, 1=有错误
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
BASE_DIR = SCRIPT_PATH.parent.parent
if BASE_DIR.name == "openclaw":
    candidate = BASE_DIR.parent
    if (candidate / "data" / "entries.json").exists():
        BASE_DIR = candidate

VALID_SOURCE_TYPES = {"github", "paper", "article", "x_post", "tweet", "newsletter", "video", "product", "dataset"}
VALID_LANGUAGES = {"en", "zh", "both"}
VALID_STATUSES = {"active", "archived", "deprecated", "score-pending"}
VALID_ONE_LINER_AUTHORS = {"gracker", "openclaw", "community-pending"}
VALID_PLATFORMS = {
    "x",
    "twitter",
    "cubox",
    "arxiv",
    "github",
    "blog",
    "newsletter",
    "youtube",
    "manual",
    "unknown",
    "wechat",
    "news",
    "google",
    "anthropic",
    "community",
}
RELATIVE_DATE_WORDS = {
    "今天", "昨天", "前天", "明天", "后天", "今日", "昨日", "本周", "上周", "下周",
    "today", "yesterday", "tomorrow", "this week", "last week", "next week",
}
CATEGORY_ALIASES = {
    "agent-frameworks": "agents",
    "coding-agents": "coding",
    "coding-ai": "coding",
    "developer-tools": "coding",
    "ai-tools": "coding",
    "workflow": "coding",
    "prompt": "learning",
    "prompt-engineering": "learning",
    "content-creation": "industry",
    "strategy": "industry",
    "ai-ux": "industry",
    "llm-infra": "infra",
    "llm-engineering": "infra",
    "llm-engineering/inference-optimization": "infra",
    "infrastructure": "infra",
    "hardware-chips": "infra",
    "ai-hardware": "infra",
    "multimodal": "infra",
    "ai-safety": "industry",
    "business": "industry",
    "research": "learning",
    "tools": "uncategorized",
    "tools-development": "uncategorized",
    "research-methods": "learning",
    "education": "learning",
}

def load_categories():
    with open(BASE_DIR / "metadata" / "categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_valid_categories(cats):
    valid = set(cats.keys())
    valid.add("uncategorized")
    return valid

def is_known_category(category, valid_categories):
    if category in valid_categories:
        return True
    prefix = str(category or "").split("/", 1)[0]
    return prefix in valid_categories or category in CATEGORY_ALIASES or prefix in CATEGORY_ALIASES

def has_relative_date_word(value):
    if not isinstance(value, str):
        return False
    lowered = value.lower()
    return any(word in lowered for word in RELATIVE_DATE_WORDS)


def is_low_signal_entry(entry):
    title = str(entry.get("title") or "")
    summary = str(entry.get("summary_zh") or "")
    summary_en = str(entry.get("summary_en") or "")
    one_liner = str(entry.get("one_liner") or "")
    tags = {str(t).lower() for t in entry.get("tags", [])}
    return (
        title.startswith("高价值AI内容 -")
        or one_liner.startswith("高价值AI内容 -")
        or re.match(r"^来自@[^，。\s]+的高价值AI相关内容", summary) is not None
        or summary_en.startswith("High-value AI content from @")
        or ("high-value" in tags and len(summary) < 50)
    )

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
    seen_active_urls = set()
    seen_ids = set()
    
    for i, e in enumerate(entries):
        idx = f"[#{i}]"
        
        # Required fields
        for field in ["id", "title", "category", "source_type", "language", 
                       "summary_zh", "one_liner", "one_liner_author",
                       "quality_score", "status", "added_date", "local_path"]:
            if field not in e:
                errors.append(f"{idx} 缺少必填字段: {field}")
        
        if "id" not in e:
            continue
        
        eid = e["id"]
        
        # ID unique
        if eid in seen_ids:
            errors.append(f"{idx} ID 重复: {eid}")
        seen_ids.add(eid)
        
        # Active URL unique (archived duplicates can remain as historical records)
        url = e.get("url")
        if url and e.get("status") == "active":
            if url in seen_active_urls:
                warnings.append(f"{idx} 活跃 URL 重复: {url}")
            seen_active_urls.add(url)
        
        # source object
        source = e.get("source")
        if source is None:
            errors.append(f"{idx} 缺少 source 对象")
        else:
            if not isinstance(source, dict):
                errors.append(f"{idx} source 必须是对象")
            else:
                platform = source.get("platform", "unknown")
                if platform not in VALID_PLATFORMS:
                    warnings.append(f"{idx} 未知 platform: {platform}")
        
        # source_type
        if e.get("source_type") not in VALID_SOURCE_TYPES:
            errors.append(f"{idx} 无效 source_type: {e.get('source_type')}")
        
        # language
        if e.get("language") not in VALID_LANGUAGES:
            errors.append(f"{idx} 无效 language: {e.get('language')}")
        
        # status
        if e.get("status") not in VALID_STATUSES:
            errors.append(f"{idx} 无效 status: {e.get('status')}")
        
        # one_liner_author
        if e.get("one_liner_author") not in VALID_ONE_LINER_AUTHORS:
            errors.append(f"{idx} 无效 one_liner_author: {e.get('one_liner_author')}")
        
        # quality_score
        score = e.get("quality_score")
        if not isinstance(score, int) or not (1 <= score <= 5):
            errors.append(f"{idx} quality_score 必须是 1-5 整数: {score}")
        
        # category
        if not is_known_category(e.get("category"), valid_cats):
            warnings.append(f"{idx} 未知分类: {e.get('category')}")
        
        # summary_zh length
        summary = e.get("summary_zh", "")
        if e.get("status") == "active" and len(summary) > 0 and len(summary) < 20:
            warnings.append(f"{idx} summary_zh 过短: {len(summary)} 字符")
        if e.get("status") == "active" and e.get("quality_score", 0) >= 3 and is_low_signal_entry(e):
            warnings.append(f"{idx} 活跃高分条目疑似占位内容，应补充可读标题/摘要或归档: {e.get('id')}")
        
        # date format
        for date_field in ["added_date", "updated_date", "published_date"]:
            val = e.get(date_field)
            if val is not None:
                if has_relative_date_word(val):
                    errors.append(f"{idx} {date_field} 禁止相对日期: {val} (应为 YYYY-MM-DD)")
                    continue
                try:
                    datetime.strptime(val, "%Y-%m-%d")
                except ValueError:
                    errors.append(f"{idx} {date_field} 格式错误: {val} (应为 YYYY-MM-DD)")
        
        # source.original_date
        orig_date = (e.get("source") or {}).get("original_date")
        if orig_date is not None:
            if has_relative_date_word(orig_date):
                errors.append(f"{idx} source.original_date 禁止相对日期: {orig_date} (应为 YYYY-MM-DD)")
            else:
                try:
                    datetime.strptime(orig_date, "%Y-%m-%d")
                except ValueError:
                    warnings.append(f"{idx} source.original_date 格式非 YYYY-MM-DD: {orig_date}")
        
        # images must be array
        if "images" in e and not isinstance(e["images"], list):
            errors.append(f"{idx} images 必须是数组")
        
        # local_path should exist as a hint
        local = e.get("local_path")
        if local and not local.endswith(".md") and not local.endswith(".pdf"):
            warnings.append(f"{idx} local_path 扩展名异常: {local}")
    
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
