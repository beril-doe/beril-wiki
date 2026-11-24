---
type: "Research direction"
description: "Why do projects disagree on whether turning off automatic broadcasting prevents failures or causes notebook hangs?"
hypothesis: "Disabling automatic broadcasting prevents failures when a very large table would be broadcast, but causes hangs on mid-size joins where broadcasting is cheap."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Controlled benchmark runs are needed; the catalog shows only reported runtimes with no baseline."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gene_cluster"]
findings: []
conflicts: ["conflict--spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses--694138ce"]
papers: []
builds_on: ["conflicts/conflict--spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses--694138ce"]
projects: ["cofitness_coinheritance", "gene_function_ecological_agora"]
topics: ["distributed-computation-and-analysis-execution"]
---
# Does disabling automatic broadcast joins help or hang Spark joins, depending on table size?

Why do projects disagree on whether turning off automatic broadcasting prevents failures or causes notebook hangs?

## Hypothesis

Disabling automatic broadcasting prevents failures when a very large table would be broadcast, but causes hangs on mid-size joins where broadcasting is cheap.

## Why it matters

It would replace conflicting advice with a rule keyed to table size, saving analysts lost notebook time.

## How to test it

Run one fixed UniProt-style join and several mid-size joins in clean sessions with the setting at -1 and at default, plus explicit hints. Record query plans, failures and hang time. Also run the presence-matrix extraction for one organism with and without hints.

## What would support or refute it

Support: the setting wins on the largest join and loses on mid-size ones. Refute: results are the same by size, so the earlier discrepancy came from session state.

## Data

Approach: experiment. Readiness: needs new measurements. Controlled benchmark runs are needed; the catalog shows only reported runtimes with no baseline.

## Builds on

- Conflict: [[conflicts/conflict--spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses--694138ce|Tension: Spark Broadcast Settings and Hints Across Lakehouse Analyses]]
