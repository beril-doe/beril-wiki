---
type: "Summary"
description: "Summary of the project Contamination Gradient vs Functional Potential in ENIGMA Communities."
doc_type: "short"
full_text: "sources/enigma_contamination_functional_potential__REPORT.md"
---
# Contamination Gradient vs Functional Potential in ENIGMA Communities

This page summarises the project Contamination Gradient vs Functional Potential in ENIGMA Communities. The predeclared defense-score versus contamination tests were non-significant. [src: enigma_contamination_functional_potential] Within this ENIGMA subset, contamination gradients did not produce a robust community-level shift in inferred stress-related functional potential aggregated at genus resolution from broad COG (clusters of orthologous groups) categories, and the confirmatory null was robust to the contamination-index definition. [src: enigma_contamination_functional_potential] Exploratory coverage-aware and fraction-aware models gave positive defense associations, but most did not survive FDR (false discovery rate) correction, and within-fraction tests did not reproduce them. [src: enigma_contamination_functional_potential] The report treats the positive defense associations as exploratory, and their significance depends on coverage and covariate specification. [src: enigma_contamination_functional_potential] See also [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]] and [[entities/enigma]].

## Key Findings

### Confirmatory tests are null
The predeclared defense-score versus contamination Spearman tests were non-significant in both mapping modes. [src: enigma_contamination_functional_potential] In relaxed_all_clades, rho = 0.0587, 95% bootstrap CI (confidence interval) [-0.128, 0.250], p = 0.546, FDR q = 0.862. [src: enigma_contamination_functional_potential] In strict_single_clade, rho = 0.0682, 95% bootstrap CI [-0.111, 0.253], p = 0.483, FDR q = 0.849. [src: enigma_contamination_functional_potential]

The confirmatory endpoint was re-tested with four contamination index variants: composite all-metals (the primary index), uranium-only, Top-3 variance metals, and the PCA (principal component analysis) first component of metal z-scores. [src: enigma_contamination_functional_potential] All variants stayed non-significant after FDR in both mapping modes (q = 0.546 across the 8 tests), including uranium-only. [src: enigma_contamination_functional_potential] The report states that confirmatory evidence remains null and robust to index definition. [src: enigma_contamination_functional_potential]

### Exploratory adjusted models show positive defense associations
The report finds its strongest positive exploratory defense associations in coverage-aware adjustments. [src: enigma_contamination_functional_potential] The coverage-adjusted OLS (ordinary least squares) model includes contamination, depth, latitude, longitude and mapped_abundance_fraction. [src: enigma_contamination_functional_potential] These associations keep positive effect estimates but are attenuated under global multiple-testing control. [src: enigma_contamination_functional_potential]

- relaxed_all_clades: beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462. [src: enigma_contamination_functional_potential]
- strict_single_clade: beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, FDR q = 0.130. [src: enigma_contamination_functional_potential]

The fraction-aware model includes contamination, mapped_abundance_fraction and categorical community_fraction_type. [src: enigma_contamination_functional_potential]

- relaxed_all_clades: beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, FDR q = 0.0838. [src: enigma_contamination_functional_potential]
- strict_single_clade: beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, FDR q = 0.130. [src: enigma_contamination_functional_potential]

Only the relaxed coverage-adjusted model has q below 0.05. [src: enigma_contamination_functional_potential]

In the high-coverage subset (mapped_abundance_fraction >= 0.25), site_defense_score had Spearman p = 0.0207 (relaxed) and 0.00980 (strict). [src: enigma_contamination_functional_potential] These were non-significant after global FDR, with q = 0.301 (relaxed) and 0.189 (strict). [src: enigma_contamination_functional_potential]

The model diagnostics in model_results.tsv include confirmatory/exploratory labels, bootstrap CIs for key effect sizes, adjusted coordinates/depth models, coverage-adjusted models, site-structure models (location_prefix), fraction-aware models (community_fraction_type), within-fraction correlations, high-coverage subset correlations, and global BH-FDR (Benjamini-Hochberg false discovery rate) q-values across all reported p-values. [src: enigma_contamination_functional_potential]

### Fraction-stratified checks do not reproduce the signal
The notebook keeps community_fraction_type, parsed from sdt_community_name, to address possible confounding from collapsing community fractions. [src: enigma_contamination_functional_potential] Fraction-aware models use n = 212 sample-fraction rows, 106 for 0.2_micron_filter and 106 for 10_micron_filter. [src: enigma_contamination_functional_potential] Within-fraction defense Spearman tests were non-significant. [src: enigma_contamination_functional_potential] Relaxed p-values were 0.767 (0.2 micron) and 0.898 (10 micron). [src: enigma_contamination_functional_potential] Strict p-values were 0.780 (0.2 micron) and 0.793 (10 micron). [src: enigma_contamination_functional_potential] The report concludes that a strong monotonic defense signal is not robustly reproducible within individual fraction strata. [src: enigma_contamination_functional_potential]

