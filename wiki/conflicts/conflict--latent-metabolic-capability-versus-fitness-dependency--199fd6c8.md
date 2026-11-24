<!-- tension-hash: 199fd6c892ed0bb0 -->
# Latent Pathways: Condition-Dependent Capability or Threshold Artifact?

Two readings compete over genomically complete metabolic pathways that look unimportant in lab fitness data. One reading is that every such "latent" pathway is truly condition-dependent, because of a 100% reclassification [src: discoveries, pathway_capability_dependency]. The other is that this reclassification is partly a threshold effect, and that laboratory fitness assays cannot show whether complete pathways are essential for viability [src: pathway_capability_dependency]. It matters because it decides whether genomic completeness can be trusted as a proxy for functional importance. The question comes from [[concepts/latent-metabolic-capability-versus-fitness-dependency]].

## Evidence Sides

**Side A: latent pathways are condition-dependent**

- The reading in [src: discoveries, pathway_capability_dependency] is that latent pathways are all truly condition-dependent. The basis is a 100% reclassification once pathways are stratified by condition subsets. RB-TnSeq (random barcode transposon sequencing, a genome-wide fitness assay) supplies the fitness data. Condition stratification partly addresses the limits of laboratory conditions. [src: pathway_capability_dependency]

**Side B: the reclassification is partly a threshold artifact, and essentiality is untested**

- The 100% reclassification is partly a threshold effect. The median-based importance threshold splits pathways about 50/50 by construction. [src: pathway_capability_dependency]
- With enough condition subsets, some pathways will inevitably cross the threshold. [src: pathway_capability_dependency]
- Laboratory RB-TnSeq cannot capture the full range of natural selective pressures. [src: pathway_capability_dependency]
- Whether complete pathways are actually essential for viability is left open. [src: essential_metabolome]

The sides differ on interpretation, not on the data. This page does not average them or prefer either one.

## Possible Reconciliations

- **Hypothesis: threshold calibration.** Calibrating against an independent validation set, such as known essentials from essential_metabolome, would give a more defensible threshold. Some latent pathways might then remain condition-dependent and others might not. [src: pathway_capability_dependency]
- **Hypothesis: different questions.** Condition-dependence of fitness and essentiality for viability may be separate properties. If so, both findings could hold at once, with essentiality still open. [src: essential_metabolome]
- **Hypothesis: partial truth.** The condition-dependent reading may hold for some pathways and be a by-product of the threshold for others. This is untested.

## Resolving Work

- **Data:** known essentials from essential_metabolome as a validation set. **Method:** recalibrate the importance threshold against it instead of the median. **Question:** does the reclassification of latent pathways persist?
- **Data:** the existing condition subsets. **Method:** a permutation or null model that shuffles fitness labels while keeping the median split. **Question:** how many pathways cross the threshold by chance as subsets are added?
- **Data:** fitness measurements across condition types. **Method:** compare effect sizes, not threshold crossing alone. **Question:** are the shifts large or marginal?
- **Data:** complete pathways in organisms with viability or essentiality evidence. **Method:** test essentiality directly against pathway completeness. **Question:** are complete pathways actually essential for viability?
- **Data:** natural-environment or non-laboratory growth data. **Method:** compare with laboratory RB-TnSeq results. **Question:** do selective pressures missing from the laboratory change which pathways count as latent?
