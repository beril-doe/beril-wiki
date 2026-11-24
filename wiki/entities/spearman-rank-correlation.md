---
type: "Method"
description: "Rank-based correlation (including partial correlation controlling covariates and BH-FDR-corrected testing) used to relate continuous variables; stops at Pearson-based and distance-matrix correlation methods."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/euk_in_prok_correlates__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md"]
aliases: ["Spearman", "Spearman BH-FDR", "Spearman correlation", "Spearman correlation with Benjamini–Hochberg FDR", "Spearman partial correlation", "Spearman ρ"]
---
# Spearman rank correlation

This page is about Spearman rank correlation. The corpus uses it in plain form, as a partial correlation that controls covariates, and with Benjamini-Hochberg false discovery rate (BH-FDR) correction across many tests. [src: alphafold_msa_annotation, cazyme_pangenome_ecology, nmdc_community_metabolic_ecology] The examples come from six projects. They show large correlations next to modest or null ones, and several carry stated confounding caveats. [src: alphafold_msa_annotation, cazyme_pangenome_ecology, euk_in_prok_correlates]

## Key facts

- Plain Spearman ρ is used for relationships between gene-annotation measures, species-level traits, community pathway completeness and metagenome fractions in these reports. [src: alphafold_msa_annotation, cazyme_pangenome_ecology, euk_in_prok_correlates, nmdc_community_metabolic_ecology, prophage_amr_comobilization]
- Partial Spearman correlation controls covariates such as genome count and genome size. [src: cazyme_pangenome_ecology, prophage_amr_comobilization]
- BH-FDR correction is applied when many pathways or phyla are tested at once. [src: cazyme_pangenome_ecology, nmdc_community_metabolic_ecology]

## Strong correlations on large datasets

Across 38,051,842 gene cluster–UniProt pairs, multiple sequence alignment (MSA) depth and domain hit count correlate strongly (Spearman ρ = 0.756). [src: alphafold_msa_annotation] A second statement gives the same result as ρ = 0.7563. [src: alphafold_msa_annotation] The value was computed on the full dataset without subgroup stratification. [src: alphafold_msa_annotation] See [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]] and [[summaries/alphafold_msa_annotation__REPORT]].

Across n=4,770 species, prophage marker density correlates positively with antimicrobial resistance (AMR) repertoire breadth (Spearman rho=0.572, p<10^-300). [src: prophage_amr_comobilization] The association persists after controlling for genome count (partial Spearman rho=0.464, p=1.0×10^-253). [src: prophage_amr_comobilization] See [[concepts/prophage-density-and-amr-repertoire-breadth-across-species]].

## Confounding and partial correlation: CAZymes and pangenome openness

Partial correlation shrinks an apparent association once sampling effort is controlled. Across n = 9,347 bacterial species with ≥3 genomes, carbohydrate-active enzyme (CAZyme) density had a modest positive correlation with pangenome cloud fraction (ρ = 0.153, p < 10^-50). [src: cazyme_pangenome_ecology] Genome count severely confounded cloud fraction (ρ = 0.913), so much apparent openness reflects sampling effort rather than biology. [src: cazyme_pangenome_ecology] After controlling for genome size and genome count, the correlation dropped to ρ = 0.101. [src: cazyme_pangenome_ecology] See [[concepts/pangenome-openness-and-its-correlates]], [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]] and [[summaries/cazyme_pangenome_ecology__REPORT]].

### Within-phylum tests (BH-adjusted)

The within-phylum correlations between total CAZymes and cloud fraction were significant in three phyla and not significant in the other seven. [src: cazyme_pangenome_ecology]

| Phylum | Species | ρ | BH-adjusted p | Significant |
|---|---|---|---|---|
| Bacillota_A | 939 | 0.288 | 2.2 × 10^-18 | Yes [src: cazyme_pangenome_ecology] |
| Bacteroidota | 1,618 | 0.147 | 1.3 × 10^-8 | Yes [src: cazyme_pangenome_ecology] |
| Firmicutes_A | 1,625 | 0.105 | 7.8 × 10^-5 | Yes [src: cazyme_pangenome_ecology] |
| Pseudomonadota | 1,689 | −0.013 | 0.74 | No [src: cazyme_pangenome_ecology] |
| Actinomycetota | 385 | −0.094 | 0.13 | No [src: cazyme_pangenome_ecology] |
| Firmicutes | 364 | 0.065 | 0.30 | No [src: cazyme_pangenome_ecology] |
| Actinobacteriota | 335 | 0.071 | 0.30 | No [src: cazyme_pangenome_ecology] |
| Thermoplasmatota | 289 | 0.112 | 0.13 | No [src: cazyme_pangenome_ecology] |
| Bacillota | 238 | 0.022 | 0.74 | No [src: cazyme_pangenome_ecology] |
| Verrucomicrobiota | 215 | −0.024 | 0.74 | No [src: cazyme_pangenome_ecology] |

