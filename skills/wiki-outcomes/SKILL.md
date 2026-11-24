---
name: wiki-outcomes
description: Classify one finding by the kind of result its evidence shows so scientists can browse the Results map by result type.
---

# Classify a finding's result

## Tools

- `submit_record(record)` submits your answer as one JSON object. Fix any
  objections and submit again. You have three attempts.

The session ends when the tool accepts the record. Use the evidence in the task message.

## Input

`FINDING` gives the title, claim, evidence quote, caveat and its quote,
extraction tag (`observation`, `inference`, `null result` or `correction`),
and plain summary.

## The record

`{"type": "...", "reason": "..."}`

## Rules

Use the evidence quote to decide the type. The extraction tag can misclassify
findings.

- `positive` means the analysis found a pattern, difference, trend,
  association or link. Include an effect opposite to the one expected and
  a prediction that worked.
- `negative` means the analysis tested for a difference, link or effect and
  found none, or a model or prediction failed to work.
- `inconclusive` means the analysis ran but could not decide between the
  outcomes it tested.
- `data` describes the coverage, missing entries, naming or provenance of
  a dataset, database, catalog or annotation. It has no biological result.
- `bookkeeping` only fixes the project's own error in a list, marker set,
  compound list or grouping rule. It has no biological result of its own.
- `untested` proposes an explanation or a rerun that the project did not test.

Classify a correction that also reports a biological result as `positive` or
`negative` according to that result. A reversed association or an effect that
shrinks after accounting for a confounder is a biological result. If a finding
reports a missing effect and a pattern the analysis found instead, choose
`positive`.

Write `reason` as one plain sentence of 4 to 30 words that states what the
evidence shows that decides the type. Use no statistics or statistical words.
