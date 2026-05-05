#!/usr/bin/env python3
"""
Generate the production God of GPT information portal.

The source of truth remains data/entries.json plus optional content/*.md files.
This script builds a polished static site into dist/ without depending on
VitePress. It also creates a cleaned display layer so scraped data quality does
not leak directly into the public UI.
"""

from __future__ import annotations

import json
import math
import re
import shutil
from collections import Counter, OrderedDict, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.parse import quote, urlparse, urlunparse


SCRIPT_PATH = Path(__file__).resolve()
BASE_DIR = SCRIPT_PATH.parent.parent
if BASE_DIR.name == "openclaw":
    candidate = BASE_DIR.parent
    if (candidate / "data" / "entries.json").exists():
        BASE_DIR = candidate

DATA_DIR = BASE_DIR / "data"
CONTENT_DIR = BASE_DIR / "content"
DIST_DIR = BASE_DIR / "dist"

SITE_NAME = "God of GPT"
SITE_TAGLINE = "每天 5 分钟，读懂 AI 圈真正值得看的变化。"
SITE_URL = "https://godofgpt.com"
BUILD_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d")


CHANNELS = OrderedDict(
    [
        (
            "brief",
            {
                "name": "今日简报",
                "short": "Brief",
                "desc": "每天最值得先看的 AI 信号。",
                "accent": "coral",
            },
        ),
        (
            "models",
            {
                "name": "模型与实验室",
                "short": "Models",
                "desc": "GPT、Claude、Gemini、开源模型、模型能力边界。",
                "accent": "cyan",
            },
        ),
        (
            "agents",
            {
                "name": "Agent 与自动化",
                "short": "Agents",
                "desc": "Agent 框架、MCP、A2A、工具调用、长期任务。",
                "accent": "violet",
            },
        ),
        (
            "coding",
            {
                "name": "AI 编程",
                "short": "Coding",
                "desc": "IDE、CLI、代码审查、工程工作流、开发者效率。",
                "accent": "green",
            },
        ),
        (
            "infra",
            {
                "name": "基础设施",
                "short": "Infra",
                "desc": "推理、RAG、微调、评测、多模态、芯片和端侧部署。",
                "accent": "amber",
            },
        ),
        (
            "business",
            {
                "name": "产品与商业",
                "short": "Business",
                "desc": "AI 产品、大厂战略、融资、监管、市场结构。",
                "accent": "blue",
            },
        ),
        (
            "research",
            {
                "name": "研究与学习",
                "short": "Research",
                "desc": "论文、课程、提示工程、长文、方法论。",
                "accent": "rose",
            },
        ),
        (
            "tools",
            {
                "name": "工具与项目",
                "short": "Tools",
                "desc": "可直接尝试的工具、开源项目、产品更新和资源库。",
                "accent": "lime",
            },
        ),
    ]
)


CHANNEL_ALIASES = {
    "models": "models",
    "models/models": "models",
    "model": "models",
    "agents": "agents",
    "agent-frameworks": "agents",
    "agent-frameworks/harness-engineering": "agents",
    "agent-frameworks/harness": "agents",
    "agent-frameworks/orchestration": "agents",
    "agent-frameworks/applications": "agents",
    "coding": "coding",
    "coding-ai": "coding",
    "coding-agents": "coding",
    "coding-ai/claude-code": "coding",
    "coding-agents/claude-code": "coding",
    "developer-tools": "coding",
    "developer-tools/browser-extensions": "coding",
    "workflow": "coding",
    "infra": "infra",
    "llm-infra": "infra",
    "llm-infra/inference-optimization": "infra",
    "llm-engineering": "infra",
    "llm-engineering/inference-optimization": "infra",
    "infrastructure": "infra",
    "hardware-chips": "infra",
    "ai-hardware": "infra",
    "multimodal": "infra",
    "industry": "business",
    "content-creation": "business",
    "strategy": "business",
    "strategy/ai-career": "business",
    "strategy/ai-product": "business",
    "ai-safety": "business",
    "ai-ux": "business",
    "learning": "research",
    "prompt": "research",
    "prompt-engineering": "research",
    "uncategorized": "tools",
    "ai-tools": "tools",
}


SOURCE_LABELS = {
    "article": "文章",
    "x_post": "X",
    "tweet": "X",
    "paper": "论文",
    "github": "GitHub",
    "product": "产品",
    "newsletter": "Newsletter",
    "video": "视频",
    "dataset": "数据集",
}


INVALID_SUMMARY_PATTERNS = (
    "cubox_url",
    "weixin/download",
    "?imageUrl=",
    "┌",
    "原文链接缺失",
)

GENERIC_PREVIEW_RE = re.compile(
    r"^(有参考价值的[\w\-/\u4e00-\u9fff]+内容|Cubox 收藏|X 链接书签|内容过短|待补充|摘要暂缺|\[需翻译\]|[\*]{3,})",
    re.I,
)
METADATA_TOKENS = (
    "source:",
    "category:",
    "feed:",
    "group:",
    "created:",
    "description:",
    "cubox_url:",
    "tags:",
)
NOISE_TAGS = {"[]", "x", "twitter", "uncategorized", "high-value", "rss"}
AI_KEYWORDS = (
    "ai",
    "aigc",
    "agent",
    "llm",
    "gpt",
    "claude",
    "gemini",
    "openai",
    "anthropic",
    "codex",
    "cursor",
    "copilot",
    "prompt",
    "rag",
    "mcp",
    "a2a",
    "model",
    "transformer",
    "diffusion",
    "neural",
    "inference",
    "fine-tuning",
    "multimodal",
    "大模型",
    "模型",
    "智能体",
    "人工智能",
    "生成式",
    "提示词",
    "推理",
    "多模态",
    "机器人",
    "算力",
    "芯片",
)


@dataclass
class Card:
    raw: dict
    id: str
    title: str
    url: str | None
    date: str
    author: str
    source_type: str
    source_label: str
    channel: str
    score: int
    tags: list[str]
    summary: str
    one_liner: str
    why: str
    audience: list[str]
    has_content: bool
    content: str
    image: str | None
    importance: float


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_url(url) -> str | None:
    if not url:
        return None
    value = str(url).strip()
    if "](" in value or value.startswith(("![](", "[")):
        return None
    if not re.match(r"^https?://", value, re.I):
        return None
    value = re.sub(r"[\x00-\x1f\x7f\s]+", "", value)
    lowered = value.lower()
    if "cubox.pro/c/filters" in lowered or "?imageurl=" in lowered:
        return None
    try:
        parsed = urlparse(value)
    except ValueError:
        return None
    if not parsed.netloc:
        return None
    return quote(value, safe="/:#?[]@!$&'()*+,;=%-._~")


def normalized_url_key(url) -> str | None:
    safe = safe_url(url)
    if not safe:
        return None
    parsed = urlparse(safe)
    host = parsed.netloc.lower()
    if host == "twitter.com":
        host = "x.com"
    return urlunparse((parsed.scheme.lower(), host, parsed.path.rstrip("/"), "", parsed.query, ""))


def has_cjk(text: str) -> bool:
    return re.search(r"[\u4e00-\u9fff]", text or "") is not None


def strip_frontmatter(text: str) -> str:
    value = text.lstrip()
    if value.startswith("---"):
        parts = value.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return value.strip()


