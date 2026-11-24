---
type: "Concept"
description: "Whether contaminant or measured metal gradients shift community stress-related functional potential, including sensitivity to contamination index construction; observational only."
sources: ["summaries/discoveries.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Contamination and metal gradients as drivers of community functional potential

This page asks whether contamination or measured metal gradients shift community stress-related functional potential. All evidence is observational. In the ENIGMA subset, confirmatory tests were null and did not depend on how the contamination index was built. Exploratory coverage-aware defense associations were positive but weakened under global multiple-testing control. A soil analysis and a groundwater analysis report stronger metal-function links, but the soil work is preliminary. [src: enigma_contamination_functional_potential, soil_metal_functional_genomics]

## ENIGMA confirmatory tests: null and robust to index definition

Within the [[entities/enigma]] subset, contamination gradients did not produce a robust community-level shift in inferred stress-related functional potential. Features were aggregated at genus resolution from broad COG (clusters of orthologous groups) categories. [src: enigma_contamination_functional_potential] Primary univariate associations were non-significant for defense, stress, metabolism and mobilome outcomes in both mapping modes, with 108 overlap samples. [src: discoveries]

The index used 8 metal columns: arsenic, cadmium, chromium, copper, lead, nickel, uranium and zinc. Each was log1p z-scored, and the row-wise mean was taken. [src: enigma_contamination_functional_potential] It covered n = 108 samples and ranged from -0.448 to 3.836. [src: enigma_contamination_functional_potential] Its median was -0.271 (IQR [-0.363, 0.053]). [src: enigma_contamination_functional_potential] The report calls it broad but right-skewed. [src: enigma_contamination_functional_potential]

The predeclared [[entities/spearman-rank-correlation]] tests of defense score against contamination were non-significant:
- relaxed_all_clades: rho = 0.0587, 95% bootstrap CI [-0.128, 0.250], p = 0.546, FDR (false discovery rate) q = 0.862. [src: enigma_contamination_functional_potential]
- strict_single_clade: rho = 0.0682, 95% bootstrap CI [-0.111, 0.253], p = 0.483, q = 0.849. [src: enigma_contamination_functional_potential]

### Sensitivity to index construction

The confirmatory endpoint was re-tested with four index variants: composite all-metals, uranium-only, Top-3 variance metals, and the first component of a PCA (principal component analysis) of metal z-scores. [src: enigma_contamination_functional_potential] Across both mapping modes, all variants stayed non-significant after FDR (q = 0.546 across the 8 confirmatory-variant tests), including uranium-only. [src: enigma_contamination_functional_potential] The report concludes that the confirmatory evidence is null and robust to index definition. [src: enigma_contamination_functional_potential]

## Exploratory coverage-aware defense signal

Adding mapped-coverage-aware models made the contamination-defense association nominally significant. Coverage-adjusted OLS (ordinary least squares) gave contamination p = 3.98e-4 (relaxed) and 3.54e-3 (strict). [src: discoveries] The high-coverage subset gave Spearman p = 0.0207 (relaxed) and 0.0098 (strict). [src: discoveries, enigma_contamination_functional_potential] The report finds its strongest positive defense associations in these coverage-aware adjustments. [src: enigma_contamination_functional_potential] The [[entities/ordinary-least-squares-sensitivity-models]] had positive effect estimates:

- Coverage-adjusted OLS, relaxed_all_clades: beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462. [src: enigma_contamination_functional_potential]
- Coverage-adjusted OLS, strict_single_clade: beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, q = 0.130. [src: enigma_contamination_functional_potential]
- Fraction-aware adjusted, relaxed_all_clades: beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, q = 0.0838. [src: enigma_contamination_functional_potential]
- Fraction-aware adjusted, strict_single_clade: beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, q = 0.130. [src: enigma_contamination_functional_potential]

These results limit one another. The high-coverage defense-score associations were non-significant after global FDR (q = 0.301 relaxed, 0.189 strict). [src: enigma_contamination_functional_potential] Within individual community-fraction strata the defense tests were non-significant. The p-values were 0.767 (0.2 micron) and 0.898 (10 micron) for relaxed, and 0.780 and 0.793 for strict. [src: enigma_contamination_functional_potential] The report concludes that a strong monotonic defense signal is not robustly reproducible within fraction strata. [src: enigma_contamination_functional_potential] The report describes the effects as persisting with positive estimates but attenuated under global multiple-testing control. [src: enigma_contamination_functional_potential] See [[concepts/robustness-of-exploratory-associations-to-coverage-fraction-and-site-covariate-specification]].

Significance in these models is concentrated in defense and depends on coverage and covariate specification. A broader effect across outcomes is not established. [src: enigma_contamination_functional_potential] Most non-defense outcomes stayed non-significant. [src: enigma_contamination_functional_potential] One exploratory exception was the strict_single_clade high-coverage site_stress_score test (Spearman rho = 0.2489, p = 0.0407). [src: enigma_contamination_functional_potential]

### Interpretation offered

The null is compatible with contamination-driven taxonomic turnover that is functionally redundant, or with effects at species, strain or pathway level that the mapping is too coarse to see. [src: enigma_contamination_functional_potential] The report also says contamination effects may not collapse into one monotonic community-wide proxy. [src: enigma_contamination_functional_potential] It reads the pattern as detectable ecological differentiation with a weaker confirmatory monotonic response in broad functional summaries. [src: enigma_contamination_functional_potential] See [[concepts/coarse-cog-fraction-proxies-versus-pathway-level-stress-evidence]].

The report relates this to earlier work:
- Hemme et al. (2015; PMID: 26583008, PubMed identifier) reported strong contamination-linked taxonomic restructuring and reduced functional breadth in stressed Oak Ridge groundwater communities. [src: enigma_contamination_functional_potential]
- Fan et al. (2025) reported pronounced compositional shifts but only modest functional-diversity decline in a mixed waste-contaminated Oak Ridge aquifer. [src: enigma_contamination_functional_potential]
- Relative to Carlson et al. (2019; PMID: 30523276), the report extends taxa-abundance association to bridge-aware functional sensitivity modeling. It covers strict, relaxed and species-proxy modes and quantifies where inference is coverage-limited. [src: enigma_contamination_functional_potential]

## Other lines of evidence: groundwater and soil

In ENIGMA Track B, community-weighted mean (CWM) metal-type diversity was significantly higher in plume wells FW215/FW216 (Kruskal-Wallis p = 0.0001). [src: microbeatlas_metal_ecology] Both wells are known to lie within the U/NO₃ contamination plume at ORFRC (Oak Ridge Field Research Center). The report reads the higher CWM as consistent with metal-contaminated environments selecting genera with broader metal resistance repertoires. [src: microbeatlas_metal_ecology] See [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater]].

