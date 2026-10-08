---
type: "Concept"
description: "How distributed queries on the KBase Data Lakehouse can fail quietly, returning plausible empty results or authorization errors that may not clearly identify the cause, and why empty results must be verified rather than trusted."
sources: ["summaries/pitfalls.md"]
---
# Distributed Queries Can Return Plausible Empty Results Instead of Errors

Several failure modes in the central pitfalls digest share one shape: the query does not stop with a clear error that names the cause. Instead it returns a result that looks valid but is empty, or it raises an error whose wording may not clearly identify the underlying problem. The working rule is that an empty or zero-row result from a distributed query must be checked independently before it is treated as a finding. Each mechanism below comes from operational reports in a single digest, not from measured failure rates. The rule is therefore a defensive practice, not a quantified risk estimate [src: pitfalls].

## Temporary Views Lost on Server Reconnection

A Spark temporary view registered in one notebook cell may be silently destroyed if the Spark Connect server reconnects during that cell, for example after an expensive 305M-row full-table scan. Later cells that JOIN against the view then return 0 rows with no error. On its own, a join that returns nothing cannot show that two datasets fail to overlap [src: pitfalls].

The recommended fix is to re-register the temporary view immediately before any cell that uses it in a JOIN. The Python variable holding the data persists in the kernel even when the Spark server reconnects, so the view can be rebuilt from that variable [src: pitfalls].

## Cold Databases: Valid Counts Alongside Empty Queries

For cold databases, the `/count` endpoint often returns correct results while the `/query` and `/sample` endpoints return 0 rows or empty results. An empty `/query` response can therefore appear alongside a valid nonzero `/count` for the same data. This **supports** the general rule, because the same empty-result signature arises here from a different cause than the temporary-view loss above [src: pitfalls].

The documented workaround is to use `/count` to verify that data exists, then retry `/query` with exponential backoff. The Spark cluster may take several minutes to warm up for a cold database, so a single immediate empty response is not evidence of absence [src: pitfalls].

## Permission Failures Surfacing as Storage or Catalog Errors

When a query fails because the current user does not have access to a table, the underlying error from S3 or the Spark catalog may say things like `S3 access denied`, `403 Forbidden`, `Token denied`, or `AccessControlException`. These messages may not clearly identify the table-permission problem. This case complements the empty-result cases: an error is raised, but its wording reflects the storage or catalog layer where the authorization failure surfaced. A reader could take it for a general storage fault rather than a missing table grant. Access lifecycle issues are covered further in [[concepts/credential-and-tenant-access-lifecycle]] [src: pitfalls].

## Synthesis

Across these cases, the absence of an error is not evidence of a correct result, and the wording of an error may not clearly identify its cause. The digest supports three practical checks. First, confirm that data exists with an independent count before trusting an empty query. Second, re-create session-scoped state such as temporary views right before it is used. Third, consider that storage-level authorization errors may reflect table-permission failures. All three come from the same single operational source and have not been tested against failure-rate data in this corpus. Related execution hazards appear in [[concepts/long-running-analysis-execution-reliability]] and [[concepts/driver-side-result-collection-limits]] [src: pitfalls].

## Open Directions

- Log the Spark Connect session identifier and the row count of each temporary view at the start of every join cell in long notebooks. This would measure how often a reconnection after a large full-table scan actually empties later joins, which is currently unquantified [src: pitfalls].
- Record paired `/count` and `/query` responses, with retry timestamps, for databases queried cold and warm. This would turn the qualitative warm-up delay of "several minutes" into an observed distribution and would test whether `/count` reliably flags data that `/query` has not yet returned [src: pitfalls].
- Build a lookup that maps S3 and Spark catalog error strings (`S3 access denied`, `403 Forbidden`, `Token denied`, `AccessControlException`) to confirmed causes from resolved access tickets. This would show how often each string actually reflects table permissions rather than other storage faults [src: pitfalls].