def markdown_text(text: str) -> str:
    value = strip_frontmatter(text)
    value = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", value)
    value = re.sub(r"\[\]\s*\([^)]*(?:\)|$)", "", value)
    value = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"(?m)^#{1,6}\s+", "", value)
    value = re.sub(r"(?m)^[-*]\s+", "", value)
    value = re.sub(r"(?m)^\d+\.\s+", "", value)
    value = re.sub(r"(?m)^>\s*", "", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def clean_preview_text(text: str, *, max_len: int = 360) -> str:
    cleaned = []
    for raw_line in str(text or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"\[Read in Cubox\]\([^)]*\)", "", line)
        line = re.sub(r"\[Read Original\]\([^)]*\)", "", line)
        line = line.replace("Read in Cubox", "").replace("Read Original", "").strip()
        line = re.sub(r"^---\s*", "", line)
        line = re.sub(r"^&gt;\s*", "", line)
        line = re.sub(r"^title:\s*", "", line, flags=re.I)
        if any(pattern in line for pattern in INVALID_SUMMARY_PATTERNS):
            continue
        if line.startswith(("来源：", "- **来源**", "**English Title:**", "**Source:**")):
            continue
        cleaned.append(line)

    value = markdown_text("\n".join(cleaned))
    value = re.sub(r"https?://\S+", "", value).strip()
    if looks_like_noisy_preview(value):
        return ""
    if len(value) <= max_len:
        return value

    cutoff = max_len
    for sep in ("。", "！", "？", ". ", "; ", "；", "，"):
        pos = value.rfind(sep, 0, max_len)
        if pos >= 120:
            cutoff = pos + len(sep)
            break
    return value[:cutoff].rstrip(" ，,;；") + "..."


def looks_like_noisy_preview(text: str) -> bool:
    value = re.sub(r"\s+", " ", str(text or "")).strip()
    if not value:
        return True
    lowered = value.lower()
    if GENERIC_PREVIEW_RE.search(value):
        return True
    if value in {"[]", "****", "---"}:
        return True
    if value.startswith(("id:", "source:", "title:")):
        return True
    metadata_hits = sum(1 for token in METADATA_TOKENS if token in lowered)
    if metadata_hits >= 2:
        return True
    if "read in cubox" in lowered or "read original" in lowered:
        return True
    if any(pattern in lowered for pattern in ("__biz=", "mpshare=", "self.__next_f.push", "window.", "datalayer", "schema.org")):
        return True
    return False


def has_readable_preview(text: str) -> bool:
    value = clean_preview_text(text, max_len=320)
    if not value or looks_like_noisy_preview(value):
        return False
    if len(value) < 24 and not has_cjk(value):
        return False
    if len(value) < 16:
        return False
    return True


def normalized_preview(value: str) -> str:
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", str(value or "").lower())


def is_title_echo(title: str, preview: str) -> bool:
    title_key = normalized_preview(title)
    preview_key = normalized_preview(preview)
    if not title_key or not preview_key:
        return False
    if len(preview) > len(title) + 36:
        return False
    return title_key in preview_key or preview_key in title_key


def is_low_signal_entry(entry: dict) -> bool:
    title = str(entry.get("title") or "")
    summary = str(entry.get("summary_zh") or "")
    summary_en = str(entry.get("summary_en") or "")
    one_liner = str(entry.get("one_liner") or "")
    tags = {str(tag).lower() for tag in entry.get("tags", [])}
    return (
        title.startswith("高价值AI内容 -")
        or one_liner.startswith("高价值AI内容 -")
        or re.match(r"^来自@[^，。\s]+的高价值AI相关内容", summary) is not None
        or summary_en.startswith("High-value AI content from @")
        or ("high-value" in tags and len(summary) < 50)
    )


def is_displayable_entry(entry: dict) -> bool:
    if is_low_signal_entry(entry):
        return False
    if not is_ai_related_entry(entry):
        return False

    title = clean_preview_text(entry.get("title") or "", max_len=120)
    if not title or title in {"原始推文", "Untitled"}:
        return False

    summary = entry.get("summary_zh") or entry.get("summary_en") or ""
    one_liner = entry.get("one_liner") or ""
    content = content_body_for(entry)
    summary_clean = clean_preview_text(summary, max_len=320)
    if summary_clean and not is_title_echo(title, summary_clean) and has_readable_preview(summary_clean):
        return True
    if has_readable_preview(content):
        return True
    one_liner_clean = clean_preview_text(one_liner, max_len=160)
    if int(entry.get("quality_score") or 0) >= 4 and one_liner_clean and not is_title_echo(title, one_liner_clean) and has_readable_preview(one_liner_clean):
        return True
    return False


def is_ai_related_entry(entry: dict) -> bool:
    fields = [
        entry.get("title") or "",
        entry.get("summary_zh") or "",
        entry.get("summary_en") or "",
        entry.get("one_liner") or "",
        entry.get("category") or "",
        " ".join(str(tag) for tag in entry.get("tags", []) or []),
    ]
    haystack = " ".join(fields).lower()
    return any(keyword in haystack for keyword in AI_KEYWORDS)


def content_path_for(entry: dict) -> Path | None:
    entry_id = entry.get("id")
    if not entry_id:
        return None
    path = CONTENT_DIR / f"{entry_id}.md"
    return path if path.exists() else None


def content_body_for(entry: dict) -> str:
    path = content_path_for(entry)
    if not path:
        return ""
    try:
        return strip_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return ""


def good_external_image(url) -> str | None:
    safe = safe_url(url)
    if not safe:
        return None
    lowered = safe.lower()
    if "cubox.pro/c/filters" in lowered:
        return None
    if lowered.endswith((".svg", ".gif")):
        return None
    if not any(ext in lowered for ext in (".jpg", ".jpeg", ".png", ".webp", "pbs.twimg.com", "images.unsplash.com")):
        return None
    return safe


def first_image(entry: dict) -> str | None:
    for image in entry.get("images", []) or []:
        good = good_external_image(image)
        if good:
            return good
    return None


def parse_date(value: str) -> datetime:
    if not value:
        return datetime(1970, 1, 1)
    for fmt, size in (("%Y-%m-%d", 10), ("%Y-%m", 7), ("%Y", 4)):
        try:
            parsed = datetime.strptime(value[:size], fmt)
            return parsed
        except ValueError:
            continue
    return datetime(1970, 1, 1)


def entry_date(entry: dict) -> str:
    source = entry.get("source") or {}
    return entry.get("published_date") or source.get("original_date") or entry.get("added_date") or ""


def channel_for(entry: dict) -> str:
    raw_category = str(entry.get("category") or "").strip()
    prefix = raw_category.split("/", 1)[0]
    tags = {str(tag).lower() for tag in entry.get("tags", [])}
    source_type = entry.get("source_type")

    if tags & {"codex", "claude-code", "cursor", "ide", "coding", "vibe-coding"}:
        return "coding"
    if tags & {"agent", "mcp", "a2a", "harness"}:
        return "agents"
    if tags & {"model", "llm", "open-source", "qwen", "gemini", "claude", "gpt", "embedding", "multimodal"}:
        return "models"
    if tags & {"ai-product", "product", "startup", "market", "business"}:
        return "business"
    if raw_category in CHANNEL_ALIASES:
        return CHANNEL_ALIASES[raw_category]
    if prefix in CHANNEL_ALIASES:
        return CHANNEL_ALIASES[prefix]
    if source_type == "paper":
        return "research"
    if source_type in {"github", "product", "dataset"}:
        return "tools"
    return "tools"


def infer_audience(entry: dict, channel: str) -> list[str]:
    tags = {str(tag).lower() for tag in entry.get("tags", [])}
    title = str(entry.get("title") or "").lower()
    audiences = []
    if channel in {"coding", "infra", "agents", "tools"} or tags & {"developer-tools", "coding", "github", "api"}:
        audiences.append("开发者")
    if channel in {"business", "tools"} or tags & {"product", "startup", "strategy", "market"}:
        audiences.append("产品/创业")
    if channel in {"models", "research"} or tags & {"paper", "research", "benchmark", "safety"}:
        audiences.append("研究者")
    if "course" in tags or "tutorial" in tags or "learning" in tags or "课程" in title:
        audiences.append("学习者")
    if not audiences:
        audiences.append("AI 从业者")
    return audiences[:3]


def derive_why(entry: dict, summary: str, one_liner: str, channel: str) -> str:
    if one_liner and not is_low_signal_entry(entry):
        return clean_preview_text(one_liner, max_len=140)
    if summary:
        first_sentence = re.split(r"(?<=[。！？.!?])\s*", summary)[0]
        if len(first_sentence) >= 18:
            return clean_preview_text(first_sentence, max_len=140)
    channel_name = CHANNELS.get(channel, {}).get("name", "AI")
    return f"这条内容提供了 {channel_name} 方向的新增信号，适合纳入近期观察。"


def entry_rank(entry: dict) -> tuple:
    content = content_body_for(entry)
    summary = clean_preview_text(entry.get("summary_zh") or entry.get("summary_en") or "", max_len=260)
    return (
        1 if is_displayable_entry(entry) else 0,
        1 if has_cjk(summary) and len(summary) >= 40 else 0,
        1 if content else 0,
        0 if any(pattern in str(entry.get("summary_zh") or "")[:300] for pattern in INVALID_SUMMARY_PATTERNS) else 1,
        int(entry.get("quality_score") or 0),
        len(summary),
        entry_date(entry),
        str(entry.get("id") or ""),
    )


def dedupe_entries(entries: list[dict]) -> list[dict]:
    grouped = OrderedDict()
    for entry in entries:
        key = normalized_url_key(entry.get("url")) or f"id:{entry.get('id')}"
        grouped.setdefault(key, []).append(entry)
    return [max(group, key=entry_rank) for group in grouped.values()]


def card_from_entry(entry: dict) -> Card:
    channel = channel_for(entry)
    content = content_body_for(entry)
    title = clean_preview_text(entry.get("title") or "Untitled", max_len=96)
    raw_summary = entry.get("summary_zh") or entry.get("summary_en") or ""
    summary = clean_preview_text(raw_summary, max_len=380)
    one_liner = clean_preview_text(entry.get("one_liner") or "", max_len=160)
    if is_title_echo(title, summary):
        summary = ""

    if (not summary or len(summary) < 30 or not has_cjk(summary)) and one_liner and has_readable_preview(one_liner):
        summary = one_liner
    if (not summary or len(summary) < 30) and content:
        content_summary = clean_preview_text(content, max_len=380)
        if content_summary:
            summary = content_summary
    if not summary:
        summary = "内容摘要暂缺，保留为资料索引。"

    date = entry_date(entry)
    score = int(entry.get("quality_score") or 0)
    source_type = str(entry.get("source_type") or "article")
    source = entry.get("source") or {}
    date_age = max((datetime.now() - parse_date(date)).days, 0)
    recency = max(0, 30 - min(date_age, 30)) / 30
    importance = score * 10 + recency * 6 + (4 if content else 0)
    if source_type in {"paper", "github", "product"}:
        importance += 2
    if is_low_signal_entry(entry):
        importance -= 30

    return Card(
        raw=entry,
        id=str(entry.get("id")),
        title=title,
        url=safe_url(entry.get("url")),
        date=date,
        author=clean_preview_text(source.get("author") or "", max_len=80),
        source_type=source_type,
        source_label=SOURCE_LABELS.get(source_type, source_type or "来源"),
        channel=channel,
        score=score,
        tags=[
            tag
            for tag in (clean_preview_text(raw_tag, max_len=28) for raw_tag in (entry.get("tags") or []))
            if tag and tag.lower() not in NOISE_TAGS
        ][:8],
        summary=summary,
        one_liner=one_liner,
        why=derive_why(entry, summary, one_liner, channel),
        audience=infer_audience(entry, channel),
        has_content=bool(content),
        content=content,
        image=first_image(entry),
        importance=importance,
    )


def sort_cards(cards: list[Card]) -> list[Card]:
    return sorted(cards, key=lambda c: (parse_date(c.date), c.importance, c.title), reverse=True)


def escape_attr(value: str) -> str:
    return escape(value or "", quote=True)


def link(path: str) -> str:
    return path


def card_url(card: Card) -> str:
    return f"/entry/{quote(card.id)}/"


def render_tags(tags: list[str], limit: int = 5) -> str:
    return "".join(f'<span class="tag">{escape(tag)}</span>' for tag in tags[:limit])


def render_score(score: int) -> str:
    label = {5: "必读", 4: "优秀", 3: "值得看"}.get(score, "参考")
    return f'<span class="score score-{score}">{score}.0 · {label}</span>'


def render_mini_card(card: Card, *, show_channel: bool = False) -> str:
    channel = CHANNELS[card.channel]
    meta = [
        escape(card.date or "未知日期"),
        escape(card.source_label),
    ]
    if card.author:
        meta.append(escape(card.author.lstrip("@")))
    channel_badge = f'<span class="channel-pill {channel["accent"]}">{escape(channel["short"])}</span>' if show_channel else ""
    return f"""
    <article class="mini-card">
      <div class="mini-card__top">
        {channel_badge}
        {render_score(card.score)}
      </div>
      <a class="mini-card__title" href="{card_url(card)}">{escape(card.title)}</a>
      <p>{escape(card.summary)}</p>
      <div class="meta-line">{' · '.join(meta)}</div>
    </article>
    """


def render_feature_card(card: Card, index: int) -> str:
    channel = CHANNELS[card.channel]
    image = ""
    if card.image:
        image = f'<img src="{escape_attr(card.image)}" alt="" loading="lazy">'
    else:
        image = f'<div class="signal-visual {channel["accent"]}"><span>{index:02d}</span><b>{escape(channel["short"])}</b></div>'
    return f"""
    <article class="feature-card">
      <a class="feature-card__media" href="{card_url(card)}">{image}</a>
      <div class="feature-card__body">
        <div class="eyebrow-row">
          <span class="channel-pill {channel["accent"]}">{escape(channel["name"])}</span>
          {render_score(card.score)}
        </div>
        <a class="feature-card__title" href="{card_url(card)}">{escape(card.title)}</a>
        <p>{escape(card.summary)}</p>
        <div class="why-box"><b>为什么重要</b><span>{escape(card.why)}</span></div>
        <div class="meta-line">{escape(card.date or "未知日期")} · {escape(card.source_label)}{(" · " + escape(card.author)) if card.author else ""}</div>
      </div>
    </article>
    """


def render_list_item(card: Card) -> str:
    channel = CHANNELS[card.channel]
    return f"""
    <article class="list-item">
      <div>
        <div class="eyebrow-row">
          <span class="channel-pill {channel["accent"]}">{escape(channel["short"])}</span>
          <span class="meta-line">{escape(card.date or "未知日期")} · {escape(card.source_label)}</span>
        </div>
        <a href="{card_url(card)}" class="list-item__title">{escape(card.title)}</a>
        <p>{escape(card.summary)}</p>
        <div class="tag-row">{render_tags(card.tags, 6)}</div>
      </div>
      <div class="list-item__side">
        {render_score(card.score)}
        <span>{escape(" / ".join(card.audience))}</span>
      </div>
    </article>
    """


def markdown_inline(text: str) -> str:
    links = []
    text = re.sub(r"!\[[^\]]*\]\([^)]*(?:\)|$)", "", text)

    def markdown_link_repl(match):
        label = match.group(1).strip() or match.group(2).strip()
        url = safe_url(match.group(2).strip())
        if not url:
            return label
        placeholder = f"@@LINK{len(links)}@@"
        links.append(f'<a href="{escape_attr(url)}" target="_blank" rel="noopener">{escape(label)}</a>')
        return placeholder

    text = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", markdown_link_repl, text)
    value = escape(text)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)

    def repl(match):
        url = safe_url(match.group(0))
        if not url:
            return match.group(0)
        return f'<a href="{escape_attr(url)}" target="_blank" rel="noopener">{escape(match.group(0))}</a>'

    value = re.sub(r"https?://[^\s<]+", repl, value)
    for index, html_link in enumerate(links):
        value = value.replace(f"@@LINK{index}@@", html_link)
    return value


