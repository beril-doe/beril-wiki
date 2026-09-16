<!-- tension-hash: b8d9172e3b6a7347 -->
# Gradient or module? Six unresolved splits in how condition-dependent fitness is read

The *Acinetobacter baylyi* ADP1 deletion work and the comparative pathway analyses that build on it agree that gene-dependent growth effects spread across several environmental axes, but they disagree — or leave open competing readings — about what those axes *are* and at what level they should be read. The `## Tensions` block of [[concepts/condition-space-dimensionality]] carries **six** distinct disagreements, and all six are recorded here, each in its own subsection: (1) whether the phenotype landscape is a continuum or contains discrete modules, and whether the dimensionality estimate is even stable; (2) whether perturbation modality — genetic deletion versus chemical treatment — explains the mix of continuous and modular structure; (3) whether the aromatic-degradation signal is a biological substrate requirement or a metabolic-model artifact; (4) whether the ADP1 quinate/Complex I respiratory story generalizes across species; (5) whether condition-specific pathway reclassification is biology or a product of how thresholds are drawn; and (6) whether clade-level pangenome dynamics can be read as evidence about pathway-level conservation. Disagreements (5) and (6) are held apart deliberately: the input introduces (6) as "a second, distinct tension," and the two come from different projects with different classifications, so they are not merged here. These splits matter because each side implies a different next step — more conditions, a different perturbation, better model inputs, a larger species panel, a recalibrated threshold, or a different level of inference.

## Evidence Sides

### 1. Continuum versus discrete modules, on a possibly under-sampled condition panel

**Side A — the landscape is a gradient.** The low clustering silhouette score (a measure of how cleanly points fall into separate clusters rather than one continuum) and the absence of functional enrichments significant after FDR correction (false discovery rate: the expected fraction of false positives among calls declared significant) favor a gradient interpretation of the phenotype landscape. [src: adp1_deletion_phenotypes]

**Side B — modules are not excluded.** Those same statistics do not exclude additional discrete modules that would emerge under a broader condition panel or with improved measurement precision. [src: adp1_deletion_phenotypes] Compounding this, the approximately 5 independent dimensions are inferred from only 8 tested carbon sources, so the dimensionality may increase when additional conditions are measured. [src: adp1_deletion_phenotypes] Neither the dimension count nor the gradient verdict is anchored against a panel large enough to falsify the alternative.

### 2. Perturbation modality versus organism biology

**Side A — modality matters.** The comparison between single-gene deletions and chemical-genetic perturbations is offered as a candidate explanation for why ADP1 shows an apparent balance between continuous and modular architectures. [src: adp1_deletion_phenotypes]

**Side B — ADP1's own metabolism may be the cause, and neither side is tested.** The comparison is interpretive rather than directly tested here, so it does not resolve whether perturbation modality or ADP1 metabolic interconnectedness explains that apparent balance. [src: adp1_deletion_phenotypes] The ADP1 dataset alone therefore does not establish a cross-organism rule about genetic deletions versus chemical perturbations. [src: adp1_deletion_phenotypes]

### 3. Aromatic degradation: substrate dependence or missing model inputs

**Side A — a concentrated biological module.** The deletion-phenotype analysis identifies aromatic degradation as a concentrated quinate-specific module. [src: adp1_deletion_phenotypes]

**Side B — a model-discordance signal.** The triple-essentiality analysis finds aromatic degradation strongly enriched among genes discordant with FBA (flux balance analysis: a stoichiometric model that predicts growth-supporting flux distributions) and reports directional FBA under-prediction. [src: adp1_deletion_phenotypes] [src: adp1_triple_essentiality] The two findings are compatible but leave unresolved whether the apparent pathway-specific requirement primarily reflects biological substrate dependence, missing model inputs, or both; the newer analysis proposes trace aromatics and mismatched environmental assumptions as hypotheses requiring direct testing rather than as established explanations. [src: adp1_triple_essentiality]

### 4. Does the ADP1 respiratory interpretation generalize?

**Side A — substrate-specific respiratory requirements are real in ADP1.** The respiratory analysis supports the existence of substrate-specific respiratory requirements. [src: respiratory_chain_wiring]

**Side B — the mechanism is unidentified and the cross-species test failed.** The same analysis leaves unresolved whether the apparent quinate Complex I requirement reflects a concentrated NADH flux burst, another function of ACIAD3522, unmeasured environmental inputs, or limitations of the fitness and FBA datasets. [src: respiratory_chain_wiring] Its cross-species test found validated NDH-2 (a non-proton-pumping alternative NADH dehydrogenase) in 5 of 14 organisms; organisms with validated NDH-2 had a larger mean Complex I aromatic deficit, −0.297, than organisms without validated NDH-2, −0.156, but the difference was not statistically significant (p = 0.52) and was opposite to the predicted compensation pattern. [src: respiratory_chain_wiring] The ADP1-specific respiratory interpretation should therefore not yet be generalized across species. [src: respiratory_chain_wiring]

### 5. Condition-dependence versus threshold construction

