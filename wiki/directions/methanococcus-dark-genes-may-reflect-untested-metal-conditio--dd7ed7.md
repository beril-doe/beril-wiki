---
type: "Research direction"
description: "Methanococcus strains S2 and JJ hold 55% of the assessed, pangenome-linked truly dark genes. Do these genes have conditional phenotypes under metal or nutrient conditions not yet tested, or are they just unannotatable by bacteria-biased tools?"
hypothesis: "A larger share of Methanococcus maripaludis truly dark genes show strong condition-specific fitness defects under Ni, Co, Cu, Zn, W or Mo manipulation than matched annotated archaeal genes."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Only iron fitness data exist for these strains, so the metal panel requires new RB-TnSeq experiments."
collections: ["kescience-fitnessbrowser"]
findings: ["truly_dark_genes--d1b84273", "truly_dark_genes--ba47a194"]
conflicts: []
papers: ["39120137", "42706541", "29769716"]
builds_on: ["findings/truly_dark_genes--d1b84273", "findings/truly_dark_genes--ba47a194"]
projects: ["truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Methanococcus dark genes may reflect untested metal conditions rather than missing function

Methanococcus strains S2 and JJ hold 55% of the assessed, pangenome-linked truly dark genes. Do these genes have conditional phenotypes under metal or nutrient conditions not yet tested, or are they just unannotatable by bacteria-biased tools?

## Hypothesis

A larger share of Methanococcus maripaludis truly dark genes show strong condition-specific fitness defects under Ni, Co, Cu, Zn, W or Mo manipulation than matched annotated archaeal genes.

## Why it matters

Support would show that part of the archaeal dark fraction is a conditions gap, so function can be recovered by phenotyping. Refutation would point to dispensability in tested conditions or genuinely hard-to-annotate biology.

## How to test it

Run RB-TnSeq (random barcode transposon sequencing) on M. maripaludis S2 and JJ across a Ni, Co, Cu, Zn, W and Mo panel, since only iron fitness data currently exist for these strains. Compare phenotype rates for truly dark genes versus annotated controls, using cofitness as suggestive evidence of shared function. Separately, check whether the archaeal share persists when the unlinked dark genes are included.

## What would support or refute it

Support: dark genes show metal-specific defects above controls. Refute: rates match or fall below controls. Phenotypes show conditional importance, not why annotation failed, and cofitness suggests but does not establish operons.

## Data

Approach: experiment. Readiness: needs new measurements. Only iron fitness data exist for these strains, so the metal panel requires new RB-TnSeq experiments.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/truly_dark_genes--d1b84273|Archaeal Methanococcus strains dominate the truly dark gene set]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--ba47a194|Most truly dark genes carry some clue; few are completely dark]] (Insufficient literature evidence)

## Closest published work

- [PMID 39120137](https://pubmed.ncbi.nlm.nih.gov/39120137/) High-throughput genetics enables identification of nutrient utilization and accessory energy metabolism genes in a model methanogen.
- [PMID 42706541](https://pubmed.ncbi.nlm.nih.gov/42706541/) Large-scale benchmarking of prokaryotic annotation tools across thousands of species.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

PMID 39120137 applied high-throughput genetics to a model methanogen for nutrient utilization, and PMID 42706541 benchmarks annotation tools, but neither tests whether metal-condition phenotypes populate the archaeal truly dark set.
