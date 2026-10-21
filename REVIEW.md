# Review rules

## Focus
- Model spend nobody asked for: a change that alters a cache key, a revision constant,
  a prompt tag, or the curator's accepted manifest, so the next run re-plans or rewrites
  the corpus; or a stage that calls a model when its inputs are unchanged. Editing
  `wiki/concepts`, `wiki/entities` or `wiki/summaries` outside a curator run makes the
  next run re-integrate every source (d609910, 2e19abb).
- A writer, merge or repair that drops a citation, figure or caveat the existing page
  carried (6178dbb, 40b592a).
- A numeric or citation check that silently stops checking, or reads identifiers,
  link targets or comments as figures (f0e7977, 4bcd7ee, c6a6beb, 6e39800).
- Reader-facing text that claims more than the corpus records: confidence labels the
  sources do not give, claims about what named people work on, "all projects" where
  some did (0053854, 1266201, 7ec2c56).
- A published route without the provenance callout, or a CI gate or path filter that
  lets a change deploy unchecked (accf865, PR #3, PR #4).
- Browser code that sends the reader's CBORG key anywhere but `api.cborg.lbl.gov`, or
  writes page, model or URL text into `innerHTML` unescaped.

## Skip
- Wording or science inside generated `wiki/` page diffs: raise it on the stage,
  prompt or contract that wrote the page, since `wiki/` is regenerated.
- `quartz/` (a gitignored Quartz clone) and `docs/drafts/` (gitignored scratch).
- Bulk data: `search/section-vectors.jsonl`, `state/*.json` caches, `wiki/sources/`.

## Human review
- `.github/workflows/`
- `contract/`
- `agentic.yaml`

## Output
- Start with the finding count; write "Nothing to fix" when it is zero.
- Cite file:line for every finding.
- Report at most three P3 findings.
