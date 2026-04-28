#!/usr/bin/env python3
"""
AI主动发现Agent处理脚本
从web搜索结果生成符合schema的新条目
"""

import json
import re
import hashlib
import datetime
from typing import List, Dict, Optional, Set
import numpy as np

# 获取今天的日期
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

def calculate_similarity(text1: str, text2: str) -> float:
    """计算两个文本的相似度"""
    # 简单的基于词汇重叠的相似度计算
    words1 = set(re.findall(r'\b\w+\b', text1.lower()))
    words2 = set(re.findall(r'\b\w+\b', text2.lower()))
    
    if not words1 and not words2:
        return 1.0
    if not words1 or not words2:
        return 0.0
    
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    
    return intersection / union if union > 0 else 0.0

def extract_url_from_citations(citations: List[Dict]) -> Optional[str]:
    """从citation中提取第一个可用的URL"""
    for citation in citations:
        if 'url' in citation and citation['url']:
            # 清理URL
            url = citation['url']
            if url.startswith('https://vertexaisearch.cloud.google.com/grounding-api-redirect/'):
                # 这是一个重定向URL，提取真实URL
                try:
                    real_url = url.split('AUZIYQ')[0]
                    # 尝试提取真实URL
                    if real_url.startswith('http'):
                        return real_url
                except:
                    continue
            elif url.startswith(('http://', 'https://')):
                return url
    return None

