---
type: Summary
description: Global PGLS links metal-resistance diversity to bacterial niche breadth.
doc_type: short
full_text: ../sources/microbeatlas_metal_ecology__REPORT.md
title: Metal Resistance Ecology — Phylogenetic Conservation vs. Environmental Selection
sources:
- id: microbeatlas_metal_ecology
  resource: ../sources/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
---
# Metal Resistance Ecology — Phylogenetic Conservation vs. Environmental Selection

## Overview

This study links genus-level metal-resistance type diversity, inferred from AMRFinderPlus pangenome annotations across 6,789 GTDB species, with global ecological niche breadth derived from a 464,000-sample 16S amplicon atlas (MicrobeAtlas). Across 1,264 bacterial genera with ≥ 3 OTUs, niche breadth was phylogenetically conserved, while phylogenetic generalized least squares (PGLS), which models trait associations while accounting for shared evolutionary history, tested whether metal-resistance traits predicted niche breadth beyond phylogeny. The analysis used 606 bacterial genera with AMR data and found that metal type diversity, rather than total AMR gene burden or core AMR fraction, was associated with broader inferred ecological ranges. [^microbeatlas_metal_ecology]

The primary evidence is correlational: the cross-sectional comparison cannot distinguish whether metal tolerance enables habitat expansion, broad ecological range increases opportunities for metal-resistance gene acquisition, or a shared factor such as genome size, metabolic versatility, or biofilm capacity promotes both traits. The report therefore concludes that genera with diverse metal-resistance repertoires are, on average, broader ecological generalists in the global microbiome, not that metal-resistance diversity causes ecological generalism. [^microbeatlas_metal_ecology]

## Key Findings

### Phylogenetic conservation and the primary PGLS association

Bacterial Levins' B_std niche breadth showed strong phylogenetic signal, with Pagel's λ = 0.787 and p = 7.9×10⁻¹⁰² across 1,264 genera; habitat range, measured as the number of detected environment categories, was more conserved with λ = 0.909 and p = 1.4×10⁻¹⁵⁷. In the primary PGLS analysis of 606 genera, metal type diversity was the only metal AMR predictor surviving Bonferroni correction across 6 simple models (β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴; threshold p < 0.0083). [^microbeatlas_metal_ecology]

The multi-predictor model retained a positive metal type effect (β = +0.023, p = 5.5×10⁻⁴), whereas total AMR cluster count (β = −0.002, SE = 0.0065, p = 0.789) and core AMR fraction (β = +0.006, SE = 0.0054, p = 0.288) were not significant. The simple PGLS estimates were β = +0.021 for metal types (SE = 0.0056, p = 1.5×10⁻⁴, ΔAIC = −12.4), β = +0.010 for AMR clusters (SE = 0.0056, p = 0.090, ΔAIC = −0.9), and β = +0.003 for core fraction (SE = 0.0054, p = 0.523, ΔAIC = +1.6). [^microbeatlas_metal_ecology]

The raw OLS correlation between mean metal type diversity and Levins' B_std was r ≈ 0.21, while the PGLS coefficient represents additional covariation after removing shared ancestry. The result indicates that breadth across multiple metal types, rather than depth represented by many genes for a smaller number of metals, distinguishes broad-niche genera. [^microbeatlas_metal_ecology]

### Metal AMR traits have intermediate phylogenetic signal

Among 606 bacterial genera in GTDB r214, total AMR cluster count had Pagel's λ = 0.260 and p = 6.1×10⁻²⁸, core AMR fraction had λ = 0.441 and p = 1.8×10⁻⁸, and metal type diversity had λ = 0.335 and p = 1.1×10⁻²³. The ordering, core fraction λ > metal type diversity λ > cluster count λ, is consistent with a mixture of vertical inheritance and horizontal gene transfer, with accessory accumulation and metal-type expansion more labile than constitutive resistance. [^microbeatlas_metal_ecology]

Nitrification provided a phylogenetic positive control: its signal was λ = 0.939 in bacteria with p = 2.5×10⁻¹⁰² and λ = 1.000 in archaea with p = 2.5×10⁻⁵. This contrasts with the intermediate signal for metal AMR and supports the interpretation that deeply inherited metabolic traits and mobile resistance traits have different phylogenetic architectures. [^microbeatlas_metal_ecology]

Standalone Pagel's λ for bacterial B_std was 0.787, whereas the PGLS-estimated λ was 0.708, a discrepancy of Δλ = 0.079. The report interprets the lower residual λ as expected because metal type diversity itself has phylogenetic signal and removes some phylogenetically structured variance; residual λ = 0.708 remained strongly non-zero. [^microbeatlas_metal_ecology]