def clean_detail_markdown(markdown: str) -> str:
    cleaned = []
    skip_table = False
    for raw in strip_frontmatter(markdown).splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            skip_table = False
            cleaned.append("")
            continue
        if stripped.startswith("![") or stripped.startswith("![]("):
            continue
        if any(pattern in stripped.lower() for pattern in ("self.__next_f.push", "window._", "datadog-rum", "dangerouslysetinnerhtml")):
            continue
        line = re.sub(r"!\[[^\]]*\]\([^)]*(?:\)|$)", "", line).rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        if any(pattern in stripped for pattern in ("cubox.pro/c/filters", "?imageUrl=", "cubox_url")):
            continue
        if "Read in Cubox" in stripped or "Read Original" in stripped:
            continue
        if "weixin/download" in stripped:
            skip_table = True
            continue
        if skip_table and ("│" in stripped or "┌" in stripped or "└" in stripped or "├" in stripped):
            continue
        if stripped.startswith(("来源：", "- **来源**：")) and "原文链接" in stripped:
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def markdown_to_html(markdown: str) -> str:
    body = clean_detail_markdown(markdown)
    lines = body.splitlines()
    html = []
    para = []
    in_code = False
    code = []
    list_items = []

    def flush_para():
        nonlocal para
        if para:
            text = " ".join(x.strip() for x in para if x.strip())
            if text:
                html.append(f"<p>{markdown_inline(text)}</p>")
            para = []

    def flush_list():
        nonlocal list_items
        if list_items:
            html.append("<ul>" + "".join(f"<li>{markdown_inline(item)}</li>" for item in list_items) + "</ul>")
            list_items = []

    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith("```"):
            if in_code:
                html.append(f"<pre><code>{escape(chr(10).join(code))}</code></pre>")
                code = []
                in_code = False
            else:
                flush_para()
                flush_list()
                in_code = True
            continue
        if in_code:
            code.append(line)
            continue
        stripped = line.strip()
        if not stripped:
            flush_para()
            flush_list()
            continue
        if stripped.startswith("#"):
            flush_para()
            flush_list()
            level = min(len(stripped) - len(stripped.lstrip("#")) + 1, 4)
            text = stripped.lstrip("#").strip()
            if text:
                html.append(f"<h{level}>{markdown_inline(text)}</h{level}>")
            continue
        if stripped.startswith(">"):
            flush_para()
            flush_list()
            html.append(f"<blockquote>{markdown_inline(stripped.lstrip('>').strip())}</blockquote>")
            continue
        m = re.match(r"^[-*]\s+(.+)$", stripped)
        if m:
            flush_para()
            list_items.append(m.group(1))
            continue
        if stripped.startswith(("---", "Read in Cubox", "Read Original")):
            continue
        para.append(stripped)

    flush_para()
    flush_list()
    if in_code and code:
        html.append(f"<pre><code>{escape(chr(10).join(code))}</code></pre>")
    return "\n".join(html)


