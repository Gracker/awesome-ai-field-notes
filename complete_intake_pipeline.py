#!/usr/bin/env python3
"""Complete daily intake pipeline for awesome-ai-field-notes"""

import json
import re
from datetime import datetime, date, timedelta
from pathlib import Path
import sys
import os
import time
import hashlib
import difflib

# Add the openclaw/scripts directory to Python path for pipeline_utils
script_dir = Path(__file__).parent / "openclaw/scripts"
sys.path.insert(0, str(script_dir))

from pipeline_utils import (
    load_entries_data, 
    save_entries_data, 
    append_entries, 
    normalize_entry,
    today_str,
    content_dir
)

def get_github_remote_count() -> int:
    """Get the current entry count from GitHub remote"""
    try:
        result = os.popen('cd "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes" && git ls-files data/entries.json | xargs -I {} git show HEAD:data/entries.json | jq -r ".total_entries" || echo "0"').read().strip()
        return int(result) if result.isdigit() else 0
    except Exception as e:
        print(f"Error getting GitHub count: {e}")
        return 0

def extract_content_from_file(file_path: Path) -> dict:
    """Extract structured content from a markdown file"""
    
    content = file_path.read_text(encoding='utf-8')
    
    # Extract title (first h1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "未命名 AI 资源"
    
    # Extract English and Chinese sections
    english_section = ""
    chinese_section = ""
    
    # Look for standard format: English title, then "英文原文", then "中文翻译"
    lines = content.split('\n')
    in_english = False
    in_chinese = False
    
    for line in lines:
        line = line.strip()
        if line == "英文原文":
            in_english = True
            in_chinese = False
            continue
        elif line == "中文翻译":
            in_chinese = True
            in_english = False
            continue
        elif line.startswith("#") and not line.startswith("##"):
            # Skip section headers
            continue
        
        if in_english:
            english_section += line + "\n"
        elif in_chinese:
            chinese_section += line + "\n"
    
    # Clean up sections
    english_section = english_section.strip()
    chinese_section = chinese_section.strip()
    
    # Generate summary (first 200 chars of English or Chinese)
    if english_section:
        summary = english_section[:200] + "..." if len(english_section) > 200 else english_section
    else:
        summary = chinese_section[:200] + "..." if len(chinese_section) > 200 else chinese_section
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    
    # Extract tags from content (look for common patterns)
    tags = []
    tag_patterns = [
        r'#[\w\u4e00-\u9fff]+',
        r'##[\w\u4e00-\u9fff]+',
        r'关键词[:：]\s*([^#\n]+)',
        r'tags[:：]\s*([^#\n]+)'
    ]
    
    for pattern in tag_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            # Clean up tag matches
            tag = re.sub(r'[^\w\u4e00-\u9fff]', '', match).strip()
            if tag and len(tag) > 1:
                tags.append(tag)
    
    # Remove duplicates and limit
    tags = list(dict.fromkeys(tags))[:8]
    
    # Determine source type based on title/content
    source_type = "article"
    if "anthropic" in title.lower():
        source_type = "paper"
    elif "github" in content.lower():
        source_type = "github"
    elif "twitter" in title.lower() or "x.com" in content.lower():
        source_type = "x_post"
    
    # Determine platform
    platform = "manual"
    if "anthropic" in title.lower() or "anthropic" in content.lower():
        platform = "anthropic"
    elif "github" in content.lower():
        platform = "github"
    elif "arxiv" in content.lower():
        platform = "arxiv"
    elif "twitter" in content.lower() or "x.com" in content.lower():
        platform = "x"
    
    return {
        "title": title,
        "summary_zh": chinese_section[:500] + "..." if len(chinese_section) > 500 else chinese_section,
        "summary_en": english_section[:500] + "..." if len(english_section) > 500 else english_section,
        "source": {
            "platform": platform,
            "author": None,  # Will be filled if needed
            "original_date": None
        },
        "source_type": source_type,
        "language": "both" if english_section and chinese_section else "zh",
        "tags": tags,
        "images": images,
        "local_path": str(file_path),
        "one_liner_author": "openclaw",
        "quality_score": 4,  # Default high quality for manually curated content
        "status": "active"
    }

