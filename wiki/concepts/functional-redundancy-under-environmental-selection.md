---
type: "Concept"
description: "Environmental selection may alter taxa without changing coarse community functions."
sources: ["summaries/enigma_contamination_functional_potential__REPORT.md"]
---
# Functional Redundancy Can Mask Environmental Selection

Functional redundancy is the possibility that different taxa provide overlapping functions, allowing community-level functional summaries to remain stable while environmental selection changes taxonomic composition. In this concept, the evidence supports the hypothesis that contamination-linked turnover can be obscured when functional potential is inferred from coarse categories and aggregated at genus resolution. [src: enigma_contamination_functional_potential]

## Evidence from the ENIGMA contamination gradient

The ENIGMA analysis integrated geochemistry, community composition, pangenome clades, and eggNOG-derived functional proxies across 108 samples. [src: enigma_contamination_functional_potential] The geochemistry matrix contained 49 columns, the community data contained 41,711 taxon rows, and the analysis covered 1,392 distinct genera. [src: enigma_contamination_functional_potential]

The contamination index combined arsenic, cadmium, chromium, copper, lead, nickel, uranium, and zinc using per-metal `log1p` z-scoring followed by a row-wise mean. [src: enigma_contamination_functional_potential] Across the 108 samples, this index ranged from -0.448 to 3.836, with median -0.271 and IQR [-0.363, 0.053]. [src: enigma_contamination_functional_potential]

Predeclared tests found no robust monotonic relationship between contamination and the broad `site_defense_score`. In the relaxed-all-clades mode, Spearman rho was 0.0587, with a 95% bootstrap CI of [-0.128, 0.250], Spearman p = 0.546, and false-discovery-rate (FDR) q = 0.862. [src: enigma_contamination_functional_potential] In the strict-single-clade mode, rho was 0.0682, with a 95% bootstrap CI of [-0.111, 0.253], Spearman p = 0.483, and FDR q = 0.849. [src: enigma_contamination_functional_potential]

The null result persisted across four contamination-index definitions: the composite all-metals index, uranium-only, the top-3-variance-metals index, and the first principal component of metal z-scores. [src: enigma_contamination_functional_potential] All 8 confirmatory variant tests remained non-significant after FDR, with q = 0.546 across the tests, including uranium-only. [src: enigma_contamination_functional_potential]

## Why coarse functional summaries can conceal selection

Coverage-adjusted exploratory ordinary least squares models detected a positive defense association in the relaxed-all-clades mode after adjustment for contamination, depth, latitude, longitude, and mapped abundance fraction. [src: enigma_contamination_functional_potential] The estimated beta was 0.000751, with a 95% bootstrap CI of [0.000224, 0.001779], p = 0.000398, and FDR q = 0.0462. [src: enigma_contamination_functional_potential] The corresponding strict-single-clade estimate was beta = 0.000640, with a 95% bootstrap CI of [0.000169, 0.001538], p = 0.00354, and FDR q = 0.130. [src: enigma_contamination_functional_potential]

These exploratory results support a coverage-sensitive defense association in the relaxed mode but do not establish a robust association across both mapping modes after global FDR. [src: enigma_contamination_functional_potential] Fraction-aware adjusted models likewise estimated positive defense effects, with beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, and FDR q = 0.0838 for relaxed-all-clades, and beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, and FDR q = 0.130 for strict-single-clade. [src: enigma_contamination_functional_potential]

The apparent signal was not robust within individual sample fractions. [src: enigma_contamination_functional_potential] Fraction-aware analyses used 212 sample-fraction rows, including 106 for the `0.2_micron_filter` fraction and 106 for the `10_micron_filter` fraction. [src: enigma_contamination_functional_potential] Within-fraction defense tests had p = 0.767 and p = 0.898 for the relaxed `0.2`- and `10`-micron fractions, respectively, and p = 0.780 and p = 0.793 for the corresponding strict fractions. [src: enigma_contamination_functional_potential]

