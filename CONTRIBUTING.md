# Contributing

Contributions should make public writing more accurate, original, understandable,
or verifiable without making simple requests heavy.

- Use synthetic examples and placeholders.
- Do not add private materials, personal identifiers, local paths, credentials,
  or copied third-party wording and layouts.
- Keep `SKILL.md` concise; move conditional detail into a linked reference or recipe.
- Add or update a behavior case when changing routing or a safety boundary.
- Keep the renderer deterministic and local. Do not add network calls, telemetry,
  model dependencies, or automatic uploads.
- Preserve the root skill entry and the five lane names.
- Run package validation and all tests before opening a pull request.

```powershell
python scripts/validate_public_package.py
python -m unittest discover -s tests -v
```
