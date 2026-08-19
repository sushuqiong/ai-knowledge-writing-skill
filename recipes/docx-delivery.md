# Recipe: DOCX Delivery

Use the deterministic renderer when the user requests a Word artifact.

1. Produce validated article JSON with a declared target range.
2. Run `scripts/render_docx.py` with an explicit output path.
3. Run `scripts/validate_article.py` against both JSON and DOCX.
4. Reopen the file and inspect body count, headings, sources, hyperlinks, and
   metadata.
5. Report the actual path and checks performed.

Do not insert source screenshots or logos by default. A generated file is not
complete until the real artifact passes validation.
