---
type: "Concept"
description: "Whether gene-content ecotypes and lifestyle-pathway profiles reflect niche adaptation or phylogenetic/demographic substructure, including intra-species phylogenetic control, permutation nulls and clustering limits."
sources: ["summaries/ecotype_analysis__REPORT.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Phylogenetic structure versus ecological adaptation in gene-content patterns

Across these reports, phylogeny usually explains more gene-content similarity than environment does. [src: ecotype_analysis] Within-species GC-content associations with isolation source survive several phylogenetic and permutation controls. [src: gc_ecotype_ecology] Each control has stated limits. [src: gc_ecotype_ecology] In Pseudomonas, the main pathway-profile signal is the deep split between subgenera, and the lifestyle signal within a subgenus is subtle and not phylogenetically controlled. [src: pseudomonas_carbon_ecology] See also [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]] and [[concepts/genome-gc-content-as-an-ecological-signal]].

## Literature Context

The candidate papers mostly address whether gene-content differences track habitat once lineage is accounted for. Several describe independent shifts into the same habitat, which gives a form of phylogenetic replication. In bee-associated lactic acid bacteria, phylogenomic analysis of 369 species found seven independent ecological shifts toward the bee environment. These species showed reduced genome size, gene repertoire and GC content, and a machine-learning classifier separated bee-associated from non-bee-associated species with 94% accuracy. The most important genes appeared to have been lost independently in multiple lineages [PMID 39440949](https://pubmed.ncbi.nlm.nih.gov/39440949/). In Methylophilaceae, a freshwater-to-marine transition was inferred in which the BS01 clade colonized the pelagic ocean independently of OM43 through convergent evolution [PMID 34154421](https://pubmed.ncbi.nlm.nih.gov/34154421/). Nectar-dwelling Acinetobacter arose from one evolutionary origin of floral adaptation, with genome reduction and gains such as pectin degradation. The authors only hypothesize that this was a key adaptive trait [PMID 39723821](https://pubmed.ncbi.nlm.nih.gov/39723821/). A review of phylogenetic reconciliation presents it as a framework for separating gene gain, loss and transfer along a species tree, and it calls for integrating habitat metadata [PMID 39001714](https://pubmed.ncbi.nlm.nih.gov/39001714/).

Two further papers bear on the lineage confound directly. In permafrost isolates, the genome-predicted sugar-acid preference explained over 50% of the variance in observed preference. It was inversely correlated with GC content, and the authors state that this coarse preference covaries with phylogeny [PMID 42505143](https://pubmed.ncbi.nlm.nih.gov/42505143/). That study used 48 isolates. In Australian soils, strain-level Bradyrhizobium community composition varied with temperature, pH, nitrate and metals, and most of the 181 strains had restricted distributions [PMID 41060304](https://pubmed.ncbi.nlm.nih.gov/41060304/). That is environment-associated structure within one genus, although it concerns strain distributions, not gene-content ecotypes.

The corpus finding that phylogeny predicts gene content better than environment across 172 species (60.5% of species phylogeny-dominated) is consistent with the permafrost observation that metabolic strategy covaries with phylogeny [PMID 42505143](https://pubmed.ncbi.nlm.nih.gov/42505143/). The Pseudomonas result is similar: the deep subgenus split dominates, and lifestyle signal is subtle and not phylogenetically controlled. The corpus's call for PGLS (phylogenetic generalized least squares) in that case matches the literature's use of independent origins and reconciliation to separate adaptation from ancestry [PMID 39440949](https://pubmed.ncbi.nlm.nih.gov/39440949/), [PMID 39001714](https://pubmed.ncbi.nlm.nih.gov/39001714/).

The corpus's GC–isolation-source results, in which 32 of 39 testable species (82%) stayed significant under continuous phylogenetic control, are compatible with the convergent GC reductions seen in bee-associated bacteria. They do not duplicate that work, because they use within-species ANI-cluster and PCoA controls instead of cross-species shifts. The corpus's open question about ecotypes versus demographic substructure, with a mean silhouette of 0.215, is not tested by any candidate paper, so that part stays novel and unresolved. The remaining candidates (Helicobacter prophages, Mycobacterium abscessus, Weissella, microcystin degraders) are only loosely related and give no direct evidence on this question.

## Phylogeny dominates cross-species gene-content similarity

In the ecotype correlation analysis of 172 species, the median partial correlation was 0.0025 for environment and 0.0143 for phylogeny. [src: ecotype_analysis] Phylogeny dominated in 60.5% of species and environment in 39.5%. [src: ecotype_analysis] The report concludes that for most bacterial species phylogenetic history predicts gene content better than environmental similarity does. [src: ecotype_analysis] It reads this as vertical inheritance dominating the signal. [src: ecotype_analysis] It calls the result consistent with Garud et al. (2019) and Shapiro et al. (2012), who are described as showing that clonal ancestry shapes genome-wide variation more than ecological niche. [src: ecotype_analysis] See [[entities/partial-correlation-of-environment-and-gene-content-distance]].

The environment effect was significant and positive (p<0.05) in 12 species (7.0%) and significant and negative in 4 species (2.3%). [src: ecotype_analysis] It was not significant in 156 species (90.7%). [src: ecotype_analysis] Free-living environmental bacteria did not differ from host-associated bacteria in environment effect (p=0.66). [src: ecotype_analysis] Partial correlations assume linear relationships between distance matrices, so they may miss nonlinear ecological effects. [src: ecotype_analysis]

## Downstream analyses that inherit the concern

The pathway_capability_dependency report cites the 60.5% result as a possibility that metabolic ecotypes partly reflect intra-species phylogenetic structure. [src: pathway_capability_dependency] It therefore checked all correlations within GTDB genera. [src: pathway_capability_dependency] In the metabolic_capability_dependency report, metabolic clusters correlated with isolation environment in Salmonella enterica (χ²=1570.2, df=25, p<0.0001) and Phenylobacterium sp. (χ²=12.2, df=1, p=0.0005). [src: metabolic_capability_dependency] They did not correlate in the marine organisms Stutzerimonas and Alteromonas. [src: metabolic_capability_dependency] That report notes the analysis is observational. It says phylogenetic confounding is possible without explicit correction. [src: metabolic_capability_dependency] In Pseudomonas, the dominant PCA (principal component analysis) signal separates subgenera rather than lifestyles. [src: pseudomonas_carbon_ecology]

## Pseudomonas: deep lineage split versus lifestyle

The pseudomonas_carbon_ecology report shows the same pattern at genus level. The primary PCA axis of species pathway profiles separates Pseudomonas s.s. from Pseudomonas_E, driven by sugar pathway loss. [src: pseudomonas_carbon_ecology] Within Pseudomonas_E, free-living, host-associated and plant-associated categories overlap substantially. The report reads this as lifestyle variation being subtler than the deep phylogenetic divide. [src: pseudomonas_carbon_ecology] The report states these lifestyle differences are subtle and that the analyses do not explicitly control for phylogenetic non-independence among species. [src: pseudomonas_carbon_ecology] It proposes phylogenetic generalized least squares (PGLS) or phylogenetic logistic regression with the GTDB species tree to test whether lifestyle-pathway associations persist after controlling for relatedness. [src: pseudomonas_carbon_ecology]

For Pseudomonas aeruginosa, the report finds the sugar pathway losses are conserved at the species level, not strain-specific. [src: pseudomonas_carbon_ecology] It suggests that much of the metabolic loss attributed to infection reflects ancestral streamlining of the lineage, because the pathways were already absent at species level across thousands of isolates. [src: pseudomonas_carbon_ecology] This is the report's interpretation, not a direct test of infection-time loss.

## Gene-content ecotypes and substructure

The ecotype_functional_differentiation report cannot tell adaptive ecotypes from demographic subpopulations. It did not control for within-species phylogeny, for example with core-genome trees. [src: ecotype_functional_differentiation] Its mean silhouette score of 0.215 indicates overlapping ecotype boundaries rather than discrete populations. [src: ecotype_functional_differentiation] The report describes the ecotypes as statistical tendencies in gene content, not sharply defined lineages. [src: ecotype_functional_differentiation]

Several limits apply to that clustering:
- KMeans was used because HDBSCAN was unavailable on the cluster. [src: ecotype_functional_differentiation] KMeans assumes spherical clusters and needs a prespecified k, searched over 2-6. The report says HDBSCAN would handle variable-density subpopulations better. [src: ecotype_functional_differentiation]
- The largest mean effect sizes (S: 0.039, L: 0.034) are about 3-4 percentage points in COG (clusters of orthologous groups) category proportions. They are statistically significant but biologically modest. [src: ecotype_functional_differentiation]
- Only ~38% of gene clusters have COG annotations. The unannotated 62% may hold ecotype-specific adaptive genes, which could bias results toward housekeeping functions. [src: ecotype_functional_differentiation]
- The sample was 12 species retained from 15 sampled, out of 456 eligible. It may not capture phylogenetic or ecological breadth. [src: ecotype_functional_differentiation] The sample of 15 was constrained by Spark cluster load. [src: ecotype_functional_differentiation]

The report itself proposes three follow-ups. It would overlay core-genome phylogenetic trees on ecotype assignments to distinguish ecological adaptation from demographic substructure. [src: ecotype_functional_differentiation] It would rerun clustering with HDBSCAN to assess sensitivity of ecotype definitions to clustering method. [src: ecotype_functional_differentiation] It would test whether ecotype-defining COG categories correlate with environmental source in species with soil, host-associated or aquatic habitat metadata. [src: ecotype_functional_differentiation]

See [[concepts/functional-differentiation-of-gene-content-ecotypes-across-cog-categories]].

## Intra-species controls for GC–ecology associations

The gc_ecotype_ecology report applies several explicit controls to the adaptation-versus-substructure question. It builds ANI (average nucleotide identity) clusters as connected components of the ANI ≥ 99% graph, using within-species pairs from kbase_ke_pangenome.genome_ani. That table has no species-clade column. [src: gc_ecotype_ecology] It calls this a tractable, pragmatic intra-species phylogenetic control. [src: gc_ecotype_ecology] A nested OLS (ordinary least squares) partial F-test compares the ANI-cluster-only model with the model that adds isolation category. [src: gc_ecotype_ecology] Seven species collapsed to one ANI cluster and were dropped, and 108 species gave valid p-values. [src: gc_ecotype_ecology]

### Permutation null

For each of the 40 species significant at FDR (false discovery rate) < 0.05, isolation labels were shuffled 200 times within species, holding ANI clusters fixed. [src: gc_ecotype_ecology] Of those 40, 39 (98%) had empirical p < 0.05 and 29 (73%) had p < 0.01. [src: gc_ecotype_ecology] The report reads this as ruling out chance exploitation of label/cluster co-occurrence, including when clusters are themselves ecology-defined. [src: gc_ecotype_ecology] The null excludes a class of confounders, not all of them. [src: gc_ecotype_ecology]

### Continuous phylogenetic control and geography

Notebook 06 replaces the cluster effect with the top-10 continuous PCoA (principal coordinates analysis) axes of pairwise branch distances. [src: gc_ecotype_ecology] 32 of 39 testable species (82%) stayed significant, and one species lacked phylogenetic coverage. [src: gc_ecotype_ecology] The report concludes that the original ANI cluster choice was not driving the result. [src: gc_ecotype_ecology]

Adding latitude and longitude kept significance in 12 of 16 species (75%) with ≥ 30 geo-bearing genomes. [src: gc_ecotype_ecology] The report reads this as the effect not being just a proxy for geography. [src: gc_ecotype_ecology] Geography was testable in only 16 of 40 species, because the other 24 had < 30 genomes with parseable lat_lon. A residual geographic confound cannot be ruled out in those species. [src: gc_ecotype_ecology]

### Remaining limits

Enterococcus faecium has only 2 ANI clusters among 1,633 genomes, and Streptococcus thermophilus has 5. [src: gc_ecotype_ecology] For such species the connected-components control is thin and could partly reflect cluster-level confounds. The PCoA control mitigates this only for the subset that retains significance. [src: gc_ecotype_ecology] Species with few clusters but many genomes need a stricter or alternative control before strong claims are made. [src: gc_ecotype_ecology] The largest partial R² values come from species with many small clusters, such as Aeromonas veronii (87 clusters of 122 genomes). There the control uses up most degrees of freedom. [src: gc_ecotype_ecology] BH (Benjamini-Hochberg) correction suits discovery, but per-species effect estimates are subject to selection bias if cherry-picked from the top. [src: gc_ecotype_ecology]

## Tensions

- Phylogeny dominates gene-content similarity in 60.5% of species, with a median environment partial correlation of 0.0025. [src: ecotype_analysis] Yet 82% of testable species keep significant GC–isolation-category associations under continuous phylogenetic control. [src: gc_ecotype_ecology] These tests use different responses, gene content versus GC, and different controls. The page does not reconcile them.
- Salmonella and Phenylobacterium show environment–cluster correlations that suggest ecological selection. [src: metabolic_capability_dependency] The same report says phylogenetic confounding is possible without explicit correction. [src: metabolic_capability_dependency]
- Pseudomonas lifestyle-pathway differences are reported as subtle, while the genus-level split is large. [src: pseudomonas_carbon_ecology] The lifestyle comparisons lack phylogenetic control. [src: pseudomonas_carbon_ecology]

## Open Directions

- Overlay core-genome phylogenetic trees on ecotype assignments to separate adaptation from demographic substructure.
- Rerun ecotype clustering with HDBSCAN to test how sensitive the ecotype definitions are to the clustering method.
- Scale to all 456 eligible species, off-peak or with optimized queries, to address the breadth limit of the small sample.
- Test whether ecotype-defining COG categories correlate with environmental source in species with soil, host-associated or aquatic metadata.
- Apply a stricter phylogenetic control to species with few ANI clusters, such as E. faecium, and extend geographic testing beyond the 16 species.
- Run PGLS or phylogenetic logistic regression on Pseudomonas lifestyle-pathway associations with the GTDB species tree, to test whether they persist beyond relatedness.
