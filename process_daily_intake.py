#!/usr/bin/env python3
"""Daily intake task for awesome-ai-field-notes"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta, date
import hashlib

# Add the scripts directory to the path
sys.path.append('./openclaw/scripts')
from pipeline_utils import (
    load_entries_data, save_entries_data, append_entries, normalize_entry,
    normalize_url, clean_text, generate_entry_id, normalize_platform,
    normalize_date, normalize_tags, canonical_category, normalize_source_type
)

def extract_metadata_from_file(file_path: Path) -> dict:
    """Extract metadata and content from markdown files"""
    content = file_path.read_text(encoding='utf-8')
    
    metadata = {}
    lines = content.split('\n')
    
    # Extract metadata from header
    for line in lines:
        line = line.strip()
        if line.startswith('> **Source:**'):
            metadata['url'] = line.replace('> **Source:**', '').strip()
        elif line.startswith('> **Author:**'):
            metadata['author'] = line.replace('> **Author:**', '').strip().replace('@', '')
        elif line.startswith('> **Platform:**'):
            metadata['platform'] = line.replace('> **Platform:**', '').strip()
        elif line.startswith('> **Original Date:**'):
            metadata['original_date'] = line.replace('> **Original Date:**', '').strip()
        elif line.startswith('> **Quality Score:**'):
            metadata['quality_score'] = int(line.replace('> **Quality Score:**', '').strip())
        elif line.startswith('> **Fetched:**'):
            metadata['fetched_date'] = line.replace('> **Fetched:**', '').strip()
    
    # Extract title
    title_match = re.match(r'# (.+)', content.split('\n')[0])
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # Extract summaries
    sections = content.split('---')
    if len(sections) > 1:
        content_section = sections[1]
        
        # Extract English summary
        english_match = re.search(r'## English\n(.+?)(?=##|\Z)', content_section, re.DOTALL)
        if english_match:
            metadata['summary_en'] = english_match.group(1).strip()
        
        # Extract Chinese summary  
        chinese_match = re.search(r'## 中文\n(.+?)(?=##|\Z)', content_section, re.DOTALL)
        if chinese_match:
            metadata['summary_zh'] = chinese_match.group(1).strip()
    
    # Extract one-liner
    one_liner_match = re.search(r'一句话总结：(.+)', content)
    if one_liner_match:
        metadata['one_liner'] = one_liner_match.group(1).strip()
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    metadata['images'] = images
    
    # Set default values
    metadata.setdefault('source_type', 'x_post')
    metadata.setdefault('language', 'both')
    metadata.setdefault('tags', ['ai-content'])
    metadata.setdefault('status', 'score-pending')
    metadata.setdefault('local_path', str(file_path.relative_to(Path('./content'))))
    
    return metadata

def process_recent_files():
    """Process recently modified files and append to entries.json"""
    # Load existing entries
    entries_data = load_entries_data()
    
    # Find recent content files (last 24 hours)
    content_dir = Path('./content')
    recent_files = []
    cutoff_time = datetime.now() - timedelta(hours=24)
    
    for file_path in content_dir.glob('*.md'):
        file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        if file_mtime > cutoff_time:
            recent_files.append(file_path)
    
    print(f"Found {len(recent_files)} recent files to process")
    
    # Process each file
    raw_entries = []
    for file_path in recent_files:
        print(f"Processing {file_path.name}")
        metadata = extract_metadata_from_file(file_path)
        
        # Normalize the entry
        normalized_entry = normalize_entry(metadata, run_date=date.today())
        raw_entries.append(normalized_entry)
    
    # Append entries to the data
    added, skipped = append_entries(entries_data, raw_entries)
    
    print(f"Added {len(added)} entries, skipped {len(skipped)}")
    
    # Save the updated entries
    save_entries_data(entries_data)
    
    return added, skipped

def validate_and_build():
    """Validate schema and build the site"""
    print("Validating schema...")
    result = exec_python("python3 scripts/validate-schema.py")
    if result != 0:
        print("Schema validation failed!")
        return False
    
    print("Building site...")
    result = exec_python("npm run build")
    if result != 0:
        print("Site build failed!")
        return False
    
    return True

def commit_changes():
    """Commit changes to git"""
    print("Adding files to git...")
    exec_git("git add -A")
    
    print("Committing changes...")
    commit_date = datetime.now().strftime("%Y-%m-%d")
    commit_message = f"[openclaw] intake: daily — {commit_date} update"
    exec_git(f'git commit -m "{commit_message}"')
    
    print("Pushing to remote...")
    exec_git("git push origin main")

def exec_python(command):
    """Execute a python command and return the result"""
    result = exec(command)
    return result

def exec_git(command):
    """Execute a git command"""
    exec(command)

def main():
    """Main execution function"""
    print("Starting awesome-ai-field-notes daily intake task...")
    print(f"Current time: {datetime.now()}")
    
    # Phase 1: Process recent files
    added, skipped = process_recent_files()
    
    if not added:
        print("No new entries added. Task completed.")
        return
    
    # Phase 2: Validate and build site
    if not validate_and_build():
        print("Validation/build failed. Aborting commit.")
        return
    
    # Phase 3: Commit changes
    commit_changes()
    
    # Generate summary
    summary = f"""
📊 AAIF 每日入库任务完成 - {datetime.now().strftime('%Y-%m-%d %H:%M')}

✅ 新增条目: {len(added)}
⏭️  跳过条目: {len(skipped)}

新增内容:
"""
    for entry in added:
        summary += f"• {entry['title']} ({entry.get('url', 'no url')})\n"
    
    print(summary)
    
    # TODO: Send summary to OpenClaw - 知识库 group
    # This would use the message tool

if __name__ == "__main__":
    main()