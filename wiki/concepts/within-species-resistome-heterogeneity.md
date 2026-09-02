---
type: "Concept"
description: "Variation in antimicrobial-resistance repertoires among strains of one species."
sources: ["summaries/amr_strain_variation__REPORT.md"]
---
# Within-Species Resistome Heterogeneity

Within-species resistome heterogeneity is the structured variation in antimicrobial-resistance (AMR) gene repertoires among strains belonging to the same species. In the analyzed resource, this variation was organized by prevalence class, co-inherited resistance islands, phylogeny, lineage-associated AMR ecotypes, and host or environmental association. [src: amr_strain_variation]

## Scale and prevalence structure

The study analyzed 1,305 species and 180,025 genomes, producing 37,444 AMR gene-species records. [src: amr_strain_variation] Among these records, 51.3% of AMR genes were rare, occurring in <=5% of strains; 41.3% were variable, occurring in 5-95% of strains; and 7.5% were fixed, occurring in >=95% of strains. [src: amr_strain_variation] The median variability index was 0.526, and the median pairwise Jaccard distance—a distance based on shared versus differing gene repertoires—was 0.435, indicating substantial differences among strains within the same species. [src: amr_strain_variation]

Atlas conservation class refined this pattern: 77.3% of Core AMR genes were fixed, 78.7% of Singletons were rare, and Auxiliary genes were 57.3% variable and 42.7% rare. [src: amr_strain_variation] AMR variability was weakly anti-correlated with pangenome openness (Spearman rho = -0.193, p = 2.2e-12), possibly because open-pangenome species accumulate more rare or singleton AMR genes below the 5% threshold. [src: amr_strain_variation] This result connects within-species resistome heterogeneity to [[concepts/pangenome-integration]] and to the broader problem of [[concepts/within-species-resistome-heterogeneity]]. [src: amr_strain_variation]

## Co-inherited resistance islands

Resistance islands—sets of AMR genes with strong pairwise co-occurrence—were detected in 705 species, representing 54% of the species analyzed, with 1,517 islands overall. [src: amr_strain_variation] Islands had a mean size of 6.2 genes, a median size of 4 genes, a maximum size of 43 genes, and a mean phi coefficient of 0.827; phi measures pairwise co-occurrence, so this value indicates tight co-inheritance. [src: amr_strain_variation]

Of the 1,517 islands, 1,343 (88%) contained genes from multiple resistance mechanisms. [src: amr_strain_variation] Efflux pumps occurred in 954 islands and enzymatic inactivation occurred in 698, making them the most common components. [src: amr_strain_variation] The complete mechanism counts were Other/Unclassified, 1,026; Efflux, 954; Enzymatic inactivation, 698; Oxidoreductase, 694; Regulatory, 502; Beta-lactamase, 341; Target modification, 293; and Cell wall modification, 137. [src: amr_strain_variation]

These multi-mechanism islands support [[concepts/cofitness-network-architecture]] by identifying tightly co-inherited AMR modules. [src: amr_strain_variation] They do not establish co-selection or functional synergy, because genes can be linked on the same mobile genetic element without producing a shared functional advantage. [src: amr_strain_variation]

## Phylogenetic structure

Phylogenetic structure was assessed by comparing average nucleotide identity (ANI) distance matrices with AMR Jaccard distance matrices using a Mantel test, which evaluates correlation between two distance matrices. [src: amr_strain_variation] Across 1,261 species, 701 (55.6%) showed significant phylogenetic signal at FDR < 0.05, where FDR is the false-discovery rate. [src: amr_strain_variation] The median Mantel r for all AMR was 0.247, and 87.8% of species showed positive correlation, indicating that closely related strains generally shared more AMR genes. [src: amr_strain_variation]

Non-core, putatively acquired AMR genes showed a stronger phylogenetic signal than core, intrinsic genes: median Mantel r was 0.222 for non-core genes versus 0.117 for core genes, with a paired t-test of t = -8.35, p = 7.0e-16, n = 489. [src: amr_strain_variation] This supports the hypothesis that acquired resistance elements can become stably maintained and vertically transmitted within lineages. [src: amr_strain_variation] The comparison is not purely biological, because near-universal core genes have little Jaccard-distance variance, which can suppress distance-based Mantel correlations independently of biology. [src: amr_strain_variation] This finding relates to [[concepts/intrinsic-versus-acquired-resistance]] and to phylogenetic confounding in [[concepts/phylogenetic-confounding-of-pangenome-associations]]. [src: amr_strain_variation]

