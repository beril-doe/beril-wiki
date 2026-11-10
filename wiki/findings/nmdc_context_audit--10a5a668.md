---
type: "Finding"
description: "Last-commit dates range from 2026-03-09 for `nmdc.ncbi_biosamples` (stalest, ~4 months) to 2026-07-02 for `kbase.nmdc_mags` and `kbase.nmdc_neon`, with the other listed resources committed on 2026-05-20 or 2026-05-27."
finding_id: "nmdc_context_audit--10a5a668"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "2026-03-09", "what": "last commit of nmdc.ncbi_biosamples", "unit": "", "denominator": "", "scope": "stalest, ~4 months"}, {"value": "2026-07-02", "what": "last commit of kbase.nmdc_mags and kbase.nmdc_neon", "unit": "", "denominator": "", "scope": "freshest"}, {"value": "2026-05-27", "what": "last commit of kbase.nmdc_arkin", "unit": "", "denominator": "", "scope": "~6 weeks"}]
caveat: "Completeness was assessed relative to snapshot timestamps, not by diffing against live upstream NMDC or NCBI record counts."
first_added: "2026-10-27"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# Data currency varies by months across NMDC-labeled resources

Last-commit dates range from 2026-03-09 for `nmdc.ncbi_biosamples` (stalest, ~4 months) to 2026-07-02 for `kbase.nmdc_mags` and `kbase.nmdc_neon`, with the other listed resources committed on 2026-05-20 or 2026-05-27. [src: nmdc_context_audit]

## Key figures

- **2026-03-09**: last commit of nmdc.ncbi_biosamples (scope stalest, ~4 months) [src: nmdc_context_audit]
- **2026-07-02**: last commit of kbase.nmdc_mags and kbase.nmdc_neon (scope freshest) [src: nmdc_context_audit]
- **2026-05-27**: last commit of kbase.nmdc_arkin (scope ~6 weeks) [src: nmdc_context_audit]

## Evidence

> | `kbase.nmdc_mags` | 2026-07-02 | freshest (days) | | `kbase.nmdc_neon` | 2026-07-02 | fresh | | `kbase.nmdc_arkin` | 2026-05-27 | ~6 weeks | | `nmdc.metadata` / `nmdc.results` / `nmdc.ref_data` | 2026-05-20 | ~7 weeks | | `nmdc.ncbi_biosamples` | 2026-03-09 | **stalest (~4 months)** | [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

Completeness was assessed relative to snapshot timestamps, not by diffing against live upstream NMDC or NCBI record counts. [src: nmdc_context_audit]

> - Completeness is assessed relative to snapshot timestamps, not by diffing against live upstream NMDC/NCBI record counts (out of scope; would require external API calls). [src: nmdc_context_audit]

## Other caveats in this report

- The BERDL Data Atlas labels Rhea/GO reference ontologies under `nmdc_arkin` as NMDC integrated, blurring their external provenance. [src: nmdc_context_audit]
- `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` is forbidden for the stated principal even though `COUNT(*)` succeeds on the same tables; metadata and data reads have different access permissions. [src: nmdc_context_audit]
- `get_databases()` returns both dotted Iceberg and underscore Hive aliases for every tenant database; using the dotted form for de-duplication avoids double counting. [src: nmdc_context_audit]
- The suggested link between overloaded labels and poor resource choice is inferred from gap analysis and prior-project usage skew, not a directly observed wrong choice. Costs to compute or conclusions are plausible, not measured. [src: nmdc_context_audit]
- Earlier repository knowledge covers `nmdc_arkin` but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit]
