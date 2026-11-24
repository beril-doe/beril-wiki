---
type: "Summary"
description: "Summary of the project CAZyme Pangenome Ecology — Carbohydrate Metabolism Distribution Across 49K Bacterial Genomes."
doc_type: "short"
full_text: "sources/cazyme_pangenome_ecology__REPORT.md"
---
# CAZyme Pangenome Ecology — Carbohydrate Metabolism Distribution Across 49K Bacterial Genomes

This report asks how carbohydrate-active enzyme (CAZyme) content differs across bacterial biomes, and whether CAZyme density tracks pangenome openness. It analyzed 49K genomes across 18 biomes. [src: cazyme_pangenome_ecology] Biome differences are very strong and survive genome-size and phylum controls. [src: cazyme_pangenome_ecology] The CAZyme–openness link is real but modest, and it appears only in some lineages. [src: cazyme_pangenome_ecology] The report itself says its data cannot establish causal direction, and that pangenome openness here is largely a sampling artifact. [src: cazyme_pangenome_ecology]

## Key Findings

### Biome differences in CAZyme composition

All 6 non-zero CAZy classes differed across 18 biomes (Kruskal-Wallis, KW, tests; all p < 10^-150 after Benjamini-Hochberg false discovery rate, BH-FDR, correction). [src: cazyme_pangenome_ecology] The effect survived genome-size correction (KW on per-Mbp residuals). It was significant within all 5 top phyla: Pseudomonadota, Firmicutes_A, Bacteroidota, Bacillota_A and Actinomycetota. [src: cazyme_pangenome_ecology] Class CL was all zeros and was excluded. [src: cazyme_pangenome_ecology]

| Class | KW H | BH p |
|---|---|---|
| GT | 12,524 | ≈ 0 [src: cazyme_pangenome_ecology] |
| GH | 7,793 | ≈ 0 [src: cazyme_pangenome_ecology] |
| CB | 7,527 | ≈ 0 [src: cazyme_pangenome_ecology] |
| CE | 2,584 | ≈ 0 [src: cazyme_pangenome_ecology] |
| PL | 893 | 1.1 × 10^-180 [src: cazyme_pangenome_ecology] |
| AA | 767 | 8.3 × 10^-154 [src: cazyme_pangenome_ecology] |

Glycoside hydrolase (GH) genes were 3–4× more abundant in fiber-rich environments than in marine genomes. The means were sheep-rumen 28.9, tomato-rhizosphere 31.9, barley-rhizosphere 37.7 and soil 23.5, against marine 9.0. [src: cazyme_pangenome_ecology] Glycosyl transferase (GT) genes were enriched in soil (22.8) and rhizosphere (20–25) relative to gut biomes (~11–13). The report calls this consistent with exopolysaccharide and biofilm biosynthesis demands. [src: cazyme_pangenome_ecology] Total CAZyme load spans 3.5×, from barley-rhizosphere (68.5) to marine (21.9). [src: cazyme_pangenome_ecology]

The report interprets the strong biome signal as reflecting the constraint that carbohydrate substrate availability places on bacterial genomes. [src: cazyme_pangenome_ecology] It states that fiber-rich rumen, soil and rhizosphere environments select for extensive GH repertoires for polysaccharide degradation. [src: cazyme_pangenome_ecology] It states that oligotrophic marine environments produce genomes with relatively more GT for protective capsules and exopolysaccharides. [src: cazyme_pangenome_ecology] These are interpretations, not direct tests.

Per-biome means (genomes; total CAZy; GH; GT; genome length in Mbp; MAG %):