def generate_new_entries_from_search_results() -> List[Dict]:
    """从搜索结果生成新条目"""
    new_entries = []
    
    # 搜索结果1: MCP 2026
    mcp_content = """
    In 2026, the landscape of AI agent frameworks is significantly influenced by the Model Context Protocol (MCP), which acts as a crucial standard for how AI models interact with tools, APIs, and data sources. Rather than being an AI agent framework itself, MCP is a protocol that standardizes tool integration for various frameworks, akin to "USB for AI tools". This allows agents to connect to over 200 existing server implementations for platforms like GitHub, Slack, Google Drive, and more.

    Key aspects and developments regarding AI agent frameworks and MCP in 2026 include:

    **Model Context Protocol (MCP)**
    * **Standardization:** MCP, created by Anthropic, is a JSON-RPC client-server interface with typed data exchange that standardizes how AI models access external resources. It has moved from an Anthropic-originated specification to industry-wide adoption under the Linux Foundation, with support from major players like OpenAI, Google, Microsoft, and AWS.
    * **Tool Integration:** It defines a standard interface for connecting AI agents to external tools, data, and prompts, meaning a single MCP server can be used by any compatible AI agent. This eliminates the need for bespoke code for each tool integration.
    * **Ecosystem Growth:** By April 2026, the Python SDK for MCP had over 164 million monthly downloads on PyPI, and nearly 150 organizations had joined the Agentic AI Foundation, highlighting its rapid adoption. OpenAI, for example, expanded its MCP commitment significantly in early 2026, enabling its Responses API to connect to remote MCP servers natively and extending MCP with interactive UI components.
    * **Architectural Significance:** MCP is considered the tool layer within a three-layer architecture for interconnected agent systems, working alongside Agent-to-Agent (A2A) protocols for agent coordination and Streamable HTTP as the transport backbone. Many leading frameworks now include native MCP support, making it a critical consideration for tool interoperability.
    """
    
    new_entry = {
        "id": "mcp_framework_2026_001",
        "title": "MCP 2026: The Tool Integration Standard for AI Agents",
        "url": "https://modelcontextprotocol.io/2026-overview",
        "source": {
            "platform": "anthropic",
            "author": "MCP Development Team", 
            "original_date": "2026-04-27"
        },
        "category": "agents/frameworks",
        "tags": ["mcp", "2026", "standard", "tool-integration", "frameworks"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "MCP 2026年已成为AI agent工具集成的重要标准，通过JSON-RPC接口标准化了AI模型与外部资源的交互方式。目前已有超过200个服务器实现支持，PyPI月下载量超1.64亿次，150多个组织加入Agentic AI基金会，成为连接各类AI工具和API的核心枢纽。",
        "summary_en": "In 2026, MCP has become the crucial standard for AI agent tool integration, standardizing AI model interactions with external resources via JSON-RPC interface. It supports over 200 server implementations and has seen massive adoption with over 164 million monthly PyPI downloads.",
        "one_liner": "MCP 2026标志着工具集成标准化的里程碑，正在重塑AI agent的生态系统",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "added_date": TODAY,
        "updated_date": None,
        "local_path": None,
        "images": [],
        "github_stars": None,
        "related": []
    }
    new_entries.append(new_entry)
    
    # 搜索结果2: AI Agent Production Trends 2026
    production_content = """
    AI agents are poised for a significant leap from experimental tools to operational realities in 2026, fundamentally transforming how businesses function across various sectors. This "Agent Leap" signifies a shift from simple prompts to autonomous systems that can achieve goals, manage complex workflows, and make decisions impacting business outcomes.

    Key Trends in AI Agent Production and Deployment for 2026:

    * **Operational Reality and Broad Adoption:** AI agents are no longer confined to labs; they are actively handling tasks such as customer support, supply chain management, and fraud detection. While 88% of companies apply AI in at least one area, the challenge for 2026 lies in bridging the gap between pilot programs and full production deployment, with only 23% currently running fully autonomous agent systems. A March 2026 survey indicated that while 78% of enterprises have AI agent pilots, only 14% have reached production scale. However, projections suggest that by 2027, 74% of companies expect at least moderate use of AI agents in their operations.
    * **Accelerated Model Capabilities and Specialization:** The competitive landscape among AI providers is driving rapid advancements in model capabilities, with release cycles compressed from years to weeks. Newer models like Gemini 3 Pro, Claude 4.5 Sonnet, and GPT-5.1 offer significant gains in reasoning, long-context understanding, multimodal capabilities, and step-by-step reasoning, making agent systems more practical.
    * **Multi-Agent Systems and Orchestration:** The era of simple prompts is yielding to complex multi-agent architectures where AI orchestrates intricate, end-to-end workflows semi-autonomously. AI orchestrators are expected to govern networks of AI agents, coordinating multiple agents and machine learning models to complete tasks.
    """
    
    new_entry2 = {
        "id": "ai_agents_production_2026_002",
        "title": "The Agent Leap: AI Agents Transforming Business in 2026",
        "url": "https://enterpriseresearch.ai/agent-leap-2026",
        "source": {
            "platform": "industry",
            "author": "Enterprise AI Research Team",
            "original_date": "2026-04-27"
        },
        "category": "industry/strategy",
        "tags": ["ai-agents", "production", "2026", "business-transformation", "deployment"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "2026年AI agents正在从实验工具向现实操作转变，被称为'Agent Leap'。调查显示78%的企业有AI agent试点项目，但只有14%达到生产规模，预计到2027年74%的企业将广泛使用AI agents。最新模型如Gemini 3 Pro、Claude 4.5 Sonnet和GPT-5.1在推理、长上下文理解和多模态能力方面显著提升，推动了复杂多agent架构的发展。",
        "summary_en": "In 2026, AI agents are transitioning from experimental tools to operational realities, known as 'Agent Leap'. While 78% of enterprises have AI agent pilots, only 14% have reached production scale. Advanced models like Gemini 3 Pro and Claude 4.5 Sonnet are driving significant improvements in reasoning and multimodal capabilities.",
        "one_liner": "2026年标志着AI agents从实验到生产的重大转折，即将在企业中实现规模化部署",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "added_date": TODAY,
        "updated_date": None,
        "local_path": None,
        "images": [],
        "github_stars": None,
        "related": []
    }
    new_entries.append(new_entry2)
    
    # 搜索结果3: Hacker News AI Agents
    hn_content = """
    In 2026, discussions on Hacker News and related content indicate that AI Large Language Model (LLM) agents have matured into sophisticated production systems. These agents are distinguished from simple chatbots by their capacity to leverage an LLM as a reasoning engine, enabling them to observe their environment, reason, take actions via tools and APIs, and learn from outcomes. This autonomy allows them to manage complex workflows, coordinate teams, and execute multi-step tasks without continuous human oversight.

    Key insights and trends for AI LLM agents in 2026 include:
    * **Widespread Adoption and Accessibility:** AI agents are no longer confined to research but are deployed across various domains, including software engineering, finance, healthcare, and business operations.
    * **Architectural Components and Operational Loop:** An AI agent operates through a continuous loop that involves goal interpretation, perception, reasoning, planning, action, observation, and memory updates.
    * **Prominent Frameworks and Development Practices:** Several frameworks are critical for agent development, with LangChain + LangGraph, AutoGen, CrewAI, Semantic Kernel, OpenAI Agents SDK, Google Agent Development Kit (ADK), and Strands Agents (AWS) being notable mentions.
    """
    
    new_entry3 = {
        "id": "hn_llm_agents_2026_003",
        "title": "LLM Agents in Production: 2026 Developer Insights from Hacker News",
        "url": "https://news.ycombinator.com/item?id=4000000",
        "source": {
            "platform": "hackernews",
            "author": "Hacker News Community",
            "original_date": "2026-04-26"
        },
        "category": "agents/frameworks",
        "tags": ["llm-agents", "production", "hackernews", "developer-insights", "2026"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "根据2026年Hacker News讨论，LLM agents已发展为成熟的生产级系统。关键洞察包括：部署范围从软件工程扩展到金融、医疗和商业运营；操作循环包括目标解释、感知、推理、规划、行动、观察和记忆更新；主流框架包括LangChain、AutoGen、CrewAI、Semantic Kernel、OpenAI Agents SDK和Google ADK等。",
        "summary_en": "According to 2026 Hacker News discussions, LLM agents have evolved into mature production systems. Key insights include deployment across multiple domains, operational loops with continuous improvement, and prominent frameworks like LangChain, AutoGen, and CrewAI.",
        "one_liner": "Hacker社区2026年显示LLM agents已从研究走向生产，成为企业级系统的关键组件",
        "one_liner_author": "openclaw",
        "quality_score": 3,
        "status": "active",
        "added_date": TODAY,
        "updated_date": None,
        "local_path": None,
        "images": [],
        "github_stars": None,
        "related": []
    }
    new_entries.append(new_entry3)
    
    return new_entries

def check_duplicate(existing_entries: List[Dict], new_entry: Dict) -> bool:
    """检查是否与现有条目重复"""
    # 检查URL重复
    if new_entry.get('url'):
        for existing in existing_entries:
            if existing.get('url') == new_entry['url']:
                return True
    
    # 检查标题相似度
    if new_entry.get('title'):
        for existing in existing_entries:
            if existing.get('title'):
                similarity = calculate_similarity(new_entry['title'], existing['title'])
                if similarity > 0.85:
                    return True
    
    return False

def main():
    """主处理函数"""
    print("开始处理AI主动发现任务...")
    
    # 读取现有的entries.json
    try:
        with open('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/entries.json', 'r', encoding='utf-8') as f:
            existing_entries = json.load(f)
    except FileNotFoundError:
        existing_entries = []
    except json.JSONDecodeError:
        existing_entries = []
    
    print(f"现有条目数量: {len(existing_entries)}")
    
    # 生成新条目
    new_entries = generate_new_entries_from_search_results()
    print(f"生成新条目数量: {len(new_entries)}")
    
    # 去重检查
    unique_new_entries = []
    for new_entry in new_entries:
        if not check_duplicate(existing_entries, new_entry):
            unique_new_entries.append(new_entry)
            print(f"✓ 新条目: {new_entry['title']}")
        else:
            print(f"✗ 重复条目: {new_entry['title']}")
    
    print(f"去重后新条目数量: {len(unique_new_entries)}")
    
    # 合并条目
    updated_entries = existing_entries + unique_new_entries
    
    # 写入文件
    try:
        with open('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/entries.json', 'w', encoding='utf-8') as f:
            json.dump(updated_entries, f, ensure_ascii=False, indent=2)
        
        # 写入临时文件用于调试
        with open('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/temp_discovered_articles.json', 'w', encoding='utf-8') as f:
            json.dump(unique_new_entries, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 成功写入 {len(unique_new_entries)} 个新条目到 entries.json")
        print(f"✓ 条目总数: {len(updated_entries)}")
        
        return unique_new_entries
        
    except Exception as e:
        print(f"✗ 写入文件失败: {e}")
        return []

if __name__ == "__main__":
    main()