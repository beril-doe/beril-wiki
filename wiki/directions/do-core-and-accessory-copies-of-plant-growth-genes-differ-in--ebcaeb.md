---
type: "Research direction"
description: "Plant-growth genes are mostly core in their species, yet they co-occur strongly with transposases. Can both hold, with widespread copies on the chromosome and rare copies inside mobile regions?"
hypothesis: "Within species carrying acdS, nifH or pqqC, the copies found in only a minority of conspecific genomes lie in or near annotated mobile elements far more often than the copies found in most conspecific genomes."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Annotation, genome and mobile-element tables are in the catalog, but whether gene identifiers can be placed on element coordinates was not shown."
databases: ["kescience.mgnify"]
tables: ["kescience.mgnify.gene_eggnog", "kescience.mgnify.gene_mobilome", "kescience.mgnify.genome"]
findings: ["pgp_pangenome_ecology--45e0cc45", "plant_microbiome_ecotypes--223dadd3"]
conflicts: ["conflict--horizontal-gene-transfer-driven-innovation--9137941d"]
papers: ["24905353", "41724873", "34946069"]
builds_on: ["findings/pgp_pangenome_ecology--45e0cc45", "findings/plant_microbiome_ecotypes--223dadd3", "conflicts/conflict--horizontal-gene-transfer-driven-innovation--9137941d"]
projects: ["pgp_pangenome_ecology", "plant_microbiome_ecotypes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do core and accessory copies of plant-growth genes differ in mobile-element context?

Plant-growth genes are mostly core in their species, yet they co-occur strongly with transposases. Can both hold, with widespread copies on the chromosome and rare copies inside mobile regions?

## Hypothesis

Within species carrying acdS, nifH or pqqC, the copies found in only a minority of conspecific genomes lie in or near annotated mobile elements far more often than the copies found in most conspecific genomes.

## Why it matters

Two projects read the spread of plant-growth traits in opposite ways. A copy-level split would turn that disagreement into a biological result and show which trait copies move between strains.

## How to test it

In the metagenome-assembled genome catalogue, find genomes carrying acdS, nifH, pqqC and hcnC by their KEGG orthologs in the eggNOG annotation. Group genomes by species and call a gene widespread if it occurs in most genomes of its species, otherwise rare. Using the mobile-element table, test whether each copy lies in or near a called element, and compare with housekeeping genes of matched prevalence. If gene identifiers do not carry contig coordinates, the proximity step needs the gene-position data, which the catalog did not show.

## What would support or refute it

Support: rare copies are enriched in mobile regions relative to widespread copies and the control. Refute: both classes show the same mobile-element proximity, or neither is near mobile elements, which would make the transposase link a species-level artefact.

## Data

Approach: lakehouse analysis. Readiness: unknown. Annotation, genome and mobile-element tables are in the catalog, but whether gene identifiers can be placed on element coordinates was not shown.

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--45e0cc45|Plant-growth genes are mostly core, rejecting the accessory/HGT hypothesis]] (Extends retrieved work)
- Finding: [[findings/plant_microbiome_ecotypes--223dadd3|Only three plant markers survive strict within-genus permutation]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--horizontal-gene-transfer-driven-innovation--9137941d|Plant-Growth-Promoting Traits: Vertically Inherited Core Genes or Transposase-Linked Mobile Cargo?]]

## Closest published work

- [PMID 24905353](https://pubmed.ncbi.nlm.nih.gov/24905353/) New insights into 1-aminocyclopropane-1-carboxylate (ACC) deaminase phylogeny, evolution and ecological significance.
- [PMID 41724873](https://pubmed.ncbi.nlm.nih.gov/41724873/) Comparative genomic analyses reveal key traits for biocontrol and the promotion of plant growth in Paenibacillus strains.
- [PMID 34946069](https://pubmed.ncbi.nlm.nih.gov/34946069/) Pseudomonas 1-Aminocyclopropane-1-carboxylate (ACC) Deaminase and Its Role in Beneficial Plant-Microbe Interactions.

PMID 24905353 describes acdS as mostly vertically inherited with some transfer, and PMID 41724873 suggests transfer of some plant-growth genes in mobile regions; neither separates widespread from rare copies within species by mobile-element context.
