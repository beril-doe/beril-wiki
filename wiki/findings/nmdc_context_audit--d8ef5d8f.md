---
type: "Finding"
description: "The genuine NMDC biosample universe is 16,640 samples (`nmdc.metadata.biosample_set`), while the co-hosted NCBI mirror alongside it is 51.7M, a ~3,000\u00d7 difference with nothing in the names to signal it."
finding_id: "nmdc_context_audit--d8ef5d8f"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "16,640", "what": "genuine NMDC biosamples", "unit": "samples", "denominator": "", "scope": "nmdc.metadata.biosample_set"}, {"value": "51.7M", "what": "samples in co-hosted NCBI mirror", "unit": "samples", "denominator": "", "scope": ""}, {"value": "~3,000\u00d7", "what": "size difference", "unit": "", "denominator": "", "scope": ""}]
caveat: "The \"nmdc\" tenant co-hosts a 51.7M-row NCBI BioSample mirror and Pfam vocabulary alongside genuine NMDC data; any project treating \"the nmdc tenant\" as one coherent NMDC dataset will mis-scope or mis-attribute."
first_added: "2026-11-24"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# Genuine NMDC biosamples are dwarfed by co-hosted NCBI mirror

The genuine NMDC biosample universe is 16,640 samples (`nmdc.metadata.biosample_set`), while the co-hosted NCBI mirror alongside it is 51.7M, a ~3,000× difference with nothing in the names to signal it. [src: nmdc_context_audit]

## Key figures

- **16,640 samples**: genuine NMDC biosamples (scope nmdc.metadata.biosample_set) [src: nmdc_context_audit]
- **51.7M samples**: samples in co-hosted NCBI mirror [src: nmdc_context_audit]
- **~3,000×**: size difference [src: nmdc_context_audit]

## Evidence

> A concrete scale trap: the genuine NMDC biosample universe is **16,640** samples (`nmdc.metadata.biosample_set`), while the co-hosted NCBI mirror alongside it is **51.7M** — a ~3,000× difference with nothing in the names to signal it. [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

The "nmdc" tenant co-hosts a 51.7M-row NCBI BioSample mirror and Pfam vocabulary alongside genuine NMDC data; any project treating "the nmdc tenant" as one coherent NMDC dataset will mis-scope or mis-attribute. [src: nmdc_context_audit]

> - The "nmdc" tenant co-hosts a 51.7M-row NCBI BioSample mirror and Pfam vocabulary alongside genuine NMDC data; substring ≠ provenance. Any project treating "the nmdc tenant" as one coherent NMDC dataset will mis-scope or mis-attribute. [src: nmdc_context_audit]

## Other caveats in this report

- The report infers that overloaded NMDC labeling drives suboptimal resource selection from gap analysis and prior-project usage skew, rather than a directly observed wrong choice. [src: nmdc_context_audit]
- The report considers wasted time and compute and weakened conclusions plausible consequences of NMDC resource-selection mistakes, not directly observed outcomes. [src: nmdc_context_audit]
- The audit's provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage rather than an ingestion manifest, because none is exposed in the catalog. [src: nmdc_context_audit]
- Access restrictions on `kbase.nmdc_*` database descriptions produced `ForbiddenException` and prevented capture of some metadata, potentially including steward-authored notes. [src: nmdc_context_audit]
- The audit assesses completeness relative to snapshot timestamps rather than live upstream NMDC/NCBI record counts, since external API comparisons were out of scope. [src: nmdc_context_audit]
