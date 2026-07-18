#!/usr/bin/env python3
"""Morning Intake Script - 2026-06-30
Scan last 24h of content/ for new/modified AI .md files,
reconcile with entries.json (append new, fix stale local_path),
then build site. NO git push.
"""
from __future__ import annotations

import json
import re
import sys
import subprocess
from datetime import datetime, date, timedelta
from pathlib import Path

ROOT = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes")
CONTENT_DIR = ROOT / "content"
DATA_PATH = ROOT / "data" / "entries.json"
SCRIPTS_DIR = ROOT / "openclaw" / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))
from pipeline_utils import (
    load_entries_data,
    save_entries_data,
    normalize_entry,
    clean_text,
    today_str,
)

# Image extraction
IMG_RE = re.compile(r"!\[.*?\]\((https?://[^)]+)\)")
META_RE = re.compile(r"^- \*\*([^*]+)\*\*:\s*(.+)$")

SCAN_CUTOFF = datetime.fromisoformat("2026-06-29T08:45:00")
RUN_DATE = date(2026, 6, 30)

def parse_metadata(content: str) -> dict:
    """Extract **Key**: value pairs from header lines"""
    md = {}
    in_header = True
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("---") and in_header:
            # YAML frontmatter - skip
            in_header = False
            continue
        if stripped.startswith("# "):
            in_header = False
            continue
        if not in_header and not stripped.startswith("- **"):
            continue
        m = META_RE.match(stripped)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            md[key] = val
        if stripped.startswith("# ") or stripped.startswith("---"):
            # first heading reached
            in_header = False
    return md

def extract_section(content: str, section_name: str) -> str:
    """Extract content under a ## section header (e.g., '## 中文翻译')."""
    out = []
    capture = False
    for line in content.splitlines():
        if line.strip().lower().startswith("## ") and section_name.lower() in line.lower():
            capture = True
            continue
        if capture and line.strip().startswith("## ") and section_name.lower() not in line.lower():
            break
        if capture:
            out.append(line)
    return "\n".join(out).strip()

def extract_summaries(content: str) -> tuple[str, str]:
    """Return (summary_zh, summary_en) extracted from content/<id>.md file."""
    zh = extract_section(content, "中文翻译")
    en = extract_section(content, "English Original")
    if not zh:
        zh = content  # fallback
    summary_zh = clean_text(zh, max_len=900)
    summary_en = clean_text(en, max_len=900) if en else None
    return summary_zh, summary_en

def extract_images(content: str) -> list[str]:
    seen = []
    seen_set = set()
    for url in IMG_RE.findall(content):
        if url not in seen_set:
            seen.append(url)
            seen_set.add(url)
        if len(seen) >= 5:
            break
    return seen

def build_entry_from_file(path: Path, fallback_id: str, fallback_url: str = "") -> dict:
    """Read content/<id>.md and build a raw entry dict."""
    content = path.read_text(encoding="utf-8")
    md = parse_metadata(content)
    summary_zh, summary_en = extract_summaries(content)
    images = extract_images(content)
    title = md.get("标题") or md.get("title") or path.stem
    title = clean_text(title, max_len=140) or "未命名 AI 资源"
    url = md.get("原文链接") or md.get("url") or fallback_url
    author = md.get("作者") or md.get("author")
    category = md.get("分类") or md.get("category")
    tags_str = md.get("标签") or md.get("tags") or ""
    if isinstance(tags_str, str):
        tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    else:
        tags = tags_str or []
    qstr = md.get("质量评分") or md.get("quality_score") or "3"
    try:
        if "/" in str(qstr):
            quality = int(str(qstr).split("/")[0])
        else:
            quality = int(qstr)
    except (ValueError, TypeError):
        quality = 3
    platform = md.get("平台") or md.get("platform") or "manual"
    source_type = md.get("来源类型") or md.get("source_type") or "article"
    original_date = md.get("日期") or md.get("original_date")

    raw = {
        "id": fallback_id,
        "title": title,
        "url": url,
        "source": {
            "platform": platform,
            "author": author,
            "original_date": original_date,
        },
        "category": category,
        "tags": tags,
        "source_type": source_type,
        "language": "both" if (summary_en and summary_zh) else ("zh" if summary_zh else "en"),
        "summary_zh": summary_zh,
        "summary_en": summary_en,
        "quality_score": max(1, min(5, quality)),
        "local_path": f"content/{path.name}",
        "images": images,
        "added_date": today_str(),
    }
    return raw

