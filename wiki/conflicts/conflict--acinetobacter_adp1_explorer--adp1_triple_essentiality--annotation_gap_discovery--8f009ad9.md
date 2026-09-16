<!-- tension-hash: cbe9a89c1da0e2bd -->
# Encoded Capability Versus Measured Dependency: When Models and Genomes Disagree With Fitness Data

Across the corpus, one recurring fault line separates what a genome or a model says an organism *can* do from what fitness experiments show the organism *needs*. On [[concepts/metabolic-model-gapfilling]] this fault line surfaces as six distinct disagreements, all recorded here: (1) how accurate flux balance analysis (FBA — a constraint-based method that predicts feasible steady-state flux distributions from a stoichiometric model) actually is against gene-level phenotype data; (2) whether cross-database metabolite evidence supports or undercuts model-derived capability calls; (3) whether FBA's respiratory routing is refuted by ADP1 growth ratios; (4) whether increased predicted aromatic flux is compatible with complex-level essentiality and with a failed cross-species compensation test; (5) whether pathway conservation and pangenome openness tell the same story about latent capability; and (6) whether community-scale and plant-microbiome association signals license claims about metabolite exchange. None of these is a clean "one side is wrong" case: in most, the two sides measure different endpoints, on different organisms, in different media. That is exactly why they must not be averaged into a single reliability number for gapfilled models.

## Evidence Sides

### 1. FBA concordance with gene-level phenotype: high, moderate, or poor?

**Side A — FBA agrees with TnSeq at scale in ADP1.** The ADP1 analysis reports 73.8% FBA/TnSeq concordance for 866 genes, drawn from a single well-characterized organism with transposon-sequencing (TnSeq) fitness data. [src: acinetobacter_adp1_explorer]

**Side B — agreement is only moderate, and vanishes inside the dispensable set.** The triple-essentiality analysis reports moderate FBA/knockout concordance and a null association between FBA class and growth defects within TnSeq-dispensable genes — i.e. among genes TnSeq calls dispensable, knowing the FBA class tells you nothing about whether a clean deletion grows poorly. [src: adp1_triple_essentiality]

**Side C — baseline FBA accuracy is poor and false-positive-dominated.** The annotation-gap work reports 42.5% baseline FBA accuracy with 330 false positives, a far weaker picture than either ADP1 figure. [src: annotation_gap_discovery]

The endpoints and gene sets differ between A and B, so matched-gene comparisons using the same medium, knockout definition, FBA class, and continuous growth endpoint are needed. [src: acinetobacter_adp1_explorer, adp1_triple_essentiality] Between A and C the organisms, media mappings, and endpoints differ, and harmonized simulations are required; the 73.8% concordance therefore does not erase the broader accuracy result. [src: acinetobacter_adp1_explorer, annotation_gap_discovery]

### 2. Metabolite-level evidence: coverage gap or model support?

**Side A — model-adjacent evidence is internally consistent where it can be tested.** FW300-N2E3 showed GapMind (a homology-based pathway-completeness tool) 13/13 and Fitness Browser 21/21 concordance. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]

**Side B — the evidence base is thin and endpoint-mismatched.** In the same comparison BacDive supported only 3/7, and 19 production-to-Fitness-Browser matches lacked consumption actions in the 2018 snapshot. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency] Production, capability, utilization, dependency, and flux remain distinct endpoints, so a high concordance count in one endpoint does not transfer to another. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]

### 3. Respiratory routing: FBA's Complex I monopoly versus ADP1 growth ratios

**Side A — FBA's prediction is contradicted by the phenotype pattern.** FBA routed NADH through Complex I and predicted zero NDH-2 and ACIAD3522 flux, yet Complex I growth ratios were 0.37 on quinate and 1.44 on glucose, and ACIAD3522 growth was 0.013 on acetate — a near-lethal defect in a gene the model assigns no flux. [src: respiratory_chain_wiring]

**Side B — this does not establish that FBA is incorrect.** NDH-2 lacks growth data, ACIAD3522 may have another function, and the NADH-capacity explanation offered to reconcile the pattern is theoretical. [src: respiratory_chain_wiring]

### 4. Aromatic catabolism: more predicted flux, more knockout defects

**Side A — higher predicted flux coexists with complex-level essentiality.** The aromatic analysis found 1.76× higher Complex I flux but 10/13 operon-subunit growth defects. [src: aromatic_catabolism_network]

**Side B — the defect pattern does not track the substrate the model implicates.** Transferred defects were strongest on acetate and succinate rather than exclusively aromatic substrates; ACIAD3522 ratios were 0.013 on acetate and 1.39 on quinate and glucose; and the cross-species NDH-2 compensation hypothesis was not supported after annotation correction (Complex I aromatic deficits −0.297 with validated NDH-2 versus −0.156 without, p = 0.52). [src: discoveries]

### 5. Conservation versus openness as evidence for latent capability

**Side A — conservation does not distinguish active from latent pathways.** Active-versus-latent conservation was non-significant (p = 0.94). [src: metabolic_capability_dependency]

