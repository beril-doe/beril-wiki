---
type: "Method"
description: "The Spark client-server interface used by Lakehouse notebooks, with strict SQL, result-size caps and fragile temporary views."
sources: ["summaries/gc_ecotype_ecology__REPORT.md", "summaries/pitfalls.md"]
---
# Spark Connect

This page covers Spark Connect, the Spark client-server interface used by Lakehouse notebooks, with strict SQL, result-size caps and fragile temporary views.

## Key facts

- The conservation_vs_fitness project reports that the Spark Connect service runs as a Java process on port 15002. [src: pitfalls]
- Its SQL analyzer rejects `SELECT DISTINCT` combined with an aggregate function when no `GROUP BY` is present (`MISSING_GROUP_BY`, SQLSTATE 42803). [src: pitfalls]
- This is a strict standard-SQL interpretation. Some other databases, such as DuckDB and SQLite, accept the syntax. [src: pitfalls]

## Result-size limits

- In the gene_function_ecological_agora project, joins of 1B-row tables were filtered to more than 200K elements via broadcast. Calling `.toPandas()` on the Spark Connect result hit `spark.driver.maxResultSize = 1024 MB` and threw a serialized-result-size error, as recorded in [[summaries/pitfalls]] and discussed in [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]]. [src: pitfalls]
- The cap cannot be raised with `SET spark.driver.maxResultSize` at runtime, because that property is read-only after session start. [src: pitfalls]

## Pandas conversion problems

- `df.to_parquet` on a Spark-Connect-derived pandas DataFrame fails with `TypeError: Object of type PlanMetrics is not JSON serializable` ([[summaries/gc_ecotype_ecology__REPORT]]). [src: gc_ecotype_ecology]
- The report's workaround is to rebuild the frame as `pd.DataFrame({c: df[c].to_numpy() for c in df.columns})`. This strips the Spark-side metadata before pyarrow serialization. [src: gc_ecotype_ecology]
- A pandas DataFrame from `.toPandas()` on Spark Connect has columns backed by PyArrow `ChunkedArray` objects. Passing it back to `spark.createDataFrame()` raises `TypeError: Cannot convert pyarrow.lib.ChunkedArray to pyarrow.lib.Array`. [src: pitfalls]
- This blocks the common pattern of pulling data to pandas, filtering it, and registering it as a Spark temporary view. [src: pitfalls]

## Fragile temporary views

- In nmdc_community_metabolic_ecology, a Spark temporary view registered in one cell may be silently destroyed if the server reconnects during that cell. An expensive 305M-row full-table scan is one example trigger. [src: pitfalls]
- Later cells that join against the lost view return 0 rows with no error. [src: pitfalls]

## Server failure and recovery

- Killing Java processes, for example when cleaning up stale notebook processes, takes down Spark Connect. `get_spark_session()` then fails with `RETRIES_EXCEEDED` or `Connection refused`. [src: pitfalls]
- Recovery means logging out of JupyterHub and starting a new session. Running `get_spark_session()` from a notebook then restarts the daemon. It cannot be restarted from the CLI. [src: pitfalls]
