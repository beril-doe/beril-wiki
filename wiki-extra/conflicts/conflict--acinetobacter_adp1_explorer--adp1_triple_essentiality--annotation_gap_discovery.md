<!-- tension-hash: 79dd08651c569825 -->
# Do metabolic models predict active, condition-specific metabolism?

The evidence from [[concepts/metabolic-model-gapfilling]] supports a real disagreement over what agreement with genomic, fitness, and environmental data means. Some analyses treat concordance, pathway conservation, and broad occurrence as evidence that models capture metabolic capability. Others find that these signals do not establish active flux, physiological use, or condition-specific dependency, especially when datasets, endpoints, and gene sets differ.

## Evidence Sides

**Model concordance and conservation support**

FBA achieved 73.8% FBA/TnSeq concordance in an 866-gene overlap [src: acinetobacter_adp1_explorer], while the FW300-N2E3 analysis found 13/13 GapMind–Fitness Browser and 21/21 Fitness Browser concordances [src: discoveries, fw300_metabolic_consistency]. The Carbon Census detected implicated genera in 83/86 genera across 1719 NMDC metagenomes [src: enigma_carbon_census_1], and pathway-level conservation supports retaining pathways in models even when condition-specific dependence is unproven [src: metabolic_capability_dependency]. Latent-capability rate also correlated with pangenome openness (ρ = 0.69, p = 0.0004, n = 22) [src: metabolic_capability_dependency].

**Endpoint, condition, and dependency challenges**

Other results weaken the interpretation that model agreement or conservation demonstrates active metabolism. Baseline FBA accuracy was 42.5% with 330 false positives [src: annotation_gap_discovery], and FBA class had a null association with growth defects within TnSeq-dispensable genes alongside only moderate FBA/knockout concordance [src: adp1_triple_essentiality]. BacDive utilization was 3/7, and tryptophan was 0+/50− despite production, complete biosynthesis, and significant fitness effects [src: fw300_metabolic_consistency]. WoM recorded 19 production-to-Fitness-Browser matches but no organism consumption or decrease action in the 2018 snapshot [src: webofmicrobes_explorer]. Conservation did not distinguish latent capabilities from active dependencies (p = 0.94) [src: metabolic_capability_dependency]. Reported latent fractions were 41.0% of 161 pairs, 35.4%, and 15.8% of 1,695 complete pairs [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]. Environmental occurrence likewise measured presence rather than degradation or activity [src: enigma_carbon_census_1].

## Possible Reconciliations

- **Hypothesis—measurement:** production, biosynthetic capability, utilization, dependency, flux, and fitness are distinct endpoints; a metabolite can be produced without being consumed or required.
- **Hypothesis—scope:** the 73.8% and 42.5% FBA results use different organisms, media mappings, gene sets, and endpoints.
- **Hypothesis—condition dependence:** standard-media FBA may miss alternative respiratory roles; Complex I and ACIAD3522 showed condition-specific effects, including Complex I growth ratios of 0.37 on quinate and 1.44 on glucose and ACIAD3522 growth of 0.013 on acetate [src: respiratory_chain_wiring].
- **Hypothesis—classification:** the differing latent fractions reflect organism coverage, pathway sets, thresholds, membership mapping, and procedures rather than biological disagreement.

## Resolving Work

- Run matched-gene FBA/TnSeq comparisons using the same medium, knockout definition, FBA class, and continuous growth endpoint.
- Update WoM/GNPS2 with consumption actions, matched strain identities, measured uptake, and condition-matched Fitness Browser assays.
- Measure ADP1 NDH-2 deletions, NADH/NAD⁺ by carbon source, ACIAD3522 function, and enzyme-capacity-constrained respiratory flux.
- Harmonize pathway sets, organism coverage, thresholds, and membership mapping across the three latent-fraction analyses.
- Pair metagenomes or metatranscriptomes with compound concentrations, uptake, and growth to distinguish occurrence from active metabolism.
