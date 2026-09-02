<!-- tension-hash: cb83a09382224a34 -->
# Does Gene Length Outweigh Fitness in Predicting Conservation?

The disagreement concerns how much explanatory and predictive importance should be assigned to fitness relative to gene length and other genomic or ecological covariates. In one dataset, adding gene length substantially improved predictive performance, while broader analyses report a real but weak fitness–conservation relationship without testing gene length directly. The conflict matters because the apparent importance of fitness may depend on whether key structural, phylogenetic, and ascertainment variables are included. The tension is documented on [[concepts/fitness-importance-versus-ecological-context]].

## Evidence Sides

**Gene length is a strong predictor in the DvH model.**  
The DvH model shows that adding gene length raised CV-AUC to 0.645, whereas fitness alone had CV-AUC values of 0.517–0.548, indicating strong predictive importance for length in that dataset. [src: field_vs_lab_fitness]

**Fitness has a real, if weak, broader association with conservation.**  
The broader analyses report a real but weak fitness–conservation gradient and do not test gene length as a covariate. [src: fitness_effects_conservation; conservation_fitness_synthesis] These analyses therefore support a fitness–conservation relationship, but do not establish how its estimated strength would change after accounting for gene length or related genomic factors.

## Possible Reconciliations

- **Hypothesis — Different datasets and organisms:** The DvH result and the broader fitness analyses may describe different biological systems, so gene length could be highly predictive in one dataset while fitness remains associated with conservation across a wider corpus.
- **Hypothesis — Different outcomes or prediction targets:** CV-AUC measures predictive discrimination for a particular modeled outcome, whereas a fitness–conservation gradient may describe an association rather than incremental predictive performance. A variable can therefore improve prediction without explaining the full broader gradient.
- **Hypothesis — Omitted-variable structure:** Gene length may capture insertion callability, annotation quality, mutational opportunity, or other features correlated with both measured fitness and conservation. Adjusting for these factors could weaken, preserve, or clarify the fitness signal.
- **Hypothesis — Phylogenetic and pangenome scope:** The broader gradient may reflect lineage composition or uneven pangenome coverage, while the DvH model may operate within a narrower or differently sampled phylogenetic scope.

## Resolving Work

- Assemble a harmonized dataset containing fitness, conservation, gene length, insertion callability, phylogeny, and pangenome coverage; test whether the fitness coefficient and predictive contribution persist after joint adjustment.
- Refit the DvH model with and without gene length and the proposed confounders; compare cross-validated CV-AUC values using the same folds and outcome definition.
- Perform phylogenetically structured analyses, including lineage-stratified models and models with phylogenetic random effects; ask whether the fitness–conservation gradient remains within lineages.
- Quantify missingness and callability across genes and pangenomes, then test whether correcting for ascertainment changes the apparent fitness effect or the contribution of gene length.
- Compare effect sizes and out-of-sample predictions across organisms and datasets using a prespecified meta-analytic framework.
