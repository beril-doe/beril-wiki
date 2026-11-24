---
type: "Summary"
description: "Summary of the project Ecotype Functional Differentiation."
doc_type: "short"
full_text: "sources/ecotype_functional_differentiation__REPORT.md"
---
# Ecotype Functional Differentiation

This report asked whether gene-content ecotypes within bacterial species differ in function, or only at random. Ecotypes were found in 12 of 15 sampled species. In every one of those 12, at least one COG (clusters of orthologous groups) category differed significantly between ecotypes. Adaptive categories differ more in magnitude than housekeeping ones, so the report treats its hypothesis as partly supported. The evidence comes from one sample of 15 species, and the ecotype boundaries are weak. [src: ecotype_functional_differentiation]

## Key Findings

### Ecotypes are common but loosely bounded

PCA (principal component analysis) plus KMeans clustering of auxiliary gene presence/absence matrices found valid ecotypes in 12 of 15 sampled species (80%). [src: ecotype_functional_differentiation] Species averaged 3.7 ecotypes (range 2–6), with mean silhouette 0.215 and median 0.174. [src: ecotype_functional_differentiation] The report assigned 1,820 genomes to ecotypes. It describes these as spanning 6 phyla, but names only four: Bacillota, Pseudomonadota, Actinomycetota and Bacteroidota. [src: ecotype_functional_differentiation] The report reads this as showing that within-species gene-content subpopulations are a general feature of bacterial pangenomes. It calls this consistent with its earlier ecotype_analysis of 172 species. [src: ecotype_functional_differentiation]

The silhouette scores are moderate, which the report reads as overlapping ecotype boundaries and not discrete populations. [src: ecotype_functional_differentiation] It states that the ecotypes are statistical tendencies in gene content, not sharply defined lineages, and that auxiliary gene acquisition and loss continue. [src: ecotype_functional_differentiation]

Per-species clustering results (genomes, ecotypes, silhouette, assigned genomes):

| Species | Genomes | Ecotypes | Silhouette | Assigned |
|---|---|---|---|---|
| Staphylococcus simulans | 78 | 3 | 0.118 | 63 [src: ecotype_functional_differentiation] |
| Enterococcus D gallinarum | 95 | 3 | 0.245 | 86 [src: ecotype_functional_differentiation] |
| Pectobacterium carotovorum | 57 | 2 | 0.196 | 57 [src: ecotype_functional_differentiation] |
| Streptococcus pseudopneumoniae | 127 | 4 | 0.131 | 118 [src: ecotype_functional_differentiation] |
| Bacillus safensis | 120 | 3 | 0.141 | 117 [src: ecotype_functional_differentiation] |
| Limosilactobacillus fermentum | 118 | 4 | 0.143 | 107 [src: ecotype_functional_differentiation] |
| Enterobacter cloacae M | 136 | 4 | 0.178 | 123 [src: ecotype_functional_differentiation] |
| Enterobacter kobei | 252 | 2 | 0.159 | 252 [src: ecotype_functional_differentiation] |
| Enterobacter cloacae | 216 | 5 | 0.170 | 210 [src: ecotype_functional_differentiation] |
| Erwinia amylovora | 231 | 2 | 0.468 | 231 [src: ecotype_functional_differentiation] |
| Bacteroides xylanisolvens | 207 | 6 | 0.366 | 207 [src: ecotype_functional_differentiation] |
| Mycobacterium avium | 249 | 6 | 0.263 | 249 [src: ecotype_functional_differentiation] |

### Ecotypes differ non-randomly in function

Chi-square and Fisher's exact tests found 170 of 257 species × COG tests (66.1%) significant after BH-FDR (Benjamini-Hochberg false discovery rate) correction (q < 0.05). [src: ecotype_functional_differentiation] All 12 species had at least one significantly differentiated COG category. The report takes this as strongly rejecting the null that ecotype gene-content variation is functionally random. [src: ecotype_functional_differentiation]

The report's framing is that accessory-genome functions do differ between gene-content ecotype subgroups, with adaptive-category effect sizes 2.1x larger than housekeeping-category effect sizes (p = 2.53 x 10^-6). [src: ecotype_functional_differentiation] It contrasts this with the cog_analysis project, which compared core versus accessory genomes in aggregate, whereas this report looks within the accessory genome between ecotype subgroups. [src: ecotype_functional_differentiation] It claims this is the first systematic multi-species analysis of COG functional differentiation between gene-content ecotypes using the KBase Data Lakehouse pangenome database. [src: ecotype_functional_differentiation]

The most often differentiated categories were E (amino acid metabolism), S (unknown function) and V (defense), each significant in 11/12 species (91.7%). [src: ecotype_functional_differentiation] G (carbohydrate metabolism) followed at 10/12 (83.3%). [src: ecotype_functional_differentiation] The least differentiated were A (RNA processing, 1/9 tests), B (chromatin, 1/8) and Z (cytoskeleton, 2/6). [src: ecotype_functional_differentiation]

