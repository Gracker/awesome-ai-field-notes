#!/usr/bin/env python3
"""
refresh-stars.py — 批量刷新 GitHub 项目 stars

用法: python3 scripts/refresh-stars.py
需要 GITHUB_TOKEN 环境变量（无 token 限 60 次/小时，有 token 5000 次/小时）
"""

import json
import os
import sys
import time
from pathlib import Path
from pipeline_utils import project_root

BASE_DIR = project_root()
ENTRIES_PATH = BASE_DIR / "data" / "entries.json"

def parse_github_url(url):
    """从 URL 提取 owner/repo"""
    url = url.rstrip("/")
    if "/repos/" in url:
        parts = url.split("/repos/")[-1].split("/")
    elif "github.com" in url:
        parts = url.split("github.com/")[-1].split("/")
    else:
        return None
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return None

def fetch_stars(owner_repo, token):
    """通过 GitHub API 获取 stars 和 archived 状态"""
    import urllib.request
    url = f"https://api.github.com/repos/{owner_repo}"
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "ai-field-notes-bot")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return {
                "stars": data.get("stargazers_count", 0),
                "archived": data.get("archived", False),
                "description": data.get("description", ""),
            }
    except Exception as ex:
        print(f"  ⚠️  {owner_repo}: {ex}", file=sys.stderr)
        return None

def main():
    with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    token = os.environ.get("GITHUB_TOKEN", "")
    
    github_entries = []
    for e in data.get("entries", []):
        if e.get("source_type") != "github":
            continue
        owner_repo = parse_github_url(e.get("url", ""))
        if owner_repo:
            github_entries.append((e, owner_repo))
    
    print(f"🔍 找到 {len(github_entries)} 个 GitHub 条目")
    
    updated = 0
    archived_count = 0
    
    for i, (entry, owner_repo) in enumerate(github_entries):
        if token and (i + 1) % 50 == 0:
            print(f"  💤 速率控制: 等待 60s (已完成 {i+1}/{len(github_entries)})")
            time.sleep(60)
        
        result = fetch_stars(owner_repo, token)
        if result is None:
            continue
        
        old_stars = entry.get("github_stars")
        new_stars = result["stars"]
        
        if old_stars != new_stars:
            entry["github_stars"] = new_stars
            updated += 1
            if old_stars:
                diff = new_stars - old_stars
                print(f"  ⭐ {owner_repo}: {old_stars:,} → {new_stars:,} ({diff:+,})")
            else:
                print(f"  ⭐ {owner_repo}: {new_stars:,}")
        
        if result["archived"] and entry.get("status") != "deprecated":
            entry["status"] = "deprecated"
            archived_count += 1
            print(f"  📦 {owner_repo}: 项目已归档 → deprecated")
        
        # 无 token 时限速
        if not token:
            time.sleep(1)
    
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 完成: 刷新 {updated} 条 stars, 标记 {archived_count} 条归档")

if __name__ == "__main__":
    main()
