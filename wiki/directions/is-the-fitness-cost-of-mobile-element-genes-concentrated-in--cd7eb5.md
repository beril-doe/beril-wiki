---
type: "Research direction"
description: "Costly but dispensable genes are mostly mobile-element debris, so does their cost appear everywhere or only under particular conditions?"
hypothesis: "Mobile-element genes show cost in many unrelated experiments within the same organism, whereas costly conserved genes show cost only in a few condition types."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Gene-level fitness, experiment descriptions, gene descriptions and orthologs are in the catalog tables listed."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.ortholog"]
findings: ["costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--e1254d2a", "costly_dispensable_genes--f3a85492"]
conflicts: []
papers: ["29769716", "22448042", "36097170", "40728316"]
builds_on: ["findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--e1254d2a", "findings/costly_dispensable_genes--f3a85492"]
projects: ["costly_dispensable_genes"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Is the fitness cost of mobile-element genes concentrated in particular growth conditions?

Costly but dispensable genes are mostly mobile-element debris, so does their cost appear everywhere or only under particular conditions?

## Hypothesis

Mobile-element genes show cost in many unrelated experiments within the same organism, whereas costly conserved genes show cost only in a few condition types.

## Why it matters

A broad cost would support steady genome-expansion pressure from horizontal transfer. A condition-limited cost would suggest that the cost label partly reflects noise in single experiments or specific stresses.

## How to test it

In the Fitness Browser, take genes with positive fitness in any experiment. Split them into mobile-element keyword genes and conserved genes using gene descriptions and ortholog tables. For each gene, count independent experiments and distinct condition types with positive fitness, and compare the two groups within each organism.

## What would support or refute it

Support: mobile-element genes are costly across many experiments and condition types. Refute: their cost comes mostly from one experiment or one condition class, as for the conserved group.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Gene-level fitness, experiment descriptions, gene descriptions and orthologs are in the catalog tables listed.

## Builds on

- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--e1254d2a|Costly non-conserved genes are mostly mobile-element debris from horizontal transfer]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--f3a85492|SEED phage and transposable element category enriched among costly dispensable genes]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 40728316](https://pubmed.ncbi.nlm.nih.gov/40728316/) Adaptive pangenomic remodeling in the Azolla cyanobiont amid a transient microbiome.

29769716 supplies the fitness data and 22448042 proposes adaptive gene loss; neither asks how widely mobile-element genes are costly across conditions.