### Robustness and sensitivity analyses

The metal type association remained significant after adding pangenome coverage as a covariate: β = +0.0204, SE = 0.0057, p = 3.4×10⁻⁴ in the simple model and β = +0.0224, SE = 0.0067, p = 8.3×10⁻⁴ in the model containing all three AMR predictors. The coverage covariate had β = +0.0093, SE = 0.0051, p = 0.068 in the simple model and β = +0.0092, SE = 0.0051, p = 0.070 in the multi-predictor model. [^microbeatlas_metal_ecology]

In 200 rarefaction iterations representing each genus by 1 randomly sampled species, the median metal type coefficient was +0.0147, the IQR was +0.0126–+0.0166, the median p-value was 0.0054, 89.5% of iterations had p < 0.05, 57.5% were Bonferroni-significant at p < 0.0083, and the median λ was 0.704. The direction was consistent across all iterations, although the median coefficient was smaller than the full-data estimate of +0.0215. [^microbeatlas_metal_ecology]

The strict 5% within-environment prevalence analysis reduced the number of OTUs from 98,919 to 10,433, the number of genera with B_std estimates from 3,160 to 1,120, and the PGLS sample size from 606 to 379. The coefficient remained positive but was not significant: β = +0.0166, SE = 0.0099, p = 0.092, λ = 0.526, compared with β = +0.0215, SE = 0.0056, p = 1.5×10⁻⁴ and λ = 0.708 in the original analysis; the Pearson correlation between original and strict B_std was 0.680. [^microbeatlas_metal_ecology]

Controlling for genome size, the metal type coefficient was β = +0.0218, SE = 0.0061, p = 3.6×10⁻⁴, while log(genome size) had β = +0.0263, SE = 0.0069, p = 1.5×10⁻⁴. The baseline genome-size-only model had β = +0.029, p = 2.7×10⁻⁵, AIC = −630.3; the full model had AIC = −641.1, giving ΔAIC = 10.8 in favor of including metal type diversity. [^microbeatlas_metal_ecology]

In the three-covariate PGLS with metal type diversity, log(n_species), and log(genome size), using 527 genera with all covariates, metal types had β = +0.0218, SE = 0.0061, t = 3.60, p = 3.5×10⁻⁴; log(n_species) had β = +0.0052, SE = 0.0057, t = 0.90, p = 0.366; and log(genome size) had β = +0.0255, SE = 0.0069, t = 3.68, p = 2.6×10⁻⁴. The model had λ = 0.628, and the metal type effect had BH-FDR q = 0.003. [^microbeatlas_metal_ecology]

In the leave-one-metal-out analysis, all 7 exclusions retained a positive coefficient but none remained significant: excluding Hg gave β = +0.0082, p = 0.233; As β = +0.0039, p = 0.518; Cu β = +0.0102, p = 0.115; Zn β = +0.0095, p = 0.140; Cd β = +0.0084, p = 0.186; Cr β = +0.0088, p = 0.173; and Ni β = +0.0095, p = 0.140. The report treats this as consistent with a distributed signal, while noting that reducing the maximum diversity score from 7 to 6 also compresses predictor variance and reduces power. [^microbeatlas_metal_ecology]

Leave-one-environment-out analyses remained nominally significant for all 13 environment categories. The weakest result followed exclusion of aquatic environments, with β = +0.0085, SE = 0.0039, p = 0.031 and λ = 0.880; the strongest was after excluding forest, with β = +0.0142, SE = 0.0042, p = 0.0007 and λ = 0.874. The remaining coefficients ranged from β = +0.0105 to +0.0131, with p-values from 0.0025 to 0.0077, except for desert at β = +0.0120, p = 0.0040 and field at β = +0.0118, p = 0.0030. [^microbeatlas_metal_ecology]

Within-genus variation did not explain the association: adding the within-genus standard deviation of metal types produced β = +0.0189, SE = 0.0060, p = 0.0016 for mean metal types and β = +0.0074, SE = 0.0055, p = 0.181 for the standard deviation. Adding log(n_species) produced β = +0.0195, SE = 0.0057, p = 6.4×10⁻⁴ for metal types and β = +0.0127, SE = 0.0053, p = 0.016 for log(n_species). [^microbeatlas_metal_ecology]

Filtering out OTUs with mean relative abundance below 0.01% removed 66% of OTUs, leaving 33,676 OTUs; 23,759 bacterial, non-organellar OTUs covered 576 of the 606 PGLS genera. Pagel's λ for B_std changed from 0.763 to 0.750 within the same 576-genus subset, a −1.7% change, and remained highly significant with p = 2.8×10⁻⁴⁰. [^microbeatlas_metal_ecology]

