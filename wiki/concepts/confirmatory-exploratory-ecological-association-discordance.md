---
type: "Concept"
description: "How confirmatory nulls can coexist with coverage-sensitive exploratory signals"
sources: ["summaries/enigma_contamination_functional_potential__REPORT.md"]
---
# Confirmatory Nulls and Exploratory Signals in Ecological Association Testing

This concept describes how predeclared ecological association tests can remain null while exploratory, coverage-adjusted analyses produce apparently positive signals that are sensitive to mapping, covariates, taxonomic resolution, and multiple-testing correction. [src: enigma_contamination_functional_potential]

The evidence comes from [[summaries/enigma_contamination_functional_potential__REPORT]], which tested whether contamination in [[entities/enigma-coral]] communities was associated with pangenome- and [[entities/eggnog]]-derived functional proxies. [src: enigma_contamination_functional_potential]

## Evidence Pattern

The analysis used 108 samples with geochemistry and community composition, a geochemistry matrix of shape `(108, 49)`, 41,711 community taxon rows, 212 distinct communities, and 1,392 distinct genera. [src: enigma_contamination_functional_potential]

The contamination index combined arsenic, cadmium, chromium, copper, lead, nickel, uranium, and zinc by per-metal `log1p` z-scoring followed by a row-wise mean; across 108 samples, it ranged from -0.448 to 3.836, with median -0.271 and IQR [-0.363, 0.053]. [src: enigma_contamination_functional_potential]

The workflow generated 324 site functional-score rows across three mapping modes and 12 model-result rows covering four outcomes across those modes. [src: enigma_contamination_functional_potential]

## Confirmatory Nulls

Predeclared Spearman tests of `site_defense_score` against contamination were non-significant in both genus-level mapping modes. [src: enigma_contamination_functional_potential]

In `relaxed_all_clades`, rho = 0.0587, the 95% bootstrap CI was [-0.128, 0.250], Spearman p = 0.546, and false-discovery-rate (FDR) q = 0.862. [src: enigma_contamination_functional_potential]

In `strict_single_clade`, rho = 0.0682, the 95% bootstrap CI was [-0.111, 0.253], Spearman p = 0.483, and FDR q = 0.849. [src: enigma_contamination_functional_potential]

The null result was robust to four contamination-index definitions: the composite all-metals index, uranium-only, the top-3-variance-metals index, and the first principal component of metal z-scores. [src: enigma_contamination_functional_potential]

All eight confirmatory variant tests remained non-significant after FDR, with q = 0.546 across the tests, including uranium-only. [src: enigma_contamination_functional_potential]

These results **support** treating the broad genus-level contamination–defense association as unconfirmed rather than as evidence of a monotonic community-level relationship. [src: enigma_contamination_functional_potential]

## Exploratory Signals

Coverage-adjusted ordinary least squares models adjusted for contamination, depth, latitude, longitude, and mapped abundance fraction. [src: enigma_contamination_functional_potential]

In `relaxed_all_clades`, the coverage-adjusted defense-score beta was 0.000751, with 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, and FDR q = 0.0462. [src: enigma_contamination_functional_potential]

The corresponding `strict_single_clade` estimate was beta = 0.000640, with 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, and FDR q = 0.130. [src: enigma_contamination_functional_potential]

These results **support** a coverage-sensitive defense association in the relaxed mode but do not establish a robust association across both mapping modes after global FDR. [src: enigma_contamination_functional_potential]

Fraction-aware adjusted models using contamination, mapped abundance fraction, and `C(community_fraction_type)` estimated beta = 0.000607, with 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, and FDR q = 0.0838 for `relaxed_all_clades`. [src: enigma_contamination_functional_potential]

The corresponding `strict_single_clade` fraction-aware estimate was beta = 0.000566, with 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, and FDR q = 0.130. [src: enigma_contamination_functional_potential]

In the high-coverage subset defined by `mapped_abundance_fraction >= 0.25`, defense-score Spearman p-values were 0.0207 for the relaxed mode and 0.00980 for the strict mode, while global FDR q-values were 0.301 and 0.189, respectively. [src: enigma_contamination_functional_potential]

Most non-defense outcomes remained non-significant, although `site_stress_score` in the strict high-coverage subset had rho = 0.2489 and p = 0.0407. [src: enigma_contamination_functional_potential]

## Robustness and Sources of Discordance

