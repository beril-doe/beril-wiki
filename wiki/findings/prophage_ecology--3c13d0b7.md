---
type: "Finding"
description: "No individual TerL lineage showed significant environment-specific enrichment after FDR correction (0/500 tests), which the report takes to indicate that lineage-level environmental adaptation does not exceed what host phylogeny predicts."
finding_id: "prophage_ecology--3c13d0b7"
result: "null result"
source: "prophage_ecology"
quantities: [{"value": "0/500", "what": "TerL lineage-environment tests significant after FDR correction", "unit": "tests", "denominator": "500 tests", "scope": ""}, {"value": "824", "what": "lineages with \u22655 species analyzed for niche breadth by Shannon entropy", "unit": "lineages", "denominator": "", "scope": ""}]
caveat: "Prophage identification relied on eggNOG annotation proxies rather than dedicated detectors such as geNomad or VIBRANT, so domesticated remnants and bacterial homologs may inflate prevalence and the false positive rate is uncharacterized."
first_added: "2026-11-09"
source_hash: "58e5dfbe672d830cc749b46434bc92ecb328e31d5cb5f793a987c72994a7e0ed"
---
# No individual TerL lineage shows environment-specific enrichment beyond host phylogeny

No individual TerL lineage showed significant environment-specific enrichment after FDR correction (0/500 tests), which the report takes to indicate that lineage-level environmental adaptation does not exceed what host phylogeny predicts. [src: prophage_ecology]

## Key figures

- **0/500 tests**: TerL lineage-environment tests significant after FDR correction (denominator 500 tests) [src: prophage_ecology]
- **824 lineages**: lineages with ≥5 species analyzed for niche breadth by Shannon entropy [src: prophage_ecology]

## Evidence

> No individual TerL lineage showed significant environment-specific enrichment after FDR correction (0/500 tests), indicating that lineage-level environmental adaptation does not exceed what host phylogeny predicts. However, Shannon entropy analysis of 824 lineages with ≥5 species reveals: [src: prophage_ecology]

From the report [[summaries/prophage_ecology__REPORT]].

## Caveat

Prophage identification relied on eggNOG annotation proxies rather than dedicated detectors such as geNomad or VIBRANT, so domesticated remnants and bacterial homologs may inflate prevalence and the false positive rate is uncharacterized. [src: prophage_ecology]

> 1. **Annotation-based prophage identification**: We use eggNOG functional annotations as proxies for prophage genes, not dedicated prophage detection tools (e.g., geNomad, VIBRANT). This likely inflates prophage prevalence by including domesticated remnants and bacterial homologs of phage genes (e.g., bacterial integrases). The false positive rate is uncharacterized. [src: prophage_ecology]

## Other caveats in this report

- The authors caution that near-universal modules may include domesticated, defective prophage remnants; head, tail, and anti-defense may better indicate more complete elements. [src: prophage_ecology]
- Packaging, lysis, integration, and lysogenic regulation were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation; masking by near-universal prevalence is the authors’ interpretation. [src: prophage_ecology]
- Metagenomic prophage burden was inferred from genus-level pangenome scores through GTDB metadata and genus matching, rather than directly measured in the NMDC samples. [src: prophage_ecology]
- The report proposes, but does not directly test, a pH-sensitive lysogeny explanation for the positive pH correlations (rho=0.519 for packaging; 0.474 overall). [src: prophage_ecology]
- The co-occurrence results support the module definitions for the core backbone—packaging, lysis, and lysogenic regulation—less strongly for the accessory integration and anti-defense functions. [src: prophage_ecology]
