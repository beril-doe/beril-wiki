<!-- tension-hash: cbe9a89c1da0e2bd -->
# Model support versus phenotype and ecological evidence — when does agreement establish function?

The [[concepts/metabolic-model-gapfilling]] record brings together disagreements about whether model predictions, gene-disruption phenotypes, conservation, and community-scale observations measure the same biological properties. The tension matters because high agreement in one organism or endpoint can coexist with modest accuracy, unexplained growth defects, incomplete coverage, and ecological signals that do not establish flux or metabolite exchange.

## Evidence Sides

**Model concordance and support.** FBA/TnSeq concordance was 73.8% for 866 genes [src: acinetobacter_adp1_explorer], and FW300-N2E3 showed GapMind 13/13 and Fitness Browser 21/21 concordance [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]. FBA also predicted Complex I routing of NADH, zero NDH-2 and ACIAD3522 flux, and 1.76× higher Complex I flux in the aromatic analysis [src: respiratory_chain_wiring, aromatic_catabolism_network].

**Accuracy and phenotype challenge.** Baseline FBA accuracy was 42.5% with 330 false positives [src: annotation_gap_discovery]. The same evidence base reports moderate FBA/knockout concordance and a null association between FBA class and growth defects within TnSeq-dispensable genes [src: adp1_triple_essentiality]. Against the respiratory predictions, Complex I ratios were 0.37 on quinate and 1.44 on glucose, while ACIAD3522 growth was 0.013 on acetate [src: respiratory_chain_wiring]. The aromatic analysis found 10/13 operon-subunit growth defects; ACIAD3522 ratios were 0.013 on acetate and 1.39 on quinate and glucose [src: aromatic_catabolism_network, discoveries]. The cross-species NDH-2 compensation hypothesis was not supported after annotation correction: Complex I aromatic deficits were −0.297 with validated NDH-2 versus −0.156 without, p = 0.52 [src: discoveries].

**Coverage, conservation, and dependency challenge.** 19 production-to-Fitness-Browser matches lacked consumption actions in the 2018 snapshot, while BacDive showed only 3/7 concordance [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]. Active-versus-latent conservation was non-significant (p = 0.94), although latent rate correlated with openness (ρ = 0.69, p = 0.0004, n = 22), and variable pathway count correlated with openness at partial rho=0.530, p=2.83e-203 [src: metabolic_capability_dependency, pathway_capability_dependency]. Latent fractions were 41.0%, 35.4%, and 15.8% in different analyses [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency].

**Ecological and complementarity challenge.** All 33 Freshwater samples lacked paired metabolomics, and abiotic covariates were unavailable [src: nmdc_community_metabolic_ecology]. Implicated genera appeared in 83/86 genera across 1,719 NMDC metagenomes [src: enigma_carbon_census_1]. Corrected complementarity was d ≈ −0.4 and prevalence-weighted d = −0.39, versus the original d = −7.54 [src: plant_microbiome_ecotypes].

## Possible Reconciliations

- **Hypothesis—measurement:** FBA, TnSeq, knockout growth, production, utilization, dependency, and flux may be distinct endpoints.
- **Hypothesis—scope:** Organism, medium mapping, endpoint, and gene set differences may explain the 73.8% versus 42.5% results.
- **Hypothesis—latent function:** Conservation or openness may predict capability without predicting current activity.
- **Hypothesis—ecological limitation:** Occurrence and community associations may indicate potential without establishing degradation, individual flux, or metabolite exchange.

## Resolving Work

- Re-run matched-gene FBA/TnSeq comparisons using the same medium, knockout definition, FBA class, and continuous growth endpoint; test whether concordance changes.
- Harmonize organisms, media mappings, annotations, and accuracy definitions; test whether the 42.5% baseline and 330 false positives persist.
- Measure substrate-specific flux and growth for NDH-2 and ACIAD3522 on acetate, quinate, and glucose; test the predicted routing and compensation mechanisms.
- Pair metagenomes with metabolomics and abiotic covariates in Freshwater samples; test whether negative completeness–metabolite associations reflect flux.
- Recompute complementarity with raw pair-level permutation values and validate exchange experimentally; test whether corrected genus-pair effects predict metabolite transfer.
