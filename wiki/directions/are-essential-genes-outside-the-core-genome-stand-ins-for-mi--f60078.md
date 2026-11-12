---
type: "Research direction"
description: "Many essential genes are not in the core genome, and they are enriched in ribosome, DNA replication, type 4 secretion and plasmid replication functions. Are these strain-specific replacements that matter only where the core copy is absent, or are they mobile-element addiction genes?"
hypothesis: "Essential non-core genes in ribosome and DNA-replication functions are found mostly in genomes that lack a core paralog of the same function. Those in secretion and plasmid functions sit next to mobile-element markers instead."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Gene, annotation, cluster and genome tables are listed, but the catalog match did not show the table linking individual genes to clusters or the Fitness Browser-to-pangenome link that the paralog search needs."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedannotation", "kescience.fitnessbrowser.seedroles", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome"]
findings: ["conservation_vs_fitness--f320d5c5", "conservation_vs_fitness--e95508d3"]
conflicts: []
papers: ["33760724", "36097170", "33753464", "25775563"]
builds_on: ["findings/conservation_vs_fitness--f320d5c5", "findings/conservation_vs_fitness--e95508d3"]
projects: ["conservation_vs_fitness"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Are essential genes outside the core genome stand-ins for missing core machinery?

Many essential genes are not in the core genome, and they are enriched in ribosome, DNA replication, type 4 secretion and plasmid replication functions. Are these strain-specific replacements that matter only where the core copy is absent, or are they mobile-element addiction genes?

## Hypothesis

Essential non-core genes in ribosome and DNA-replication functions are found mostly in genomes that lack a core paralog of the same function. Those in secretion and plasmid functions sit next to mobile-element markers instead.

## Why it matters

The first outcome would show that essentiality can be reassigned between lineages by genome context. The second would show that part of apparent essentiality is dependence on selfish elements. Each changes how essential-gene lists are used as drug-target or minimal-genome catalogues.

## How to test it

For the essential non-core genes in the Fitness Browser organisms, assign functions from the SEED annotations. Using the pangenome gene-cluster and genome tables, plus the table linking genes to their clusters, ask for each gene whether genomes of the same species lacking it carry a core paralog with the same function. Separately, test whether the secretion and plasmid genes lie within a few genes of transposase, integrase or phage genes. Compare with matched non-essential non-core genes. Exclude clades with very few genomes, where core status is trivially high.

## What would support or refute it

Support: replication and ribosome-type essential non-core genes show mutually exclusive presence with a core paralog, and the plasmid-type ones sit by mobile-element genes. Refute: they co-occur with a core paralog as often as other genes, or have no mobile-element association.

## Data

Approach: lakehouse analysis. Readiness: unknown. Gene, annotation, cluster and genome tables are listed, but the catalog match did not show the table linking individual genes to clusters or the Fitness Browser-to-pangenome link that the paralog search needs.

## Builds on

- Finding: [[findings/conservation_vs_fitness--f320d5c5|Essential-auxiliary genes are poorly characterized and may reflect strain-specific machinery]] (Extends retrieved work)
- Finding: [[findings/conservation_vs_fitness--e95508d3|Putative essential genes are modestly more often core than non-essential genes]] (Insufficient literature evidence)

## Closest published work

- [PMID 33760724](https://pubmed.ncbi.nlm.nih.gov/33760724/) In vitro exploration of the Xanthomonas hortorum pv. vitians genome using transposon insertion sequencing and comparative genomics to discriminate between core and contextual essential genes.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 33753464](https://pubmed.ncbi.nlm.nih.gov/33753464/) Non-essential ribosomal proteins in bacteria and archaea identified using COGs.
- [PMID 25775563](https://pubmed.ncbi.nlm.nih.gov/25775563/) Essential genome of Pseudomonas aeruginosa in cystic fibrosis sputum.

PMID 33760724 links essential genes outside the core to mobile elements in Xanthomonas, and PMID 36097170 shows strain-dependent essentiality in S. pneumoniae. Neither tests whether the non-core essential genes substitute for a missing core paralog.
