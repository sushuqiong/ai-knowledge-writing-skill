# AI Knowledge Writing Skill

A route-first Codex skill for turning technical material into clear learning notes and public-facing explainers.

This repository contains a single reusable skill:

```text
ai-knowledge-writing-skill/
  SKILL.md
  agents/openai.yaml
```

## What It Does

The skill helps Codex handle a common knowledge workflow:

1. understand the source
2. separate facts from interpretation
3. choose the right route
4. write a beginner-friendly explanation
5. check originality, uncertainty, and privacy

It is especially useful for:

- learning a new concept
- reading a paper, document, screenshot, or workflow diagram
- writing a WeChat-style popular-science article
- turning AI, computing, research, or biomedical material into public copy
- reviewing public text for privacy leakage and unsupported claims

## Route Map

| Route | Best For | Output |
| --- | --- | --- |
| Concept Explainer | "What is this?" beginner learning tasks | short plain-language explanation |
| Paper / Document Reading | papers, PDFs, Word files, long articles | structured summary and limitations |
| Public Writing | WeChat/公众号 articles or explainers | polished public copy |
| Image / Workflow Interpretation | diagrams, screenshots, process maps | what it shows and how it works |
| Fact / Privacy Review | content before publishing | uncertainty and privacy checks |

## How To Use

Copy the `ai-knowledge-writing-skill` folder into your Codex skills directory, then ask Codex with the skill name.

Example prompts:

```text
Use $ai-knowledge-writing-skill to explain this workflow diagram in a beginner-friendly way.
```

```text
Use $ai-knowledge-writing-skill to turn this paper into a 1200-word WeChat-style explainer.
```

```text
Use $ai-knowledge-writing-skill to review this draft for unsupported claims and privacy risks.
```

## Privacy Principles

This skill is designed for public-facing writing. It instructs Codex to remove or generalize:

- local file paths
- names, accounts, IDs, tokens, keys, and private URLs
- unpublished or sensitive data
- screenshots or excerpts from private systems

Use placeholders such as `[project]`, `[paper]`, `[dataset]`, or `[repository]` when examples are needed.

## Design Notes

The structure is inspired by route-first navigation: choose the type of task first, then follow the matching workflow. The wording and skill content are original and intentionally generic so they can be reused without private context.

## License

MIT

