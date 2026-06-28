#!/usr/bin/env python3
"""
Compare entries.json with last week's git snapshot and generate changelog.
"""

import json
import subprocess
from datetime import datetime, date, timedelta
from pathlib import Path
import os

# Configuration
REPO_ROOT = Path(__file__).parent
DATA_FILE = REPO_ROOT / "data/entries.json"
CHANGELOG_FILE = REPO_ROOT / "CHANGELOG.md"

# Get current date (Asia/Shanghai Sunday 04:30 = UTC Saturday 20:30)
# For changelog, we want the week ending Sunday 04:00
current_date = datetime.now().astimezone()
# Find the most recent Sunday at 04:00 (Asia/Shanghai)
if current_date.weekday() == 6 and current_date.hour >= 4 and current_date.minute >= 0:  # Sunday
    end_date = current_date.replace(hour=4, minute=0, second=0, microsecond=0)
else:
    # Go to previous Sunday at 04:00
    days_since_sunday = current_date.weekday() + 1
    end_date = current_date - timedelta(days=days_since_sunday)
    end_date = end_date.replace(hour=4, minute=0, second=0, microsecond=0)
    
start_date = end_date - timedelta(days=7)

print(f"Analyzing changelog for {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}")

def get_git_snapshot(commit_hash, file_path):
    """Get JSON data from git snapshot"""
    try:
        result = subprocess.run([
            'git', 'show', f'{commit_hash}:{file_path}'
        ], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error getting git snapshot: {e}")
        return None

def get_current_entries():
    """Load current entries.json"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error reading current entries: {e}")
        return None

def compare_entries(current_data, snapshot_data):
    """Compare current entries with snapshot"""
    if not current_data or not snapshot_data:
        return None
    
    current_entries = current_data.get('entries', [])
    snapshot_entries = snapshot_data.get('entries', [])
    
    # Create lookup maps
    current_ids = {entry['id']: entry for entry in current_entries}
    snapshot_ids = {entry['id']: entry for entry in snapshot_entries}
    
    # Find differences
    added_entries = []
    archived_entries = []
    rating_changes = []
    category_changes = []
    
    # New entries (in current but not in snapshot)
    for entry_id, entry in current_ids.items():
        if entry_id not in snapshot_ids:
            if entry.get('added_date', '9999-01-01') >= start_date.strftime('%Y-%m-%d'):
                added_entries.append(entry)
        else:
            # Check for rating changes
            snapshot_entry = snapshot_ids[entry_id]
            current_rating = entry.get('quality_score', 0)
            snapshot_rating = snapshot_entry.get('quality_score', 0)
            if current_rating != snapshot_rating and current_rating > 0:
                rating_changes.append({
                    'entry': entry,
                    'from': snapshot_rating,
                    'to': current_rating
                })
            
            # Check for category changes
            current_category = entry.get('category', 'uncategorized')
            snapshot_category = snapshot_entry.get('category', 'uncategorized')
            if current_category != snapshot_category:
                category_changes.append({
                    'entry': entry,
                    'from': snapshot_category,
                    'to': current_category
                })
            
            # Check for archived status
            current_status = entry.get('status', 'active')
            snapshot_status = snapshot_entry.get('status', 'active')
            if current_status == 'archived' and snapshot_status == 'active':
                archived_entries.append(entry)
    
    return {
        'added': sorted(added_entries, key=lambda x: x.get('added_date', '9999-01-01')),
        'archived': archived_entries,
        'rating_changes': rating_changes,
        'category_changes': category_changes,
        'current_total': current_data.get('total_entries', len(current_entries)),
        'snapshot_total': snapshot_data.get('total_entries', len(snapshot_entries))
    }

def get_category_stats(entries):
    """Get statistics by category"""
    categories = {}
    for entry in entries:
        category = entry.get('category', 'uncategorized')
        if category not in categories:
            categories[category] = {'total': 0, 'high_quality': 0}
        categories[category]['total'] += 1
        if entry.get('quality_score', 0) >= 4:
            categories[category]['high_quality'] += 1
    return categories

def generate_changelog(diff, start_date, end_date):
    """Generate changelog markdown"""
    if not diff:
        return "# No changes detected"
    
    high_quality_added = [e for e in diff['added'] if e.get('quality_score', 0) >= 4]
    regular_added = [e for e in diff['added'] if e.get('quality_score', 0) < 4]
    
    changelog = f"""# Changelog

## {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}

> 上次变更日志: {start_date.strftime('%Y-%m-%d')} 04:35 (commit {commit_hash}, {diff['snapshot_total']} 条) → 本次: {diff['current_total']} 条 (**+{diff['current_total'] - diff['snapshot_total']}**)
> 基线快照: `{commit_hash}:data/entries.json` ({start_date.strftime('%Y-%m-%d')} 23:34)

### 📈 新增 ({len(diff['added'])})

**🆕 高质量新增 (⭐≥4, {len(high_quality_added)} 条)**"""
    
    for entry in high_quality_added[:20]:  # Limit to 20 entries
        stars = "⭐" * min(entry.get('quality_score', 0), 5)
        category = entry.get('category', 'uncategorized')
        added_date = entry.get('added_date', 'Unknown')
        title = entry.get('title', 'No Title')
        url = entry.get('url', '')
        
        if url:
            changelog += f"- [{title}]({url}) — {category} {stars} ({added_date})\n"
        else:
            changelog += f"- {title} — {category} {stars} ({added_date})\n"
    
    if len(high_quality_added) > 20:
        changelog += f"\n...还有 {len(high_quality_added) - 20} 条高质量新增条目（已省略）"
    
    changelog += f"\n\n**📝 普通新增 (⭐<4, {len(regular_added)} 条)**"
    
    for entry in regular_added[:30]:  # Limit to 30 entries
        stars = "⭐" * min(entry.get('quality_score', 0), 5)
        category = entry.get('category', 'uncategorized')
        added_date = entry.get('added_date', 'Unknown')
        title = entry.get('title', 'No Title')
        url = entry.get('url', '')
        
        if url:
            changelog += f"- [{title}]({url}) — {category} {stars} ({added_date})\n"
        else:
            changelog += f"- {title} — {category} {stars} ({added_date})\n"
    
    if len(regular_added) > 30:
        changelog += f"\n...还有 {len(regular_added) - 30} 条普通新增条目（已省略）"
    
    # Archived entries
    if diff['archived']:
        changelog += f"\n\n### 📦 归档 ({len(diff['archived'])})\n"
        for entry in diff['archived']:
            title = entry.get('title', 'No Title')
            url = entry.get('url', '')
            if url:
                changelog += f"- [{title}]({url}) — 归档\n"
            else:
                changelog += f"- {title} — 归档\n"
    
    # Rating changes
    if diff['rating_changes']:
        changelog += f"\n\n### ✏️ 评分调整 ({len(diff['rating_changes'])})\n"
        for change in diff['rating_changes'][:10]:  # Limit to 10
            entry = change['entry']
            title = entry.get('title', 'No Title')
            url = entry.get('url', '')
            direction = "↑" if change['to'] > change['from'] else "↓"
            changelog += f"- [{title}]({url}) — {change['from']}→{change['to']}{direction}\n"
    
    # Category changes
    if diff['category_changes']:
        changelog += f"\n\n### 🔀 分类变更 ({len(diff['category_changes'])})\n"
        for change in diff['category_changes'][:10]:  # Limit to 10
            entry = change['entry']
            title = entry.get('title', 'No Title')
            url = entry.get('url', '')
            changelog += f"- [{title}]({url}) — {change['from']} → {change['to']}\n"
    
    # Statistics
    changelog += f"""

### 📊 统计

- 总条目: {diff['snapshot_total']} → {diff['current_total']} (**+{diff['current_total'] - diff['snapshot_total']}**)
- 新增条目: {len(diff['added'])}
- 归档条目: {len(diff['archived'])}
- 评分调整: {len(diff['rating_changes'])}
"""
    
    return changelog

# Main execution
if __name__ == "__main__":
    # Get last week's snapshot (aced01a had 895 entries)
    commit_hash = "aced01a"
    snapshot_data = get_git_snapshot(commit_hash, "data/entries.json")
    
    if not snapshot_data:
        print("Error: Could not get git snapshot")
        exit(1)
    
    # Get current entries
    current_data = get_current_entries()
    
    if not current_data:
        print("Error: Could not read current entries")
        exit(1)
    
    print(f"Current entries: {current_data.get('total_entries', len(current_data.get('entries', [])))}")
    print(f"Last week entries: {snapshot_data.get('total_entries', len(snapshot_data.get('entries', [])))}")
    
    # Compare
    diff = compare_entries(current_data, snapshot_data)
    
    if not diff:
        print("Error: Could not compare entries")
        exit(1)
    
    print(f"Generated changelog:")
    
    # Generate changelog
    changelog_content = generate_changelog(diff, start_date, end_date)
    print(changelog_content)
    
    # Save changelog
    with open(CHANGELOG_FILE, 'r', encoding='utf-8') as f:
        existing_content = f.read()
    
    # Insert new changelog after the title
    title_end = existing_content.find('\n', 1)
    if title_end == -1:
        title_end = len(existing_content)
    
    new_content = existing_content[:title_end+1] + changelog_content + '\n\n' + existing_content[title_end+1:]
    
    with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Changelog updated: {CHANGELOG_FILE}")