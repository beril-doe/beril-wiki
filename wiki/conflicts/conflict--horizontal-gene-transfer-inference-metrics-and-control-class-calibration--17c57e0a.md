<!-- tension-hash: 17c57e0aeb24ef19 -->
# Strong Control-Class Ratios Versus Small UniRef50 Effect Sizes in Horizontal Gene Transfer Inference

Horizontal gene transfer (HGT) is the movement of genes between lineages. This tension concerns how strongly tree-aware inference separates HGT-active gene classes from vertically inherited ones. Sankoff parsimony, which infers gain events on a species tree at minimum cost, gives a recent-to-ancient ratio of 24.5× for CRISPR-Cas against ~1× for strict housekeeping [src: discoveries], yet the UniRef50 (a protein-cluster resolution) effect size is small, d = 0.15 [src: gene_function_ecological_agora]. The report's strict housekeeping ratio also differs between its text and its atlas table. This matters because it determines how far the metric can be trusted and whether DTL (duplication-transfer-loss) reconciliation is a feasible alternative. Concept source: [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].

## Evidence Sides

**Side A: the signal is strong or at least separable**
- The recent-to-ancient ratio contrasts CRISPR-Cas at 24.5× with strict housekeeping at ~1×. [src: discoveries]
- At KO (KEGG ortholog) level with clean controls, Cohen's d (a standardized effect size) reaches 0.665–3.558. [src: gene_function_ecological_agora]
- The report gives strict housekeeping at ~1×. [src: gene_function_ecological_agora]
- Williams et al. say principled DTL methods are scaling, though not yet to 18,989 leaves. [src: gene_function_ecological_agora]

**Side B: the signal is small, inconsistent, or limited by method**
- The UniRef50 Sankoff effect size is small, with d = 0.15 against the pre-registered d ≥ 0.3 threshold. [src: gene_function_ecological_agora]
- The atlas table of the same report gives ratios of 2.3 to 6.4 for the strict housekeeping classes, which conflicts with ~1×. [src: gene_function_ecological_agora]
- The report argues DTL does not scale to GTDB (Genome Taxonomy Database). [src: gene_function_ecological_agora]

The ratio and Cohen's d are different metrics, so the pre-registered threshold applies only to the d effect size, not to the ratio.

## Possible Reconciliations

- **Hypothesis: resolution dependence.** UniRef50 may dilute the signal through annotation heterogeneity, while KO resolution with clean controls recovers it. This would explain d = 0.15 versus 0.665–3.558. [src: gene_function_ecological_agora]
- **Hypothesis: control-class definitions differ.** The ~1× figure and the 2.3 to 6.4 table ratios may come from different housekeeping memberships or contaminated classes. [src: gene_function_ecological_agora]
- **Hypothesis: scaling claims address different states.** DTL may be infeasible for the full GTDB tree at present yet become feasible as methods scale, so the two statements may not contradict each other. [src: gene_function_ecological_agora]

## Resolving Work

- Data: the strict housekeeping class definitions and per-class ratios in the atlas table. Method: re-derive the ratios from the same gain events. Question: which membership produces ~1× and which produces 2.3 to 6.4?
- Data: UniRef50 and KO annotations for identical control genes. Method: recompute Cohen's d at both resolutions. Question: does resolution alone explain d = 0.15 versus 0.665–3.558?
- Data: CRISPR-Cas and housekeeping gain events. Method: bootstrap confidence intervals on the ratio. Question: is the 24.5× versus ~1× contrast stable under resampling?
- Data: a GTDB subtree smaller than 18,989 leaves. Method: benchmark DTL reconciliation against Sankoff parsimony. Question: do the two agree on control-class direction where DTL is feasible?
