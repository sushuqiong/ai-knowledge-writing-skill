# SPDX-License-Identifier: MIT
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    ".github/release-template.md",
    ".github/workflows/validate.yml",
    ".gitignore",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "README.en.md",
    "SECURITY.md",
    "SKILL.md",
    "agents/openai.yaml",
    "assets/repo-cover.svg",
    "docs/index.html",
    "docs/en.html",
    "docs/assets/app.js",
    "docs/assets/favicon.svg",
    "docs/assets/styles.css",
    "docs/assets/workflow.svg",
    "evals/cases.json",
    "evals/rubric.md",
    "requirements.txt",
    "scripts/article_schema.py",
    "scripts/render_docx.py",
    "scripts/validate_article.py",
    "scripts/validate_public_package.py",
    "templates/article.example.json",
    "templates/review-checklist.md",
    "tests/test_toolchain.py",
}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".html", ".css", ".js", ".svg", ".txt"}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HTML_LINK = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.I)


class PackageValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PackageValidationError(message)


def files_under(root: Path) -> set[str]:
    return {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts and "dist" not in path.parts
    }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_required_files(root: Path, files: set[str]) -> None:
    missing = sorted(REQUIRED_FILES - files)
    require(not missing, "missing required files: " + ", ".join(missing))
    for relative in REQUIRED_FILES:
        require((root / relative).stat().st_size > 0, f"empty required file: {relative}")


def validate_skill(root: Path) -> None:
    text = read_text(root / "SKILL.md")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    require(match is not None, "SKILL.md frontmatter is missing")
    frontmatter = match.group(1)
    require(re.search(r"^name:\s*ai-knowledge-writing-skill\s*$", frontmatter, re.M) is not None, "invalid skill name")
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    require(description is not None and 80 <= len(description.group(1)) <= 700, "skill description length is invalid")
    for marker in ("seven-step", "browser-lane", "DOCX", "privacy"):
        require(marker.lower() in text.lower(), f"SKILL.md missing marker: {marker}")


def validate_links(root: Path, files: set[str]) -> int:
    checked = 0
    for relative in sorted(files):
        suffix = Path(relative).suffix.lower()
        if suffix not in {".md", ".html"}:
            continue
        source = root / relative
        pattern = MARKDOWN_LINK if suffix == ".md" else HTML_LINK
        for raw in pattern.findall(read_text(source)):
            target = raw.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "data:", "javascript:")):
                continue
            destination = (source.parent / unquote(target)).resolve()
            require(destination.exists(), f"broken local link in {relative}: {raw}")
            checked += 1
    return checked


def validate_privacy(root: Path, files: set[str]) -> int:
    exact_markers = ("RESTORED_CONTEXT",)
    private_paths = (
        re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+"),
        re.compile(r"/(?:Users|home)/[^/\s]+"),
    )
    email = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
    credential = re.compile(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}")
    scanned = 0
    for relative in sorted(files):
        if relative == "scripts/validate_public_package.py":
            continue
        if Path(relative).suffix.lower() not in TEXT_SUFFIXES or relative == "LICENSE":
            continue
        text = read_text(root / relative)
        for marker in exact_markers:
            require(marker not in text, f"private marker found in {relative}")
        for pattern in private_paths:
            require(pattern.search(text) is None, f"private path found in {relative}")
        for found in email.findall(text):
            require(found.lower().endswith("@users.noreply.github.com"), f"personal email found in {relative}")
        require(credential.search(text) is None, f"credential-like assignment found in {relative}")
        scanned += 1
    return scanned


def validate_evals(root: Path) -> int:
    data = json.loads(read_text(root / "evals/cases.json"))
    require(data.get("schema_version") == 1, "eval schema_version must be 1")
    cases = data.get("cases")
    require(isinstance(cases, list) and len(cases) == 24, "exactly 24 eval cases are required")
    ids = [case.get("id") for case in cases]
    require(all(isinstance(value, str) and value for value in ids), "eval id missing")
    require(len(ids) == len(set(ids)), "duplicate eval id")
    for case in cases:
        for key in ("class", "prompt", "expected_recipe", "requirements", "forbidden"):
            require(case.get(key), f"eval {case['id']} missing {key}")
    expected_counts = {"should-trigger": 6, "should-not-trigger": 6, "evidence-boundary": 6}
    for label, count in expected_counts.items():
        require(sum(case["class"] == label for case in cases) == count, f"expected {count} {label} cases")
    require(sum(case["class"] in {"privacy-boundary", "artifact-boundary"} for case in cases) == 6, "expected six privacy/artifact cases")
    return len(cases)


def validate_readmes(root: Path) -> None:
    chinese = read_text(root / "README.md")
    english = read_text(root / "README.en.md")
    commands = (
        "npx skills add sushuqiong/ai-knowledge-writing-skill --list",
        "npx skills add sushuqiong/ai-knowledge-writing-skill --skill ai-knowledge-writing-skill -g -y",
    )
    for command in commands:
        require(command in chinese and command in english, f"README missing install command: {command}")
    require("README.en.md" in chinese and "README.md" in english, "README language links are missing")


def validate_site(root: Path) -> None:
    styles = read_text(root / "docs/assets/styles.css")
    require("border-radius: var(--radius)" in styles, "site does not use the bounded shared radius")
    require("linear-gradient" not in styles and "radial-gradient" not in styles, "site must not use gradients")
    for relative in ("docs/index.html", "docs/en.html"):
        text = read_text(root / relative)
        require("v0.3.0" in text, f"{relative} missing version marker")
        require("data-copy" in text, f"{relative} missing copy controls")


def validate_repository(root: Path = REPO_ROOT) -> dict[str, int]:
    root = root.resolve()
    files = files_under(root)
    validate_required_files(root, files)
    validate_skill(root)
    links = validate_links(root, files)
    scanned = validate_privacy(root, files)
    cases = validate_evals(root)
    validate_readmes(root)
    validate_site(root)
    return {"files": len(files), "links": links, "privacy_files": scanned, "eval_cases": cases}


def main() -> int:
    try:
        result = validate_repository()
    except (OSError, UnicodeError, json.JSONDecodeError, PackageValidationError) as error:
        print(f"FAIL: {error}")
        return 1
    print("PASS " + " ".join(f"{key}={value}" for key, value in result.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
