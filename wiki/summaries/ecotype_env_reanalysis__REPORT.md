---
type: "Summary"
description: "Summary of the project Ecotype Reanalysis — Environmental vs Human-Associated Species."
doc_type: "short"
full_text: "sources/ecotype_env_reanalysis__REPORT.md"
---
# Ecotype Reanalysis — Environmental vs Human-Associated Species

This report asked whether environmental bacterial species show stronger environment–gene content correlations than human-associated species, using genome-level environment classification. The answer was no: the comparison was null, and the direction was slightly opposite to the hypothesis. [src: ecotype_env_reanalysis] The evidence is a single reanalysis with a group comparison and a continuous check, and both agree. [src: ecotype_env_reanalysis] The work relates to [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Key Findings

### Main comparison

Environmental species (n=37, median partial correlation 0.051) did not show stronger correlations than human-associated species (n=93, median 0.084); the one-sided Mann-Whitney U test gave U=1536, p=0.83. [src: ecotype_env_reanalysis] Human-associated species showed slightly higher partial correlations, opposite to the hypothesis. [src: ecotype_env_reanalysis] The hypothesis rested on the earlier finding that environmental species' AlphaEarth embeddings carry more geographic signal (3.4x ratio vs 2.0x for human-associated). [src: ecotype_env_reanalysis] The partial correlation here is described in [[entities/partial-correlation-of-environment-and-gene-content-distance]].

| Group | n | Median | Mean | SD | Range |
|---|---|---|---|---|---|
| Environmental | 37 | 0.051 | 0.073 | 0.299 | [-0.50, 0.78] [src: ecotype_env_reanalysis] |
| Human-associated | 93 | 0.084 | 0.110 | 0.226 | [-0.30, 0.73] [src: ecotype_env_reanalysis] |
| Mixed/Other | 53 | 0.109 | 0.148 | 0.261 | [-0.38, 0.69] [src: ecotype_env_reanalysis] |

The report suggests the Mixed/Other group's highest median may reflect diverse sampling campaigns. [src: ecotype_env_reanalysis]

### Continuous checks

The fraction of environmental genomes per species did not predict partial correlation (Spearman rho=-0.085, p=0.25). [src: ecotype_env_reanalysis] The fraction of human-associated genomes did not either (rho=0.030, p=0.69). [src: ecotype_env_reanalysis] Both the binary and continuous analyses found no relationship between environment type and correlation strength. [src: ecotype_env_reanalysis]

### Relation to earlier projects

The original ecotype_analysis (Dehal et al., 2026) found phylogeny dominates, with p=0.66 for a coarse manual environment-versus-host comparison. The genome-level harmonized reanalysis confirmed the null at p=0.83. [src: ecotype_env_reanalysis] The report calls this the first test of whether genome-level classification changes that conclusion. [src: ecotype_env_reanalysis] Species were classified by majority vote of genome environments, using the harmonized env_category mapping from env_embedding_explorer. [src: ecotype_env_reanalysis]

Of 224 species selected (>=20 genomes with AlphaEarth embeddings, >=30% coverage), 106 (47%) were majority human-associated. [src: ecotype_env_reanalysis] A further 47 (21%) were majority environmental (Soil, Marine, Freshwater, Extreme, Plant) [src: ecotype_env_reanalysis], and 71 (32%) were mixed/other. [src: ecotype_env_reanalysis] The report confirms the strong clinical sampling bias in the AlphaEarth subset but finds it does not account for the weak environment signal. [src: ecotype_env_reanalysis] It concludes the bias, though real for embedding-based analyses, does not confound the ecotype environment–gene content relationship. [src: ecotype_env_reanalysis] See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]].

### Proposed explanations (not tested)

- Embedding similarity may not equal ecological relevance: climate, vegetation and land use may not strongly predict gene content. [src: ecotype_env_reanalysis]
- Clinical taxa such as Klebsiella and Enterococcus have global epidemiological patterns, with different lineages dominating different regions. [src: ecotype_env_reanalysis] Embeddings may capture these, giving real but epidemiological associations. [src: ecotype_env_reanalysis]
- Species with more genomes, often clinical, have more power to detect weak correlations. [src: ecotype_env_reanalysis]

## Data and Methods

The analysis used the kbase_ke_pangenome tables genome, alphaearth_embeddings_all_years, genome_ani, gene and gene_genecluster_junction. [src: ecotype_env_reanalysis] Inputs were partial correlations for 213 species and 25,205 target genomes from ecotype_analysis, and harmonized env_category per genome from env_embedding_explorer. [src: ecotype_env_reanalysis] Outputs were a 224-row species classification and a 213-row table of correlations with group labels. [src: ecotype_env_reanalysis] One notebook does the loading, classification, comparison, tests and plots. [src: ecotype_env_reanalysis] The reanalysis used all genomes with embeddings (up to 3,505/species), not the original's diversity-maximizing downsampling (max 250). [src: ecotype_env_reanalysis] The report presents the project as a template for follow-up work. [src: ecotype_env_reanalysis]

## Caveats and Open Work

- **No downsampling:** The median partial correlation across all 183 species was 0.081, against 0.003 in the original. [src: ecotype_env_reanalysis] This 27x difference makes absolute values not comparable with the original, but the group comparison stays valid because both groups use the same method. [src: ecotype_env_reanalysis] Larger samples detect weaker correlations, and omitting downsampling changes distance distributions. [src: ecotype_env_reanalysis]
- **NaN exclusion:** Of 30 species with NaN (not a number) partial correlations, rates were 10/47 = 21% for environmental, 13/66 = 20% for Mixed/Other and 7/100 = 7% for human-associated. [src: ecotype_env_reanalysis] The report says this would bias toward a stronger environmental signal, opposite to what was observed, so correcting it would only strengthen the null. [src: ecotype_env_reanalysis]
- **Klebsiella pneumoniae:** This major clinical species was excluded because gene cluster extraction exceeded Spark's maxResultSize. [src: ecotype_env_reanalysis] See [[entities/klebsiella-pneumoniae]].
- **Majority vote:** A species with 51% gut genomes counts as human-associated. The continuous Spearman analysis addresses this and confirms the null. [src: ecotype_env_reanalysis]
- **Proposed next steps:** Compare downsampled and full-genome extraction to explain the 27x gap. [src: ecotype_env_reanalysis] Test specific gene subsets, since environment may act on functional categories such as transport and secondary metabolism rather than whole-genome Jaccard distance. [src: ecotype_env_reanalysis] Repeat with ENVO (Environment Ontology) terms from env_broad_scale. [src: ecotype_env_reanalysis] Add genome count as a covariate, since species with more genomes may have inflated correlations. [src: ecotype_env_reanalysis]

## Slots Into

- [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]: Environmental species showed no stronger environment–gene content correlation than human-associated ones (p=0.83), consistent with the earlier phylogeny-dominance result (p=0.66). [src: ecotype_env_reanalysis]
- [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]]: The clinical bias in the AlphaEarth subset is confirmed but does not explain the weak signal. [src: ecotype_env_reanalysis]
- [[concepts/genome-sampling-depth-and-downsampling-effects-on-partial-correlation-estimates]]: Omitting downsampling gave 27x higher overall partial correlations. [src: ecotype_env_reanalysis]
