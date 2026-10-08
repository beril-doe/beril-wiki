---
type: "Concept"
description: "How the REST interface, direct Spark SQL, hosted notebooks, cluster scripts and local machines each impose different access paths, failure signatures and limits on the same KBase Data Lakehouse analysis."
sources: ["summaries/pitfalls.md"]
---
The same query or analysis on the KBase Data Lakehouse does not behave the same way in every execution environment. In the cases the pitfalls digest records, the REST interface hits timeouts and rejects some query text, while direct [[entities/spark-sql]] handles the same work or accepts the same text. The digest recommends direct Spark as the alternative, but it does not show that direct Spark can never time out or fail. Spark session construction differs between hosted notebooks, cluster-side scripts and local machines. Off-cluster object-store access and Spark Connect daemon recovery each need steps specific to the environment. Together these operational records, collected in the central pitfalls digest ([[summaries/pitfalls]]), support the working claim that the access path is part of the method and should be reported with it [src: pitfalls].

## REST interface versus direct Spark SQL

| REST API error | Reported cause | Reported remedy |
|---|---|---|
| 504 Gateway Timeout | Query took too long | Simplify query, add filters, use direct Spark [src: pitfalls] |
| 524 Origin Timeout | Server didn't respond | Retry after a few seconds [src: pitfalls] |
| 503 "cannot schedule new futures after shutdown" | Spark executor restarting | Wait 30s, retry [src: pitfalls] |

The table above reproduces the digest's mapping of REST API status codes to causes and remedies [src: pitfalls].

The digest calls the REST `/count` endpoint particularly unreliable: it frequently returns errors or times out for tables that Spark queries handle instantly [src: pitfalls].

The REST `/schema` endpoint frequently times out for large tables. For more reliable schema introspection, the digest recommends running `DESCRIBE database.table` through the `/query` endpoint instead [src: pitfalls].

Query text that one path accepts can be rejected by the other. A double hyphen (`--`) inside a quoted species-clade identifier is not a problem in direct Spark SQL. The REST API, however, rejects any query containing `--` regardless of quoting, treating it as a SQL comment metacharacter, and returns a 400 error [src: pitfalls]. This **refines** the general contrast between REST and Spark: the difference is not only about scale and timeouts but also about which query strings are accepted at all [src: pitfalls].

The digest recommends direct `spark.sql()` on the cluster when a query involves >1M rows, JOINs across large tables or aggregations on billion-row tables, or when the REST API keeps timing out [src: pitfalls].

## Session construction differs by environment

The digest distinguishes three environments that use different import patterns to obtain a Spark session, and warns that using the wrong one causes `ImportError` [src: pitfalls].

- **JupyterHub notebooks**: `spark = get_spark_session()` works with no import, because `/configs/ipython_startup/00-notebookutils.py` injects the function [src: pitfalls].
- **Regular Python scripts on the cluster**: these need the explicit import `from berdl_notebook_utils.setup_spark_session import get_spark_session`, from the same module the notebooks use. The fitness_modules project found that this import works from regular Python scripts, not just notebooks [src: pitfalls].
- **Local machine**: the listed import is `from get_spark_session import get_spark_session`, which differs from the cluster-script import [src: pitfalls].
- **Failure signature**: calling bare `get_spark_session()` (no import) in a CLI script on JupyterHub raises `NameError`, because the auto-import only applies to notebook kernels [src: pitfalls].

## Off-cluster access and daemon recovery

When the MinIO client (`mc`) is used off-cluster, proxy environment variables must be set or commands time out [src: pitfalls].

The conservation_vs_fitness project reported that the Spark Connect service runs as a Java process on port 15002. Killing Java processes, for example while cleaning up stale notebook processes, takes down Spark Connect, after which `get_spark_session()` fails with `RETRIES_EXCEEDED` / `Connection refused` [src: pitfalls].

The reported recovery is to log out of JupyterHub, start a new session and run `get_spark_session()` from a notebook, which restarts the Spark Connect daemon. The daemon cannot be restarted from the CLI [src: pitfalls].

The ingest skill's `initialize()` is off-cluster-only. On JupyterHub, the digest advises bypassing `initialize()` and building Spark and MinIO clients directly [src: pitfalls].

## Evidence strength

These are operational observations from a cross-project pitfalls digest, several of them attributed to single projects. They are not systematic measurements of failure rates. The rule that the access path should be treated as part of the method is therefore well supported in practice but not backed by a quantified benchmark. The evidence also does not show that direct Spark is immune to timeouts; it only shows that the digest recommends direct Spark where REST fails [src: pitfalls]. Related failure classes are covered in [[concepts/silent-failure-modes-in-distributed-queries]], [[concepts/long-running-analysis-execution-reliability]] and [[concepts/driver-side-result-collection-limits]].

## Open Directions

- Run the same table counts and `DESCRIBE` calls through REST `/count`, `/schema` and `/query` and through direct Spark SQL, on tables of increasing size, and log the status codes and timeouts for each path. Measured failure rates per path would replace the qualitative description "frequently times out" and would test whether direct Spark also fails at scale [src: pitfalls].
- Add a check before submission that flags `--` in query text bound for the REST API, and record in each project's provenance which access path it used, so results can be traced to the environment that produced them [src: pitfalls].
- Provide a single session helper that detects whether it is running in a notebook, a cluster script or on a local machine, and test it against the `ImportError` and `NameError` failure signatures the digest lists [src: pitfalls].
