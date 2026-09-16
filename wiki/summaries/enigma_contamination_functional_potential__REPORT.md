---
type: "Summary"
description: "Summary of an ENIGMA project linking groundwater metal-contamination gradients to genus-bridged pangenome functional proxies, in which confirmatory contamination\u2013defense tests were null and exploratory coverage-aware associations were sensitive to coverage, covariates, taxonomic resolution and FDR correction."
doc_type: "short"
full_text: "sources/enigma_contamination_functional_potential__REPORT.md"
---
# Contamination Gradient vs Functional Potential in ENIGMA Communities

## Overview

This project developed a reproducible workflow linking [[entities/enigma-coral]] geochemistry and community composition to [[entities/kbase-ke-pangenome]] pangenome clades and [[entities/eggnog]]-derived functional proxies. Across 108 ENIGMA samples, confirmatory genus-level tests found no robust monotonic association between contamination and broad functional scores, while exploratory coverage-aware models detected positive defense associations that were sensitive to coverage, covariate specification, taxonomic resolution, and multiple-testing correction. [src: enigma_contamination_functional_potential]

## Key Findings

### Data scope and modeling context

Quality-controlled overlap data comprised 108 samples with geochemistry and community composition, a geochemistry matrix of shape `(108, 49)`, 41,711 community taxon rows, 212 distinct communities, and 1,392 distinct genera. [src: enigma_contamination_functional_potential]

The taxonomy bridge parsed 27,690 GTDB species rows, mapped 530 genera, left 862 genera unmapped, and produced 530 strict clades, 7,380 relaxed clades, and 150 species-proxy clades restricted to genera mapping to exactly one clade. [src: enigma_contamination_functional_potential]

The analysis generated 324 site functional-score rows, corresponding to 108 samples across 3 mapping modes, and 12 model-result rows covering 4 outcomes across those modes. Model diagnostics included confirmatory and exploratory labels, bootstrap confidence intervals, adjusted coordinate/depth models, coverage-adjusted models, site-structure models using `location_prefix`, fraction-aware models using `community_fraction_type`, within-fraction correlations, high-coverage subset correlations, and global Benjamini–Hochberg false-discovery-rate q-values. [src: enigma_contamination_functional_potential]

Model-family counts were 108 for base Spearman, adjusted-plus-covariate, and strict/relaxed analyses; fraction-aware models used 212 sample-fraction rows; and high-coverage subsets used 68 rows. The `species_proxy_unique_genus` high-coverage test had `n=1`, making that analysis underpowered. [src: enigma_contamination_functional_potential]

### Confirmatory contamination–defense tests were null

The report designates the Spearman tests as confirmatory and the adjusted models as exploratory sensitivity analyses. Predeclared Spearman tests of `site_defense_score` against contamination were non-significant in both genus-level modes. In `relaxed_all_clades`, rho = 0.0587, the 95% bootstrap CI was [-0.128, 0.250], Spearman p = 0.546, and FDR q = 0.862; in `strict_single_clade`, rho = 0.0682, the 95% bootstrap CI was [-0.111, 0.253], Spearman p = 0.483, and FDR q = 0.849. [src: enigma_contamination_functional_potential]

The confirmatory null result was robust to four contamination-index definitions: the composite all-metals index, uranium-only, the top-3-variance-metals index, and the first principal component of metal z-scores. All 8 confirmatory variant tests remained non-significant after FDR, with q = 0.546 across the tests, including uranium-only. [src: enigma_contamination_functional_potential]

### Exploratory coverage-aware defense associations

Coverage-adjusted ordinary least squares models, adjusting for contamination, depth, latitude, longitude, and mapped abundance fraction, estimated a defense-score beta of 0.000751 with 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, and FDR q = 0.0462 for `relaxed_all_clades`; the corresponding `strict_single_clade` estimate was beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, and FDR q = 0.130. These exploratory results support a coverage-sensitive defense association in the relaxed mode but do not establish a robust association across both mapping modes after global FDR. [src: enigma_contamination_functional_potential]

Fraction-aware adjusted models using contamination, mapped abundance fraction, and `C(community_fraction_type)` estimated beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, and FDR q = 0.0838 for `relaxed_all_clades`; `strict_single_clade` estimated beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, and FDR q = 0.130. [src: enigma_contamination_functional_potential]

In the high-coverage subset defined by `mapped_abundance_fraction >= 0.25`, defense-score Spearman p-values were 0.0207 for the relaxed mode and 0.00980 for the strict mode, but global FDR q-values were 0.301 and 0.189, respectively. Most non-defense outcomes remained non-significant; the one exploratory exception was `site_stress_score` in the strict high-coverage subset, with rho = 0.2489 and p = 0.0407. [src: enigma_contamination_functional_potential]

### Fraction and taxonomic-resolution robustness

