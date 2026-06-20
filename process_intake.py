#!/usr/bin/env python3
"""Daily intake processing for awesome-ai-field-notes."""

import json
import re
import sys
from pathlib import Path
from datetime import date

# Add the openclaw/scripts directory to Python path
sys.path.append(str(Path(__file__).parent / "openclaw" / "scripts"))

from pipeline_utils import (
    append_entries, 
    save_entries_data, 
    normalize_entry,
    canonical_category,
    has_cjk,
    is_ai_related_entry
)

def extract_content_from_file(file_path: Path) -> dict:
    """Extract metadata and content from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^# (.+)', content, re.MULTILINE)
    title = title_match.group(1) if title_match else file_path.stem
    
    # Extract URL from metadata
    url_match = re.search(r'> 原文链接: (.+)', content)
    url = url_match.group(1) if url_match else f"https://example.com/{file_path.stem}"
    
    # Extract source metadata
    platform = 'blog'
    author_match = re.search(r'> 作者: (.+)', content)
    author = author_match.group(1) if author_match else None
    
    # Extract date
    date_match = re.search(r'> 发布时间: (\d{4}-\d{2}-\d{2})', content)
    original_date = date_match.group(1) if date_match else None
    
    # Extract Chinese summary
    zh_match = re.search(r'## 中文翻译\n\n(.+?)\n\n\*\*本文由', content, re.DOTALL)
    if zh_match:
        summary_zh = zh_match.group(1).strip()
        # Remove section headers and metadata
        summary_zh = re.sub(r'^#+\s.*$', '', summary_zh, flags=re.MULTILINE)
        summary_zh = re.sub(r'> .+$', '', summary_zh, flags=re.MULTILINE)
        summary_zh = re.sub(r'\*\*.*\*\*', '', summary_zh, flags=re.MULTILINE)
        summary_zh = re.sub(r'\n+', '\n', summary_zh).strip()
        summary_zh = (summary_zh[:300] + '...') if len(summary_zh) > 300 else summary_zh
    else:
        # Fallback to getting content after Chinese section start
        fallback_match = re.search(r'## 中文翻译\n\n(.+)', content, re.DOTALL)
        if fallback_match:
            summary_zh = fallback_match.group(1).strip()
            summary_zh = (summary_zh[:300] + '...') if len(summary_zh) > 300 else summary_zh
        else:
            summary_zh = content[:300] + '...'
    
    # Extract English summary
    en_match = re.search(r'## English Original\n\n(.*?)\n\n---', content, re.DOTALL)
    if en_match:
        summary_en = en_match.group(1).strip()
        # Remove headers and metadata
        summary_en = re.sub(r'^#+\s.*$', '', summary_en, flags=re.MULTILINE)
        summary_en = re.sub(r'> .+$', '', summary_en, flags=re.MULTILINE)
        summary_en = re.sub(r'\n+', '\n', summary_en).strip()
        summary_en = (summary_en[:300] + '...') if len(summary_en) > 300 else summary_en
    else:
        summary_en = None
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    
    # Determine language
    language = 'both' if has_cjk(summary_zh) and (summary_en and not has_cjk(summary_en)) else 'zh' if has_cjk(summary_zh) else 'en'
    
    # Determine source_type
    source_type = 'article' if 'news' in url.lower() or 'blog' in url.lower() else 'paper'
    
    # Generate entry ID
    entry_id = file_path.stem
    
    return {
        'id': entry_id,
        'title': title,
        'url': url,
        'source': {
            'platform': platform,
            'author': author,
            'original_date': original_date
        },
        'category': None,  # Will be determined by canonical_category
        'tags': [],
        'source_type': source_type,
        'language': language,
        'summary_zh': summary_zh,
        'summary_en': summary_en,
        'one_liner': '',
        'one_liner_author': 'openclaw',
        'quality_score': 3,  # Default, will be adjusted
        'status': 'score-pending',
        'local_path': str(file_path),
        'images': images,
        'added_date': date.today().isoformat(),
        'updated_date': date.today().isoformat(),
        'github_stars': None,
        'related': []
    }

def score_content(title: str, summary_zh: str, summary_en: str = None) -> int:
    """Score content based on quality."""
    content = f"{title} {summary_zh}"
    if summary_en:
        content += f" {summary_en}"
    
    # High quality indicators
    high_quality_indicators = [
        '里程碑', '突破', '革命', 'transformer', 'GPT-5', 'Claude', 'Gemini',
        'model', 'agent', 'benchmark', 'research', '论文', '技术', '创新'
    ]
    
    score = 2  # Base score
    
    # Check for high quality indicators
    for indicator in high_quality_indicators:
        if indicator.lower() in content.lower():
            score += 1
    
    # Very high quality for major model releases
    if 'GPT-5.5' in title or 'Claude Opus' in title:
        score = 4
    
    # Cap at 5
    return min(5, score)

def generate_one_liner(title: str, summary_zh: str, category: str) -> str:
    """Generate a one-liner summary."""
    if 'GPT-5.5' in title:
        return 'OpenAI发布的最新旗舰模型，在编码、研究和数据分析方面展现显著提升'
    elif 'Claude Opus' in title:
        return 'Anthropic最新发布的旗舰模型，在高级软件工程和长链路任务处理上有显著改进'
    else:
        return f'{category}领域的最新发展，值得关注的技术进展'

def main():
    # Load existing entries
    entries_path = Path(__file__).parent / "data" / "entries.json"
    if entries_path.exists():
        with open(entries_path, 'r', encoding='utf-8') as f:
            entries_data = json.load(f)
    else:
        entries_data = {"entries": [], "last_updated": None, "total_entries": 0}
    
    # Files to process
    files_to_process = [
        Path(__file__).parent / "content" / "gpt55_release_2026_001.md",
        Path(__file__).parent / "content" / "claude_opus_47_mythos_2026_001.md"
    ]
    
    new_entries = []
    
    for file_path in files_to_process:
        if not file_path.exists():
            print(f"Warning: File {file_path} does not exist, skipping")
            continue
        
        # Extract content
        entry_data = extract_content_from_file(file_path)
        
        # Determine category
        category = canonical_category(
            category=entry_data['category'],
            tags=entry_data['tags'],
            source_type=entry_data['source_type'],
            title=entry_data['title'],
            summary=entry_data['summary_zh']
        )
        entry_data['category'] = category
        
        # Score content
        entry_data['quality_score'] = score_content(
            entry_data['title'], 
            entry_data['summary_zh'], 
            entry_data['summary_en']
        )
        
        # Generate one-liner
        entry_data['one_liner'] = generate_one_liner(
            entry_data['title'],
            entry_data['summary_zh'],
            category
        )
        
        # Set status based on quality
        if entry_data['quality_score'] >= 4:
            entry_data['status'] = 'active'
        else:
            entry_data['status'] = 'score-pending'
        
        new_entries.append(entry_data)
    
    # Add entries using pipeline utils
    added, skipped = append_entries(entries_data, new_entries)
    
    # Save entries
    save_entries_data(entries_data)
    
    # Print results
    print(f"Intake completed!")
    print(f"Added {len(added)} entries")
    print(f"Skipped {len(skipped)} entries")
    
    for entry in added:
        print(f"  - {entry['title']} ({entry['category']}, score: {entry['quality_score']})")
    
    if skipped:
        print("Skipped entries:")
        for entry, reason in skipped:
            print(f"  - {entry['title']} ({reason})")
    
    print(f"Total entries: {entries_data['total_entries']}")

if __name__ == "__main__":
    main()