## AMR ecotypes and environment

Among 974 species with at least 15 genomes suitable for clustering, 190 (19.5%) formed >=2 distinct AMR ecotypes. [src: amr_strain_variation] Ecotypes were identified with UMAP, a nonlinear dimensionality-reduction method, followed by DBSCAN density-based clustering; the median silhouette score was 0.620. [src: amr_strain_variation]

Case-study UMAP plots for Klebsiella pneumoniae, Staphylococcus aureus, and Salmonella enterica showed visible environmental structuring. [src: amr_strain_variation] However, environment-ecotype association testing was severely limited: 52.7% of genomes had no classifiable isolation_source, and only 2 species had sufficient within-species environmental diversity for chi-squared testing after strict expected-frequency criteria. [src: amr_strain_variation] Consequently, the case studies suggest environmental structuring as a hypothesis but do not establish a general environment-ecotype association. [src: amr_strain_variation]

Both a rule-based keyword classification approximating BacDive categories and an NCBI keyword-based environment annotation found that host-associated species carried more AMR genes per genome than terrestrial or aquatic species, with Kruskal-Wallis p < 0.05. [src: amr_strain_variation] The NCBI keyword classifier assigned environments to 1,190/1,307 species (91%), whereas the BacDive approximation classified 459/1,307 species (35%); both methods agreed in direction, with human-clinical isolates having the highest AMR burden. [src: amr_strain_variation] These observations extend [[concepts/environmental-resistome]] while remaining limited by approximate classifiers and incomplete metadata. [src: amr_strain_variation]

## Temporal and sampling constraints

Among 513 species with >=20 genomes spanning >=3 years after 1990, none showed a significant temporal trend in AMR gene count after Benjamini-Hochberg FDR correction. [src: amr_strain_variation] Slopes were approximately symmetrically distributed, with 251 positive and 262 negative slopes. [src: amr_strain_variation] This null result should not be interpreted as evidence that AMR accumulation lacks temporal trends, because collection-date metadata were sparse and noisy and only 70% of genomes had parseable collection dates. [src: amr_strain_variation]

The GTDB/NCBI genome collection was heavily biased toward clinical and human-associated isolates, particularly for Klebsiella pneumoniae, Staphylococcus aureus, and Escherichia coli, while environmental species were underrepresented. [src: amr_strain_variation] AMR detection relied on AMRFinderPlus, so novel resistance mechanisms absent from that database were missed. [src: amr_strain_variation] ANI extraction for Mantel tests was limited to species with <=500 genomes, excluding Escherichia coli, with 15,388 genomes, and Klebsiella pneumoniae, with 14,240 genomes, from phylogenetic-signal analysis. [src: amr_strain_variation]

## Tensions

The dataset supports strong within-species structure in AMR repertoires, but it does not support a general causal interpretation of that structure. [src: amr_strain_variation] Resistance-island co-occurrence indicates linkage rather than demonstrated co-selection or functional synergy, and visible environmental separation in selected ecotype plots is not validated by adequately powered within-species tests. [src: amr_strain_variation] The stronger phylogenetic signal of non-core genes also partly reflects the low Jaccard-distance variance expected for nearly universal core genes, so the biological contribution of vertical transmission remains difficult to separate from a statistical effect. [src: amr_strain_variation]

## Open Directions

- Use the 1,305 genome-by-AMR presence/absence matrices and genomic-context mapping to test whether the 1,517 resistance islands reside on plasmids, chromosomes, integron boundaries, or insertion sequences, and whether physical context predicts persistence across lineages. [src: amr_strain_variation]
- Subsample species with >500 genomes and repeat ANI–AMR Mantel analyses to determine whether the phylogenetic signal generalizes to mega-species excluded by the current computational cap. [src: amr_strain_variation]
- Curate collection dates and isolation_source metadata, then apply temporal regression and adequately powered within-species association tests to distinguish AMR change through time from sampling composition. [src: amr_strain_variation]
- Combine AMR ecotype assignments with virulence-factor profiles and metabolic pathway variation to test whether resistance-defined lineages also differ in pathogenicity-associated or ecological functions. [src: amr_strain_variation]
- Apply predictive modeling to the per-gene prevalence records and resistance-island records to ask whether existing co-inheritance patterns predict future AMR gene co-acquisition. [src: amr_strain_variation]
- Reanalyze AMR repertoires with resistance databases beyond AMRFinderPlus to quantify how database scope changes estimates of rare, variable, and fixed within-species resistance. [src: amr_strain_variation]