**Side B — pangenome dynamics do track latency.** Latent rate correlated with pangenome openness (ρ = 0.69, p = 0.0004, n = 22), and variable pathway count correlated with openness at partial rho = 0.530, p = 2.83e-203. [src: metabolic_capability_dependency, pathway_capability_dependency]

**Scale disagreement.** Separate analyses report latent fractions of 41.0%, 35.4%, and 15.8%; these come from different analyses and must not be averaged. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]

### 6. Community and host-associated signals versus metabolite exchange

**Side A — community-scale associations exist.** The NMDC negative completeness–metabolite associations suggest a community-scale signal. [src: nmdc_community_metabolic_ecology] The ENIGMA Carbon Census found broad occurrence: implicated genera appeared in 83/86 genera across 1,719 NMDC metagenomes. [src: enigma_carbon_census_1]

**Side B — neither establishes flux, causality, or degradation.** All 33 Freshwater samples lacked paired metabolomics and abiotic covariates were unavailable, so individual flux and causality are not established. [src: nmdc_community_metabolic_ecology] The Carbon Census measured occurrence rather than degradation or activity. [src: enigma_carbon_census_1]

**Side C — a corrected effect size contradicts the published magnitude.** Corrected genus-pair analysis found weakly negative complementarity (d ≈ −0.4; prevalence-weighted d = −0.39), whereas the original analysis reported d = −7.54 because it divided by the standard deviation of permutation means rather than raw pair-level values. [src: plant_microbiome_ecotypes]

**Side D — even the corrected result does not demonstrate exchange.** 62/322 genera (19.3%) were lost from the NMDC bridge, the C-score co-occurrence test found 0 PGP-dominant (plant growth-promoting), 3 pathogen-dominant, and 66 dual-or-mixed genera, and core-level GapMind completeness was 0% across compartments. [src: plant_microbiome_ecotypes]

## Possible Reconciliations

These are hypotheses, not findings.

**Denominator and endpoint mismatch (disagreements 1, 2).** *Hypothesis:* the 73.8% and 42.5% figures do not share a denominator, so neither confirms nor refutes the other arithmetically. The 73.8% figure is a gene-level agreement between FBA class and TnSeq fitness calls in one organism [src: acinetobacter_adp1_explorer]; the 42.5% accuracy figure, reported with 330 false positives, comes from a different study whose organisms, media mappings, and endpoints differ [src: annotation_gap_discovery, acinetobacter_adp1_explorer]. Until the two are recomputed on a common footing, the tension may be entirely an artifact of what each number counts. A second, testable hypothesis operates *within* the gene-level comparison: FBA agreement may be high for the essential/strongly-deleterious tail and near-chance in the middle, of which the null association within TnSeq-dispensable genes would be the direct prediction. [src: adp1_triple_essentiality]

**Definitional mismatch across knockout types (disagreement 1).** *Hypothesis:* transposon insertion (TnSeq) and complete-gene deletion measure different things — polar effects, partial function, and pooled-versus-clonal competition — so "concordance" computed against each is not the same quantity. [src: acinetobacter_adp1_explorer, adp1_triple_essentiality]

**Database endpoint semantics (disagreement 2).** *Hypothesis:* the BacDive 3/7 shortfall reflects curated growth-condition coverage rather than a biological contradiction, while the 19 unmatched production events reflect an asymmetry between what a 2018 snapshot records as produced and what any database records as consumed. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]

**Capacity versus optimality in respiration (disagreements 3, 4).** *Hypothesis:* FBA optimizes yield and therefore selects the proton-pumping route, while the measured defects report rate or capacity limits that an optimality objective does not encode; both could be right if the objective, not the network, is the mismatch. Note that the report itself labels this NADH-capacity explanation theoretical. [src: respiratory_chain_wiring] A competing hypothesis for ACIAD3522's 0.013 acetate ratio is a non-respiratory function, which would remove it from the model's remit entirely. [src: respiratory_chain_wiring] The failure of the cross-species compensation test (−0.297 vs −0.156, p = 0.52) is consistent with the ADP1 wiring being species-specific rather than a general rule. [src: discoveries]

**Level-of-analysis mismatch (disagreement 5).** *Hypothesis:* conservation is measured per pathway across genomes and openness per clade, so a null at the pathway level (p = 0.94) and a positive at the clade level (ρ = 0.69, p = 0.0004, n = 22) can coexist without contradiction — the signal lives in genome dynamics, not in per-pathway retention. [src: metabolic_capability_dependency] The divergent latent fractions (41.0%, 35.4%, 15.8%) are then denominator artifacts of different pathway-organism universes and thresholds, which is why they must not be averaged. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]

**Occurrence-to-activity gap (disagreement 6).** *Hypothesis:* the association and occurrence signals are real but index community composition, not exchange; the corrected d ≈ −0.4 / −0.39 is the honest effect size, and the 0% core-level GapMind completeness plus 19.3% genus loss set an evidence ceiling that no reanalysis of the same tables can lift. [src: plant_microbiome_ecotypes, nmdc_community_metabolic_ecology, enigma_carbon_census_1]