Within-fraction defense Spearman tests were non-significant for both mapping modes and both fractions: relaxed `0.2_micron_filter` p = 0.767, relaxed `10_micron_filter` p = 0.898, strict `0.2_micron_filter` p = 0.780, and strict `10_micron_filter` p = 0.793. [src: enigma_contamination_functional_potential]

This **contradicts** interpreting the pooled exploratory defense signal as a robust monotonic relationship that reproduces within individual fraction strata. [src: enigma_contamination_functional_potential]

The species-proxy mode retained 150 unique-clade genera compared with 530 mapped genera overall, while 380 mapped genera were ambiguous multi-clade genera. [src: enigma_contamination_functional_potential]

Mean mapped abundance fraction was 0.031 in the species-proxy mode versus 0.343 in the strict and relaxed modes. [src: enigma_contamination_functional_potential]

The species-proxy defense trend was positive but non-significant, with rho = 0.169 and Spearman p = 0.081, and no high-coverage test was feasible at `mapped_abundance_fraction >= 0.25` because of low retained coverage. [src: enigma_contamination_functional_potential]

The bridge contained 8,242 genus-to-clade bridge rows, with a maximum of 433 clades per genus; the most ambiguous genera were `pseudomonas` (433), `streptomyces` (378), `prevotella` (358), `streptococcus` (214), and `mycobacterium` (186). [src: enigma_contamination_functional_potential]

A total of 862 of 1,392 observed genera were unmapped to the current pangenome bridge. [src: enigma_contamination_functional_potential]

These coverage, ambiguity, and unmapped-genus patterns **refine** the interpretation of the exploratory signal: it may reflect functional differences detectable through the retained mapped fraction, while the broader community-level relationship remains unresolved. [src: enigma_contamination_functional_potential]

## Tensions

The principal tension is between null predeclared genus-level Spearman tests and positive exploratory models that adjust for mapped coverage and additional covariates. [src: enigma_contamination_functional_potential]

The confirmatory tests provide no robust monotonic contamination–defense association, whereas the relaxed coverage-adjusted model has FDR q = 0.0462 and the strict model has FDR q = 0.130. [src: enigma_contamination_functional_potential]

The discordance is not resolved by the high-coverage subset or fraction-aware analyses, because high-coverage defense tests have global FDR q-values of 0.301 and 0.189, and within-fraction tests are non-significant. [src: enigma_contamination_functional_potential]

The project therefore supports a cautious hypothesis that contamination-linked functional differentiation may exist at finer taxonomic, pathway, or strain resolution than the current genus-level COG-fraction proxies, but it does not establish that hypothesis as a community-wide finding. [src: enigma_contamination_functional_potential]

## Relation to Other Concepts

This concept **supports** [[concepts/statistical-significance-versus-effect-size]] because nominal p-values and exploratory FDR results differ from the broader evidence needed for a stable ecological association. [src: enigma_contamination_functional_potential]

It **refines** [[concepts/coverage-confounding-of-community-functional-scores]] by showing that mapped abundance fraction changes the apparent defense association and that low-coverage modes can lose usable signal. [src: enigma_contamination_functional_potential]

It **supports** [[concepts/taxonomic-resolution-dependent-functional-inference]] because strict, relaxed, and species-proxy mapping modes produce different coverage and association results. [src: enigma_contamination_functional_potential]

It **connects** to [[concepts/confirmatory-exploratory-ecological-association-discordance]] as a general framework for separating predeclared evidence from sensitivity-generated hypotheses. [src: enigma_contamination_functional_potential]

## Open Directions

- Replace broad COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether the confirmatory contamination association remains null at finer functional resolution. [src: enigma_contamination_functional_potential]
- Add species- or strain-level ENIGMA or metagenomic data and repeat the confirmatory and coverage-adjusted models to test whether genus-level aggregation masks adaptation. [src: enigma_contamination_functional_potential]
- Fit models including depth, location cluster, sampling date, and compositional controls, using mixed-effects or hierarchical structure, to determine whether the exploratory defense association persists beyond coarse `location_prefix` adjustment. [src: enigma_contamination_functional_potential]
- Investigate the 862 unmapped genera and expand the genus-to-clade bridge to test whether missing coverage changes the direction or magnitude of the contamination–functional association. [src: enigma_contamination_functional_potential]
- Reanalyze the 212 sample-fraction rows with preregistered fraction-stratified and pooled contrasts to determine whether the pooled exploratory signal can be reproduced across the `0.2_micron_filter` and `10_micron_filter` fractions. [src: enigma_contamination_functional_potential]
