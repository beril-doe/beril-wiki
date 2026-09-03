<!-- tension-hash: 7d4b0a6299664e1b -->
# Within-Collection Association vs. Transportable Inference

The disagreement concerns whether strong classifier-derived associations within a collection support inference that will generalize across studies or environments. The evidence indicates that matrix contrasts can be statistically significant while an out-of-study model performs poorly, creating a tension between detecting an association under controlled study conditions and transporting that association to new data. The [[concepts/classifier-database-compatibility-in-taxonomic-quantification]] page also connects this tension to classifier/database compatibility, study structure, and differences in ecological response variables.

## Evidence Sides

**Within-collection matrix association**

Matrix contrasts were statistically significant, showing a strong matrix association in the analyzed collection. The result is described as a within-collection association rather than evidence that the classifier necessarily supports transportable inference across studies. [src: euk_in_prok_correlates]

**Poor cross-study generalization**

The out-of-study environment model had R²=−0.30 and detection AUC=0.56. These values indicate that the association detected within the collection did not translate straightforwardly to out-of-study prediction. [src: euk_in_prok_correlates]

**Phylogeny-dominated genome-wide similarity**

The ecotype analysis found that phylogeny generally dominated environmental similarity as a predictor of genome-wide gene-content similarity. This result is related to, but non-identical with, the classifier-derived matrix association because it uses a different response, data structure, and environmental representation. [src: ecotype_analysis]

**Different analytical objects**

The ecotype result and the present classifier-derived result cannot be directly reconciled because they use different responses, data structures, and environmental representations. The apparent disagreement therefore concerns both the strength of environmental signal and what is being measured. [src: ecotype_analysis, euk_in_prok_correlates]

## Possible Reconciliations

- **Hypothesis — scope difference:** Matrix contrasts may capture a real association within the sampled collection, while the out-of-study model tests whether that association is transportable to a different study structure or environment. Both findings could therefore be correct at their respective scopes. [src: euk_in_prok_correlates]
- **Hypothesis — measurement difference:** Classifier-derived environmental associations and genome-wide gene-content similarity may measure different biological or analytical responses. A strong result for one response need not imply a strong result for the other. [src: ecotype_analysis, euk_in_prok_correlates]
- **Hypothesis — representation and compatibility:** Classifier/database compatibility and study structure may alter the observed association, producing significant within-matrix contrasts without stable cross-study inference. [src: euk_in_prok_correlates]
- **Hypothesis — phylogenetic confounding:** Environmental similarity may appear associated with classifier-derived patterns within a matrix while phylogeny dominates genome-wide gene-content similarity in the ecotype analysis. [src: ecotype_analysis, euk_in_prok_correlates]

## Resolving Work

- Assemble matched samples spanning multiple studies, matrices, environments, and phylogenetic groups; test whether matrix effects remain after study and phylogeny are modeled.
- Refit the environment classifier with held-out studies and databases; compare cross-study R² and detection AUC with within-study performance to quantify transportability.
- Harmonize classifier assignments and database versions across studies; test whether classifier/database compatibility changes matrix contrasts and out-of-study predictions.
- Analyze the same samples using both classifier-derived environmental variables and genome-wide gene-content similarity; test whether their associations differ after aligning environmental representations.
- Use nested cross-validation and study-stratified permutation tests to determine whether the observed signal reflects environment, matrix, phylogeny, or study structure.
