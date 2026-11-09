---
type: "Finding"
description: "In constrained permutation tests, tail (log2 odds ratio 2.21, Z 10.86), head morphogenesis (1.98, 10.00) and anti-defense (1.70, 8.76) were enriched in human_associated species, while anti-defense was depleted in freshwater (-0.74, Z -4.74) and animal_associated (-0.24, Z -8.77)."
finding_id: "prophage_ecology--fc67e694"
result: "observation"
source: "prophage_ecology"
quantities: [{"value": "2.21", "what": "log2 odds ratio for tail enrichment in human_associated", "unit": "log2 odds ratio", "denominator": "", "scope": "Z = 10.86"}, {"value": "1.98", "what": "log2 odds ratio for head morphogenesis enrichment in human_associated", "unit": "log2 odds ratio", "denominator": "", "scope": "Z = 10.00"}, {"value": "1.70", "what": "log2 odds ratio for anti-defense enrichment in human_associated", "unit": "log2 odds ratio", "denominator": "", "scope": "Z = 8.76"}, {"value": "-0.74", "what": "log2 odds ratio for anti-defense depletion in freshwater", "unit": "log2 odds ratio", "denominator": "", "scope": "Z = -4.74"}]
caveat: "Sparse, inconsistently labeled NCBI isolation_source metadata was collapsed into 10 categories, and the \"other_unknown\" category (9,659 species, 35%) limits statistical power."
first_added: "2026-11-09"
source_hash: "58e5dfbe672d830cc749b46434bc92ecb328e31d5cb5f793a987c72994a7e0ed"
---
# Tail, head and anti-defense modules enriched in human-associated genomes against null models

In constrained permutation tests, tail (log2 odds ratio 2.21, Z 10.86), head morphogenesis (1.98, 10.00) and anti-defense (1.70, 8.76) were enriched in human_associated species, while anti-defense was depleted in freshwater (-0.74, Z -4.74) and animal_associated (-0.24, Z -8.77). [src: prophage_ecology]

## Key figures

- **2.21 log2 odds ratio**: log2 odds ratio for tail enrichment in human_associated (scope Z = 10.86) [src: prophage_ecology]
- **1.98 log2 odds ratio**: log2 odds ratio for head morphogenesis enrichment in human_associated (scope Z = 10.00) [src: prophage_ecology]
- **1.70 log2 odds ratio**: log2 odds ratio for anti-defense enrichment in human_associated (scope Z = 8.76) [src: prophage_ecology]
- **-0.74 log2 odds ratio**: log2 odds ratio for anti-defense depletion in freshwater (scope Z = -4.74) [src: prophage_ecology]

## Evidence

> | Tail | human_associated | 2.21 | 10.86 | Enriched | | Head Morphogenesis | human_associated | 1.98 | 10.00 | Enriched | | Anti-Defense | human_associated | 1.70 | 8.76 | Enriched | | Anti-Defense | human_clinical | 0.14 | 5.14 | Enriched | | Tail | human_clinical | 0.77 | 3.90 | Enriched | | Head Morphogenesis | human_clinical | 0.70 | 3.59 | Enriched | | Anti-Defense | freshwater | -0.74 | -4.74 | Depleted | | Anti-Defense | animal_associated | -0.24 | -8.77 | Depleted | [src: prophage_ecology]

From the report [[summaries/prophage_ecology__REPORT]].

## Caveat

Sparse, inconsistently labeled NCBI isolation_source metadata was collapsed into 10 categories, and the "other_unknown" category (9,659 species, 35%) limits statistical power. [src: prophage_ecology]

> 3. **Environment classification granularity**: NCBI isolation_source metadata is sparse and inconsistently labeled. Our classification into 10 categories collapses substantial within-category variation. The "other_unknown" category (9,659 species, 35%) limits statistical power. [src: prophage_ecology]

## Other caveats in this report

- The authors caution that near-universal modules may include domesticated, defective prophage remnants; head, tail, and anti-defense may better indicate more complete elements. [src: prophage_ecology]
- Packaging, lysis, integration, and lysogenic regulation were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation; masking by near-universal prevalence is the authors’ interpretation. [src: prophage_ecology]
- Metagenomic prophage burden was inferred from genus-level pangenome scores through GTDB metadata and genus matching, rather than directly measured in the NMDC samples. [src: prophage_ecology]
- The report proposes, but does not directly test, a pH-sensitive lysogeny explanation for the positive pH correlations (rho=0.519 for packaging; 0.474 overall). [src: prophage_ecology]
- The co-occurrence results support the module definitions for the core backbone—packaging, lysis, and lysogenic regulation—less strongly for the accessory integration and anti-defense functions. [src: prophage_ecology]