### Non-defense outcomes
Most non-defense outcomes stayed non-significant in the sensitivity tests. [src: enigma_contamination_functional_potential] The one exploratory exception was strict_single_clade site_stress_score in the high-coverage subset: Spearman rho = 0.2489, p = 0.0407. [src: enigma_contamination_functional_potential]

### Species-proxy mode
The species_proxy_unique_genus mode keeps only genera that map to exactly one GTDB species clade, because ENIGMA taxonomy stops at genus. [src: enigma_contamination_functional_potential] This gave 150 unique-clade genera out of 530 mapped genera, and 380 ambiguous multi-clade genera. [src: enigma_contamination_functional_potential] Mean mapped abundance fraction was 0.031 in this mode, against 0.343 in strict/relaxed modes. [src: enigma_contamination_functional_potential] The site_defense_score trend was positive but non-significant (rho = 0.169, p = 0.081). [src: enigma_contamination_functional_potential] No high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25, because retained coverage was low. [src: enigma_contamination_functional_potential] The report suggests that, at current ENIGMA taxonomy granularity, stricter resolution sharply cuts analyzable signal without yet strengthening inference. [src: enigma_contamination_functional_potential]

### Taxonomy bridge
Upstream outputs had 1,392 observed genera, of which 530 mapped and 862 did not. [src: enigma_contamination_functional_potential] The genus-to-clade bridge table had 8,242 rows from many-to-many expansion. [src: enigma_contamination_functional_potential] The bridge has a long right tail, with a maximum of 433 clades per genus. [src: enigma_contamination_functional_potential] The most ambiguous genera were pseudomonas (433 clades), streptomyces (378), prevotella (358), streptococcus (214) and mycobacterium (186). [src: enigma_contamination_functional_potential] See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].

Functional features comprised 3,630 rows across 3 mapping modes: strict_single_clade, relaxed_all_clades and species_proxy_unique_genus. [src: enigma_contamination_functional_potential] Mean mapped abundance fraction was 0.343 in strict/relaxed modes (range 0.031 to 0.854) and 0.031 in species-proxy mode (range 0.0002 to 0.543). [src: enigma_contamination_functional_potential]

### Interpretation and relation to prior work
The report reads the genus-aggregated null Spearman results as consistent with contamination effects that do not collapse into one robust monotonic community-wide proxy. [src: enigma_contamination_functional_potential] It also says the null is compatible with contamination-driven taxonomic turnover that is functionally redundant, or too fine-scale (species, strain or pathway level) for the present mapping. [src: enigma_contamination_functional_potential] The report describes the pattern as detectable ecological differentiation with a weaker confirmatory monotonic response in broad functional summaries. [src: enigma_contamination_functional_potential]

The report describes Hemme et al. (2015; PMID: 26583008, PubMed identifier) as finding strong contamination-linked taxonomic restructuring and reduced functional breadth in stressed Oak Ridge groundwater communities, and says its result is directionally aligned with that work. [src: enigma_contamination_functional_potential] It describes Fan et al. (2025) as finding pronounced compositional shifts but only modest functional-diversity decline in a mixed waste-contaminated Oak Ridge aquifer, and calls its own result consistent with that. [src: enigma_contamination_functional_potential] Relative to Carlson et al. (2019; PMID: 30523276), the report extends taxa-abundance association to reproducible strict, relaxed and species-proxy bridge-aware functional sensitivity modeling, and quantifies where inference is coverage-limited. [src: enigma_contamination_functional_potential]

The report presents a reproducible ENIGMA-to-KBase Data Lakehouse functional inference workflow with independent strict-versus-relaxed features, mapped-coverage diagnostics, a species-proxy unique-clade sensitivity mode, and multi-tier modeling. [src: enigma_contamination_functional_potential]

## Data and Methods

NB01 extracted and QC (quality control)-filtered 108 samples that have both geochemistry and community composition. [src: enigma_contamination_functional_potential] The geochemistry matrix had shape (108, 49). [src: enigma_contamination_functional_potential] The overlap data had 41,711 community taxon rows, 212 distinct communities and 1,392 distinct genera. [src: enigma_contamination_functional_potential]

NB02 built a genus-normalized bridge to pangenome clades. [src: enigma_contamination_functional_potential] It parsed 27,690 GTDB species rows. [src: enigma_contamination_functional_potential] It mapped 530 genera and left 862 unmapped. [src: enigma_contamination_functional_potential] It had 530 strict clades and 7,380 relaxed clades. [src: enigma_contamination_functional_potential] The species-proxy mapping had 150 clades. [src: enigma_contamination_functional_potential] Functional features were computed independently for each mapping mode. [src: enigma_contamination_functional_potential]

