---
type: "Finding"
description: "The genuine NMDC biosample universe is 16,640 samples (`nmdc.metadata.biosample_set`), while the co-hosted NCBI mirror alongside it is 51.7M, a ~3,000\u00d7 difference with nothing in the names to signal it."
finding_id: "nmdc_context_audit--d8ef5d8f"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "16,640", "what": "samples in nmdc.metadata.biosample_set", "unit": "samples", "denominator": "", "scope": "genuine NMDC biosample universe"}, {"value": "51.7M", "what": "samples in the co-hosted NCBI mirror", "unit": "samples", "denominator": "", "scope": ""}, {"value": "~3,000\u00d7", "what": "scale difference between the two", "unit": "fold", "denominator": "", "scope": ""}]
caveat: "The link between the overloaded label and sub-optimal resource choice is inferred from gap analysis and prior-project usage skew, not from a directly observed wrong choice; costs are plausible, not measured."
first_added: "2026-10-27"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# Genuine NMDC biosamples are dwarfed by the co-hosted NCBI mirror

The genuine NMDC biosample universe is 16,640 samples (`nmdc.metadata.biosample_set`), while the co-hosted NCBI mirror alongside it is 51.7M, a ~3,000× difference with nothing in the names to signal it. [src: nmdc_context_audit]

## Key figures

- **16,640 samples**: samples in nmdc.metadata.biosample_set (scope genuine NMDC biosample universe) [src: nmdc_context_audit]
- **51.7M samples**: samples in the co-hosted NCBI mirror [src: nmdc_context_audit]
- **~3,000× fold**: scale difference between the two [src: nmdc_context_audit]

## Evidence

> A concrete scale trap: the genuine NMDC biosample universe is **16,640** samples (`nmdc.metadata.biosample_set`), while the co-hosted NCBI mirror alongside it is **51.7M** — a ~3,000× difference with nothing in the names to signal it. [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

The link between the overloaded label and sub-optimal resource choice is inferred from gap analysis and prior-project usage skew, not from a directly observed wrong choice; costs are plausible, not measured. [src: nmdc_context_audit]

> The overloaded label is not a cosmetic issue — the evidence is consistent with it driving the sub-optimal-resource selection the project set out to test (this is inferred from the gap analysis and prior-project usage skew, not from a directly observed wrong choice; see Limitations). A user who wants NMDC-curated microbiome metadata but pulls `nmdc.ncbi_biosamples` operates on the wrong data at 3,000× the scale; a user who searches only the `nmdc` tenant silently excludes the freshest MAG catalog; a user who cites `kbase.nmdc_neon` as NMDC mis-attributes an NSF program. Each such mistake would plausibly cost time and compute and weaken conclusions — the failure mode the knowledge layer is designed to prevent — though, as noted in Limitations, this is inferred from the gap analysis and prior-project reuse skew, not from a directly observed wrong choice. [src: nmdc_context_audit]

## Other caveats in this report

- The BERDL Data Atlas labels Rhea/GO reference ontologies under `nmdc_arkin` as NMDC integrated, blurring their external provenance. [src: nmdc_context_audit]
- `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` is forbidden for the stated principal even though `COUNT(*)` succeeds on the same tables; metadata and data reads have different access permissions. [src: nmdc_context_audit]
- `get_databases()` returns both dotted Iceberg and underscore Hive aliases for every tenant database; using the dotted form for de-duplication avoids double counting. [src: nmdc_context_audit]
- Earlier repository knowledge covers `nmdc_arkin` but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit]
- Provenance classes were inferred from schema, table properties, tenant metadata, and prior usage, without an exposed in-catalog ingestion manifest. [src: nmdc_context_audit]
