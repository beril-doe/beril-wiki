---
type: "Research direction"
description: "Only 25 of 3109 genomes (0.8%) carry both an aromatic and a non-aromatic callable capacity, and generalists (3 or more capacities) number 18 against 675 specialists. Is this exclusion selective, or a phylogenetic and annotation artifact?"
hypothesis: "Aromatic and non-aromatic capacities are co-carried less often than expected after phylogeny is controlled, because aromatic catabolism imposes metabolic or regulatory costs that favour specialization. If exclusion vanishes within clades, it is only a clade trait."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome-level capacity calls exist for 3109 genomes, but the phylogeny-aware co-occurrence model must be built and the callable set is only 8 capacities."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["enigma_carbon_census_1--16f93626", "enigma_carbon_census_1--8b8214bb", "enigma_carbon_census_1--bc52527b"]
conflicts: []
papers: ["22026719", "17030797", "11260461"]
builds_on: ["findings/enigma_carbon_census_1--16f93626", "findings/enigma_carbon_census_1--8b8214bb", "findings/enigma_carbon_census_1--bc52527b"]
projects: ["enigma_carbon_census_1"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Why do aromatic and non-aromatic catabolic capacities almost never share a genome?

Only 25 of 3109 genomes (0.8%) carry both an aromatic and a non-aromatic callable capacity, and generalists (3 or more capacities) number 18 against 675 specialists. Is this exclusion selective, or a phylogenetic and annotation artifact?

## Hypothesis

Aromatic and non-aromatic capacities are co-carried less often than expected after phylogeny is controlled, because aromatic catabolism imposes metabolic or regulatory costs that favour specialization. If exclusion vanishes within clades, it is only a clade trait.

## Why it matters

A selective cost would give an ecological explanation for why catabolic versatility is concentrated in Paraburkholderia, Burkholderia and Hydrogenophaga. A pure clade effect would show it is not a portable module.

## How to test it

Expand the 8 callable aromatic/alkaloid capacities (corrected to exclude xanthine) with the compound-to-pathway map. Within Burkholderiales genera in the Pangenome Collection, test co-occurrence of aromatic and non-aromatic capacities using phylogenetic logistic regression, with Haldane-corrected odds ratios and Jaccard indices (about 0.04 for the enriched phenylethylamine pairs). Compare co-occurrence in generalist genera with the rest, and relate it to genome size and respiratory gene content.

## What would support or refute it

Support: co-occurrence stays below expectation within clades after phylogenetic control, including inside generalist genera. Refute: exclusion disappears once clade is modelled, or rare capacities alone explain the low Jaccard.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome-level capacity calls exist for 3109 genomes, but the phylogeny-aware co-occurrence model must be built and the callable set is only 8 capacities.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/enigma_carbon_census_1--16f93626|Aromatic and non-aromatic capacities almost never occur in the same genome]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--8b8214bb|Callable capacity mostly single-capacity, Burkholderiales-concentrated, suggesting a clade trait]] (Extends retrieved work)
- Finding: [[findings/enigma_carbon_census_1--bc52527b|Xanthine was mis-included as a carbon-catabolic callable compound]] (Established in retrieved literature)

## Closest published work

- [PMID 22026719](https://pubmed.ncbi.nlm.nih.gov/22026719/) Genomic analysis of the potential for aromatic compounds biodegradation in Burkholderiales.
- [PMID 17030797](https://pubmed.ncbi.nlm.nih.gov/17030797/) Burkholderia xenovorans LB400 harbors a multi-replicon, 9.73-Mbp genome shaped for versatility.
- [PMID 11260461](https://pubmed.ncbi.nlm.nih.gov/11260461/) The phenylacetyl-CoA catabolon: a complex catabolic unit with broad biotechnological applications.

PMID 22026719 reports aromatic catabolic versatility as a lineage-level property shaped by habitat in 80 Burkholderiales genomes, but does not test whether aromatic and non-aromatic capacities are co-carried less than expected.
