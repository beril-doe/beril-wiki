---
type: "Concept"
description: "Which COG functional categories differ between within-species accessory gene-content ecotypes, and whether adaptive categories differ more than housekeeping ones; stops at the clustering method caveats."
sources: ["summaries/ecotype_functional_differentiation__REPORT.md"]
---
# Functional differentiation of gene-content ecotypes across COG categories

Within accessory-genome gene-content ecotypes of bacterial species, many COG (clusters of orthologous groups) functional categories differ between ecotypes, and adaptive categories shift more in magnitude than housekeeping ones. The evidence comes from one report that analysed 12 species. It supports the adaptive-versus-housekeeping hypothesis only partially, and the absolute effects are small. [src: ecotype_functional_differentiation] See also [[summaries/ecotype_functional_differentiation__REPORT]] and [[entities/clusters-of-orthologous-groups-functional-categories]].

## Literature Context

The candidate papers show that functional differences between related bacterial populations are often concentrated in categories tied to environmental interaction. In marine Actinobacteria, 75% of the species-specific genes of Salinispora tropica and Salinispora arenicola sit in 21 genomic islands. Secondary metabolism is the major functional category separating the two species, at 8.8% and 10.9% of genes [PMID 19474814](https://pubmed.ncbi.nlm.nih.gov/19474814/). In Rhizobium leguminosarum, a pangenome analysis found transport, metabolism and regulatory categories over-represented on extrachromosomal replicons. Transcriptomic stress responses involved those replicons substantially, and the differentially expressed genes were enriched in amino acid and carbohydrate metabolism [PMID 39519284](https://pubmed.ncbi.nlm.nih.gov/39519284/). In 595 Salmonella Typhimurium genomes, accessory genome size differed across host sources, and so did the functional categories targeted by positive selection in the core genome [PMID 42971789](https://pubmed.ncbi.nlm.nih.gov/42971789/).

Across community-level studies, functional categories also differ in how much they vary. Among bacterial communities and 28,000 randomly sampled GTDB genomes, categories mediating environmental and microbe-to-microbe interactions showed the highest dissimilarity. Genetic information processing showed the lowest [PMID 42260652](https://pubmed.ncbi.nlm.nih.gov/42260652/). In soils, gene abundances shifted coherently with pH, for example cation efflux pumps in acidic soils and transporters in high-pH soils [PMID 28679747](https://pubmed.ncbi.nlm.nih.gov/28679747/). The Loktak Phumdi metagenome study reported 12 functional categories exclusive to that habitat compared with other freshwater habitats [PMID 27842027](https://pubmed.ncbi.nlm.nih.gov/27842027/). These are metagenomic or interspecies contrasts, not within-species gene-content ecotypes.

The corpus's main pattern is that adaptive COG categories shift about 2.1x more in magnitude than housekeeping ones, and that housekeeping categories also differ in most species. This is consistent with the literature. The prominence of E, G, P, M and V matches the environmental-interaction categories that vary most in [PMID 42260652](https://pubmed.ncbi.nlm.nih.gov/42260652/). It also matches the metabolism and transport enrichment in [PMID 39519284](https://pubmed.ncbi.nlm.nih.gov/39519284/) and the pH-linked transport and efflux signals in [PMID 28679747](https://pubmed.ncbi.nlm.nih.gov/28679747/). The low differentiation of information-processing categories such as J agrees directionally with the low dissimilarity of genetic information processing in [PMID 42260652](https://pubmed.ncbi.nlm.nih.gov/42260652/).

The corpus extends this work by testing the contrast within ecotypes across 12 species. Most candidate studies compare species, habitats or host sources, or examine a single lineage. The corpus's reading of its 2.1x ratio as selection on top of a drift baseline is an interpretation, not a test. [PMID 42260652](https://pubmed.ncbi.nlm.nih.gov/42260652/) used a GTDB null model to infer functional selection, and the corpus has no comparable null.

One candidate adds caution. In 44 Acetobacteraceae isolates, free-living and Drosophila-associated bacteria were not enriched for different gene sets or predicted-function categories. Habitat cycling was proposed to prevent differentiation in wild populations [PMID 28667798](https://pubmed.ncbi.nlm.nih.gov/28667798/). This is a null result for one family. It suggests that category-level differences need not track habitat, which fits the hub's small effect sizes and low mean silhouette score of 0.215. It also supports the open direction of linking clusters to isolation source.

## Ecotypes analysed

PCA (principal component analysis) plus KMeans clustering of auxiliary gene presence/absence matrices found valid gene-content ecotypes in 12 of 15 sampled species (80%). [src: ecotype_functional_differentiation] Species averaged 3.7 ecotypes each (range 2–6), with mean silhouette score 0.215 and median 0.174. [src: ecotype_functional_differentiation] In total, 1,820 genomes were assigned to ecotypes across 12 species, described as spanning 6 phyla (Bacillota, Pseudomonadota, Actinomycetota, Bacteroidota). [src: ecotype_functional_differentiation]

## Which categories differ

Differentiation is common but not universal. Chi-square and Fisher's exact tests (see [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]) found 170 of 257 species x COG tests (66.1%) significant after BH-FDR (Benjamini-Hochberg false discovery rate) correction (q < 0.05). [src: ecotype_functional_differentiation] All 12 species had at least one significantly differentiated category, which the report reads as strongly rejecting functionally random ecotype gene content. [src: ecotype_functional_differentiation]

Most frequently differentiated categories (significant species out of 12, then mean effect):

- E amino acid metabolism, Adaptive: 11/12, 0.0120 [src: ecotype_functional_differentiation]
- S unknown function, Other: 11/12, 0.0392 [src: ecotype_functional_differentiation]
- V defense, Adaptive: 11/12, 0.0078 [src: ecotype_functional_differentiation]
- G carbohydrate metabolism, Adaptive: 10/12, 0.0176 [src: ecotype_functional_differentiation]
- M cell wall, Adaptive: 9/12, 0.0155 [src: ecotype_functional_differentiation]
- P inorganic ion transport, Adaptive: 9/12, 0.0170 [src: ecotype_functional_differentiation]
- Q secondary metabolites, Adaptive: 9/12, 0.0112 [src: ecotype_functional_differentiation]
- L replication/repair, Other: 9/12, 0.0337 [src: ecotype_functional_differentiation]
- C energy production, Housekeeping: 9/12, 0.0095 [src: ecotype_functional_differentiation]
- K transcription, Adaptive: 8/12, 0.0141 [src: ecotype_functional_differentiation]
- J translation, Housekeeping: 8/12, 0.0051 [src: ecotype_functional_differentiation]
- F nucleotide metabolism, Housekeeping: 8/12, 0.0041 [src: ecotype_functional_differentiation]
- H coenzyme metabolism, Housekeeping: 8/12, 0.0069 [src: ecotype_functional_differentiation]

The least differentiated categories were A (RNA, ribonucleic acid, processing; 1/9 tests), B (chromatin; 1/8) and Z (cytoskeleton; 2/6). [src: ecotype_functional_differentiation] S and L had the largest mean effects, 0.039 and 0.034. [src: ecotype_functional_differentiation] The report ties the strongest signals to environmental interaction: E, G, V, M and P. [src: ecotype_functional_differentiation] It also notes that P and S were among the most differentiated categories, extending an earlier single-species finding. [src: ecotype_functional_differentiation] For the unknown-function category see [[concepts/unknown-function-genes-in-niche-differentiated-accessory-genomes]]. For defense, the report links V's dominance (11/12 species) to defense islands co-localized with mobile genetic elements (Millman et al. 2022) [src: ecotype_functional_differentiation]; see [[concepts/defense-and-mobile-element-gene-content-as-drivers-of-ecotype-differences]].

## Adaptive versus housekeeping

Hypothesis H1 predicted that adaptive categories (V, P, G, E, Q, M, K) would differentiate more than housekeeping ones (J, F, H, C). The report calls the result partial support. [src: ecotype_functional_differentiation] By significance rate the gap is small: 79.8% (67/84) for adaptive versus 68.8% (33/48) for housekeeping, a ratio of 1.16x, because housekeeping categories also differentiate in most species. [src: ecotype_functional_differentiation] By magnitude the gap is clearer: mean effect size was 0.0136 versus 0.0064 (2.13x). [src: ecotype_functional_differentiation] The report gives the difference as 2.1x, with one-sided Mann-Whitney U p = 2.53 x 10^-6. [src: ecotype_functional_differentiation]

The report concludes that ecotypes differ in both kinds of function, but adaptive categories show larger proportional shifts. [src: ecotype_functional_differentiation] It reads the 2.1x ratio as selection acting on top of a drift baseline, since it argues that pure drift would give uniform differentiation. [src: ecotype_functional_differentiation] This is an interpretation, not a test of drift. The report also says the pattern matches single-species studies and that its contribution is showing it within ecotypes across 12 diverse species. [src: ecotype_functional_differentiation] It describes the work as the first systematic multi-species analysis of this kind on the KBase Data Lakehouse pangenome database [src: ecotype_functional_differentiation], and as showing that gene-content subpopulations are a general pangenome feature. [src: ecotype_functional_differentiation]

## Caveats

Effect sizes are small. The largest (S 0.039, L 0.034) are about 3–4 percentage-point differences in COG proportions, and they are significant largely because of large sample sizes. [src: ecotype_functional_differentiation] The clustering produced mean silhouette 0.215 and median 0.174. [src: ecotype_functional_differentiation]

## Open Directions

- Test whether specific categories such as V (defense) and L (mobile) show stronger environment effects, using environment metadata per genome. This would show whether category-level differences track environment.
- Compare gene content between ecotype clusters within species that have identified ecotypes, linking clusters to isolation source. This would show whether ecotypes are ecological.
- Repeat the adaptive-versus-housekeeping contrast with alternative clustering methods and a silhouette threshold. This would show whether the 2.1x ratio survives different cluster separation.
- Compare effects with and without categories S and L, which have the largest effects but are not classed adaptive. This would show whether the contrast depends on category assignment.
- Compare these results with [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]. This would separate phylogenetic from ecological structure.