def main():
    print(f"[Morning Intake] {RUN_DATE.isoformat()}")
    print(f"Scan cutoff: {SCAN_CUTOFF.isoformat()}")
    print(f"Content dir: {CONTENT_DIR}")

    data = load_entries_data(DATA_PATH)
    entries = data["entries"]
    initial_count = len(entries)

    # Index existing entries by id and by local_path basename
    by_id = {e["id"]: e for e in entries if e.get("id")}
    by_local = {}
    for e in entries:
        lp = e.get("local_path") or ""
        if lp:
            by_local.setdefault(Path(lp).name, e)

    # Scan content/ for files modified in last 24h
    recent_files = []
    for p in CONTENT_DIR.glob("*.md"):
        mtime = datetime.fromtimestamp(p.stat().st_mtime)
        if mtime >= SCAN_CUTOFF:
            recent_files.append((p, mtime))
    recent_files.sort(key=lambda x: x[1])

    print(f"\nFiles modified in last 24h: {len(recent_files)}")

    added, fixed = [], []
    skipped = []

    for path, mtime in recent_files:
        file_id = path.stem  # filename without .md
        existing = by_id.get(file_id)
        # Fallback: try local_path basename match
        if existing is None:
            existing = by_local.get(path.name)

        if existing:
            current_lp = existing.get("local_path") or ""
            current_basename = Path(current_lp).name if current_lp else ""
            if current_basename == path.name:
                # local_path already correct → no action
                continue
            # local_path is stale → fix it + re-extract summaries
            content = path.read_text(encoding="utf-8")
            _, summary_en = extract_summaries(content)
            summary_zh, _ = extract_summaries(content)
            existing["local_path"] = f"content/{path.name}"
            existing["updated_date"] = today_str()
            if summary_zh and (not existing.get("summary_zh") or len(existing.get("summary_zh","")) < 100):
                existing["summary_zh"] = summary_zh
            if summary_en and (not existing.get("summary_en") or len(existing.get("summary_en","")) < 100):
                existing["summary_en"] = summary_en
            fixed.append({
                "id": existing["id"],
                "title": existing.get("title",""),
                "old_local_path": current_lp,
                "new_local_path": existing["local_path"],
                "mtime": mtime.isoformat(),
            })
            print(f"  [FIX-LP] {existing['id']}: {current_lp} → {existing['local_path']}")
            continue

        # Truly new entry → build, normalize, append
        raw = build_entry_from_file(path, fallback_id=file_id)
        normalized = normalize_entry(raw, run_date=RUN_DATE)
        # Append only if not already present by id
        if any(e.get("id") == normalized["id"] for e in entries):
            skipped.append((file_id, "duplicate-id"))
            continue
        entries.append(normalized)
        by_id[normalized["id"]] = normalized
        by_local[path.name] = normalized
        added.append({
            "id": normalized["id"],
            "title": normalized.get("title",""),
            "url": normalized.get("url"),
            "category": normalized.get("category"),
            "quality_score": normalized.get("quality_score"),
            "status": normalized.get("status"),
        })
        print(f"  [NEW] {normalized['id']}: {normalized.get('title','')[:60]}")

    # Always update last_updated/total_entries
    final_count = len(entries)
    data["last_updated"] = today_str()
    data["total_entries"] = final_count

    if added or fixed:
        save_entries_data(data, DATA_PATH)
        print(f"\n[SAVE] entries.json updated ({initial_count} → {final_count}, +{final_count-initial_count})")
    else:
        print(f"\n[SKIP-SAVE] No changes; entries.json untouched")

    # Validate
    print("\n[VALIDATE] running validate-schema.py")
    validate_proc = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "validate-schema.py"), str(DATA_PATH)],
        capture_output=True, text=True,
    )
    print(validate_proc.stdout[-2000:] if validate_proc.stdout else "(no stdout)")
    if validate_proc.returncode != 0:
        print(validate_proc.stderr[-2000:])
        sys.exit(1)

    # Build site
    print("\n[BUILD] npm run build")
    build_proc = subprocess.run(
        ["npm", "run", "build"],
        cwd=str(ROOT), capture_output=True, text=True,
    )
    print(build_proc.stdout[-2500:] if build_proc.stdout else "(no stdout)")
    if build_proc.returncode != 0:
        print(build_proc.stderr[-2500:])
        sys.exit(1)

    # Summary
    summary = {
        "date": RUN_DATE.isoformat(),
        "task": "morning_intake_incremental",
        "scan_window": f"{SCAN_CUTOFF.isoformat()} → {RUN_DATE.isoformat()}",
        "content_files_scanned": len(recent_files),
        "new_entries_added": len(added),
        "local_path_fixed": len(fixed),
        "skipped": len(skipped),
        "total_entries_before": initial_count,
        "total_entries_after": final_count,
        "added": added,
        "fixed": fixed,
        "git_push": "skipped (delegated to evening intake)",
    }
    summary_path = ROOT / "data" / f"intake_summary_{RUN_DATE.isoformat()}.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[SUMMARY] saved → {summary_path}")
    print(json.dumps({k: v for k, v in summary.items() if k not in {"added", "fixed"}}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
