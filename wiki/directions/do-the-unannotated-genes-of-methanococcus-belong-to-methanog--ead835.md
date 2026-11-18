---
type: "Research direction"
description: "Two Methanococcus strains hold more than half of all truly dark genes. Are these genes functionally coherent archaeal biology that annotation databases lack, or an unstructured collection?"
hypothesis: "The dark genes of Methanococcus have strong co-fitness partners enriched for annotated methanogenesis, cofactor and nutrient-utilization genes. The partners are concentrated in a small number of coherent groups, not scattered at random."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness tables for both strains are in the catalog; the module grouping and cross-archaea family lookup need new computation."
databases: ["kbase.uniref50", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.specog", "kescience.fitnessbrowser.experiment", "kbase.uniref50.clustermember"]
findings: ["truly_dark_genes--d1b84273", "truly_dark_genes--92c362cf"]
conflicts: []
papers: ["39120137", "29769716", "38977308"]
builds_on: ["findings/truly_dark_genes--d1b84273", "findings/truly_dark_genes--92c362cf"]
projects: ["truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do the unannotated genes of Methanococcus belong to methanogen-specific energy and cofactor metabolism?

Two Methanococcus strains hold more than half of all truly dark genes. Are these genes functionally coherent archaeal biology that annotation databases lack, or an unstructured collection?

## Hypothesis

The dark genes of Methanococcus have strong co-fitness partners enriched for annotated methanogenesis, cofactor and nutrient-utilization genes. The partners are concentrated in a small number of coherent groups, not scattered at random.

## Why it matters

If true, a small set of archaeal-specific functions explains much of the remaining dark gene space. Targeted methanogen work would then be a more efficient route to it than broad surveys.

## How to test it

Using the transposon-fitness compendium, collect the dark genes of the two Methanococcus strains and their co-fit partners. Test whether the partners are enriched for annotated methanogenesis and cofactor functions beyond a gene-length-matched random set. Check whether the same dark genes are conserved in the other Methanococcus strain and in other archaea, using the protein-cluster resources. Group dark genes by shared partners to get testable modules.

## What would support or refute it

Support: partner enrichment for methanogenesis or cofactor functions, with the dark genes falling into a few modules shared by both strains. Refute: partners are no more functional than random and modules are not shared between strains.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness tables for both strains are in the catalog; the module grouping and cross-archaea family lookup need new computation.

## Builds on

- Finding: [[findings/truly_dark_genes--d1b84273|Archaeal Methanococcus strains dominate the truly dark gene set]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--92c362cf|Reannotation resolves most dark genes, leaving small truly dark core]] (Insufficient literature evidence)

## Closest published work

- [PMID 39120137](https://pubmed.ncbi.nlm.nih.gov/39120137/) High-throughput genetics enables identification of nutrient utilization and accessory energy metabolism genes in a model methanogen.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38977308](https://pubmed.ncbi.nlm.nih.gov/38977308/) Large-scale investigation of species-specific orphan genes in the human gut microbiome elucidates their evolutionary origins.

PMID 39120137 maps nutrient and energy-metabolism genes in a model methanogen by high-throughput genetics. It does not ask what the genes that remain unannotated after reannotation are doing.
