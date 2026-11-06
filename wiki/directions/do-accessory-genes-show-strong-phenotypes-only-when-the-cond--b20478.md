---
type: "Research direction"
description: "Genes with strong condition-specific effects are more often core than accessory. Is that because accessory genes were simply not tested under the conditions they serve, or because their effects are weaker?"
hypothesis: "Accessory genes cause strong growth changes mainly in the specific condition their annotation predicts (for example efflux genes under their metal). The core excess therefore reflects a mismatch between lab conditions and accessory gene function, not weaker accessory effects."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Fitness data and pangenome core labels are in the lakehouse, but matching annotation-predicted conditions to experiments needs new curation and compute."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["fitness_effects_conservation--ae67b7f2", "conservation_fitness_synthesis--0c074210", "fitness_effects_conservation--e931cad7", "metal_specificity--fed6dcbd"]
conflicts: []
papers: ["29769716", "38948139", "21592774", "42262111"]
builds_on: ["findings/fitness_effects_conservation--ae67b7f2", "findings/conservation_fitness_synthesis--0c074210", "findings/fitness_effects_conservation--e931cad7", "findings/metal_specificity--fed6dcbd"]
projects: ["conservation_fitness_synthesis", "fitness_effects_conservation", "metal_specificity"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do accessory genes show strong phenotypes only when the condition matches their function?

Genes with strong condition-specific effects are more often core than accessory. Is that because accessory genes were simply not tested under the conditions they serve, or because their effects are weaker?

## Hypothesis

Accessory genes cause strong growth changes mainly in the specific condition their annotation predicts (for example efflux genes under their metal). The core excess therefore reflects a mismatch between lab conditions and accessory gene function, not weaker accessory effects.

## Why it matters

It would show whether 'condition-specific does not mean niche-specific' is a limit of lab panels or a real property of bacterial genomes. That changes how accessory genes are screened for function.

## How to test it

In the Fitness Browser, tag each gene with the condition class its annotation predicts, such as metal transporters or efflux for metals and catabolic genes for the matching carbon source. Using pangenome core/accessory labels, compare how strongly mutants grow worse or better in annotation-matched conditions versus unmatched ones, separately for core and accessory genes. Restrict to organisms with many metal and carbon experiments, such as Desulfovibrio vulgaris Hildenborough, Pseudomonas stutzeri RCH2 and Bacteroides thetaiotaomicron. Then test a few predicted-condition accessory genes with targeted deletions.

## What would support or refute it

Support: accessory genes show a much larger growth change under matched conditions than under unmatched ones, which core genes do not, and the core excess disappears among matched-condition tests. Refute: accessory genes stay weaker than core genes even under matched conditions, so the gap is not a coverage artefact.

## Data

Approach: analysis then experiment. Readiness: needs compute. Fitness data and pangenome core labels are in the lakehouse, but matching annotation-predicted conditions to experiments needs new curation and compute.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/fitness_effects_conservation--ae67b7f2|Condition-specific phenotype genes are enriched in the core genome]] (Candidate novel)
- Finding: [[findings/conservation_fitness_synthesis--0c074210|Condition-specific fitness effects do not imply accessory status]] (Insufficient literature evidence)
- Finding: [[findings/fitness_effects_conservation--e931cad7|Neutral-overall, condition-critical genes are commoner among core genes]] (Insufficient literature evidence)
- Finding: [[findings/metal_specificity--fed6dcbd|Metal-specific genes are less core-enriched than general-sick genes]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 21592774](https://pubmed.ncbi.nlm.nih.gov/21592774/) Gene dispensability.
- [PMID 42262111](https://pubmed.ncbi.nlm.nih.gov/42262111/) Systemic trade-offs between core and accessory genomes govern stress adaptation in Rhodococcus erythropolis.

PMID 29769716 reports condition-specific phenotypes and PMID 38948139 shows fitness genes enriched in core genes in one rich medium; neither asks whether accessory phenotypes appear when the tested condition matches gene function.
