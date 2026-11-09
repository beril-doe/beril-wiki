---
type: "Research direction"
description: "Hypothetical essential genes cannot be tested by deletion. Are functions inferred from the fitness modules of their non-essential orthologs in other organisms actually right, given that an essential gene's function may have diverged from those orthologs?"
hypothesis: "Module-transfer predictions recover the annotated function of known essential genes far more often than random assignment, despite possible functional divergence from the orthologs. If so, predictions for hypothetical essentials are reliable enough to select genes for depletion tests."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Predictions, ortholog families and essentiality calls exist for the hidden-function benchmark, but the depletion tests need new experiments."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["essential_genome--2c306756", "essential_genome--a70d258c"]
conflicts: []
papers: ["29769716", "36097170", "27013737"]
builds_on: ["findings/essential_genome--2c306756", "findings/essential_genome--a70d258c"]
projects: ["essential_genome"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Can fitness-module transfer correctly predict functions of essential genes of unknown function?

Hypothetical essential genes cannot be tested by deletion. Are functions inferred from the fitness modules of their non-essential orthologs in other organisms actually right, given that an essential gene's function may have diverged from those orthologs?

## Hypothesis

Module-transfer predictions recover the annotated function of known essential genes far more often than random assignment, despite possible functional divergence from the orthologs. If so, predictions for hypothetical essentials are reliable enough to select genes for depletion tests.

## Why it matters

Essential genes of unknown function are the hardest part of the dark proteome, since they lack fitness data. A tested prediction method, with its failure rate known, would give a route to assign them functions and target them.

## How to test it

Using the Fitness Browser, hide the annotation of essential genes with well-established functions, rerun module transfer through their non-essential orthologs, and score recovery of the correct family, noting cases where the ortholog's module reflects a diverged role. Include the orphan essentials with no orthologs as a case the method cannot reach. Then deplete several top predictions in a tractable organism and check the growth defect predicted by the module context.

## What would support or refute it

Support: hidden functions are recovered well above shuffled assignment and depletion phenotypes match the predicted context. Refutation: recovery is near chance, or predictions fail in depletion, meaning the orthologs' module context does not carry over to essential genes because function has diverged.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Predictions, ortholog families and essentiality calls exist for the hidden-function benchmark, but the depletion tests need new experiments.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/essential_genome--2c306756|Module transfer yields function predictions for hypothetical essential genes]] (Extends retrieved work)
- Finding: [[findings/essential_genome--a70d258c|Orphan essential genes are mostly uncharacterized compared with universal ones]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 27013737](https://pubmed.ncbi.nlm.nih.gov/27013737/) Design and synthesis of a minimal bacterial genome.

PMID 29769716 supports function proposals from conserved fitness associations among genes that have mutant data, and PMID 36097170 treats strain-dependent essentiality. Neither benchmarks predictions made indirectly for genes that lack fitness data.
