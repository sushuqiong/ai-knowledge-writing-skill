# DOCX Delivery

## Input contract

The renderer accepts JSON with `schema_version`, `title`, optional `subtitle`,
`sections`, optional `sources`, optional `disclaimer`, and `target_chars` with
inclusive `min` and `max` values. Each section has an optional `heading` and a
non-empty `paragraphs` array.

## Count scope

Count non-whitespace characters in section headings and body paragraphs only.
Exclude title, subtitle, disclaimer, source labels, URLs, and document metadata.

## Acceptance

- JSON validates and the count is within the requested inclusive range.
- The DOCX archive opens and contains the same title and body text.
- Heading hierarchy and short paragraphs are preserved.
- Source URLs are hyperlinks when sources are present.
- Author, last-modified-by, comments, and local-path metadata are empty.
- The file is reopened after generation; an office application check is added
  when available.

The renderer never uploads content, fetches sources, or embeds images by default.
