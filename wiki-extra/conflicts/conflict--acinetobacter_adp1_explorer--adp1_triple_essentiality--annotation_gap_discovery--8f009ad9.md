---
title: Model Predictions Versus Phenotypic and Ecological Evidence
type: Conflict
sources:
- id: acinetobacter_adp1_explorer
  resource: ../../wiki/summaries/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
- id: adp1_triple_essentiality
  resource: ../../wiki/summaries/adp1_triple_essentiality__REPORT.md
  title: adp1 triple essentiality
- id: webofmicrobes_explorer
  resource: ../../wiki/summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
- id: discoveries
  resource: ../../wiki/summaries/discoveries.md
  title: discoveries
- id: fw300_metabolic_consistency
  resource: ../../wiki/summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: annotation_gap_discovery
  resource: ../../wiki/summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: respiratory_chain_wiring
  resource: ../../wiki/summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
- id: aromatic_catabolism_network
  resource: ../../wiki/summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: metabolic_capability_dependency
  resource: ../../wiki/summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: pathway_capability_dependency
  resource: ../../wiki/summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: nmdc_community_metabolic_ecology
  resource: ../../wiki/summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
- id: enigma_carbon_census_1
  resource: ../../wiki/summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
- id: plant_microbiome_ecotypes
  resource: ../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
---
<!-- tension-hash: 20239306e157e1cd -->
# Model Predictions Versus Phenotypic and Ecological Evidence

[metabolic-model-gapfilling](../../wiki/concepts/metabolic-model-gapfilling.md) records a recurring disagreement over what metabolic models can establish. Some analyses report substantial agreement between FBA predictions and observed gene or growth phenotypes, while others find low baseline accuracy, unexplained false positives, or mismatches between predicted flux and respiratory defects. The same tension extends to conservation, metabolite use, and community-scale evidence: model support, capability, dependency, occurrence, production, and activity are not interchangeable endpoints.

## Evidence Sides

**Models often agree with measured phenotypes.** The 73.8% FBA/TnSeq concordance for 866 genes [^acinetobacter_adp1_explorer] sits alongside moderate FBA/knockout concordance [^adp1_triple_essentiality]. In FW300-N2E3, GapMind showed 13/13 and Fitness Browser 21/21 concordance, although BacDive showed only 3/7 [^webofmicrobes_explorer][^discoveries][^fw300_metabolic_consistency]. These results support useful model or annotation agreement in particular organisms, media, and endpoints.

**Broader evaluations and targeted respiratory analyses show substantial disagreement.** Baseline FBA accuracy was 42.5%, with 330 false positives [^annotation_gap_discovery]. In the respiratory analysis, FBA routed NADH through Complex I and predicted zero NDH-2 and ACIAD3522 flux, while Complex I ratios were 0.37 on quinate and 1.44 on glucose, and ACIAD3522 growth was 0.013 on acetate [^respiratory_chain_wiring]. The aromatic analysis found 1.76× higher Complex I flux but 10/13 operon-subunit growth defects [^aromatic_catabolism_network]. ACIAD3522 ratios were 0.013 on acetate and 1.39 on quinate and glucose, while the cross-species NDH-2 compensation hypothesis was not supported after annotation correction: Complex I aromatic deficits were −0.297 with validated NDH-2 versus −0.156 without, p = 0.52 [^discoveries].

**Conservation and ecological signals do not cleanly validate dependency or activity.** Active-versus-latent conservation was non-significant (p = 0.94), although latent rate correlated with openness (ρ = 0.69, p = 0.0004, n = 22), and variable pathway count correlated with openness at partial rho=0.530, p=2.83e-203 [^metabolic_capability_dependency][^pathway_capability_dependency]. The NMDC signal lacked paired metabolomics in all 33 Freshwater samples, while implicated genera occurred in 83/86 genera across 1,719 NMDC metagenomes [^nmdc_community_metabolic_ecology][^enigma_carbon_census_1]. Corrected plant complementarity was weakly negative (d ≈ −0.4; prevalence-weighted d = −0.39), not the original d = −7.54 [^plant_microbiome_ecotypes].

## Possible Reconciliations

- **Hypothesis—endpoint differences:** production, capability, utilization, dependency, flux, growth defects, and occurrence may measure different biological processes. The 19 production-to-Fitness-Browser matches lacking consumption actions in the 2018 snapshot therefore need not contradict model support [^webofmicrobes_explorer][^discoveries].
- **Hypothesis—scope and harmonization:** the 42.5% baseline result and the 73.8% ADP1 result may differ because organisms, media mappings, gene sets, knockout definitions, and endpoints differ [^annotation_gap_discovery][^acinetobacter_adp1_explorer].
- **Hypothesis—latent capacity:** models may represent potential pathways without demonstrating realized flux, exchange, or growth dependence; the 41.0%, 35.4%, and 15.8% latent fractions must not be averaged [^discoveries][^pathway_capability_dependency][^metabolic_capability_dependency].

## Resolving Work

- Re-run matched-gene comparisons using the same medium, knockout definition, FBA class, and continuous growth endpoint to test whether concordance remains.
- Harmonize organism annotations, media mappings, and simulation constraints across the 42.5% and 73.8% evaluations, then compare accuracy and false positives.
- Measure respiratory flux, NDH-2 activity, ACIAD3522 function, and growth on acetate, quinate, and glucose to test the proposed NADH-capacity explanation.
- Pair NMDC metagenomes with metabolomics and abiotic covariates, asking whether completeness associations predict measured metabolites or flux.
- Test plant metabolite exchange with compartment-resolved metabolomics and validated pathway completeness rather than occurrence or complementarity alone.

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../../wiki/summaries/acinetobacter_adp1_explorer__REPORT.md)
[^adp1_triple_essentiality]: [adp1 triple essentiality](../../wiki/summaries/adp1_triple_essentiality__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../../wiki/summaries/webofmicrobes_explorer__REPORT.md)
[^discoveries]: [discoveries](../../wiki/summaries/discoveries.md)
[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../../wiki/summaries/fw300_metabolic_consistency__REPORT.md)
[^annotation_gap_discovery]: [annotation gap discovery](../../wiki/summaries/annotation_gap_discovery__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../../wiki/summaries/respiratory_chain_wiring__REPORT.md)
[^aromatic_catabolism_network]: [aromatic catabolism network](../../wiki/summaries/aromatic_catabolism_network__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../../wiki/summaries/metabolic_capability_dependency__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../../wiki/summaries/pathway_capability_dependency__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../../wiki/summaries/nmdc_community_metabolic_ecology__REPORT.md)
[^enigma_carbon_census_1]: [enigma carbon census 1](../../wiki/summaries/enigma_carbon_census_1__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md)
