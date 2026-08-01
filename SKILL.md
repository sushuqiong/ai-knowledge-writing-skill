---
name: ai-knowledge-writing-skill
description: Route learning, verification, visualization, site publishing, task ordering, and precision clarification into a five-function Codex workbench. Use when Codex needs to understand source material, verify current facts, build visual summaries, publish static pages, split or prioritize work, or ask the minimum clarifying questions while protecting privacy.
---

# AI Knowledge Workbench

Use this skill as a route-first workbench for learning, visualization, site publishing, task ordering, and precision clarification. Do not jump straight into writing or building. First classify the task, identify the source type, and protect privacy.

## Five Lanes

- **browser-lane**: read a source, inspect a screenshot or diagram, and verify public facts with the browser when recency matters.
- **visualize-lane**: turn an idea or dataset into a chart, diagram, flow, comparison table, or visual summary.
- **sites-lane**: build or improve a README, static site, GitHub Pages demo, or other public-facing site surface.
- **queue-lane**: split work into ordered steps, batch tasks, reprioritize, or insert an urgent item into the plan.
- **precision-lane**: handle ambiguity, privacy risk, unsupported claims, and prompts that need only the minimum clarifying questions.

When a request crosses lanes, choose one primary lane and add brief handoff notes for the next lane. Common sequence: `browser-lane -> visualize-lane -> sites-lane -> precision-lane`.

## Routing Workflow

1. Classify the request into one or more lanes.
2. Ask only for missing details that materially change the route, such as audience, source type, target length, output format, or whether content will be public.
3. If the task needs current or external facts, route through `browser-lane` first.
4. If the output will be public, route through `precision-lane` before publishing and before copying external wording.
5. If several lanes are needed, pick one primary lane and one follow-up lane at most.
6. Generalize private details and ask only questions that change the output.
7. If the request is only for a direct answer and no source or build step is needed, answer directly and keep the route compact.
8. Load the relevant reference:
   - `references/routing.md` for route selection and minimal questions.
   - `references/browser-lane.md` for source reading, browser verification, and fact boundaries.
   - `references/visualize-lane.md` for diagrams, charts, flows, and visual summaries.
   - `references/sites-lane.md` for README pages, static sites, and GitHub Pages delivery.
   - `references/queue-lane.md` for prioritization, batching, and insertion rules.
   - `references/precision-lane.md` for ambiguity handling, uncertainty, and clarification.
   - `references/output-templates.md` for reusable learning, visualization, site, queue, and review templates.
   - `references/privacy-originality.md` before publishing, summarizing private material, or reusing external source content.
9. Produce a compact answer or artifact with the chosen route, source facts versus inference, reader-first structure, the final artifact or next artifact, and privacy/originality checks when relevant.

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
- If a request is ambiguous, ask the smallest question set that unlocks the next step.
- If a claim might have changed recently, verify it rather than guessing.

## Example Triggers

- "Verify this tool workflow and turn it into a public explainer."
- "Turn this diagram into a visual summary for beginners."
- "Build a GitHub Pages demo for this workflow."
- "Split these requests into an ordered queue and mark what is urgent."
- "Ask only the minimum clarifying question needed to proceed."
