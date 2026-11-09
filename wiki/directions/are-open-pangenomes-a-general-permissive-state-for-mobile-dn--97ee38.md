---
type: "Research direction"
description: "Within a single phylum, do species with more open pangenomes carry more of every kind of mobile gene, including prophages and resistance genes, or only some?"
hypothesis: "Openness is a lineage-level tolerance for foreign DNA. Within a phylum, openness should predict prophage markers, resistance genes and mobile-element genes alike, while a non-mobile accessory category such as housekeeping variants should show no such link."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Species-level openness, resistance and prophage tables exist; gain and loss modelling on the species tree has not been run."
collections: ["kbase-ke-pangenome"]
findings: ["amr_pangenome_atlas--ee1ea51b", "prophage_amr_comobilization--02e63b0a", "pangenome_openness--737ca282"]
conflicts: ["conflict--pangenome-openness-determinants--0f0709ff", "conflict--phylogenetic-confounding-of-pangenome-associations--7b9c5a6c"]
papers: ["34983386", "30576310", "31639358"]
builds_on: ["findings/amr_pangenome_atlas--ee1ea51b", "findings/prophage_amr_comobilization--02e63b0a", "findings/pangenome_openness--737ca282", "conflicts/conflict--pangenome-openness-determinants--0f0709ff", "conflicts/conflict--phylogenetic-confounding-of-pangenome-associations--7b9c5a6c"]
projects: ["amr_pangenome_atlas", "gene_function_ecological_agora", "pangenome_openness", "prophage_amr_comobilization"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Are open pangenomes a general permissive state for mobile DNA or only resistance?

Within a single phylum, do species with more open pangenomes carry more of every kind of mobile gene, including prophages and resistance genes, or only some?

## Hypothesis

Openness is a lineage-level tolerance for foreign DNA. Within a phylum, openness should predict prophage markers, resistance genes and mobile-element genes alike, while a non-mobile accessory category such as housekeeping variants should show no such link.

## Why it matters

Across all species pooled, openness and resistance are essentially unrelated, yet the link is positive in most tested phyla. A general permissive state would make openness a predictor of how fast a lineage acquires new resistance. Specificity would instead point to selection on resistance.

## How to test it

Using the Pangenome Collection, within each phylum relate openness to resistance-gene count, prophage marker density and mobile-element gene count. Add a non-mobile accessory category as a negative control, with genome count and phylogenetic relatedness modelled. Estimate gain and loss rates on the species tree for each category to ask whether openness predicts acquisition rate or only present-day content.

## What would support or refute it

Support: openness predicts all mobile categories and their gain rates within phyla but not the non-mobile control. Refutation: openness tracks only one category, or none once relatedness is modelled, which would make the within-phylum positives a lineage artefact.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Species-level openness, resistance and prophage tables exist; gain and loss modelling on the species tree has not been run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_pangenome_atlas--ee1ea51b|Overall openness–AMR correlation hides positive within-phylum associations]] (Insufficient literature evidence)
- Finding: [[findings/prophage_amr_comobilization--02e63b0a|Prophage density predicts AMR repertoire breadth across species]] (Extends retrieved work)
- Finding: [[findings/pangenome_openness--737ca282|Pangenome openness is not associated with the phylogeny effect]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--pangenome-openness-determinants--0f0709ff|Does a Null Pooled Openness Association Mean No Association Within Lineages?]]
- Conflict: [[conflicts/conflict--phylogenetic-confounding-of-pangenome-associations--7b9c5a6c|Does the Prophage–AMR Association Survive Shared Ancestry, Given That Pangenome Openness Does Not Predict the Magnitude of Environment or Phylogeny Effects?]]

## Closest published work

- [PMID 34983386](https://pubmed.ncbi.nlm.nih.gov/34983386/) Comparative pangenomics: analysis of 12 microbial pathogen pangenomes reveals conserved global structures of genetic and functional diversity.
- [PMID 30576310](https://pubmed.ncbi.nlm.nih.gov/30576310/) Genetic exchanges are more frequent in bacteria encoding capsules.
- [PMID 31639358](https://pubmed.ncbi.nlm.nih.gov/31639358/) The Ecology and Evolution of Pangenomes.

PMID 34983386 links openness to phylogenetic placement across 12 pathogen species and PMID 30576310 links capsules to larger pan-genomes with more prophages and resistance genes. Neither compares several mobile categories against a non-mobile control within lineages.