### Archaeal analysis and multiple testing

The archaeal analysis included 48 genera and was severely underpowered: metal type diversity had β = +0.0145, SE = 0.0198, t = 0.73, p = 0.467, and λ = 0.567. Formal power was 11% at α = 0.05, and the report estimates that 80% power would require n ≥ 702 at α = 0.05 or n ≥ 1,084 at Bonferroni α = 0.0083; the non-significant result is therefore not interpreted as evidence against the association. [^microbeatlas_metal_ecology]

The confirmatory analysis comprised 6 simple PGLS models with Bonferroni threshold p < 0.0083. Across approximately 47 tests, the primary result p = 1.5×10⁻⁴ also survived the more conservative full-family threshold 0.05/47 ≈ 0.0011. Benjamini-Hochberg false discovery rate correction identified 23 of 47 tests at q < 0.05; the primary PGLS had q = 0.0028, the multi-predictor model q = 0.0037, the genome-size and three-covariate results q = 0.0028, and the archaeal result q = 0.55. [^microbeatlas_metal_ecology]

## Independent Environmental Validation

Track A analyzed 1,624 groundwater samples and 767 genera with groundwater detections and AMR data. Metal type diversity correlated positively with groundwater prevalence, with Spearman ρ = +0.112 and p = 0.0019; top-Q4 versus bottom-Q1 metal-diversity genera also differed in groundwater prevalence with Mann–Whitney p = 0.007. Median prevalence was 0.81% for top-Q4 genera and 0.62% for bottom-Q1 genera, a ratio of 1.31×. [^microbeatlas_metal_ecology]

The groundwater-specific fold-enrichment analysis was null: Spearman ρ = +0.042 and p = 0.242, and the top-Q4 versus bottom-Q1 fold-enrichment comparison had p = 0.181. The report therefore treats Track A as supporting a prevalence association but not demonstrating groundwater-specific enrichment or uniquely confirming a metal-contamination mechanism. [^microbeatlas_metal_ecology]

Track B processed all 133 PRJNA1084851 samples into a 133-sample × 24,295-OTU table, with 14,021 OTUs assigned genus-level taxonomy and 1,637 OTUs representing 16.8% of reads joinable to genus metal-diversity data. Community-weighted mean metal-type diversity ranged from 1.01 to 1.83, with mean 1.28 ± 0.19. [^microbeatlas_metal_ecology]

Community-weighted mean metal-type diversity differed across 8 wells with Kruskal–Wallis H = 29.10 and p = 0.0001, increased with time point with Spearman ρ = +0.383 and p < 0.0001, and increased within FW216 with ρ = +0.576 and p = 0.0001 across 40 samples. EVO09 versus EVO17 differed with Mann–Whitney p = 0.0012. FW215 and FW216 had the highest median values, 1.37 and 1.36, respectively, compared with 1.23 for GP01, 1.22 for GP03, 1.14 for MLSB3, and 1.09, 1.08, and 1.08 for MLSA3, FW202, and MLSG4. [^microbeatlas_metal_ecology]

The same Track B dataset showed that Sulfurimonas relative abundance decreased with time, with Spearman ρ = −0.323 and p = 0.0002. The report interprets this as a counterexample showing that ecological dominance can be driven by electron-acceptor availability rather than metal resistance. [^microbeatlas_metal_ecology]

## Experimental Validation Framework

The study identified 435 candidate OTUs: 215 in the top 10% for both Levins' B_std and mean metal-type diversity, using B_std ≥ 0.718 and n_metal_types ≥ 2.0, plus 220 nitrifier positive controls. Eight priority OTUs were selected for microcosm experiments, with Levins' B values from 0.770 to 0.999 and metal-type values from 2.1 to 3.7; the recommended stresses included Ag, Te, Cu, Cd, As, Hg, and Cu or Hg co-stress. [^microbeatlas_metal_ecology]

The proposed experiment uses 4–6 metal-stress treatments, 5 replicates, and 7- and 14-day time points, with relative-abundance fold-change versus metal-free controls as the primary endpoint. The recommended pre-treatment sequencing design uses 5 replicates and ≥ 50,000 reads per sample to confirm detectable OTUs at ≥ 0.1% relative abundance; at 1% initial abundance, the report estimates coefficient of variation ≈ 10% and power >99% for detecting a 2-fold increase with 3 replicates at 10,000 reads. [^microbeatlas_metal_ecology]

## Caveats and Limitations

MicrobeAtlas niche breadth is a sequencing-effort proxy rather than confirmed ecological range. Detection across 13 environment categories is affected by sampling intensity, primer bias, geographic and temporal non-uniformity, and missing environments; Levins' B_std corrects for unequal environment sizes but not for detection-probability differences. Genus aggregation also means that a broad genus score can reflect different species occupying different habitats rather than one organism being a generalist. [^microbeatlas_metal_ecology]

