<!-- tension-hash: c0666023464f7ad3 -->
# Concordance of Metabolic Model Predictions: 73.8% Database Agreement Versus Moderate Knockout Agreement

Two reports of Acinetobacter baylyi ADP1 give different-looking figures for how well flux balance analysis (FBA, a computational method that predicts gene essentiality and growth from a metabolic network) agrees with experiment. One report gives 73.8% concordance in a database comparison. [src: acinetobacter_adp1_explorer] The other gives κ≈0.49 and F1≈0.62-0.67 in a knockout comparison. [src: adp1_triple_essentiality] The reports use different metrics and gene sets, so the figures are not directly comparable. This matters because readers may take either number as the reliability of FBA for model refinement. The tension comes from [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

## Evidence Sides

**Database comparison**

- Concordance is 73.8% in the database comparison. [src: acinetobacter_adp1_explorer]
- The metric is percent concordance, not a chance-corrected statistic. The TENSION text gives no denominator or threshold beyond this figure.

**Knockout comparison**

- Agreement is κ≈0.49 in the knockout comparison. [src: adp1_triple_essentiality] κ (Cohen's kappa) measures agreement between two sets of calls after correcting for chance.
- F1≈0.62-0.67 in the same comparison. [src: adp1_triple_essentiality] F1 is the harmonic mean of precision and recall, two measures of how well positive calls match the reference.
- The two reports use different metrics and gene sets, so the figures are not directly comparable.

## Possible Reconciliations

- **Hypothesis: metric difference.** Percent concordance, κ and F1 summarize agreement in different ways, so the same underlying agreement could give different-looking numbers.
- **Hypothesis: gene-set difference.** The database comparison and the knockout comparison cover different gene sets. Differences in gene composition, such as the share of essential genes, could shift each score.
- **Hypothesis: reference-data difference.** The two comparisons may use different experimental references, so each is measuring agreement with different biology.

None of these is established. None supports preferring one figure or averaging them.

## Resolving Work

- **Data:** the gene lists behind each report. **Method:** compute the overlap between the two gene sets. **Question:** how many genes are common to both comparisons?
- **Data:** the shared genes with FBA predictions and experimental calls. **Method:** compute percent concordance, κ and F1 on the same genes. **Question:** do the metrics still differ on identical genes?
- **Data:** the experimental calls from each report. **Method:** cross-tabulate the calls gene by gene. **Question:** do the two references label the same genes essential?
- **Data:** the FBA predictions from each report. **Method:** compare model versions and media assumptions. **Question:** do the two analyses use the same predictions?
- **Data:** the class balance in each gene set. **Method:** resample to matched class proportions and recompute each metric. **Question:** does class balance explain the gap between the figures?