| Biome | n | Total | GH | GT | Mbp | MAG % |
|---|---|---|---|---|---|---|
| barley-rhizo. | 74 | 68.5 | 37.7 | 24.6 | 4.4 | 67.6 [src: cazyme_pangenome_ecology] |
| tomato-rhizo. | 471 | 60.2 | 31.9 | 22.0 | 4.1 | 95.1 [src: cazyme_pangenome_ecology] |
| soil | 16,628 | 50.7 | 23.5 | 22.8 | 3.9 | 99.1 [src: cazyme_pangenome_ecology] |
| maize-rhizo. | 265 | 50.4 | 25.4 | 19.9 | 3.9 | 94.3 [src: cazyme_pangenome_ecology] |
| sheep-rumen | 1,871 | 49.4 | 28.9 | 15.8 | 2.2 | 99.9 [src: cazyme_pangenome_ecology] |
| zebrafish-fecal | 67 | 41.5 | 19.3 | 18.2 | 4.0 | 100.0 [src: cazyme_pangenome_ecology] |
| cow-rumen | 2,729 | 39.1 | 23.7 | 11.7 | 2.3 | 100.0 [src: cazyme_pangenome_ecology] |
| mouse-gut | 2,847 | 36.2 | 20.0 | 12.9 | 2.5 | 95.4 [src: cazyme_pangenome_ecology] |
| honeybee-gut | 128 | 35.1 | 14.8 | 18.4 | 2.7 | 74.2 [src: cazyme_pangenome_ecology] |
| human-skin | 476 | 32.8 | 14.0 | 15.0 | 2.6 | 88.7 [src: cazyme_pangenome_ecology] |
| marine-sed. | 5,169 | 32.5 | 14.6 | 15.6 | 2.9 | 95.1 [src: cazyme_pangenome_ecology] |
| human-gut | 4,158 | 31.4 | 16.6 | 12.2 | 2.4 | 80.3 [src: cazyme_pangenome_ecology] |
| chicken-gut | 1,286 | 30.5 | 16.4 | 11.4 | 2.3 | 100.0 [src: cazyme_pangenome_ecology] |
| pig-gut | 1,263 | 30.1 | 16.8 | 10.8 | 2.1 | 100.0 [src: cazyme_pangenome_ecology] |
| non-model-fish | 152 | 30.0 | 15.0 | 12.4 | 2.3 | 100.0 [src: cazyme_pangenome_ecology] |
| human-oral | 408 | 25.2 | 11.3 | 11.5 | 1.8 | 100.0 [src: cazyme_pangenome_ecology] |
| marine | 11,132 | 21.9 | 9.0 | 11.0 | 2.4 | 99.5 [src: cazyme_pangenome_ecology] |
| human-vaginal | 249 | 20.5 | 8.9 | 9.0 | 1.7 | 100.0 [src: cazyme_pangenome_ecology] |

### GT/GH ratio as a proposed biome indicator

The report proposes the ratio of biosynthetic GT to degradative GH CAZymes as a novel ecological biome indicator of the dominant carbohydrate metabolic strategy. [src: cazyme_pangenome_ecology] It describes the ratio as separating primarily carbohydrate-consuming (GH-dominant) genomes from carbohydrate-producing (GT-dominant) ones. [src: cazyme_pangenome_ecology] This is a proposal built on the measurements above. Its explanations are interpretations, not tests.
- Marine: 71% of genomes had GT > GH, read as glycan investment in capsules, biofilms and cell-surface structures in oligotrophic waters. [src: cazyme_pangenome_ecology] The report says this was not previously reported. [src: cazyme_pangenome_ecology]
- Rumen: 74% of genomes had GH > GT, read as reflecting fiber-rich substrates. [src: cazyme_pangenome_ecology] The report says this was also not previously reported. [src: cazyme_pangenome_ecology]
- Soil: GT ≈ GH, read as dual demands for plant-polysaccharide degradation and EPS biosynthesis. [src: cazyme_pangenome_ecology]

### Phylum structure

Soil Bacteroidota carried a mean of 65.3 GH genes. This was the highest phylum–biome combination and 2.8× the Bacteroidota average across biomes. [src: cazyme_pangenome_ecology] The report says the magnitude of this soil enrichment had not previously been quantified at genome-resolved scale. [src: cazyme_pangenome_ecology] It also says the figure quantifies the specialization at pan-bacterial scale for the first time. [src: cazyme_pangenome_ecology] Bacteroidota had the most GH-skewed profiles, and Pseudomonadota were relatively GT-enriched. [src: cazyme_pangenome_ecology]

### CAZymes and pangenome openness