The strict 5% prevalence analysis preserved the direction of the association but reduced the PGLS sample size by 37%, from 606 to 379, and produced p = 0.092. Primer bias, missing environments, and the ecological meaning of sparse detections remain unresolved without a multi-primer, multi-region survey design. [^microbeatlas_metal_ecology]

The 48-genus archaeal analysis is biased toward cultured methanogens, halophiles, and thermoacidophiles and misses environmentally dominant groups including Thaumarchaeota and Woesearchaeota. The report states that ≥200 archaeal genera would be needed for improved power in the planned expansion, while its formal power analysis estimates n ≥ 702 for 80% power at α = 0.05 under the observed effect and error assumptions. [^microbeatlas_metal_ecology]

Pangenome coverage is uneven: the correlation between sequenced genomes per genus and inferred metal type diversity was r = 0.35 with p = 2.6×10⁻¹⁹, and single-genome genera had lower metal type counts than multi-genome genera with Mann–Whitney p = 5.1×10⁻¹⁰. Coverage and rarefaction analyses substantially addressed this concern, but a formal rarefaction curve across multiple species-per-genus thresholds remains outstanding. [^microbeatlas_metal_ecology]

Environment categories are heterogeneous, especially aquatic, which combines marine, freshwater, estuarine, hydrothermal-vent, and pond environments. Aquatic represented 40,353 OTUs, or 40.8% of the dataset; excluding it reduced β from +0.021 to +0.0085 but retained nominal significance at p = 0.031. Finer subdivision into marine, freshwater, and saline categories requires re-analysis of MicrobeAtlas metadata. [^microbeatlas_metal_ecology]

The Gaussian PGLS treats metal type diversity, an integer count from 1–7, as a continuous z-scored predictor; the report considers this standard when the count is an independent variable but notes that residual normality should be inspected. Pagel's λ for the count trait also assumes Brownian-motion evolution, and discrete-state, threshold, Poisson, or negative-binomial phylogenetic models remain possible alternatives. [^microbeatlas_metal_ecology]

The GTDB r214 genus-representative tree was used for all phylogenetic analyses, but sensitivity to NCBI, SILVA-based 16S, or other GTDB trees was not tested. Genus-level pruning discards within-genus phylogenetic structure, although the within-genus metal-type standard-deviation test was non-significant at p = 0.18. [^microbeatlas_metal_ecology]

AMRFinderPlus annotations use HMM-based detection against the NCBI Bacterial AMR Reference Gene Database, and the report notes possible cross-reactive false positives, uncertainty in the “other” metal category, and the absence of manual validation. The recommended follow-up is manual BLAST verification of 100 randomly sampled annotated gene clusters. [^microbeatlas_metal_ecology]

Track B community-weighted means cover only 16.8% of reads because the remaining approximately 83% could not be joined to genus-level GTDB AMR annotations. If uncovered genera have systematically different resistance profiles, the community-weighted means could be biased upward; correlation between per-sample covered-read fraction and community-weighted mean is required as a diagnostic. [^microbeatlas_metal_ecology]

The study's robustness and sensitivity analyses were post-hoc exploratory analyses rather than confirmatory tests, and the analysis plan was not preregistered. The report also identifies unresolved needs for HGT-burden predictors, site-level contamination metadata, co-resistance clustering, finer environment classification, alternative phylogenetic mixed models, AMRFinderPlus validation, and a public Zenodo archive with a citable DOI. [^microbeatlas_metal_ecology]

## Slots Into

- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — The PGLS result distinguishes breadth across metal types from total AMR gene burden and supports a cross-metal resistance ecology interpretation. [^microbeatlas_metal_ecology]
- [environmental-resistome](../concepts/environmental-resistome.md) — The study integrates AMRFinderPlus metal-resistance annotations with global environmental occurrence data and independent groundwater validation. [^microbeatlas_metal_ecology]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — MicrobeAtlas environment categories, groundwater prevalence, and ENIGMA well-level gradients connect resistance repertoires to environmental distributions. [^microbeatlas_metal_ecology]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — Intermediate phylogenetic signal for metal AMR, contrasted with strongly conserved niche and nitrification traits, informs the balance of vertical inheritance and horizontal acquisition. [^microbeatlas_metal_ecology]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — The association between genus-level metal-resistance diversity and inferred niche breadth provides a testable link between environmental range and gene-content variation, while retaining explicit causal and aggregation caveats. [^microbeatlas_metal_ecology]

[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../sources/microbeatlas_metal_ecology__REPORT.md)
