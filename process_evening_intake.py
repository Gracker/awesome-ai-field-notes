#!/usr/bin/env python3
"""
Evening AI Field Notes Intake Script
Processes recent markdown files and adds them to entries.json
"""

import json
import re
import sys
from datetime import datetime, date
from pathlib import Path
import os

# Add the openclaw/scripts directory to path to import pipeline_utils
scripts_dir = Path(__file__).parent / "openclaw/scripts"
sys.path.insert(0, str(scripts_dir))

try:
    from pipeline_utils import (
        load_entries_data,
        save_entries_data,
        append_entries,
        normalize_entry,
        normalize_url,
        clean_text,
        today_str,
        has_cjk
    )
except ImportError as e:
    print(f"Error importing pipeline_utils: {e}")
    sys.exit(1)

def extract_metadata_from_file(file_path: Path) -> dict:
    """Extract metadata from markdown file header"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Find YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                metadata = {}
                
                # Parse simple key-value pairs
                for line in yaml_content.split('\n'):
                    line = line.strip()
                    if ':' in line and not line.startswith('#'):
                        key, value = line.split(':', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Remove quotes if present
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        
                        metadata[key] = value
                
                return metadata
        
        # If no YAML, try to extract from content
        lines = content.split('\n')
        metadata = {}
        for line in lines[:20]:  # Check first 20 lines
            line = line.strip()
            if line.startswith('- **') and ':' in line:
                # Format: - **Key**: value
                match = re.match(r'- \*\*([^:]+)\*\*:\s*(.+)', line)
                if match:
                    key, value = match.groups()
                    metadata[key] = value.strip()
            elif line.startswith('**') and ':' in line and line.endswith('**'):
                # Format: **Key**: value
                match = re.match(r'\*\*([^:]+)\*\*:\s*(.+)', line)
                if match:
                    key, value = match.groups()
                    metadata[key] = value.strip()
        
        return metadata
        
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
        return {}

def extract_content_from_file(file_path: Path) -> str:
    """Extract main content from markdown file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Remove YAML frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
        
        # Find Chinese content section
        chinese_section = ""
        english_section = ""
        
        lines = content.split('\n')
        in_chinese_section = False
        in_english_section = False
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('## 中文翻译'):
                in_chinese_section = True
                in_english_section = False
                continue
            elif line.startswith('## English Original'):
                in_chinese_section = False
                in_english_section = True
                continue
            
            if in_chinese_section and line:
                chinese_section += line + '\n'
            elif in_english_section and line:
                english_section += line + '\n'
        
        # If no clear sections, use content after metadata
        if not chinese_section and not english_section:
            content = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', content)  # Remove images
            content = re.sub(r'\[[^\]]*\]\([^)]*\)', '', content)  # Remove links
            chinese_section = content
        
        return chinese_section, english_section
        
    except Exception as e:
        print(f"Error extracting content from {file_path}: {e}")
        return "", ""

def create_entry_from_file(file_path: Path, run_date: date) -> dict:
    """Create an entry dict from a markdown file"""
    metadata = extract_metadata_from_file(file_path)
    chinese_content, english_content = extract_content_from_file(file_path)
    
    # Extract basic fields
    title = metadata.get('标题', metadata.get('title', 'Untitled'))
    url = normalize_url(metadata.get('原文链接', metadata.get('url', '')))
    author = metadata.get('作者', metadata.get('author', None))
    category = metadata.get('分类', metadata.get('category', None))
    tags_str = metadata.get('标签', metadata.get('tags', ''))
    source_type = metadata.get('来源类型', metadata.get('source_type', 'article'))
    # Handle quality score format (e.g., "4/5")
    quality_str = metadata.get('质量评分', metadata.get('quality_score', '3'))
    if isinstance(quality_str, str) and '/' in quality_str:
        try:
            quality_score = int(quality_str.split('/')[0])
        except (ValueError, IndexError):
            quality_score = 3
    else:
        try:
            quality_score = int(quality_str)
        except (ValueError, TypeError):
            quality_score = 3
    
    # Parse tags
    if isinstance(tags_str, str):
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
    else:
        tags = tags_str or []
    
    # Clean text
    title = clean_text(title, max_len=140)
    chinese_content = clean_text(chinese_content, max_len=2000)
    english_content = clean_text(english_content, max_len=2000) if english_content else None
    
    # Generate summaries (first 200 characters)
    summary_zh = chinese_content[:200] + '...' if len(chinese_content) > 200 else chinese_content
    summary_en = english_content[:200] + '...' if english_content and len(english_content) > 200 else english_content
    
    # Extract images
    images = []
    content = file_path.read_text(encoding='utf-8')
    image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    
    # Create entry
    entry = {
        'id': metadata.get('ID', file_path.stem),
        'title': title,
        'url': url,
        'source': {
            'platform': metadata.get('平台', metadata.get('platform', 'manual')),
            'author': author,
            'original_date': metadata.get('日期', metadata.get('original_date', None))
        },
        'category': category,
        'tags': tags,
        'source_type': source_type,
        'language': 'both' if english_content else 'zh',
        'summary_zh': summary_zh,
        'summary_en': summary_en,
        'one_liner': '',
        'one_liner_author': 'openclaw',
        'quality_score': max(1, min(5, quality_score)),
        'status': 'active',
        'local_path': str(file_path).replace('\\', '/'),
        'images': images,
        'added_date': today_str(),
        'updated_date': today_str(),
        'github_stars': None,
        'related': []
    }
    
    return entry

