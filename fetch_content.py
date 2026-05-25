import sys
sys.path.insert(0, 'openclaw/scripts')
from pipeline_utils import load_entries_data, save_entries_data
import os

# Mock web_fetch function since we can't import from tools
def web_fetch(url, maxChars=5000):
    try:
        import requests
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.text[:maxChars]
        else:
            return None
    except:
        return None

# Get the top 5 entries to fetch
data = load_entries_data()
active_high_quality = []
for e in data['entries']:
    if e.get('status') == 'active':
        try:
            score = float(e.get('quality_score', 0))
            if score >= 4:
                content_file = e.get('content_file')
                if content_file:
                    exists = os.path.exists(content_file)
                else:
                    exists = os.path.exists(f'content/{e["id"]}.md')
                if not exists:
                    active_high_quality.append((e, score))
        except:
            pass

active_high_quality.sort(key=lambda x: -x[1])
top_5 = [e for e, score in active_high_quality[:5]]

print(f'Fetching content for {len(top_5)} entries...')
success_count = 0
skip_count = 0

for entry in top_5:
    entry_id = entry['id']
    url = entry.get('url', '')
    title = entry.get('title', '')
    score = entry.get('quality_score', '')
    
    print(f'\nProcessing: {entry_id} - {title[:50]}...')
    
    # Use web_fetch to get content
    try:
        result = web_fetch(url, maxChars=5000)
        
        if result and len(result) > 500:
            content = result
            # Create bilingual content
            bilingual_content = f'''# {title}

## Original English Content

{content}

## 中文翻译

[翻译将在实际实现中完成]

---

*质量评分: {score}*
*来源: {url}*
'''
            
            # Save content file
            content_path = f'content/{entry_id}.md'
            with open(content_path, 'w', encoding='utf-8') as f:
                f.write(bilingual_content)
            
            # Update entry with content_file
            entry['content_file'] = content_path
            save_entries_data(data)
            
            print(f'  ✓ Successfully saved: {content_path}')
            success_count += 1
        else:
            print(f'  ✗ Invalid content length: {len(result) if result else 0}')
            skip_count += 1
            
    except Exception as e:
        print(f'  ✗ Error: {str(e)}')
        skip_count += 1

print(f'\n=== Results ===')
print(f'Fetch {success_count}/5 successful, skipped {skip_count}')
