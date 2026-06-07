#!/usr/bin/env python3
"""
weekly-maintain.py — AAIF 周维护脚本
执行：时效归档、本地路径校验、图片URL抽样校验
输出：维护报告到 logs/
"""

import json
import os
import random
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pipeline_utils import has_readable_text, is_ai_related_entry, is_low_signal_entry, is_placeholder_text, project_root

BASE_DIR = project_root()
ENTRIES_PATH = BASE_DIR / "data" / "entries.json"
LOGS_DIR = BASE_DIR / "logs"
CONTENT_DIR = BASE_DIR / "content"

TODAY = datetime.now().strftime("%Y-%m-%d")
CUTOFF_DAYS = 180

def load_entries():
    with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_entries(data):
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def content_is_readable(entry):
    content_path = CONTENT_DIR / f"{entry.get('id')}.md"
    if not content_path.exists():
        return False
    try:
        return has_readable_text(content_path.read_text(encoding="utf-8", errors="replace"), min_len=80)
    except OSError:
        return False

# ─── Step 0: Public readability guardrail ───
def quarantine_low_signal_entries(data):
    quarantined = []
    for e in data["entries"]:
        if e.get("status") != "active":
            continue
        readable = (
            has_readable_text(e.get("summary_zh") or "")
            or has_readable_text(e.get("one_liner") or "")
            or content_is_readable(e)
        )
        placeholder_only = (
            is_placeholder_text(e.get("summary_zh") or "")
            and is_placeholder_text(e.get("one_liner") or "")
            and not content_is_readable(e)
        )
        if is_low_signal_entry(e) or (not is_ai_related_entry(e) and not readable) or placeholder_only:
            e["status"] = "score-pending"
            e["quality_score"] = min(int(e.get("quality_score") or 1), 2)
            e["updated_date"] = TODAY
            quarantined.append({"id": e["id"], "title": e.get("title", "")[:50]})
    return quarantined

# ─── Step 1: Time-based archival ───
def archive_old_low_score(data):
    cutoff = (datetime.now() - timedelta(days=CUTOFF_DAYS)).strftime("%Y-%m-%d")
    archived = []
    for e in data["entries"]:
        if e.get("status") != "active":
            continue
        if e.get("source_type") not in ("article", "x_post"):
            continue
        if not e.get("added_date"):
            continue
        if e["added_date"] < cutoff and e.get("quality_score", 5) <= 3:
            e["status"] = "archived"
            archived.append({"id": e["id"], "title": e.get("title","")[:50]})
    return archived

# ─── Step 2: Local path validation ───
def validate_local_paths(data):
    missing = []
    for e in data["entries"]:
        if e.get("status") != "active":
            continue
        lp = e.get("local_path")
        if not lp:
            continue
        full_path = BASE_DIR / lp
        if not full_path.exists():
            e["local_path_valid"] = False
            missing.append({"id": e["id"], "title": e.get("title","")[:50], "path": lp})
    return missing

# ─── Step 3: Image URL sampling ───
def check_image_urls(data, sample_size=20):
    entries_with_images = [e for e in data["entries"] if e.get("status") == "active" and e.get("images")]
    if not entries_with_images:
        return [], 0, []
    
    sample = random.sample(entries_with_images, min(sample_size, len(entries_with_images)))
    checked = 0
    failed = []
    
    for e in sample:
        for img_url in e["images"][:2]:  # check up to 2 images per entry
            try:
                req = Request(img_url, method="HEAD")
                req.add_header("User-Agent", "Mozilla/5.0 (compatible; AAIF-Bot/1.0)")
                resp = urlopen(req, timeout=10)
                checked += 1
            except Exception as ex:
                checked += 1
                failed.append({
                    "entry_id": e["id"],
                    "title": e.get("title","")[:40],
                    "url": img_url[:100],
                    "error": str(ex)[:80]
                })
                break  # one fail per entry is enough
            time.sleep(0.3)
    
    return sample, checked, failed

