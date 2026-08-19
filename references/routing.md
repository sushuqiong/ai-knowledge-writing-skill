# Routing Guide

Use this file to choose the smallest useful lane before writing, visualizing,
building, or publishing. Public writing composes lanes; it is not a sixth lane.

## Lane Table

| Lane | Use when the user asks about | Default output |
|---|---|---|
| browser-lane | a source, screenshot, diagram, paper, page, or any fact that may need verification | source inventory, fact/inference split, safe summary |
| visualize-lane | a chart, flow, comparison, infographic, map, or visual explanation | visual brief, layout plan, labels, and export target |
| sites-lane | a README, static site, GitHub Pages page, demo surface, or repo homepage | page map, content blocks, and publish checklist |
| queue-lane | multiple tasks, priorities, dependencies, or urgent insertions | ordered queue, status labels, and handoff notes |
| precision-lane | ambiguity, privacy risk, copied wording risk, or uncertain claims | minimal questions, safe assumption, and boundary notes |

## Route Selection Rules

- If the user provides a source, start with `browser-lane`.
- If the user asks for a visual or diagram, start with `visualize-lane`.
- If the user asks for a repo page, demo page, or public surface, start with `sites-lane`.
- If the user gives multiple requests, start with `queue-lane`.
- If the request is unclear, risky, or likely to leak private information, start with `precision-lane`.
- If the task mixes source reading and public writing, use
  `browser-lane -> precision-lane -> DOCX or sites-lane` as needed.
- Use `visualize-lane` only when a visual is requested or materially improves
  the explanation.
- Use `queue-lane` when several articles or artifacts have dependencies; a
  single article normally does not need it.

## Writing recipe selection

| Request shape | Primary recipe |
| --- | --- |
| explain a concept, workflow, or method | `concept-explainer` |
| interpret an attachment, image, or document | `source-to-article` |
| medicine, public health, law, finance, or safety | `high-risk-health` plus domain review |
| compare products, prices, or current capabilities | `product-comparison` |
| explain a fixed list item by item | `glossary-list` |
| create and verify a Word file | `docx-delivery` |

## Minimal Clarifying Questions

Ask only when the answer changes the artifact:

- Target audience: beginner, professional, public reader, student, or researcher?
- Output format: note, visual, article, site, checklist, or script?
- Length: short, medium, or full draft?
- Source status: public source, private draft, screenshot, paper, or internal material?
- Publishing destination: private note, public article, GitHub repo, or GitHub Pages?

When a safe default exists, state the assumption and continue.
