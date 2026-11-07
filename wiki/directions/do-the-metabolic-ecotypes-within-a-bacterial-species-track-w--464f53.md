---
type: "Research direction"
description: "Species with many genomes split into a handful of metabolic ecotypes by their pathway profiles. Do these ecotypes correspond to distinct isolation environments, or do they simply mirror subclades?"
hypothesis: "Metabolic ecotypes predict isolation environment better than core-genome subclade membership alone does, and pathways that vary within a species are those tied to nutrient sources of different habitats."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pathway profiles and isolation metadata exist, but subclade structure and metadata harmonisation must be computed, and only a minority of genomes carry environmental embeddings."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["pathway_capability_dependency--4df15631", "pathway_capability_dependency--f655b856"]
conflicts: []
papers: ["24465487", "22928415", "17449702"]
builds_on: ["findings/pathway_capability_dependency--4df15631", "findings/pathway_capability_dependency--f655b856"]
projects: ["pathway_capability_dependency"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do the metabolic ecotypes within a bacterial species track where its strains live?

Species with many genomes split into a handful of metabolic ecotypes by their pathway profiles. Do these ecotypes correspond to distinct isolation environments, or do they simply mirror subclades?

## Hypothesis

Metabolic ecotypes predict isolation environment better than core-genome subclade membership alone does, and pathways that vary within a species are those tied to nutrient sources of different habitats.

## Why it matters

It would show that within-species metabolic variation is ecological adaptation rather than neutral drift, and give a way to infer habitat from genome content. The planned niche-breadth test for these ecotypes was never run.

## How to test it

For the species with at least 50 genomes and variable pathways, cluster genomes by pathway profile in the Pangenome Collection. Score isolation-source categories using genome metadata, supplemented by NMDC BioSamples where strains link. Compare how well ecotype labels and core-genome subclade labels each predict isolation category within species, and whether the discriminating pathways are carbon or nitrogen utilization routes.

## What would support or refute it

Support: ecotype labels carry environment information beyond what subclade labels carry, concentrated in nutrient-use pathways. Refute: environment is explained by subclade, or ecotype and environment are unrelated across species.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pathway profiles and isolation metadata exist, but subclade structure and metadata harmonisation must be computed, and only a minority of genomes carry environmental embeddings.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/pathway_capability_dependency--4df15631|Species with many genomes split into a handful of metabolic ecotypes]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--f655b856|Planned test of ecotypes against environmental niche breadth was not run]] (Insufficient literature evidence)

## Closest published work

- [PMID 24465487](https://pubmed.ncbi.nlm.nih.gov/24465487/) Metabolic flexibility as a major predictor of spatial distribution in microbial communities.
- [PMID 22928415](https://pubmed.ncbi.nlm.nih.gov/22928415/) Mapping the niche space of soil microorganisms using taxonomy and traits.
- [PMID 17449702](https://pubmed.ncbi.nlm.nih.gov/17449702/) Genomic and phenotypic diversity of coastal Vibrio cholerae strains is linked to environmental factors.

PMID 24465487 links metabolic flexibility to spatial distribution of communities and PMID 22928415 maps soil niche space by traits, but neither tests ecotypes inside species against isolation environment with phylogeny held fixed.