def page_shell(title: str, body: str, *, description: str = SITE_TAGLINE, active: str = "") -> str:
    nav = [
        ("首页", "/", "home"),
        ("频道", "/channels/", "channels"),
        ("专题", "/topics/", "topics"),
        ("归档", "/archive/", "archive"),
        ("赞助", "/sponsor/", "sponsor"),
    ]
    nav_html = "".join(
        f'<a class="{ "active" if key == active else "" }" href="{href}">{label}</a>'
        for label, href, key in nav
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} · {SITE_NAME}</title>
  <meta name="description" content="{escape_attr(description)}">
  <meta property="og:title" content="{escape_attr(title)} · {SITE_NAME}">
  <meta property="og:description" content="{escape_attr(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_URL}">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
  <header class="site-header">
    <a class="brand" href="/" aria-label="{SITE_NAME}">
      <span class="brand-mark">GG</span>
      <span><b>{SITE_NAME}</b><em>AI 信息导航</em></span>
    </a>
    <nav class="site-nav">{nav_html}</nav>
    <button class="search-trigger" type="button" data-open-search>搜索</button>
  </header>
  <main>{body}</main>
  <footer class="site-footer">
    <div>
      <b>{SITE_NAME}</b>
      <p>由 OpenClaw 自动采集、清洗、去重、归类；人工口径是：少一点噪音，多一点判断。</p>
    </div>
    <div class="footer-links">
      <a href="/archive/">全部归档</a>
      <a href="/sponsor/">赞助合作</a>
      <a href="https://github.com/Gracker/awesome-ai-field-notes">GitHub</a>
    </div>
  </footer>
  <div class="search-modal" data-search-modal hidden>
    <div class="search-panel">
      <div class="search-panel__head">
        <input type="search" placeholder="搜索模型、Agent、公司、工具..." data-search-input>
        <button type="button" data-close-search>关闭</button>
      </div>
      <div class="search-results" data-search-results></div>
    </div>
  </div>
  <script src="/assets/app.js" defer></script>
