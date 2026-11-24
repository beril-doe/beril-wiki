---
type: "Method"
description: "Phylogeny-aware regression proposed to remove phylogenetic signal before testing phenotype–metal associations."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
aliases: ["PGLS", "Pagel's lambda", "Pagel's λ", "phylogenetic signal λ"]
---
# Phylogenetic generalized least squares

This page covers phylogenetic generalized least squares, a phylogeny-aware regression proposed to remove phylogenetic signal before testing phenotype–metal associations. Also known as PGLS, Pagel's lambda and phylogenetic signal λ. Several projects propose it as a way to remove phylogenetic signal before testing trait associations. [src: bacdive_phenotype_metal_tolerance] Two projects ran it on genus-level data. One found a negative association between metal-gene density and niche breadth, and the other found a positive association between metal type diversity and niche breadth. [src: comprehensive_metal_ecology, microbeatlas_metal_ecology]

## Key facts

- PGLS or phylogenetic PCA (principal component analysis) is proposed to formally remove phylogenetic signal before testing phenotype–metal associations. [src: bacdive_phenotype_metal_tolerance]
- The same proposal appears for the metal cross-resistance conservation analysis. [src: metal_cross_resistance]
- Pagel's λ measures phylogenetic signal: λ = 0 means no signal (environmentally structured) and λ = 1 means Brownian motion evolution (fully phylogenetically structured). [src: microbeatlas_metal_ecology]
- Phylogenetic signal can be high for chemical sensitivity traits: Van Assche & Álvarez (2017) found values up to λ = 0.98 in *Acinetobacter*. [src: bacdive_phenotype_metal_tolerance]

## Applied results

### Metal-gene density and niche breadth

In 1,574 bacterial genera matched across the GTDB phylogeny and global MGnify MAG (metagenome assembled genomes) data, per-Mb Tier 1+2 metal-gene KO (KEGG ortholog) density was negatively associated with standardised Levins' niche breadth. The estimates were β = −0.021, SE = 0.0037, t = −5.63, p = 2.1×10⁻⁸, FDR (false discovery rate) joint p = 6.4×10⁻⁸, Pagel's λ = 0.757, ΔAIC = −29.4 and r² = 0.046. [src: comprehensive_metal_ecology] The baseline conditional model gave β = −0.0207 and p = 2.1×10⁻⁸. [src: comprehensive_metal_ecology]

The association also appeared with no phylogenetic correction, under λ = 0 ordinary least squares (β = −0.032, p ≈ 0). [src: comprehensive_metal_ecology] It appeared under λ = 1 Brownian motion as well (β = −0.018, p = 3.7×10⁻⁶). The report reads this as showing the result is not an artefact of any single phylogenetic correction assumption. [src: comprehensive_metal_ecology]

Pagel's λ for pH niche (0.11–0.20) was lower than for Levins' B_std (0.757). The report interprets this to mean specific environmental-axis niches are mostly shaped by ecology rather than phylogeny. [src: comprehensive_metal_ecology]

### Metal type diversity in MicrobeAtlas genera

The PGLS subset was 606 bacterial genera with ≥ 3 OTUs (operational taxonomic units), present in the GTDB r214 bacterial genus tree, and with metal AMR (antimicrobial resistance) data from kbase_ke_pangenome. Predictors were z-scored, and the Bonferroni threshold was p < 0.0083 for 6 simple models. [src: microbeatlas_metal_ecology] Metal type diversity is an integer count from 1 to 7, used as a continuous z-scored predictor in a Gaussian PGLS. [src: microbeatlas_metal_ecology]

Models were fitted jointly with λ by maximum likelihood using ape::gls and nlme::corPagel, with data sorted to tree$tip.label order. [src: microbeatlas_metal_ecology] A unit test with synthetic λ = 0.8 and β = 0.05 and scrambled rows passed. Sorted PGLS recovered the correct λ and β, and unsorted PGLS failed. [src: microbeatlas_metal_ecology] Standalone λ was computed with phytools::phylosig(method='lambda', test=TRUE) against GTDB r214 genus-representative trees. [src: microbeatlas_metal_ecology]

For Levins' B_std against metal types, the model gave n = 606, λ_PGLS = 0.708, β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴ and ΔAIC = −12.4, which meets Bonferroni significance. [src: microbeatlas_metal_ecology] Metal type diversity was the only bacterial metal AMR predictor to survive Bonferroni correction in the simple models. [src: microbeatlas_metal_ecology] The β of +0.021 per SD (standard deviation) is the covariation left after removing shared ancestry estimated by the λ-transformed VCV matrix. [src: microbeatlas_metal_ecology]

### Two kinds of λ

Standalone λ for bacterial B_std was 0.787 and PGLS-estimated λ was 0.708, a difference of Δλ = 0.079 that the report calls expected and informative. [src: microbeatlas_metal_ecology] Standalone λ is the phylogenetic signal in B_std without predictors. It measures how much of the total variance Brownian-motion covariance explains. [src: microbeatlas_metal_ecology] PGLS λ is the residual signal after the predictor's variance is removed. [src: microbeatlas_metal_ecology]

The report explains the gap by the predictor's own signal (λ_metal_types = 0.335). Including it as a covariate removes some phylogenetically structured variance. [src: microbeatlas_metal_ecology] It reads the drop from 0.787 to 0.708 (a 10% reduction) as metal type diversity accounting for about 10% of B_std's phylogenetic covariance. [src: microbeatlas_metal_ecology]

### Soil metal functional genomics

Biome-stratified PGLS showed distinct metal–COG relationships in soil, marine and wastewater. The report takes this to indicate environment-specific functional responses rather than a universal resistance programme. [src: soil_metal_functional_genomics] This report is preliminary: Spearman correlation, db-RDA and PGLS analyses are complete in NB01–NB04, while NB05 effect size and spatial validation and NB06 figures are pending. [src: soil_metal_functional_genomics]

## Caveats and proposed work

- The 28 organisms in the metal cross-resistance report are not phylogenetically independent. Formal comparative methods such as PGLS or independent contrasts would strengthen its conservation claim. [src: metal_cross_resistance]
- In the Pseudomonas carbon-ecology report, lifestyle-associated differences within Pseudomonas_E are subtle. The analyses do not explicitly control phylogenetic non-independence among species. [src: pseudomonas_carbon_ecology]
- That report proposes PGLS or phylogenetic logistic regression with the GTDB species tree to test whether lifestyle–pathway associations persist after controlling for relatedness. [src: pseudomonas_carbon_ecology]

See also [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]], [[concepts/metal-gene-density-and-ecological-niche-breadth]] and [[concepts/phylogenetic-signal-of-gene-content-and-traits]].
