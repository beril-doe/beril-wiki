---
type: "Method"
description: "Spark SQL is KBase Data Lakehouse's preferred interface for large and complex queries."
sources: ["summaries/pitfalls.md"]
---
# Spark SQL

## What it is

Spark SQL is the canonical name for the distributed SQL query interface used to analyze KBase Data Lakehouse data at scale. [src: pitfalls] Known aliases include `Spark SQL` and direct Spark SQL. [src: pitfalls] No stable external identifier is specified in `pitfalls`. [src: pitfalls]

## Key facts from pitfalls

Direct Spark SQL is preferred over the KBase Data Lakehouse REST API for complex or large queries because REST requests can return 504 Gateway Timeout, 524 Origin Timeout, 503 executor-restart errors, or empty responses. [src: pitfalls] The REST `/count` endpoint is particularly unreliable for loops over many tables, and `/schema` frequently times out on large tables. [src: pitfalls]

Many KBase Data Lakehouse numeric fields are stored as strings, including all Fitness Browser columns and relevant pangenome and genome metadata fields, so values must be explicitly cast before comparisons, ordering, arithmetic, or aggregation. [src: pitfalls] Spark `DECIMAL` values arrive in pandas as `decimal.Decimal`; using `CAST(... AS DOUBLE)` in SQL or `.astype(float)` after collection prevents mixed-type arithmetic failures. [src: pitfalls]

`SELECT DISTINCT col, COUNT(*)` without `GROUP BY` fails in Spark strict mode with `MISSING_GROUP_BY`; `GROUP BY col` alone is the correct replacement. [src: pitfalls] Spark Connect temporary views can disappear after a reconnect during a long-running query, so views should be re-registered immediately before use. [src: pitfalls]

The pangenome includes billion-row tables, including `gene` and `gene_genecluster_junction`, each approximately 1B rows; `genome_ani` is approximately 421M rows; `eggnog_mapper_annotations` approximately 93M rows; `interproscan_domains` approximately 833M rows; `bakta_db_xrefs` approximately 572M rows; and `gapmind_pathways` approximately 305M rows. [src: pitfalls] These tables require key filters before joins, and results should remain in Spark until the final small output. [src: pitfalls]

A Spark Connect driver result-size cap of 1 GB serialized data makes large `.toPandas()` collections unsafe. [src: pitfalls] A filtered contig-feature result involving 218K Bacteroidota contigs produced more than 30M rows and approximately 1.5 GB serialized, requiring MinIO parquet staging or server-side aggregation. [src: pitfalls]

Disabling `spark.sql.autoBroadcastJoinThreshold` with `-1` can harm performance: an NB10 job joining 13.7M rows with 18,989 species-taxonomy rows hung for 17+ minutes when automatic broadcasting was disabled. [src: pitfalls] The optimizer should generally be trusted, with explicit broadcast hints used only when needed. [src: pitfalls]

## Related pages

- [[summaries/pitfalls]] — source summary for the KBase Data Lakehouse database pitfalls document. [src: pitfalls]
- [[concepts/provenance-aware-resource-discovery]] — live catalog and schema discovery before querying. [src: pitfalls]
- [[concepts/cross-tenant-data-bridging]] — tenant, namespace, and cross-resource query considerations. [src: pitfalls]
- [[concepts/pangenome-integration]] — large pangenome tables and their join constraints. [src: pitfalls]
- [[concepts/multi-omics-integration]] — Spark-based handling of NMDC and other multi-omics resources. [src: pitfalls]
