---
type: "Finding"
description: "The report observes that heavy-in-lakehouse is not heavy-in-reuse: ENIGMA holds 36% of tables but appears in only 6 projects, PhageFoundry holds 14% / 5 projects, and PROTECT holds 4% / 2 projects, while kbase appears in 53/66 projects (80%)."
finding_id: "berdl_data_atlas--5f0ea1fc"
result: "observation"
source: "berdl_data_atlas"
quantities: [{"value": "36%", "what": "share of tables held by ENIGMA", "unit": "percent", "denominator": "", "scope": "appears in only 6 projects"}, {"value": "14%", "what": "share of tables held by PhageFoundry", "unit": "percent", "denominator": "", "scope": "appears in 5 projects"}, {"value": "53/66", "what": "audited projects using kbase", "unit": "projects", "denominator": "66 projects", "scope": "80%"}, {"value": "4%", "what": "share of tables held by PROTECT", "unit": "percent", "denominator": "", "scope": "appears in 2 projects"}]
caveat: "The realized-use audit is README-based and may miss mentions in plans or notebooks, so per-project tenant breadth is a lower bound."
first_added: "2026-11-12"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Tenant table shares and project reuse are sharply unequal across tenants

The report observes that heavy-in-lakehouse is not heavy-in-reuse: ENIGMA holds 36% of tables but appears in only 6 projects, PhageFoundry holds 14% / 5 projects, and PROTECT holds 4% / 2 projects, while kbase appears in 53/66 projects (80%). [src: berdl_data_atlas]

## Key figures

- **36%**: share of tables held by ENIGMA (scope appears in only 6 projects) [src: berdl_data_atlas]
- **14%**: share of tables held by PhageFoundry (scope appears in 5 projects) [src: berdl_data_atlas]
- **53/66 projects**: audited projects using kbase (denominator 66 projects; scope 80%) [src: berdl_data_atlas]
- **4%**: share of tables held by PROTECT (scope appears in 2 projects) [src: berdl_data_atlas]

## Evidence

> `kbase` appears in 53/66 projects (80%); `kescience` in 35/66 (53%); the `kbase ↔ kescience` realized bridge accounts for 36 cross-tenant projects on its own (mostly pangenome × fitness joins via `genome_id` and `ncbi_taxon_id`). Heavy-in-BERDL ≠ heavy-in-reuse: ENIGMA holds 36% of tables but appears in only 6 projects; PhageFoundry holds 14% / 5 projects; PROTECT holds 4% / 2 projects. [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The realized-use audit is README-based and may miss mentions in plans or notebooks, so per-project tenant breadth is a lower bound. [src: berdl_data_atlas]

> - **Realized-use audit is README-based** — data-source mentions buried in research plans or in notebook source may have been missed. True per-project tenant breadth is a **lower bound**. [src: berdl_data_atlas]

## Other caveats in this report

- The 29 canonical keys include sample_id across 10 tenants and genome_id, ncbi_taxon_id, and feature_id across 9 each; 536 bridges are counted at tenant × topic cell granularity, not as validated record-level joins. [src: berdl_data_atlas]
- The unused-bridge ranking is based on schema-level join surface and project use only at audit time. [src: berdl_data_atlas]
- UC2 proposes testing prophage-mediated metal-resistance along the Oak Ridge contamination gradient using enigma ↔ phagefoundry (11 shared keys); this is a question, not a demonstrated effect. [src: berdl_data_atlas]
- UC3 proposes comparing GTDB clades and KBase species pangenomes using kbase ↔ refdata (11 shared keys); disagreement and gene-flow implications remain questions. [src: berdl_data_atlas]
- UC4 proposes linking environmental pathogen occurrence and biogeochemistry using nmdc ↔ protect (10 shared keys); occurrence is not reported as a result. [src: berdl_data_atlas]
