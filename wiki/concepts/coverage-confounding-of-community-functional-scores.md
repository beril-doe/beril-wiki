---
type: "Concept"
description: "Mapped coverage can confound community-level functional associations."
sources: ["summaries/enigma_contamination_functional_potential__REPORT.md"]
---
# Mapped Coverage Constrains Community Functional Associations

Mapped coverage is the fraction of community abundance that can be linked to the functional-feature construction being tested. In community-level analyses, an apparent association between environment and inferred function can therefore reflect differences in how much of each community is represented, rather than a biological shift in the function itself. [src: enigma_contamination_functional_potential]

## Core Interpretation

The ENIGMA analysis supports the interpretation that mapped coverage constrains contamination–function inference: broad genus-level functional associations were null in predeclared tests, whereas positive defense associations appeared in exploratory models that adjusted for mapped abundance fraction. [src: enigma_contamination_functional_potential]

This pattern suggests the hypothesis that coverage is not merely a reporting diagnostic but a potential confounder of community functional scores. [src: enigma_contamination_functional_potential]

The result refines [[concepts/environmental-resistome]] by showing that a contamination-linked defense signal should not be treated as robust unless it persists across coverage adjustment, taxonomic mappings, fraction strata, and multiple-testing correction. [src: enigma_contamination_functional_potential]

## Evidence from the ENIGMA Analysis

The quality-controlled overlap contained 108 samples, a geochemistry matrix with shape `(108, 49)`, 41,711 community taxon rows, 212 distinct communities, and 1,392 distinct genera. [src: enigma_contamination_functional_potential]

The taxonomy bridge mapped 530 genera, left 862 genera unmapped, and produced 530 strict clades, 7,380 relaxed clades, and 150 species-proxy clades restricted to genera mapping to exactly one clade. [src: enigma_contamination_functional_potential]

Strict and relaxed mapping modes had a mean mapped abundance fraction of 0.343, whereas the species-proxy mode had a mean mapped abundance fraction of 0.031. [src: enigma_contamination_functional_potential]

The species-proxy mode retained 150 unique-clade genera compared with 530 mapped genera overall, and 380 mapped genera were ambiguous multi-clade genera. [src: enigma_contamination_functional_potential]

The bridge generated 8,242 genus-to-clade rows, with a maximum of 433 clades per genus; the most ambiguous genera were `pseudomonas` with 433 clades, `streptomyces` with 378, `prevotella` with 358, `streptococcus` with 214, and `mycobacterium` with 186. [src: enigma_contamination_functional_potential]

These diagnostics support [[concepts/pangenome-integration]] by showing that mapping choice changes both represented abundance and the ambiguity of the functional bridge. [src: enigma_contamination_functional_potential]

## Null Confirmatory Association

Predeclared Spearman tests of `site_defense_score` against contamination were non-significant in both genus-level modes. [src: enigma_contamination_functional_potential]

For `relaxed_all_clades`, rho = 0.0587, the 95% bootstrap confidence interval was [-0.128, 0.250], Spearman p = 0.546, and false-discovery-rate q = 0.862. [src: enigma_contamination_functional_potential]

For `strict_single_clade`, rho = 0.0682, the 95% bootstrap confidence interval was [-0.111, 0.253], Spearman p = 0.483, and false-discovery-rate q = 0.849. [src: enigma_contamination_functional_potential]

The confirmatory null was unchanged across four contamination-index definitions: the composite all-metals index, uranium-only, the top-3-variance-metals index, and the first principal component of metal z-scores. [src: enigma_contamination_functional_potential]

All 8 confirmatory variant tests remained non-significant after false-discovery-rate correction, with q = 0.546 across the tests, including uranium-only. [src: enigma_contamination_functional_potential]

## Coverage-Adjusted Exploratory Signals

Coverage-adjusted ordinary least squares models, adjusting for contamination, depth, latitude, longitude, and mapped abundance fraction, estimated a defense-score beta of 0.000751 for `relaxed_all_clades`, with 95% bootstrap confidence interval [0.000224, 0.001779], p = 0.000398, and false-discovery-rate q = 0.0462. [src: enigma_contamination_functional_potential]

The corresponding `strict_single_clade` model estimated beta = 0.000640, with 95% bootstrap confidence interval [0.000169, 0.001538], p = 0.00354, and false-discovery-rate q = 0.130. [src: enigma_contamination_functional_potential]

