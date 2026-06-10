#!/usr/bin/env python3
"""Daily intake task for awesome-ai-field-notes.

Extracts AI-related content from recent markdown files and adds to entries.json.
"""

import json
import re
import sys
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add the scripts directory to path
scripts_dir = Path(__file__).parent / "scripts"
sys.path.insert(0, str(scripts_dir))

try:
    from pipeline_utils import (
        append_entries,
        normalize_entry,
        entries_path,
        content_dir,
        validate_entries_data,
        normalize_url,
        clean_text,
        has_cjk,
        has_readable_text,
        generate_entry_id,
        normalize_date,
        load_entries_data,
        save_entries_data
    )
except ImportError:
    print("Error: Could not import pipeline_utils. Make sure you're running from the project root.")
    sys.exit(1)

def find_recent_ai_files(root_path: Path, days: int = 1) -> List[Path]:
    """Find AI-related markdown files modified within the last N days."""
    ai_keywords = [
        "AI", "artificial intelligence", "machine learning", "neural", 
        "transformer", "llm", "gpt", "claude", "gemini", "qwen", 
        "openai", "anthropic", "智能体", "大模型", "agents", "models",
        "coding", "framework", "harness", "codex", "cursor"
    ]
    
    # Define the main Obsidian vault directory (outside the project)
    obsidian_vault = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian")
    
    recent_files = []
    
    # Search in the main Obsidian vault, not in the project directory
    if obsidian_vault.exists():
        for md_file in obsidian_vault.rglob("*.md"):
            # Skip files in project directories
            if "awesome-ai-field-notes" in str(md_file):
                continue
                
            if (datetime.now() - datetime.fromtimestamp(md_file.stat().st_mtime)).days <= days:
                try:
                    content = md_file.read_text(encoding='utf-8', errors='ignore')
                    if any(keyword.lower() in content.lower() for keyword in ai_keywords):
                        recent_files.append(md_file)
                        print(f"Found AI file: {md_file}")
                except Exception as e:
                    print(f"Warning: Could not read {md_file}: {e}")
    
    return sorted(recent_files)

