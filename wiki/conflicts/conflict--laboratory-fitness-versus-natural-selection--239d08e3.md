<!-- tension-hash: 239d08e358ff3c3b -->
# Does the essential-gene conservation gradient survive adjustment for gene length and scope?

Projects linking laboratory fitness to pangenome conservation (whether a gene belongs to the core genome shared across a species' genomes) report effects that cannot be compared directly. Two cross-organism estimates of how often essential genes are core come from different cohorts and definitions. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness] A single-organism model improves when gene length is added to fitness. [src: field_vs_lab_fitness] The broad analyses report a weak gradient without adjusting for length. [src: fitness_effects_conservation, conservation_fitness_synthesis] The [[concepts/laboratory-fitness-versus-natural-selection]] argument depends on this point: if much of the gradient reflects gene length or other confounders, laboratory fitness is an even weaker proxy for natural selection than the broad analyses imply.

## Evidence Sides

**Broad cross-organism analyses: a real but weak gradient, without length adjustment**

The broad synthesis estimates that 82% of essential genes are core. [src: conservation_fitness_synthesis] A separate 33-organism linkage of Fitness Browser essentiality calls to pangenome conservation estimates 86.1%. [src: conservation_vs_fitness] These are an unresolved scope tension, not competing measurements, because their cohorts and definitions differ. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness] Broader analyses report a real but weak gradient between fitness importance and conservation, with no adjustment for gene length. [src: fitness_effects_conservation, conservation_fitness_synthesis]

**Within-organism DvH model: adding gene length improves prediction**

In *Desulfovibrio vulgaris* Hildenborough (DvH), models predicting conservation from fitness alone reached a cross-validated area under the receiver operating characteristic curve (CV-AUC, a measure of how well a model separates classes on held-out data) of 0.517–0.548. Adding gene length raised CV-AUC to 0.645. [src: field_vs_lab_fitness] This result comes from a single organism and should be treated as such.

These results do not estimate a shared model. The open question is how much of the broad gradient survives explicit adjustment for length, insertion callability (whether transposon insertions can be detected in a gene), phylogeny and pangenome coverage. [src: field_vs_lab_fitness] [src: fitness_effects_conservation, conservation_fitness_synthesis]

## Possible Reconciliations

- *Hypothesis:* Gene length confounds both essentiality calls and core status across organisms, so part of the broad gradient is a length effect.
- *Hypothesis:* The gap between the 82% and 86.1% estimates reflects differences in cohort membership and essentiality definitions, not a disagreement about biology. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness]
- *Hypothesis:* DvH is atypical, and adjusting for length in other organisms would leave more of the fitness–conservation gradient intact.

## Resolving Work

- **Data:** the 33-organism Fitness Browser cohort, restricted to genes shared with the broad synthesis cohort. **Method:** recompute core fraction under one shared essentiality definition. **Question:** does the scope gap between the two estimates close under matched cohorts and definitions?
- **Data:** per-gene fitness, length and core status for every organism in the broad synthesis. **Method:** per-organism logistic models (models estimating the probability of a binary outcome) with and without length, compared by CV-AUC. **Question:** is the DvH length effect general?
- **Data:** transposon insertion density per gene. **Method:** add an insertion-callability covariate (an explanatory variable included in a model) to the models. **Question:** does part of the "essential" signal reflect genes that cannot receive detectable insertions?
- **Data:** a species phylogeny alongside the gene-level tables. **Method:** phylogenetic mixed models of core status (models that account for relatedness through shared ancestry). **Question:** does the gradient persist once shared ancestry is controlled for?
- **Data:** genome counts per species pangenome. **Method:** stratify the gradient by pangenome coverage. **Question:** is the gradient weaker or stronger in well-sampled pangenomes?
