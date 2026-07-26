---
name: ai-knowledge-writing-skill
description: Route knowledge-learning and public writing tasks into concise, source-aware workflows. Use when Codex needs to explain concepts, read papers or documents, analyze screenshots/videos/transcripts, create WeChat-style explainers, turn technical material into beginner-friendly content, or review outputs for fact boundaries, originality, and privacy risks.
---

# AI Knowledge Writing Skill

## Core Rule

Start with routing, then work the chosen route. Do not jump straight into writing. First identify the user goal, source material, audience, output format, fact-risk level, and privacy risk.

Use this skill for learning and writing tasks, especially when the user asks to:

- understand a concept, image, video, paper, tool, or workflow
- turn technical material into a beginner-friendly article
- write a public-facing WeChat/公众号 explainer
- summarize or compare AI, computing, biomedical, or research topics
- produce a document while avoiding plagiarism and privacy leakage

## Route Map

Choose one primary route. If the request spans routes, do them in this order: learn -> verify -> structure -> write -> review.

| Route | Use When | Main Output |
| --- | --- | --- |
| Concept Explainer | The user asks "what is this" or wants beginner learning | plain-language concept map and short explainer |
| Paper / Document Reading | The source is a paper, PDF, Word file, report, or long article | structured summary, key claims, limitations |
| Public Writing | The user wants a WeChat-style article or popular-science copy | polished article with title, sections, and clear logic |
| Image / Workflow Interpretation | The source is a screenshot, diagram, workflow, or poster | what it shows, steps, tools, caveats |
| Fact / Privacy Review | The user asks to polish, publish, or reuse material | risk notes, uncertain facts, privacy redactions |

## Workflow

1. **Inventory the source.** Identify source type, visible claims, missing context, and whether browsing or primary references are needed.
2. **Separate facts from interpretation.** Mark what is directly supported, what is inferred, and what needs verification.
3. **Build a reader-first outline.** Prefer "what it is -> why it matters -> how it works -> how to use it -> caveats" for explainers.
4. **Write in plain language.** Use short paragraphs, concrete analogies, and minimal jargon. Explain technical terms at first use.
5. **Avoid copying.** Do not mirror source wording, section order, slogans, or image labels. Rebuild the explanation in a new structure.
6. **Review before finalizing.** Check fact boundaries, audience fit, word count, output format, and privacy.

## Route Details

### Concept Explainer

- Define the concept in one sentence first.
- Explain the core mechanism with a familiar analogy.
- Add 3-5 practical examples or common use cases.
- End with "what beginners should remember".

### Paper / Document Reading

- Extract title, problem, method, evidence, result, limitation, and significance.
- Do not overstate causality or novelty unless the source supports it.
- Distinguish computation, experiment, review, opinion, and speculation.
- If the user wants public writing, translate the technical summary into a new article structure.

### Public Writing

- Use a clear title and short section headings.
- Keep the article concise when the user gives a word limit.
- Write for the stated audience, usually beginners.
- Prefer useful explanation over decorative prose.
- For biomedical or clinical topics, include boundaries such as "not medical advice" when appropriate.

### Image / Workflow Interpretation

- Read visible text and layout first.
- Explain the workflow in your own words.
- Clarify whether the image shows a standard method, a personal workflow, a tool stack, or an opinionated diagram.
- Avoid reproducing command lists unless the user explicitly asks for a runnable tutorial.

### Fact / Privacy Review

- Remove or generalize personal names, local file paths, tokens, keys, account identifiers, private URLs, screenshots of private systems, and unpublished data.
- Use placeholders such as `[project]`, `[paper]`, `[repository]`, or `[dataset]` when examples are needed.
- Flag claims that depend on current tool behavior, pricing, rankings, laws, or external documentation.
- For public publishing, prefer verified facts and cautious phrasing.

## Output Patterns

When writing an article, default to:

1. Title
2. Short opening that explains why the topic matters
3. 3-6 short sections with concrete headings
4. Brief caveats or common mistakes
5. One-sentence takeaway

When producing a document file, verify:

- the file opens successfully
- required count or length is met
- images are embedded when requested
- no private paths or credentials are present in public-facing text

## Quality Bar

The final output should be:

- beginner-friendly without being inaccurate
- original rather than copied from the source
- structured enough to paste into a public article
- explicit about uncertainty and limitations
- clean of private local details