def extract_metadata_from_file(file_path: Path) -> Dict[str, Any]:
    """Extract metadata from a markdown file."""
    content = file_path.read_text(encoding='utf-8', errors='ignore')

    # Extract frontmatter if present
    frontmatter = {}
    content_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if content_match:
        frontmatter_str, main_content = content_match.groups()

        # Parse frontmatter YAML-like structure
        for line in frontmatter_str.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                frontmatter[key] = value
        content = main_content
    else:
        content = content

    # Handle special case for X文章 files with specific format
    if 'X 文章' in str(file_path) and ('来源:' in content or '**来源**' in content):
        # Parse the X文章 format
        title_match = re.search(r'#\s*(.+)', content)
        title = title_match.group(1).strip() if title_match else frontmatter.get('title', '')

        # Extract metadata from the specific format
        source_info = {}
        if '来源:' in content:
            source_match = re.search(r'来源:\s*([^\n]+)', content)
            source_info['platform'] = source_match.group(1).split('/')[0].strip() if source_match else 'unknown'
        elif '**来源**' in content:
            source_match = re.search(r'\*\*来源\*\*:\s*([^\n]+)', content)
            source_info['platform'] = source_match.group(1).split('/')[0].strip() if source_match else 'unknown'

        author_info = {}
        if '作者' in content:
            author_match = re.search(r'作者:\s*([^\n]+)', content)
            author_info['author'] = author_match.group(1).strip() if author_match else None
        elif '**作者**' in content:
            author_match = re.search(r'\*\*作者\*\*:\s*([^\n]+)', content)
            author_info['author'] = author_match.group(1).strip() if author_match else None

        url_info = {}
        if '原文链接' in content:
            url_match = re.search(r'原文链接:\s*([^\n\s]+)', content)
            url_info['url'] = url_match.group(1).strip() if url_match else None
        elif '**原文链接**' in content:
            url_match = re.search(r'\*\*原文链接\*\*:\s*([^\n\s]+)', content)
            url_info['url'] = url_match.group(1).strip() if url_match else None

        date_info = {}
        if '日期' in content:
            date_match = re.search(r'日期:\s*([^\n]+)', content)
            date_info['date'] = date_match.group(1).strip() if date_match else None
        elif '**日期**' in content:
            date_match = re.search(r'\*\*日期\*\*:\s*([^\n]+)', content)
            date_info['date'] = date_match.group(1).strip() if date_match else None

        # Use extracted info or fall back to frontmatter
        url = url_info.get('url') or frontmatter.get('url', '')
        author = author_info.get('author') or frontmatter.get('author', '')
        raw_date = date_info.get('date') or frontmatter.get('date', '')

        # Extract summary from main content (skip metadata section)
        content_lines = content.split('\n')
        summary_lines = []
        in_content = False

        for line in content_lines:
            line = line.strip()
            if line.startswith('#') or '来源:' in line or '**来源**' in line or '作者:' in line or '原文链接:' in line:
                in_content = True
                continue
            if in_content and line and not line.startswith('---'):
                summary_lines.append(line)
                if len(summary_lines) >= 15:
                    break

        summary_zh = '\n'.join(summary_lines)
        summary_en = None

        # Determine platform from URL
        platform = source_info.get('platform', 'manual')
        if url:
            if 'twitter.com' in url or 'x.com' in url:
                platform = 'x'
            elif 'github.com' in url:
                platform = 'github'
            elif 'mp.weixin.qq.com' in url:
                platform = 'wechat'
            elif 'anthropic.com' in url:
                platform = 'anthropic'
            elif 'google' in url:
                platform = 'google'

        # Extract images
        images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

        # Clean and validate data
        cleaned_title = clean_text(title, max_len=140) or f"AI资源 - {file_path.stem}"
        cleaned_summary_zh = clean_text(summary_zh, max_len=300) if has_readable_text(summary_zh) else None

        return {
            'id': generate_entry_id(title=cleaned_title, url=url),
            'title': cleaned_title,
            'url': normalize_url(url),
            'source': {
                'platform': platform,
                'author': clean_text(author, max_len=100) if author else None,
                'original_date': normalize_date(raw_date)
            },
            'summary_zh': cleaned_summary_zh,
            'summary_en': summary_en,
            'category': frontmatter.get('category', 'uncategorized'),
            'source_type': 'x_post' if platform == 'x' else 'article',
            'language': 'both' if (summary_zh and summary_en) else ('zh' if has_cjk(summary_zh or title) else 'en'),
            'tags': frontmatter.get('tags', []),
            'one_liner_author': 'openclaw',
            'quality_score': 3,  # Default score
            'status': 'score-pending',
            'local_path': f"content/{generate_entry_id(title=cleaned_title, url=url)}.md",
            'images': images[:5],  # Limit to 5 images
            'added_date': date.today().isoformat(),
            'updated_date': date.today().isoformat(),
            'related': []
        }

    # Handle regular files
    # Extract key information
    title = frontmatter.get('title', '')
    url = frontmatter.get('url', '')
    author = frontmatter.get('author', frontmatter.get('source_platform', ''))

    # Extract date - handle relative dates
    raw_date = frontmatter.get('date', '')
    if not raw_date:
        # Try to extract date from filename or content
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', str(file_path))
        if date_match:
            raw_date = date_match.group(1)

    # Extract summary from content
    summary_lines = []
    lines = content.split('\n')
    for line in lines:
        if line.strip() and not line.startswith('#') and not line.startswith('---'):
            summary_lines.append(line.strip())
            if len(summary_lines) >= 10:  # Limit summary length
                break

    summary_zh = '\n'.join(summary_lines[:50])  # First 50 lines as summary
    summary_en = None  # Will be set later if content is English

    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

    # Determine language and create bilingual summary if needed
    if has_cjk(summary_zh) and not has_cjk(title):
        # If title is English but summary has Chinese, assume mixed content
        pass
    elif not has_cjk(summary_zh) and not has_cjk(title):
        # If both are English, create English summary
        summary_en = summary_zh
        summary_zh = clean_text(summary_zh, max_len=300) if has_readable_text(summary_zh) else None

    # Clean and validate data
    cleaned_title = clean_text(title, max_len=140) or f"AI资源 - {file_path.stem}"
    cleaned_summary_zh = clean_text(summary_zh, max_len=300) if has_readable_text(summary_zh) else None

    # Calculate relative path from project root to content directory
    project_root = Path.cwd()
    if str(file_path).startswith(str(project_root)):
        relative_path = str(file_path.relative_to(project_root))
    else:
        # If file is outside project, use a reasonable path
        relative_path = f"content/external/{file_path.stem}.md"

    return {
        'id': generate_entry_id(title=cleaned_title, url=url),
        'title': cleaned_title,
        'url': normalize_url(url),
        'source': {
            'platform': frontmatter.get('source_platform', 'manual'),
            'author': clean_text(author, max_len=100) if author else None,
            'original_date': normalize_date(raw_date)
        },
        'summary_zh': cleaned_summary_zh,
        'summary_en': summary_en,
        'category': frontmatter.get('category', 'uncategorized'),
        'source_type': 'article',  # Default to article
        'language': 'both' if (summary_zh and summary_en) else ('zh' if has_cjk(summary_zh or title) else 'en'),
        'tags': frontmatter.get('tags', []),
        'one_liner_author': 'openclaw',
        'quality_score': 3,  # Default score
        'status': 'score-pending',
        'local_path': relative_path,
        'images': images[:5],  # Limit to 5 images
        'added_date': date.today().isoformat(),
        'updated_date': date.today().isoformat(),
        'related': []
    }

