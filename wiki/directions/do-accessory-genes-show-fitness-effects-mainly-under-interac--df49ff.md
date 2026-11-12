---
type: "Research direction"
description: "Genes with condition-specific phenotypes are more often core than accessory, and singleton genes look neutral in lab screens. Is that because most tested conditions are chemical or nutrient, while accessory genes may matter mainly in interactions such as mixed communities?"
hypothesis: "Accessory genes lag behind core genes in showing condition-specific fitness effects under nutrient and chemical conditions, but the lag shrinks under interaction-type conditions such as mixed-community growth."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Fitness data and pangenome links exist, but the number of interaction-type experiments per organism is not stated and may be small."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["fitness_effects_conservation--ae67b7f2", "fitness_effects_conservation--13498333", "fitness_effects_conservation--87474237", "fitness_effects_conservation--e931cad7"]
conflicts: []
papers: ["29769716", "25968644"]
builds_on: ["findings/fitness_effects_conservation--ae67b7f2", "findings/fitness_effects_conservation--13498333", "findings/fitness_effects_conservation--87474237", "findings/fitness_effects_conservation--e931cad7"]
projects: ["fitness_effects_conservation"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do accessory genes show fitness effects mainly under interaction conditions rather than chemical conditions?

Genes with condition-specific phenotypes are more often core than accessory, and singleton genes look neutral in lab screens. Is that because most tested conditions are chemical or nutrient, while accessory genes may matter mainly in interactions such as mixed communities?

## Hypothesis

Accessory genes lag behind core genes in showing condition-specific fitness effects under nutrient and chemical conditions, but the lag shrinks under interaction-type conditions such as mixed-community growth.

## Why it matters

It would show that the apparent lab neutrality of accessory genes reflects a gap in the tested conditions rather than true uselessness, and tell screen designers which condition classes to add.

## How to test it

First count, per organism, how many Fitness Browser experiments are interaction-type (for example mixed-community growth) versus chemical or nutrient; the test proceeds only for organisms with enough of each. Then, per class, compute the share of core, accessory and singleton genes with strong condition-specific effects, linking genes through the Pangenome Collection and controlling for gene length and insertion coverage.

## What would support or refute it

Support: the accessory shortfall shrinks or disappears in interaction-type classes. Refute: the shortfall is the same size in every class, which favours measurement bias or a genuine lack of effect. If too few interaction-type experiments exist, the question cannot be answered with current data and needs new screens.

## Data

Approach: lakehouse analysis. Readiness: unknown. Fitness data and pangenome links exist, but the number of interaction-type experiments per organism is not stated and may be small.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/fitness_effects_conservation--ae67b7f2|Condition-specific phenotype genes are enriched in the core genome]] (Candidate novel)
- Finding: [[findings/fitness_effects_conservation--13498333|Condition-specific genes are not preferentially accessory]] (Insufficient literature evidence)
- Finding: [[findings/fitness_effects_conservation--87474237|Singleton genes show near-zero fitness, likely invisible to lab assays]] (Insufficient literature evidence)
- Finding: [[findings/fitness_effects_conservation--e931cad7|Neutral-overall, condition-critical genes are commoner among core genes]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

PMID 29769716 reports condition-specific phenotypes for poorly annotated genes but does not split them by core versus accessory status or by interaction conditions.
