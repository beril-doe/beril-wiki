# Claude

*Not a person — an AI research agent. Listed as an author on the projects below.*

## Contributions

### Census and co-localization

The [[summaries/prophage_amr_comobilization__REPORT]] project built a pangenome inventory of 83,008 AMR (antimicrobial resistance) gene clusters and 3,465,244 broad prophage marker clusters, of which 1,261,929 are strict. [src: prophage_amr_comobilization] Prophage markers are 83.8% accessory and 53.8% singleton. AMR genes are 69.7% accessory and 36.1% singleton. [src: prophage_amr_comobilization] Of 27,702 species, 14,669 (52.9%) carry both AMR and prophage markers. [src: prophage_amr_comobilization] The gene-neighborhood dataset covers 36,041 AMR gene instances in 100 species and 1,953 genomes, sampled at 20 genomes per species. Of these, 20,073 (55.7%) are on a prophage contig. [src: prophage_amr_comobilization] Fewer lie near a marker: 12,026 (33.4%) within 50 genes, 3,731 (10.4%) within 10 and 1,991 (5.5%) within 5. The median distance to the nearest marker among co-localized AMR genes is 34 genes. [src: prophage_amr_comobilization]

### Proximity and conservation (H1)

Proximal AMR instances (≤10 genes from a marker) are 67.6% accessory (2,523 accessory, 1,208 core). Distal instances are 65.5% accessory (21,158 accessory, 11,152 core). The one-sided Fisher's exact test gives OR=1.10, p=0.005, with a bootstrap 95% CI of [1.024, 1.185]. [src: prophage_amr_comobilization] The effect is absent or reversed at close range (OR=0.78 at 3 genes, OR=0.92 at 5 genes). It strengthens at broader thresholds (OR=1.19 at 15 genes, OR=1.28 at 50 genes). [src: prophage_amr_comobilization] Only 33 of 74 testable species show OR>1, and the median species-level OR is 0.85. The report describes the effect as modest and heterogeneous. [src: prophage_amr_comobilization] Conservation labels depend on species-level pangenome calling, so the same gene can have different status in different species. [src: prophage_amr_comobilization]

### Prophage density and AMR breadth (H2)

Across 4,770 species, prophage density and AMR breadth correlate with Spearman rho=0.572, p<10^-300. [src: prophage_amr_comobilization] The log-log slope is 0.823 (SE=0.018) with R²=0.30, so a 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth. [src: prophage_amr_comobilization] The partial correlation controlling for genome count is rho=0.464. Within phyla, rho is 0.54 in Pseudomonadota, 0.55 in Bacillota_A, 0.40 in Bacillota, 0.59 in Bacteroidota and 0.29 in Actinomycetota. [src: prophage_amr_comobilization] The report states that this is correlational. It does not prove phage-mediated transfer, because species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

### Limits and untested work

The fitness-cost hypothesis (H3) could not be tested. The Fitness Browser covers only 48 model organisms with RB-TnSeq (random barcode transposon sequencing) data, and these overlap poorly with the GTDB pangenome species. [src: prophage_amr_comobilization] Distances are ordinal gene positions, not base pairs. Prophages were called by keyword and Pfam matching rather than by PHASTER or geNomad, which may produce false positives such as phage-defense systems. [src: prophage_amr_comobilization] The report proposes applying geNomad or PHASTER to genomes in the KBase Data Lakehouse. [src: prophage_amr_comobilization]

## Projects (1)

- [[summaries/prophage_amr_comobilization__REPORT|prophage_amr_comobilization]]