The contrast between taxonomic, coverage-adjusted, and coarse functional results is consistent with the hypothesis that environmental selection may change which taxa are present without producing a large shift in aggregated functional potential. [src: enigma_contamination_functional_potential] The source analysis specifically identifies contamination-driven taxonomic turnover that is functionally redundant, or that operates at species, strain, or pathway resolution finer than the current mapping, as an interpretation compatible with the data. [src: enigma_contamination_functional_potential]

## Mapping and annotation constraints

The taxonomy bridge parsed 27,690 GTDB species rows, mapped 530 genera, left 862 genera unmapped, and produced 530 strict clades, 7,380 relaxed clades, and 150 species-proxy clades restricted to genera mapping to exactly one clade. [src: enigma_contamination_functional_potential] The bridge contained 8,242 genus-to-clade rows because of many-to-many expansion, and the maximum number of clades associated with one genus was 433. [src: enigma_contamination_functional_potential]

The most ambiguous genera were `pseudomonas` with 433 clades, `streptomyces` with 378, `prevotella` with 358, `streptococcus` with 214, and `mycobacterium` with 186. [src: enigma_contamination_functional_potential] These ambiguities can redistribute functional features across clades and weaken the ability of genus-level summaries to resolve species- or strain-specific environmental responses. [src: enigma_contamination_functional_potential]

The species-proxy mode retained 150 unique-clade genera versus 530 mapped genera overall, while 380 mapped genera were ambiguous multi-clade genera. [src: enigma_contamination_functional_potential] Mean mapped abundance fraction was 0.031 in the species-proxy mode versus 0.343 in the strict and relaxed modes. [src: enigma_contamination_functional_potential] The species-proxy defense trend was positive but non-significant, with rho = 0.169 and Spearman p = 0.081, and no high-coverage test was feasible at `mapped_abundance_fraction >= 0.25` because of low retained coverage. [src: enigma_contamination_functional_potential]

The analysis generated 3,630 functional feature rows across mapping modes, with mean mapped abundance fraction of 0.343 in strict and relaxed modes and 0.031 in the species-proxy mode. [src: enigma_contamination_functional_potential] The source taxonomy table provided labels through Genus but no species or strain labels, preventing direct species-level bridge testing for this dataset slice. [src: enigma_contamination_functional_potential] COG-fraction proxies therefore represent coarse functional summaries rather than curated metal-resistance pathways. [src: enigma_contamination_functional_potential]

## Relation to broader interpretation

This finding refines [[concepts/environmental-resistome]] by showing that a contamination gradient need not produce a detectable shift in broad community defense scores, even when exploratory coverage-aware models suggest a possible association. [src: enigma_contamination_functional_potential] It also connects to [[concepts/ecotype-environment-gene-content]] because environmental differentiation may be detectable in taxonomic composition or gene content before it is visible in aggregated functional categories. [src: enigma_contamination_functional_potential]

The result highlights a limitation of [[concepts/pangenome-integration]]: bridging genus-level observations to pangenome clades can quantify functional potential while still losing species- or strain-level ecological specialization. [src: enigma_contamination_functional_potential] It also supports [[concepts/multi-omics-integration]] by demonstrating that integrating geochemistry, community composition, taxonomy, pangenome clades, and functional annotations does not eliminate coverage, mapping, or resolution constraints. [src: enigma_contamination_functional_potential]

The complete project summary is available at [[summaries/enigma_contamination_functional_potential__REPORT]]. [src: enigma_contamination_functional_potential]

## Open Directions

- Replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether contamination-associated functional shifts emerge after coverage adjustment. [src: enigma_contamination_functional_potential]
- Add species- or strain-level ENIGMA or metagenomic data and use higher-resolution pangenome mappings to ask whether contamination effects are hidden below genus resolution. [src: enigma_contamination_functional_potential]
- Fit mixed-effects or hierarchical models using depth, location cluster, sampling date, and compositional controls to determine whether exploratory defense associations persist after richer site-structure adjustment. [src: enigma_contamination_functional_potential]
- Quantify the contribution of the 862 unmapped genera and expand the genus-to-clade bridge to test whether missing taxa account for the weak broad functional signal. [src: enigma_contamination_functional_potential]
