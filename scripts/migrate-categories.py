#!/usr/bin/env python3
"""Migrate 15 categories → 6 flat categories in entries.json"""
import json

MAPPING = {
    # 模型
    "models-providers/frontier-models": "models",
    "models-providers/open-source-models": "models",
    "models-providers/model-architecture": "models",
    "models-providers/chinese-llm": "models",
    # Agent
    "agent-frameworks/orchestration": "agents",
    "agent-frameworks/single-agent": "agents",
    "agent-frameworks/multi-agent": "agents",
    "agent-frameworks/lightweight": "agents",
    "agent-protocols/mcp": "agents",
    "agent-protocols/a2a": "agents",
    "agent-protocols/acp-other": "agents",
    "agent-protocols/tool-use": "agents",
    "agent-os/agent-os-concepts": "agents",
    "agent-os/phone-ai": "agents",
    "agent-os/desktop-agents": "agents",
    "agent-os/browser-agents": "agents",
    # AI编程
    "coding-ai/ide-editor": "coding",
    "coding-ai/cli-terminal": "coding",
    "coding-ai/review-devops": "coding",
    "coding-ai/skills-workflows": "coding",
    # 基础设施
    "benchmarks-evals/general": "infra",
    "benchmarks-evals/coding": "infra",
    "benchmarks-evals/agent": "infra",
    "benchmarks-evals/reasoning": "infra",
    "benchmarks-evals/chinese": "infra",
    "benchmarks-evals/multimodal": "infra",
    "benchmarks-evals/methodology": "infra",
    "rag-knowledge/rag-frameworks": "infra",
    "rag-knowledge/vector-db": "infra",
    "rag-knowledge/knowledge-graphs": "infra",
    "rag-knowledge/embedding-reranking": "infra",
    "inference-serving/inference-engines": "infra",
    "inference-serving/quantization": "infra",
    "inference-serving/on-device-edge": "infra",
    "inference-serving/serving-platforms": "infra",
    "finetuning-training/methods": "infra",
    "finetuning-training/platforms-tools": "infra",
    "finetuning-training/data": "infra",
    "multimodal-ai/vision-language": "infra",
    "multimodal-ai/image-generation": "infra",
    "multimodal-ai/video-generation": "infra",
    "multimodal-ai/audio-speech": "infra",
    "multimodal-ai/world-models": "infra",
    # 行业观察
    "ai-products/chat-assistant": "industry",
    "ai-products/search": "industry",
    "ai-products/writing-content": "industry",
    "ai-products/enterprise": "industry",
    "ai-products/vertical": "industry",
    "industry-strategy/funding-valuation": "industry",
    "industry-strategy/big-tech": "industry",
    "industry-strategy/china-ai": "industry",
    "industry-strategy/oem-device": "industry",
    "industry-strategy/regulation": "industry",
    "industry-strategy/market-analysis": "industry",
    # 学习资源
    "prompt-engineering/techniques": "learning",
    "prompt-engineering/system-prompts": "learning",
    "prompt-engineering/jailbreak-safety": "learning",
    "research-papers/architecture-scaling": "learning",
    "research-papers/alignment-safety": "learning",
    "research-papers/agents-planning": "learning",
    "research-papers/efficiency": "learning",
    "research-papers/survey-position": "learning",
    "tutorials-learning/getting-started": "learning",
    "tutorials-learning/best-practices": "learning",
    "tutorials-learning/talks-videos": "learning",
    "tutorials-learning/newsletters-blogs": "learning",
}

NEW_CATEGORIES = {
    "models": {"name": "Models", "name_zh": "模型", "icon": "🧠", "desc": "GPT / Claude / Gemini / 开源模型 / 架构"},
    "agents": {"name": "Agents", "name_zh": "智能体", "icon": "🤖", "desc": "Agent 框架 / MCP / A2A / 手机&桌面助手"},
    "coding": {"name": "Coding", "name_zh": "AI编程", "icon": "💻", "desc": "IDE / CLI / 代码审查 / 工作流"},
    "infra": {"name": "Infrastructure", "name_zh": "基础设施", "icon": "⚡", "desc": "推理部署 / RAG / 微调 / 评测 / 多模态"},
    "industry": {"name": "Industry", "name_zh": "行业观察", "icon": "🌍", "desc": "AI 产品 / 大厂战略 / 融资 / 市场分析"},
    "learning": {"name": "Learning", "name_zh": "学习资源", "icon": "📖", "desc": "教程 / 论文 / 提示工程 / 演讲"},
}

import os; os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
with open("data/entries.json", "r") as f:
    data = json.load(f)
    entries = data["entries"]

migrated = 0
unmapped = set()
for e in entries:
    old = e.get("category", "")
    if old in MAPPING:
        e["category"] = MAPPING[old]
        migrated += 1
    elif old != "uncategorized":
        unmapped.add(old)

with open("data/entries.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("metadata/categories.json", "w") as f:
    json.dump(NEW_CATEGORIES, f, ensure_ascii=False, indent=2)

print(f"Migrated: {migrated}/{len(entries)}")
if unmapped:
    print(f"Unmapped: {unmapped}")
else:
    print("No unmapped categories ✅")