## Amino acid pathways in NMDC (BH-FDR)

Across 13 testable amino acid biosynthesis pathways, 11 of 13 (85%) had negative Spearman correlations between community pathway completeness and ambient amino acid metabolite intensity. This is the direction predicted by the Black Queen Hypothesis. [src: nmdc_community_metabolic_ecology] The results table holds 15 rows, with 13 testable and 2 skipped pathways (gln n=4, pro n=9). [src: nmdc_community_metabolic_ecology] After BH correction only two pathways were significant: leucine (r = −0.390, p = 0.002, q = 0.022, n = 62) and arginine (r = −0.297, p = 0.007, q = 0.049, n = 80). [src: nmdc_community_metabolic_ecology] See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]] and [[summaries/nmdc_community_metabolic_ecology__REPORT]].

Two others had nominal p below 0.05 but did not survive correction: methionine (r = −0.496, p = 0.036, q = 0.117, n = 18) [src: nmdc_community_metabolic_ecology] and tyrosine, which was positive (r = +0.419, p = 0.033, q = 0.117, n = 26). [src: nmdc_community_metabolic_ecology] The remaining pathways were not significant after correction:

- Tryptophan: r = −0.294, p = 0.052, q = 0.136, n = 44. [src: nmdc_community_metabolic_ecology]
- Threonine: r = −0.271, p = 0.211, q = 0.393, n = 23. [src: nmdc_community_metabolic_ecology]
- Phenylalanine: r = −0.159, p = 0.140, q = 0.303, n = 88. [src: nmdc_community_metabolic_ecology]
- Valine: r = −0.151, p = 0.275, q = 0.446, n = 54. [src: nmdc_community_metabolic_ecology]
- Serine: r = −0.061, p = 0.645, q = 0.762, n = 59. [src: nmdc_community_metabolic_ecology]
- Asparagine: r = −0.061, p = 0.610, q = 0.762, n = 73. [src: nmdc_community_metabolic_ecology]
- Isoleucine: r = −0.057, p = 0.823, q = 0.823, n = 18. [src: nmdc_community_metabolic_ecology]
- Chorismate: r = −0.038, p = 0.765, q = 0.823, n = 65. [src: nmdc_community_metabolic_ecology]
- Glycine: r = +0.081, p = 0.389, q = 0.562, n = 114. [src: nmdc_community_metabolic_ecology]

## ENIGMA contamination tests

The predeclared Spearman tests of defense score against contamination were non-significant. [src: enigma_contamination_functional_potential] High-coverage subset tests gave p-values below 0.05, and one of them is described as exploratory. [src: enigma_contamination_functional_potential] See [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]], [[concepts/robustness-of-exploratory-associations-to-coverage-fraction-and-site-covariate-specification]] and [[summaries/enigma_contamination_functional_potential__REPORT]].

- In the high-coverage subset (mapped_abundance_fraction >= 0.25), site_defense_score had Spearman p = 0.0207 (relaxed) and 0.00980 (strict). [src: enigma_contamination_functional_potential]
- In the exploratory strict_single_clade high-coverage subset, site_stress_score gave rho = 0.2489, p = 0.0407. [src: enigma_contamination_functional_potential]
- The predeclared relaxed_all_clades test was non-significant: rho = 0.0587, 95% bootstrap confidence interval (CI) [-0.128, 0.250], p = 0.546, FDR q = 0.862. [src: enigma_contamination_functional_potential]
- The predeclared strict_single_clade test was non-significant: rho = 0.0682, 95% bootstrap CI [-0.111, 0.253], p = 0.483, FDR q = 0.849. [src: enigma_contamination_functional_potential]
- Within-fraction defense tests were non-significant for relaxed_all_clades (p = 0.767 for 0.2 micron, p = 0.898 for 10 micron). [src: enigma_contamination_functional_potential]
- Within-fraction defense tests were also non-significant for strict_single_clade (p = 0.780 for 0.2 micron, p = 0.793 for 10 micron). [src: enigma_contamination_functional_potential]
- The species-proxy site_defense_score trend was positive but not significant (rho = 0.169, p = 0.081). [src: enigma_contamination_functional_potential]

## Eukaryotic fraction and depth in NMDC

Across NMDC studies, measured depth correlates negatively with eukaryotic fraction (ρ = −0.29, p=5.2×10⁻⁷, n=292 runs with measured depth), so shallower samples carry more eukaryotic DNA. [src: euk_in_prok_correlates] The report treats this as suggestive only. It is not batch-controlled, measured-depth runs come from a handful of non-soil studies, and the dominant NEON soil study records no depth. [src: euk_in_prok_correlates] See [[concepts/sources-and-prevalence-of-eukaryotic-contamination-in-prokaryote-targeted-metagenomes]] and [[summaries/euk_in_prok_correlates__REPORT]].
