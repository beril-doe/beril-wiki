---
type: "Concept"
description: "How Spark SQL numeric types and Arrow-backed pandas columns change or fail when data moves between the query engine and the analysis frame, and the casting and query-design practices that avoid it."
sources: ["summaries/pitfalls.md"]
---
# Numeric and Array Types Do Not Survive Transfers Between Query Engine and Analysis Frame

The [[entities/spark-sql]] engine and the pandas analysis frame do not share a type system. A value can change type when it is collected out of the engine or passed back into it. The central pitfalls digest documents two forms of this problem. Numeric columns can arrive in pandas as Python `decimal.Decimal` objects instead of floats. Pandas frames produced from Spark Connect can carry Arrow-backed columns that the engine refuses to take back in [src: pitfalls]. Both are recorded as operational caveats, not scientific findings. In the documented cases, both stop the calculation with an error (a `TypeError` or a `spark.createDataFrame()` failure). Whether either problem can also change results silently is an untested possibility that the digest does not cover [src: pitfalls].

Spark SQL `DECIMAL` columns are returned as Python `decimal.Decimal` objects when collected with `.toPandas()`. One example is `abundance` in `kbase.nmdc_arkin.centrifuge_gold` (see [[data/nmdc-arkin]]). Arithmetic between these values and `float` values, such as the results of `AVG()` aggregates, raises `TypeError: unsupported operand type(s) for *: 'float' and 'decimal.Decimal'` [src: pitfalls].

The mismatch can happen even when no column is declared `DECIMAL`. `AVG(CASE WHEN condition THEN 1.0 ELSE 0.0 END)` also returns `DECIMAL`, because Spark treats the literal `1.0` as `DECIMAL(2,1)`, not `DOUBLE` [src: pitfalls]. This **refines** the previous caveat. The risk depends on how the engine types an expression, so checking only the declared types of the source columns does not rule it out [src: pitfalls].

## Remedies

The digest gives two alternative remedies for the DECIMAL mismatch: `CAST(col AS DOUBLE)` in the SQL query, or `.astype(float)` on the pandas column after collection [src: pitfalls].

Its rule of thumb is to wrap any `AVG()` over integers or decimal literals in Spark SQL in `CAST(... AS DOUBLE)`. It also recommends adding `.astype(float)` after `.toPandas()` as a defensive safety net [src: pitfalls].

## Arrow-Backed Frames Do Not Round-Trip

When `.toPandas()` is called on a Spark Connect DataFrame, the resulting pandas DataFrame has columns backed by PyArrow `ChunkedArray` objects. Passing that DataFrame back to `spark.createDataFrame()` raises an error [src: pitfalls]. This is the reverse direction of the DECIMAL problem. The engine does not accept the column representation that its own collection step produced [src: pitfalls].

The digest's solution is to avoid the pandas-to-Spark roundtrip entirely. All filtering and joining stays in Spark SQL, using subqueries and the original table name. For bridge joins, the full table name goes directly into the SQL instead of the bridge being materialized as a temp view [src: pitfalls]. This **supports** a design principle shared with [[concepts/cross-tenant-data-bridging]] and [[concepts/driver-side-result-collection-limits]]: keep relational work inside the engine [src: pitfalls].

## Evidence Strength

All of these records come from one source, the central pitfalls digest ([[summaries/pitfalls]]). They describe engine behaviour together with the exact error messages and the recommended workarounds [src: pitfalls]. The assigned records do not say how many analyses or projects were affected or how often the errors occurred. The rule of thumb is therefore best read as defensive practice, not as a quantified failure rate [src: pitfalls]. A related set of failure modes is collected under [[concepts/silent-failure-modes-in-distributed-queries]].

## Open Directions

- Audit project notebooks for `AVG(CASE WHEN ... THEN 1.0 ELSE 0.0 END)` patterns that lack `CAST(... AS DOUBLE)`. Check whether any downstream arithmetic or proportion estimates depended on the `DECIMAL` result, to find out whether the caveat only raised errors or ever affected reported numbers [src: pitfalls].
- Inventory `DECIMAL`-typed columns across lakehouse tables, starting with `abundance` in `kbase.nmdc_arkin.centrifuge_gold`, so that collection code can apply `.astype(float)` systematically instead of case by case [src: pitfalls].
- Test whether the Spark Connect `ChunkedArray` failure in `spark.createDataFrame()` persists across client versions. This would show whether the advice to avoid the pandas-to-Spark roundtrip is permanent or depends on the version [src: pitfalls].
