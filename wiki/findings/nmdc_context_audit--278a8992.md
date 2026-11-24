---
type: "Finding"
description: "The hypothesis (H1) is supported: the label is systematically overloaded, and every one of the four predicted confusion modes is realized by an actual resource."
finding_id: "nmdc_context_audit--278a8992"
result: "inference"
source: "nmdc_context_audit"
quantities: [{"value": "four", "what": "predicted confusion modes, all realized", "unit": "modes", "denominator": "", "scope": ""}]
caveat: "The link to sub-optimal resource selection is inferred from the gap analysis and prior-project usage skew, not from a directly observed wrong choice."
first_added: "2026-11-24"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# NMDC label is systematically overloaded

The hypothesis (H1) is supported: the label is systematically overloaded, and every one of the four predicted confusion modes is realized by an actual resource. [src: nmdc_context_audit]

## Key figures

- **four modes**: predicted confusion modes, all realized [src: nmdc_context_audit]

## Evidence

> The hypothesis (H1) is supported: the label is systematically overloaded, and every one of the four predicted confusion modes is realized by an actual resource. [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

The link to sub-optimal resource selection is inferred from the gap analysis and prior-project usage skew, not from a directly observed wrong choice. [src: nmdc_context_audit]

> The overloaded label is not a cosmetic issue — the evidence is consistent with it driving the sub-optimal-resource selection the project set out to test (this is inferred from the gap analysis and prior-project usage skew, not from a directly observed wrong choice; see Limitations). [src: nmdc_context_audit]

## Other caveats in this report

- The report warns that treating the nmdc tenant as one coherent NMDC dataset will mis-scope or mis-attribute data. [src: nmdc_context_audit]
- The report considers wasted time and compute and weakened conclusions plausible consequences of NMDC resource-selection mistakes, not directly observed outcomes. [src: nmdc_context_audit]
- The audit's provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage rather than an ingestion manifest, because none is exposed in the catalog. [src: nmdc_context_audit]
- Access restrictions on `kbase.nmdc_*` database descriptions produced `ForbiddenException` and prevented capture of some metadata, potentially including steward-authored notes. [src: nmdc_context_audit]
- The audit assesses completeness relative to snapshot timestamps rather than live upstream NMDC/NCBI record counts, since external API comparisons were out of scope. [src: nmdc_context_audit]
