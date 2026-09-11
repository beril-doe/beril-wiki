---
type: "Summary"
description: "Large-scale analysis of structured within-species antimicrobial-resistance variation"
doc_type: "short"
full_text: "sources/amr_strain_variation__REPORT.md"
---
# Within-Species AMR Strain Variation

## Overview

This report analyzes antimicrobial-resistance (AMR) gene variation across 1,305 species and 180,025 genomes using the KBase/KBase Data Lakehouse pangenome resource. It finds that within-species AMR repertoires are extensive but structured by prevalence class, tightly co-inherited resistance islands, phylogeny, lineage-associated ecotypes, and environment. [src: amr_strain_variation]

## Key Findings

### AMR genes are usually variable or rare within species

Among 37,444 AMR gene-species records, 51.3% were rare, present in <=5% of strains; 41.3% were variable, present in 5-95%; and 7.5% were fixed, present in >=95%. The median variability index was 0.526, and the median pairwise Jaccard distance—a distance based on shared versus differing gene repertoires—was 0.435, indicating that strains within the same species shared less than 60% of their AMR repertoire. [src: amr_strain_variation]

Atlas conservation class strongly predicted within-species prevalence: 77.3% of Core AMR genes were fixed, while 78.7% of Singletons were rare. Auxiliary genes were 57.3% variable and 42.7% rare. AMR variability weakly anti-correlated with pangenome openness (Spearman rho = -0.193, p = 2.2e-12), possibly because open-pangenome species accumulate more rare or singleton AMR genes below the 5% threshold. [src: amr_strain_variation]

### Resistance islands are widespread and tightly co-inherited

The analysis detected 1,517 resistance islands across 705 species, or 54% of the species analyzed. Islands had a mean size of 6.2 genes, a median size of 4 genes, a maximum size of 43 genes, and a mean phi coefficient of 0.827; phi measures pairwise co-occurrence and the value indicates very tight co-inheritance. Of the islands, 1,343/1,517 (88%) contained genes from multiple resistance mechanisms. Efflux pumps occurred in 954 islands and enzymatic inactivation in 698, making them the most common components. [src: amr_strain_variation]

The complete island mechanism counts were: Other/Unclassified, 1,026; Efflux, 954; Enzymatic inactivation, 698; Oxidoreductase, 694; Regulatory, 502; Beta-lactamase, 341; Target modification, 293; and Cell wall modification, 137. The multi-mechanism composition suggests coordinated defense against multiple drug classes, but co-occurrence does not establish co-selection or functional synergy. [src: amr_strain_variation]

### AMR variation commonly tracks phylogeny

Mantel tests compared ANI (average nucleotide identity) distance matrices with AMR Jaccard distance matrices across 1,261 species. A Mantel test assesses correlation between two distance matrices; 701/1,261 species (55.6%) showed significant phylogenetic signal at FDR < 0.05, where FDR is the false-discovery rate. The median Mantel r for all AMR was 0.247, and 87.8% of species showed positive correlation, indicating that closely related strains tend to share more AMR genes. [src: amr_strain_variation]

Non-core, putatively acquired AMR genes showed stronger phylogenetic signal than core, intrinsic genes: median Mantel r was 0.222 for non-core genes versus 0.117 for core genes, with a paired t-test of t = -8.35, p = 7.0e-16, n = 489. This supports the hypothesis that acquired resistance elements can become stably maintained and vertically transmitted within lineages, although the report notes that near-universal core genes have little Jaccard-distance variance, which can suppress distance-based Mantel correlations independently of biology. [src: amr_strain_variation]

### Distinct AMR ecotypes occur in a subset of species

Of 974 species with at least 15 genomes suitable for clustering, 190 (19.5%) formed >=2 distinct AMR ecotypes. Ecotypes were identified using UMAP, a nonlinear dimensionality-reduction method, followed by DBSCAN density-based clustering; the median silhouette score was 0.620. Environment-ecotype association testing was limited because 52.7% of genomes had no classifiable isolation_source, and only 2 species had sufficient within-species environmental diversity for chi-squared testing after strict expected-frequency criteria. [src: amr_strain_variation]

Case-study UMAP plots for Klebsiella pneumoniae, Staphylococcus aureus, and Salmonella enterica showed visible environmental structuring, but the underpowered statistical tests do not establish a general environment-ecotype association. Escherichia coli was excluded from case studies because it exceeded the 500-genome computational cap. [src: amr_strain_variation]

