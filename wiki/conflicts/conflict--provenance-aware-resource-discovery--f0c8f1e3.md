<!-- tension-hash: f0c8f1e3efe3039f -->
# Metadata Availability Versus Interface Reliability in NMDC Table Discovery

This tension concerns whether table-level metadata can be relied on when discovering resources in the KBase Data Lakehouse. One project reports that metadata counts succeeded for the tables it audited from NMDC (the National Microbiome Data Collaborative). A central digest reports that the same kinds of metadata requests are unreliable or time out when made through the REST (Representational State Transfer, a web-service interface style) interface. The source text says these findings "are not contradictory because they concern different access surfaces" [src: nmdc_context_audit] [src: pitfalls]. They still matter together. The source text concludes that discovery cards should record the interface and query path used to establish each claim [src: nmdc_context_audit] [src: pitfalls]. This page is part of the argument in [[concepts/provenance-aware-resource-discovery]] that scale, provenance and access conditions must be shown together.

## Evidence Sides

**Metadata counts succeeded through Iceberg**

Iceberg metadata counts succeeded for the audited NMDC tables [src: nmdc_context_audit]. Here, Iceberg names the table-format access path through which these counts were obtained. This is a positive operational result, but its scope is limited to the tables the audit examined and to the Iceberg metadata path. It does not show that every interface returns counts reliably.

**REST count and schema calls are unreliable**

The pitfalls report finds the REST `/count` endpoint particularly unreliable for loops over many tables [src: pitfalls]. It also finds `/schema` prone to timeout on large tables [src: pitfalls]. Both are statements of operational fragility under specific conditions:
- iterating over many tables, for `/count`;
- large tables, for `/schema`.

The report does not show a universal failure of either endpoint.

## Possible Reconciliations

- **Hypothesis: the difference is in the access surface.** Iceberg catalog metadata and REST endpoints are different code paths, so success on one does not predict success on the other. The TENSION text itself takes this position [src: nmdc_context_audit] [src: pitfalls].
- **Hypothesis: the difference is in workload shape.** The audit may have issued a bounded set of count requests. The REST failures are tied to loops over many tables and to large tables. The same interface could therefore behave differently depending on how many tables are queried and how large they are.
- **Hypothesis: the difference is in table characteristics.** The audited NMDC tables may not include the large tables on which `/schema` times out. If so, the two findings sample different parts of the table-size range.

The supplied evidence does not report a direct test of any of these hypotheses.

## Resolving Work

- **Same-table comparison:** Take the audited NMDC tables, request counts and schemas through both Iceberg metadata and REST `/count` and `/schema`, and log success, failure and latency for each call. This tests whether the outcome depends on the interface when the table is held fixed.
- **Loop-size test:** Run REST `/count` in loops over increasing numbers of tables and record the point where failures begin. This tests whether the unreliability is driven by loop size rather than by the endpoint itself.
- **Table-size test:** Stratify tables by size and call `/schema` on each stratum, comparing timeout rates with Iceberg schema retrieval. This tests whether table size explains the timeouts.
- **Provenance field on discovery cards:** Add an interface/query-path field to discovery cards and audit existing count and schema claims for it. This tests how many published claims currently cannot be traced to an access surface.
