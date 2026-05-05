#!/usr/bin/env python3
"""
check-links.py — 批量检测死链

用法: python3 scripts/check-links.py
连续 3 次检测失效的条目会标记为 archived
"""

import json
import sys
import time
from pathlib import Path
from datetime import datetime
from pipeline_utils import project_root

BASE_DIR = project_root()
ENTRIES_PATH = BASE_DIR / "data" / "entries.json"
LINK_LOG = BASE_DIR / "metadata" / "link-check-log.json"

def check_url(url, timeout=10):
    """HTTP HEAD 检测，返回 (status_code, is_alive)"""
    import urllib.request
    import urllib.error
    
    req = urllib.request.Request(url, method="HEAD")
    req.add_header("User-Agent", "ai-field-notes-bot/1.0")
    
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, True
    except urllib.error.HTTPError as e:
        # 4xx 不算死链（可能是权限问题）
        return e.code, e.code < 500
    except Exception:
        return 0, False

def main():
    with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 加载历史检测记录
    log = {}
    if LINK_LOG.exists():
        with open(LINK_LOG, "r", encoding="utf-8") as f:
            log = json.load(f)
    
    entries = data.get("entries", [])
    active = [e for e in entries if e.get("status") == "active"]
    
    print(f"🔍 检测 {len(active)} 条活跃链接...")
    
    dead_count = 0
    archived_count = 0
    
    for i, e in enumerate(active):
        url = e.get("url", "")
        eid = e["id"]
        
        if not url:
            continue
        
        code, alive = check_url(url)
        
        # 记录检测结果
        if eid not in log:
            log[eid] = {"url": url, "checks": []}
        log[eid]["checks"].append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status_code": code,
            "alive": alive,
        })
        # 只保留最近 5 次检测
        log[eid]["checks"] = log[eid]["checks"][-5:]
        
        if not alive:
            dead_count += 1
            consecutive = sum(1 for c in reversed(log[eid]["checks"]) if not c["alive"])
            print(f"  ❌ [{consecutive}次] {url[:80]}")
            
            if consecutive >= 3:
                e["status"] = "archived"
                archived_count += 1
                print(f"     → 连续 3 次失效，标记为 archived")
        else:
            if len(log[eid]["checks"]) > 1 and not log[eid]["checks"][-2]["alive"]:
                print(f"  ✅ 已恢复: {url[:60]}")
        
        # 限速
        if (i + 1) % 20 == 0:
            print(f"  💤 速率控制: 等待 5s ({i+1}/{len(active)})")
            time.sleep(5)
        elif not alive:
            time.sleep(1)
    
    # 保存
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    LINK_LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"\n✅ 完成: {dead_count} 条死链, {archived_count} 条归档")

if __name__ == "__main__":
    main()
