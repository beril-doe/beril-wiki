---
type: "Finding"
description: "The bacterial biome effect on CAZymes survived genome-size correction using Kruskal-Wallis tests on per-Mbp residuals and was significant within all 5 top phyla: Pseudomonadota, Firmicutes_A, Bacteroidota, Bacillota_A, and Actinomycetota."
finding_id: "cazyme_pangenome_ecology--1104ea25"
result: "observation"
source: "cazyme_pangenome_ecology"
quantities: [{"value": "5", "what": "top phyla in which the biome effect was significant", "unit": "", "denominator": "", "scope": ""}]
caveat: "Causal inference (environment shapes CAZyme repertoire vs. CAZyme repertoire determines environment) is not possible from this data alone."
first_added: "2026-11-24"
source_hash: "1ce54ec75c76a907e66fb3384355bc52bed7225dc2b7b0ae857f63fc93273712"
---
# Biome effect on CAZymes survives genome-size and phylum controls

The bacterial biome effect on CAZymes survived genome-size correction using Kruskal-Wallis tests on per-Mbp residuals and was significant within all 5 top phyla: Pseudomonadota, Firmicutes_A, Bacteroidota, Bacillota_A, and Actinomycetota. [src: cazyme_pangenome_ecology]

## Key figures

- **5**: top phyla in which the biome effect was significant [src: cazyme_pangenome_ecology]

## Evidence

> The effect survives genome-size correction (KW on per-Mbp residuals) and within-phylum stratification (significant in all 5 top phyla: Pseudomonadota, Firmicutes_A, Bacteroidota, Bacillota_A, Actinomycetota). [src: cazyme_pangenome_ecology]

From the report [[summaries/cazyme_pangenome_ecology__REPORT]].

## Caveat

Causal inference (environment shapes CAZyme repertoire vs. CAZyme repertoire determines environment) is not possible from this data alone. [src: cazyme_pangenome_ecology]

> Causal inference (environment shapes CAZyme repertoire vs. CAZyme repertoire determines environment) is not possible from this data alone. [src: cazyme_pangenome_ecology]

## Other caveats in this report

- In the bacterial CAZyme–pangenome analysis, genome_count severely confounded cloud_fraction (ρ = 0.913), indicating that much apparent openness reflects sampling effort rather than biology. [src: cazyme_pangenome_ecology]
- In the report's bacterial dataset, genome_count and cloud_fraction correlate at ρ = 0.913, making pangenome openness largely a sampling artifact and limiting biological interpretation. [src: cazyme_pangenome_ecology]
- The report presents the genome_count → cloud_fraction correlation of ρ = 0.913 as a methodological caution for pangenome openness studies using MGnify-scale catalogs. [src: cazyme_pangenome_ecology]
- The kescience_mgnify.genome_cazy dataset provides only 7 top-level CAZy classes, GH, GT, PL, CE, AA, CB, and CL, rather than individual CAZy families. [src: cazyme_pangenome_ecology]
- The report states that finer CAZyme substrate-specificity analysis would require arkinlab_dbcan, which contains only 1,161 MGnify genomes, or 2.3% of the catalog. [src: cazyme_pangenome_ecology]
