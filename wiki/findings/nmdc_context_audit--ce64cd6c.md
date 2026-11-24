---
type: "Finding"
description: "The 20 database names containing \"nmdc\" resolve to 7 real, maintained resources across three tenants (`nmdc`, `kbase`, plus broken user copies), falling into six provenance classes."
finding_id: "nmdc_context_audit--ce64cd6c"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "20", "what": "database names containing \"nmdc\"", "unit": "database names", "denominator": "", "scope": "KBase Data Lakehouse"}, {"value": "7", "what": "real, maintained resources", "unit": "resources", "denominator": "", "scope": ""}, {"value": "six", "what": "provenance classes", "unit": "classes", "denominator": "", "scope": ""}]
caveat: "Provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage, not from an ingestion manifest (none is exposed in-catalog)."
first_added: "2026-11-24"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# Twenty nmdc-named databases resolve to seven real resources

The 20 database names containing "nmdc" resolve to 7 real, maintained resources across three tenants (`nmdc`, `kbase`, plus broken user copies), falling into six provenance classes. [src: nmdc_context_audit]

## Key figures

- **20 database names**: database names containing "nmdc" (scope KBase Data Lakehouse) [src: nmdc_context_audit]
- **7 resources**: real, maintained resources [src: nmdc_context_audit]
- **six classes**: provenance classes [src: nmdc_context_audit]

## Evidence

> The 20 database names containing "nmdc" resolve to **7 real, maintained resources** across **three tenants** (`nmdc`, `kbase`, plus broken user copies), falling into six provenance classes: [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

Provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage, not from an ingestion manifest (none is exposed in-catalog). [src: nmdc_context_audit]

> - Provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage — not from an ingestion manifest (none is exposed in-catalog). [src: nmdc_context_audit]

## Other caveats in this report

- The report warns that treating the nmdc tenant as one coherent NMDC dataset will mis-scope or mis-attribute data. [src: nmdc_context_audit]
- The report infers that overloaded NMDC labeling drives suboptimal resource selection from gap analysis and prior-project usage skew, rather than a directly observed wrong choice. [src: nmdc_context_audit]
- The report considers wasted time and compute and weakened conclusions plausible consequences of NMDC resource-selection mistakes, not directly observed outcomes. [src: nmdc_context_audit]
- Access restrictions on `kbase.nmdc_*` database descriptions produced `ForbiddenException` and prevented capture of some metadata, potentially including steward-authored notes. [src: nmdc_context_audit]
- The audit assesses completeness relative to snapshot timestamps rather than live upstream NMDC/NCBI record counts, since external API comparisons were out of scope. [src: nmdc_context_audit]