These results support a coverage-sensitive defense association in the relaxed mode but do not establish a robust association across both mapping modes after global false-discovery-rate correction. [src: enigma_contamination_functional_potential]

Fraction-aware adjusted models used contamination, mapped abundance fraction, and `C(community_fraction_type)`. [src: enigma_contamination_functional_potential]

In those models, `relaxed_all_clades` estimated beta = 0.000607, with 95% bootstrap confidence interval [0.000213, 0.001221], p = 0.00144, and false-discovery-rate q = 0.0838, while `strict_single_clade` estimated beta = 0.000566, with 95% bootstrap confidence interval [0.000214, 0.001113], p = 0.00548, and false-discovery-rate q = 0.130. [src: enigma_contamination_functional_potential]

## Robustness Limits

Fraction-aware analyses used 212 sample-fraction rows: 106 for the `0.2_micron_filter` fraction and 106 for the `10_micron_filter` fraction. [src: enigma_contamination_functional_potential]

Within-fraction defense Spearman tests were non-significant, with p = 0.767 and p = 0.898 for relaxed `0.2`- and `10`-micron fractions, respectively, and p = 0.780 and p = 0.793 for the corresponding strict fractions. [src: enigma_contamination_functional_potential]

This supports the conclusion that the strong monotonic defense signal is not robustly reproducible within individual fraction strata. [src: enigma_contamination_functional_potential]

In the high-coverage subset defined by `mapped_abundance_fraction >= 0.25`, defense-score Spearman p-values were 0.0207 for the relaxed mode and 0.00980 for the strict mode, but global false-discovery-rate q-values were 0.301 and 0.189, respectively. [src: enigma_contamination_functional_potential]

Most non-defense outcomes remained non-significant, although `site_stress_score` in the strict high-coverage subset had rho = 0.2489 and p = 0.0407. [src: enigma_contamination_functional_potential]

The species-proxy defense trend was positive but non-significant, with rho = 0.169 and Spearman p = 0.081, and no high-coverage test was feasible at `mapped_abundance_fraction >= 0.25` because of low retained coverage. [src: enigma_contamination_functional_potential]

The species-proxy high-coverage analysis had `n=1`, making it underpowered. [src: enigma_contamination_functional_potential]

These findings connect to [[concepts/taxonomic-resolution-dependent-functional-inference]] and [[concepts/coverage-confounding-of-community-functional-scores]] by demonstrating that taxonomic resolution and represented abundance jointly constrain the stability of inferred associations. [src: enigma_contamination_functional_potential]

## Implications for Functional Scores

The functional features totaled 3,630 rows across mapping modes, while COG-fraction proxies summarized broad categories rather than curated metal-resistance pathways. [src: enigma_contamination_functional_potential]

The analysis therefore does not establish that contamination causes a broad community-level shift in stress-related functional potential. [src: enigma_contamination_functional_potential]

Instead, the evidence is compatible with contamination-driven taxonomic turnover that is functionally redundant or expressed at species, strain, or pathway resolution finer than the current mapping. [src: enigma_contamination_functional_potential]

The interpretation also connects to [[concepts/functional-redundancy-under-environmental-selection]] because broad functional scores can remain stable even when community membership changes, although this dataset does not directly demonstrate redundancy. [src: enigma_contamination_functional_potential]

## Open Directions

- Replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether contamination associations persist after mapped-coverage adjustment. [src: enigma_contamination_functional_potential]
- Add species- or strain-level ENIGMA or metagenomic data and test whether finer taxonomic resolution reduces unmapped abundance and changes the defense association. [src: enigma_contamination_functional_potential]
- Fit models including depth, location cluster, sampling date, and compositional controls to determine whether coverage-adjusted associations survive richer confounding control. [src: enigma_contamination_functional_potential]
- Investigate the functional contribution of unmapped genera and expand the genus-to-clade bridge to determine whether missing coverage drives the observed score instability. [src: enigma_contamination_functional_potential]
- Fit mixed-effects or hierarchical site models using well- or location-level structure to test whether the exploratory defense associations persist beyond coarse `location_prefix` effects. [src: enigma_contamination_functional_potential]
- Compare the detailed results with [[summaries/enigma_contamination_functional_potential__REPORT]] and integrate the workflow with [[concepts/multi-omics-integration]] to quantify how geochemistry, community composition, pangenome mapping, and functional annotation jointly constrain inference. [src: enigma_contamination_functional_potential]
