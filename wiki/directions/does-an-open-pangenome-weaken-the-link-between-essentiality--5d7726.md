---
type: "Research direction"
description: "Essential genes are only modestly more often core than other genes, and the enrichment is clearly present in only about half the organisms. Does the enrichment fade in species with open, diverse pangenomes, where strains may supply essential functions through accessory genes?"
hypothesis: "The strength of essential-gene core enrichment declines with pangenome openness across organisms, even after matching the number of genomes per species."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Per-organism enrichment results and pangenome tables exist; only the openness comparison across organisms is new."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["conservation_vs_fitness--23e6bd24", "conservation_vs_fitness--e95508d3", "essential_genome--876909a2"]
conflicts: []
papers: ["36097170", "38948139", "39012116", "42348439"]
builds_on: ["findings/conservation_vs_fitness--23e6bd24", "findings/conservation_vs_fitness--e95508d3", "findings/essential_genome--876909a2"]
projects: ["conservation_vs_fitness", "essential_genome"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Does an open pangenome weaken the link between essentiality and core status?

Essential genes are only modestly more often core than other genes, and the enrichment is clearly present in only about half the organisms. Does the enrichment fade in species with open, diverse pangenomes, where strains may supply essential functions through accessory genes?

## Hypothesis

The strength of essential-gene core enrichment declines with pangenome openness across organisms, even after matching the number of genomes per species.

## Why it matters

It would explain why conservation is a poor essentiality predictor in some lineages and show that essentiality depends on pangenome structure, guiding when conservation can be used to flag drug targets.

## How to test it

For each of the 33 organisms, take the essential-gene core enrichment from the Fitness Browser linked to the Pangenome Collection. Compute openness on genome-count-matched resamples and compare with enrichment across organisms, adding lineage as a covariate. Examine the organisms with no enrichment individually.

## What would support or refute it

Support: enrichment weakens steadily as openness rises after genome-count matching. Refute: enrichment is unrelated to openness, leaving thin sampling or biology unrelated to pangenome structure as explanations.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Per-organism enrichment results and pangenome tables exist; only the openness comparison across organisms is new.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/conservation_vs_fitness--23e6bd24|Essential-gene core enrichment is significant in just over half of organisms]] (Extends retrieved work)
- Finding: [[findings/conservation_vs_fitness--e95508d3|Putative essential genes are modestly more often core than non-essential genes]] (Insufficient literature evidence)
- Finding: [[findings/essential_genome--876909a2|Clade size does not predict essentiality rate; core link weak]] (Candidate novel)

## Closest published work

- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 39012116](https://pubmed.ncbi.nlm.nih.gov/39012116/) Pangenome evaluation of gene essentiality in Streptococcus pyogenes.
- [PMID 42348439](https://pubmed.ncbi.nlm.nih.gov/42348439/) Integrated analysis of transposon insertion sequencing and pangenome reveals core and lineage-specific essential genes in Mycobacterium avium subsp. hominissuis.

PMID 36097170, PMID 39012116 and PMID 42348439 describe core and strain-specific essential genes within single species or genera, and PMID 38948139 relates fitness to core status in one species. None relates enrichment strength to pangenome openness across organisms.
