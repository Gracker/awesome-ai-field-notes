#!/usr/bin/env python3
"""Shared helpers for the OpenClaw intake and site-generation pipeline.

Daily tasks should normalize entries here before writing data/entries.json.
The public site may still apply an extra display filter, but bad placeholders,
relative dates, noisy summaries, and odd category branches should not enter the
durable data layer in the first place.
"""

from __future__ import annotations

import hashlib
import json
import re
import string
from copy import deepcopy
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


VALID_SOURCE_TYPES = {"github", "paper", "article", "x_post", "tweet", "newsletter", "video", "product", "dataset"}
VALID_LANGUAGES = {"en", "zh", "both"}
VALID_STATUSES = {"active", "archived", "deprecated", "score-pending"}
VALID_PLATFORMS = {
    "x",
    "twitter",
    "cubox",
    "arxiv",
    "github",
    "blog",
    "newsletter",
    "youtube",
    "manual",
    "unknown",
    "wechat",
    "news",
    "google",
    "anthropic",
    "community",
}

CANONICAL_CATEGORIES = {"models", "agents", "coding", "infra", "industry", "learning", "uncategorized"}

CATEGORY_ALIASES = {
    "model": "models",
    "models/models": "models",
    "agent": "agents",
    "agents/frameworks": "agents",
    "agent-frameworks": "agents",
    "agent-frameworks/applications": "agents",
    "agent-frameworks/benchmark": "agents",
    "agent-frameworks/evolution": "agents",
    "agent-frameworks/harness": "agents",
    "agent-frameworks/harness-engineering": "agents",
    "agent-frameworks/human-agent-collaboration": "agents",
    "agent-frameworks/knowledge-management": "agents",
    "agent-frameworks/mcp": "agents",
    "agent-frameworks/memory": "agents",
    "agent-frameworks/multi-agent": "agents",
    "agent-frameworks/orchestration": "agents",
    "agent-frameworks/production": "agents",
    "agent-frameworks/project-knowledge": "agents",
    "agent-frameworks/self-improving": "agents",
    "coding-agents": "coding",
    "coding-agents/claude-code": "coding",
    "coding-ai": "coding",
    "coding-ai/claude-code": "coding",
    "developer-tools": "coding",
    "developer-tools/browser-extensions": "coding",
    "workflow": "coding",
    "ai-tools": "uncategorized",
    "tools": "uncategorized",
    "tools-development": "uncategorized",
    "tools-development/applications": "uncategorized",
    "tools-development/frameworks": "uncategorized",
    "business": "industry",
    "content-creation": "industry",
    "strategy": "industry",
    "strategy/ai-career": "industry",
    "strategy/ai-news": "industry",
    "strategy/ai-product": "industry",
    "strategy/business-models": "industry",
    "ai-safety": "industry",
    "ai-safety/alignment": "industry",
    "ai-ux": "industry",
    "ai-ux/design-tools": "industry",
    "hardware-chips": "infra",
    "hardware-chips/risc-v-ai": "infra",
    "ai-hardware": "infra",
    "ai-hardware/chip-architecture": "infra",
    "infrastructure": "infra",
    "infrastructure/dev-tools": "infra",
    "llm-infra": "infra",
    "llm-infra/inference-optimization": "infra",
    "llm-engineering": "infra",
    "llm-engineering/inference-optimization": "infra",
    "multimodal": "infra",
    "multimodal/image-generation": "infra",
    "prompt": "learning",
    "prompt-engineering": "learning",
    "research": "learning",
    "research-methods": "learning",
    "research-methods/benchmarks": "learning",
    "research-methods/datasets": "learning",
    "education": "learning",
    "education/books": "learning",
    "education/online-courses": "learning",
    "learning/ai-courses": "learning",
    "learning/daily-digest": "learning",
}

