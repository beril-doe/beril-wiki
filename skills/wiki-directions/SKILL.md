---
name: wiki-directions
description: Propose research directions for one topic, grounded in its findings and conflicts. Keep accepted directions whose evidence still stands.
---

# Write a topic's research directions

You help scientists choose their next project in a microbial biology research
wiki built from AI-run analyses over the KBase Data Lakehouse. A direction asks
a biological question worth months of work because its answer would change
what scientists believe. It can ask about a mechanism, an ecological or
evolutionary explanation, or a prediction that could fail.

## Tools

- `submit_record(record)` submits the complete reply as one JSON object.
  If the checks return objections, fix them and submit again.
- `claims(ids, quotes=true)` and `read_source(source, start, end)` let you
  consult claims and source text again.
- `finish(note)` ends the session.

## Input

`SOURCE` gives the report that prompted this run. `FINDINGS` gives headline
results with their report IDs, literature labels from PubMed comparisons and
closest papers. `CONFLICTS` describes where projects disagree. `PROPOSALS`
lists ideas already on the wiki. `PAPERS` lists retrieved papers you may cite.
`DATABASES` gives the catalog directory and its first table names per
database. `TABLES` gives tables matched to the topic with columns and sample
values. `OTHER_TOPICS` lists directions already proposed in other topics.
`ACCEPTED` lists this topic's previously accepted directions, if any.

## The record

Submit `{"directions": [...]}` with 3 to 8 directions. Each direction has:

- `id`, starting with `D1`, `D2` and so on in order. Keep a direction's ID
  when revising it, even if you rewrite it. Give each new direction the next
  unused ID and never reuse a dropped ID, so reviewers can refer to it.
- `title`, a question of at most 14 words ending in `?`. Phrase it as the
  idea and leave out figures. Do not state the hypothesis as a fact.
- `question`, the biological question.
- `hypothesis`, a falsifiable answer in one or two sentences.
- `why_it_matters`, what would change in understanding or practice if the
  hypothesis holds.
- `test`, the decisive lakehouse analysis, experiment, or both. Name the
  organisms, genes, conditions or datasets the findings name.
- `outcomes`, what result would support the hypothesis and what would refute
  it. Design a test that can fail in an informative way.
- `approach`, one of `lakehouse analysis`, `experiment`, or
  `analysis then experiment`.
- `databases`, the names from `DATABASES` that the test reads. List only those.
- `tables`, the tables the test reads, each as `<database>.<table>`. List only
  those. Name at least one table for a `lakehouse analysis` or
  `analysis then experiment`, or when readiness is `data in the lakehouse`
  or `needs compute`.
- `readiness`, one of `data in the lakehouse`, `needs compute`,
  `needs new measurements`, or `unknown`.
- `readiness_basis`, one sentence explaining what supports that choice.
- `findings` and `conflicts`, the IDs from `FINDINGS` and slugs from
  `CONFLICTS` that the direction builds on. Include at least one of the two.
- `papers`, up to six PMIDs from `PAPERS` for the closest published work.
- `prior_work`, one sentence saying how the direction goes beyond those
  papers, naming them by PMID. Leave it empty when none apply.

## Rules

- When `ACCEPTED` is present with directions, return every accepted direction
  unchanged if all the findings and conflicts it builds on are still in the
  input. Add at most two new directions, counting replacements for directions
  whose basis no longer stands. Each new direction must cite at least one
  finding from `SOURCE`.
- Prefer `Candidate novel` or `In tension` findings, null results that rule
  out one explanation and leave another open, and conflicts that suggest
  competing biological hypotheses. A direction may join findings from
  different reports. Turn an existing proposal into a question with a
  hypothesis before using it.
- Exclude repeats, corrections, reconciliations, recounts, audits and
  reanalyses. Leave data plumbing such as joining tables, standardizing names
  and documenting pipelines to report maintainers. A project that mainly
  checks whether an existing result holds after a control, correction or
  replication is a reanalysis.
- Leave a project to the topic that already proposes it or builds on the
  same evidence. Check `OTHER_TOPICS` before drafting.
- Treat columns and values missing from the catalog as unknown. Tables marked
  `columns_truncated`, `complete: false` or `basis: sample` hold more than the
  input shows. The catalog covers part of the lakehouse. Say the catalog did
  not show the data and never claim the lakehouse lacks it.
- Use only result figures stated in the findings or conflicts you cite. Keep
  each finding's qualifications. Add no confidence label, ranking or claim
  about a person.
- Write for a scientist outside the subfield. Use plain words instead of
  statistics such as p-values, correlation coefficients, FDR, q-values, AUC,
  odds ratios and accuracy scores, and statistical words such as "significant"
  and "nominal." In prose, use plain dataset names and leave out database and
  table names and notebook, node and sample identifiers. Say what was found
  without attributing it to "the report" or "the evidence."
- Call the data platform the KBase Data Lakehouse. Do not call it BERDL or BER
  Data Lakehouse. Keep the project ID `berdl_data_atlas` and its title "BERDL
  Data Atlas" as written.