Per-category results (significant species, mean effect):

| COG | Class | Significant | Mean effect |
|---|---|---|---|
| E amino acid metabolism | Adaptive | 11/12 | 0.0120 [src: ecotype_functional_differentiation] |
| S unknown function | Other | 11/12 | 0.0392 [src: ecotype_functional_differentiation] |
| V defense | Adaptive | 11/12 | 0.0078 [src: ecotype_functional_differentiation] |
| G carbohydrate metabolism | Adaptive | 10/12 | 0.0176 [src: ecotype_functional_differentiation] |
| M cell wall | Adaptive | 9/12 | 0.0155 [src: ecotype_functional_differentiation] |
| L replication/repair | Other | 9/12 | 0.0337 [src: ecotype_functional_differentiation] |
| C energy production | Housekeeping | 9/12 | 0.0095 [src: ecotype_functional_differentiation] |
| P inorganic ion transport | Adaptive | 9/12 | 0.0170 [src: ecotype_functional_differentiation] |
| Q secondary metabolites | Adaptive | 9/12 | 0.0112 [src: ecotype_functional_differentiation] |
| K transcription | Adaptive | 8/12 | 0.0141 [src: ecotype_functional_differentiation] |
| J translation | Housekeeping | 8/12 | 0.0051 [src: ecotype_functional_differentiation] |
| F nucleotide metabolism | Housekeeping | 8/12 | 0.0041 [src: ecotype_functional_differentiation] |
| H coenzyme metabolism | Housekeeping | 8/12 | 0.0069 [src: ecotype_functional_differentiation] |

### Adaptive versus housekeeping categories (H1)

The report's hypothesis H1 predicted that adaptive categories (V, P, G, E, Q, M, K) would differentiate more than housekeeping categories (J, F, H, C). It describes the results as partial support. [src: ecotype_functional_differentiation] The significance rate was 79.8% (67/84) for adaptive categories and 68.8% (33/48) for housekeeping, a ratio of 1.16x. [src: ecotype_functional_differentiation] The report calls this difference modest, because housekeeping categories also differentiate in most species. [src: ecotype_functional_differentiation] It describes the "partial support", where housekeeping categories also differentiate but with smaller effect sizes, as consistent with Domingo-Sananes & McInerney (2021), who argued that pangenome gene content reflects the interplay of drift, selection and ecological interactions. [src: ecotype_functional_differentiation]

Effect size separates the two groups more clearly. Mean effect was 0.0136 for adaptive and 0.0064 for housekeeping categories, a ratio of 2.13x. [src: ecotype_functional_differentiation] The report gives the magnitude difference as 2.1x, with a one-sided Mann-Whitney U p = 2.53 x 10^-6. [src: ecotype_functional_differentiation] It concludes that ecotypes differ in both kinds of function, but adaptive categories show substantially larger proportional shifts. [src: ecotype_functional_differentiation] It interprets the 2.1x ratio as selection acting on top of a drift baseline, arguing that pure drift would produce uniform differentiation across categories. [src: ecotype_functional_differentiation]

The report says this core-housekeeping versus accessory-adaptive/defense gradient matches single-species studies of Pasteurella multocida, Lactococcus garvieae, Mycobacterium bovis and Lysinibacillus boronitolerans. [src: ecotype_functional_differentiation] It claims its own contribution is showing the pattern within ecotypes across 12 phylogenetically diverse species simultaneously. [src: ecotype_functional_differentiation]

### Unknown function and mobile elements

COG S had the largest mean effect, 0.039, and was significant in 11/12 species. COG L had the second largest, 0.034, and was significant in 9/12. [src: ecotype_functional_differentiation] Category L covers replication/repair and includes transposases, integrases and mobile genetic element machinery. [src: ecotype_functional_differentiation] The report links this prominence to the "two-speed genome" pattern from its cog_analysis project, where novel genes were enriched in L (+10.88%) and V (+2.83%) relative to core genes. [src: ecotype_functional_differentiation] The report suggests the large S effect means much ecotype differentiation involves genes of unknown function, which points to annotation gaps for niche-specific genes. [src: ecotype_functional_differentiation]

The report relates the large L effect to source-specific enrichment of category L in Cronobacter sakazakii pangenomes reported by Gao et al. (2025). [src: ecotype_functional_differentiation] It attributes variation in mobile-element content between ecotypes to these elements being vehicles of horizontal gene transfer that create gene-content differences. [src: ecotype_functional_differentiation]

The report cites Moulana et al. (2020), who found COG categories P and S varied most between Sulfurovum ecotypes at hydrothermal vents. [src: ecotype_functional_differentiation] In this analysis P was among the most differentiated categories in 9/12 species. [src: ecotype_functional_differentiation] S was among them in 11/12 species and had the largest effect. [src: ecotype_functional_differentiation]

### Interpretation proposed by the report

