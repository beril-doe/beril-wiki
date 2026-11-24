---
type: "Research direction"
description: "Resistance mechanism does not explain baseline fitness cost of AMR genes, but efflux genes flip more strongly under antibiotics, so is mechanism a condition-dependent trait?"
hypothesis: "Efflux genes are the only mechanism class whose fitness effect changes sign between antibiotic and non-antibiotic conditions across organisms, while baseline cost stays similar across classes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness and AMR annotation tables are in the catalog, but gene-to-cluster mapping and mechanism classification must be built."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kbase.ke_pangenome.bakta_amr"]
findings: ["amr_fitness_cost--7ffc7d6b", "amr_fitness_cost--0371e1c6", "amr_fitness_cost--67395444"]
conflicts: []
papers: ["26203082", "25861385", "20208551", "29769716"]
builds_on: ["findings/amr_fitness_cost--7ffc7d6b", "findings/amr_fitness_cost--0371e1c6", "findings/amr_fitness_cost--67395444"]
projects: ["amr_fitness_cost"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Does resistance mechanism matter for fitness only when antibiotics are present?

Resistance mechanism does not explain baseline fitness cost of AMR genes, but efflux genes flip more strongly under antibiotics, so is mechanism a condition-dependent trait?

## Hypothesis

Efflux genes are the only mechanism class whose fitness effect changes sign between antibiotic and non-antibiotic conditions across organisms, while baseline cost stays similar across classes.

## Why it matters

It would separate baseline cost from conditional benefit and show that mechanism predicts conservation through conditional benefit, not constant cost.

## How to test it

Annotate AMR genes in Fitness Browser organisms with pangenome AMR calls. Split experiments into antibiotic and non-antibiotic. Compare fitness shifts by mechanism class within organisms that have many AMR genes, and test whether efflux pumps of broad and narrow spectrum differ.

## What would support or refute it

Support: only efflux shows a clear flip within organisms, with equal baseline cost across classes. Refute: the flip disappears within organisms or appears in enzymatic genes once antibiotic class is matched.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness and AMR annotation tables are in the catalog, but gene-to-cluster mapping and mechanism classification must be built.

## Builds on

- Finding: [[findings/amr_fitness_cost--7ffc7d6b|Efflux genes flip more strongly under antibiotics than enzymatic genes]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--0371e1c6|Resistance mechanism does not explain AMR fitness cost differences]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--67395444|Mechanism predicts pangenome conservation of AMR genes]] (Candidate novel)

## Closest published work

- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.
- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

25861385 and 20208551 cover resistance cost in general, and 26203082 covers in vivo fitness; none compares conditional fitness flips across mechanism classes.