def process_intake_task(root_path: Path, max_entries: int = 20) -> Dict[str, Any]:
    """Execute the daily intake task."""
    print("Starting daily intake task...")

    # Step 1: Find recent AI files
    print("Step 1: Finding recent AI-related files...")
    recent_files = find_recent_ai_files(root_path, days=1)
    print(f"Found {len(recent_files)} recent AI-related files")

    if not recent_files:
        print("No recent AI files found. Exiting.")
        return {'success': True, 'message': 'No recent AI files found', 'processed': 0}

    # Step 2: Extract metadata from files
    print("Step 2: Extracting metadata...")
    new_entries = []
    for file_path in recent_files[:max_entries]:  # Limit processing
        try:
            entry = extract_metadata_from_file(file_path)
            print(f"Processing: {entry['title']}")
            new_entries.append(entry)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"Extracted {len(new_entries)} entries")

    if not new_entries:
        print("No valid entries extracted. Exiting.")
        return {'success': True, 'message': 'No valid entries extracted', 'processed': 0}

    # Step 3: Load existing entries and append new ones
    print("Step 3: Loading existing entries and appending new ones...")
    try:
        existing_data = load_entries_data(entries_path())
        print(f"Loaded existing entries: {len(existing_data.get('entries', []))}")
    except Exception as e:
        print(f"Warning: Could not load existing entries: {e}")
        existing_data = {'entries': []}

    # Add the new entries using pipeline_utils
    added_entries, skipped_entries = append_entries(existing_data, new_entries)

    print(f"Added {len(added_entries)} new entries")
    print(f"Skipped {len(skipped_entries)} entries (duplicates or invalid)")

    if skipped_entries:
        for entry, reason in skipped_entries:
            print(f"Skipped: {entry['title']} - {reason}")

    # Step 4: Save updated entries
    print("Step 4: Saving updated entries...")
    try:
        save_entries_data(existing_data)
        print("Entries saved successfully")
    except Exception as e:
        print(f"Error saving entries: {e}")
        return {'success': False, 'message': f'Save failed: {e}', 'processed': len(added_entries)}

    total_entries = len(existing_data.get('entries', []))
    return {
        'success': True,
        'message': 'Intake task completed successfully',
        'processed': len(added_entries),
        'total_entries': total_entries
    }

def main():
    """Main execution function."""
    project_root = Path(__file__).parent.parent
    print(f"Working in: {project_root}")

    if not (project_root / "data" / "entries.json").exists():
        print("Error: entries.json not found. Make sure you're in the project root.")
        sys.exit(1)

    # Execute intake task
    result = process_intake_task(project_root)

    # Print results
    if result['success']:
        print(f"\n✅ Daily intake completed successfully!")
        print(f"Processed: {result['processed']} new entries")
        if 'total_entries' in result and result['total_entries']:
            print(f"Total entries in database: {result['total_entries']}")
    else:
        print(f"\n❌ Daily intake failed: {result['message']}")
        sys.exit(1)

if __name__ == "__main__":
    main()