</body>
</html>
"""


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def pick_daily(cards: list[Card]) -> list[Card]:
    recent = sort_cards(cards)
    selected = []
    seen_channels = set()
    for card in recent:
        if card.score < 3 or is_low_signal_entry(card.raw):
            continue
        if card.channel not in seen_channels or len(selected) >= 4:
            selected.append(card)
            seen_channels.add(card.channel)
        if len(selected) == 7:
            break
    return selected


def week_cards(cards: list[Card], days: int = 10) -> list[Card]:
    latest_date = max(parse_date(card.date) for card in cards)
    return [card for card in cards if (latest_date - parse_date(card.date)).days <= days]


def render_home(cards: list[Card], stats: dict, tag_counts: Counter):
    daily = pick_daily(cards)
    lead = daily[0]
    channel_cards = {slug: sort_cards([card for card in cards if card.channel == slug])[:4] for slug in CHANNELS if slug != "brief"}
    deep_reads = [
        card
        for card in sort_cards(cards)
        if card.score >= 4 and card.source_type in {"article", "paper", "github"} and card.channel in {"research", "agents", "coding", "infra", "business"}
    ][:8]
    tools = [card for card in sort_cards(cards) if card.channel == "tools" or card.source_type in {"github", "product"}][:8]
    trending_tags = [tag for tag, _ in tag_counts.most_common(18)]

    brief_items = "".join(render_mini_card(card, show_channel=True) for card in daily[1:7])
    channel_html = ""
    for slug, info in CHANNELS.items():
        if slug == "brief":
            continue
        items = channel_cards.get(slug, [])
        channel_html += f"""
        <section class="channel-block {info["accent"]}">
          <div class="section-head">
            <div><span>{escape(info["short"])}</span><h2>{escape(info["name"])}</h2></div>
            <a href="/channel/{slug}/">进入频道</a>
          </div>
          <p class="section-desc">{escape(info["desc"])}</p>
          <div class="compact-list">{''.join(render_mini_card(card) for card in items[:3])}</div>
        </section>
        """

    trend_html = "".join(f'<a href="/topics/#{quote(tag)}">{escape(tag)}</a>' for tag in trending_tags)
    deep_html = "".join(render_list_item(card) for card in deep_reads)
    tool_html = "".join(render_mini_card(card, show_channel=True) for card in tools)

    body = f"""
    <section class="hero-dashboard">
      <div class="hero-copy">
        <div class="kicker">AI Intelligence Navigator · {escape(BUILD_DATE)}</div>
        <h1>每天 5 分钟，知道 AI 圈真正值得看的变化。</h1>
        <p>{SITE_TAGLINE} 这里不是原始链接仓库，而是经过清洗、去重、归类和价值判断的 AI 信息导航站。</p>
        <div class="hero-actions">
          <a class="button primary" href="#today">看今日要闻</a>
          <a class="button secondary" href="/archive/">浏览全部资料</a>
        </div>
      </div>
      <div class="signal-board" aria-label="站点数据概览">
        <div><b>{stats["cards"]}</b><span>精选条目</span></div>
        <div><b>{stats["content"]}</b><span>全文备份</span></div>
        <div><b>{stats["channels"]}</b><span>主题频道</span></div>
        <div><b>{stats["week"]}</b><span>近期信号</span></div>
      </div>
    </section>

    <section id="today" class="today-grid">
      <article class="lead-card">
        <div class="eyebrow-row">
          <span class="channel-pill {CHANNELS[lead.channel]["accent"]}">{escape(CHANNELS[lead.channel]["name"])}</span>
          {render_score(lead.score)}
        </div>
        <a href="{card_url(lead)}"><h2>{escape(lead.title)}</h2></a>
        <p>{escape(lead.summary)}</p>
        <div class="why-box"><b>先看它的理由</b><span>{escape(lead.why)}</span></div>
        <div class="tag-row">{render_tags(lead.tags)}</div>
      </article>
      <div class="brief-stack">
        <div class="section-head tight"><div><span>Today</span><h2>今日要闻</h2></div><a href="/channel/brief/">更多</a></div>
        {brief_items}
      </div>
    </section>

    <section class="ad-slot">
      <div>
        <span>Sponsored slot</span>
        <b>预留赞助位</b>
        <p>只接受与 AI 工具、开发者服务、学习资源相关的赞助，并会明确标注。</p>
      </div>
      <a href="/sponsor/">了解合作方式</a>
    </section>

    <section class="channel-grid">
      {channel_html}
    </section>

    <section class="two-column">
      <div>
        <div class="section-head"><div><span>Deep Reads</span><h2>深度阅读</h2></div><a href="/archive/?type=article">全部</a></div>
        <div class="list-stack">{deep_html}</div>
      </div>
      <aside>
        <div class="section-head"><div><span>Watchlist</span><h2>趋势标签</h2></div><a href="/topics/">专题</a></div>
        <div class="topic-cloud">{trend_html}</div>
        <div class="section-head spacer"><div><span>Tools</span><h2>工具与项目</h2></div><a href="/channel/tools/">更多</a></div>
        <div class="compact-list">{tool_html}</div>
      </aside>
    </section>
    """
    return page_shell("首页", body, active="home")


def render_channels_index(cards: list[Card]):
    blocks = ""
    for slug, info in CHANNELS.items():
        if slug == "brief":
            continue
        items = sort_cards([card for card in cards if card.channel == slug])
        blocks += f"""
        <a class="directory-card {info["accent"]}" href="/channel/{slug}/">
          <span>{escape(info["short"])}</span>
          <h2>{escape(info["name"])}</h2>
          <p>{escape(info["desc"])}</p>
          <b>{len(items)} 条</b>
        </a>
        """
    body = f"""
    <section class="page-hero">
      <span>Channels</span>
      <h1>按使用场景重新组织 AI 信息</h1>
      <p>频道不是原始分类，而是面向读者的稳定入口。模型、Agent、编程、基础设施、商业、研究和工具各自承载不同阅读任务。</p>
    </section>
    <section class="directory-grid">{blocks}</section>
    """
    return page_shell("频道", body, active="channels")


def render_channel_page(slug: str, cards: list[Card]):
    info = CHANNELS[slug]
    items = sort_cards([card for card in cards if card.channel == slug])
    top = items[:3]
    rest = items[3:]
    body = f"""
    <section class="page-hero {info["accent"]}">
      <span>{escape(info["short"])}</span>
      <h1>{escape(info["name"])}</h1>
      <p>{escape(info["desc"])}</p>
      <div class="hero-metrics"><b>{len(items)}</b><span>精选条目</span></div>
    </section>
    <section class="feature-grid">
      {''.join(render_feature_card(card, index + 1) for index, card in enumerate(top))}
    </section>
    <section class="list-stack archive-list">
      {''.join(render_list_item(card) for card in rest)}
    </section>
    """
    return page_shell(info["name"], body, active="channels")


def render_entry_page(card: Card, related: list[Card]):
    channel = CHANNELS[card.channel]
    content = card.content
    content_html = markdown_to_html(content) if content else f"<p>{escape(card.summary)}</p>"
    source_link = f'<a class="button secondary" href="{escape_attr(card.url)}" target="_blank" rel="noopener">打开原文</a>' if card.url else ""
    image = f'<img class="entry-image" src="{escape_attr(card.image)}" alt="" loading="lazy">' if card.image else ""
    related_html = "".join(render_mini_card(item, show_channel=True) for item in related[:4])
    audience = "".join(f"<span>{escape(item)}</span>" for item in card.audience)
    body = f"""
    <article class="entry-layout">
      <header class="entry-header">
        <div class="eyebrow-row">
          <a class="channel-pill {channel["accent"]}" href="/channel/{card.channel}/">{escape(channel["name"])}</a>
          {render_score(card.score)}
          <span class="meta-line">{escape(card.date or "未知日期")} · {escape(card.source_label)}</span>
        </div>
        <h1>{escape(card.title)}</h1>
        <p>{escape(card.summary)}</p>
        <div class="entry-actions">{source_link}<a class="button secondary" href="/archive/">回到归档</a></div>
      </header>
      <aside class="entry-aside">
        <div class="why-box"><b>为什么重要</b><span>{escape(card.why)}</span></div>
        <div class="audience-box"><b>适合谁看</b><div>{audience}</div></div>
        <div class="tag-row">{render_tags(card.tags, 8)}</div>
      </aside>
      <section class="entry-content">
        {image}
        {content_html}
      </section>
      <section class="related-block">
        <div class="section-head"><div><span>Related</span><h2>继续阅读</h2></div></div>
        <div class="compact-list related-grid">{related_html}</div>
      </section>
    </article>
    """
    return page_shell(card.title, body, description=card.summary, active="")


def render_archive(cards: list[Card]):
    items = "".join(render_list_item(card) for card in sort_cards(cards))
    filters = "".join(
        f'<a href="/channel/{slug}/">{escape(info["name"])}</a>'
        for slug, info in CHANNELS.items()
        if slug != "brief"
    )
    body = f"""
    <section class="page-hero">
      <span>Archive</span>
      <h1>全部 AI 信息索引</h1>
      <p>这里保留全部经过展示层清洗和去重后的条目。搜索适合精确查找，频道适合日常浏览。</p>
      <div class="filter-links">{filters}</div>
    </section>
    <section class="list-stack archive-list">{items}</section>
    """
    return page_shell("归档", body, active="archive")


def render_topics(cards: list[Card], tag_counts: Counter):
    clusters = ""
    for tag, count in tag_counts.most_common(36):
        tagged = [card for card in sort_cards(cards) if tag in card.tags][:4]
        clusters += f"""
        <section class="topic-section" id="{escape_attr(tag)}">
          <div class="section-head">
            <div><span>{count} 条</span><h2>{escape(tag)}</h2></div>
          </div>
          <div class="compact-list">{''.join(render_mini_card(card, show_channel=True) for card in tagged)}</div>
        </section>
        """
    body = f"""
    <section class="page-hero">
      <span>Topics</span>
      <h1>从标签进入专题阅读</h1>
      <p>专题页用于积累长期价值：同一模型、同一工具、同一方法论会逐步聚合为可持续更新的阅读路径。</p>
    </section>
    <section class="topic-layout">{clusters}</section>
    """
    return page_shell("专题", body, active="topics")


def render_sponsor():
    body = """
    <section class="page-hero">
      <span>Sponsor</span>
      <h1>赞助位会服务读者，而不是打断读者</h1>
      <p>God of GPT 未来会开放少量赞助位置，只接受与 AI 工具、开发者服务、云基础设施、学习资源相关的合作。所有赞助内容都会明确标注。</p>
    </section>
    <section class="sponsor-grid">
      <article>
        <h2>适合投放</h2>
        <p>AI 编程工具、模型 API、Agent 平台、开发者基础设施、课程与研究资源。</p>
      </article>
      <article>
        <h2>不会接受</h2>
        <p>与 AI 无关、夸大收益、无法验证、影响读者判断的广告内容。</p>
      </article>
      <article>
        <h2>位置规划</h2>
        <p>首页一个低侵入 sponsor slot，频道页一个主题赞助位，Newsletter 预留一期合作位。</p>
      </article>
    </section>
    """
    return page_shell("赞助合作", body, active="sponsor")


def related_for(card: Card, cards: list[Card]) -> list[Card]:
    tag_set = set(card.tags)
    scored = []
    for other in cards:
        if other.id == card.id:
            continue
        overlap = len(tag_set & set(other.tags))
        score = overlap * 8 + (5 if other.channel == card.channel else 0) + other.score
        if score > 0:
            scored.append((score, other))
    return [item for _, item in sorted(scored, key=lambda pair: (pair[0], parse_date(pair[1].date)), reverse=True)]


def build_search_data(cards: list[Card]):
    return [
        {
            "id": card.id,
            "title": card.title,
            "summary": card.summary,
            "channel": CHANNELS[card.channel]["name"],
            "tags": card.tags,
            "date": card.date,
            "url": card_url(card),
        }
        for card in cards
    ]


def build_site():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    (DIST_DIR / "assets").mkdir(parents=True, exist_ok=True)

    data = load_json(DATA_DIR / "entries.json")
    entries = data.get("entries", data) if isinstance(data, dict) else data
    active_raw = [
        entry
        for entry in entries
        if entry.get("status") == "active" and int(entry.get("quality_score") or 0) >= 3
    ]
    display_entries = dedupe_entries(active_raw)
    cards = sort_cards([card_from_entry(entry) for entry in display_entries if is_displayable_entry(entry)])

    tag_counts = Counter()
    for card in cards:
        tag_counts.update(card.tags)

    recent = week_cards(cards)
    stats = {
        "raw": len(entries),
        "cards": len(cards),
        "content": sum(1 for card in cards if card.has_content),
        "channels": len(CHANNELS) - 1,
        "week": len(recent),
    }

    write_text(DIST_DIR / "index.html", render_home(cards, stats, tag_counts))
    write_text(DIST_DIR / "channels" / "index.html", render_channels_index(cards))
    for slug in CHANNELS:
        if slug == "brief":
            continue
        write_text(DIST_DIR / "channel" / slug / "index.html", render_channel_page(slug, cards))
    write_text(DIST_DIR / "archive" / "index.html", render_archive(cards))
    write_text(DIST_DIR / "topics" / "index.html", render_topics(cards, tag_counts))
    write_text(DIST_DIR / "sponsor" / "index.html", render_sponsor())

    for card in cards:
        write_text(DIST_DIR / "entry" / card.id / "index.html", render_entry_page(card, related_for(card, cards)))

    write_text(DIST_DIR / "assets" / "style.css", build_css())
    write_text(DIST_DIR / "assets" / "app.js", build_js())
    write_text(
        DIST_DIR / "assets" / "search-data.json",
        json.dumps(build_search_data(cards), ensure_ascii=False, separators=(",", ":")),
    )
    write_text(DIST_DIR / "assets" / "favicon.svg", build_favicon())
    write_text(DIST_DIR / "robots.txt", "User-agent: *\nAllow: /\nSitemap: https://godofgpt.com/sitemap.xml\n")
    sitemap = "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            f"<url><loc>{SITE_URL}/</loc></url>",
            *[f"<url><loc>{SITE_URL}/channel/{slug}/</loc></url>" for slug in CHANNELS if slug != "brief"],
            *[f"<url><loc>{SITE_URL}/entry/{card.id}/</loc></url>" for card in cards],
            "</urlset>",
        ]
    )
    write_text(DIST_DIR / "sitemap.xml", sitemap)
    write_text(
        DIST_DIR / "site-stats.json",
        json.dumps({"generated_at": datetime.now().isoformat(), **stats}, ensure_ascii=False, indent=2),
    )
    for junk in DIST_DIR.rglob(".DS_Store"):
        junk.unlink(missing_ok=True)
    print(f"✅ Modern site generated: {len(cards)} display cards, {stats['content']} content pages, {len(CHANNELS) - 1} channels")


def build_favicon() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#111318"/>
  <path d="M17 20c3-5 8-8 15-8 6 0 11 2 15 6l-5 6c-3-3-6-4-10-4-7 0-12 5-12 12s5 12 12 12c3 0 6-1 8-3v-6h-10v-7h18v17c-4 4-10 7-17 7-8 0-14-3-18-8-4-6-4-17 0-24Z" fill="#73d2de"/>
  <path d="M43 16h7v33h-7V16Z" fill="#f4b860"/>
</svg>"""


