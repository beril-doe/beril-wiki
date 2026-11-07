---
type: "Research direction"
description: "More than half of dark-gene ortholog groups are classed as kingdom-level, meaning the narrowest taxonomic rank containing all their member species is Bacteria. Yet 37 of 48 tested organisms are Pseudomonadota. Do orthologs of a dark gene respond to the same kind of condition in more distant organisms?"
hypothesis: "Pairs of dark orthologs share their strongest condition class more often than shuffled pairings do, but less often than annotated orthologs of equal breadth do. Agreement is lowest with the one Bacteroidetes, Bacteroides thetaiotaomicron."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Ortholog groups, condition labels and fitness records exist for the tested organisms; the agreement scoring is new, and Bacteroides is the only non-Proteobacterial organism available."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["functional_dark_matter--b069dc6a", "functional_dark_matter--1e0e1f03", "annotation_gap_discovery--12a061bc"]
conflicts: []
papers: ["29769716", "22125499", "25968644", "11701626"]
builds_on: ["findings/functional_dark_matter--b069dc6a", "findings/functional_dark_matter--1e0e1f03", "findings/annotation_gap_discovery--12a061bc"]
projects: ["annotation_gap_discovery", "functional_dark_matter"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does a dark gene keep the same phenotype in a distant, non-Proteobacterial relative?

More than half of dark-gene ortholog groups are classed as kingdom-level, meaning the narrowest taxonomic rank containing all their member species is Bacteria. Yet 37 of 48 tested organisms are Pseudomonadota. Do orthologs of a dark gene respond to the same kind of condition in more distant organisms?

## Hypothesis

Pairs of dark orthologs share their strongest condition class more often than shuffled pairings do, but less often than annotated orthologs of equal breadth do. Agreement is lowest with the one Bacteroidetes, Bacteroides thetaiotaomicron.

## Why it matters

It tests whether a phenotype found in one model organism can be carried to relatives that cannot be tested. If agreement is at chance, wide distribution alone would not imply shared function.

## How to test it

For dark ortholog groups with fitness data in two or more Fitness Browser organisms, score whether the strongest condition class agrees between organisms. Compare with shuffled gene pairings and with annotated orthologs of the same breadth. Split pairs into Proteobacteria-only and those involving Bacteroides thetaiotaomicron to see whether agreement falls with phylogenetic distance. Record how many member species and phyla each group actually spans, since kingdom-level only sets an upper rank.

## What would support or refute it

Support: agreement beats the shuffled null but trails annotated orthologs, and is lowest in pairs with Bacteroides thetaiotaomicron. Refutation: agreement equals shuffled pairings, or does not fall with distance.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Ortholog groups, condition labels and fitness records exist for the tested organisms; the agreement scoring is new, and Bacteroides is the only non-Proteobacterial organism available.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/functional_dark_matter--b069dc6a|Over half of dark-gene ortholog groups are pan-bacterial]] (Insufficient literature evidence)
- Finding: [[findings/functional_dark_matter--1e0e1f03|Many unannotated Fitness Browser genes have measurable phenotypes]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--12a061bc|Resolution rates varied widely across organisms, lowest in the Bacteroidetes]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 11701626](https://pubmed.ncbi.nlm.nih.gov/11701626/) How many genes can make a cell: the minimal-gene-set concept.

PMID 29769716 and PMID 22125499 infer functions from phenotypes in one or a few organisms. Neither checks whether widespread dark genes behave consistently across distant lineages.
