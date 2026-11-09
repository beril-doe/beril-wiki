---
type: "Research direction"
description: "Some genes are essential in the Fitness Browser organism where they were measured yet are accessory across related genomes, and many are poorly annotated or tied to mobile elements. Do they keep cells alive by replacing a missing core function, or because a mobile element makes the cell dependent on them?"
hypothesis: "Most such genes are addiction-type genes, for example toxin-antitoxin or replication-maintenance genes of plasmids and prophages. They become dispensable once the element is removed, and the strain lacks no core function that they replace."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Fitness calls and pangenome links exist, but the decisive element-curing step needs new strains and growth measurements."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["conservation_vs_fitness--f320d5c5", "conservation_vs_fitness--23e6bd24", "conservation_vs_fitness--e95508d3"]
conflicts: []
papers: ["33760724", "36097170", "22448042", "39012116"]
builds_on: ["findings/conservation_vs_fitness--f320d5c5", "findings/conservation_vs_fitness--23e6bd24", "findings/conservation_vs_fitness--e95508d3"]
projects: ["conservation_vs_fitness"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Are accessory essential genes mobile-element addictions or stand-ins for missing core functions?

Some genes are essential in the Fitness Browser organism where they were measured yet are accessory across related genomes, and many are poorly annotated or tied to mobile elements. Do they keep cells alive by replacing a missing core function, or because a mobile element makes the cell dependent on them?

## Hypothesis

Most such genes are addiction-type genes, for example toxin-antitoxin or replication-maintenance genes of plasmids and prophages. They become dispensable once the element is removed, and the strain lacks no core function that they replace.

## Why it matters

It would show whether the loose link between essentiality and core status mostly reflects selfish DNA rather than flexible genome function. That bears on drug-target choice, since accessory essential genes make poor species-wide targets.

## How to test it

Take the essential-auxiliary genes in Fitness Browser organisms and annotate their neighbourhoods for antitoxins, replication proteins and integrases, and check whether genomes lacking the gene lack the element or lack a core function. Then, for a few genes lying on a plasmid or prophage, cure or delete the element in the host and ask whether the gene stops being essential; compare with essential core genes.

## What would support or refute it

Support: neighbourhoods are enriched for mobile-element partners, and curing the element makes the gene dispensable. Refutation: the genes sit in core-like operons, remain essential after the element is removed, and genomes lacking them lack a core function the gene could replace.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Fitness calls and pangenome links exist, but the decisive element-curing step needs new strains and growth measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/conservation_vs_fitness--f320d5c5|Essential-auxiliary genes are poorly characterized and may reflect strain-specific machinery]] (Extends retrieved work)
- Finding: [[findings/conservation_vs_fitness--23e6bd24|Essential-gene core enrichment is significant in just over half of organisms]] (Extends retrieved work)
- Finding: [[findings/conservation_vs_fitness--e95508d3|Putative essential genes are modestly more often core than non-essential genes]] (Insufficient literature evidence)

## Closest published work

- [PMID 33760724](https://pubmed.ncbi.nlm.nih.gov/33760724/) In vitro exploration of the Xanthomonas hortorum pv. vitians genome using transposon insertion sequencing and comparative genomics to discriminate between core and contextual essential genes.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 39012116](https://pubmed.ncbi.nlm.nih.gov/39012116/) Pangenome evaluation of gene essentiality in Streptococcus pyogenes.

PMID 33760724 links Xanthomonas essential genes outside the core to mobile elements, and PMID 36097170 shows strain-dependent essentiality in S. pneumoniae. Neither separates addiction from compensation by removing the element.
