<!-- tension-hash: cf98e361c044acb7 -->
# Community-Scale Signals Versus Flux-Level Inference in NMDC-Based Metabolic Ecology

Two projects that use National Microbiome Data Collaborative (NMDC) metagenomes find broad community-scale patterns, but each also states limits on what those patterns show. The tension is how much weight community-scale association or occurrence data can carry when used to support or constrain model-based predictions of metabolic function. This bears on [[concepts/metabolic-model-gapfilling]], where gapfilling means adding reactions so a model can simulate growth. Treating community-scale co-variation or genus occurrence as evidence of flux (the rate of material flow through metabolic reactions), causality or activity would add a layer of inference.

## Evidence Sides

**Community-scale data detect consistent signals**

- The NMDC community metabolic ecology analysis reports negative associations between community pathway completeness and metabolite levels. These associations suggest a community-scale signal. [src: nmdc_community_metabolic_ecology]
- The Carbon Census found broad occurrence: implicated genera appeared in 83/86 genera across 1,719 NMDC metagenomes. [src: enigma_carbon_census_1]

**Those signals do not establish flux, causality or activity**

- The negative completeness–metabolite associations do not establish individual flux or causality. All 33 Freshwater samples lacked paired metabolomics (direct metabolite measurement from the same sample), and abiotic covariates (nonliving environmental variables, such as physical or chemical conditions, included in an analysis) were unavailable. [src: nmdc_community_metabolic_ecology]
- The Carbon Census measured occurrence rather than degradation or activity. Detecting a genus therefore shows presence, not function. [src: enigma_carbon_census_1]

These two sides are not opposed findings. Each project's own data support both a detectable pattern and a stated limit on what that pattern means. The tension lies between the breadth of the signal and the depth of inference it permits. Neither side should be preferred by default.

## Possible Reconciliations

- **Hypothesis 1 — scale separation.** Community-scale associations and occurrence may be valid constraints at the ecosystem level while staying silent about organism-level flux. If so, they can prioritize which pathways or genera to test, but they cannot validate model predictions.
- **Hypothesis 2 — confounding.** The negative completeness–metabolite associations may partly reflect abiotic or environmental structure that the analysis could not adjust for. If so, the signal would weaken once covariates are added.
- **Hypothesis 3 — presence without function.** Broad genus occurrence may coexist with a narrow set of active degraders. If so, occurrence would overstate the functional reach of implicated genera.

## Resolving Work

- **Covariate adjustment.** Use NMDC samples that carry abiotic covariates and re-fit the completeness–metabolite associations with those covariates included. Question: do the negative associations survive adjustment?
- **Paired metabolomics for Freshwater.** Obtain Freshwater samples with paired metagenomics and metabolomics and repeat the association test within that biome. Question: does the community-scale signal extend to the samples that currently lack metabolite data?
- **Activity evidence for implicated genera.** Join the Carbon Census genera to metatranscriptomic data (sequencing of community RNA to assess gene expression) or fitness data where available. Question: are the genera detected in NMDC metagenomes actually expressing or depending on the relevant degradation genes?
- **Model-level test.** For genera with both NMDC occurrence and pathway completeness, compare gapfilled model predictions against measured growth or fitness. Question: does community-scale completeness predict organism-level metabolic sufficiency?