The soil analysis is preliminary. Spearman, db-RDA and PGLS analyses are complete, but effect-size and spatial validation and the figures are pending. [src: soil_metal_functional_genomics] It found 2,355 significant COG-metal associations (FDR < 0.05) across 9 metals in 51,748 soil samples. [src: soil_metal_functional_genomics] Chromium and lead drive the strongest signals. [src: soil_metal_functional_genomics] Transporters (ABC, ATP-binding cassette, and RND) and biosynthesis genes dominate the top hits. [src: soil_metal_functional_genomics]

The soil db-RDA gave R² = 0.799, p = 0.005 (999 permutations). The report describes this as metal concentrations explaining 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics] It argues the link is not a batch artefact because project accession was conditioned out. [src: soil_metal_functional_genomics] Biome-stratified PGLS shows distinct metal-COG relationships in soil, marine and wastewater. The report reads this as environment-specific responses, not a universal resistance programme. [src: soil_metal_functional_genomics] See [[entities/phylogenetic-generalized-least-squares]].

The copper-specific analysis found 116 COGs at FDR < 0.05, using 7,566 samples with nearby KBase genomes at 10 km. [src: soil_metal_functional_genomics] Top positives include cell division and nucleotide transport (BQ, FQ, FK, CF). [src: soil_metal_functional_genomics] Top negatives include energy production (DI, CE), which suggests energetic trade-offs under copper stress. [src: soil_metal_functional_genomics] The report calls this direction consistent with known copper toxicity mechanisms. [src: soil_metal_functional_genomics] All these associations are observational. [src: soil_metal_functional_genomics] See [[concepts/co-contamination-and-multiple-testing-confounding-in-metal-function-associations]].

## Open Directions

- Run the ENIGMA confirmatory tests at pathway or gene level, not broad COG categories. This would test whether the genus-level null reflects coarse mapping.
- Repeat the coverage-aware defense models on a larger set of samples with high mapped-abundance fraction. This would show whether the signal survives global FDR control.
- Run the soil metal-function analysis with individual metals, covariates for co-occurring metals, and the pending spatial validation. This would test whether the strong soil signal is specific to one metal.
- Apply the ENIGMA index variants to the plume-well CWM metal-diversity contrast. This would test whether plume status and measured metal gradients give the same signal.
