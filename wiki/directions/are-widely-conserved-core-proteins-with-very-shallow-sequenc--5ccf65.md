---
type: "Research direction"
description: "Hundreds of thousands of core gene clusters have very shallow sequence families and are rarely annotated with an enzyme or pathway. Does their conservation reflect essential or condition-critical roles in their lineages, or is it an artefact of over-sampled genera and of depth measured on one representative sequence?"
hypothesis: "Core proteins with shallow sequence families are more often essential or strongly condition-dependent than deep-family core proteins of similar length. Their conservation then reflects selection on lineage-restricted functions, not sampling bias."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "The low-depth core cluster list and fitness data both exist, but the join of cluster representatives to Fitness Browser genes has not been run and member-level depth must be computed."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser", "kbase-uniprot"]
findings: ["alphafold_msa_annotation--b7b252bd", "alphafold_msa_annotation--f4d7e00d", "alphafold_msa_annotation--3386d12a", "essential_genome--a70d258c"]
conflicts: []
papers: ["41273079", "34791371", "29769716", "36097170"]
builds_on: ["findings/alphafold_msa_annotation--b7b252bd", "findings/alphafold_msa_annotation--f4d7e00d", "findings/alphafold_msa_annotation--3386d12a", "findings/essential_genome--a70d258c"]
projects: ["alphafold_msa_annotation", "essential_genome"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Are widely conserved core proteins with very shallow sequence families quietly essential?

Hundreds of thousands of core gene clusters have very shallow sequence families and are rarely annotated with an enzyme or pathway. Does their conservation reflect essential or condition-critical roles in their lineages, or is it an artefact of over-sampled genera and of depth measured on one representative sequence?

## Hypothesis

Core proteins with shallow sequence families are more often essential or strongly condition-dependent than deep-family core proteins of similar length. Their conservation then reflects selection on lineage-restricted functions, not sampling bias.

## Why it matters

If shallow core proteins are disproportionately essential, they are the best-justified targets for structure-based function discovery. If not, the conserved-yet-novel population is largely a sampling artefact and the unannotated core is smaller than it looks.

## How to test it

Map the shallow-family core clusters to Fitness Browser genes through the Pangenome Collection and compare essentiality and strong condition-specific fitness with deep-family core clusters. Depth was looked up only for each cluster's representative sequence, so recompute depth for the fitness-tested gene itself and for several members, and drop clusters where these disagree. Match on gene length, because short genes get fewer transposon insertions. Repeat within Pseudomonas and E. coli separately and in less sampled lineages, since these genera are over-represented. Follow up with knockdown phenotyping of a few top candidates in E. coli K-12.

## What would support or refute it

Support: after length matching and member-level depth checks, shallow core genes show more essentiality or condition-specific defects in several lineages. Refute: they look like deep core genes once length is controlled, or the enrichment appears only in the over-sampled genera or only with representative-sequence depth.

## Data

Approach: analysis then experiment. Readiness: needs compute. The low-depth core cluster list and fitness data both exist, but the join of cluster representatives to Fitness Browser genes has not been run and member-level depth must be computed.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]

## Builds on

- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--f4d7e00d|Core clusters have much deeper MSAs than accessory clusters]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--3386d12a|Domain annotation richness rises steadily with MSA depth in core clusters]] (Insufficient literature evidence)
- Finding: [[findings/essential_genome--a70d258c|Orphan essential genes are mostly uncharacterized compared with universal ones]] (Insufficient literature evidence)

## Closest published work

- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 34791371](https://pubmed.ncbi.nlm.nih.gov/34791371/) AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 41273079 and PMID 34791371 describe structure coverage of sequence space, and PMID 29769716 reports phenotypes for poorly annotated genes. None asks whether shallow sequence families among conserved genes are enriched for essential functions.