### Temporal trends were not detected after correction

Among 513 species with >=20 genomes spanning >=3 years after 1990, none showed a significant temporal trend in AMR gene count after Benjamini-Hochberg FDR correction. Slopes were approximately symmetrically distributed, with 251 positive and 262 negative slopes. The report interprets this null result cautiously because collection-date metadata are sparse and noisy, rather than as evidence that AMR accumulation lacks temporal trends. [src: amr_strain_variation]

### Host-associated species carry more AMR genes

Both rule-based keyword classification approximating BacDive categories and NCBI keyword-based environment annotation found that host-associated species carried more AMR genes per genome than terrestrial or aquatic species, with Kruskal-Wallis p < 0.05. The NCBI keyword classifier assigned environments to 1,190/1,307 species (91%), while the BacDive approximation classified 459/1,307 species (35%); both methods agreed in direction, with human-clinical isolates having the highest AMR burden. [src: amr_strain_variation]

## Scale and Generated Data

The study analyzed 1,305 species, 180,025 genomes, 37,444 AMR gene-species records, 1,517 resistance islands, 1,261 species with Mantel tests, 974 species with ecotype analysis, and 513 species with temporal data. Generated resources included 1,305 genome-by-AMR presence/absence matrices, 1,305 per-species variation summaries, 37,444 per-gene prevalence records, 1,517 resistance-island records, 1,305 phi summaries, 1,259 ANI matrices, 1,261 Mantel results, 176,177 ecotype assignments, 974 ecotype summaries, 2 environment-ecotype tests, 513 temporal regression results, 1,307 BacDive/NCBI environment bridge records, and an integrated summary with one row per species across 1,305 species. [src: amr_strain_variation]

## Caveats

- The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly for Klebsiella pneumoniae, Staphylococcus aureus, and Escherichia coli; environmental species are underrepresented. [src: amr_strain_variation]
- Metadata sparsity limits interpretation of temporal and ecological results. Only 70% of genomes had parseable collection dates, and 52.7% had no classifiable isolation_source. [src: amr_strain_variation]
- AMR detection relies on the AMRFinderPlus database, so novel resistance mechanisms absent from that database are missed. [src: amr_strain_variation]
- ANI extraction for Mantel tests was limited to species with <=500 genomes, excluding mega-species such as Escherichia coli (15,388 genomes) and Klebsiella pneumoniae (14,240 genomes) from phylogenetic-signal analysis. [src: amr_strain_variation]
- BacDive and NCBI keyword environment classifiers are approximate, and dedicated metadata curation would improve ecotype analyses. [src: amr_strain_variation]
- Resistance-gene co-occurrence in islands does not prove co-selection; genes may simply be linked on the same mobile genetic element without functional synergy. [src: amr_strain_variation]
- The stronger phylogenetic signal of non-core than core AMR genes may be partly statistical: core genes are nearly universal by definition, producing little Jaccard-distance variance and suppressing Mantel r. [src: amr_strain_variation]

## Future Directions

The report proposes detailed UMAP and heatmap case studies for Klebsiella pneumoniae, Escherichia coli, Staphylococcus aureus, Pseudomonas aeruginosa, Salmonella enterica, and Acinetobacter baumannii; subsampling strategies for Mantel tests on species with >500 genomes; curated collection dates for temporal analysis; genomic-context mapping of resistance islands to plasmids, chromosomes, integron boundaries, and insertion sequences; predictive modeling of future AMR gene co-acquisition; and integration of AMR ecotypes with virulence-factor profiles and metabolic pathway variation. [src: amr_strain_variation]

## Slots Into

- [[concepts/environmental-resistome]] — adds large-scale evidence that host association, environmental metadata, resistance islands, and lineage structure organize AMR repertoires within species. [src: amr_strain_variation]
- [[concepts/pangenome-integration]] — quantifies how atlas conservation classes and pangenome openness relate to within-species AMR prevalence and variation. [src: amr_strain_variation]
- [[concepts/cofitness-network-architecture]] — provides resistance-island co-occurrence evidence and identifies tightly co-inherited multi-mechanism AMR modules. [src: amr_strain_variation]