def build_js() -> str:
    return r"""
const modal = document.querySelector('[data-search-modal]');
const input = document.querySelector('[data-search-input]');
const results = document.querySelector('[data-search-results]');
let searchData = [];

async function ensureData() {
  if (searchData.length) return;
  const res = await fetch('/assets/search-data.json');
  searchData = await res.json();
}

function openSearch() {
  modal.hidden = false;
  document.body.classList.add('search-open');
  ensureData().then(() => {
    input.focus();
    renderResults('');
  });
}

function closeSearch() {
  modal.hidden = true;
  document.body.classList.remove('search-open');
}

function scoreItem(item, terms) {
  const haystack = `${item.title} ${item.summary} ${item.channel} ${(item.tags || []).join(' ')}`.toLowerCase();
  let score = 0;
  for (const term of terms) {
    if (!haystack.includes(term)) return 0;
    if (item.title.toLowerCase().includes(term)) score += 8;
    if ((item.tags || []).join(' ').toLowerCase().includes(term)) score += 4;
    score += 1;
  }
  return score;
}

function renderResults(query) {
  const terms = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const items = terms.length
    ? searchData.map(item => [scoreItem(item, terms), item]).filter(([score]) => score > 0).sort((a, b) => b[0] - a[0]).slice(0, 30).map(([, item]) => item)
    : searchData.slice(0, 16);
  results.innerHTML = items.map(item => `
    <a class="search-result" href="${item.url}">
      <span>${item.channel} · ${item.date || ''}</span>
      <b>${item.title}</b>
      <p>${item.summary || ''}</p>
    </a>
  `).join('') || '<p class="empty-state">没有找到匹配内容。</p>';
}

document.querySelectorAll('[data-open-search]').forEach(btn => btn.addEventListener('click', openSearch));
document.querySelectorAll('[data-close-search]').forEach(btn => btn.addEventListener('click', closeSearch));
modal?.addEventListener('click', event => {
  if (event.target === modal) closeSearch();
});
input?.addEventListener('input', event => renderResults(event.target.value));
document.addEventListener('keydown', event => {
  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
    event.preventDefault();
    openSearch();
  }
  if (event.key === 'Escape' && modal && !modal.hidden) closeSearch();
});
"""


