---
type: "Research direction"
description: "After comparison within the same genus, nitrogen fixation and ACC deaminase stayed tied to plant association most clearly, with the type III secretion system a weaker case. For these markers, is presence fixed within a species but gained or lost between sister species?"
hypothesis: "Where nitrogen fixation and ACC deaminase occur, they are near-universal within a species, yet sister species in the same genus differ in carrying them at all. The lifestyle switch then happens between species, and the type III secretion system may follow the same pattern less clearly."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Marker calls and species-level core status exist for plant-associated species; the rerun shuffle, sister-species comparison and neighbourhood analysis need new queries, and tree coverage is limited for many plant-associated species."
collections: ["kbase-ke-pangenome"]
findings: ["plant_microbiome_ecotypes--223dadd3"]
conflicts: ["conflict--ecotype-environment-gene-content--aa91ad15", "conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1"]
papers: ["29255260", "22792073", "35536128", "32040377"]
builds_on: ["findings/plant_microbiome_ecotypes--223dadd3", "conflicts/conflict--ecotype-environment-gene-content--aa91ad15", "conflicts/conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1"]
projects: ["cog_analysis", "plant_microbiome_ecotypes", "prophage_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are nitrogen fixation and ACC deaminase fixed within species but switched between sister species?

After comparison within the same genus, nitrogen fixation and ACC deaminase stayed tied to plant association most clearly, with the type III secretion system a weaker case. For these markers, is presence fixed within a species but gained or lost between sister species?

## Hypothesis

Where nitrogen fixation and ACC deaminase occur, they are near-universal within a species, yet sister species in the same genus differ in carrying them at all. The lifestyle switch then happens between species, and the type III secretion system may follow the same pattern less clearly.

## Why it matters

It would show whether plant-association genes are stable within a species but move over evolutionary time between species, which bears on the higher mobile-element load of plant-associated genera. It would also say where to look for the mobile elements involved. The 64.6% core share measured for beneficial gene clusters as a group does not by itself show that these markers are core, so this must be tested marker by marker.

## How to test it

For each marker, in genera with both plant-associated and non-plant species in the Pangenome Collection, compute the fraction of genomes carrying the marker within each species and whether it is classed as core. Count how often presence differs between sister species. Check whether carrier gene neighbourhoods contain mobile-element genes or breaks in gene order, compared with markers that did not stay tied to plant association. Because the original within-genus shuffle used only 200 repeats and no correction across 15 markers, rerun it with many more repeats and a correction, and treat the type III secretion result as provisional.

## What would support or refute it

Support: within-species fixation is high, presence between sister species is patchy, and carrier neighbourhoods show more mobile signatures than the other markers. Refute: the markers vary within species, or sister species rarely differ, which would point to inheritance from a common ancestor.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Marker calls and species-level core status exist for plant-associated species; the rerun shuffle, sister-species comparison and neighbourhood analysis need new queries, and tree coverage is limited for many plant-associated species.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/plant_microbiome_ecotypes--223dadd3|Only three plant markers survive strict within-genus permutation]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--aa91ad15|Core-Dominated Beneficial Clusters vs. Elevated Mobilome Burden in Plant-Associated Genera]]
- Conflict: [[conflicts/conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1|Do Adaptive Functions Sit in the Accessory Genome or Inside the Core?]]

## Closest published work

- [PMID 29255260](https://pubmed.ncbi.nlm.nih.gov/29255260/) Genomic features of bacterial adaptation to plants.
- [PMID 22792073](https://pubmed.ncbi.nlm.nih.gov/22792073/) Comparative genomics of plant-associated Pseudomonas spp.: insights into diversity and inheritance of traits involved in multitrophic interactions.
- [PMID 35536128](https://pubmed.ncbi.nlm.nih.gov/35536128/) Cruciferous Weed Isolates of Xanthomonas campestris Yield Insight into Pathovar Genomic Relationships and Genetic Determinants of Host and Tissue Specificity.
- [PMID 32040377](https://pubmed.ncbi.nlm.nih.gov/32040377/) Genomic Acquisitions in Emerging Populations of Xanthomonas vasicola pv. vasculorum Infecting Corn in the United States and Argentina.

PMID 29255260 and PMID 22792073 describe genomic features that distinguish plant-associated bacteria and diversity of plant-interaction traits in Pseudomonas, but neither asks whether the key genes are fixed within species and switched between sister species.
