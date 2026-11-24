---
type: "Concept"
description: "How coverage-aware, fraction-aware, within-fraction and high-coverage sensitivity models change the apparent contamination–defense association and its multiple-testing standing."
sources: ["summaries/discoveries.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/pitfalls.md"]
---
# Robustness of exploratory associations to coverage, fraction and site covariate specification

This page covers how coverage-aware, fraction-aware, within-fraction and high-coverage sensitivity models change the apparent contamination–defense association in [[entities/enigma]] communities. Primary tests were null, and coverage-aware models gave nominally significant defense associations. [src: discoveries] Only one exploratory model kept q=0.046 after global correction. [src: discoveries] The evidence is exploratory and comes from one project. See also [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]].

## Literature Context

None of the candidate papers tests how mapped-coverage, community-fraction or site covariates change a contamination–defense association. They do give biological context for why a link between contamination and functional potential might be expected, and for why it may be weak or inconsistent.

Several candidates report metagenomic functional responses to metal stress. In a groundwater study of 66 samples near Baiyangdian Lake, 160 metal(loid) resistance genes showed significant seasonal variation. Dissolved metal(loid)s, particularly Ba, promoted their proliferation even at relatively low concentrations, and 27.4% of MRG-carrying metagenome-assembled genomes (MAGs, genomes reconstructed from metagenomes) also carried antibiotic resistance genes [PMID 39271075](https://pubmed.ncbi.nlm.nih.gov/39271075/). Vanadium-impacted systems show a similar pattern. Vanadium was among the factors shaping community structure in a polluted stream, and metagenomes there highlighted electron-transfer and resistance genes [PMID 35810633](https://pubmed.ncbi.nlm.nih.gov/35810633/). In a vanadium-titanium tailings chronosequence, vanadium-associated genes such as napA, narG and nirS increased 1.5- to 2-fold over time [PMID 42102564](https://pubmed.ncbi.nlm.nih.gov/42102564/). In a soil–plant system, vanadium and other environmental variables significantly influenced community composition [PMID 39486340](https://pubmed.ncbi.nlm.nih.gov/39486340/). These studies are consistent with the hub's positive effect estimates for defense in contaminated sites. They are mostly designed around a single metal and a single system, and their abstracts report associations without the global multiple-testing control the hub applies.

Other candidates suggest that responses to contamination are not uniform. At a molybdenum plume, community diversity was not reduced, unlike trends at other metal-impacted industrial sites. Burkholderiales were more abundant where Mo exceeded 0.3 mg/L, and sulfate reducers were less abundant but not absent [PMID 41347789](https://pubmed.ncbi.nlm.nih.gov/41347789/). Arsenic studies find that mobilization capacity is spread across broad phylogenetic lineages, with 194 MAGs analyzed in Ohio groundwater [PMID 31490939](https://pubmed.ncbi.nlm.nih.gov/31490939/). Arsenic cycling also varies with geochemical zonation and depth [PMID 41819657](https://pubmed.ncbi.nlm.nih.gov/41819657/), [PMID 29184025](https://pubmed.ncbi.nlm.nih.gov/29184025/). This heterogeneity supports the hub's caution that site structure, such as depth and location, matters. It also fits the report's statement that the signal is not broad across outcomes. Pilot or laboratory papers on Cr(VI) reduction under different initial pHs and on lead immobilization by Penicillium oxalicum are about remediation mechanisms. They add little to this question [PMID 32135365](https://pubmed.ncbi.nlm.nih.gov/32135365/), [PMID 36584858](https://pubmed.ncbi.nlm.nih.gov/36584858/).

Against this background, the corpus's findings are consistent with the literature in direction but not in strength. The primary and confirmatory defense tests were null across the four contamination indices. Only the relaxed coverage-adjusted model kept q=0.046 after global correction, and the within-fraction tests were null. The candidates do not contradict this attenuated picture. They also cannot confirm it, because none examines mapped-abundance fraction, 0.2 micron versus 10 micron fractions, or high-coverage subsets. The sensitivity analysis of coverage and fraction specification is therefore novel relative to these papers. It remains a single-project, exploratory result.

The hub's proposed mixed-effects site models would address a gap that the heterogeneity above makes plausible.

## Primary and confirmatory results are null

In the project with 108 overlap samples, primary univariate associations were non-significant for defense, stress, metabolism and mobilome outcomes in both mapping modes. [src: discoveries] After global Benjamini-Hochberg false discovery rate (BH-FDR) correction across all reported p-values, confirmatory genus-level defense Spearman tests stayed null (p=0.546/0.483; q=0.862/0.849). [src: discoveries] Re-testing the defense endpoint under four contamination indices (all-metals composite, uranium-only, top-3 variance metals, PCA-PC1) gave no significant result (all q=0.546 across 8 confirmatory-variant tests). [src: discoveries] The report concludes the null is not an artifact of one index formulation. [src: discoveries]

## Coverage-aware models produce a signal

Adding mapped-coverage terms made the contamination–defense association nominally significant, with coverage-adjusted ordinary least squares (OLS) contamination p = 3.98e-4 relaxed and 3.54e-3 strict. [src: discoveries] The OLS model includes contamination, depth, latitude, longitude and mapped_abundance_fraction. [src: enigma_contamination_functional_potential] Reported effects:

- relaxed_all_clades coverage-adjusted OLS: beta = 0.000751, 95% bootstrap confidence interval (CI) [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462. [src: enigma_contamination_functional_potential]
- strict_single_clade coverage-adjusted OLS: beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, FDR q = 0.130. [src: enigma_contamination_functional_potential]

The report finds the strongest positive exploratory defense associations in the coverage-aware adjustments. [src: enigma_contamination_functional_potential]

## Fraction-aware and high-coverage models

The fraction-aware model includes contamination, mapped_abundance_fraction and categorical community_fraction_type. [src: enigma_contamination_functional_potential] It was added to address possible confounding from collapsing community fractions. [src: enigma_contamination_functional_potential] It uses n = 212 sample-fraction rows, 106 for 0.2_micron_filter and 106 for 10_micron_filter. [src: enigma_contamination_functional_potential]

- relaxed_all_clades: beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, FDR q = 0.0838. [src: enigma_contamination_functional_potential]
- strict_single_clade: beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, FDR q = 0.130. [src: enigma_contamination_functional_potential]

In the high-coverage subset (mapped_abundance_fraction >= 0.25), site_defense_score Spearman p = 0.0207 (relaxed) and 0.00980 (strict). [src: enigma_contamination_functional_potential, discoveries] After global FDR these were non-significant, with q = 0.301 (relaxed) and 0.189 (strict). [src: enigma_contamination_functional_potential]

Sample sizes by mapping mode:

| Mode | Base Spearman | Adj+Cov | Adj+Fraction | High-coverage |
|---|---|---|---|---|
| relaxed_all_clades | 108 | 108 | 212 (sample-fraction rows) | 68 [src: enigma_contamination_functional_potential] |
| strict_single_clade | 108 | 108 | 212 (sample-fraction rows) | 68 [src: enigma_contamination_functional_potential] |
| species_proxy_unique_genus | 108 | 108 | 212 (sample-fraction rows) | 1 [src: enigma_contamination_functional_potential] |

The species-proxy high-coverage tests are underpowered (n=1). Coverage-aware models increase effective rows at fraction level. [src: enigma_contamination_functional_potential]

## Within-fraction tests are null

Within-fraction defense Spearman tests were non-significant. Relaxed mode gave p = 0.767 (0.2 micron) and p = 0.898 (10 micron). [src: enigma_contamination_functional_potential] Strict mode gave p = 0.780 (0.2 micron) and p = 0.793 (10 micron). [src: enigma_contamination_functional_potential] The report concludes that a strong monotonic defense signal is not robustly reproducible inside individual fraction strata. [src: enigma_contamination_functional_potential]

## Standing after multiple-testing control

Only the relaxed coverage-adjusted defense model kept q=0.046 after global correction. [src: discoveries] Strict and other sensitivity signals attenuated above q<0.1. [src: discoveries] Exploratory associations keep positive effect estimates but are attenuated under global control. [src: enigma_contamination_functional_potential] The strongest signal depends on mapping coverage and model specification and is not broad across outcomes. [src: discoveries, enigma_contamination_functional_potential] The report advises prioritizing null confirmatory evidence and framing positive results as exploratory. [src: discoveries] Diagnostics in model_results.tsv carry confirmatory/exploratory labels and global BH-FDR q-values across all reported p-values. [src: enigma_contamination_functional_potential]

A correction pitfall applies here. Correction limited to columns ending in `_p` misses p-values named like `adj_cov_p_contamination` and `adj_frac_p_contamination`. [src: pitfalls] The recommended fix is substring detection that excludes derived q-value columns, or an explicit allowlist, before BH-FDR. [src: pitfalls] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Limits on site covariates

Site structure is represented only by coarse location_prefix effects, not full hierarchical or random-effects modeling. [src: enigma_contamination_functional_potential] The report proposes adjusted models with explicit depth, location cluster and sampling date covariates plus compositional controls. [src: enigma_contamination_functional_potential] It also proposes mixed-effects or hierarchical site models with well/location-level random effects. [src: enigma_contamination_functional_potential]

## Open Directions

- Fit mixed-effects models with well/location random effects on the 212 sample-fraction rows. This tests whether the relaxed coverage-adjusted defense signal (q=0.046) survives richer site structure.
- Add sampling date and location cluster covariates with compositional controls. This separates contamination from spatial and temporal confounding.
- Re-run the global BH-FDR with an explicit p-column allowlist. This confirms that no adjusted p-values were missed.
- Repeat the high-coverage analysis at several coverage thresholds. This checks whether the n=68 subset result depends on the 0.25 cutoff.
