#!/usr/bin/env python3
"""
Morning Intake Pipeline - 2026-06-22
Process AI-related files from the past 24 hours
"""

import json
import re
import sys
from datetime import datetime, date
from pathlib import Path
import hashlib

# Add openclaw scripts to path
sys.path.append('openclaw/scripts')
from pipeline_utils import (
    append_entries, normalize_entry, 
    clean_text, normalize_url, normalize_date,
    normalize_tags, canonical_category,
    normalize_source_type, normalize_platform,
    generate_entry_id, has_cjk, has_readable_text,
    load_entries_data, save_entries_data
)

def extract_metadata_from_file(file_path):
    """Extract metadata from .md file headers and content"""
    content = file_path.read_text(encoding='utf-8')
    
    # Extract YAML frontmatter if exists
    yaml_metadata = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            # Simple YAML parsing for key-value pairs
            for line in yaml_content.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    yaml_metadata[key.lower()] = value
    
    # Extract title from first H1 heading or filename
    title = ""
    yaml_title = yaml_metadata.get('title') or yaml_metadata.get('标题')
    if yaml_title:
        title = yaml_title
    else:
        # Look for H1 heading
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
    
    if not title:
        # Use filename as fallback
        title = file_path.stem.replace('-', ' ').replace('_', ' ')
    
    # Extract URL from various sources
    url = None
    if 'url' in yaml_metadata:
        url = yaml_metadata['url']
    elif '原文链接' in yaml_metadata:
        url = yaml_metadata['原文链接']
    elif '链接' in yaml_metadata:
        url = yaml_metadata['链接']
    else:
        # Look for URLs in content
        url_matches = re.findall(r'https?://[^\s\)]+', content)
        if url_matches:
            url = url_matches[0]
    
    # Extract author
    author = yaml_metadata.get('author') or yaml_metadata.get('作者')
    
    # Extract original date
    original_date = None
    if 'date' in yaml_metadata:
        original_date = yaml_metadata['date']
    elif '日期' in yaml_metadata:
        original_date = yaml_metadata['日期']
    elif '发表时间' in yaml_metadata:
        original_date = yaml_metadata['发表时间']
    elif '发布时间' in yaml_metadata:
        original_date = yaml_metadata['发布时间']
    
    # Extract source platform from directory structure or metadata
    platform = 'manual'
    file_path_str = str(file_path)
    if 'X 文章' in file_path_str or 'Twitter' in file_path_str:
        platform = 'x'
    elif 'Cubox' in file_path_str:
        platform = 'cubox'
    elif '论文' in file_path_str or 'arxiv' in file_path_str:
        platform = 'arxiv'
    elif 'github' in file_path_str.lower():
        platform = 'github'
    elif 'youtube' in file_path_str.lower():
        platform = 'youtube'
    elif 'newsletter' in file_path_str.lower():
        platform = 'newsletter'
    
    return {
        'title': title,
        'url': url,
        'author': author,
        'original_date': original_date,
        'platform': platform,
        'yaml_metadata': yaml_metadata,
        'content': content
    }

def extract_summary_and_images(content, is_english=False):
    """Extract summary and images from content"""
    
    # Remove YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    
    # Clean content for summary extraction
    clean_content = re.sub(r'!\[.*?\]\([^)]*\)', '', content)  # Remove images
    clean_content = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', clean_content)  # Remove links but keep text
    clean_content = re.sub(r'#{1,6}\s+', '', clean_content)  # Remove headings
    clean_content = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean_content)  # Remove bold
    clean_content = re.sub(r'`([^`]+)`', r'\1', clean_content)  # Remove code
    clean_content = re.sub(r'>\s*', '', clean_content)  # Remove blockquotes
    
    # Split into sentences for summary extraction
    sentences = re.split(r'(?<=[。！？.!?])\s*', clean_content)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 10]
    
    # Generate summary (100-300 characters)
    summary_zh = ""
    summary_en = None
    
    if is_english:
        # For English content, provide English summary
        summary_en = clean_text(clean_content[:500], max_len=300)
        summary_zh = f"{summary_en} (英文内容待翻译)"  # Placeholder for translation
    else:
        # For Chinese content, provide Chinese summary
        summary_zh = clean_text(clean_content[:500], max_len=300)
    
    return summary_zh, summary_en, images

