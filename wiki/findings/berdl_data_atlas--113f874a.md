---
type: "Finding"
description: "At audit time, five high-leverage bridges had zero realized use: kescience \u2194 refdata (12 keys, including AlphaFold IDs), enigma \u2194 phagefoundry (11), kbase \u2194 refdata (11, including gtdb_taxonomy), nmdc \u2194 protect (10), and nmdc \u2194 refdata (9)."
finding_id: "berdl_data_atlas--113f874a"
result: "null result"
source: "berdl_data_atlas"
quantities: [{"value": "12", "what": "shared keys in kescience \u2194 refdata bridge", "unit": "keys", "denominator": "", "scope": "zero realized use at audit time"}, {"value": "11", "what": "shared keys in enigma \u2194 phagefoundry bridge", "unit": "keys", "denominator": "", "scope": ""}, {"value": "11", "what": "shared keys in kbase \u2194 refdata bridge", "unit": "keys", "denominator": "", "scope": ""}, {"value": "10", "what": "shared keys in nmdc \u2194 protect bridge", "unit": "keys", "denominator": "", "scope": ""}]
caveat: "The realized-use audit is README-based, so use mentioned only in research plans or notebook source may have been missed and per-project tenant breadth is a lower bound."
first_added: "2026-11-11"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Five high-leverage schema bridges had no recorded use at audit

At audit time, five high-leverage bridges had zero realized use: kescience ↔ refdata (12 keys, including AlphaFold IDs), enigma ↔ phagefoundry (11), kbase ↔ refdata (11, including gtdb_taxonomy), nmdc ↔ protect (10), and nmdc ↔ refdata (9). [src: berdl_data_atlas]

## Key figures

- **12 keys**: shared keys in kescience ↔ refdata bridge (scope zero realized use at audit time) [src: berdl_data_atlas]
- **11 keys**: shared keys in enigma ↔ phagefoundry bridge [src: berdl_data_atlas]
- **11 keys**: shared keys in kbase ↔ refdata bridge [src: berdl_data_atlas]
- **10 keys**: shared keys in nmdc ↔ protect bridge [src: berdl_data_atlas]

## Evidence

> 5. **Five high-leverage bridges had zero realized use at audit time**: `kescience ↔ refdata` (12 keys, including AlphaFold IDs), `enigma ↔ phagefoundry` (11), `kbase ↔ refdata` (11, including `gtdb_taxonomy`), `nmdc ↔ protect` (10), `nmdc ↔ refdata` (9). Five concrete use cases derived from these bridges are documented (UC1–UC5). [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The realized-use audit is README-based, so use mentioned only in research plans or notebook source may have been missed and per-project tenant breadth is a lower bound. [src: berdl_data_atlas]

> - **Realized-use audit is README-based** — data-source mentions buried in research plans or in notebook source may have been missed. True per-project tenant breadth is a **lower bound**. [src: berdl_data_atlas]

## Other caveats in this report

- The 29 canonical keys include sample_id across 10 tenants and genome_id, ncbi_taxon_id, and feature_id across 9 each; 536 bridges are counted at tenant × topic cell granularity, not as validated record-level joins. [src: berdl_data_atlas]
- The unused-bridge ranking is based on schema-level join surface and project use only at audit time. [src: berdl_data_atlas]
- UC2 proposes testing prophage-mediated metal-resistance along the Oak Ridge contamination gradient using enigma ↔ phagefoundry (11 shared keys); this is a question, not a demonstrated effect. [src: berdl_data_atlas]
- UC3 proposes comparing GTDB clades and KBase species pangenomes using kbase ↔ refdata (11 shared keys); disagreement and gene-flow implications remain questions. [src: berdl_data_atlas]
- UC4 proposes linking environmental pathogen occurrence and biogeochemistry using nmdc ↔ protect (10 shared keys); occurrence is not reported as a result. [src: berdl_data_atlas]
