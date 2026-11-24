---
type: "Organism"
description: "A bacterial phylum dominating the BacDive metal tolerance analysis, with larger genomes and contamination-associated higher metal scores."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/bacdive_metal_validation__REPORT.md", "summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md", "summaries/phb_granule_ecology__REPORT.md"]
aliases: ["Proteobacteria"]
---
# Pseudomonadota

Pseudomonadota (also known as Proteobacteria) is a bacterial phylum. This page collects what the reports show about it. It is the dominant phylum in the BacDive metal tolerance analysis. [src: bacdive_metal_validation] The evidence comes from several separate projects, each using its own dataset and test.

## Key facts

- Pseudomonadota is the dominant phylum in the BacDive metal tolerance analysis. [src: bacdive_metal_validation]
- Within it, 85 contamination isolates versus 5,655 environmental isolates show a metal tolerance score delta of +0.040 (p<0.001), a significant difference. [src: bacdive_metal_validation] The report says contamination isolates still score significantly higher than environmental isolates within this phylum. [src: bacdive_metal_validation] See [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance]] and [[summaries/bacdive_metal_validation__REPORT]].

## Genome size and confounding

The report's metal_score_norm controls for genome size, which matters because Pseudomonadota tend to have larger genomes. [src: bacdive_metal_validation] The report likely attributes the unexpectedly higher host-associated scores in BacDive to genome-size confounding. It points to dominant large-genome Pseudomonadota pathogens (*Pseudomonas*, *Klebsiella*, *Acinetobacter*) with more KEGG-annotated gene clusters. [src: bacdive_metal_validation]

In the separate phenotype project, the Gram-stain association with metal tolerance cannot be tested within taxonomic classes. It is almost entirely a between-lineage signal of Gram-positive Actinomycetes versus Gram-negative Proteobacteria. [src: bacdive_phenotype_metal_tolerance] The matched data contain no Gram-positive Proteobacteria and no Gram-negative Actinomycetes. [src: bacdive_phenotype_metal_tolerance] The report calls the Gram-negative advantage real but indistinguishable from "being a Proteobacterium" in a predictive model. [src: bacdive_phenotype_metal_tolerance] See [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]] and [[entities/actinomycetota]].

## Other measurements

- **Antimicrobial resistance (AMR):** In the AMR pangenome atlas, Pseudomonadota has 4,992 species with AMR, 42,904 total AMR, a mean AMR/sp of 8.6, and 67.0% of species with AMR. [src: amr_pangenome_atlas]
- **Carbohydrate-active enzymes (CAZymes):** The biome effect on CAZymes survived genome-size correction (Kruskal-Wallis, KW, on per-Mbp residuals). It was significant within all 5 top phyla, including Pseudomonadota. [src: cazyme_pangenome_ecology] Within Pseudomonadota, the CAZy–pangenome openness correlation across 1,689 species was Spearman ρ = −0.013, BH-adjusted p = 0.74, and was not significant. [src: cazyme_pangenome_ecology] See [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation]] and [[concepts/pangenome-openness-and-its-correlates]].
- **Gene copy number:** Pseudomonadota has the strongest mean adaptive-to-housekeeping multi-copy rate ratio, 15.4× (n=5). Campylobacterota has the weakest, 4.0× (n=4). [src: gene_copy_number_variation] For Pseudomonadota, the mean housekeeping multi-copy rate is 0.034% and the mean adaptive rate is 0.528%. Adaptive exceeds housekeeping in 5/5 species. [src: gene_copy_number_variation] The report links this to the largest and most mobile accessory genomes in its set. [src: gene_copy_number_variation] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].
- **Polyhydroxybutyrate (PHB):** In the GTDB species analysis, PHB prevalence in Pseudomonadota is 60.9% (4,544/7,456 species). [src: phb_granule_ecology] See [[concepts/phylogenetic-distribution-of-phb-synthesis-across-bacteria-and-archaea]].
