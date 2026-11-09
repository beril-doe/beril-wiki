---
type: "Research direction"
description: "Are host-associated bacteria less shaped by their environment than free-living ones when environment is measured by body site and host rather than collection coordinates?"
hypothesis: "Host-associated species show weaker environment-to-gene-content association than free-living species when environment is defined by body site or host-niche labels. The earlier equal result came from coordinates that say little about a host's microenvironment."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Isolation-source text is in the genome metadata, but harmonizing body-site labels and rerunning partial-correlation tests across species has not been done."
collections: ["kbase-ke-pangenome"]
findings: ["ecotype_analysis--aa4707c1", "ecotype_env_reanalysis--ebb50481", "env_embedding_explorer--974280a5"]
conflicts: ["conflict--environment-embedding-geography--545921e4", "conflict--ecotype-environment-gene-content--66537c9c"]
papers: ["31227022", "34523223", "32503908", "36445161"]
builds_on: ["findings/ecotype_analysis--aa4707c1", "findings/ecotype_env_reanalysis--ebb50481", "findings/env_embedding_explorer--974280a5", "conflicts/conflict--environment-embedding-geography--545921e4", "conflicts/conflict--ecotype-environment-gene-content--66537c9c"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "env_embedding_explorer", "prophage_ecology", "snipe_defense_system"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do host-associated bacteria respond less to environment once host-proximal conditions are used?

Are host-associated bacteria less shaped by their environment than free-living ones when environment is measured by body site and host rather than collection coordinates?

## Hypothesis

Host-associated species show weaker environment-to-gene-content association than free-living species when environment is defined by body site or host-niche labels. The earlier equal result came from coordinates that say little about a host's microenvironment.

## Why it matters

Related literature reports host-associated communities responding less to environment, while the corpus saw no difference. This shows whether that disagreement comes from biology or from using location as the environment measure, which matters for any satellite-embedding-based claim about microbial habitat.

## How to test it

In the Pangenome Collection, take species with at least 20 genomes and both coordinate-based and organism-proximal labels (body site, host, tissue from isolation source). Compute gene-content versus environment association controlling for phylogeny, once with embedding distance and once with host-proximal labels. Compare the free-living minus host-associated gap between the two environment measures, including a version restricted to species that are not majority clinical.

## What would support or refute it

Support: a gap appears with host-proximal labels but not with coordinates. Refutation: no gap under either measure, meaning host and free-living lifestyles do not differ in environmental responsiveness at this scale.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Isolation-source text is in the genome metadata, but harmonizing body-site labels and rerunning partial-correlation tests across species has not been done.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ecotype_analysis--aa4707c1|No significant difference in environment effects between free-living and host-associated bacteria]] (In tension with retrieved work)
- Finding: [[findings/ecotype_env_reanalysis--ebb50481|Clinical sampling dominates species selected for the AlphaEarth ecotype analysis]] (Insufficient literature evidence)
- Finding: [[findings/env_embedding_explorer--974280a5|Geographic gradient in embeddings is stronger for environmental than human-associated samples]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--environment-embedding-geography--545921e4|Does the embedded genome subset favour clinical or environmental isolates?]]
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--66537c9c|Does a Strong Geographic Signal in AlphaEarth Embeddings Mean Environment Shapes Gene Content More Strongly?]]

## Closest published work

- [PMID 31227022](https://pubmed.ncbi.nlm.nih.gov/31227022/) Microbial indicators of environmental perturbations in coral reef ecosystems.
- [PMID 34523223](https://pubmed.ncbi.nlm.nih.gov/34523223/) Keep your friends close: Host compartmentalisation of microbial communities facilitates decoupling from effects of habitat fragmentation.
- [PMID 32503908](https://pubmed.ncbi.nlm.nih.gov/32503908/) Fish Skin and Gut Microbiomes Show Contrasting Signatures of Host Species and Habitat.
- [PMID 36445161](https://pubmed.ncbi.nlm.nih.gov/36445161/) Genomic and Environmental Factors Shape the Active Gill Bacterial Community of an Amazonian Teleost Holobiont.

PMID 31227022 and PMID 34523223 measured host-associated communities with direct environmental measurements and found weaker environment tracking. This direction tests whether the same pattern appears in genome gene content across many bacterial species.
