---
type: "Finding"
description: "NMDC-derived data is split across two tenant homes (`nmdc.*` and `kbase.nmdc_*`) with no cross-link; the freshest NMDC resource (`kbase.nmdc_mags`, 62,346 MAGs) sits in the tenant a user is least likely to search for NMDC."
finding_id: "nmdc_context_audit--86d9733d"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "62,346", "what": "MAGs in kbase.nmdc_mags", "unit": "MAGs", "denominator": "", "scope": ""}]
caveat: "`kbase.nmdc_*` database descriptions are access-restricted (`ForbiddenException`), so some metadata (e.g. steward-authored notes, if any) could not be captured."
first_added: "2026-11-24"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# Freshest NMDC resource sits in the kbase tenant

NMDC-derived data is split across two tenant homes (`nmdc.*` and `kbase.nmdc_*`) with no cross-link; the freshest NMDC resource (`kbase.nmdc_mags`, 62,346 MAGs) sits in the tenant a user is least likely to search for NMDC. [src: nmdc_context_audit]

## Key figures

- **62,346 MAGs**: MAGs in kbase.nmdc_mags [src: nmdc_context_audit]

## Evidence

> - NMDC-derived data is split across two tenant homes (`nmdc.*` and `kbase.nmdc_*`) with no cross-link; the freshest NMDC resource (`kbase.nmdc_mags`, 62,346 MAGs) sits in the tenant a user is least likely to search for NMDC. [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

`kbase.nmdc_*` database descriptions are access-restricted (`ForbiddenException`), so some metadata (e.g. steward-authored notes, if any) could not be captured. [src: nmdc_context_audit]

> - `kbase.nmdc_*` database descriptions are access-restricted (`ForbiddenException`), so some metadata (e.g. steward-authored notes, if any) could not be captured. [src: nmdc_context_audit]

## Other caveats in this report

- The report warns that treating the nmdc tenant as one coherent NMDC dataset will mis-scope or mis-attribute data. [src: nmdc_context_audit]
- The report infers that overloaded NMDC labeling drives suboptimal resource selection from gap analysis and prior-project usage skew, rather than a directly observed wrong choice. [src: nmdc_context_audit]
- The report considers wasted time and compute and weakened conclusions plausible consequences of NMDC resource-selection mistakes, not directly observed outcomes. [src: nmdc_context_audit]
- The audit's provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage rather than an ingestion manifest, because none is exposed in the catalog. [src: nmdc_context_audit]
- The audit assesses completeness relative to snapshot timestamps rather than live upstream NMDC/NCBI record counts, since external API comparisons were out of scope. [src: nmdc_context_audit]
