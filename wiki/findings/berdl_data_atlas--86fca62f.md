---
type: "Finding"
description: "User-confirmed corrections assign phagefoundry to DOE BRaVE and msyscolo to DOE/NSF, replacing initial likely Defense/HHS and NSF/USDA inferences."
finding_id: "berdl_data_atlas--86fca62f"
result: "correction"
source: "berdl_data_atlas"
quantities: []
caveat: "The evaluation and lambda tenants remain unmapped to agencies, with 4 tables total and mappings not yet verified by program documentation."
first_added: "2026-11-24"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Tenant-to-agency mappings corrected for phagefoundry and msyscolo

User-confirmed corrections assign phagefoundry to DOE BRaVE and msyscolo to DOE/NSF, replacing initial likely Defense/HHS and NSF/USDA inferences. [src: berdl_data_atlas]

## Evidence

> `phagefoundry` and `msyscolo` were originally inferred as "likely" Defense/HHS and NSF/USDA; user-confirmed corrections (DOE BRaVE and DOE/NSF) have been folded in. [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The evaluation and lambda tenants remain unmapped to agencies, with 4 tables total and mappings not yet verified by program documentation. [src: berdl_data_atlas]

> **Two tenant→agency mappings are not yet verified by program documentation.** `evaluation` and `lambda` (4 tables total) remain unmapped. [src: berdl_data_atlas]

## Other caveats in this report

- The proposed structural fitness atlas join required correction because FitnessBrowser exposes (orgId, locusId), not protein_id, and its AlphaFold bridge runs through besthitswissprot.sprotAccession. [src: berdl_data_atlas]
- The proposed structural-fitness atlas bridge through protein_id was incorrect because FitnessBrowser uses a composite (orgId, locusId) primary key and does not expose protein_id. [src: berdl_data_atlas]
- The atlas references canonically cite catalogued data systems rather than biological hypotheses being tested. [src: berdl_data_atlas]
- Join value-space validity is established only for UC1; the bridge atlas establishes schema compatibility but not overlapping values. [src: berdl_data_atlas]
- The genome_id key has different meanings in KBase, NCBI, and MAG pipelines: UPA, accession, and hash, respectively. [src: berdl_data_atlas]
