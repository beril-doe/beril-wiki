---
type: "Finding"
description: "77% (51/66) of audited BERIL projects already span multiple tenants, which the report reads as the lakehouse architecture delivering on cross-program synergy."
finding_id: "berdl_data_atlas--d19ee80c"
result: "observation"
source: "berdl_data_atlas"
quantities: [{"value": "77%", "what": "share of audited BERIL projects spanning multiple tenants", "unit": "", "denominator": "", "scope": ""}, {"value": "51/66", "what": "cross-tenant projects out of audited projects", "unit": "projects", "denominator": "", "scope": ""}]
caveat: "The realized-use audit is README-based, so data-source mentions in research plans or notebook source may have been missed and true per-project tenant breadth is a lower bound."
first_added: "2026-11-24"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Most audited BERIL projects already span multiple lakehouse tenants

77% (51/66) of audited BERIL projects already span multiple tenants, which the report reads as the lakehouse architecture delivering on cross-program synergy. [src: berdl_data_atlas]

## Key figures

- **77%**: share of audited BERIL projects spanning multiple tenants [src: berdl_data_atlas]
- **51/66 projects**: cross-tenant projects out of audited projects [src: berdl_data_atlas]

## Evidence

> **77% (51/66) of audited BERIL projects already span multiple tenants** — the lakehouse architecture is delivering on cross-program synergy. [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The realized-use audit is README-based, so data-source mentions in research plans or notebook source may have been missed and true per-project tenant breadth is a lower bound. [src: berdl_data_atlas]

> **Realized-use audit is README-based** — data-source mentions buried in research plans or in notebook source may have been missed. True per-project tenant breadth is a **lower bound**. [src: berdl_data_atlas]

## Other caveats in this report

- The proposed structural fitness atlas join required correction because FitnessBrowser exposes (orgId, locusId), not protein_id, and its AlphaFold bridge runs through besthitswissprot.sprotAccession. [src: berdl_data_atlas]
- The proposed structural-fitness atlas bridge through protein_id was incorrect because FitnessBrowser uses a composite (orgId, locusId) primary key and does not expose protein_id. [src: berdl_data_atlas]
- The atlas references canonically cite catalogued data systems rather than biological hypotheses being tested. [src: berdl_data_atlas]
- Join value-space validity is established only for UC1; the bridge atlas establishes schema compatibility but not overlapping values. [src: berdl_data_atlas]
- The genome_id key has different meanings in KBase, NCBI, and MAG pipelines: UPA, accession, and hash, respectively. [src: berdl_data_atlas]
