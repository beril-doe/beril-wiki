---
type: "Research direction"
description: "Are latent-capability pathway-organism pairs (41.0% of 161 classified pairs) in the process of being lost, shown by gene-level erosion in close relatives, or are they retained reserves?"
hypothesis: "Latent-capability pathways show more gene-level loss (absence, truncation or pseudogenization) among close relatives than active-dependency pathways in the same organisms."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pathway classification exists for only 161 pairs; gene-level erosion across strain phylogenies must be newly built."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["pathway_capability_dependency--250e9510", "pathway_capability_dependency--4df15631"]
conflicts: []
papers: ["22448042", "22761588", "29672509"]
builds_on: ["findings/pathway_capability_dependency--250e9510", "findings/pathway_capability_dependency--4df15631"]
projects: ["pathway_capability_dependency"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do latent metabolic capabilities decay by gene loss, as the Black Queen hypothesis predicts?

Are latent-capability pathway-organism pairs (41.0% of 161 classified pairs) in the process of being lost, shown by gene-level erosion in close relatives, or are they retained reserves?

## Hypothesis

Latent-capability pathways show more gene-level loss (absence, truncation or pseudogenization) among close relatives than active-dependency pathways in the same organisms.

## Why it matters

It would distinguish adaptive gene loss from retained condition-specific capacity, testing the Black Queen idea against niche-breadth maintenance.

## How to test it

For the 7 Fitness Browser organisms with GapMind data and the 23 annotated pathways, map latent versus active-dependency pairs onto strain phylogenies in the Pangenome Collection. Count gene-level loss events per pathway in close relatives, using singleton or auxiliary status as a loss marker, and compare latent versus active classes with organism as a random effect. Pathway completeness did not separate latent from active pathways, so gene-level erosion is the measure. Pathways in the Incomplete but Important class (14.9%) serve as a comparison for annotation gaps.

## What would support or refute it

Support: latent pathways show significantly more gene-level loss than active ones. Refute: erosion is equal across classes, which would favor retained condition-specific capacity.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pathway classification exists for only 161 pairs; gene-level erosion across strain phylogenies must be newly built.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/pathway_capability_dependency--250e9510|Latent capability outnumbers active dependency among model-bacteria pathways]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--4df15631|Species with many genomes split into a handful of metabolic ecotypes]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 29672509](https://pubmed.ncbi.nlm.nih.gov/29672509/) Robustness encoded across essential and accessory replicons of the ecologically versatile bacterium Sinorhizobium meliloti.

PMID 22448042 proposes adaptive loss of leaky functions and PMID 22761588 reviews selection-driven gene loss; neither tests latent versus active pathways in model bacteria using fitness-classified pathway dependencies.
