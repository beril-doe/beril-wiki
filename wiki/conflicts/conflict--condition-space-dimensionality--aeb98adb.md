<!-- tension-hash: aeb98adb7b42a8e6 -->
# Aromatic degradation in *Acinetobacter baylyi* ADP1: substrate-specific biology or missing model inputs?

Two analyses of the same organism place aromatic degradation genes in different explanatory frames. The deletion-phenotype analysis treats them as a concentrated, quinate-specific phenotypic module — a discrete set of genes whose growth requirement appears only on one carbon source. The triple-essentiality analysis finds the same functional category strongly enriched among genes where flux balance analysis (FBA, a constraint-based model that predicts growth from a metabolic network) disagrees with experiment, and reports that the disagreement runs in one direction: FBA under-predicts. The two readings are compatible as stated, but they assign the signal to different causes, and the choice matters for how the corpus interprets [[concepts/condition-space-dimensionality]]: if a discrete pathway module is partly a model artifact, then the count of independent phenotype axes is measuring the model as much as the biology.

## Evidence Sides

**Aromatic degradation as a substrate-dependent biological module.** The deletion-phenotype analysis identifies aromatic degradation as a concentrated quinate-specific module — a pathway-specific requirement expressed on one carbon source rather than spread across conditions. [src: adp1_deletion_phenotypes] Under this reading the enrichment is real substrate dependence: the genes are needed because quinate catabolism needs them, and the module's discreteness is a property of the organism's metabolism.

**Aromatic degradation as a locus of directional model failure.** The triple-essentiality analysis finds aromatic degradation strongly enriched among FBA-discordant genes and reports directional FBA under-prediction. [src: adp1_triple_essentiality] Under this reading the same gene set marks where model and experiment part company, and the direction of the discrepancy — under-prediction rather than scattered disagreement — is the feature any explanation of the module has to account for. [src: adp1_triple_essentiality]

## Possible Reconciliations

**Hypothesis 1 (both causes, additively).** The two findings are compatible but leave unresolved whether the apparent pathway-specific requirement primarily reflects biological substrate dependence, missing model inputs, or both. [src: adp1_triple_essentiality] The reconciliation to test is that a genuine quinate-specific requirement and a model-input gap coexist, each contributing part of the signal.

**Hypothesis 2 (trace aromatics).** The triple-essentiality analysis proposes trace aromatics as a hypothesis requiring direct testing rather than as an established explanation. [src: adp1_triple_essentiality] If undeclared aromatic compounds are present in media, genes scored as condition-specific could be responding to substrates the model does not know about.

**Hypothesis 3 (mismatched environmental assumptions).** The same analysis proposes mismatched environmental assumptions as a hypothesis requiring direct testing, not as an established explanation. [src: adp1_triple_essentiality] If the model's simulated medium differs from the assayed medium, directional under-prediction would follow without any biological module being illusory.

## Resolving Work

- Analytically profile the assayed media (e.g. by chromatography) for aromatic compounds, and ask whether trace aromatics are present at all — converting Hypothesis 2 from a proposed explanation into a measured presence or absence. [src: adp1_triple_essentiality]
- Re-run FBA with the media composition as actually measured rather than as declared, and ask whether the directional under-prediction on aromatic degradation genes persists. [src: adp1_triple_essentiality]
- Compare the aromatic-degradation gene set defined by deletion phenotype against the set defined by FBA discordance, and ask how far the two overlap — a partial overlap would support Hypothesis 1's additive account. [src: adp1_deletion_phenotypes] [src: adp1_triple_essentiality]
- Check whether other functional categories also show directional FBA under-prediction, and ask whether the directionality is specific to aromatic degradation or a global property of the model. [src: adp1_triple_essentiality]
