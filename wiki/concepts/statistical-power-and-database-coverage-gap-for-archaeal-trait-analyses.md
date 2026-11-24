---
type: "Concept"
description: "What can and cannot be concluded about archaea from phylogenetic comparative analyses given few archaeal genera with annotation data; covers power analysis and sampling bias toward cultured lineages."
sources: ["summaries/gene_function_ecological_agora__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Statistical power and database coverage gap for archaeal trait analyses

Archaeal phylogenetic comparative analyses currently rest on very few genera with annotation data. In the one project that tested this directly, the archaeal PGLS (phylogenetic generalized least squares) used only 48 genera and was too underpowered to support or refute the bacterial finding. [src: microbeatlas_metal_ecology] Evidence comes mainly from [[summaries/microbeatlas_metal_ecology__REPORT]], with a related scope limit noted in [[summaries/gene_function_ecological_agora__REPORT]]. [src: gene_function_ecological_agora, microbeatlas_metal_ecology] The power figures are an analytical projection from a single observed effect, not a measurement. [src: microbeatlas_metal_ecology]

## Coverage of archaea in the data

Only 48 archaeal genera had both MicrobeAtlas representation (≥ 3 OTUs, operational taxonomic units) and AMR (antimicrobial resistance) data in [[entities/kbase-ke-pangenome]]. [src: microbeatlas_metal_ecology] These genera are biased toward cultured methanogens, halophiles and thermoacidophiles. They miss the environmentally dominant MicrobeAtlas archaea, including Thaumarchaeota and Woesearchaeota. [src: microbeatlas_metal_ecology]

A separate project reports the same kind of gap. CPR (candidate phyla radiation) and DPANN under-representation is an acknowledged substrate constraint of its Phase 1A, not a failure of that phase. [src: gene_function_ecological_agora] That report says its effective-N reporting flags the gap per phase. [src: gene_function_ecological_agora] See also [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]].

## What the archaeal data still show

Phylogenetic signal is detectable in the traits that have 132 archaeal genera, a larger set than the 48-genus AMR sample. Archaeal niche breadth shows significant signal for B_std (λ = 0.197, p = 1.1×10⁻⁵) and for number of environments (λ = 0.898, p = 4.6×10⁻¹⁴), across 132 genera. [src: microbeatlas_metal_ecology] Nitrification has λ = 1.000 (p = 2.5×10⁻⁵¹) across 132 genera. [src: microbeatlas_metal_ecology] The archaeal B_std λ is notably lower than the bacterial value of 0.787. The report considers this consistent with phylogenetically sparse, ecologically distinct archaeal genera captured by 16S amplicon surveys. [src: microbeatlas_metal_ecology] AMR cluster count across 48 genera has λ ≈ 0 with p = 1.0. [src: microbeatlas_metal_ecology] See [[concepts/phylogenetic-signal-of-gene-content-and-traits]].

## Power of the archaeal PGLS

The archaeal PGLS on 48 genera with AMR data gave a positive but non-significant metal-types effect: β = +0.0145, SE = 0.0198, t = 0.73, p = 0.467, λ = 0.567. [src: microbeatlas_metal_ecology] The BH-FDR (Benjamini-Hochberg false discovery rate) q was 0.548, so it is not significant after adjustment. [src: microbeatlas_metal_ecology] The AMR-cluster coefficient (β = +0.0146, p = 0.488) and the core-fraction coefficient (β = +0.0002, p = 0.991) were also non-significant. [src: microbeatlas_metal_ecology] The metal-types direction matches the bacterial coefficient (+0.0215), but the SE is nearly as large as the estimate, which indicates severe underpowering. [src: microbeatlas_metal_ecology]

Power at the observed effect is 11% at α = 0.05. The report therefore says the result is not evidence against the association in archaea. [src: microbeatlas_metal_ecology] It includes the archaeal analysis only to quantify the statistical gap, and it suggests reading that section as a power-analysis appendix, not as a replication attempt. [src: microbeatlas_metal_ecology]

The projection uses a non-central t-distribution, with SE scaled as SE_obs × √(n_obs/n), β_true = +0.0145 and λ fixed at 0.567. [src: microbeatlas_metal_ecology] Rows below give expected SE, expected t, power at α = 0.05, and power at Bonferroni α = 0.0083.

- n = 48 (current): 0.0198, 0.73, 11%, 3%. [src: microbeatlas_metal_ecology]
- n = 100: 0.0137, 1.06, 18%, 6%. [src: microbeatlas_metal_ecology]
- n = 200: 0.0097, 1.50, 32%, 12%. [src: microbeatlas_metal_ecology]
- n = 300: 0.0079, 1.83, 45%, 21%. [src: microbeatlas_metal_ecology]
- n = 400: 0.0069, 2.12, 56%, 30%. [src: microbeatlas_metal_ecology]
- n = 600: 0.0056, 2.59, 74%, 48%. [src: microbeatlas_metal_ecology]
- n = 800: 0.0048, 3.00, 85%, 64%. [src: microbeatlas_metal_ecology]
- n = 1,000: 0.0043, 3.35, 92%, 76%. [src: microbeatlas_metal_ecology]

Reaching 80% power requires n ≥ 702 at α = 0.05, or n ≥ 1,084 with Bonferroni correction. [src: microbeatlas_metal_ecology] The report also states that ≥200 archaeal genera with AMR data are needed for adequate power, which requires expanded archaeal pangenome sequencing and annotation. [src: microbeatlas_metal_ecology] Its own proposal is to add environmental MAGs (metagenome-assembled genomes), particularly Thaumarchaeota, and to repeat the PGLS once ≥ 100 archaeal genera have AMR data. [src: microbeatlas_metal_ecology]

## Tensions

- The report states that ≥200 genera are needed for adequate power. [src: microbeatlas_metal_ecology] Its own table gives 32% power at n = 200 and puts 80% power at n ≥ 702. [src: microbeatlas_metal_ecology] The two figures are not reconciled in the report.

## Open Directions

- Add environmental archaeal MAGs, especially Thaumarchaeota and Woesearchaeota, to the pangenome. Then re-run the PGLS to test whether the cultured-lineage bias changes the estimate.
- Re-run the power analysis after each coverage increase. Use the updated SE and λ, not the single β of +0.0145, so the required n is not tied to one noisy effect size.
- Report effective N per clade for archaea, as the D3 reporting does for CPR and DPANN, so each analysis states what it can conclude.
- Run phylogenetic-signal analyses on traits that already have more archaeal data, such as niche breadth with 132 genera. This gives interim results while AMR coverage grows.
