<!-- tension-hash: 9cf52c50424ab132 -->
# Does Web of Microbes production evidence corroborate metabolic-model support, or measure a different endpoint?

Gapfilling adds reactions or functions needed to complete a metabolic model and enable simulated growth. Gapfilled models are often checked against independent evidence, so it matters whether every evidence stream measures the same thing. Two lines of evidence pull in different directions. Web of Microbes (WoM), a curated exometabolomics database, has a coverage gap: the 19 production-to-Fitness-Browser matches lacked consumption actions in the 2018 snapshot [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]. In contrast, FW300-N2E3 showed GapMind 13/13 and Fitness Browser 21/21 concordance but BacDive only 3/7 [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]. The open question for [[concepts/metabolic-model-gapfilling]] is whether these sources can validate one another, or whether they report different endpoints that should not be pooled.

## Evidence Sides

**Production records lack consumption actions**

The 19 production-to-Fitness-Browser matches lacked consumption actions in the 2018 WoM snapshot [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]. On this side, WoM records production but not consumption, so its matches cannot by themselves speak to utilization or dependency endpoints [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency].

**Full GapMind and Fitness Browser concordance, partial BacDive concordance, in one strain**

For FW300-N2E3, concordance was GapMind 13/13 and Fitness Browser 21/21, but BacDive only 3/7 [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]. The tension does not specify the reference each concordance was measured against, and the result comes from a single organism, so it should not be read as general validation.

Production, capability, utilization, dependency, and flux remain distinct endpoints [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency].

## Possible Reconciliations

- *Hypothesis:* The two sides do not conflict because they measure different endpoints. On this reading, WoM production speaks to excretion, GapMind to pathway capability, and the Fitness Browser to condition-specific dependency.
- *Hypothesis:* The low BacDive agreement reflects how the phenotype database records and covers traits, not a failure of the model or pathway evidence.
- *Hypothesis:* The missing consumption actions are a feature of this one snapshot export. Consumption may be recorded in other WoM releases, which would close the coverage gap without changing any endpoint.

## Resolving Work

- **WoM releases newer than the 2018 snapshot:** test whether consumption actions exist there. Then ask whether metabolites that strains consume line up with Fitness Browser conditions where the relevant genes are needed for fitness.
- **FW300-N2E3 BacDive records, compared trait by trait against GapMind calls:** for each disagreement, decide whether it reflects a database annotation gap, a mismatch in growth conditions, or a missing pathway.
- **Other Fitness Browser organisms that also have GapMind and BacDive records:** repeat the three-source concordance analysis with a stated common reference. The question is whether the full GapMind and Fitness Browser concordance and the partial BacDive concordance hold beyond one strain.
- **Flux balance analysis (FBA), a constraint-based method that predicts feasible flux distributions, run on gapfilled models for strains with WoM production data:** check whether the predicted secretion fluxes match the metabolites WoM records as produced. This would test production directly as its own endpoint.
