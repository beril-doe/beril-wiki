---
type: "Research direction"
description: "Most cystic fibrosis Pseudomonas aeruginosa isolates carry the ExoS toxin gene, whereas environmental isolates are far more often ExoU-positive. Are the ExoU-positive CF isolates recent environmental immigrants and the ExoS-positive ones long-adapted lung lineages?"
hypothesis: "ExoS-positive CF isolates form CF-specific clades with more accessory-gene divergence from environmental strains, while ExoU-positive CF isolates sit inside environmental clades."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Effector typing and isolation labels exist for thousands of genomes, but a tree-based comparison has not been done."
collections: ["kbase-ke-pangenome", "protect-genomedepot"]
findings: ["cf_formulation_design--1799127b"]
conflicts: []
papers: ["19936230", "39770290", "42151817", "14688090"]
builds_on: ["findings/cf_formulation_design--1799127b"]
projects: ["cf_formulation_design"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are ExoU-carrying cystic fibrosis Pseudomonas recent arrivals from the environment?

Most cystic fibrosis Pseudomonas aeruginosa isolates carry the ExoS toxin gene, whereas environmental isolates are far more often ExoU-positive. Are the ExoU-positive CF isolates recent environmental immigrants and the ExoS-positive ones long-adapted lung lineages?

## Hypothesis

ExoS-positive CF isolates form CF-specific clades with more accessory-gene divergence from environmental strains, while ExoU-positive CF isolates sit inside environmental clades.

## Why it matters

It would show that toxin type marks adaptation history and that results from the ExoU-positive PA14 strain may not apply to typical CF infections.

## How to test it

Using the Pangenome Collection and PROTECT Pathogen Browser, build a core-genome tree for the Pseudomonas aeruginosa genomes with environmental metadata. Classify each by effector type and isolation source. Test whether ExoU-positive CF isolates have nearest relatives from environmental sources more often than ExoS-positive CF isolates, and compare accessory gene divergence from the nearest environmental relative.

## What would support or refute it

Support: ExoU-positive CF isolates are nested in environmental clades and ExoS-positive isolates form CF-dominated clades. Refutation: both groups are equally mixed with environmental relatives.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Effector typing and isolation labels exist for thousands of genomes, but a tree-based comparison has not been done.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/protect-genomedepot|PROTECT Pathogen Browser]]

## Builds on

- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)

## Closest published work

- [PMID 19936230](https://pubmed.ncbi.nlm.nih.gov/19936230/) Pseudomonas aeruginosa population structure revisited.
- [PMID 39770290](https://pubmed.ncbi.nlm.nih.gov/39770290/) The exoS, exoT, exoU and exoY Virulotypes of the Type 3 Secretion System in Multidrug Resistant Pseudomonas aeruginosa as a Death Risk Factor in Pediatric Patients.
- [PMID 42151817](https://pubmed.ncbi.nlm.nih.gov/42151817/) Characterization of two exoU+/exoS+ carbapenem-non-susceptible Pseudomonas aeruginosa co-colonizing the lung of a bacterial pneumonia patient.
- [PMID 14688090](https://pubmed.ncbi.nlm.nih.gov/14688090/) Cross-sectional analysis of clinical and environmental isolates of Pseudomonas aeruginosa: biofilm formation, virulence, and genome diversity.

PMID 19936230 found nearly all CF strains ExoS-positive in a 328-isolate panel, and PMID 42151817 describes co-colonising ExoU and ExoS strains; this asks about origin and adaptation history across thousands of genomes.
