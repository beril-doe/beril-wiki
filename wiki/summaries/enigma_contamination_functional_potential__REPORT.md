---
type: Summary
description: ENIGMA contamination gradients show null broad functional shifts but
  coverage-sensitive defense signals.
doc_type: short
full_text: ../sources/enigma_contamination_functional_potential__REPORT.md
title: Contamination Gradient vs Functional Potential in ENIGMA Communities
sources:
- id: enigma_contamination_functional_potential
  resource: ../sources/enigma_contamination_functional_potential__REPORT.md
  title: enigma contamination functional potential
---
# Contamination Gradient vs Functional Potential in ENIGMA Communities

## Overview

This project developed a reproducible workflow linking [enigma-coral](../entities/enigma-coral.md) geochemistry and community composition to [kbase-ke-pangenome](../entities/kbase-ke-pangenome.md) pangenome clades and [eggnog](../entities/eggnog.md)-derived functional proxies. Across 108 ENIGMA samples, confirmatory genus-level tests found no robust monotonic association between contamination and broad functional scores, while exploratory coverage-aware models detected positive defense associations that were sensitive to coverage, covariate specification, taxonomic resolution, and multiple-testing correction. [^enigma_contamination_functional_potential]

## Key Findings

### Data scope and modeling context

Quality-controlled overlap data comprised 108 samples with geochemistry and community composition, a geochemistry matrix of shape `(108, 49)`, 41,711 community taxon rows, 212 distinct communities, and 1,392 distinct genera. [^enigma_contamination_functional_potential]

The taxonomy bridge parsed 27,690 GTDB species rows, mapped 530 genera, left 862 genera unmapped, and produced 530 strict clades, 7,380 relaxed clades, and 150 species-proxy clades restricted to genera mapping to exactly one clade. [^enigma_contamination_functional_potential]

The analysis generated 324 site functional-score rows, corresponding to 108 samples across 3 mapping modes, and 12 model-result rows covering 4 outcomes across those modes. Model diagnostics included confirmatory and exploratory labels, bootstrap confidence intervals, adjusted coordinate/depth models, coverage-adjusted models, site-structure models using `location_prefix`, fraction-aware models using `community_fraction_type`, within-fraction correlations, high-coverage subset correlations, and global Benjamini–Hochberg false-discovery-rate q-values. [^enigma_contamination_functional_potential]

Model-family counts were 108 for base Spearman, adjusted-plus-covariate, and strict/relaxed analyses; fraction-aware models used 212 sample-fraction rows; and high-coverage subsets used 68 rows. The `species_proxy_unique_genus` high-coverage test had `n=1`, making that analysis underpowered. [^enigma_contamination_functional_potential]

### Confirmatory contamination–defense tests were null

Predeclared Spearman tests of `site_defense_score` against contamination were non-significant in both genus-level modes. In `relaxed_all_clades`, rho = 0.0587, the 95% bootstrap CI was [-0.128, 0.250], Spearman p = 0.546, and FDR q = 0.862; in `strict_single_clade`, rho = 0.0682, the 95% bootstrap CI was [-0.111, 0.253], Spearman p = 0.483, and FDR q = 0.849. [^enigma_contamination_functional_potential]

The confirmatory null result was robust to four contamination-index definitions: the composite all-metals index, uranium-only, the top-3-variance-metals index, and the first principal component of metal z-scores. All 8 confirmatory variant tests remained non-significant after FDR, with q = 0.546 across the tests, including uranium-only. [^enigma_contamination_functional_potential]

### Exploratory coverage-aware defense associations

Coverage-adjusted ordinary least squares models, adjusting for contamination, depth, latitude, longitude, and mapped abundance fraction, estimated a defense-score beta of 0.000751 with 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, and FDR q = 0.0462 for `relaxed_all_clades`; the corresponding `strict_single_clade` estimate was beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, and FDR q = 0.130. These exploratory results support a coverage-sensitive defense association in the relaxed mode but do not establish a robust association across both mapping modes after global FDR. [^enigma_contamination_functional_potential]

Fraction-aware adjusted models using contamination, mapped abundance fraction, and `C(community_fraction_type)` estimated beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, and FDR q = 0.0838 for `relaxed_all_clades`; `strict_single_clade` estimated beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, and FDR q = 0.130. [^enigma_contamination_functional_potential]

In the high-coverage subset defined by `mapped_abundance_fraction >= 0.25`, defense-score Spearman p-values were 0.0207 for the relaxed mode and 0.00980 for the strict mode, but global FDR q-values were 0.301 and 0.189, respectively. Most non-defense outcomes remained non-significant; the one exploratory exception was `site_stress_score` in the strict high-coverage subset, with rho = 0.2489 and p = 0.0407. [^enigma_contamination_functional_potential]

### Fraction and taxonomic-resolution robustness

