---
type: "Finding"
description: "Cross-tenant analyses occur in 77% (51/66) of audited BERIL projects, and realized use is concentrated on the kbase \u00d7 kescience axis (36 projects)."
finding_id: "berdl_data_atlas--a65ca624"
result: "observation"
source: "berdl_data_atlas"
quantities: [{"value": "77%", "what": "share of audited BERIL projects spanning multiple tenants", "unit": "percent", "denominator": "66 audited BERIL projects", "scope": "README-based audit"}, {"value": "51", "what": "audited projects that span multiple tenants", "unit": "projects", "denominator": "66 audited BERIL projects", "scope": ""}, {"value": "36", "what": "projects using the kbase \u00d7 kescience bridge", "unit": "projects", "denominator": "", "scope": "realized use concentrated on this axis"}]
caveat: "The realized-use audit is README-based, so mentions in research plans or notebook source may have been missed and true per-project tenant breadth is a lower bound."
first_added: "2026-11-12"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Most audited BERIL projects already span multiple tenants, mainly kbase with kescience

Cross-tenant analyses occur in 77% (51/66) of audited BERIL projects, and realized use is concentrated on the kbase × kescience axis (36 projects). [src: berdl_data_atlas]

## Key figures

- **77%**: share of audited BERIL projects spanning multiple tenants (denominator 66 audited BERIL projects; scope README-based audit) [src: berdl_data_atlas]
- **51 projects**: audited projects that span multiple tenants (denominator 66 audited BERIL projects) [src: berdl_data_atlas]
- **36 projects**: projects using the kbase × kescience bridge (scope realized use concentrated on this axis) [src: berdl_data_atlas]

## Evidence

> 4. **77% (51/66) of audited BERIL projects already span multiple tenants** — the lakehouse architecture is delivering on cross-program synergy. Realized use is concentrated on the `kbase × kescience` axis (36 projects). [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The realized-use audit is README-based, so mentions in research plans or notebook source may have been missed and true per-project tenant breadth is a lower bound. [src: berdl_data_atlas]

> - **Realized-use audit is README-based** — data-source mentions buried in research plans or in notebook source may have been missed. True per-project tenant breadth is a **lower bound**. [src: berdl_data_atlas]

## Other caveats in this report

- The 29 canonical keys include sample_id across 10 tenants and genome_id, ncbi_taxon_id, and feature_id across 9 each; 536 bridges are counted at tenant × topic cell granularity, not as validated record-level joins. [src: berdl_data_atlas]
- The unused-bridge ranking is based on schema-level join surface and project use only at audit time. [src: berdl_data_atlas]
- UC2 proposes testing prophage-mediated metal-resistance along the Oak Ridge contamination gradient using enigma ↔ phagefoundry (11 shared keys); this is a question, not a demonstrated effect. [src: berdl_data_atlas]
- UC3 proposes comparing GTDB clades and KBase species pangenomes using kbase ↔ refdata (11 shared keys); disagreement and gene-flow implications remain questions. [src: berdl_data_atlas]
- UC4 proposes linking environmental pathogen occurrence and biogeochemistry using nmdc ↔ protect (10 shared keys); occurrence is not reported as a result. [src: berdl_data_atlas]
