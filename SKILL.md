---
name: ai-knowledge-writing-skill
description: Route learning, verification, visualization, site publishing, task ordering, and precision clarification into a five-function Codex workbench while keeping public outputs privacy-safe.
---

# AI Knowledge Workbench

Use this skill as a route-first workbench for learning, visualization, site publishing, task ordering, and precision clarification.

Do not jump straight into writing or building. First classify the task, choose the smallest useful lane, and protect privacy.

## What It Is For

- reading a source before writing about it
- turning an idea into a diagram, chart, or visual brief
- building or polishing a README or GitHub Pages surface
- splitting a multi-step task into an ordered queue
- asking only the minimum clarifying question when the prompt is ambiguous

## When To Use It

- the user shares a file, screenshot, page, paper, or source text
- the user asks "what is this" and the answer depends on the material
- the user wants a visual summary, comparison, or flow
- the user wants a public-facing repository page or demo page
- the user has several tasks with dependencies or priorities
- the request may leak private paths, accounts, secrets, or unpublished material

## Five Lanes

| Lane | Use it for | Output |
|---|---|---|
| `browser-lane` | sources, screenshots, pages, papers, current facts | source map, fact/inference split, safe summary |
| `visualize-lane` | charts, diagrams, flows, comparisons, visual notes | visual brief, layout, labels, export target |
| `sites-lane` | README, static site, GitHub Pages, demo page | page map, content blocks, publish checklist |
| `queue-lane` | multiple tasks, dependencies, priorities, inserts | ordered queue, status notes, handoff plan |
| `precision-lane` | ambiguity, privacy risk, unsupported claims | minimum question, safe assumption, caveats |

When a request crosses lanes, choose one primary lane and add brief handoff notes for the next lane.

Common sequence: `browser-lane -> precision-lane -> visualize-lane -> sites-lane`.

## Routing Workflow

1. Classify the request into one or two lanes at most.
2. If the task depends on current facts or a source file, use `browser-lane` first.
3. If the task will be public, route through `precision-lane` before publishing.
4. If the task needs a visual or site surface, hand off to `visualize-lane` or `sites-lane`.
5. If the request contains many items, use `queue-lane` to order them.
6. Ask only the smallest question that changes the output.
7. Generalize private details before you write anything public.
8. Load the relevant reference:
   - `references/routing.md`
   - `references/browser-lane.md`
   - `references/visualize-lane.md`
   - `references/sites-lane.md`
   - `references/queue-lane.md`
   - `references/precision-lane.md`
   - `references/output-templates.md`
   - `references/privacy-originality.md`
9. Produce a compact answer with the route, what is known, what is inferred, what is next, and what must stay private.

## Default Output Shape

For broad requests, answer with:

1. **Route**: chosen lane and why.
2. **Source Map**: what is directly supported, inferred, or uncertain.
3. **Output Plan**: audience, structure, tone, and length.
4. **Artifact**: summary, diagram brief, page brief, queue, or review note.
5. **Review**: fact boundaries, originality, privacy, and caveats.

For narrow requests, skip unnecessary sections and answer directly.

## Core Guardrails

- Do not copy source wording, slogans, command lists, labels, or section order unless the user explicitly asks for quotation.
- Treat current tools, policies, prices, software behavior, and external claims as verification-sensitive.
- Remove or generalize local file paths, private URLs, account identifiers, tokens, keys, personal details, and unpublished data.
- Use placeholders like `[source]`, `[topic]`, `[document]`, `[dataset]`, or `[repository]` in public examples.
- For biomedical, legal, financial, or clinical topics, keep claims cautious and use source-aware wording.
- If a request is ambiguous, ask the smallest question set that unlocks the next step.
- If a claim might have changed recently, verify it rather than guessing.

## Example Triggers

- "Verify this tool workflow and turn it into a public explainer."
- "Turn this diagram into a visual summary for beginners."
- "Build a GitHub Pages demo for this workflow."
- "Split these requests into an ordered queue and mark what is urgent."
- "Ask only the minimum clarifying question needed to proceed."