def find_recent_md_files() -> list[Path]:
    """Find markdown files modified in the last 24 hours"""
    from datetime import datetime, timedelta
    
    twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
    recent_files = []
    
    # Find .md files in content directory
    content_dir = Path('content')
    if content_dir.exists():
        for md_file in content_dir.glob('*.md'):
            try:
                if md_file.is_file():
                    mod_time = datetime.fromtimestamp(md_file.stat().st_mtime)
                    if mod_time >= twenty_four_hours_ago:
                        recent_files.append(md_file)
            except Exception as e:
                print(f"Error checking file {md_file}: {e}")
    
    # Also check web-articles directory
    web_articles_dir = Path('web-articles')
    if web_articles_dir.exists():
        for md_file in web_articles_dir.rglob('*.md'):
            try:
                if md_file.is_file():
                    mod_time = datetime.fromtimestamp(md_file.stat().st_mtime)
                    if mod_time >= twenty_four_hours_ago:
                        recent_files.append(md_file)
            except Exception as e:
                print(f"Error checking file {md_file}: {e}")
    
    return sorted(recent_files)

def main():
    """Main intake processing function"""
    print("Starting evening AI field notes intake...")
    
    # Load existing entries
    try:
        data = load_entries_data()
        original_count = len(data.get('entries', []))
        print(f"Loaded {original_count} existing entries")
    except Exception as e:
        print(f"Error loading entries: {e}")
        data = {'entries': [], 'last_updated': today_str(), 'total_entries': 0}
        original_count = 0
    
    # Find recent files
    recent_files = find_recent_md_files()
    print(f"Found {len(recent_files)} recent markdown files")
    
    if not recent_files:
        print("No recent files to process")
        return
    
    # Process files
    raw_entries = []
    for file_path in recent_files:
        print(f"Processing {file_path}...")
        try:
            entry = create_entry_from_file(file_path, date.today())
            raw_entries.append(entry)
            print(f"  Created entry: {entry['title']}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Add entries using pipeline utils
    if raw_entries:
        try:
            added, skipped = append_entries(data, raw_entries)
            new_count = len(data.get('entries', []))
            
            print(f"\nProcessing complete:")
            print(f"  Original entries: {original_count}")
            print(f"  Added entries: {len(added)}")
            print(f"  Skipped entries: {len(skipped)}")
            print(f"  Total entries: {new_count}")
            
            # Save entries
            save_entries_data(data)
            print("Entries saved to data/entries.json")
            
            # Save content files
            content_dir = Path('content')
            for entry in added:
                if 'local_path' in entry:
                    content_file = Path(entry['local_path'])
                    if content_file.exists():
                        # Copy content file to content/ with new ID
                        new_content_path = content_dir / f"{entry['id']}.md"
                        if not new_content_path.exists():
                            content_file.rename(new_content_path)
                            print(f"  Content saved to {new_content_path}")
            
            return True
            
        except Exception as e:
            print(f"Error adding entries: {e}")
            return False
    else:
        print("No valid entries to add")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)