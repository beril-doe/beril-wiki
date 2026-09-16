<!-- tension-hash: aeb98adb7b42a8e6 -->
# Aromatic degradation in *Acinetobacter baylyi* ADP1: substrate-specific requirement or model-input gap?

Two analyses of *Acinetobacter baylyi* ADP1 single out aromatic degradation genes but read them differently. The deletion-phenotype analysis treats aromatic degradation as a concentrated quinate-specific module. The triple-essentiality analysis finds the same functional class strongly enriched among genes where FBA (flux balance analysis, a constraint-based model that predicts growth from metabolic network stoichiometry) disagrees with experiment, and it reports directional FBA under-prediction [src: adp1_deletion_phenotypes] [src: adp1_triple_essentiality]. The findings are compatible, but it remains unresolved whether the apparent pathway-specific requirement mainly reflects biological substrate dependence, missing model inputs, or both [src: adp1_triple_essentiality]. The answer bears on how [[concepts/condition-space-dimensionality]] interprets the discrete pathway-specific module.

## Evidence Sides

**Side A: a concentrated, quinate-specific biological module**

The deletion-phenotype analysis identifies aromatic degradation as a concentrated quinate-specific module [src: adp1_deletion_phenotypes]. One interpretation, not established by the evidence, is that this module reflects a discrete, substrate-dependent requirement of ADP1 metabolism.

**Side B: enrichment among FBA-discordant genes with directional under-prediction**

The triple-essentiality analysis finds aromatic degradation strongly enriched among FBA-discordant genes and reports directional FBA under-prediction [src: adp1_triple_essentiality]. The analysis proposes trace aromatics and mismatched environmental assumptions as possible causes. It presents these as hypotheses requiring direct testing, not as established explanations [src: adp1_triple_essentiality].

## Possible Reconciliations

- **Hypothesis 1: genuine substrate dependence.** The quinate-specific module is real biology. FBA discordance arises because the model does not fully capture this dependence. Both observations then describe the same underlying requirement.
- **Hypothesis 2: missing model inputs.** Trace aromatics or mismatched environmental assumptions in the model's medium definition produce the discordance [src: adp1_triple_essentiality]. Part of the apparent pathway specificity would then reflect model inputs rather than biology.
- **Hypothesis 3: both contribute.** A real quinate-linked requirement coexists with input mismatches that inflate or misplace FBA discordance in other conditions. Separating the contributions would require condition-by-condition attribution.

None of these is established by the current evidence. The triple-essentiality analysis explicitly frames its explanations as hypotheses [src: adp1_triple_essentiality].

## Resolving Work

- **Medium composition audit.** Compare the measured composition of growth media, including trace aromatic contaminants quantified by targeted metabolomics (quantitative measurement of a predefined set of small molecules), against the FBA medium definitions. Question: do unmodelled aromatics exist in the conditions where under-prediction occurs?
- **Model input perturbation.** Rerun FBA with trace aromatic uptake enabled and with revised environmental assumptions. Then re-score concordance against deletion phenotypes. Question: does the aromatic-degradation enrichment among discordant genes disappear, shrink, or persist?
- **Defined-medium regrowth.** Regrow aromatic degradation deletion mutants on rigorously aromatic-free defined media, with and without quinate. Question: is the growth defect strictly quinate-dependent, which would support biological substrate dependence?
- **Cross-condition attribution.** Stratify FBA-discordant aromatic degradation genes by carbon source using the deletion collection's per-condition growth data. Question: is discordance confined to the quinate condition or spread across conditions where no aromatic substrate is supplied?