To address potential confounding from collapsing multiple community fractions, the analysis retained `community_fraction_type` parsed from `sdt_community_name` and ran fraction-aware robustness analyses. Fraction-aware models used 212 sample-fraction rows: 106 for the `0.2_micron_filter` fraction and 106 for the `10_micron_filter` fraction. Within-fraction defense Spearman tests were non-significant, with p = 0.767 and p = 0.898 for relaxed `0.2`- and `10`-micron fractions, respectively, and p = 0.780 and p = 0.793 for the corresponding strict fractions. This supports the conclusion that the strong monotonic defense signal is not robustly reproducible within individual fraction strata. [src: enigma_contamination_functional_potential]

Because the available ENIGMA taxonomy stops at genus, the `species_proxy_unique_genus` mode approximates higher taxonomic resolution using only genera that map to exactly one GTDB species clade. The species-proxy mode retained 150 unique-clade genera versus 530 mapped genera overall, while 380 mapped genera were ambiguous multi-clade genera. Mean mapped abundance fraction was 0.031 in the species-proxy mode versus 0.343 in the strict and relaxed modes. The species-proxy defense trend was positive but non-significant, with rho = 0.169 and Spearman p = 0.081, and no high-coverage test was feasible at `mapped_abundance_fraction >= 0.25` because of low retained coverage. [src: enigma_contamination_functional_potential]

Bridge diagnostics showed 8,242 genus-to-clade bridge rows, reflecting many-to-many expansion. The clade-count distribution had a long right tail, with a maximum of 433 clades per genus; the most ambiguous genera were `pseudomonas` (433), `streptomyces` (378), `prevotella` (358), `streptococcus` (214), and `mycobacterium` (186). [src: enigma_contamination_functional_potential]

The bridge observed 1,392 ENIGMA genera, mapped 530 and left 862 unmapped; of the mapped genera, 150 were unique-clade (species-proxy resolvable) and 380 were multi-clade ambiguous, and the bridge table had 8,242 rows from many-to-many genus-to-clade expansion. Functional feature rows totaled 3,630 across 3 mapping modes (`strict_single_clade`, `relaxed_all_clades`, `species_proxy_unique_genus`). Mean mapped abundance fraction was 0.343 in strict and relaxed modes, with range 0.031 to 0.854, and 0.031 in species-proxy mode, with range 0.0002 to 0.543. [src: enigma_contamination_functional_potential]

### Contamination index and overall interpretation

The contamination index combined 8 metal columns—arsenic, cadmium, chromium, copper, lead, nickel, uranium, and zinc—by per-metal `log1p` z-scoring followed by a row-wise mean. Across 108 samples, the index ranged from -0.448 to 3.836, with median -0.271 and IQR [-0.363, 0.053]. [src: enigma_contamination_functional_potential]

Overall, the report distinguishes confirmatory evidence that remains null and robust to contamination-index definition from exploratory coverage-aware defense associations that persist with positive effect estimates but are attenuated under global multiple-testing control. Within this ENIGMA subset, contamination gradients did not produce a robust community-level shift in inferred stress-related functional potential when broad COG-category (Clusters of Orthologous Groups, coarse functional classes of orthologous genes) proxies were aggregated at genus resolution. The result is compatible with contamination-driven taxonomic turnover that is functionally redundant or operates at species, strain, or pathway resolution finer than the current mapping; these remain possible interpretations, not established results. [src: enigma_contamination_functional_potential]

The project contributes independent strict-versus-relaxed functional-feature construction, mapped-coverage diagnostics, a unique-clade species-proxy sensitivity mode, and multi-tier modeling beyond basic univariate association tests. [src: enigma_contamination_functional_potential]

### Literature context

As literature context, the report describes its results as directionally aligned with Hemme et al. (2015; PMID: 26583008), who reported strong contamination-linked taxonomic restructuring in Oak Ridge groundwater with reduced functional breadth in stressed communities; it interprets its own confirmatory null genus-aggregated Spearman results as consistent with contamination effects that do not collapse into one robust monotonic community-wide proxy. It also cites Fan et al. (2025), who reported pronounced compositional shifts but only modest functional-diversity decline in a mixed waste-contaminated Oak Ridge aquifer, as matching a pattern in which ecological differentiation is detectable while broad functional summaries show weaker confirmatory monotonic response. Relative to Carlson et al. (2019; PMID: 30523276), the report positions its strict, relaxed, and species-proxy bridge-aware functional sensitivity modeling as an extension from taxa-abundance association that quantifies where inference remains coverage-limited. These are literature comparisons drawn by the report, not new measurements. [src: enigma_contamination_functional_potential]

## Caveats and Limitations

The ENIGMA taxonomy table `ddt_brick0000454` provides labels through Genus but no species or strain labels, so direct species-level bridge testing is not possible for this dataset slice. Genus-level mapping may therefore mask strain-level adaptation. [src: enigma_contamination_functional_potential]

A total of 862 of 1,392 observed genera were unmapped to the current pangenome bridge, and the bridge includes substantial ambiguity, including 380 multi-clade genera and a maximum of 433 species clades per genus. [src: enigma_contamination_functional_potential]

