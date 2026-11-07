---
type: "Research direction"
description: "The nitrogenase gene nifH is negatively associated with the cyanide-synthesis gene hcnC and the PQQ gene pqqC across genomes. Does the cyanide operon impair nitrogen fixation when both sit in one strain, or do the two traits simply belong to different lifestyles?"
hypothesis: "Within genera that contain both, hcnC and nifH co-occur less often than expected, and deleting the hcn operon from a diazotroph raises nitrogenase activity and growth without a nitrogen source."
approach: "analysis then experiment"
readiness: "data in the lakehouse"
readiness_basis: "Gene presence for nifH, hcnC and pqqC across genomes is already analysed; the within-genus test uses the same data, and the deletion test needs new work."
collections: ["kbase-ke-pangenome"]
findings: ["pgp_pangenome_ecology--7e9e60f9"]
conflicts: []
papers: ["41190207", "41612514", "34352636", "21856827"]
builds_on: ["findings/pgp_pangenome_ecology--7e9e60f9"]
projects: ["pgp_pangenome_ecology"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does carrying the cyanide operon impair nitrogen fixation in the same strain?

The nitrogenase gene nifH is negatively associated with the cyanide-synthesis gene hcnC and the PQQ gene pqqC across genomes. Does the cyanide operon impair nitrogen fixation when both sit in one strain, or do the two traits simply belong to different lifestyles?

## Hypothesis

Within genera that contain both, hcnC and nifH co-occur less often than expected, and deleting the hcn operon from a diazotroph raises nitrogenase activity and growth without a nitrogen source.

## Why it matters

It would explain why plant-growth traits do not stack in one organism and guide the design of inoculants that combine nitrogen fixation with biocontrol.

## How to test it

In the Pangenome Collection, take genera containing both nifH and hcnC carriers. Test whether co-carriage is rarer than expected within genus and within soil habitat. Then, in a Pseudomonas or Azotobacter strain, compare acetylene-reduction activity and nitrogen-free growth between the intact strain and an hcn deletion.

## What would support or refute it

Support: co-carriage is rarer within genera than expected, and the hcn deletion raises nitrogenase activity and nitrogen-free growth. Refutation: co-carriage is as common as expected within genera and the deletion changes neither measure, which would point to separate lifestyles instead.

## Data

Approach: analysis then experiment. Readiness: data in the lakehouse. Gene presence for nifH, hcnC and pqqC across genomes is already analysed; the within-genus test uses the same data, and the deletion test needs new work.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--7e9e60f9|Nitrogen fixation gene is negatively associated with other plant-growth genes]] (Candidate novel)

## Closest published work

- [PMID 41190207](https://pubmed.ncbi.nlm.nih.gov/41190207/) Integrated metagenomic and soil chemical analyses revealed shifts of microbial nutrient cycling with poplar plantation age.
- [PMID 41612514](https://pubmed.ncbi.nlm.nih.gov/41612514/) Effects of legume-based rotation on subsequent sorghum rhizosphere microbial communities and their drought tolerance-related genes.
- [PMID 34352636](https://pubmed.ncbi.nlm.nih.gov/34352636/) Impacts of bio-stimulants on pyrene degradation, prokaryotic community compositions, and functions.
- [PMID 21856827](https://pubmed.ncbi.nlm.nih.gov/21856827/) Pyrroloquinoline quinone biosynthesis gene pqqC, a novel molecular marker for studying the phylogeny and diversity of phosphate-solubilizing pseudomonads.

PMIDs 41190207, 41612514 and 34352636 report nifH and pqqC only as abundance shifts in metagenomes; none tests co-carriage or a mechanism.
