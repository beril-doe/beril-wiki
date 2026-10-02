<!-- tension-hash: 68690ec7a11f5d94 -->
# Conflict: Does FBA Agreement With Essentiality Data in ADP1 Look Substantial or Absent?

Two projects in this corpus evaluate the same organism, *Acinetobacter baylyi* ADP1, against the same class of model output — flux balance analysis (FBA), a constraint-based method that predicts feasible metabolic flux distributions and, from them, whether a gene is needed for simulated growth — and reach readings that point in opposite directions. One reports substantial agreement between FBA and transposon-sequencing (TnSeq) essentiality calls; the other reports only moderate agreement with experimental knockouts, together with a null association between FBA class and growth defects within TnSeq-dispensable genes. Gapfilled-model predictions are here being compared directly against experimental essentiality data (see [[concepts/metabolic-model-gapfilling]]), so whether FBA agrees or fails to discriminate in this exact setting bounds how much downstream inference a gapfilled model can carry.

## Evidence Sides

**Side A — substantial FBA/TnSeq concordance.** Across the genes carrying both an FBA flux prediction and a TnSeq essentiality call, 73.8% of 866 genes are concordant. [src: acinetobacter_adp1_explorer] The claim is a binary agreement rate over a defined intersection of two call sets, not a test of predictive power on any continuous phenotype.

**Side B — moderate knockout concordance plus a null within dispensable genes.** The triple-essentiality analysis reports moderate concordance between FBA and experimental knockouts, and, separately, a null association between FBA class and growth defects within TnSeq-dispensable genes. [src: adp1_triple_essentiality] The null is a null: it states that among genes TnSeq calls dispensable, FBA class does not distinguish those with growth defects from those without. It is not a weak positive and must not be reported as one.

The two sides are not obviously arithmetic opposites. Their endpoints and gene sets differ, and matched-gene comparisons using the same medium, the same knockout definition, the same FBA class, and the same continuous growth endpoint are needed before either reading can be set against the other.

## Possible Reconciliations

- *Hypothesis:* the denominators differ — Side A's 866-gene intersection and Side B's TnSeq-dispensable subset may share few genes, so a high overall agreement rate and a null within one stratum could both hold.
- *Hypothesis:* the endpoints differ — binary concordance of essentiality calls and association with a growth-defect phenotype measure different things, and a model can match call labels without ranking defect severity.
- *Hypothesis:* condition differs — media and knockout definitions may not be matched across the two analyses, so concordance is being estimated under different growth regimes.

## Resolving Work

- Restrict both analyses to the intersecting gene set and recompute FBA/TnSeq concordance and the FBA-class/growth-defect association on identical genes: does the null survive on Side A's genes?
- Fix one medium and one knockout definition across both projects, then re-derive FBA classes: how much of the gap is definitional rather than biological?
- Replace binary essentiality labels with a continuous growth endpoint and test FBA class against it: does FBA rank defect magnitude even where it fails binary discrimination?
- Stratify concordance by FBA class and TnSeq call to locate where the 73.8% figure is carried [src: acinetobacter_adp1_explorer]: is agreement concentrated in one call combination?
