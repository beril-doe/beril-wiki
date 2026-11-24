---
name: wiki-links
description: Classify related findings or references between microbial-biology research projects and give each link a short reader label.
---

# Describe links between projects

## Tools

- `submit_record(record)` submits one JSON object for the batch. Fix any
  objections and submit again. You have three attempts.

The session ends when the tool accepts the record. Use the evidence in the task message.

## Input

A related-results batch gives `PAIRS`. Each pair includes the titles,
claims, evidence quotes and key figures of two results from different
projects. Say how the results relate.

A reference batch gives `REPORT` and `NAMED`. Each named project has the
lines that mention it, with context. Say what the report does with that
project.

## The record

Submit `{"items": [{"id": "P1", "relation": "...", "label": "..."}]}` as one
JSON object. Use each supplied `P` or `R` id exactly once.

For a related-results pair, choose one relation.

- `same result` when both report the same measured outcome.
- `one extends the other` when one builds a further analysis on the other's result.
- `same direction, different definitions` when both find the same direction of effect but define the groups differently.
- `similar comparison, different scope` when they make a similar comparison on different organisms, cohorts or baselines.
- `one measures what the other cannot` when one covers cases the other's method cannot reach.
- `not the same question` when they share words but ask different questions.

For a reference, choose one relation.

- `uses its data or methods`
- `compares with its results`
- `corrects it`
- `applies its warning` when the report applies a pitfall or warning the named project documented.
- `audits it`
- `lists it as a reference only`
- `not a reference` for a file name, a generic phrase or a proposal the report did not carry out.

## Rules

- Write a label of 3 to 16 words for a microbiologist reading the link.
  Use plain biological words to say how the results relate or what the
  report did with the named project.
- Leave the label empty for `not the same question` and `not a reference`.
- Never say or imply that the projects confirm, corroborate, validate,
  reproduce, replicate or agree with each other. Never imply independence.
  Identical figures often mean shared data.
- Use no statistics or significance wording. Use only figures that the pair
  or report lines state.
- Describe the data in biological words. Leave out files, tables, columns
  and their names. In a reference label, say whose data or result it is,
  as in “Builds on the other project's mutant fitness data.”
- Leave out caveats, limitations and “however” clauses, and avoid “novel”,
  “first” and “breakthrough”.