CATEGORY_KEYWORDS = {
    "coding": {"codex", "claude-code", "cursor", "copilot", "ide", "sdk", "devtool", "developer", "vibe-coding", "代码", "编程"},
    "agents": {"agent", "agents", "mcp", "a2a", "harness", "tool-calling", "automation", "智能体", "自动化"},
    "models": {"model", "models", "llm", "gpt", "claude", "gemini", "qwen", "openai", "anthropic", "模型", "大模型"},
    "infra": {"rag", "inference", "eval", "benchmark", "chip", "gpu", "cuda", "multimodal", "fine-tuning", "推理", "芯片", "算力"},
    "industry": {"product", "startup", "market", "business", "strategy", "funding", "ipo", "regulation", "产品", "商业", "融资"},
    "learning": {"paper", "research", "course", "tutorial", "prompt", "guide", "arxiv", "论文", "课程", "教程", "学习"},
}

AI_KEYWORDS = set().union(*CATEGORY_KEYWORDS.values()) | {
    "ai",
    "aigc",
    "neural",
    "transformer",
    "diffusion",
    "人工智能",
    "生成式",
    "提示词",
    "多模态",
}

NOISE_TAGS = {"", "[]", "x", "twitter", "tweet", "uncategorized", "high-value", "rss", "ai"}
RELATIVE_DATES = {
    "今天": 0,
    "今日": 0,
    "today": 0,
    "昨天": -1,
    "昨日": -1,
    "yesterday": -1,
    "前天": -2,
    "明天": 1,
    "tomorrow": 1,
}

INVALID_SUMMARY_PATTERNS = (
    "cubox_url",
    "weixin/download",
    "?imageUrl=",
    "self.__next_f.push",
    "window.",
    "schema.org",
    "Read in Cubox",
    "Read Original",
)

GENERIC_PREVIEW_RE = re.compile(
    r"^(高价值AI内容|来自@[^，。\s]+的高价值AI相关内容|有参考价值的|Cubox 收藏|X 链接书签|内容过短|待补充|摘要暂缺|\[需翻译\]|待人工点评|\*{3,}|-{3,})",
    re.I,
)


def project_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "data" / "entries.json").exists():
            return candidate
    return Path(__file__).resolve().parents[2]


def entries_path() -> Path:
    return project_root() / "data" / "entries.json"


def content_dir() -> Path:
    return project_root() / "content"


def today_str() -> str:
    return date.today().isoformat()


def validate_entries_data(data: dict, path: Path | None = None) -> dict:
    """Reject corrupted entries.json shapes before any pipeline write.

    entries.json is a durable data file. It must stay a dict with an
    ``entries`` list; list-shaped writes previously caused production data
    loss, so fail fast here instead of trying to be permissive.
    """
    label = str(path or entries_path())
    if not isinstance(data, dict):
        raise ValueError(f"entries.json must be a dict with an 'entries' list, got {type(data).__name__}: {label}")
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise ValueError(f"entries.json missing list field 'entries': {label}")
    return data


def load_entries_data(path: Path | None = None) -> dict:
    target = path or entries_path()
    data = json.loads(target.read_text(encoding="utf-8"))
    return validate_entries_data(data, target)


def save_entries_data(data: dict, path: Path | None = None) -> None:
    target = path or entries_path()
    validate_entries_data(data, target)
    data["last_updated"] = today_str()
    data["total_entries"] = len(data["entries"])
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_url(url) -> str | None:
    if not url:
        return None
    value = str(url).strip()
    if not re.match(r"^https?://", value, re.I):
        return None
    if "](" in value or value.startswith(("![](", "[")):
        return None
    value = re.sub(r"[\x00-\x1f\x7f\s]+", "", value)
    if not value:
        return None
    try:
        parsed = urlparse(value)
    except ValueError:
        return None
    if not parsed.netloc:
        return None

    params = parse_qs(parsed.query, keep_blank_values=True)
    filtered = {
        key: vals
        for key, vals in params.items()
        if not key.lower().startswith("utm_") and key.lower() not in {"ref", "ref_src", "fbclid", "gclid"}
    }
    query = urlencode(filtered, doseq=True)
    netloc = parsed.netloc.lower()
    if netloc == "twitter.com":
        netloc = "x.com"
    path = parsed.path.rstrip("/") or parsed.path
    return urlunparse((parsed.scheme.lower(), netloc, path, "", query, ""))