def process_file(file_path, run_date):
    """Process a single AI-related file"""
    print(f"Processing {file_path}...")
    
    # Extract metadata
    metadata = extract_metadata_from_file(file_path)
    
    # Determine if content is English
    content_text = metadata['content']
    is_english = not has_cjk(content_text)
    
    # Extract summary and images
    summary_zh, summary_en, images = extract_summary_and_images(content_text, is_english)
    
    # Determine source type
    source_type = normalize_source_type('article')
    if metadata['platform'] == 'x':
        source_type = 'x_post'
    elif 'github' in str(file_path).lower():
        source_type = 'github'
    elif 'arxiv' in str(file_path).lower():
        source_type = 'paper'
    
    # Create entry
    entry = {
        'title': metadata['title'],
        'url': normalize_url(metadata['url']),
        'source': {
            'platform': normalize_platform(metadata['platform'], url=metadata['url']),
            'author': metadata['author'],
            'original_date': normalize_date(metadata['original_date'], run_date=run_date)
        },
        'category': 'uncategorized',  # Will be normalized later
        'tags': normalize_tags(metadata['yaml_metadata'].get('tags', [])),
        'source_type': source_type,
        'language': 'both' if is_english and summary_zh else 'zh',
        'summary_zh': summary_zh if summary_zh else "内容过短，待补充",
        'summary_en': summary_en,
        'one_liner': f"{metadata['title']} - 待补充详细点评",
        'one_liner_author': 'openclaw',
        'quality_score': 3,  # Default score, will be adjusted
        'status': 'score-pending',
        'local_path': str(file_path).replace('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/', ''),
        'images': images,
        'added_date': run_date.isoformat(),
        'updated_date': run_date.isoformat(),
        'github_stars': None,
        'related': []
    }
    
    # Normalize the entry
    normalized_entry = normalize_entry(entry, run_date=run_date)
    
    # Create content file
    content_dir = Path('content')
    content_dir.mkdir(exist_ok=True)
    content_file_path = content_dir / f"{normalized_entry['id']}.md"
    
    # Write content to file
    with open(content_file_path, 'w', encoding='utf-8') as f:
        f.write(metadata['content'])
    
    print(f"Created content file: {content_file_path}")
    return normalized_entry

def find_ai_files_in_obsidian(root_path, days=1):
    """Find AI-related files modified in the last N days"""
    root = Path(root_path)
    ai_files = []
    
    # Search for .md files in the Obsidian vault
    for md_file in root.rglob("*.md"):
        try:
            # Check if file was modified in the last N days
            stat = md_file.stat()
            file_date = datetime.fromtimestamp(stat.st_mtime).date()
            days_ago = (date.today() - file_date).days
            
            if days_ago <= days:
                # Check if file is AI-related
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                if is_ai_content(content):
                    ai_files.append(md_file)
                    
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
    
    return ai_files

def is_ai_content(content):
    """Check if content is AI-related"""
    ai_keywords = [
        'AI', 'artificial intelligence', '机器', '智能', '大模型', '语言模型',
        'Claude', 'GPT', 'OpenAI', 'Anthropic', 'transformer', 'neural',
        'deep learning', 'machine learning', 'LLM', 'agent', '智能体',
        'prompt', '提示词', 'multimodal', '多模态'
    ]
    
    content_lower = content.lower()
    return any(keyword.lower() in content_lower for keyword in ai_keywords)

def main():
    """Main intake pipeline"""
    print("=== Morning Intake Pipeline - 2026-06-22 ===")
    
    # Set run date
    run_date = date.today()
    print(f"Run date: {run_date}")
    
    # Find AI-related files from past 24 hours
    obsidian_root = "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian"
    ai_files = find_ai_files_in_obsidian(obsidian_root, days=1)
    
    print(f"Found {len(ai_files)} AI-related files:")
    for file in ai_files:
        print(f"  - {file}")
    
    if not ai_files:
        print("No AI-related files found in the past 24 hours")
        return
    
    # Process files (limit to 20 as per task requirements)
    processed_entries = []
    for i, file_path in enumerate(ai_files[:20]):
        try:
            entry = process_file(file_path, run_date)
            processed_entries.append(entry)
            print(f"✓ Processed {i+1}/{len(ai_files[:20])}: {entry['title']}")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")
            continue
    
    if not processed_entries:
        print("No entries were successfully processed")
        return
    
    print(f"\nProcessed {len(processed_entries)} entries")
    
    # Load existing entries data
    try:
        entries_data = load_entries_data()
    except Exception as e:
        print(f"Error loading existing entries: {e}")
        entries_data = {"entries": [], "last_updated": run_date.isoformat(), "total_entries": 0}
    
    # Add new entries using pipeline_utils
    added, skipped = append_entries(entries_data, processed_entries)
    
    print(f"\nResults:")
    print(f"  - Added: {len(added)} entries")
    print(f"  - Skipped: {len(skipped)} entries")
    
    if skipped:
        print("\nSkipped entries:")
        for entry, reason in skipped:
            print(f"  - {entry['title']} ({reason})")
    
    # Save entries data
    save_entries_data(entries_data)
    print(f"\n✓ Updated entries.json with {len(entries_data['entries'])} total entries")
    
    # Run site generation
    print("\n=== Generating site ===")
    try:
        subprocess.run(["python3", "openclaw/scripts/generate-site.py"], check=True)
        if result == 0:
            print("✓ Site generation completed successfully")
        else:
            print(f"✗ Site generation failed with exit code: {result}")
    except Exception as e:
        print(f"✗ Error running site generation: {e}")

if __name__ == "__main__":
    main()
