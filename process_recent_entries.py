#!/usr/bin/env python3
"""Process recent AI-related entries from Obsidian content."""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, date
import sys
sys.path.append(str(Path(__file__).parent / "openclaw" / "scripts"))

from pipeline_utils import (
    append_entries, normalize_entry, clean_text, normalize_url,
    today_str, markdown_to_text
)

def extract_metadata(file_content: str) -> dict:
    """Extract metadata from file content."""
    metadata = {}
    
    # Extract URL
    url_match = re.search(r'\*\*URL:\*\*\s*(https?://[^\s]+)', file_content)
    if url_match:
        metadata['url'] = normalize_url(url_match.group(1))
    
    # Extract source and author
    source_match = re.search(r'\*\*Source:\*\*\s*(.+)', file_content)
    if source_match:
        source_text = source_match.group(1).strip()
        if ' | ' in source_text:
            parts = source_text.split(' | ')
            metadata['author'] = parts[0].strip()
            metadata['platform'] = parts[1].strip() if len(parts) > 1 else None
        else:
            metadata['author'] = source_text
            metadata['platform'] = None
    
    # Extract date
    date_patterns = [
        r'\*\*Date:\*\*\s*(.+)',
        r'\*\*Published:\*\*\s*(.+)',
        r'\*\*发布日期：\*\*\s*(.+)'
    ]
    for pattern in date_patterns:
        date_match = re.search(pattern, file_content)
        if date_match:
            metadata['original_date'] = date_match.group(1).strip()
            break
    
    # Extract title from first heading
    title_match = re.search(r'^#\s+(.+)$', file_content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', file_content)
    metadata['images'] = images
    
    return metadata

def extract_sections(file_content: str) -> dict:
    """Extract English and Chinese sections."""
    sections = {'english': '', 'chinese': ''}
    
    # Split by language headers
    parts = re.split(r'^## (English|中文)$', file_content, flags=re.MULTILINE)
    
    if len(parts) >= 3:
        if parts[1].strip() == 'English':
            sections['english'] = parts[2].strip()
        if len(parts) >= 5 and parts[3].strip() == '中文':
            sections['chinese'] = parts[4].strip()
    else:
        # Fallback: split by language keywords
        english_pattern = r'(?i)(?:english|en)\s*\n(#\s+.+|$)'
        chinese_pattern = r'(?:中文|chinese)\s*\n(#\s+.+|$)'
        
        english_match = re.search(english_pattern, file_content)
        chinese_match = re.search(chinese_pattern, file_content)
        
        if english_match:
            sections['english'] = file_content[english_match.start():].split('\n#', 1)[0]
        if chinese_match:
            sections['chinese'] = file_content[chinese_match.start():].split('\n#', 1)[0]
    
    return sections

def generate_summaries(sections: dict, metadata: dict) -> dict:
    """Generate summaries for both languages."""
    summaries = {}
    
    # Chinese summary
    if sections['chinese']:
        # Remove metadata section
        content = re.sub(r'^#\s+.+?\n', '', sections['chinese'], count=1, flags=re.MULTILINE)
        content = re.sub(r'\*\*[^*]+\*\*\s*', '', content)  # Remove bold metadata
        summaries['summary_zh'] = clean_text(content, max_len=300)
    
    # English summary
    if sections['english']:
        content = re.sub(r'^#\s+.+?\n', '', sections['english'], count=1, flags=re.MULTILINE)
        content = re.sub(r'\*\*[^*]+\*\*\s*', '', content)  # Remove bold metadata
        summaries['summary_en'] = clean_text(content, max_len=300)
    
    return summaries

def detect_category_and_tags(content: str, metadata: dict) -> tuple[str, list[str]]:
    """Detect category and generate tags."""
    # Simple keyword-based detection
    content_lower = content.lower()
    
    # Category detection
    if any(keyword in content_lower for keyword in ['claude code', 'codex', 'cursor', 'copilot']):
        category = 'coding'
    elif any(keyword in content_lower for keyword in ['agent', 'harness', 'mcp', 'tool calling']):
        category = 'agents'
    elif any(keyword in content_lower for keyword in ['model', 'llm', 'gpt', 'gemini', 'qwen']):
        category = 'models'
    elif any(keyword in content_lower for keyword in ['rag', 'inference', 'benchmark', 'chip']):
        category = 'infra'
    elif any(keyword in content_lower for keyword in ['product', 'business', 'market', 'startup']):
        category = 'industry'
    elif any(keyword in content_lower for keyword in ['paper', 'research', 'arxiv', 'course']):
        category = 'learning'
    else:
        category = 'uncategorized'
    
    # Generate tags
    tags = []
    tag_keywords = {
        'ai': ['ai', 'artificial intelligence'],
        'research': ['research', 'paper', 'study'],
        'engineering': ['engineering', 'system', 'architecture'],
        'safety': ['safety', 'alignment', 'security'],
        'multimodal': ['multimodal', 'vision', 'audio'],
        'opensource': ['open source', 'github', 'opensource'],
    }
    
    for tag, keywords in tag_keywords.items():
        if any(keyword in content_lower for keyword in keywords):
            tags.append(tag)
    
    # Add platform-based tags
    if metadata.get('platform'):
        tags.append(metadata['platform'].lower())
    
    # Limit tags
    tags = tags[:6]
    
    return category, tags

def process_file(file_path: Path) -> dict:
    """Process a single file and return normalized entry."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    
    # Extract metadata
    metadata = extract_metadata(content)
    
    # Extract sections
    sections = extract_sections(content)
    
    # Generate summaries
    summaries = generate_summaries(sections, metadata)
    
    # Detect category and tags
    content_for_analysis = sections['english'] + sections['chinese']
    category, tags = detect_category_and_tags(content_for_analysis, metadata)
    
    # Determine source type
    if metadata.get('url') and 'github.com' in metadata['url']:
        source_type = 'github'
    elif metadata.get('url') and ('arxiv.org' in metadata['url'] or 'paper' in metadata['title'].lower()):
        source_type = 'paper'
    elif metadata.get('url') and ('twitter.com' in metadata['url'] or 'x.com' in metadata['url']):
        source_type = 'x_post'
    else:
        source_type = 'article'
    
    # Determine language
    has_cjk = re.search(r'[\u4e00-\u9fff]', content) is not None
    language = 'both' if (sections['english'] and sections['chinese']) else ('zh' if has_cjk else 'en')
    
    # Create raw entry
    raw_entry = {
        'title': metadata.get('title', file_path.stem),
        'url': metadata.get('url'),
        'source': {
            'platform': metadata.get('platform'),
            'author': metadata.get('author'),
            'original_date': metadata.get('original_date'),
        },
        'category': category,
        'tags': tags,
        'source_type': source_type,
        'language': language,
        'summary_zh': summaries.get('summary_zh'),
        'summary_en': summaries.get('summary_en'),
        'local_path': str(file_path.relative_to(Path.cwd())),
        'images': metadata.get('images', []),
        'quality_score': 3,  # Default score
        'status': 'score-pending',
    }
    
    # Normalize the entry
    normalized = normalize_entry(raw_entry)
    
    return normalized

def main():
    """Main processing function."""
    obsidian_root = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes")
    content_dir = obsidian_root / "content"
    
    # Load existing entries
    entries_file = obsidian_root / "data" / "entries.json"
    existing_data = json.loads(entries_file.read_text(encoding='utf-8'))
    
    # Find recent files
    recent_files = []
    for file_path in content_dir.glob("*.md"):
        if file_path.stat().st_mtime > (datetime.now().timestamp() - 86400):  # Last 24 hours
            recent_files.append(file_path)
    
    print(f"Found {len(recent_files)} recent files to process")
    
    # Process files
    new_entries = []
    for file_path in recent_files:
        print(f"Processing: {file_path.name}")
        entry = process_file(file_path)
        if entry:
            new_entries.append(entry)
    
    print(f"Generated {len(new_entries)} new entries")
    
    # Add to existing entries
    if new_entries:
        added, skipped = append_entries(existing_data, new_entries)
        
        print(f"Added {len(added)} new entries")
        print(f"Skipped {len(skipped)} duplicate entries")
        
        # Save updated entries
        from pipeline_utils import save_entries_data
        save_entries_data(existing_data)
        
        # Show summary
        print("\nSummary of added entries:")
        for entry in added:
            print(f"- {entry['title']} ({entry['category']})")
        
        return len(added)
    else:
        print("No new entries to add")
        return 0

if __name__ == "__main__":
    main()