---
type: "Research direction"
description: "Which gene classes make up the extra DNA in deep-clay Bacillota_B genomes relative to soil Bacillota_B, and is the expansion shared across anchor genera?"
hypothesis: "The orthogroups enriched in deep-clay anchors recur across at least two anchor genera and fall into a few functional classes, so the larger genomes reflect shared expansion rather than a few lineage-specific marker genes."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "The orthogroup presence matrix and the anchor and baseline genomes already exist in the pangenome collection; the decomposition is a stratified re-tabulation, although the 10-genome anchor is genus-clumped."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["bacillota_b_subsurface_accessory--0b68d03d", "bacillota_b_subsurface_accessory--b2fd7eb1"]
conflicts: []
papers: ["38902796", "32252814", "40054447", "30728279"]
builds_on: ["findings/bacillota_b_subsurface_accessory--0b68d03d", "findings/bacillota_b_subsurface_accessory--b2fd7eb1"]
projects: ["bacillota_b_subsurface_accessory"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Confinement in deep clay may select genome expansion in Bacillota_B rather than streamlining

Which gene classes make up the extra DNA in deep-clay Bacillota_B genomes relative to soil Bacillota_B, and is the expansion shared across anchor genera?

## Hypothesis

The orthogroups enriched in deep-clay anchors recur across at least two anchor genera and fall into a few functional classes, so the larger genomes reflect shared expansion rather than a few lineage-specific marker genes.

## Why it matters

Retrieved work links groundwater habitats to streamlined genomes, while hadal sediment is reported to favour larger genomes under dispersal limitation. A recurrent expansion signature would show that confined, isolated habitats can push genome size either way, and would identify the gene classes involved.

## How to test it

In the pangenome collection, decompose the 547 enriched orthogroups (anchor n=10 vs baseline n=62) by COG/KEGG class and by anchor genus (BRH-c8a, BRH-c4a, Desulfosporosinus, Desulforudis). Count the enriched orthogroups that recur across at least two genera. Estimate how much of the 35% mean size difference and the ~25% excess eggNOG OGs per genome they account for. Repeat with each genus left out in turn.

## What would support or refute it

Support: enriched orthogroups recur across genera and concentrate in a few classes that explain much of the size gap. Refute: enrichment is mostly genus-specific, so a few lineages drive the difference. A positive result shows expansion in this lineage but not whether gain or loss shaped it.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. The orthogroup presence matrix and the anchor and baseline genomes already exist in the pangenome collection; the decomposition is a stratified re-tabulation, although the 10-genome anchor is genus-clumped.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/bacillota_b_subsurface_accessory--0b68d03d|Deep-clay Bacillota_B genomes are larger than soil baselines, not compact]] (Extends retrieved work)
- Finding: [[findings/bacillota_b_subsurface_accessory--b2fd7eb1|Many orthogroups are enriched in deep-clay anchors versus soil baselines]] (Insufficient literature evidence)

## Closest published work

- [PMID 38902796](https://pubmed.ncbi.nlm.nih.gov/38902796/) Genome streamlining in Parcubacteria transitioning from soil to groundwater.
- [PMID 32252814](https://pubmed.ncbi.nlm.nih.gov/32252814/) Small and mighty: adaptation of superphylum Patescibacteria to groundwater environment drives their genome simplicity.
- [PMID 40054447](https://pubmed.ncbi.nlm.nih.gov/40054447/) Microbial ecosystems and ecological driving forces in the deepest ocean sediments.
- [PMID 30728279](https://pubmed.ncbi.nlm.nih.gov/30728279/) Gene Expansion and Positive Selection as Bacterial Adaptations to Oligotrophic Conditions.

PMID 38902796 and 32252814 tie groundwater lifestyles to smaller genomes, and PMID 40054447 reports that dispersal limitation in hadal sediment favours larger genomes; this direction asks which gene classes and genera produce the larger genomes in a deep-clay lineage.
