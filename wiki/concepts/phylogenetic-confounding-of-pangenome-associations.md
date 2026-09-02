---
type: "Concept"
description: "Phylogeny can obscure or create aggregate pangenome associations."
sources: ["summaries/amr_pangenome_atlas__REPORT.md"]
---
# Phylogenetic Confounding of Pangenome Associations

Phylogenetic confounding occurs when differences among taxonomic groups dominate an aggregate association, potentially hiding relationships that exist within lineages or creating apparent relationships because two traits share the same taxonomic distribution. [src: amr_pangenome_atlas]

The [[summaries/amr_pangenome_atlas__REPORT]] provides a direct example using antimicrobial-resistance (AMR) burden and pangenome openness across bacterial species. [src: amr_pangenome_atlas] Pangenome openness positively correlated with AMR count in 8/10 tested phyla, but the overall correlation across the dataset was near zero (rho=0.006), indicating that phylogeny dominated the aggregate signal. [src: amr_pangenome_atlas] The strongest within-phylum associations were observed in Bacillota (rho=0.219, p=1.0e-16) and Bacillota_C (rho=0.374, p=3.1e-5). [src: amr_pangenome_atlas]

This pattern **supports** the interpretation that a near-zero global association does not demonstrate the absence of a relationship between openness and AMR burden. [src: amr_pangenome_atlas] Instead, associations may be positive within several phyla while differing in magnitude, direction, or baseline across phyla, causing them to cancel when species are pooled. [src: amr_pangenome_atlas] The result is an association rather than a causal inference, because the analysis describes correlations across pangenome species and does not by itself establish that openness causes AMR accumulation. [src: amr_pangenome_atlas]

Phylogeny can also generate an aggregate association when both variables are concentrated in the same clades, even if the variables are not mechanistically related within those clades. [src: amr_pangenome_atlas] In this dataset, Gammaproteobacteria contained 45% of all AMR clusters (37,752/83,008), while the taxonomic census recorded 4,992 Pseudomonadota species with AMR, 42,904 total AMR hits, 8.6 mean AMR hits per species, and 67.0% of species carrying AMR. [src: amr_pangenome_atlas] These taxonomic concentrations make lineage composition a necessary consideration when interpreting pan-bacterial AMR summaries. [src: amr_pangenome_atlas]

The same issue applies to comparisons of environmental AMR patterns. [src: amr_pangenome_atlas] Human/Clinical species carried 10.6 AMR clusters per species (n=2,248), compared with 4.6 for Soil/Terrestrial (n=2,469), 3.9 for Aquatic (n=1,827), and 3.0 for Animal (n=959), with a significant Kruskal-Wallis result (H=440, p=7.0e-93). [src: amr_pangenome_atlas] Clinical AMR was less core (30.8%) than soil AMR (58.1%) or plant AMR (63.1%), but these contrasts may combine environmental effects with differences in taxonomic composition, sampling, and genome representation. [src: amr_pangenome_atlas] The report identifies database sampling bias because genome collections over-represent clinical pathogens, potentially inflating AMR counts for human-associated species. [src: amr_pangenome_atlas]

The concept connects directly to [[concepts/pangenome-integration]], because interpreting pangenome openness requires integrating taxonomy, gene-family distributions, and environmental metadata rather than treating species as exchangeable observations. [src: amr_pangenome_atlas] It also qualifies interpretations of [[concepts/environmental-resistome]]: environmental and clinical AMR differences should be tested with lineage-aware models before being attributed to environment alone. [src: amr_pangenome_atlas] Associations between AMR burden and [[concepts/condition-specific-fitness]] should likewise be evaluated across comparable lineages and organisms, because cross-organism fitness measurements can inherit taxonomic structure. [src: amr_pangenome_atlas]

## Tensions

The aggregate result and the within-phylum results point in different directions: the overall openness–AMR correlation was near zero (rho=0.006), whereas openness positively correlated with AMR count in 8/10 tested phyla, including Bacillota and Bacillota_C. [src: amr_pangenome_atlas] This is a tension between a pooled analysis that suggests little association and stratified analyses that show positive associations in multiple lineages; the report attributes the discrepancy to phylogenetic dominance of the aggregate signal rather than resolving it as a causal effect. [src: amr_pangenome_atlas]

## Open Directions

- Use the existing species-level openness, AMR-count, and taxonomic data with phylogenetic generalized least squares (PGLS), a regression method that models covariance among related species, to test whether the openness–AMR association remains after accounting for shared ancestry. [src: amr_pangenome_atlas]
- Combine the pangenome species table with a species phylogeny and fit within-phylum hierarchical models to ask whether the positive associations in 8/10 phyla share a common slope or instead arise from lineage-specific processes. [src: amr_pangenome_atlas]
- Reanalyze the six-category environmental comparison using taxonomic matching or lineage-stratified permutation tests to determine whether the clinical, soil, plant, aquatic, and animal contrasts persist after controlling for uneven taxonomic sampling. [src: amr_pangenome_atlas]
- Add environmental metadata and AlphaEarth embeddings for the currently under-covered genomes, then use phylogeny-aware partial association analyses to test whether environmental diversity predicts AMR count independently of lineage. [src: amr_pangenome_atlas]
- Estimate AMR gene gain and loss rates on a dated or calibrated species phylogeny, and test whether pangenome openness predicts transition rates rather than only present-day AMR counts. [src: amr_pangenome_atlas]