Across n = 9,347 species with ≥3 genomes, CAZyme density correlated modestly with pangenome cloud fraction (Spearman ρ = 0.153, p < 10^-50). [src: cazyme_pangenome_ecology] Genome count strongly confounded cloud fraction (ρ = 0.913), so much apparent openness reflects sampling effort rather than biology. [src: cazyme_pangenome_ecology] After partial correlation controlling for genome size and genome count, the correlation fell to ρ = 0.101. [src: cazyme_pangenome_ecology] The report presents the ρ = 0.913 confound as a methodological caution for all pangenome openness studies using MGnify-scale catalogs. [src: cazyme_pangenome_ecology] It adds that species with few sequenced genomes appear closed regardless of true gene flux. [src: cazyme_pangenome_ecology]

Within phyla the signal is lineage-specific. Three phyla were significant after BH correction, and the remaining 7/10 tested were not. [src: cazyme_pangenome_ecology] The report calls the signal real but modest and concentrated in carbohydrate-specialist lineages. [src: cazyme_pangenome_ecology] It suggests CAZymes are part of the accessory gene pool in specific lineages, particularly Bacillota_A and Bacteroidota. [src: cazyme_pangenome_ecology] It describes this as consistent with niche-adaptive accessory CAZymes in specific lineages rather than a universal pattern. [src: cazyme_pangenome_ecology]

| Phylum | Species | ρ | BH p | Significant |
|---|---|---|---|---|
| Bacillota_A | 939 | 0.288 | 2.2 × 10^-18 | Yes [src: cazyme_pangenome_ecology] |
| Bacteroidota | 1,618 | 0.147 | 1.3 × 10^-8 | Yes [src: cazyme_pangenome_ecology] |
| Firmicutes_A | 1,625 | 0.105 | 7.8 × 10^-5 | Yes [src: cazyme_pangenome_ecology] |
| Pseudomonadota | 1,689 | −0.013 | 0.74 | No [src: cazyme_pangenome_ecology] |
| Actinomycetota | 385 | −0.094 | 0.13 | No [src: cazyme_pangenome_ecology] |
| Firmicutes | 364 | 0.065 | 0.30 | No [src: cazyme_pangenome_ecology] |
| Actinobacteriota | 335 | 0.071 | 0.30 | No [src: cazyme_pangenome_ecology] |
| Thermoplasmatota | 289 | 0.112 | 0.13 | No [src: cazyme_pangenome_ecology] |
| Bacillota | 238 | 0.022 | 0.74 | No [src: cazyme_pangenome_ecology] |
| Verrucomicrobiota | 215 | −0.024 | 0.74 | No [src: cazyme_pangenome_ecology] |

### Relation to published work

The report positions its results against earlier studies.
- It says its biome-specific enrichment aligns with López-Sánchez et al. (2024), who found more abundant and diverse CAZymes in soil MAGs than marine sediment MAGs within Bacteroidia, Gammaproteobacteria and Alphaproteobacteria. [src: cazyme_pangenome_ecology] It says its work extends this from 37 sediment sites to 18 biomes at 49K-genome scale. [src: cazyme_pangenome_ecology]
- It calls its polymeric carbohydrate niche separation consistent with Sun et al. (2023), who showed different CAZyme compositions in free-living and particle-associated marine bacteria. [src: cazyme_pangenome_ecology] It says its analysis extends this within-marine observation to a pan-environmental framework. [src: cazyme_pangenome_ecology]
- It cites Huang et al. (2023) on Bacteroidota's successional role in paddy-soil straw decomposition, with the highest proportion of total GHs and the most CAZyme gene clusters. [src: cazyme_pangenome_ecology] It cites Nweze et al. (2024) on Bacteroidota as primary complex-carbon degraders in arthropod guts. [src: cazyme_pangenome_ecology]
- It cites Pudlo et al. (2022), who found wide carbohydrate-utilization variation across 354 gut Bacteroidetes isolates. [src: cazyme_pangenome_ecology] It says its analysis extends this single-clade, single-biome study to a pan-bacterial, multi-biome comparison. [src: cazyme_pangenome_ecology]
- It cites White et al. (2022), who found different selection pressures on core and accessory genomes of Bacillus cereus clades. [src: cazyme_pangenome_ecology] It cites Andrade et al. (2017), who found environment-specific differences between freshwater and soil CAZyme metagenomes in the Caatinga. [src: cazyme_pangenome_ecology]
- It claims the first genome-resolved CAZyme class-composition analysis across 18 biomes at 49K-genome scale. [src: cazyme_pangenome_ecology]