def normalized_url_key(url) -> str | None:
    normalized = normalize_url(url)
    if not normalized:
        return None
    parsed = urlparse(normalized)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", parsed.query, ""))


def markdown_to_text(text: str) -> str:
    value = str(text or "")
    if value.lstrip().startswith("---"):
        parts = value.split("---", 2)
        if len(parts) >= 3:
            value = parts[2]
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
    return re.sub(r"\s+", " ", value).strip()


def clean_text(text, *, max_len: int | None = None) -> str:
    lines = []
    for raw_line in str(text or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if any(pattern.lower() in line.lower() for pattern in INVALID_SUMMARY_PATTERNS):
            continue
        if line.startswith(("来源：", "- **来源**", "**Source:**", "**English Title:**")):
            continue
        line = re.sub(r"\[Read in Cubox\]\([^)]*\)", "", line)
        line = re.sub(r"\[Read Original\]\([^)]*\)", "", line)
        lines.append(line)

    value = markdown_to_text("\n".join(lines))
    value = re.sub(r"https?://\S+", "", value).strip()
    value = "".join(ch for ch in value if ch in string.printable or ord(ch) >= 0x4E00)
    value = re.sub(r"\s+", " ", value).strip()
    if max_len and len(value) > max_len:
        cutoff = max_len
        for sep in ("。", "！", "？", ". ", "; ", "；", "，"):
            pos = value.rfind(sep, 0, max_len)
            if pos >= max(24, max_len // 3):
                cutoff = pos + len(sep)
                break
        value = value[:cutoff].rstrip(" ，,;；") + "..."
    return value


def has_cjk(text: str) -> bool:
    return re.search(r"[\u4e00-\u9fff]", text or "") is not None


def is_placeholder_text(text: str) -> bool:
    value = clean_text(text, max_len=220)
    if not value:
        return True
    lowered = value.lower()
    if GENERIC_PREVIEW_RE.search(value):
        return True
    if value in {"[]", "****", "---"}:
        return True
    if lowered.startswith(("id:", "source:", "title:", "category:", "tags:")):
        return True
    metadata_hits = sum(1 for token in ("source:", "category:", "created:", "description:", "cubox_url:", "tags:") if token in lowered)
    return metadata_hits >= 2


def has_readable_text(text: str, *, min_len: int = 24) -> bool:
    value = clean_text(text, max_len=320)
    if is_placeholder_text(value):
        return False
    if len(value) < min_len and not has_cjk(value):
        return False
    return len(value) >= min(16, min_len)


def normalize_date(value, *, run_date: date | None = None, allow_partial: bool = False) -> str | None:
    if value is None or value == "":
        return None
    base = run_date or date.today()
    raw = str(value).strip()
    lowered = raw.lower()
    for token, delta in RELATIVE_DATES.items():
        if token in lowered:
            return (base + timedelta(days=delta)).isoformat()
    raw = raw.replace("/", "-")
    if re.fullmatch(r"\d{4}-\d{1,2}-\d{1,2}", raw):
        try:
            return datetime.strptime(raw, "%Y-%m-%d").date().isoformat()
        except ValueError:
            return None
    if allow_partial and re.fullmatch(r"\d{4}-\d{1,2}", raw):
        year, month = raw.split("-")
        return f"{int(year):04d}-{int(month):02d}"
    if allow_partial and re.fullmatch(r"\d{4}", raw):
        return raw
    try:
        return datetime.fromisoformat(raw[:10]).date().isoformat()
    except ValueError:
        return None


def normalize_tags(tags) -> list[str]:
    if isinstance(tags, str):
        raw_tags = re.split(r"[,，\s]+", tags)
    elif isinstance(tags, list):
        raw_tags = tags
    else:
        raw_tags = []
    out = []
    seen = set()
    for tag in raw_tags:
        clean = clean_text(tag, max_len=36).strip().lower().replace(" ", "-")
        clean = re.sub(r"[^a-z0-9\u4e00-\u9fff_.+/#-]+", "", clean)
        if not clean or clean in NOISE_TAGS or clean in seen:
            continue
        seen.add(clean)
        out.append(clean)
    return out[:12]


def canonical_category(category, *, tags=None, source_type=None, title: str = "", summary: str = "") -> str:
    raw = str(category or "").strip().lower()
    prefix = raw.split("/", 1)[0]
    if raw in CANONICAL_CATEGORIES:
        return raw
    if raw in CATEGORY_ALIASES:
        return CATEGORY_ALIASES[raw]
    if prefix in CATEGORY_ALIASES:
        return CATEGORY_ALIASES[prefix]

    haystack = " ".join(
        [
            raw,
            " ".join(normalize_tags(tags)),
            str(source_type or ""),
            str(title or ""),
            str(summary or ""),
        ]
    ).lower()
    if source_type == "paper":
        return "learning"
    if source_type in {"github", "product", "dataset"} and not raw:
        return "uncategorized"
    scores = {
        cat: sum(1 for keyword in keywords if keyword in haystack)
        for cat, keywords in CATEGORY_KEYWORDS.items()
    }
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "uncategorized"


def normalize_source_type(value) -> str:
    raw = str(value or "article").strip().lower()
    aliases = {"x": "x_post", "twitter": "x_post", "post": "x_post", "repo": "github", "blog": "article"}
    raw = aliases.get(raw, raw)
    return raw if raw in VALID_SOURCE_TYPES else "article"


def normalize_platform(value, *, url: str | None = None) -> str:
    raw = str(value or "").strip().lower()
    raw = {"x/twitter": "x", "twitter": "x", "medium": "blog"}.get(raw, raw)
    if raw in VALID_PLATFORMS:
        return raw
    host = urlparse(url or "").netloc.lower()
    if "x.com" in host or "twitter.com" in host:
        return "x"
    if "github.com" in host:
        return "github"
    if "arxiv.org" in host:
        return "arxiv"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    if "mp.weixin.qq.com" in host:
        return "wechat"
    if "anthropic.com" in host:
        return "anthropic"
    if "google" in host:
        return "google"
    return "blog" if host else "unknown"


def generate_entry_id(*, title: str = "", url: str = "") -> str:
    base = normalized_url_key(url) or clean_text(title, max_len=120) or datetime.now().isoformat()
    digest = hashlib.sha1(base.encode("utf-8")).hexdigest()
    return digest[:8]


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
        or ("high-value" in tags and len(clean_text(summary)) < 50)
    )


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


def derive_one_liner(title: str, summary: str, existing: str | None = None) -> str:
    cleaned_existing = clean_text(existing, max_len=140)
    if cleaned_existing and not is_placeholder_text(cleaned_existing):
        return cleaned_existing
    cleaned_summary = clean_text(summary, max_len=180)
    if cleaned_summary and not is_placeholder_text(cleaned_summary):
        sentence = re.split(r"(?<=[。！？.!?])\s*", cleaned_summary)[0].strip()
        if len(sentence) >= 18:
            return clean_text(sentence, max_len=140)
    return clean_text(title, max_len=120) or "待补充可读摘要后再发布"


def normalize_entry(raw_entry: dict, *, run_date: date | None = None) -> dict:
    entry = deepcopy(raw_entry)
    source = entry.get("source") if isinstance(entry.get("source"), dict) else {}
    url = normalize_url(entry.get("url"))
    title = clean_text(entry.get("title") or "", max_len=140) or "未命名 AI 资源"
    summary_zh = clean_text(entry.get("summary_zh") or "", max_len=900)
    summary_en = clean_text(entry.get("summary_en") or "", max_len=900) or None
    source_type = normalize_source_type(entry.get("source_type"))
    tags = normalize_tags(entry.get("tags"))
    category = canonical_category(
        entry.get("category"),
        tags=tags,
        source_type=source_type,
        title=title,
        summary=summary_zh or summary_en or "",
    )

    try:
        quality = int(entry.get("quality_score", 3))
    except (TypeError, ValueError):
        quality = 3
    quality = max(1, min(5, quality))

    status = str(entry.get("status") or "active").strip()
    if status not in VALID_STATUSES:
        status = "active"

    one_liner = derive_one_liner(title, summary_zh or summary_en or "", entry.get("one_liner"))
    language = str(entry.get("language") or "zh").strip().lower()
    if language not in VALID_LANGUAGES:
        language = "zh" if has_cjk(summary_zh or title) else "en"

    normalized = {
        "id": str(entry.get("id") or generate_entry_id(title=title, url=url or "")),
        "title": title,
        "url": url,
        "source": {
            "platform": normalize_platform(source.get("platform") or entry.get("platform"), url=url),
            "author": clean_text(source.get("author") or entry.get("author") or "", max_len=100) or None,
            "original_date": normalize_date(
                source.get("original_date") or entry.get("original_date"),
                run_date=run_date,
                allow_partial=True,
            ),
        },
        "category": category,
        "tags": tags,
        "source_type": source_type,
        "language": language,
        "summary_zh": summary_zh,
        "summary_en": summary_en,
        "one_liner": one_liner,
        "one_liner_author": entry.get("one_liner_author") or "openclaw",
        "quality_score": quality,
        "status": status,
        "local_path": clean_text(entry.get("local_path") or "", max_len=240) or f"content/{entry.get('id') or generate_entry_id(title=title, url=url or '')}.md",
        "images": [],
        "added_date": normalize_date(entry.get("added_date"), run_date=run_date) or today_str(),
        "updated_date": normalize_date(entry.get("updated_date"), run_date=run_date),
        "github_stars": entry.get("github_stars"),
        "related": entry.get("related") if isinstance(entry.get("related"), list) else [],
    }

    seen_images = set()
    for image in entry.get("images") or []:
        normalized_image = normalize_url(image)
        if not normalized_image or normalized_image in seen_images:
            continue
        seen_images.add(normalized_image)
        normalized["images"].append(normalized_image)
        if len(normalized["images"]) >= 5:
            break

    low_signal = is_low_signal_entry(normalized) or (
        normalized["status"] == "active"
        and quality >= 3
        and is_placeholder_text(summary_zh)
        and not has_readable_text(normalized.get("one_liner"))
    )
    if low_signal:
        normalized["quality_score"] = min(normalized["quality_score"], 2)
        if normalized["status"] == "active":
            normalized["status"] = "score-pending"

    if normalized["status"] == "active" and not is_ai_related_entry(normalized):
        normalized["quality_score"] = min(normalized["quality_score"], 2)
        normalized["status"] = "score-pending"

    return normalized


def title_key(title: str) -> str:
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", clean_text(title).lower())


def append_entries(data: dict, raw_entries: list[dict]) -> tuple[list[dict], list[tuple[dict, str]]]:
    entries = data.setdefault("entries", [])
    seen_urls = {normalized_url_key(entry.get("url")) for entry in entries if entry.get("url")}
    seen_titles = {title_key(entry.get("title") or "") for entry in entries if entry.get("title")}
    added = []
    skipped = []

    for raw_entry in raw_entries:
        entry = normalize_entry(raw_entry)
        url_key = normalized_url_key(entry.get("url"))
        t_key = title_key(entry.get("title") or "")
        if url_key and url_key in seen_urls:
            skipped.append((entry, "duplicate-url"))
            continue
        if not url_key and t_key and t_key in seen_titles:
            skipped.append((entry, "duplicate-title"))
            continue
        entries.append(entry)
        added.append(entry)
        if url_key:
            seen_urls.add(url_key)
        if t_key:
            seen_titles.add(t_key)

    data["last_updated"] = today_str()
    return added, skipped