Fraction-aware models used 212 sample-fraction rows: 106 for the `0.2_micron_filter` fraction and 106 for the `10_micron_filter` fraction. Within-fraction defense Spearman tests were non-significant, with p = 0.767 and p = 0.898 for relaxed `0.2`- and `10`-micron fractions, respectively, and p = 0.780 and p = 0.793 for the corresponding strict fractions. This supports the conclusion that the strong monotonic defense signal is not robustly reproducible within individual fraction strata. [^enigma_contamination_functional_potential]

The species-proxy mode retained 150 unique-clade genera versus 530 mapped genera overall, while 380 mapped genera were ambiguous multi-clade genera. Mean mapped abundance fraction was 0.031 in the species-proxy mode versus 0.343 in the strict and relaxed modes. The species-proxy defense trend was positive but non-significant, with rho = 0.169 and Spearman p = 0.081, and no high-coverage test was feasible at `mapped_abundance_fraction >= 0.25` because of low retained coverage. [^enigma_contamination_functional_potential]

Bridge diagnostics showed 8,242 genus-to-clade bridge rows, reflecting many-to-many expansion. The clade-count distribution had a long right tail, with a maximum of 433 clades per genus; the most ambiguous genera were `pseudomonas` (433), `streptomyces` (378), `prevotella` (358), `streptococcus` (214), and `mycobacterium` (186). [^enigma_contamination_functional_potential]

Across mapping modes, functional feature rows totaled 3,630. Mean mapped abundance fraction was 0.343 in strict and relaxed modes, with range 0.031 to 0.854, and 0.031 in species-proxy mode, with range 0.0002 to 0.543. [^enigma_contamination_functional_potential]

### Contamination index and overall interpretation

The contamination index combined 8 metal columns—arsenic, cadmium, chromium, copper, lead, nickel, uranium, and zinc—by per-metal `log1p` z-scoring followed by a row-wise mean. Across 108 samples, the index ranged from -0.448 to 3.836, with median -0.271 and IQR [-0.363, 0.053]. [^enigma_contamination_functional_potential]

Within this ENIGMA subset, contamination gradients did not produce a robust community-level shift in inferred stress-related functional potential when broad COG-category proxies were aggregated at genus resolution. The result is compatible with contamination-driven taxonomic turnover that is functionally redundant or operates at species, strain, or pathway resolution finer than the current mapping. [^enigma_contamination_functional_potential]

The project contributes independent strict-versus-relaxed functional-feature construction, mapped-coverage diagnostics, a unique-clade species-proxy sensitivity mode, and multi-tier modeling beyond basic univariate association tests. [^enigma_contamination_functional_potential]

## Caveats and Limitations

The ENIGMA taxonomy table `ddt_brick0000454` provides labels through Genus but no species or strain labels, so direct species-level bridge testing is not possible for this dataset slice. Genus-level mapping may therefore mask strain-level adaptation. [^enigma_contamination_functional_potential]

A total of 862 of 1,392 observed genera were unmapped to the current pangenome bridge, and the bridge includes substantial ambiguity, including 380 multi-clade genera and a maximum of 433 species clades per genus. [^enigma_contamination_functional_potential]

COG-fraction proxies are coarse summaries rather than curated metal-resistance pathways. Exploratory sensitivity significance was concentrated in defense and depended on coverage and covariate specification; broader effects across outcomes are not established. [^enigma_contamination_functional_potential]

Site structure was represented by coarse `location_prefix` effects rather than full hierarchical or random-effects modeling. The analysis therefore does not yet establish whether the exploratory defense associations persist under richer well- or location-level structure control. [^enigma_contamination_functional_potential]

The document identifies five next analyses: replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries; increase taxonomic resolution using species- or strain-level ENIGMA or metagenomic data; fit models with depth, location cluster, sampling date, and compositional controls; investigate unmapped-genera contributions and bridge expansion; and add mixed-effects or hierarchical site models. [^enigma_contamination_functional_potential]

## Slots Into

- [environmental-resistome](../concepts/environmental-resistome.md) — contamination-index analyses test whether metal gradients correspond to broad community defense and stress functional potential, while showing that confirmatory genus-level associations remain null. [^enigma_contamination_functional_potential]
- [pangenome-integration](../concepts/pangenome-integration.md) — the project quantifies strict, relaxed, and species-proxy bridges from 1,392 ENIGMA genera to GTDB clades and documents coverage and ambiguity constraints. [^enigma_contamination_functional_potential]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — the findings distinguish detectable contamination-linked ecological differentiation from weaker broad functional shifts and motivate higher-resolution taxonomic and pathway analyses. [^enigma_contamination_functional_potential]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — the workflow integrates geochemistry, community composition, taxonomy, pangenome clades, and eggNOG-derived functional features, while exposing limits of cross-dataset coverage. [^enigma_contamination_functional_potential]

[^enigma_contamination_functional_potential]: [enigma contamination functional potential](../sources/enigma_contamination_functional_potential__REPORT.md)