def build_css() -> str:
    return r"""
:root {
  --bg: #f5f7fb;
  --panel: #ffffff;
  --panel-2: #eef2f7;
  --ink: #14171f;
  --muted: #647084;
  --line: #d9e0ea;
  --cyan: #2f9fb3;
  --green: #3b9f73;
  --amber: #c7832b;
  --coral: #d76d55;
  --violet: #7a69c7;
  --blue: #4d78c7;
  --rose: #c75f87;
  --lime: #7a9f38;
  --shadow: 0 18px 50px rgba(32, 45, 68, .10);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background:
    linear-gradient(90deg, rgba(20,23,31,.04) 1px, transparent 1px) 0 0 / 32px 32px,
    linear-gradient(rgba(20,23,31,.035) 1px, transparent 1px) 0 0 / 32px 32px,
    var(--bg);
  color: var(--ink);
  font: 16px/1.65 ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a { color: inherit; text-decoration: none; }
p { margin: 0; color: var(--muted); }
main { width: min(1180px, calc(100% - 32px)); margin: 0 auto; }

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 24px;
  min-height: 72px;
  padding: 12px max(16px, calc((100vw - 1180px) / 2));
  background: rgba(245,247,251,.88);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid var(--line);
}
.brand { display: flex; align-items: center; gap: 12px; min-width: 230px; }
.brand-mark {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background: var(--ink);
  color: #73d2de;
  font-weight: 800;
}
.brand b, .brand em { display: block; line-height: 1.15; }
.brand em { color: var(--muted); font-style: normal; font-size: 12px; }
.site-nav { display: flex; gap: 4px; flex: 1; }
.site-nav a, .search-trigger, .button {
  border: 1px solid transparent;
  border-radius: 8px;
  padding: 9px 13px;
  font-weight: 700;
  color: #30394a;
}
.site-nav a.active, .site-nav a:hover { background: #fff; border-color: var(--line); }
.search-trigger {
  background: #fff;
  border-color: var(--line);
  cursor: pointer;
}
.button { display: inline-flex; align-items: center; justify-content: center; }
.button.primary { background: var(--ink); color: white; }
.button.secondary { background: white; border-color: var(--line); }

.hero-dashboard {
  display: grid;
  grid-template-columns: 1.25fr .75fr;
  gap: 24px;
  padding: 56px 0 28px;
}
.hero-copy {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 34px;
  box-shadow: var(--shadow);
}
.kicker, .section-head span, .page-hero > span {
  color: var(--coral);
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0;
  text-transform: uppercase;
}
h1, h2, h3 { margin: 0; line-height: 1.12; letter-spacing: 0; }
.hero-copy h1 { max-width: 820px; margin-top: 12px; font-size: clamp(38px, 6vw, 70px); }
.hero-copy p { margin-top: 18px; max-width: 720px; font-size: 18px; }
.hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 26px; }
.signal-board {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.signal-board div {
  min-height: 150px;
  padding: 22px;
  background: var(--ink);
  color: white;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.signal-board b { font-size: 42px; line-height: 1; }
.signal-board span { color: #b6c0ce; font-weight: 700; }

.today-grid, .two-column {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(320px, .72fr);
  gap: 24px;
  margin-top: 24px;
}
.lead-card, .channel-block, .mini-card, .list-item, .ad-slot, .directory-card, .entry-header, .entry-aside, .entry-content, .related-block, .sponsor-grid article {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: 0 8px 28px rgba(32, 45, 68, .06);
}
.lead-card { padding: 28px; }
.lead-card h2 { margin-top: 16px; font-size: clamp(28px, 4vw, 46px); }
.lead-card p { margin-top: 16px; font-size: 17px; }
.brief-stack, .compact-list, .list-stack { display: grid; gap: 12px; }
.section-head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
}
.section-head h2 { margin-top: 3px; font-size: 26px; }
.section-head a { color: var(--muted); font-weight: 800; }
.section-head.tight { margin: 0 0 10px; }
.spacer { margin-top: 24px; }

.eyebrow-row { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }
.channel-pill, .score, .tag, .audience-box span {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  border: 1px solid var(--line);
  padding: 5px 9px;
  font-size: 12px;
  font-weight: 900;
}
.channel-pill.cyan { color: var(--cyan); background: rgba(47,159,179,.08); }
.channel-pill.green { color: var(--green); background: rgba(59,159,115,.09); }
.channel-pill.amber { color: var(--amber); background: rgba(199,131,43,.10); }
.channel-pill.coral { color: var(--coral); background: rgba(215,109,85,.10); }
.channel-pill.violet { color: var(--violet); background: rgba(122,105,199,.10); }
.channel-pill.blue { color: var(--blue); background: rgba(77,120,199,.10); }
.channel-pill.rose { color: var(--rose); background: rgba(199,95,135,.10); }
.channel-pill.lime { color: var(--lime); background: rgba(122,159,56,.10); }
.score { background: #f8fafc; color: #2f3a4d; }
.score-5 { border-color: rgba(215,109,85,.35); }
.score-4 { border-color: rgba(47,159,179,.35); }
.score-3 { border-color: rgba(122,159,56,.35); }
.meta-line { color: var(--muted); font-size: 13px; font-weight: 700; }
.tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px; }
.tag { background: #f6f8fb; color: #566174; }
.why-box {
  display: grid;
  gap: 5px;
  margin-top: 18px;
  padding: 14px;
  background: #f4f7f8;
  border-left: 4px solid var(--cyan);
  border-radius: 6px;
}
.why-box b, .audience-box b { font-size: 13px; }
.why-box span { color: #354052; }

.mini-card { padding: 16px; display: grid; gap: 8px; }
.mini-card__top { display: flex; justify-content: space-between; gap: 8px; }
.mini-card__title { font-size: 17px; font-weight: 900; line-height: 1.3; }
.mini-card p { font-size: 14px; }

.ad-slot {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  align-items: center;
  margin-top: 24px;
  padding: 22px;
  background: #111318;
  color: white;
}
.ad-slot p { color: #b8c1cf; }
.ad-slot span { color: #f4b860; font-size: 12px; font-weight: 900; text-transform: uppercase; }
.ad-slot a { color: white; font-weight: 900; }

.channel-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  margin-top: 24px;
}
.channel-block { padding: 22px; }
.section-desc { margin: -6px 0 16px; }

.list-item {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 150px;
  gap: 18px;
  padding: 18px;
}
.list-item__title {
  display: block;
  margin: 7px 0 8px;
  font-size: 20px;
  font-weight: 900;
  line-height: 1.25;
}
.list-item__side {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 800;
}
.topic-cloud { display: flex; flex-wrap: wrap; gap: 8px; }
.topic-cloud a, .filter-links a {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 10px;
  font-weight: 800;
}

.page-hero {
  margin: 38px 0 24px;
  padding: 34px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
}
.page-hero h1 { margin-top: 10px; font-size: clamp(34px, 5vw, 58px); }
.page-hero p { margin-top: 14px; max-width: 780px; font-size: 17px; }
.hero-metrics { margin-top: 18px; display: flex; gap: 10px; align-items: baseline; }
.hero-metrics b { font-size: 38px; }
.directory-grid, .feature-grid, .sponsor-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}
.directory-card { padding: 24px; }
.directory-card span { color: var(--muted); font-weight: 900; }
.directory-card h2 { margin-top: 8px; }
.directory-card p { margin: 10px 0 20px; }

.feature-card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
}
.feature-card__media { display: block; height: 190px; background: var(--panel-2); }
.feature-card__media img { width: 100%; height: 100%; object-fit: cover; display: block; }
.signal-visual {
  height: 100%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #14171f;
  color: white;
}
.signal-visual span { font-size: 48px; font-weight: 900; color: #73d2de; }
.signal-visual b { font-size: 18px; }
.feature-card__body { padding: 18px; }
.feature-card__title { display: block; margin: 12px 0 10px; font-size: 22px; font-weight: 900; line-height: 1.22; }
.archive-list { margin: 24px 0 50px; }

.entry-layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
  gap: 22px;
  margin: 34px 0 50px;
}
.entry-header {
  grid-column: 1 / -1;
  padding: 32px;
}
.entry-header h1 { margin-top: 14px; font-size: clamp(34px, 5vw, 58px); max-width: 940px; }
.entry-header p { margin-top: 14px; max-width: 860px; font-size: 18px; }
.entry-actions { margin-top: 22px; display: flex; gap: 10px; flex-wrap: wrap; }
.entry-aside {
  grid-column: 2;
  grid-row: 2;
  align-self: start;
  position: sticky;
  top: 92px;
  padding: 18px;
}
.audience-box { margin-top: 18px; display: grid; gap: 10px; }
.audience-box div { display: flex; flex-wrap: wrap; gap: 8px; }
.entry-content {
  grid-column: 1;
  grid-row: 2;
  min-width: 0;
  padding: 30px;
}
.entry-image { width: 100%; max-height: 360px; object-fit: cover; border-radius: 8px; margin-bottom: 24px; }
.entry-content h2, .entry-content h3, .entry-content h4 { margin: 30px 0 12px; }
.entry-content p, .entry-content li, .entry-content blockquote {
  color: #30394a;
  font-size: 17px;
  overflow-wrap: anywhere;
}
.entry-content p { margin: 0 0 15px; }
.entry-content ul { padding-left: 22px; }
.entry-content blockquote { margin: 20px 0; padding: 12px 16px; border-left: 4px solid var(--amber); background: #f8fafc; }
.entry-content pre { overflow: auto; padding: 16px; background: #111318; color: #e8edf5; border-radius: 8px; }
.entry-content code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.related-block { grid-column: 1 / -1; padding: 22px; }
.related-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); display: grid; }

.topic-layout { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; margin-bottom: 50px; }
.topic-section { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 20px; }
.filter-links { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 18px; }

.site-footer {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  margin-top: 60px;
  padding: 30px max(16px, calc((100vw - 1180px) / 2));
  border-top: 1px solid var(--line);
  background: #eef2f7;
}
.site-footer p { max-width: 620px; }
.footer-links { display: flex; gap: 14px; flex-wrap: wrap; align-items: start; font-weight: 800; }

.search-open { overflow: hidden; }
.search-modal {
  position: fixed;
  inset: 0;
  z-index: 100;
  padding: 70px 16px;
  background: rgba(20,23,31,.45);
}
.search-panel {
  width: min(760px, 100%);
  max-height: calc(100vh - 140px);
  margin: 0 auto;
  overflow: hidden;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
}
.search-panel__head { display: flex; gap: 10px; padding: 14px; border-bottom: 1px solid var(--line); }
.search-panel input {
  flex: 1;
  min-width: 0;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px 14px;
  font: inherit;
}
.search-panel button { border: 1px solid var(--line); background: #fff; border-radius: 8px; padding: 0 14px; font-weight: 800; }
.search-results { max-height: calc(100vh - 220px); overflow: auto; padding: 10px; }
.search-result { display: block; padding: 14px; border-radius: 8px; }
.search-result:hover { background: #f4f7fb; }
.search-result span { color: var(--muted); font-size: 12px; font-weight: 900; }
.search-result b { display: block; margin: 4px 0; }
.search-result p { font-size: 14px; }
.empty-state { padding: 20px; }

@media (max-width: 940px) {
  .site-header { align-items: flex-start; flex-wrap: wrap; gap: 10px; }
  .brand { min-width: 0; }
  .search-trigger { order: 2; margin-left: auto; }
  .site-nav { order: 3; flex: 0 0 100%; width: 100%; overflow-x: auto; padding-bottom: 2px; }
  .hero-dashboard, .today-grid, .two-column, .entry-layout { grid-template-columns: 1fr; }
  .signal-board, .channel-grid, .directory-grid, .feature-grid, .topic-layout, .related-grid { grid-template-columns: 1fr; }
  .list-item { grid-template-columns: 1fr; }
  .list-item__side { align-items: flex-start; }
  .entry-aside { position: static; }
  .entry-aside, .entry-content { grid-column: auto; grid-row: auto; }
}

@media (max-width: 560px) {
  main { width: min(100% - 20px, 1180px); }
  .hero-copy, .page-hero, .entry-header, .entry-content { padding: 22px; }
  .hero-copy h1, .page-hero h1, .entry-header h1 { font-size: 34px; }
  .signal-board { grid-template-columns: 1fr 1fr; }
  .signal-board div { min-height: 110px; padding: 16px; }
  .signal-board b { font-size: 30px; }
  .ad-slot, .site-footer { flex-direction: column; align-items: flex-start; }
}
"""


if __name__ == "__main__":
    build_site()
