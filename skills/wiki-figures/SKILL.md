---
name: wiki-figures
description: Place existing report figures beside the key claims of a wiki page.
---

Choose where existing figures support a scientific wiki page.

## Tools

- `submit_record(record)` submits your placements and visualization flags.

The session ends when the tool accepts the record. Use the evidence in the task message.

## Input

`PAGE_PARAGRAPHS` gives the page's paragraphs in order. `CANDIDATE_FIGURES`
gives the source report, file, caption and report context for each available
figure. Use zero-based indices into both lists. `MAX_PLACE` gives the maximum
number of figures you can place.

## The record

`{"placements": [{"after_paragraph": 0, "figure": 0}], "csv_flags": ["what to visualize and why"]}`

Give each placement by its two indices. The wiki copies captions directly from
the reports.

## Rules

- Choose only figures a reader must see to understand the page's key claims
  in the context of the reported data. Leave a figure out when in doubt. The
  complete set is on the raw report page.
- Most pages need zero to two figures. Place at most `MAX_PLACE`. Skip
  decorative, redundant or merely related figures.
- When the page discusses quantitative evidence that clearly needs a figure
  and no candidate covers it, add a `csv_flags` entry describing what to
  visualize and why. This can include a dense table, a distribution or a
  correlation described only in prose.