def main():
    print(f"🔧 AAIF 周维护 · {TODAY}")
    print("=" * 50)
    
    data = load_entries()
    entries = data["entries"]
    active_before = sum(1 for e in entries if e.get("status") == "active")
    print(f"📊 当前: {len(entries)} 条目 ({active_before} active)")
    
    # Step 0: Public readability guardrail
    print("\n🧹 Step 0: 可读性门禁（低信号/非AI/无摘要 → score-pending）...")
    quarantined = quarantine_low_signal_entries(data)
    print(f"   挂起: {len(quarantined)} 条")
    for q in quarantined[:5]:
        print(f"   - {q['id']}: {q['title']}")
    if len(quarantined) > 5:
        print(f"   - ... 还有 {len(quarantined)-5} 条")

    # Step 1: Archive
    print("\n📅 Step 1: 时效归档 (>180天, score≤3)...")
    archived = archive_old_low_score(data)
    print(f"   归档: {len(archived)} 条")
    for a in archived[:5]:
        print(f"   - {a['id']}: {a['title']}")
    if len(archived) > 5:
        print(f"   - ... 还有 {len(archived)-5} 条")
    
    # Step 2: Local paths
    print("\n📂 Step 2: 本地路径校验...")
    missing_paths = validate_local_paths(data)
    print(f"   缺失: {len(missing_paths)} 条")
    for m in missing_paths[:5]:
        print(f"   - {m['id']}: {m['path']}")
    if len(missing_paths) > 5:
        print(f"   - ... 还有 {len(missing_paths)-5} 条")
    
    # Step 3: Image URLs
    print("\n🖼️  Step 3: 图片URL抽样校验 (20条)...")
    sample, checked, failed_images = check_image_urls(data)
    print(f"   抽样: {len(sample)} 条目, 检查 {checked} URL")
    print(f"   失效: {len(failed_images)} 条")
    for f in failed_images[:5]:
        print(f"   - {f['entry_id']}: {f['error']}")
    
    # Save
    data["last_updated"] = TODAY
    save_entries(data)
    
    active_after = sum(1 for e in data["entries"] if e.get("status") == "active")
    
    # Report
    report = f"""# 维护报告 · {TODAY}

## 总览
- 总条目: {len(entries)}
- Active: {active_before} → {active_after}
- 可读性挂起: {len(quarantined)}
- 归档: {len(archived)}

## 时效归档
归档条件: added_date > {CUTOFF_DAYS}天 且 score ≤ 3
归档数量: {len(archived)}
"""
    if archived:
        report += "\n| ID | 标题 |\n|---|---|\n"
        for a in archived:
            report += f"| {a['id']} | {a['title']} |\n"
    
    report += f"""
## 本地路径校验
缺失数量: {len(missing_paths)}
"""
    if missing_paths:
        report += "\n| ID | 路径 |\n|---|---|\n"
        for m in missing_paths:
            report += f"| {m['id']} | {m['path']} |\n"
    
    report += f"""
## 图片URL抽样
抽样: {len(sample)} 条目, 检查 {checked} URL
失效: {len(failed_images)} 条
"""
    if failed_images:
        report += "\n| Entry | 错误 |\n|---|---|\n"
        for fi in failed_images:
            report += f"| {fi['entry_id']} | {fi['error']} |\n"
    
    report_path = LOGS_DIR / f"maintain-report-{TODAY}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n📝 报告: {report_path}")
    
    # Summary line for git commit
    summary = f"archived={len(archived)}, missing_paths={len(missing_paths)}, img_failures={len(failed_images)}"
    print(f"\n✅ 维护完成: {summary}")
    
    # Output summary for caller
    print(f"::MAINTAIN_SUMMARY::{json.dumps({
        'archived': len(archived),
        'quarantined': len(quarantined),
        'missing_paths': len(missing_paths),
        'img_sampled': len(sample),
        'img_checked': checked,
        'img_failed': len(failed_images),
        'active_before': active_before,
        'active_after': active_after,
        'total': len(entries)
    }, ensure_ascii=False)}")

if __name__ == "__main__":
    main()
