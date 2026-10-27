---
type: "Research direction"
description: "For gapfilled reactions with no convincing gene candidate (52.2% of pairs), and EC-less 'dark' reactions (16% resolved vs 58.3% with EC), is the missing enzyme a novel family or a divergent member of known families?"
hypothesis: "Candidate genes for EC-less gapfilled reactions fall more often in the truly dark set or shallow-MSA clusters, and show no recognizable known-enzyme fold, than candidates for reactions with EC numbers."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Gapfill pairs, fitness data and dark sets exist in the lakehouse, but enzyme assays and structural searches are new work."
collections: ["kescience-fitnessbrowser", "kbase-msd-biochemistry", "kbase-ke-pangenome"]
findings: ["annotation_gap_discovery--ccaed616", "annotation_gap_discovery--61f3d4be", "annotation_gap_discovery--41b7c54a", "annotation_gap_discovery--fa3a9dc4", "alphafold_msa_annotation--b7b252bd"]
conflicts: []
papers: ["30910961", "28823675", "25968644"]
builds_on: ["findings/annotation_gap_discovery--ccaed616", "findings/annotation_gap_discovery--61f3d4be", "findings/annotation_gap_discovery--41b7c54a", "findings/annotation_gap_discovery--fa3a9dc4", "findings/alphafold_msa_annotation--b7b252bd"]
projects: ["alphafold_msa_annotation", "annotation_gap_discovery"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Gapfilled reactions without EC numbers may be catalyzed by novel enzyme families

For gapfilled reactions with no convincing gene candidate (52.2% of pairs), and EC-less 'dark' reactions (16% resolved vs 58.3% with EC), is the missing enzyme a novel family or a divergent member of known families?

## Hypothesis

Candidate genes for EC-less gapfilled reactions fall more often in the truly dark set or shallow-MSA clusters, and show no recognizable known-enzyme fold, than candidates for reactions with EC numbers.

## Why it matters

It would link metabolic-model gaps to unexplored enzyme space, showing whether model failures reflect missing enzyme classes and which dark genes to characterize first.

## How to test it

For the 14 Fitness Browser organisms, compare fitness-significant carbon-source genes for EC-less reactions with those for EC-assigned reactions, scoring overlap with truly dark genes and low-MSA clusters and running structural-family searches. Treat the 96 assigned pairs as candidates, since 33 have only single-stream, low-confidence support. Test top candidates by purified-protein assays of the specific reaction, as knockouts cannot separate direct from indirect pathway effects. Consider alternative gapfill solutions, since default gapfilling minimizes added reactions without guaranteeing optimality.

## What would support or refute it

Support: EC-less candidates are enriched in dark or shallow-MSA sets, lack known folds, and show the predicted activity. Refute: overlap matches EC-assigned reactions or purified enzymes lack the activity, favouring model error or alternative solutions. Draft-model errors limit knockout simulation, which showed zero wildtype growth.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Gapfill pairs, fitness data and dark sets exist in the lakehouse, but enzyme assays and structural searches are new work.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-msd-biochemistry|ModelSEED Biochemistry]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/annotation_gap_discovery--ccaed616|Over half of gapfilled pairs remain without a convincing gene candidate]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--61f3d4be|Dark reactions without EC numbers are far harder to resolve]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--41b7c54a|Knockout simulation could not validate candidate gene assignments]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--fa3a9dc4|Integrated evidence assigned candidate genes to nearly half of gapfilled reactions]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)

## Closest published work

- [PMID 30910961](https://pubmed.ncbi.nlm.nih.gov/30910961/) Enzyme annotation for orphan and novel reactions using knowledge of substrate reactive sites.
- [PMID 28823675](https://pubmed.ncbi.nlm.nih.gov/28823675/) Transposon Sequencing Uncovers an Essential Regulatory Function of Phosphoribulokinase for Methylotrophy.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

PMID 30910961 predicts enzymes for orphan reactions from reactive sites and PMID 28823675 found a methylotrophy gene by transposon sequencing, but neither tests whether unresolved model reactions map onto the dark genome.
