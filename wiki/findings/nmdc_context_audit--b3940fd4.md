---
type: "Finding"
description: "Two of the four databases in the `nmdc` tenant are external data re-hosted, not NMDC output: `nmdc.ncbi_biosamples` (an NCBI BioSample harvest with 51,711,888 biosamples and 756,112,544 attribute rows) and `nmdc.ref_data` (Pfam, 27,481 terms), while `nmdc_arkin`, `nmdc_mags` and `nmdc_neon` live in `kbase` and are invisible to anyone browsing the `nmdc` tenant."
finding_id: "nmdc_context_audit--b3940fd4"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "51,711,888", "what": "biosamples in nmdc.ncbi_biosamples", "unit": "biosamples", "denominator": "", "scope": "NCBI BioSample harvest"}, {"value": "756,112,544", "what": "attribute rows in nmdc.ncbi_biosamples", "unit": "rows", "denominator": "", "scope": ""}, {"value": "27,481", "what": "terms in nmdc.ref_data (Pfam)", "unit": "terms", "denominator": "", "scope": ""}]
caveat: "Provenance classes were inferred from schema, table properties, tenant metadata, and prior project usage, not from an ingestion manifest, since none is exposed in-catalog."
first_added: "2026-10-27"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# Half the nmdc tenant is re-hosted external data; NMDC databases sit elsewhere

Two of the four databases in the `nmdc` tenant are external data re-hosted, not NMDC output: `nmdc.ncbi_biosamples` (an NCBI BioSample harvest with 51,711,888 biosamples and 756,112,544 attribute rows) and `nmdc.ref_data` (Pfam, 27,481 terms), while `nmdc_arkin`, `nmdc_mags` and `nmdc_neon` live in `kbase` and are invisible to anyone browsing the `nmdc` tenant. [src: nmdc_context_audit]

## Key figures

- **51,711,888 biosamples**: biosamples in nmdc.ncbi_biosamples (scope NCBI BioSample harvest) [src: nmdc_context_audit]
- **756,112,544 rows**: attribute rows in nmdc.ncbi_biosamples [src: nmdc_context_audit]
- **27,481 terms**: terms in nmdc.ref_data (Pfam) [src: nmdc_context_audit]

## Evidence

> Two of the four databases in the `nmdc` tenant are **external data re-hosted**, not NMDC output: `nmdc.ncbi_biosamples` (an NCBI BioSample harvest — 51,711,888 biosamples, 756,112,544 attribute rows) and `nmdc.ref_data` (Pfam, 27,481 terms). Meanwhile, three NMDC-related databases live *outside* the tenant, in `kbase`: `nmdc_arkin`, `nmdc_mags`, `nmdc_neon`. Because the inventory groups by catalog prefix, these are filed under "kbase" and are invisible to anyone browsing the `nmdc` tenant. [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

Provenance classes were inferred from schema, table properties, tenant metadata, and prior project usage, not from an ingestion manifest, since none is exposed in-catalog. [src: nmdc_context_audit]

> - Provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage — not from an ingestion manifest (none is exposed in-catalog). [src: nmdc_context_audit]

## Other caveats in this report

- The BERDL Data Atlas labels Rhea/GO reference ontologies under `nmdc_arkin` as NMDC integrated, blurring their external provenance. [src: nmdc_context_audit]
- `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` is forbidden for the stated principal even though `COUNT(*)` succeeds on the same tables; metadata and data reads have different access permissions. [src: nmdc_context_audit]
- `get_databases()` returns both dotted Iceberg and underscore Hive aliases for every tenant database; using the dotted form for de-duplication avoids double counting. [src: nmdc_context_audit]
- The suggested link between overloaded labels and poor resource choice is inferred from gap analysis and prior-project usage skew, not a directly observed wrong choice. Costs to compute or conclusions are plausible, not measured. [src: nmdc_context_audit]
- Earlier repository knowledge covers `nmdc_arkin` but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit]