## Resolving Work

**1. FBA concordance.**
- Recompute concordance on a matched gene set for ADP1 using one medium, one knockout definition, one FBA class assignment, and one continuous growth endpoint, then report 73.8% and the moderate knockout concordance on that common footing. [src: acinetobacter_adp1_explorer, adp1_triple_essentiality]
- Stratify concordance by fitness-effect magnitude to test whether accuracy collapses in the dispensable middle, as the null association within TnSeq-dispensable genes predicts. [src: adp1_triple_essentiality]
- State explicitly what each accuracy figure is computed over, so the 42.5% result and the 73.8% result are compared only if they share a denominator. [src: annotation_gap_discovery, acinetobacter_adp1_explorer]
- Rerun the 42.5%-accuracy pipeline with the ADP1 media mapping and endpoint definition to determine how much of the gap is organism versus protocol, and audit the 330 false positives by whether the offending reaction was gapfilled. [src: annotation_gap_discovery, acinetobacter_adp1_explorer]

**2. Metabolite-database evidence.**
- Re-query a current Web of Microbes release for consumption actions matching the 19 production events that had none in the 2018 snapshot, separating "absent" from "not yet curated". [src: webofmicrobes_explorer, discoveries]
- Test the metabolites of the BacDive 3/7 comparison directly in FW300-N2E3 growth assays, since curated-record absence and measured inability are not the same claim. [src: fw300_metabolic_consistency]
- Score each cross-database call by endpoint (production, capability, utilization, dependency, flux) and report concordance per endpoint rather than pooled. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]

**3. Respiratory routing.**
- Construct and phenotype an NDH-2 deletion strain on quinate, glucose, and acetate — the missing measurement that would let the zero-flux prediction be tested rather than argued. [src: respiratory_chain_wiring]
- Measure NADH oxidation rate, not only yield, on quinate versus glucose to test the theoretical capacity explanation against the 0.37 / 1.44 Complex I growth-ratio split. [src: respiratory_chain_wiring]
- Determine ACIAD3522's biochemical activity independently, so the 0.013 acetate growth ratio can be attributed to respiration or excluded from the respiratory comparison. [src: respiratory_chain_wiring]
- Re-simulate with a rate- or capacity-constrained objective and ask whether nonzero NDH-2 and ACIAD3522 flux appear. [src: respiratory_chain_wiring]

**4. Aromatic flux versus operon essentiality.**
- Phenotype the 10/13 defective operon subunits on acetate and succinate versus aromatic substrates in the same run, to test whether the defects are aromatic-specific at all. [src: aromatic_catabolism_network, discoveries]
- Repeat the NDH-2 compensation test with manually curated NDH-2 calls and a larger organism panel; at −0.297 versus −0.156 with p = 0.52, the current panel cannot separate a null from an underpowered effect. [src: discoveries]
- Compare predicted 1.76× Complex I flux against measured respiratory flux on aromatics, so the model quantity and the experimental quantity are the same quantity. [src: aromatic_catabolism_network]

**5. Conservation, openness, and latency.**
- Re-test active-versus-latent conservation at the clade level, the level at which the ρ = 0.69 openness correlation was found, to see whether the p = 0.94 null is a level-of-analysis artifact. [src: metabolic_capability_dependency]
- Publish the pathway-organism universe, latency threshold, and condition panel behind each of the 41.0%, 35.4%, and 15.8% latent fractions, and recompute all three under one definition instead of averaging. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]
- Test whether the partial rho = 0.530, p = 2.83e-203 variable-pathway/openness relation survives when latent rate is the response, isolating whether openness predicts latency specifically or pathway variability generally. [src: pathway_capability_dependency, metabolic_capability_dependency]

**6. Community signals and complementarity.**
- Acquire paired metagenomics-plus-metabolomics for Freshwater samples — all 33 currently lack it — and re-fit the completeness–metabolite associations with abiotic covariates included. [src: nmdc_community_metabolic_ecology]
- Pair the 83/86 genera occurrence result with activity evidence (transcript, protein, or isotope labelling) on the same samples, converting an occurrence claim into a degradation claim. [src: enigma_carbon_census_1]
- Publish the corrected complementarity pipeline with raw pair-level standard deviations, and report d ≈ −0.4 / prevalence-weighted −0.39 alongside the superseded d = −7.54 with the divisor error named. [src: plant_microbiome_ecotypes]
- Recover or explicitly account for the 62/322 genera (19.3%) lost from the NMDC bridge and re-run the C-score test, since 0 plant growth-promoting (PGP)-dominant / 3 pathogen-dominant / 66 dual-or-mixed leaves the guild structure undetermined. [src: plant_microbiome_ecotypes]
- Establish why core-level GapMind completeness is 0% across compartments — genuine absence versus tool coverage — before any exchange claim is attempted from these genomes. [src: plant_microbiome_ecotypes]