COG-fraction proxies are coarse summaries rather than curated metal-resistance pathways. Exploratory sensitivity significance was concentrated in defense and depended on coverage and covariate specification; broader effects across outcomes are not established. The bridge and annotation stack depends on GTDB and eggNOG conventions, and at genus-level aggregation broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]

Site structure was represented by coarse `location_prefix` effects rather than full hierarchical or random-effects modeling. The analysis therefore does not yet establish whether the exploratory defense associations persist under richer well- or location-level structure control. [src: enigma_contamination_functional_potential]

The document identifies five next analyses: replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries; increase taxonomic resolution using species- or strain-level ENIGMA or metagenomic data; fit models with depth, location cluster, sampling date, and compositional controls; investigate unmapped-genera contributions and bridge expansion; and add mixed-effects or hierarchical site models. [src: enigma_contamination_functional_potential]

## Data Sources and Figures

The `enigma_coral` collection ([[entities/enigma-coral]]) supplied geochemistry, community composition, taxonomy linkage, and sample metadata from `ddt_brick0000010`, `ddt_brick0000459`, `ddt_brick0000454`, `sdt_sample`, `sdt_community`, and `sdt_location`. The `kbase_ke_pangenome` collection ([[entities/kbase-ke-pangenome]]) supplied `gtdb_species_clade`, `pangenome`, `gene_cluster`, and `eggnog_mapper_annotations` for the taxonomy bridge and COG-derived functional feature construction. The report cites GTDB ([[entities/gtdb]]; Parks et al. 2022) as a phylogenetically consistent, rank-normalized, genome-based taxonomy of bacterial and archaeal diversity, and eggNOG-mapper v2 ([[entities/eggnog]]; Cantalapiedra et al. 2021) as a tool for functional annotation, orthology assignment, and domain prediction at the metagenomic scale. [src: enigma_contamination_functional_potential]

Figures referenced by the report [src: enigma_contamination_functional_potential]:
- `figures/confirmatory_defense_vs_contamination.png` — confirmatory defense score versus contamination index, faceted by strict and relaxed mapping mode. [src: enigma_contamination_functional_potential]
- `figures/contamination_vs_functional_score.png` — exploratory stress score versus contamination index, faceted by mapping mode. [src: enigma_contamination_functional_potential]
- `figures/contamination_index_distribution.png` — histogram of contamination-index values across 108 samples. [src: enigma_contamination_functional_potential]
- `figures/mapping_coverage_by_mode.png` — number of feature-covered genera per mapping mode. [src: enigma_contamination_functional_potential]

## Slots Into

- [[concepts/environmental-resistome]] — contamination-index analyses test whether metal gradients correspond to broad community defense and stress functional potential, while showing that confirmatory genus-level associations remain null. [src: enigma_contamination_functional_potential]
- [[concepts/pangenome-integration]] — the project quantifies strict, relaxed, and species-proxy bridges from 1,392 ENIGMA genera to GTDB clades and documents coverage and ambiguity constraints. [src: enigma_contamination_functional_potential]
- [[concepts/ecotype-environment-gene-content]] — the findings distinguish detectable contamination-linked ecological differentiation from weaker broad functional shifts and motivate higher-resolution taxonomic and pathway analyses. [src: enigma_contamination_functional_potential]
- [[concepts/multi-omics-integration]] — the workflow integrates geochemistry, community composition, taxonomy, pangenome clades, and eggNOG-derived functional features, while exposing limits of cross-dataset coverage. [src: enigma_contamination_functional_potential]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — predeclared Spearman contamination–defense tests were null and robust to four index variants, while exploratory coverage-adjusted and fraction-aware models gave positive defense coefficients attenuated by global FDR and absent within fraction strata. [src: enigma_contamination_functional_potential]
- [[concepts/taxonomic-resolution-dependent-functional-inference]] — genus-only ENIGMA taxonomy, 380 multi-clade genera, up to 433 clades per genus, and a species-proxy mode with mean mapped abundance fraction 0.031 show how resolution limits functional inference. [src: enigma_contamination_functional_potential]
- [[concepts/composite-resistance-score-limitations]] — the eight-metal log1p z-score contamination index and coarse COG-fraction proxies are composite summaries rather than curated resistance pathways. [src: enigma_contamination_functional_potential]
- [[concepts/cross-tenant-data-bridging]] — the ENIGMA-to-pangenome bridge mapped 530 genera and left 862 of 1,392 unmapped, with 8,242 many-to-many bridge rows. [src: enigma_contamination_functional_potential]
- [[concepts/taxonomic-nomenclature-reconciliation]] — genus-to-GTDB-clade mapping showed a long right tail of ambiguity led by `pseudomonas` (433). [src: enigma_contamination_functional_potential]
- [[concepts/functional-marker-validation]] — broad COG-style features may dilute pathway-specific metal-response signals, motivating curated metal-stress gene sets. [src: enigma_contamination_functional_potential]
- [[concepts/study-batch-confounding-of-environmental-associations]] — site structure was controlled only through coarse `location_prefix` effects, not hierarchical or random-effects models. [src: enigma_contamination_functional_potential]
