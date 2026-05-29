#!/usr/bin/env python3
"""
Process newly modified AI-related .md files and add them to entries.json
Following the awesome-ai-field-notes daily intake workflow
"""

import json
import re
import os
import sys
from pathlib import Path
from datetime import datetime, date
from urllib.parse import urlparse
import hashlib

# Add the openclaw/scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent / "openclaw" / "scripts"))
from pipeline_utils import (
    load_entries_data, save_entries_data, append_entries, normalize_entry,
    normalize_url, clean_text, generate_entry_id, normalize_date,
    markdown_to_text, has_cjk, is_placeholder_text, has_readable_text
)


def extract_metadata(content):
    """Extract metadata from markdown headers"""
    metadata = {}
    
    # Check for YAML frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            content = parts[2]
            # Parse simple key-value pairs from YAML
            for line in yaml_content.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    metadata[key] = value
    
    # Extract common metadata patterns
    patterns = {
        '来源': r'[-\s]*来源[:：]\s*(.+)',
        '原文链接': r'[-\s]*原文链接[:：]\s*(.+)',
        '链接': r'[-\s]*链接[:：]\s*(.+)',
        '作者': r'[-\s]*作者[:：]\s*(.+)',
        '日期': r'[-\s]*日期[:：]\s*(.+)',
        '发表时间': r'[-\s]*发表时间[:：]\s*(.+)',
        '抓取时间': r'[-\s]*抓取时间[:：]\s*(.+)',
        '标题': r'[-\s]*标题[:：]\s*(.+)',
        '平台': r'[-\s]*平台[:：]\s*(.+)',
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            metadata[key] = match.group(1).strip()
    
    return metadata, content


def extract_summary(content, min_length=100, max_length=300):
    """Extract summary from content"""
    # Remove markdown links and images, keep text
    text = markdown_to_text(content)
    
    # Try to extract meaningful sentences
    sentences = re.split(r'[。！？.!?]\s*', text)
    
    # Look for meaningful content (not too short, not metadata-like)
    meaningful_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if (len(sentence) >= 20 and 
            not is_placeholder_text(sentence) and
            not any(keyword in sentence.lower() for keyword in ['来源', '链接', '作者', '日期', '标签'])):
            meaningful_sentences.append(sentence)
    
    if meaningful_sentences:
        summary = '。'.join(meaningful_sentences[:3])
        if len(summary) > max_length:
            summary = summary[:max_length] + '...'
    else:
        # Fallback to first non-placeholder part
        paragraphs = text.split('\n\n')
        for para in paragraphs:
            para = para.strip()
            if len(para) >= min_length and not is_placeholder_text(para):
                summary = para[:max_length] + '...'
                break
        else:
            summary = text[:max_length] + '...' if text else "内容过短，待补充"
    
    return summary


def extract_images(content):
    """Extract image URLs from markdown content"""
    image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    return [normalize_url(img) for img in images if normalize_url(img)]


def determine_platform(metadata, content, url=None):
    """Determine platform from metadata and content"""
    if '平台' in metadata:
        platform = metadata['平台'].lower()
        return platform
    
    # Check content for platform indicators
    content_lower = content.lower()
    
    if 'twitter' in content_lower or 'x.com' in content_lower or 'x文章' in content_lower:
        return 'x'
    elif 'arxiv' in content_lower or 'arxiv.org' in content_lower:
        return 'arxiv'
    elif 'github' in content_lower:
        return 'github'
    elif 'medium' in content_lower or '博客' in content_lower:
        return 'blog'
    elif 'newsletter' in content_lower:
        return 'newsletter'
    elif 'youtube' in content_lower:
        return 'youtube'
    
    # Use URL if available
    if url:
        url_lower = url.lower()
        if 'twitter.com' in url_lower or 'x.com' in url_lower:
            return 'x'
        elif 'arxiv.org' in url_lower:
            return 'arxiv'
        elif 'github.com' in url_lower:
            return 'github'
        elif 'medium.com' in url_lower:
            return 'blog'
        elif 'youtube.com' in url_lower:
            return 'youtube'
    
    # Check directory structure (for file processing)
    return 'manual'


def determine_source_type(platform, content):
    """Determine source type based on platform and content"""
    if platform == 'x':
        return 'x_post'
    elif platform == 'arxiv':
        return 'paper'
    elif platform == 'github':
        return 'product'
    elif platform == 'manual':
        # Check content type
        if '论文精读' in content or 'arxiv' in content.lower():
            return 'paper'
        else:
            return 'article'
    else:
        return 'article'


def extract_ai_content(ai_files):
    """Extract content from AI-related files"""
    entries = []
    obsidian_root = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian")
    
    for file_path in ai_files:
        try:
            print(f"Processing: {file_path}")
            
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata
            metadata, clean_content = extract_metadata(content)
            
            # Generate entry ID
            entry_id = generate_entry_id(
                title=metadata.get('标题', ''),
                url=metadata.get('原文链接', '')
            )
            
            # Extract summary
            summary_zh = extract_summary(clean_content)
            
            # Determine platform and source type
            platform = determine_platform(
                metadata, 
                clean_content, 
                metadata.get('原文链接')
            )
            source_type = determine_source_type(platform, clean_content)
            
            # Extract images
            images = extract_images(clean_content)
            
            # Determine language
            has_chinese = has_cjk(summary_zh)
            language = 'both' if has_cjk(clean_content) else 'zh'
            
            # Create entry
            entry = {
                'id': entry_id,
                'title': metadata.get('标题', clean_content.split('\n')[0].replace('#', '').strip()),
                'url': normalize_url(metadata.get('原文链接')),
                'source': {
                    'platform': platform,
                    'author': clean_text(metadata.get('作者')) or None,
                    'original_date': normalize_date(metadata.get('日期') or metadata.get('发表时间')),
                },
                'category': 'uncategorized',  # Will be normalized by pipeline_utils
                'tags': [],
                'source_type': source_type,
                'language': language,
                'summary_zh': summary_zh,
                'summary_en': None,  # Will be handled if English content found
                'one_liner': "待补充可读摘要后再发布",
                'one_liner_author': 'openclaw',
                'quality_score': 3,  # Default, will be adjusted
                'status': 'active',
                'local_path': str(Path(file_path).relative_to(obsidian_root)),
                'images': images,
                'added_date': date.today().isoformat(),
                'updated_date': date.today().isoformat(),
                'github_stars': None,
                'related': [],
            }
            
            entries.append(entry)
            print(f"  - Entry ID: {entry_id}")
            print(f"  - Title: {entry['title']}")
            print(f"  - Platform: {platform}")
            print(f"  - Source Type: {source_type}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    return entries


def main():
    # Find recently modified AI-related files (last 24 hours)
    obsidian_root = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian")
    
    # Get all files modified in last 24 hours
    cmd = f'find "{obsidian_root}" -name "*.md" -type f -mtime -1'
    result = os.popen(cmd).read().strip().split('\n')
    
    # Filter for AI-related content
    ai_files = []
    for file_path in result:
        if not file_path:
            continue
        
        # Check if it's in the awesome-ai-field-notes repo
        if 'awesome-ai-field-notes' in file_path:
            continue
            
        # Skip certain directories that are not AI-related
        skip_dirs = ['Android-Internal-Wiki', 'OpenClaw定时任务']
        if any(skip_dir in file_path for skip_dir in skip_dirs):
            continue
            
        # Check file content for AI keywords
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # AI keywords
                ai_keywords = ['ai', 'artificial', 'intelligence', 'machine', 'learning', 'neural', 'model', 'agent', 'gpt', 'claude', 'gemini', '智能', '人工智能', '大模型']
                content_lower = content.lower()
                
                if any(keyword in content_lower for keyword in ai_keywords):
                    ai_files.append(file_path)
        except Exception as e:
            print(f"Could not read {file_path}: {e}")
            continue
    
    print(f"Found {len(ai_files)} AI-related files to process:")
    for file_path in ai_files:
        print(f"  - {file_path}")
    
    if not ai_files:
        print("No new AI-related files found")
        return
    
    # Extract content from files
    entries = extract_ai_content(ai_files)
    print(f"\nExtracted {len(entries)} entries from files")
    
    if not entries:
        print("No entries could be extracted")
        return
    
    # Load existing entries
    try:
        existing_data = load_entries_data()
        print(f"Loaded existing data with {existing_data['total_entries']} entries")
    except Exception as e:
        print(f"Error loading existing entries: {e}")
        existing_data = {"entries": [], "last_updated": "", "total_entries": 0}
    
    # Use pipeline_utils to append entries (normalization, deduplication)
    added, skipped = append_entries(existing_data, entries)
    
    print(f"\nProcessing results:")
    print(f"  - Added: {len(added)} entries")
    print(f"  - Skipped: {len(skipped)} entries")
    
    if skipped:
        print("  Skipped entries:")
        for entry, reason in skipped:
            print(f"    - {entry.get('title', 'Unknown')}: {reason}")
    
    if added:
        print("  Added entries:")
        for entry in added:
            print(f"    - {entry['title']} ({entry['source']['platform']})")
        
        # Save the updated data
        save_entries_data(existing_data)
        print(f"\nSaved {existing_data['total_entries']} total entries to entries.json")
        
        # Save content files
        content_dir = Path.cwd() / "content"
        content_dir.mkdir(exist_ok=True)
        
        for entry in added:
            content_file = content_dir / f"{entry['id']}.md"
            # The original file is the one we processed
            original_file = file_path
            
            if original_file:
                with open(original_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                with open(content_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  - Saved content to {content_file}")
        
        return True
    else:
        print("No entries were added")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)