def check_existing_entries_by_title(entries: list, new_title: str, threshold: float = 0.85) -> bool:
    """Check if title is similar to existing entries"""
    for entry in entries:
        existing_title = entry.get('title', '')
        similarity = difflib.SequenceMatcher(None, existing_title.lower(), new_title.lower()).ratio()
        if similarity >= threshold:
            print(f"Title similarity too high: '{new_title}' vs '{existing_title}' ({similarity:.2f})")
            return True
    return False

def validate_and_build():
    """Phase 5: Validate and build site"""
    print("=== Phase 5: Validate and Build ===")
    
    # Run schema validation
    print("Running schema validation...")
    try:
        result = os.system('cd "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes" && python3 scripts/validate-schema.py')
        if result != 0:
            print("Schema validation failed!")
            return False
        print("Schema validation passed")
    except Exception as e:
        print(f"Schema validation error: {e}")
        return False
    
    # Build site
    print("Building site...")
    try:
        result = os.system('cd "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes" && npm run build')
        if result != 0:
            print("Site build failed!")
            return False
        print("Site built successfully")
    except Exception as e:
        print(f"Site build error: {e}")
        return False
    
    return True

def git_push():
    """Git commit and push"""
    print("=== Git Commit and Push ===")
    
    # Check GitHub remote count first
    github_count = get_github_remote_count()
    print(f"GitHub remote entry count: {github_count}")
    
    # Load current entries to check count
    entries_data = load_entries_data()
    current_count = len(entries_data.get("entries", []))
    print(f"Current local entry count: {current_count}")
    
    # Safety check: ensure we don't push fewer entries than remote
    if current_count < github_count:
        print(f"❌ CRITICAL: Local count ({current_count}) < GitHub count ({github_count})")
        print("ERROR: Entry count decreased - pushing would cause data loss!")
        return False
    
    # Git add all changes
    print("Running git add -A...")
    result = os.system('cd "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes" && git add -A')
    if result != 0:
        print("Git add failed!")
        return False
    
    # Git commit
    commit_msg = f"[openclaw] intake: daily — {current_count - github_count} entries added (2026-05-24)"
    print(f"Running git commit: {commit_msg}")
    result = os.system(f'cd "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes" && git commit -m "{commit_msg}"')
    if result != 0:
        print("Git commit failed!")
        return False
    
    # Git push
    print("Running git push...")
    result = os.system('cd "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes" && git push origin main')
    if result != 0:
        print("Git push failed!")
        return False
    
    print("✅ Git operations completed successfully")
    return True