NB03 built the contamination index from 8 metal columns (arsenic, cadmium, chromium, copper, lead, nickel, uranium, zinc). It used per-metal log1p z-scoring followed by a row-wise mean. [src: enigma_contamination_functional_potential] The report calls the index broad but right-skewed. [src: enigma_contamination_functional_potential] It covers n = 108 samples, with min = -0.448 and max = 3.836. [src: enigma_contamination_functional_potential] The median is -0.271 and the IQR is [-0.363, 0.053]. [src: enigma_contamination_functional_potential] NB03 produced 324 site functional score rows (108 samples x 3 mapping modes) and 12 model result rows (4 outcomes x 3 mapping modes). [src: enigma_contamination_functional_potential]

Data came from two collections. The enigma_coral collection (ddt_brick0000010, ddt_brick0000459, ddt_brick0000454, sdt_sample, sdt_community, sdt_location) supplies geochemistry, community composition, taxonomy linkage and sample metadata. [src: enigma_contamination_functional_potential] The kbase_ke_pangenome collection (gtdb_species_clade, pangenome, gene_cluster, eggnog_mapper_annotations) supplies the taxonomy bridge and COG-derived functional features. [src: enigma_contamination_functional_potential]

Sample sizes by mode:

| Mode | Base Spearman | Adj+Cov | Adj+Fraction | High-coverage |
|---|---|---|---|---|
| relaxed_all_clades | 108 | 108 | 212 (sample-fraction rows) | 68 [src: enigma_contamination_functional_potential] |
| strict_single_clade | 108 | 108 | 212 (sample-fraction rows) | 68 [src: enigma_contamination_functional_potential] |
| species_proxy_unique_genus | 108 | 108 | 212 (sample-fraction rows) | 1 [src: enigma_contamination_functional_potential] |

## Caveats and Open Work

Coverage-aware models raise the effective rows at fraction level. Species-proxy high-coverage tests are underpowered (n=1). [src: enigma_contamination_functional_potential] Species-proxy mode retained too little coverage for a high-coverage test. [src: enigma_contamination_functional_potential] The positive adjusted associations are exploratory. Most have FDR q above 0.05, and the within-fraction tests did not reproduce them. [src: enigma_contamination_functional_potential] Exploratory sensitivity-model significance is concentrated in defense and depends on coverage/covariate specification. Broader effects across outcomes are not established. [src: enigma_contamination_functional_potential] The stress-score result (p = 0.0407) is a single exploratory exception among mostly null outcomes. [src: enigma_contamination_functional_potential] The report suggests that finer taxonomic resolution does not yet strengthen inference. [src: enigma_contamination_functional_potential]

Other limits the report states:
- The ENIGMA taxonomy table ddt_brick0000454 gives labels only through Genus, so true species-level bridge testing is not possible in this slice. [src: enigma_contamination_functional_potential]
- Genus-level mapping may mask strain-level adaptation. [src: enigma_contamination_functional_potential]
- 862/1,392 observed genera were unmapped to the current pangenome bridge. [src: enigma_contamination_functional_potential]
- COG-fraction proxies are coarse summaries, not curated resistance pathways. [src: enigma_contamination_functional_potential]
- The bridge and annotation stack depends on GTDB and eggNOG conventions, and at genus level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]
- Site structure is represented by coarse location_prefix effects, not full hierarchical or random-effects modeling. [src: enigma_contamination_functional_potential]

Next analyses the report proposes:
1. Replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries. [src: enigma_contamination_functional_potential]
2. Increase taxonomic resolution (species/strain-level bridge from metagenomic or higher-resolution ENIGMA taxonomy) and quantify gains over genus and species-proxy modes. [src: enigma_contamination_functional_potential]
3. Fit adjusted models with explicit depth, location cluster and sampling date covariates and compositional modeling controls. [src: enigma_contamination_functional_potential]
4. Investigate the contribution of unmapped genera to contamination gradients and bridge expansion opportunities. [src: enigma_contamination_functional_potential]
5. Add mixed-effects or hierarchical site models with well/location-level random effects to test whether defense associations persist under richer structure control. [src: enigma_contamination_functional_potential]

## Slots Into

- [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]]: the confirmatory defense-versus-contamination tests were null across all index variants. [src: enigma_contamination_functional_potential]
- [[concepts/robustness-of-exploratory-associations-to-coverage-fraction-and-site-covariate-specification]]: positive defense associations appear under coverage-aware adjustment and fraction-aware adjustment, but a strong monotonic signal is not robustly reproducible within fraction strata. [src: enigma_contamination_functional_potential]
- [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]]: only 530 of 1,392 genera mapped, and 380 genera were ambiguous. [src: enigma_contamination_functional_potential]
- [[concepts/coarse-cog-fraction-proxies-versus-pathway-level-stress-evidence]]: COG-fraction proxies are coarse and may dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]
