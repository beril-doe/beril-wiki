---
type: "Research direction"
description: "Efflux genes shift toward importance under antibiotics (mean shift +0.094) while enzymatic-inactivation genes do not (-0.001), measured against any antibiotic. Is the shift set by whether the drug is a substrate of the specific gene, rather than by mechanism class?"
hypothesis: "Within each mechanism class, an AMR gene becomes important only in experiments with a drug it acts on. Genes that do not shift are narrow-spectrum genes tested against non-matching drugs, not non-functional genes."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Fitness and AMR annotations exist for 25 organisms, but existing class-matched pairs are too few to decide, so competition assays with matched drugs are needed."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["amr_fitness_cost--7ffc7d6b", "amr_fitness_cost--104baecc"]
conflicts: []
papers: ["26203082", "25861385", "29769716", "20208551"]
builds_on: ["findings/amr_fitness_cost--7ffc7d6b", "findings/amr_fitness_cost--104baecc"]
projects: ["amr_fitness_cost"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do efflux genes matter under antibiotics only when the drug is one they pump?

Efflux genes shift toward importance under antibiotics (mean shift +0.094) while enzymatic-inactivation genes do not (-0.001), measured against any antibiotic. Is the shift set by whether the drug is a substrate of the specific gene, rather than by mechanism class?

## Hypothesis

Within each mechanism class, an AMR gene becomes important only in experiments with a drug it acts on. Genes that do not shift are narrow-spectrum genes tested against non-matching drugs, not non-functional genes.

## Why it matters

The apparent mechanism difference would turn out to be a substrate-match effect, which changes how the cost and benefit of a resistance gene are predicted from sequence. A class-matched comparison already done was inconclusive because few gene-drug pairs were available, so the any-antibiotic contrast is not yet evidence for substrate matching.

## How to test it

Step 1, lakehouse: label each antibiotic experiment in the Fitness Browser by drug class and each AMR gene by annotated substrate range, including efflux genes in Cup4G11 and BFirm. Count how many gene-drug pairs each class has, and state which comparisons are too thin to decide. Step 2, experiment: in two organisms with matched and mismatched drugs available, grow efflux and enzymatic-inactivation knockouts in competition with the parent under a matching drug, a non-matching drug and no drug.

## What would support or refute it

Support: fitness importance rises only for matching drugs in both classes, and the efflux-versus-enzymatic gap shrinks once matching is imposed. Refute: broad efflux genes become important regardless of drug match, or non-flipping genes stay neutral even under their own drug class.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Fitness and AMR annotations exist for 25 organisms, but existing class-matched pairs are too few to decide, so competition assays with matched drugs are needed.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_fitness_cost--7ffc7d6b|Efflux genes flip toward importance under antibiotics more than enzymatic inactivation genes]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--104baecc|Fitness cost does not vary by resistance mechanism]] (Candidate novel)

## Closest published work

- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.
- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?

PMID 26203082 shows resistance genes help in vivo but does not split by mechanism or drug match; PMID 25861385 covers resistance mutations, not native AMR genes.
