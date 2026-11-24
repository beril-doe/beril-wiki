---
type: "Finding"
description: "The bacterial CAZyme\u2013openness correlation was not statistically significant after BH correction in the remaining 7/10 tested phyla outside Bacillota_A, Bacteroidota, and Firmicutes_A."
finding_id: "cazyme_pangenome_ecology--b0a9cf4f"
result: "null result"
source: "cazyme_pangenome_ecology"
quantities: [{"value": "7/10", "what": "phyla tested without a significant correlation after BH correction", "unit": "", "denominator": "", "scope": ""}, {"value": "\u03c1 = 0.288", "what": "Spearman correlation in Bacillota_A", "unit": "", "denominator": "", "scope": ""}]
caveat: "The severe genome_count confound (\u03c1 = 0.913 between genome_count and cloud_fraction) means that pangenome openness in this dataset is largely a sampling artifact, limiting biological interpretation."
first_added: "2026-11-24"
source_hash: "1ce54ec75c76a907e66fb3384355bc52bed7225dc2b7b0ae857f63fc93273712"
---
# CAZyme–openness correlation not significant in most phyla tested

The bacterial CAZyme–openness correlation was not statistically significant after BH correction in the remaining 7/10 tested phyla outside Bacillota_A, Bacteroidota, and Firmicutes_A. [src: cazyme_pangenome_ecology]

## Key figures

- **7/10**: phyla tested without a significant correlation after BH correction [src: cazyme_pangenome_ecology]
- **ρ = 0.288**: Spearman correlation in Bacillota_A [src: cazyme_pangenome_ecology]

## Evidence

> Within-phylum analysis reveals the signal is lineage-specific: Bacillota_A (ρ = 0.288, p < 10^-18), Bacteroidota (ρ = 0.147, p < 10^-8), and Firmicutes_A (ρ = 0.105, p < 10^-4) show significant correlations after BH correction, while the remaining 7/10 phyla tested do not. [src: cazyme_pangenome_ecology]

From the report [[summaries/cazyme_pangenome_ecology__REPORT]].

## Caveat

The severe genome_count confound (ρ = 0.913 between genome_count and cloud_fraction) means that pangenome openness in this dataset is largely a sampling artifact, limiting biological interpretation. [src: cazyme_pangenome_ecology]

> However, the severe genome_count confound (ρ = 0.913 between genome_count and cloud_fraction) means that pangenome "openness" in this dataset is largely a sampling artifact, limiting biological interpretation. [src: cazyme_pangenome_ecology]

## Other caveats in this report

- In the bacterial CAZyme–pangenome analysis, genome_count severely confounded cloud_fraction (ρ = 0.913), indicating that much apparent openness reflects sampling effort rather than biology. [src: cazyme_pangenome_ecology]
- The report presents the genome_count → cloud_fraction correlation of ρ = 0.913 as a methodological caution for pangenome openness studies using MGnify-scale catalogs. [src: cazyme_pangenome_ecology]
- The kescience_mgnify.genome_cazy dataset provides only 7 top-level CAZy classes, GH, GT, PL, CE, AA, CB, and CL, rather than individual CAZy families. [src: cazyme_pangenome_ecology]
- The report states that finer CAZyme substrate-specificity analysis would require arkinlab_dbcan, which contains only 1,161 MGnify genomes, or 2.3% of the catalog. [src: cazyme_pangenome_ecology]
- Soil (34%) and marine (23%) genomes dominate the report's bacterial CAZyme dataset. [src: cazyme_pangenome_ecology]
