---
name: ai-knowledge-writing-skill
description: Route knowledge-learning and public writing tasks into concise, source-aware workflows. Use when Codex needs to explain concepts, read papers or documents, analyze images/screenshots/videos/transcripts, create WeChat-style public explainers, turn technical material into beginner-friendly content, or review outputs for fact boundaries, originality, and privacy risks.
---

# AI Knowledge Writing Skill

Use this skill as a route-first workbench for learning, source interpretation, public writing, and publishing review. Do not jump straight into writing. First classify the task, identify the source type, and protect privacy.

## Four-Lane Workbench

- **concept-lane**: terms, tools, workflows, beginner questions, and "what is this?" tasks.
- **source-lane**: documents, screenshots, images, diagrams, transcripts, papers, and long-form source material.
- **writing-lane**: WeChat/公众号 drafts, popular-science articles, learning notes, captions, and public explainers.
- **review-lane**: fact-boundary checks, privacy checks, originality checks, and final publishing review.

When a request crosses lanes, choose one primary lane and add brief handoff notes for the other lanes. Common sequence: concept-lane -> source-lane -> writing-lane -> review-lane.

## Routing Workflow

1. Classify the request into one or more lanes.
2. Ask only for missing details that materially change the route, such as audience, source type, target length, output format, or whether content will be public.
3. Load the relevant reference:
   - `references/routing.md` for route selection and minimal questions.
   - `references/source-reading.md` for documents, images, screenshots, diagrams, transcripts, papers, and fact boundaries.
   - `references/public-writing.md` for public explainers, WeChat/公众号 articles, tone, structure, and non-copying rewrites.
   - `references/output-templates.md` for reusable learning, article, document, and review templates.
   - `references/privacy-originality.md` before publishing, summarizing private material, or reusing external source content.
4. Produce a compact answer or artifact with:
   - chosen route
   - source facts versus inference
   - reader-first structure
   - final output or next artifact
   - privacy/originality checks when relevant

## Default Output Shape

For broad learning or writing requests, answer with:

1. **Route**: chosen lane and why.
2. **Source Map**: what is directly supported, inferred, or uncertain.
3. **Reader Plan**: intended audience, outline, tone, and length.
4. **Artifact**: summary, article, document, checklist, or template.
5. **Review**: fact boundaries, originality, privacy, and caveats.

For narrow requests, skip unnecessary sections and answer directly.

## Core Guardrails

- Do not copy source wording, slogans, command lists, image labels, or section order unless the user explicitly asks for quotation and copyright limits allow it.
- Treat current tools, policies, prices, software behavior, and external claims as verification-sensitive.
- Remove or generalize local file paths, private URLs, account identifiers, tokens, keys, personal details, and unpublished data.
- Use placeholders like `[source]`, `[topic]`, `[document]`, `[dataset]`, or `[repository]` in public examples.
- For biomedical, legal, financial, or clinical topics, keep claims cautious and use source-aware wording.

## Example Triggers

- "Explain this diagram for beginners and write a short public article."
- "Read this paper and turn it into a WeChat-style explainer."
- "Summarize this tool workflow without copying the screenshot."
- "Review this draft for privacy leakage and unsupported claims."
- "Make a learning note and a 1000-word public-facing version."