def main():
    """Execute complete daily intake pipeline"""
    print(f"🚀 Starting complete daily intake pipeline - {today_str()}")
    
    # Phase 1: Discover files
    print("=== Phase 1: Discovery ===")
    entries_data = load_entries_data()
    existing_count = len(entries_data.get("entries", []))
    print(f"Existing entries count: {existing_count}")
    
    # Find recent files in 24 hours
    content_dir_path = Path(__file__).parent / "content"
    recent_files = []
    
    print(f"Looking for files in: {content_dir_path}")
    for file_path in content_dir_path.glob("*.md"):
        stat = file_path.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        time_diff = (datetime.now() - mod_time).total_seconds()
        if time_diff < 86400:  # 24 hours
            recent_files.append(file_path)
            print(f"  Found recent file: {file_path.name} (modified {time_diff/3600:.1f} hours ago)")
        else:
            print(f"  Skipping old file: {file_path.name} (modified {time_diff/3600:.1f} hours ago)")
    
    print(f"Found {len(recent_files)} recent files to process")
    
    if not recent_files:
        print("No recent files to process")
        send_telegram_message("⚠️ No recent AI files found for intake")
        return
    
    # Phase 2: Extract and Phase 3: Process
    print("=== Phase 2-3: Extract and Process ===")
    new_entries = []
    processed_count = 0
    
    for file_path in recent_files:
        print(f"Processing: {file_path.name}")
        
        try:
            entry_data = extract_content_from_file(file_path)
            normalized_entry = normalize_entry(entry_data, run_date=date.today())
            
            # Check for exact title matches (to avoid complete duplicates)
            existing_titles = [entry.get('title', '') for entry in entries_data.get("entries", [])]
            if normalized_entry['title'] in existing_titles:
                print(f"  - Skipping exact duplicate: {normalized_entry['title']}")
                continue
            
            new_entries.append(normalized_entry)
            processed_count += 1
            print(f"  - Title: {normalized_entry['title']}")
            print(f"  - Category: {normalized_entry['category']}")
            print(f"  - Score: {normalized_entry['quality_score']}")
            
            # Copy content to content/ directory
            content_dir_path.mkdir(exist_ok=True)
            entry_id = normalized_entry['id']
            dest_file = content_dir_path / f"{entry_id}.md"
            source_content = file_path.read_text(encoding='utf-8')
            
            if not dest_file.exists():
                dest_file.write_text(source_content, encoding='utf-8')
                print(f"  - Copied content to: {dest_file.name}")
            else:
                print(f"  - Content already exists: {dest_file.name}")
            
        except Exception as e:
            print(f"  - Error processing {file_path.name}: {e}")
            continue
    
    if not new_entries:
        print("No valid entries to add")
        send_telegram_message("⚠️ Processed files but no valid entries added")
        return
    
    # Limit to max 20 entries per run
    if len(new_entries) > 20:
        print(f"Limiting entries to first 20 (total: {len(new_entries)})")
        new_entries = new_entries[:20]
    
    # Phase 4: Append entries
    print("=== Phase 4: Append Entries ===")
    try:
        added, skipped = append_entries(entries_data, new_entries)
        
        print(f"Added {len(added)} entries, skipped {len(skipped)}")
        
        # Save updated entries
        save_entries_data(entries_data)
        
        print(f"Total entries: {len(entries_data.get('entries', []))}")
        
        # Generate summary
        categories = {}
        for entry in added:
            cat = entry['category']
            categories[cat] = categories.get(cat, 0) + 1
        
        summary = {
            "date": today_str(),
            "processed_files": len(recent_files),
            "processed_entries": processed_count,
            "added_entries": len(added),
            "skipped_entries": len(skipped),
            "categories": categories,
            "total_entries": len(entries_data.get('entries', [])),
            "previous_count": existing_count,
            "github_count": get_github_remote_count()
        }
        
        print("Processing summary:")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        
    except Exception as e:
        print(f"Error appending entries: {e}")
        send_telegram_message(f"❌ Error adding entries: {e}")
        raise
    
    # Phase 5: Validate and Build
    if not validate_and_build():
        print("❌ Build validation failed")
        send_telegram_message("❌ Site build validation failed")
        return
    
    # Git operations
    if not git_push():
        print("❌ Git operations failed")
        send_telegram_message("❌ Git operations failed")
        return
    
    # Success - send notification
    success_msg = f"""
🎉 AAIF Daily Intake Completed - 2026-05-24

✅ Processed: {summary['processed_files']} files
✅ Added: {summary['added_entries']} new entries
📊 Categories: {', '.join([f"{k}({v})" for k, v in categories.items()])}
📈 Total: {summary['total_entries']} entries (+{summary['added_entries']})

🔧 Validation: ✅ Passed
🏗️ Build: ✅ Success  
📤 Push: ✅ Completed

GitHub: {summary['github_count']} → Local: {summary['total_entries']}
""".strip()
    
    send_telegram_message(success_msg)
    print("✅ Complete pipeline finished successfully")

def send_telegram_message(message: str):
    """Send notification to OpenClaw - EBook group"""
    try:
        # Try different import approaches
        import importlib.util
        
        # Look for message module in Python path
        try:
            from message import message as send_message
        except ImportError:
            try:
                # Try relative import
                import sys
                from pathlib import Path
                current_dir = Path(__file__).parent
                message_path = current_dir / "message.py"
                spec = importlib.util.spec_from_file_location("message", message_path)
                message_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(message_module)
                send_message = message_module.message
            except Exception:
                print(f"Cannot import message module: {e}")
                return
        
        # Use OpenClaw messaging to send to the group
        send_message(
            action="send",
            channel="OpenClaw - EBook",
            message=message
        )
        print("✅ Notification sent to OpenClaw - EBook group")
    except Exception as ex:
        print(f"Failed to send notification: {ex}")
        # Don't fail the pipeline if notification fails

if __name__ == "__main__":
    main()