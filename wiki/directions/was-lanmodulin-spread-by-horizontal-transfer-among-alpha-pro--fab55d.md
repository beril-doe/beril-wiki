---
type: "Research direction"
description: "Lanmodulin occurs only in three alpha-Proteobacterial methylotroph families. Was it inherited from a common ancestor and lost elsewhere, or passed sideways between lineages that share habitats?"
hypothesis: "The lanmodulin gene tree disagrees with the species tree, and the gene sits next to mobile-element or insertion-like genes in some genomes, which points to horizontal transfer."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome and annotation data are present; tree building and synteny comparison need new computation."
collections: ["kbase-ke-pangenome", "kbase-uniref"]
findings: ["lanthanide_methylotrophy_atlas--d54adcf1"]
conflicts: []
papers: ["37259003", "35814700", "30351021"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--d54adcf1"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Was lanmodulin spread by horizontal transfer among alpha-Proteobacterial methylotrophs?

Lanmodulin occurs only in three alpha-Proteobacterial methylotroph families. Was it inherited from a common ancestor and lost elsewhere, or passed sideways between lineages that share habitats?

## Hypothesis

The lanmodulin gene tree disagrees with the species tree, and the gene sits next to mobile-element or insertion-like genes in some genomes, which points to horizontal transfer.

## Why it matters

It would explain the narrow distribution and show whether metal-handling proteins move between lineages in the same habitat, which bears on how lanthanide use evolves.

## How to test it

Using the Pangenome Collection, build a gene tree for lanmodulin proteins from the bakta-validated genomes and compare it with the species tree. Test whether closely related species differ in carrying lanmodulin. Check the flanking genes of each copy for transposases, integrases and phage genes, and compare the base composition of the gene with its host genome.

## What would support or refute it

Support: clear gene-tree/species-tree conflict, copies in mobile-associated contexts, and base composition unlike the host. Refutation: the gene tree follows the species tree and the neighbourhood is conserved, which means vertical inheritance with lineage-specific loss.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome and annotation data are present; tree building and synteny comparison need new computation.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--d54adcf1|Bakta-validated lanmodulin is confined to alpha-Proteobacterial methylotroph families]] (Insufficient literature evidence)

## Closest published work

- [PMID 37259003](https://pubmed.ncbi.nlm.nih.gov/37259003/) Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer.
- [PMID 35814700](https://pubmed.ncbi.nlm.nih.gov/35814700/) A Periplasmic Lanthanide Mediator, Lanmodulin, in Methylobacterium aquaticum Strain 22A.
- [PMID 30351021](https://pubmed.ncbi.nlm.nih.gov/30351021/) Lanmodulin: A Highly Selective Lanthanide-Binding Protein from a Lanthanide-Utilizing Bacterium.

PMID 30351021, 35814700 and 37259003 characterise single lanmodulins; none reconstructs how the gene moved among lineages.