**Side A — latency is condition-specific.** All 66 aggregate Latent Capability pairs became important under at least one condition type, which supports condition dependence. [src: pathway_capability_dependency]

**Side B — the thresholds can manufacture the crossings.** The analysis itself cautions that median thresholds applied within condition subsets can force crossings. [src: pathway_capability_dependency] This does not contradict the ADP1 evidence for multiple phenotype axes, but it limits how strongly condition-specific pathway reclassification can be treated as independent biological confirmation. [src: pathway_capability_dependency]

### 6. Clade-level genome dynamics versus pathway-level conservation

This is a second, distinct tension, raised by a different project from the one in (5) and resting on its own latency classification. [src: metabolic_capability_dependency]

**Side A — clade-level genome dynamics track latency.** The capability–dependency analysis associates higher latent capability rates with more open pangenomes (Spearman ρ = 0.69, p = 0.0004, n = 22 clades), where ρ is a rank correlation coefficient. [src: metabolic_capability_dependency]

**Side B — pathway-level conservation does not.** Its pathway-level comparison did not distinguish latent from active pathways (Mann–Whitney U, a rank-based two-sample test, p = 0.94; rank-biserial r = 0.052, an effect size near zero). [src: metabolic_capability_dependency] These results should not be reconciled by treating openness as proof of pathway-level conservation or loss: they support different levels of inference and require analyses that connect individual pathway trajectories to clade-level genome dynamics. [src: metabolic_capability_dependency]

## Possible Reconciliations

All of the following are hypotheses, not findings. Items marked **(page-author)** are inferences made on this page; no cited source asserts them, and they carry no source tag.

- **Scope hypothesis (1).** Both sides can hold if the gradient is a true description of the sampled condition subspace while additional discrete modules exist along axes the 8-condition panel did not vary — precisely the possibility the analysis itself leaves open in invoking "a broader condition panel." [src: adp1_deletion_phenotypes] The input does not specify which axes are unsampled, so the hypothesis is about panel breadth in general, not about any named condition class.
- **Measurement-precision hypothesis (1).** The analysis names improved measurement precision, alongside a broader panel, as a route by which additional discrete modules could emerge; on this reading the gradient verdict is a statement about what the current precision can resolve rather than about the underlying architecture. [src: adp1_deletion_phenotypes]
- **Modality-as-filter hypothesis (2) (page-author).** Perturbation modality and ADP1 metabolic interconnectedness may not be competing explanations at all, but two filters acting on the same architecture, in which case the observed balance would be jointly determined and no single-cause verdict would be available even from a well-powered comparison. The input leaves both candidate explanations unresolved and tests neither. [src: adp1_deletion_phenotypes]
- **Both-causes hypothesis (3).** Aromatic degradation could be genuinely required on quinate *and* be systematically under-predicted by FBA if the model omits trace aromatics or assumes a mismatched environment; the phenotype module and the discordance enrichment would then be two readouts of one missing model input rather than rival explanations. The trace-aromatics and environment-mismatch possibilities are the source's own untested hypotheses. [src: adp1_triple_essentiality]
- **Taxon-restriction hypothesis (4) (page-author).** The quinate/Complex I requirement may be real but restricted to organisms with ADP1's respiratory wiring; a null cross-species result (p = 0.52) with an effect in the direction opposite to the compensation prediction is one of the patterns a taxon-restricted mechanism can produce when tested as a universal rule in 14 organisms. [src: respiratory_chain_wiring]
- **Non-compensation hypothesis (4) (page-author).** Alternatively, validated NDH-2 presence may simply not be the compensating variable: the larger deficit in NDH-2-positive organisms (−0.297 versus −0.156) is compatible with NDH-2 presence co-varying with something else, which would leave the ADP1 mechanism untested rather than refuted. [src: respiratory_chain_wiring]
- **Definitional hypothesis (5).** "Latent" may be partly a property of a threshold rather than of a pathway: if median cutoffs applied within condition subsets force some pairs across the line by construction, the 66-of-66 crossing rate would be inflated relative to a fixed, condition-independent cutoff. This hypothesis is confined to the classification that produced the 66 pairs. [src: pathway_capability_dependency]
- **Separate-classification hypothesis (5, 6) (page-author).** The threshold caveat and the clade-level correlation belong to different projects and different latency classifications, so a threshold artifact in one does not automatically propagate to the other; treating them as one calibration problem would presuppose a shared set of latency calls that the evidence does not provide. [src: pathway_capability_dependency, metabolic_capability_dependency]
- **Level-of-inference hypothesis (6).** Pangenome openness may summarize gene gain and loss aggregated over many pathways and long timescales, while pathway-level conservation is a per-pathway contrast; a strong clade-level correlation (ρ = 0.69) and a null pathway-level result (p = 0.94; r = 0.052) are then measurements of different quantities rather than contradictory measurements of one — which is why the source insists the two support different levels of inference. [src: metabolic_capability_dependency]

## Resolving Work

