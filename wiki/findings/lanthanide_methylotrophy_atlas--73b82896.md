---
type: "Finding"
description: "A within-Acidobacteriota soil/sediment analysis retained enrichment (odds ratio 2.16, adjusted p = 2.2 \u00d7 10\u207b\u2075), suggesting at least part of the broader soil signal is not pure phylogenetic confounding."
finding_id: "lanthanide_methylotrophy_atlas--73b82896"
result: "observation"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "2.16", "what": "within-phylum odds ratio for xoxF in soil/sediment", "unit": "odds ratio", "denominator": "", "scope": "Acidobacteriota"}, {"value": "2.2 \u00d7 10\u207b\u2075", "what": "BH-adjusted p value", "unit": "", "denominator": "", "scope": ""}]
caveat: "H2 environmental analyses were stratified within phyla but not assessed with a fully phylogeny-aware mixed model."
first_added: "2026-10-27"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# Soil enrichment of xoxF persists within Acidobacteriota

A within-Acidobacteriota soil/sediment analysis retained enrichment (odds ratio 2.16, adjusted p = 2.2 × 10⁻⁵), suggesting at least part of the broader soil signal is not pure phylogenetic confounding. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **2.16 odds ratio**: within-phylum odds ratio for xoxF in soil/sediment (scope Acidobacteriota) [src: lanthanide_methylotrophy_atlas]
- **2.2 × 10⁻⁵**: BH-adjusted p value [src: lanthanide_methylotrophy_atlas]

## Evidence

> Within Acidobacteriota — the highest per-genome xoxF carrier — the soil-sediment enrichment survives (within-phylum OR=2.16, p_BH=2.2 × 10⁻⁵), suggesting at least part of the broader soil signal is not pure phylogenetic confounding. [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

H2 environmental analyses were stratified within phyla but not assessed with a fully phylogeny-aware mixed model. [src: lanthanide_methylotrophy_atlas]

> **H2 still relies on within-phylum stratified analyses rather than a fully phylogeny-aware mixed model** [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies. [src: lanthanide_methylotrophy_atlas]
- Environmental associations used per-class Fisher exact tests for any xoxF against a generic-environmental reference, with Benjamini–Hochberg correction. [src: lanthanide_methylotrophy_atlas]
- The REE-impacted class had only 37 genomes; its 10.81% xoxF rate and odds ratio 3.51 were descriptive, with adjusted p value 0.082. [src: lanthanide_methylotrophy_atlas]
- The report grades H2 as partially supported: soil/sediment and marine enrichment and host-associated depletion passed its correction, while the n=37 REE-impacted elevation did not pass the false-discovery-rate threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- Of 2,185 genomes with no eggNOG pqq, 1,288 (59%) had at least one bakta PQQ product. The other 897 (24% of all xoxF carriers) lacked evidence in both sources; assembly incompleteness, pseudogenization, and community-acquired PQQ remain unresolved without sequence-level inspection. [src: lanthanide_methylotrophy_atlas]
