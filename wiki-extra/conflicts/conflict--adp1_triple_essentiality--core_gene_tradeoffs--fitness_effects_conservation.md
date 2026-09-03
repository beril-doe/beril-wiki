<!-- tension-hash: e406e19b31b8d436 -->
# Graded Fitness Predicts Lethality Better Than Thresholded Essentiality Calls

The disagreement concerns what transposon-based measurements can legitimately establish about gene essentiality. The evidence supports continuous fitness as a potentially informative predictor of knockout lethality, while showing poor agreement between thresholded RB-TnSeq essentiality and complete-knockout calls. Conservation and costly-conserved-gene analyses add biological context, but they do not by themselves determine whether an apparently neutral or costly perturbation reflects true natural essentiality. This distinction is central to interpreting [[concepts/essentiality-assay-discordance]] without treating any single assay as a universal definition of essentiality.

## Evidence Sides

**Continuous fitness contains predictive information**

Continuous transposon fitness contains useful information about knockout lethality. This conclusion is supported by AUC values of 0.700 and 0.725 for inverted fitness. [src: adp1_triple_essentiality] The conservation evidence supports the graded-fitness conclusion, although the conservation gradient was statistically robust yet weak. [src: fitness_effects_conservation]

**Thresholded essentiality shows poor assay concordance**

Thresholded RB-TnSeq essentiality shows poor agreement with complete-knockout calls. The 0.05-threshold AUC of 0.344 for essentiality fraction and Cohen’s kappa of -0.081 support this conclusion. [src: adp1_triple_essentiality] Thus, binary assay concordance differs from the predictive signal available in continuous fitness measurements. [src: adp1_triple_essentiality]

**Conservation and costly conservation qualify interpretation**

Singleton neutrality may reflect poor transposon coverage rather than true neutrality, so conservation cannot independently resolve whether an apparently neutral insertion mutant retains function or simply lacks reliable fitness measurement. [src: fitness_effects_conservation] The Costly + Conserved category is inferred from laboratory burden and conservation, and costly conservation should be treated as a selection hypothesis requiring ecological validation, not as direct evidence that a gene is essential in nature. [src: core_gene_tradeoffs]

## Possible Reconciliations

- **Hypothesis — measurement scale:** Continuous fitness may preserve graded information about gene disruption, whereas thresholding converts that signal into a binary call and can discard distinctions relevant to knockout lethality.
- **Hypothesis — perturbation modality:** Complete knockouts and transposon insertions may produce different biological effects, so disagreement could reflect the perturbation itself rather than a simple failure of one assay.
- **Hypothesis — coverage and detectability:** An apparently neutral singleton may result from poor transposon coverage, making missing or weak fitness evidence difficult to distinguish from genuine functional neutrality.
- **Hypothesis — ecological scope:** Laboratory burden plus conservation may identify genes that are costly and conserved without proving that they are essential under natural conditions.

## Resolving Work

- Compare continuous inverted-fitness values and thresholded essentiality calls for the same genes, using receiver-operating-characteristic and calibration analyses to test how much predictive information is lost through thresholding.
- Measure transposon insertion coverage for singleton and apparently neutral genes, then test whether coverage-adjusted fitness estimates alter the conservation gradient or essentiality classification.
- Run matched complete-knockout and transposon-perturbation experiments under the same conditions to determine whether assay discordance is caused by perturbation modality.
- Test costly and conserved genes across ecologically relevant environments, asking whether laboratory burden predicts fitness costs outside the laboratory.
- Evaluate whether conservation, coverage, continuous fitness, and knockout phenotype jointly improve prediction over any individual measurement.