**1. Dimensionality and gradient-versus-module**
- Re-run the phenotype-space decomposition after extending the panel beyond the 8 tested conditions, and ask whether the approximately 5 independent dimensions grow, plateau, or reorganize. [src: adp1_deletion_phenotypes]
- Estimate the replicate-noise floor per gene per condition and repeat clustering on noise-matched simulated data, to test whether a low silhouette score is attainable from a truly modular architecture at the achieved precision. [src: adp1_deletion_phenotypes]
- Run enrichment on the gradient axes themselves (component loadings) rather than on cluster membership, to see whether functional structure is present but not cluster-shaped after FDR correction. [src: adp1_deletion_phenotypes]
- Subsample the existing conditions to 4, 5, 6 and 7 and plot the recovered dimension count against panel size, to establish whether the estimate has saturated at 8. [src: adp1_deletion_phenotypes]

**2. Deletion versus chemical perturbation**
- Profile the same ADP1 gene set with a chemical-genetic panel on the same conditions and compare modularity metrics head-to-head; this converts the deletion-versus-chemical comparison from interpretation into a direct test. [src: adp1_deletion_phenotypes]
- Repeat that paired deletion/chemical design in a second organism, since the ADP1 dataset alone cannot establish a cross-organism rule about genetic deletions versus chemical perturbations. [src: adp1_deletion_phenotypes]
- Quantify metabolic interconnectedness independently (for example from the metabolic network reconstruction) for each organism in such a panel, and test whether modularity tracks interconnectedness after modality is held fixed — the only way to separate the two candidate explanations the analysis leaves open. [src: adp1_deletion_phenotypes]
- Re-analyze existing chemical-genetic datasets under the identical clustering and dimensionality pipeline used here, so that any modality difference is not confounded by differences in analysis method. [src: adp1_deletion_phenotypes]

**3. Aromatic degradation: biology or model inputs**
- Grow ADP1 on quinate in aromatics-free defined medium versus medium spiked with the proposed trace aromatics, and test whether the quinate-specific aromatic-degradation requirement persists. [src: adp1_deletion_phenotypes, adp1_triple_essentiality]
- Re-run FBA with the medium composition corrected to the assayed environment and ask whether aromatic degradation remains enriched among discordant genes and whether the directional under-prediction shrinks. [src: adp1_triple_essentiality]
- Partition discordant genes into those whose discordance disappears under corrected inputs and those that survive, to size how much of the signal is model artifact versus biology. [src: adp1_triple_essentiality]
- Measure aromatic-pathway flux directly (labeled-substrate tracing) on quinate, and check whether measured and predicted flux differ in the direction FBA under-predicts. [src: adp1_triple_essentiality]

**4. Generalizing the respiratory interpretation**
- Expand the cross-species test well beyond 14 organisms, since the observed contrast (−0.297 versus −0.156, p = 0.52) is underpowered and directionally opposite to the compensation prediction. [src: respiratory_chain_wiring]
- Obtain direct fitness data for NDH-2 and for ACIAD3522 on quinate in ADP1, to separate a concentrated NADH flux burst from an unrelated ACIAD3522 function. [src: respiratory_chain_wiring]
- Measure NADH turnover or respiratory flux on quinate versus other substrates rather than inferring it from fitness and FBA, whose limitations are explicitly flagged as a candidate explanation for the pattern. [src: respiratory_chain_wiring]
- Replace the binary "validated NDH-2 present/absent" contrast with a graded measure of alternative-dehydrogenase capacity and re-test the Complex I aromatic deficit against it. [src: respiratory_chain_wiring]

**5. Threshold calibration of condition-specific latency**
- Re-classify the 66 aggregate Latent Capability pairs under fixed, condition-independent thresholds and report how many still become important under at least one condition type; the drop quantifies the forced-crossing artifact. [src: pathway_capability_dependency]
- Run a label-permutation null in which condition assignments are shuffled, to establish the crossing rate expected from median thresholds applied within condition subsets alone. [src: pathway_capability_dependency]
- Report the number of measurements per condition subset alongside each crossing, since a median cutoff computed within a small subset is the specific mechanism the analysis warns can force a crossing. [src: pathway_capability_dependency]

**6. Connecting clade-level and pathway-level inference**
- Reconstruct gain/loss trajectories for individual pathways along clade phylogenies and ask whether latent pathways are preferentially recent gains or imminent losses — the analysis that connects individual pathway trajectories to clade-level genome dynamics, and the one the source names as required. [src: metabolic_capability_dependency]
- Stratify the pathway-level conservation comparison by clade openness, to test whether a latent-versus-active difference exists inside open pangenomes even though it is absent when pooled (p = 0.94; r = 0.052). [src: metabolic_capability_dependency]
- Re-test the pangenome-openness correlation (ρ = 0.69, p = 0.0004, n = 22 clades) under alternative latency cutoffs drawn within this project's own classification, to check whether the clade-level result is itself threshold-sensitive — without importing the separate threshold calibration applied to the 66-pair classification. [src: metabolic_capability_dependency]
- Cross-map the two projects' latency calls onto shared organisms or pathways and report their concordance, which would establish whether the clade-level and condition-stratified results are even describing the same pathway set. [src: pathway_capability_dependency, metabolic_capability_dependency]
