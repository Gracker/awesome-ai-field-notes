#!/usr/bin/env python3
"""
Simple changelog generator for awesome-ai-field-notes
"""

import json
import subprocess
from datetime import datetime, date, timedelta
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent
DATA_FILE = REPO_ROOT / "data/entries.json"
CHANGELOG_FILE = REPO_ROOT / "CHANGELOG.md"

print(f"Working in: {REPO_ROOT}")
print(f"Data file: {DATA_FILE}")
print(f"Changelog file: {CHANGELOG_FILE}")

# Check if data file exists
if not DATA_FILE.exists():
    print(f"Error: Data file {DATA_FILE} does not exist")
    exit(1)

# Load current entries
try:
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        current_data = json.load(f)
    print(f"Current entries loaded: {current_data.get('total_entries', len(current_data.get('entries', [])))}")
except Exception as e:
    print(f"Error loading current entries: {e}")
    exit(1)

# Get git snapshot
try:
    result = subprocess.run([
        'git', 'show', 'aced01a:data/entries.json'
    ], capture_output=True, text=True, check=True)
    snapshot_data = json.loads(result.stdout)
    print(f"Snapshot entries loaded: {snapshot_data.get('total_entries', len(snapshot_data.get('entries', [])))}")
except subprocess.CalledProcessError as e:
    print(f"Error getting git snapshot: {e}")
    exit(1)

# Compare entries
current_entries = current_data.get('entries', [])
snapshot_entries = snapshot_data.get('entries', [])

current_ids = {entry['id']: entry for entry in current_entries}
snapshot_ids = {entry['id']: entry for entry in snapshot_entries}

# Find new entries
added_entries = []
for entry_id, entry in current_ids.items():
    if entry_id not in snapshot_ids:
        added_entries.append(entry)

print(f"Added entries: {len(added_entries)}")

# Generate basic changelog
current_date = datetime.now().astimezone()
end_date = current_date.replace(hour=4, minute=0, second=0, microsecond=0)
start_date = end_date - timedelta(days=7)

changelog = f"""# Changelog

## {start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}

> 上次变更日志: {start_date.strftime('%Y-%m-%d')} 04:35 (commit aced01a, {snapshot_data.get('total_entries', len(snapshot_entries))} 条) → 本次: {current_data.get('total_entries', len(current_entries))} 条 (**+{current_data.get('total_entries', len(current_entries)) - snapshot_data.get('total_entries', len(snapshot_entries))}**)
> 基线快照: `aced01a:data/entries.json` ({start_date.strftime('%Y-%m-%d')} 23:34)

### 📈 新增 ({len(added_entries)})

"""

# Add new entries (limit to 50)
high_quality_added = [e for e in added_entries if e.get('quality_score', 0) >= 4]
regular_added = [e for e in added_entries if e.get('quality_score', 0) < 4]

changelog += f"**🆕 高质量新增 (⭐≥4, {len(high_quality_added)} 条)**\n\n"

for entry in high_quality_added[:20]:
    stars = "⭐" * min(entry.get('quality_score', 0), 5)
    category = entry.get('category', 'uncategorized')
    added_date = entry.get('added_date', 'Unknown')
    title = entry.get('title', 'No Title')
    url = entry.get('url', '')
    
    if url:
        changelog += f"- [{title}]({url}) — {category} {stars} ({added_date})\n"
    else:
        changelog += f"- {title} — {category} {stars} ({added_date})\n"

changelog += f"\n**📝 普通新增 (⭐<4, {len(regular_added)} 条)**\n\n"

for entry in regular_added[:30]:
    stars = "⭐" * min(entry.get('quality_score', 0), 5)
    category = entry.get('category', 'uncategorized')
    added_date = entry.get('added_date', 'Unknown')
    title = entry.get('title', 'No Title')
    url = entry.get('url', '')
    
    if url:
        changelog += f"- [{title}]({url}) — {category} {stars} ({added_date})\n"
    else:
        changelog += f"- {title} — {category} {stars} ({added_date})\n"

changelog += f"""

### 📊 统计

- 总条目: {snapshot_data.get('total_entries', len(snapshot_entries))} → {current_data.get('total_entries', len(current_entries))} (**+{current_data.get('total_entries', len(current_entries)) - snapshot_data.get('total_entries', len(snapshot_entries))}**)
- 新增条目: {len(added_entries)}
"""

# Save to changelog
try:
    with open(CHANGELOG_FILE, 'r', encoding='utf-8') as f:
        existing_content = f.read()
    
    # Insert new changelog after the title
    title_end = existing_content.find('\n', 1)
    if title_end == -1:
        title_end = len(existing_content)
    
    new_content = existing_content[:title_end+1] + changelog + '\n\n' + existing_content[title_end+1:]
    
    with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Changelog updated successfully")
except Exception as e:
    print(f"Error saving changelog: {e}")
    exit(1)