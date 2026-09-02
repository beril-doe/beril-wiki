---
type: "Method"
description: "Phylogeny-aware regression for testing trait associations"
sources: ["summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Phylogenetic Generalized Least Squares

## What this entity is

**Canonical name:** phylogenetic generalized least squares. [src: microbeatlas_metal_ecology]

**Known alias:** PGLS. [src: microbeatlas_metal_ecology]

**Stable external identifier:** Not specified in the source. [src: microbeatlas_metal_ecology]

Phylogenetic generalized least squares is a regression method that tests associations between traits while accounting for shared evolutionary history. [src: microbeatlas_metal_ecology] In the [[summaries/microbeatlas_metal_ecology__REPORT]] study, PGLS was used to evaluate whether genus-level metal-resistance traits predicted inferred ecological niche breadth beyond phylogenetic effects. [src: microbeatlas_metal_ecology]

## Use in the MicrobeAtlas metal-ecology study

The primary PGLS analysis included 606 bacterial genera with AMR data from GTDB r214 and tested metal type diversity, total AMR cluster count, and core AMR fraction as predictors of Levins' B_std niche breadth. [src: microbeatlas_metal_ecology]

Metal type diversity was positively associated with niche breadth in the primary simple model, with β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴, and ΔAIC = −12.4. [src: microbeatlas_metal_ecology] This result survived Bonferroni correction across 6 simple models using a threshold of p < 0.0083. [src: microbeatlas_metal_ecology]

In the multi-predictor PGLS model, metal type diversity retained a positive effect with β = +0.023 and p = 5.5×10⁻⁴. [src: microbeatlas_metal_ecology] Total AMR cluster count was not significant in that model, with β = −0.002, SE = 0.0065, and p = 0.789, while core AMR fraction was also not significant, with β = +0.006, SE = 0.0054, and p = 0.288. [src: microbeatlas_metal_ecology]

The raw OLS correlation between mean metal type diversity and Levins' B_std was r ≈ 0.21, whereas the PGLS coefficient represented covariation after accounting for shared ancestry. [src: microbeatlas_metal_ecology]

## Phylogenetic signal and robustness

Levins' B_std had strong phylogenetic signal across 1,264 genera, with Pagel's λ = 0.787 and p = 7.9×10⁻¹⁰². [src: microbeatlas_metal_ecology] Habitat range had an even stronger signal, with λ = 0.909 and p = 1.4×10⁻¹⁵⁷. [src: microbeatlas_metal_ecology]

The standalone Pagel's λ for bacterial B_std was 0.787, while the PGLS-estimated λ was 0.708, a difference of Δλ = 0.079. [src: microbeatlas_metal_ecology] The report interpreted the lower residual λ as expected because metal type diversity itself had phylogenetic signal, while noting that residual λ = 0.708 remained strongly non-zero. [src: microbeatlas_metal_ecology]

Metal type diversity had intermediate phylogenetic signal among the 606 bacterial genera, with λ = 0.335 and p = 1.1×10⁻²³, compared with λ = 0.260 and p = 6.1×10⁻²⁸ for total AMR cluster count and λ = 0.441 and p = 1.8×10⁻⁸ for core AMR fraction. [src: microbeatlas_metal_ecology]

Adding pangenome coverage retained the metal type association, with β = +0.0204, SE = 0.0057, and p = 3.4×10⁻⁴ in the simple model, and β = +0.0224, SE = 0.0067, and p = 8.3×10⁻⁴ in the model containing all three AMR predictors. [src: microbeatlas_metal_ecology]

Controlling for genome size produced a metal type coefficient of β = +0.0218, SE = 0.0061, and p = 3.6×10⁻⁴, while log(genome size) had β = +0.0263, SE = 0.0069, and p = 1.5×10⁻⁴. [src: microbeatlas_metal_ecology] The full model had AIC = −641.1 compared with AIC = −630.3 for the genome-size-only model, giving ΔAIC = 10.8 in favor of including metal type diversity. [src: microbeatlas_metal_ecology]

In a three-covariate PGLS model using 527 genera, metal type diversity had β = +0.0218, SE = 0.0061, t = 3.60, and p = 3.5×10⁻⁴, while log(n_species) had β = +0.0052, SE = 0.0057, t = 0.90, and p = 0.366, and log(genome size) had β = +0.0255, SE = 0.0069, t = 3.68, and p = 2.6×10⁻⁴. [src: microbeatlas_metal_ecology] That model had λ = 0.628, and the metal type effect had BH-FDR q = 0.003. [src: microbeatlas_metal_ecology]

A 200-iteration rarefaction analysis had a median metal type coefficient of +0.0147, an IQR of +0.0126–+0.0166, a median p-value of 0.0054, 89.5% of iterations with p < 0.05, 57.5% Bonferroni-significant iterations at p < 0.0083, and a median λ of 0.704. [src: microbeatlas_metal_ecology]

The strict 5% within-environment prevalence analysis reduced the PGLS sample size from 606 to 379 genera and produced β = +0.0166, SE = 0.0099, p = 0.092, and λ = 0.526, compared with β = +0.0215, SE = 0.0056, p = 1.5×10⁻⁴, and λ = 0.708 in the original analysis. [src: microbeatlas_metal_ecology]

The archaeal PGLS analysis included 48 genera and produced β = +0.0145, SE = 0.0198, t = 0.73, p = 0.467, and λ = 0.567. [src: microbeatlas_metal_ecology] The report considered this analysis severely underpowered, estimating formal power of 11% at α = 0.05 and requiring n ≥ 702 for 80% power at α = 0.05 or n ≥ 1,084 at Bonferroni α = 0.0083 under the observed effect and error assumptions. [src: microbeatlas_metal_ecology]

## Extension to soil metal functional genomics

The [[summaries/soil_metal_functional_genomics__REPORT]] report **supports** using PGLS to test whether metal–functional-gene relationships persist across related organisms: biome-stratified analyses found distinct metal–COG relationships in soil, marine, and wastewater environments rather than a universal resistance programme. [src: soil_metal_functional_genomics] COG means Cluster of Orthologous Groups functional category. [src: soil_metal_functional_genomics] This is an observational comparative result, and effect-size and spatial validation remain pending. [src: soil_metal_functional_genomics]

The soil study used PGLS alongside Spearman correlation and distance-based redundancy analysis (db-RDA) across 51,748 soil samples and nine metals. [src: soil_metal_functional_genomics] Its PGLS application **refines** the existing emphasis on phylogenetic non-independence by shifting the question from genus-level resistance diversity and niche breadth to environment-specific metal–COG relationships; it does not establish that any individual metal caused the observed functional shift. [src: soil_metal_functional_genomics]

## Extension to carbon-pathway ecology

The [[summaries/pseudomonas_carbon_ecology__REPORT]] report **refines** the method's role as a needed control for phylogenetic non-independence: its carbon-pathway analysis found that the dominant PCA separation was between *Pseudomonas* s.s. and *Pseudomonas_E*, rather than among lifestyles within *Pseudomonas_E*. [src: pseudomonas_carbon_ecology] The report therefore proposes PGLS, or phylogenetic logistic regression, using the GTDB species tree to test whether environment-associated pathway differences persist after accounting for relatedness. [src: pseudomonas_carbon_ecology]

This proposed application is not yet a PGLS result; it is a follow-up to a significant permutation association between carbon profiles and isolation environment (p = 0.006) and a modest Random Forest balanced accuracy of 0.408 +/- 0.169. [src: pseudomonas_carbon_ecology] It **supports** retaining phylogenetic structure as an explicit concern while cautioning against interpreting the observed ecological signal as independent lifestyle adaptation. [src: pseudomonas_carbon_ecology]

## Interpretation and limitations

The PGLS association supports the interpretation that genera with diverse metal-resistance repertoires tend to have broader inferred ecological ranges, but the cross-sectional analysis cannot distinguish causal ecological expansion from increased opportunities for resistance-gene acquisition or a shared factor such as genome size, metabolic versatility, or biofilm capacity. [src: microbeatlas_metal_ecology]

The study treated Levins' B_std as an inferred niche-breadth measure from MicrobeAtlas detections, while noting that it is a sequencing-effort proxy rather than confirmed ecological range. [src: microbeatlas_metal_ecology] Genus-level aggregation also means that a broad genus score may reflect different species occupying different habitats rather than a single organism being a generalist. [src: microbeatlas_metal_ecology]

The analysis modeled metal type diversity, an integer count from 1–7, as a continuous z-scored predictor in a Gaussian PGLS framework. [src: microbeatlas_metal_ecology] The report identified discrete-state, threshold, Poisson, and negative-binomial phylogenetic models as possible alternatives. [src: microbeatlas_metal_ecology]

The study used the GTDB r214 genus-representative tree for its phylogenetic analyses and did not test sensitivity to NCBI, SILVA-based 16S, or other GTDB trees. [src: microbeatlas_metal_ecology]

For the soil application, co-varying chromium, copper, lead, and zinc leave it unresolved whether individual COG associations are metal-specific or reflect multi-metal contamination; planned partial-correlation models and spatial validation are therefore needed before treating the biome-specific PGLS relationships as mechanistic. [src: soil_metal_functional_genomics]

## Related pages

- [[concepts/metal-cross-resistance]] — connects metal-type diversity with cross-metal resistance ecology. [src: microbeatlas_metal_ecology]
- [[concepts/environmental-resistome]] — links AMRFinderPlus resistance annotations with environmental occurrence data. [src: microbeatlas_metal_ecology]
- [[concepts/environment-embedding-geography]] — relates environmental distributions to resistance repertoires and the proposed phylogeny-aware analysis of carbon-pathway ecology. [src: microbeatlas_metal_ecology, pseudomonas_carbon_ecology]
- [[concepts/gene-function-acquisition-depth]] — frames the contrast between phylogenetically conserved traits and more labile metal-resistance traits. [src: microbeatlas_metal_ecology]
- [[concepts/ecotype-environment-gene-content]] — connects ecological breadth with genus-level gene-content variation and the proposed testing of metabolic ecotypes after phylogenetic correction. [src: microbeatlas_metal_ecology, pseudomonas_carbon_ecology]
- [[entities/metal-fitness-atlas]] — provides a related cross-metal resistance resource. [src: microbeatlas_metal_ecology]