## Data and Methods

The report uses the kescience_mgnify tables genome, genome_cazy and pangenome_stats for metadata, CAZy class counts and pangenome statistics for 49K genomes across 18 biomes. [src: cazyme_pangenome_ecology] MAGs (metagenome assembled genomes) made up 96% of the dataset. [src: cazyme_pangenome_ecology] Within-biome Mann-Whitney tests found no significant difference in total CAZyme counts between isolates and MAGs (all Cohen's d < 0.21). The report takes this as validating that MAG incompleteness does not drive the biome patterns. [src: cazyme_pangenome_ecology] The table kescience_mgnify.genome_cazy has ~345K rows and joined cleanly to kescience_mgnify.genome on genome_id. [src: cazyme_pangenome_ecology] Pivoting 49K genomes × 7 CAZy classes took seconds in pandas, with no Spark needed. [src: cazyme_pangenome_ecology] kescience_mgnify.pangenome_stats is pre-computed. [src: cazyme_pangenome_ecology]

## Caveats and Open Work

- Sampling effort confounds apparent pangenome openness, so the openness association is weak after controls. [src: cazyme_pangenome_ecology]
- The openness signal is absent in most phyla tested. [src: cazyme_pangenome_ecology]
- The GT/GH interpretations (capsules, biofilms, fiber substrates) are the report's readings, not direct tests. [src: cazyme_pangenome_ecology]
- The genome_cazy table gives only 7 top-level classes (GH, GT, PL, CE, AA, CB, CL), not families. [src: cazyme_pangenome_ecology] Family-level work needs arkinlab_dbcan, which has only 1,161 MGnify genomes, 2.3% of the catalog. [src: cazyme_pangenome_ecology]
- Soil (34%) and marine (23%) dominate the dataset. [src: cazyme_pangenome_ecology] Rare biomes (barley-rhizosphere n=74, zebrafish-fecal n=67) have limited statistical power. [src: cazyme_pangenome_ecology]
- Incomplete MAGs may still undercount absolute CAZyme abundance, despite no systematic isolate–MAG bias within biomes. [src: cazyme_pangenome_ecology]
- Phylogeny was controlled by within-phylum stratification, not formal regression such as PGLS (phylogenetic generalized least squares), which would need a resolved tree for 9,347 species. [src: cazyme_pangenome_ecology]
- The design is cross-sectional: profiles are compared across biomes, not tracked in lineages colonizing new environments. [src: cazyme_pangenome_ecology] Causal direction cannot be established from these data. [src: cazyme_pangenome_ecology]
- Proposed next analyses:
  - Repeat at CAZy family level as arkinlab_dbcan grows. [src: cazyme_pangenome_ecology]
  - Apply PGLS or phylogenetic mixed models with a GTDB species tree. [src: cazyme_pangenome_ecology]
  - Track CAZyme gain and loss across close species in different biomes. [src: cazyme_pangenome_ecology]
  - Cross-reference CAZyme profiles with kescience_fitnessbrowser fitness data. [src: cazyme_pangenome_ecology]
  - Test whether GT/GH predicts biome in a held-out set [src: cazyme_pangenome_ecology] and whether it correlates with EPS production or polysaccharide degradation phenotypes. [src: cazyme_pangenome_ecology]

## Slots Into

- [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation]]: all non-zero CAZy classes differ across 18 biomes, with GH 3–4× higher in fiber-rich biomes. [src: cazyme_pangenome_ecology]
- [[concepts/pangenome-openness-and-its-correlates]]: CAZyme density shows a modest association with cloud fraction, ρ = 0.101 after controls. [src: cazyme_pangenome_ecology]
- [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]]: genome count correlates with cloud fraction at ρ = 0.913. [src: cazyme_pangenome_ecology]
- [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys]]: isolate and MAG CAZyme counts did not differ within biomes. [src: cazyme_pangenome_ecology]
