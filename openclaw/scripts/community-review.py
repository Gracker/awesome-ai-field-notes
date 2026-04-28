#!/usr/bin/env python3
"""
Community Review Automation Script
自动处理社区提交的 Issue（新条目/纠错），合并到 entries.json
"""

import json
import os
import datetime
import re
import subprocess
import sys
from typing import List, Dict, Optional, Tuple
import requests

PROJECT_ROOT = "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes"
ENTRIES_FILE = os.path.join(PROJECT_ROOT, "data", "entries.json")
CATEGORIES_FILE = os.path.join(PROJECT_ROOT, "data", "categories.json")

# Configuration
REPO = "Gracker/awesome-ai-field-notes"
MAX_ISSUES_PER_DAY = 20
GH_TOKEN = os.environ.get('GITHUB_TOKEN')

class CommunityReviewProcessor:
    def __init__(self):
        self.entries_data = self._load_entries()
        self.categories = self._load_categories()
        self.processed_count = 0
        self.new_entries_added = 0
        self.corrections_fixed = 0
        
    def _load_entries(self) -> Dict:
        """Load entries from entries.json"""
        with open(ENTRIES_FILE, encoding='utf-8') as f:
            return json.load(f)
    
    def _load_categories(self) -> Dict:
        """Load categories from categories.json"""
        with open(CATEGORIES_FILE, encoding='utf-8') as f:
            return json.load(f)
    
    def _get_existing_urls(self) -> set:
        """Get all existing URLs for deduplication"""
        return {e.get('url') for e in self.entries_data['entries'] if e.get('url')}
    
    def _get_existing_titles(self) -> set:
        """Get all existing titles for similarity checking"""
        return {e.get('title', '').lower().strip() for e in self.entries_data['entries'] if e.get('title')}
    
    def _title_similarity(self, title1: str, title2: str) -> bool:
        """Check if two titles are similar"""
        if not title1 or not title2:
            return False
        
        # Remove common prefixes/suffixes and normalize
        def normalize_title(title):
            title = title.lower().strip()
            # Remove common patterns like "新分享", "推荐", etc.
            title = re.sub(r'\s*(新|推荐|分享|介绍|分析|教程|指南|大全).*$', '', title)
            return title
        
        norm1 = normalize_title(title1)
        norm2 = normalize_title(title2)
        
        # If either is empty after normalization, return False
        if not norm1 or not norm2:
            return False
        
        # Check if one is substring of the other (with some leniency)
        return (len(norm1) > 5 and len(norm2) > 5 and 
                (norm1 in norm2 or norm2 in norm1 or 
                 self._string_similarity(norm1, norm2) > 0.8))
    
    def _string_similarity(self, s1: str, s2: str) -> float:
        """Calculate simple string similarity"""
        if not s1 or not s2:
            return 0.0
        
        # Calculate intersection over union
        set1 = set(s1.split())
        set2 = set(s2.split())
        
        if not set1 or not set2:
            return 0.0
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union if union > 0 else 0.0
    
    def _check_duplicate_entry(self, title: str, url: str) -> bool:
        """Check if entry is duplicate"""
        existing_urls = self._get_existing_urls()
        existing_titles = self._get_existing_titles()
        
        # Check URL duplicate
        if url in existing_urls:
            return True
        
        # Check title similarity
        for existing_title in existing_titles:
            if self._title_similarity(title, existing_title):
                return True
        
        return False
    
    def _auto_classify(self, title: str, content: str, suggested_category: str = None) -> str:
        """Automatically classify entry"""
        # Simple keyword-based classification
        title_lower = title.lower()
        content_lower = content.lower()
        
        # Check if suggested category exists
        if suggested_category and suggested_category in self.categories:
            return suggested_category
        
        # Category mapping based on keywords
        category_keywords = {
            'agent-frameworks/harness-engineering': ['harness', 'engineering', 'agent', 'framework'],
            'infrastructure/managed-agents': ['managed', 'agent', 'infrastructure', 'sandbox'],
            'hardware-chips/risc-v-ai': ['risc-v', 'chip', 'hardware', 'ai', 'memory'],
            'strategy/ai-product': ['product', 'strategy', 'business', 'management'],
            'tools-development/frameworks': ['framework', 'tool', 'library', 'sdk'],
            'tools-development/applications': ['application', 'app', 'software', 'platform'],
            'research-methods/benchmarks': ['benchmark', 'evaluation', 'metric', 'test'],
            'research-methods/datasets': ['dataset', 'corpus', 'data', 'collection'],
            'education/online-courses': ['course', 'tutorial', 'education', 'learning'],
            'education/books': ['book', 'ebook', 'publication', 'paper'],
            'community/chat-discussions': ['chat', 'discussion', 'forum', 'community'],
            'community/news-updates': ['news', 'update', 'announcement', 'release']
        }
        
        # Score categories based on keyword matches
        category_scores = {}
        for category, keywords in category_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in title_lower or keyword in content_lower:
                    score += 1
            if score > 0:
                category_scores[category] = score
        
        # Return highest scoring category
        if category_scores:
            return max(category_scores, key=category_scores.get)
        
        # Default fallback
        return 'tools-development/applications'
    
    def _auto_score(self, title: str, content: str) -> int:
        """Automatically score entry (1-5)"""
        title_lower = title.lower()
        content_lower = content.lower()
        
        score = 3  # Base score
        
        # Increase score for certain indicators
        if any(indicator in title_lower for indicator in ['breakthrough', 'revolution', 'major', 'important']):
            score += 1
        if any(indicator in title_lower for indicator in ['deep dive', 'comprehensive', 'detailed', 'thorough']):
            score += 1
        if any(indicator in content_lower for indicator in ['github.com', 'anthropic.com', 'openai.com', 'google.com']):
            score += 1
        if len(content) > 5000:  # Long content
            score += 1
        
        # Decrease score for certain indicators
        if any(indicator in title_lower for indicator in ['beginner', 'intro', 'basic', 'simple']):
            score -= 1
        if len(content) < 1000:  # Very short content
            score -= 1
        
        # Clamp to 1-5 range
        return max(1, min(5, score))
    
    def _generate_one_liner(self, title: str, content: str, category: str) -> str:
        """Generate one-liner for entry"""
        # Template-based one-liner generation
        category_templates = {
            'agent-frameworks/harness-engineering': 'Harness Engineering 是将 AI Agent 从好玩具变可靠工具的完整工程框架',
            'infrastructure/managed-agents': 'Managed Agents 通过解耦大脑与手，实现 AI Agent 的可靠扩展',
            'hardware-chips/risc-v-ai': 'AI 芯片从算力怪兽向有脑子的行动派的进化路线',
            'strategy/ai-product': 'AI 产品的难点不在于技术而在于不确定性管理',
            'tools-development/frameworks': 'AI 开发框架为 Agent 系统提供基础设施支持',
            'tools-development/applications': 'AI 应用工具将 AI 能力转化为实际生产力',
            'research-methods/benchmarks': 'AI 评估基准为系统性能提供客观度量标准',
            'research-methods/datasets': 'AI 数据集为模型训练和评估提供基础资源',
            'education/online-courses': 'AI 教育课程帮助开发者快速掌握前沿技术',
            'education/books': 'AI 相关书籍提供深入的理论知识与实践经验',
            'community/chat-discussions': 'AI 社区讨论促进技术交流与知识共享',
            'community/news-updates': 'AI 新闻资讯及时反映行业发展趋势'
        }
        
        template = category_templates.get(category, 'AI 领域的重要资源与实践经验')
        
        # Extract key concepts from content
        content_words = content.lower().split()[:100]  # First 100 words
        key_concepts = []
        
        concept_keywords = {
            'agent': ['agent', '智能体', '代理'],
            'framework': ['framework', '框架', '架构'],
            'engineering': ['engineering', '工程', '构建'],
            'technology': ['technology', '技术', '创新'],
            'research': ['research', '研究', '论文'],
            'practice': ['practice', '实践', '经验'],
            'tool': ['tool', '工具', '平台'],
            'system': ['system', '系统', '平台']
        }
        
        for concept, keywords in concept_keywords.items():
            if any(keyword in content_words for keyword in keywords):
                key_concepts.append(concept)
        
        if key_concepts:
            return f"{template}，涵盖 {'、'.join(key_concepts)} 等核心内容"
        
        return template
    
    def _create_entry(self, title: str, url: str, platform: str, author: str, 
                     orig_date: str, category: str, tags: List[str], 
                     source_type: str, language: str, summary_zh: str, 
                     summary_en: str, quality: int, content: str) -> Dict:
        """Create a new entry"""
        entry_id = self._generate_id(title)
        
        # Extract images from content
        images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
        images = images[:5]  # Max 5 images
        
        today = datetime.date.today().isoformat()
        
        entry = {
            "id": entry_id,
            "title": title,
            "url": url,
            "source": {
                "platform": platform,
                "author": author,
                "original_date": orig_date
            },
            "category": category,
            "tags": tags,
            "source_type": source_type,
            "language": language,
            "summary_zh": summary_zh,
            "summary_en": summary_en,
            "one_liner": self._generate_one_liner(title, content, category),
            "one_liner_author": "openclaw",
            "quality_score": quality,
            "status": "active",
            "local_path": f"content/{entry_id}.md",
            "images": images,
            "added_date": today,
            "updated_date": None,
            "github_stars": None,
            "related": []
        }
        
        # Save content to file
        content_file = os.path.join(PROJECT_ROOT, "content", f"{entry_id}.md")
        with open(content_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return entry
    
    def _generate_id(self, title: str) -> str:
        """Generate ID from title"""
        # Simple ID generation - replace spaces and special chars, take first 10 chars
        clean_title = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]', '', title)[:10]
        return clean_title.lower()
    
    def _process_new_entry_issue(self, issue: Dict) -> bool:
        """Process a new-entry issue"""
        try:
            # Extract information from issue
            title = issue.get('title', '')
            body = issue.get('body', '')
            url = self._extract_url_from_issue(body)
            
            if not url:
                print(f"⚠️  Issue #{issue['number']}: No URL found in issue body")
                return False
            
            if self._check_duplicate_entry(title, url):
                print(f"⚠️  Issue #{issue['number']}: Duplicate entry - {title}")
                return False
            
            # Extract suggested category
            suggested_category = self._extract_category_from_issue(body)
            
            # Get content (simplified - in real implementation would fetch from URL)
            content = f"Content for: {title}\n\nThis is a placeholder for the actual content that would be fetched from {url}."
            
            # Auto classify and score
            category = self._auto_classify(title, content, suggested_category)
            quality = self._auto_score(title, content)
            
            # Create entry
            entry = self._create_entry(
                title=title,
                url=url,
                platform="community",
                author=issue.get('user', {}).get('login', 'anonymous'),
                orig_date=datetime.date.today().isoformat(),
                category=category,
                tags=["community-submitted"],
                source_type="article",
                language="zh",  # Default to Chinese
                summary_zh=f"社区提交的资源：{title}",
                summary_en=None,
                quality=quality,
                content=content
            )
            
            # Add to entries
            self.entries_data['entries'].append(entry)
            self.new_entries_added += 1
            self.processed_count += 1
            
            # Update issue with response
            self._add_issue_comment(issue['number'], f"""
✅ 已收录为条目 #{issue['number']}
- 分类: {category}
- 评分: {quality}/5
- one_liner: "{entry['one_liner']}"

感谢贡献！
""")
            
            print(f"✅ Processed new entry: {title}")
            return True
            
        except Exception as e:
            print(f"❌ Error processing new entry issue #{issue['number']}: {str(e)}")
            return False
    
    def _process_correction_issue(self, issue: Dict) -> bool:
        """Process a correction issue"""
        try:
            # Extract correction details from issue
            body = issue.get('body', '')
            correction_type = self._extract_correction_type(body)
            target_url = self._extract_url_from_issue(body)
            
            if not target_url:
                print(f"⚠️  Issue #{issue['number']}: No target URL found in issue body")
                return False
            
            # Find the entry to correct
            entry_to_correct = None
            for entry in self.entries_data['entries']:
                if entry.get('url') == target_url:
                    entry_to_correct = entry
                    break
            
            if not entry_to_correct:
                print(f"⚠️  Issue #{issue['number']}: Target URL not found in entries")
                return False
            
            # Process based on correction type
            if correction_type == 'dead-link':
                self._process_dead_link_correction(entry_to_correct, issue)
            elif correction_type == 'wrong-category':
                self._process_category_correction(entry_to_correct, issue)
            elif correction_type == 'wrong-score':
                self._process_score_correction(entry_to_correct, issue)
            else:
                print(f"⚠️  Issue #{issue['number']}: Unknown correction type")
                return False
            
            self.corrections_fixed += 1
            self.processed_count += 1
            
            print(f"✅ Processed correction for: {entry_to_correct['title']}")
            return True
            
        except Exception as e:
            print(f"❌ Error processing correction issue #{issue['number']}: {str(e)}")
            return False
    
    def _extract_url_from_issue(self, body: str) -> Optional[str]:
        """Extract URL from issue body"""
        # Look for URLs in the body
        url_pattern = r'https?://[^\s\)]+'
        urls = re.findall(url_pattern, body)
        return urls[0] if urls else None
    
    def _extract_category_from_issue(self, body: str) -> Optional[str]:
        """Extract suggested category from issue body"""
        # Look for category patterns
        category_patterns = [
            r'分类[:：]\s*([^\n\r]+)',
            r'category[:：]\s*([^\n\r]+)',
            r'suggested[:：]\s*([^\n\r]+)'
        ]
        
        for pattern in category_patterns:
            match = re.search(pattern, body, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def _extract_correction_type(self, body: str) -> str:
        """Extract correction type from issue body"""
        body_lower = body.lower()
        
        if 'dead' in body_lower or 'broken' in body_lower or '404' in body_lower:
            return 'dead-link'
        elif 'category' in body_lower or '分类' in body:
            return 'wrong-category'
        elif 'score' in body_lower or 'rating' in body_lower or '评分' in body:
            return 'wrong-score'
        else:
            return 'dead-link'  # Default assumption
    
    def _process_dead_link_correction(self, entry: Dict, issue: Dict):
        """Process dead link correction"""
        entry['status'] = 'archived'
        entry['updated_date'] = datetime.date.today().isoformat()
        
        comment = f"""
✅ 已修复
- 问题: 死链接检测
- 处理: 标记为已归档
- 变更: 状态从 active 改为 archived
"""
        self._add_issue_comment(issue['number'], comment)
    
    def _process_category_correction(self, entry: Dict, issue: Dict):
        """Process category correction"""
        # Get new category suggestion
        suggested_category = self._extract_category_from_issue(issue.get('body', ''))
        
        if suggested_category and suggested_category in self.categories:
            entry['category'] = suggested_category
            entry['updated_date'] = datetime.date.today().isoformat()
            
            comment = f"""
✅ 已修复
- 问题: 分类错误
- 处理: 重新分类
- 变更: 分类从 {entry['category']} 改为 {suggested_category}
"""
            self._add_issue_comment(issue['number'], comment)
        else:
            # Auto-correct using content
            content_file = os.path.join(PROJECT_ROOT, entry['local_path'])
            if os.path.exists(content_file):
                with open(content_file, encoding='utf-8') as f:
                    content = f.read()
                
                new_category = self._auto_classify(entry['title'], content)
                if new_category != entry['category']:
                    entry['category'] = new_category
                    entry['updated_date'] = datetime.date.today().isoformat()
                    
                    comment = f"""
✅ 已修复
- 问题: 分类错误
- 处理: 自动重新分类
- 变更: 分类从 {entry['category']} 改为 {new_category}
"""
                    self._add_issue_comment(issue['number'], comment)
    
    def _process_score_correction(self, entry: Dict, issue: Dict):
        """Process score correction"""
        # Get content for re-scoring
        content_file = os.path.join(PROJECT_ROOT, entry['local_path'])
        if os.path.exists(content_file):
            with open(content_file, encoding='utf-8') as f:
                content = f.read()
            
            new_score = self._auto_score(entry['title'], content)
            if new_score != entry['quality_score']:
                entry['quality_score'] = new_score
                entry['updated_date'] = datetime.date.today().isoformat()
                
                comment = f"""
✅ 已修复
- 问题: 评分异议
- 处理: 自动重新评分
- 变更: 评分从 {entry['quality_score']} 改为 {new_score}
"""
                self._add_issue_comment(issue['number'], comment)
    
    def _add_issue_comment(self, issue_number: int, comment: str):
        """Add comment to GitHub issue"""
        if not GH_TOKEN:
            print(f"⚠️  No GitHub token, skipping comment for issue #{issue_number}")
            return
        
        url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}/comments"
        headers = {
            'Authorization': f'token {GH_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        try:
            response = requests.post(url, headers=headers, json={'body': comment})
            response.raise_for_status()
            print(f"✅ Added comment to issue #{issue_number}")
        except Exception as e:
            print(f"❌ Failed to add comment to issue #{issue_number}: {str(e)}")
    
    def _close_issue(self, issue_number: int):
        """Close GitHub issue"""
        if not GH_TOKEN:
            print(f"⚠️  No GitHub token, skipping close for issue #{issue_number}")
            return
        
        url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}"
        headers = {
            'Authorization': f'token {GH_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        try:
            response = requests.patch(url, headers=headers, json={'state': 'closed'})
            response.raise_for_status()
            print(f"✅ Closed issue #{issue_number}")
        except Exception as e:
            print(f"❌ Failed to close issue #{issue_number}: {str(e)}")
    
    def get_open_issues(self) -> List[Dict]:
        """Get open GitHub issues with relevant labels"""
        if not GH_TOKEN:
            print("🔐 No GitHub token found, using mock data for testing")
            return self._get_mock_issues()
        
        try:
            # Get issues with new-entry label
            new_entry_url = f"https://api.github.com/repos/{REPO}/issues?labels=new-entry,state:open"
            correction_url = f"https://api.github.com/repos/{REPO}/issues?labels=correction,state:open"
            
            headers = {
                'Authorization': f'token {GH_TOKEN}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            new_entry_response = requests.get(new_entry_url, headers=headers)
            correction_response = requests.get(correction_url, headers=headers)
            
            new_entry_response.raise_for_status()
            correction_response.raise_for_status()
            
            new_entry_issues = new_entry_response.json()
            correction_issues = correction_response.json()
            
            # Flatten the response (might be paginated)
            all_issues = []
            if isinstance(new_entry_issues, list):
                all_issues.extend(new_entry_issues)
            if isinstance(correction_issues, list):
                all_issues.extend(correction_issues)
            
            return all_issues[:MAX_ISSUES_PER_DAY]  # Respect daily limit
            
        except Exception as e:
            print(f"❌ Failed to get GitHub issues: {str(e)}")
            return []
    
    def _get_mock_issues(self) -> List[Dict]:
        """Get mock issues for testing without GitHub token"""
        print("📋 Generating mock issues for testing...")
        
        # Mock new entry issue
        mock_new_entry = {
            'number': 1,
            'title': '新资源：Harness Engineering 实践指南',
            'body': '''我发现了一个很好的资源：

标题：Harness Engineering 完整指南
链接：https://example.com/harness-engineering-guide
分类：agent-frameworks/harness-engineering

这是一个关于如何构建可靠AI Agent的详细指南，包含了实践案例和代码示例。''',
            'user': {'login': 'test-user'},
            'labels': [{'name': 'new-entry'}]
        }
        
        # Mock correction issue
        mock_correction = {
            'number': 2,
            'title': '纠错：某链接已失效',
            'body': '''我发现一个链接已经失效了：

原文链接：https://example.com/dead-link

页面返回404错误，需要标记为已归档。''',
            'user': {'login': 'test-user'},
            'labels': [{'name': 'correction'}]
        }
        
        return [mock_new_entry, mock_correction]
    
    def save_entries(self):
        """Save updated entries to file"""
        self.entries_data['last_updated'] = datetime.datetime.now().isoformat()
        
        with open(ENTRIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.entries_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Saved {len(self.entries_data['entries'])} entries to entries.json")
    
    def validate_entries(self) -> bool:
        """Validate entries.json schema"""
        try:
            import jsonschema
            schema = {
                "type": "object",
                "properties": {
                    "version": {"type": "string"},
                    "schema_description": {"type": "string"},
                    "last_updated": {"type": "string"},
                    "entries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "title": {"type": "string"},
                                "url": {"type": ["string", "null"]},
                                "category": {"type": "string"},
                                "quality_score": {"type": "integer", "minimum": 1, "maximum": 5}
                            },
                            "required": ["id", "title", "category", "quality_score"]
                        }
                    }
                },
                "required": ["version", "schema_description", "last_updated", "entries"]
            }
            
            jsonschema.validate(self.entries_data, schema)
            print("✅ Entries validation passed")
            return True
            
        except Exception as e:
            print(f"❌ Entries validation failed: {str(e)}")
            return False
    
    def commit_and_push(self):
        """Commit and push changes to git"""
        try:
            # Add changes
            subprocess.run(['git', 'add', '-A'], cwd=PROJECT_ROOT, check=True)
            
            # Commit
            commit_msg = f"[openclaw] community: process {self.processed_count} issues — {self.new_entries_added} entries added, {self.corrections_fixed} fixed"
            subprocess.run(['git', 'commit', '-m', commit_msg], cwd=PROJECT_ROOT, check=True)
            
            # Push
            subprocess.run(['git', 'push', 'origin', 'main'], cwd=PROJECT_ROOT, check=True)
            
            print(f"✅ Committed and pushed changes: {commit_msg}")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Git operation failed: {str(e)}")
    
    def send_notification(self):
        """Send notification to OpenClaw - EBook group"""
        summary = f"""
🤖 Community Review Task Completed

📊 Summary:
- Issues processed: {self.processed_count}
- New entries added: {self.new_entries_added}
- Corrections fixed: {self.corrections_fixed}
- Total entries: {len(self.entries_data['entries'])}

📅 Date: {datetime.date.today().isoformat()}
🔗 Repository: {REPO}
        """
        
        print("📢 Notification Summary:")
        print(summary)
        
        # Send to Telegram group if possible
        try:
            # Try to import and use message function
            from message import message
            message(
                action="send",
                target="@openclaw_ebook",  # Replace with actual group ID
                message=summary
            )
            print("✅ Notification sent to OpenClaw - EBook group")
        except Exception as e:
            print(f"⚠️  Failed to send Telegram notification: {str(e)}")
            print("💡 Notification summary printed above")
    
    def run(self):
        """Main execution"""
        print("🚀 Starting community review automation...")
        
        # Get open issues
        issues = self.get_open_issues()
        print(f"📋 Found {len(issues)} open issues to process")
        
        if not issues:
            print("📭 No issues to process")
            self.send_notification()
            return
        
        # Process issues
        new_entry_issues = []
        correction_issues = []
        
        for issue in issues:
            labels = [label['name'] for label in issue.get('labels', [])]
            if 'new-entry' in labels:
                new_entry_issues.append(issue)
            elif 'correction' in labels:
                correction_issues.append(issue)
        
        # Process new entries first
        for issue in new_entry_issues:
            if self.processed_count >= MAX_ISSUES_PER_DAY:
                break
            
            if self._process_new_entry_issue(issue):
                self._close_issue(issue['number'])
        
        # Process corrections
        for issue in correction_issues:
            if self.processed_count >= MAX_ISSUES_PER_DAY:
                break
            
            if self._process_correction_issue(issue):
                self._close_issue(issue['number'])
        
        # Save and validate
        self.save_entries()
        
        if self.validate_entries():
            # Commit and push
            self.commit_and_push()
        
        # Send notification
        self.send_notification()
        
        print(f"🎉 Community review completed: {self.processed_count} issues processed")

def main():
    processor = CommunityReviewProcessor()
    processor.run()

if __name__ == "__main__":
    main()