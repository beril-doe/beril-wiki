---
type: "Research direction"
description: "Core gene clusters whose sequences have very few relatives in reference sequence space are mostly unannotated. Are they needed for growth as often as deeply represented core genes, or are they largely neutral and merely conserved within a species?"
hypothesis: "After matching for gene length, core genes with very shallow relative depth are at least as often essential or strongly condition-dependent as annotated, deeply represented core genes. Conservation in these proteins then reflects function, not neglect."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The shallow-depth core list and the Fitness Browser links already exist, but the join, length matching and phenotype comparison have not been run, and only organisms with fitness data can be tested."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["alphafold_msa_annotation--b7b252bd", "alphafold_msa_annotation--f4d7e00d", "truly_dark_genes--947aec4f"]
conflicts: []
papers: ["29769716", "34791371", "41273079", "37821698", "32124724"]
builds_on: ["findings/alphafold_msa_annotation--b7b252bd", "findings/alphafold_msa_annotation--f4d7e00d", "findings/truly_dark_genes--947aec4f"]
projects: ["alphafold_msa_annotation", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do conserved proteins with almost no relatives elsewhere matter for growth?

Core gene clusters whose sequences have very few relatives in reference sequence space are mostly unannotated. Are they needed for growth as often as deeply represented core genes, or are they largely neutral and merely conserved within a species?

## Hypothesis

After matching for gene length, core genes with very shallow relative depth are at least as often essential or strongly condition-dependent as annotated, deeply represented core genes. Conservation in these proteins then reflects function, not neglect.

## Why it matters

The census counts 415,603 shallow core clusters, 68.9% of them hypothetical, and reads conservation as importance without measuring it. That census also rests on a genome collection in which Pseudomonas and E. coli are over-represented, so part of the pattern may reflect sampling. If shallow core genes are often needed for growth, they become high-value targets for structure and function work. If not, conservation alone is a poor guide for choosing targets.

## How to test it

Link core gene clusters in the Pangenome Collection to Fitness Browser genes. Split them into shallow-depth and deep-depth classes and compare the share with strong fitness effects in at least one condition and the share that are essential. Match on gene length, because short genes are poorly measured, and stratify by annotation tier and by organism. Depth was looked up only for each cluster's representative sequence, so check a sample of clusters for member-level diversity. Run the comparison on genera with balanced genome sampling, to see whether the over-represented genera drive the pattern.

## What would support or refute it

Support: shallow core genes show strong or essential phenotypes at rates comparable to deep core genes in length-matched comparisons, in balanced genera as well. Refutation: their rates are clearly lower even when length is matched, which would suggest conservation without much measurable importance under lab conditions. If the pattern holds only in the over-represented genera, it reflects sampling and not biology.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The shallow-depth core list and the Fitness Browser links already exist, but the join, length matching and phenotype comparison have not been run, and only organisms with fitness data can be tested.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--f4d7e00d|Core clusters have much deeper MSAs than accessory clusters]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 34791371](https://pubmed.ncbi.nlm.nih.gov/34791371/) AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models.
- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 37821698](https://pubmed.ncbi.nlm.nih.gov/37821698/) Unraveling the functional dark matter through global metagenomics.
- [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/) An assessment of genome annotation coverage across the bacterial tree of life.

PMID 29769716 links mutant phenotypes to poorly annotated genes but does not sort genes by sequence-space depth. PMID 34791371 and PMID 41273079 provide structure coverage, not growth importance.
