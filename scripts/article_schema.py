# SPDX-License-Identifier: MIT
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse


class ArticleValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArticleValidationError(message)


def load_article(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    validate_article_data(data)
    return data


def validate_article_data(data: dict) -> None:
    require(isinstance(data, dict), "article must be a JSON object")
    require(data.get("schema_version") == 1, "schema_version must be 1")
    require(isinstance(data.get("title"), str) and data["title"].strip(), "title is required")
    if "subtitle" in data:
        require(isinstance(data["subtitle"], str), "subtitle must be a string")
    if "disclaimer" in data:
        require(isinstance(data["disclaimer"], str), "disclaimer must be a string")

    sections = data.get("sections")
    require(isinstance(sections, list) and sections, "sections must be a non-empty list")
    for index, section in enumerate(sections, start=1):
        require(isinstance(section, dict), f"section {index} must be an object")
        heading = section.get("heading", "")
        require(isinstance(heading, str), f"section {index} heading must be a string")
        paragraphs = section.get("paragraphs")
        require(isinstance(paragraphs, list) and paragraphs, f"section {index} paragraphs are required")
        for paragraph in paragraphs:
            require(isinstance(paragraph, str) and paragraph.strip(), f"section {index} has an empty paragraph")

    target = data.get("target_chars")
    require(isinstance(target, dict), "target_chars is required")
    minimum, maximum = target.get("min"), target.get("max")
    require(isinstance(minimum, int) and minimum >= 1, "target_chars.min must be a positive integer")
    require(isinstance(maximum, int) and maximum >= minimum, "target_chars.max must be >= min")

    sources = data.get("sources", [])
    require(isinstance(sources, list), "sources must be a list")
    seen_urls: set[str] = set()
    for index, source in enumerate(sources, start=1):
        require(isinstance(source, dict), f"source {index} must be an object")
        require(isinstance(source.get("label"), str) and source["label"].strip(), f"source {index} label is required")
        url = source.get("url")
        require(isinstance(url, str), f"source {index} url is required")
        parsed = urlparse(url)
        require(parsed.scheme in {"http", "https"} and parsed.netloc, f"source {index} must use http or https")
        require(url not in seen_urls, f"duplicate source URL: {url}")
        seen_urls.add(url)
        if "accessed" in source:
            require(isinstance(source["accessed"], str), f"source {index} accessed must be a string")


def body_parts(data: dict) -> list[str]:
    parts: list[str] = []
    for section in data["sections"]:
        heading = section.get("heading", "").strip()
        if heading:
            parts.append(heading)
        parts.extend(paragraph.strip() for paragraph in section["paragraphs"])
    return parts


def nonspace_count(parts: list[str]) -> int:
    return len(re.sub(r"\s+", "", "".join(parts)))


def validate_target_count(data: dict) -> int:
    count = nonspace_count(body_parts(data))
    minimum = data["target_chars"]["min"]
    maximum = data["target_chars"]["max"]
    require(minimum <= count <= maximum, f"body count {count} is outside {minimum}-{maximum}")
    return count


def public_text(data: dict) -> str:
    values = [data["title"], data.get("subtitle", ""), data.get("disclaimer", "")]
    values.extend(body_parts(data))
    for source in data.get("sources", []):
        values.extend([source["label"], source["url"], source.get("accessed", "")])
    return "\n".join(values)


def privacy_findings(text: str) -> list[str]:
    patterns = {
        "Windows user path": re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+"),
        "Unix user path": re.compile(r"/(?:Users|home)/[^/\s]+"),
        "private IPv4 address": re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b"),
        "credential assignment": re.compile(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    }
    findings = [label for label, pattern in patterns.items() if pattern.search(text)]
    for email in re.findall(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", text, flags=re.I):
        if not email.lower().endswith("@users.noreply.github.com"):
            findings.append("email address")
            break
    return findings


def validate_privacy(data: dict) -> None:
    findings = privacy_findings(public_text(data))
    require(not findings, "privacy findings: " + ", ".join(findings))
