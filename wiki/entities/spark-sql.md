---
type: Method
description: Spark SQL is BERDL's preferred interface for large and complex queries.
sources:
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
title: Spark SQL
---
# Spark SQL

## What it is

Spark SQL is the canonical name for the distributed SQL query interface used to analyze BERDL data at scale. [^pitfalls] Known aliases include `Spark SQL` and direct Spark SQL. [^pitfalls] No stable external identifier is specified in `pitfalls`. [^pitfalls]

## Key facts from pitfalls

Direct Spark SQL is preferred over the BERDL REST API for complex or large queries because REST requests can return 504 Gateway Timeout, 524 Origin Timeout, 503 executor-restart errors, or empty responses. [^pitfalls] The REST `/count` endpoint is particularly unreliable for loops over many tables, and `/schema` frequently times out on large tables. [^pitfalls]

Many BERDL numeric fields are stored as strings, including all Fitness Browser columns and relevant pangenome and genome metadata fields, so values must be explicitly cast before comparisons, ordering, arithmetic, or aggregation. [^pitfalls] Spark `DECIMAL` values arrive in pandas as `decimal.Decimal`; using `CAST(... AS DOUBLE)` in SQL or `.astype(float)` after collection prevents mixed-type arithmetic failures. [^pitfalls]

`SELECT DISTINCT col, COUNT(*)` without `GROUP BY` fails in Spark strict mode with `MISSING_GROUP_BY`; `GROUP BY col` alone is the correct replacement. [^pitfalls] Spark Connect temporary views can disappear after a reconnect during a long-running query, so views should be re-registered immediately before use. [^pitfalls]

The pangenome includes billion-row tables, including `gene` and `gene_genecluster_junction`, each approximately 1B rows; `genome_ani` is approximately 421M rows; `eggnog_mapper_annotations` approximately 93M rows; `interproscan_domains` approximately 833M rows; `bakta_db_xrefs` approximately 572M rows; and `gapmind_pathways` approximately 305M rows. [^pitfalls] These tables require key filters before joins, and results should remain in Spark until the final small output. [^pitfalls]

A Spark Connect driver result-size cap of 1 GB serialized data makes large `.toPandas()` collections unsafe. [^pitfalls] A filtered contig-feature result involving 218K Bacteroidota contigs produced more than 30M rows and approximately 1.5 GB serialized, requiring MinIO parquet staging or server-side aggregation. [^pitfalls]

Disabling `spark.sql.autoBroadcastJoinThreshold` with `-1` can harm performance: an NB10 job joining 13.7M rows with 18,989 species-taxonomy rows hung for 17+ minutes when automatic broadcasting was disabled. [^pitfalls] The optimizer should generally be trusted, with explicit broadcast hints used only when needed. [^pitfalls]

## Related pages

- [pitfalls](../summaries/pitfalls.md) — source summary for the BERDL database pitfalls document. [^pitfalls]
- [provenance-aware-resource-discovery](../concepts/provenance-aware-resource-discovery.md) — live catalog and schema discovery before querying. [^pitfalls]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — tenant, namespace, and cross-resource query considerations. [^pitfalls]
- [pangenome-integration](../concepts/pangenome-integration.md) — large pangenome tables and their join constraints. [^pitfalls]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — Spark-based handling of NMDC and other multi-omics resources. [^pitfalls]

[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
