---
type: "Finding"
description: "Catalog tables carry no `Comment` and databases have empty `Properties` (owner `tgu2`), so there is zero human-readable context in the KBase Data Lakehouse itself."
finding_id: "nmdc_context_audit--99bbd8c1"
result: "null result"
source: "nmdc_context_audit"
quantities: []
caveat: "`kbase.nmdc_*` database descriptions are access-restricted (`ForbiddenException`), so some metadata, such as steward-authored notes if any, could not be captured."
first_added: "2026-10-27"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# The lakehouse catalog provides no human-readable context for NMDC resources

Catalog tables carry no `Comment` and databases have empty `Properties` (owner `tgu2`), so there is zero human-readable context in the KBase Data Lakehouse itself. [src: nmdc_context_audit]

## Evidence

> - **Catalog layer**: tables carry **no `Comment`**; databases have empty `Properties` (owner `tgu2`). Zero human-readable context in the lakehouse itself. [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

`kbase.nmdc_*` database descriptions are access-restricted (`ForbiddenException`), so some metadata, such as steward-authored notes if any, could not be captured. [src: nmdc_context_audit]

> - `kbase.nmdc_*` database descriptions are access-restricted (`ForbiddenException`), so some metadata (e.g. steward-authored notes, if any) could not be captured. [src: nmdc_context_audit]

## Other caveats in this report

- The BERDL Data Atlas labels Rhea/GO reference ontologies under `nmdc_arkin` as NMDC integrated, blurring their external provenance. [src: nmdc_context_audit]
- `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` is forbidden for the stated principal even though `COUNT(*)` succeeds on the same tables; metadata and data reads have different access permissions. [src: nmdc_context_audit]
- `get_databases()` returns both dotted Iceberg and underscore Hive aliases for every tenant database; using the dotted form for de-duplication avoids double counting. [src: nmdc_context_audit]
- The suggested link between overloaded labels and poor resource choice is inferred from gap analysis and prior-project usage skew, not a directly observed wrong choice. Costs to compute or conclusions are plausible, not measured. [src: nmdc_context_audit]
- Earlier repository knowledge covers `nmdc_arkin` but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit]
