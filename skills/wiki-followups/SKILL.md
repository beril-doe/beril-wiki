---
name: wiki-followups
description: Classify what the deciding test for one research direction needs and name any catalog tables it would read.
---

# Classify a research direction's follow-up needs

## Tools

- `submit_record(record)` submits your answer as one JSON object. Fix any
  objections and submit again. You have three attempts.
- `claims(ids, quotes=true)` and `read_source(source, start, end)` let you
  inspect the claims and report again.
- `finish(note)` ends the session.

## Input

`QUESTION` gives the open question's title, hypothesis, how to test it, what
would support or refute it, the planned approach, and a note on what data
exist. The KBase Data Lakehouse is the shared database the projects queried.
`DIRECTION_TABLES` lists the catalog tables the direction names. `DATABASES`
lists the databases the catalog covers and their first table names. `TABLES`
lists catalog tables matched to the question, with columns and sample values.

## The record

`{"need": "...", "first_step_existing": false, "data_unclear": false, "reason": "...", "tables": ["<database>.<table>"]}`

## Rules

The catalog covers only part of the lakehouse. Treat values, columns and
tables that the inputs do not show as unknown. A table marked
`columns_truncated`, `complete: false` or `basis: sample` holds more than
the input shows. When data do not appear, say the catalog did not show them.
Never claim the lakehouse lacks data.

Decide `need` from the test and what would support or refute the hypothesis.
The planned approach and the data note can both misstate what the deciding
test needs.

- `existing` means tables the catalog lists can support or refute the
  hypothesis. The test may need a new analysis. Name those tables in `tables`.
- `outside` means the deciding data did not appear in the catalog's tenants
  and already exist elsewhere or can be collected without new lab or field
  work. Examples include public genomes or metagenomes, another study's
  measurements, or registered samples that no one has loaded yet.
- `experiment` means only a new lab or field measurement can decide it.

Choose `outside` or `experiment` according to what the test needs. A table's
absence from `DATABASES` or `TABLES` cannot decide the label. If a later
experiment would only confirm what existing or outside data can already
decide, choose `existing` or `outside`.

Set `first_step_existing` to true only when `need` is `experiment` and an
analysis of lakehouse data comes first and narrows what the experiment tests.
Then name the tables that first analysis reads. Otherwise set it to false.

Set `data_unclear` to true when the note or the test leaves it unresolved
whether the data needed can be found or joined. Otherwise set it to false.

Name at most 12 catalog tables in `tables`, each as `<database>.<table>`.
Use an empty list when `need` is `outside` or the experiment requires no
prior lakehouse analysis.

Write `reason` as one plain sentence of 4 to 30 words naming what decides
the hypothesis and what it needs. Call the platform the KBase Data Lakehouse
or the lakehouse. Never write BERDL. Use no statistics or statistical words.