These are the report's interpretations, not direct measurements. It reads the strongest differentiation in E, G, V, M and P as consistent with niche-specific selection. [src: ecotype_functional_differentiation] It relates the V result to defense islands co-localized with mobile genetic elements, as described by Millman et al. (2022). [src: ecotype_functional_differentiation] It hypothesizes that different ecotypes face different phage selection pressures, which would drive different defense gene repertoires. [src: ecotype_functional_differentiation]

## Data and Methods

Of 27,702 species in the KBase Data Lakehouse pangenome database, 457 had at least 50 genomes. After filtering on COG annotation coverage, 456 were eligible. [src: ecotype_functional_differentiation] The kbase_ke_pangenome collection supplied pangenome, genome, gene, gene_cluster, gene_genecluster_junction and eggnog_mapper_annotations tables across 27,702 bacterial species. [src: ecotype_functional_differentiation] The report drew a stratified random sample of 15 species, 5 per genome-count bin (50–100, 100–200, 200–300). [src: ecotype_functional_differentiation] Clustering used PCA with up to 50 components, then KMeans with k=2–6 chosen by best silhouette. [src: ecotype_functional_differentiation] A valid result needed at least 2 ecotypes with at least 10 genomes each, and at least 20 assigned genomes in total. [src: ecotype_functional_differentiation] Enrichment used 257 chi-square/Fisher's exact tests across 12 species × 23 COG categories, with BH-FDR correction at alpha = 0.05. [src: ecotype_functional_differentiation]

Generated outputs were 456 eligible species rows, 1,820 genome-to-ecotype assignments for 12 species, 12 per-species clustering statistics rows, 894 COG profile rows, and 257 test result rows with FDR-corrected q-values. [src: ecotype_functional_differentiation]

## Caveats and Open Work

Two sampled species experienced transient Spark S3 read errors. Separately, one species, Limisoma sp., had too little structure for valid clustering. [src: ecotype_functional_differentiation] Spark query times varied from 94s to 1642s per species during heavy cluster usage, and 2 species were lost to S3 read errors. [src: ecotype_functional_differentiation] The moderate silhouette scores mean the ecotypes overlap and are not discrete. [src: ecotype_functional_differentiation] The significance-rate advantage of adaptive over housekeeping categories is modest, so H1 is only partly supported. [src: ecotype_functional_differentiation]

- Sample: 12 species were retained from 15 sampled (80%), out of 456 eligible. The pangenome-size-stratified sample may not capture phylogenetic or ecological breadth. [src: ecotype_functional_differentiation]
- Clustering: KMeans was used because HDBSCAN was unavailable on the cluster. [src: ecotype_functional_differentiation] KMeans assumes spherical clusters and needs a prespecified k (searched 2-6), whereas HDBSCAN would better handle variable-density subpopulations. [src: ecotype_functional_differentiation]
- Annotation: only ~38% of gene clusters have COG annotations. [src: ecotype_functional_differentiation] The 62% without annotations may contain ecotype-specific adaptive genes in poorly characterized categories, potentially biasing results toward well-annotated housekeeping functions. [src: ecotype_functional_differentiation]
- Phylogeny: gene-content ecotypes may reflect within-species phylogenetic substructure, not ecological specialization. Without within-species phylogenetic controls, the report cannot distinguish adaptive ecotypes from demographic subpopulations. [src: ecotype_functional_differentiation]
- Effect size: the largest mean effects (S: 0.039, L: 0.034) are ~3-4 percentage point differences in COG category proportions. They are statistically significant because of large sample sizes, but biologically modest. [src: ecotype_functional_differentiation]

Next analyses proposed by the report:

- Scale to all 456 eligible species, using off-peak execution or optimized queries, since Spark load constrained the sample of 15. [src: ecotype_functional_differentiation]
- Overlay core-genome phylogenetic trees on ecotype assignments to separate ecological adaptation from demographic substructure. [src: ecotype_functional_differentiation]
- Characterize S (unknown function) genes with AlphaFold structure prediction or domain analysis, to test for cryptic defense, transport or regulatory functions. [src: ecotype_functional_differentiation]
- For species with soil, host-associated or aquatic habitat metadata, test whether ecotype-defining COG categories correlate with environmental source. [src: ecotype_functional_differentiation]
- Re-run clustering with HDBSCAN, if available, to assess how sensitive ecotype definitions are to clustering method. [src: ecotype_functional_differentiation]

## Slots Into

- [[concepts/functional-differentiation-of-gene-content-ecotypes-across-cog-categories]]: 170 of 257 tests were significant, and adaptive categories showed 2.13x larger mean effects than housekeeping ones. [src: ecotype_functional_differentiation]
- [[concepts/defense-and-mobile-element-gene-content-as-drivers-of-ecotype-differences]]: V was significant in 11/12 species, and L was prominent, with mean effect 0.034. [src: ecotype_functional_differentiation]
- [[concepts/unknown-function-genes-in-niche-differentiated-accessory-genomes]]: S had the largest mean effect, 0.039, with significance in 11/12 species. [src: ecotype_functional_differentiation]
