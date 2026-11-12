---
type: "Research direction"
description: "Acinetobacter ADP1 genes vary smoothly in growth importance across eight carbon sources, and only aromatic degradation forms a discrete module. Does this reflect ADP1's interconnected metabolism, or the single-timepoint gene-deletion assay used to measure it?"
hypothesis: "If ADP1 is measured with barcoded transposon mutants on the same eight carbon sources, gene importance stays smooth, with broad sensitive and tolerant groups and quinate-specific aromatic genes as the only discrete module. Other bacteria measured the same way show more functionally coherent modules."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "ADP1 is absent from the barcoded-fitness collection, so the matched-assay comparison needs a new ADP1 library. The catalog showed experiment, gene and SEED-role tables but not per-gene fitness values."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedroles", "kescience.fitnessbrowser.organism"]
findings: ["adp1_deletion_phenotypes--86a03233", "adp1_deletion_phenotypes--ec39f324", "adp1_deletion_phenotypes--e7f5d7d3", "acinetobacter_adp1_explorer--886c47ff"]
conflicts: []
papers: ["18319726", "25968644", "25374488", "38323821"]
builds_on: ["findings/adp1_deletion_phenotypes--86a03233", "findings/adp1_deletion_phenotypes--ec39f324", "findings/adp1_deletion_phenotypes--e7f5d7d3", "findings/acinetobacter_adp1_explorer--886c47ff"]
projects: ["acinetobacter_adp1_explorer", "adp1_deletion_phenotypes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Is smooth, module-free gene importance an Acinetobacter trait or an assay effect?

Acinetobacter ADP1 genes vary smoothly in growth importance across eight carbon sources, and only aromatic degradation forms a discrete module. Does this reflect ADP1's interconnected metabolism, or the single-timepoint gene-deletion assay used to measure it?

## Hypothesis

If ADP1 is measured with barcoded transposon mutants on the same eight carbon sources, gene importance stays smooth, with broad sensitive and tolerant groups and quinate-specific aromatic genes as the only discrete module. Other bacteria measured the same way show more functionally coherent modules.

## Why it matters

ADP1 deletion data and E. coli chemical-genetic data have been read as disagreeing about whether fitness falls into functional modules. Measuring ADP1 with both methods separates a real organism difference from a measurement artefact. That decides how far condition-specific gene sets can be trusted across studies.

## How to test it

Build a barcoded transposon library in ADP1 and grow it on the same eight carbon sources used for the deletion collection. Cluster genes by their growth profiles with the published ADP1 analysis pipeline. Compare the two ADP1 datasets gene by gene, and test for functional enrichment among clusters. Then use the public barcoded-fitness collection to see which carbon-source experiments exist for Putida, psRCH2 and Keio, and cluster those organisms on matched carbon sources if per-gene fitness values are available. The catalog did not show per-gene fitness values.

## What would support or refute it

Support: barcoded ADP1 is also smooth and aromatic-only, while the other organisms show several coherent modules, so the continuity belongs to ADP1. Refute: barcoded ADP1 shows many discrete modules, so the smooth landscape came from the deletion assay. A third result is smooth profiles in every organism, which would point to a general property.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. ADP1 is absent from the barcoded-fitness collection, so the matched-assay comparison needs a new ADP1 library. The catalog showed experiment, gene and SEED-role tables but not per-gene fitness values.

## Builds on

- Finding: [[findings/adp1_deletion_phenotypes--86a03233|Gene clustering yields no functional enrichment surviving multiple-testing correction]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--ec39f324|Aromatic degradation genes form the only discrete phenotypic module]] (Extends retrieved work)
- Finding: [[findings/adp1_deletion_phenotypes--e7f5d7d3|Eight conditions provide about five independent phenotypic dimensions]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--886c47ff|ADP1 is absent from the Fitness Browser]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.

PMID 18319726 built and phenotyped the ADP1 deletion collection and PMID 25968644 introduced barcoded fitness profiling, but neither measures one organism by both methods; PMID 38323821 found modules in Pseudomonas putida only.
