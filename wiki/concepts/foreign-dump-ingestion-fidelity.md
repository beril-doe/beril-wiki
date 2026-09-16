---
type: "Concept"
description: "How the documented MySQL dumps and SQLite files lose fidelity at ingestion through headerless data, literal null markers, unparseable DDL and non-UTF-8 text, and the preprocessing proposed to repair them."
sources: ["summaries/pitfalls.md"]
---
The central pitfalls digest documents specific MySQL dump and SQLite ingestion cases in which column names, null encodings, schema definitions and text encodings each had to be repaired before the data could be used, and in which one failure was silent rather than loud [src: pitfalls]. See [[summaries/pitfalls]] for the full digest.

## Headerless data and literal nulls

The described MySQL dump data files have no header row, so column names must be taken from the `CREATE TABLE` statement rather than from the first line of the data file [src: pitfalls].

The same dump encodes NULL as the literal `\N`, which is neither an empty string nor the token `NULL` [src: pitfalls].

## Schema parsing failures

A MySQL-specific DDL trailer (`) ENGINE=InnoDB AUTO_INCREMENT=... DEFAULT CHARSET=utf8mb3;`) follows the column list. The regex `\)\s*;` used by `ingest_lib.parse_sql_schema` requires the closing parenthesis to be followed only by whitespace and a semicolon, so it does not match these schemas [src: pitfalls].

The `parse_sql_schema()` function extracts column definitions from `CREATE TABLE` statements by regex. When the table body begins with an inline comment (for example `/* geneId is actually a fully specified protein id like YP_006960813.1 */`), the parser treats `/*` as a column name instead of skipping it [src: pitfalls].

This comment misparse produces an invalid schema string like `/* STRING, geneId STRING, ...`, and the ingest pipeline then silently skips the entire table with no error message or quarantine entry [src: pitfalls]. This **supports** the pattern described in [[concepts/silent-failure-modes-in-distributed-queries]], in which data-handling failures emit no error and can only be caught by explicit checks [src: pitfalls].

## Encoding failures

When a SQLite database is exported to TSV with `sqlite3.connect()` and cursor iteration, Python's `sqlite3` module decodes TEXT columns as strict UTF-8 by default. Non-UTF-8 byte sequences raise `OperationalError: Could not decode to UTF-8 column 'comment' with text '...'` during cursor iteration, before any row-level cleaning such as `_clean()` is invoked [src: pitfalls].

The documented workaround sets `conn.text_factory = lambda b: b.decode('utf-8', errors='replace')` immediately after connecting and before executing any queries [src: pitfalls].

This workaround trades fidelity for completeness. Iteration then succeeds, but invalid bytes become U+FFFD replacement characters instead of being preserved [src: pitfalls].

## Preprocessing remedy

For schemas, the proposed preprocessing strips the `ENGINE=...;` trailer to leave just `CREATE TABLE name (cols);` and concatenates all per-table `.sql` files into one `schema.sql` [src: pitfalls].

For data, each `.txt` file is streamed through `csv.reader` (comma-delimited, `doublequote=True`), `\N` is replaced with an empty string, and the result is written as TSV with a prepended header derived from the `CREATE TABLE` statement [src: pitfalls]. This **refines** the null-handling caveat above: the remedy maps the literal marker to an empty string rather than keeping a distinct null token [src: pitfalls].

A reference implementation of this preprocessing (`~/data/genome_depot_enigma/preprocess.py`) reportedly handles 13 GB / 32 tables in ~5 minutes [src: pitfalls].

## Tensions

The encoding workaround and the goal of faithful ingestion pull against each other. Strict decoding halts the export, while the documented permissive decoding completes it but replaces invalid bytes with U+FFFD; the assigned evidence describes no byte-preserving alternative [src: pitfalls].

## Open Directions

- Post-ingest table-count audit: compare the set of `CREATE TABLE` names in each source dump against the tables actually loaded. This would detect the silent whole-table skips caused by comment misparsing, which currently leave no error or quarantine entry [src: pitfalls].
- Replacement-character census: count U+FFFD occurrences per column after permissive SQLite decoding. This would show how much text was altered and whether affected columns (such as `comment`) matter for any analysis [src: pitfalls].
- Schema-parser regression test: run `parse_sql_schema` on dumps that have leading inline comments and on dumps that have MySQL DDL trailers, after preprocessing. The test would check whether either failure remains, since stripping the trailer alone does not address the leading-comment misparse [src: pitfalls].
