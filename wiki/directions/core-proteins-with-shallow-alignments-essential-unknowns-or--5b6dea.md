---
type: "Research direction"
description: "Are core gene clusters with very shallow alignments and almost no annotation functionally important, or do they persist as lineage-bound remnants?"
hypothesis: "Core clusters with MSA depth below 10 carry measurable fitness phenotypes at a higher rate than depth-matched accessory clusters, after gene-length control, and concentrate in specific lineages instead of spreading evenly across phyla."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The census and fitness data are in the lakehouse, but the cluster-to-gene join and length-controlled comparison are not yet done."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser", "kbase-uniprot"]
findings: ["alphafold_msa_annotation--b7b252bd", "alphafold_msa_annotation--f4d7e00d", "alphafold_msa_annotation--0b782ee2", "field_vs_lab_fitness--d31622df"]
conflicts: []
papers: ["29769716", "41273079", "32124724", "36097170"]
builds_on: ["findings/alphafold_msa_annotation--b7b252bd", "findings/alphafold_msa_annotation--f4d7e00d", "findings/alphafold_msa_annotation--0b782ee2", "findings/field_vs_lab_fitness--d31622df"]
projects: ["alphafold_msa_annotation", "field_vs_lab_fitness"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Core proteins with shallow alignments: essential unknowns or relaxed-constraint remnants?

Are core gene clusters with very shallow alignments and almost no annotation functionally important, or do they persist as lineage-bound remnants?

## Hypothesis

Core clusters with MSA depth below 10 carry measurable fitness phenotypes at a higher rate than depth-matched accessory clusters, after gene-length control, and concentrate in specific lineages instead of spreading evenly across phyla.

## Why it matters

It would show whether the 415,603 low-depth clusters (68.9% hypothetical) deserve experimental effort. Shallow depth is only an interpretation of possible novelty, so this tests functional importance, not unprecedented folds.

## How to test it

Join low-depth core clusters to Fitness Browser genes through the pangenome link. Compare the fraction with significant fitness phenotypes against depth-matched accessory clusters and deeper core clusters, controlling for gene length, which confounds both transposon coverage and core status. Map the clusters onto GTDB to find high-density lineages. Depth was taken from each cluster's representative only, and 71% of clusters lack AlphaFold entries.

## What would support or refute it

Support: low-depth core clusters have more fitness phenotypes than depth-matched accessory ones after length control, concentrated in particular lineages. Refute: rates equal to or below accessory clusters, or the signal vanishes after length control.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The census and fitness data are in the lakehouse, but the cluster-to-gene join and length-controlled comparison are not yet done.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]

## Builds on

- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--f4d7e00d|Core clusters have much deeper MSAs than accessory clusters]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--0b782ee2|EC and KEGG annotation almost absent among low-depth core proteins]] (Insufficient literature evidence)
- Finding: [[findings/field_vs_lab_fitness--d31622df|Gene length is judged a stronger predictor of core status than fitness]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/) An assessment of genome annotation coverage across the bacterial tree of life.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 29769716 gives mutant phenotypes for thousands of unknown genes and PMID 32124724 assesses annotation coverage; neither links shallow MSA depth in core clusters to fitness.
