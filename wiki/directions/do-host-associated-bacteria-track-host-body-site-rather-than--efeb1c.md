---
type: "Research direction"
description: "Why do host-associated and free-living bacteria look equally weak in environment-gene-content links, when published work finds host-associated communities less responsive to the environment? Is collection-site location the wrong variable for hosts?"
hypothesis: "In host-associated species, gene content varies with body site or tissue of isolation more strongly than with geographic or satellite-embedding distance, while in free-living species the reverse holds."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Source text exists but body-site harmonisation and per-species distance models must be built."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["ecotype_analysis--aa4707c1", "env_embedding_explorer--0ef24a89", "ecotype_env_reanalysis--82307b2c"]
conflicts: ["conflict--ecotype-environment-gene-content--66537c9c"]
papers: ["31227022", "34523223", "32503908", "36445161"]
builds_on: ["findings/ecotype_analysis--aa4707c1", "findings/env_embedding_explorer--0ef24a89", "findings/ecotype_env_reanalysis--82307b2c", "conflicts/conflict--ecotype-environment-gene-content--66537c9c"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "env_embedding_explorer"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do host-associated bacteria track host body site rather than geography?

Why do host-associated and free-living bacteria look equally weak in environment-gene-content links, when published work finds host-associated communities less responsive to the environment? Is collection-site location the wrong variable for hosts?

## Hypothesis

In host-associated species, gene content varies with body site or tissue of isolation more strongly than with geographic or satellite-embedding distance, while in free-living species the reverse holds.

## Why it matters

It would explain the null difference between lifestyles as a measurement error and show what environment variable matters for host-associated bacteria.

## How to test it

Select species in the Pangenome Collection that have many genomes from both host and non-host sources, including the clinical-heavy species. Harmonise body site or tissue from isolation source and NMDC BioSamples text. For each species, compare how much gene-content distance is explained by body-site labels versus embedding distance, after removing phylogenetic distance. Compare hosts with free-living species.

## What would support or refute it

Support: body site explains more than embedding distance in host-associated species and not in free-living species. Refutation: body site adds nothing beyond embeddings, or the lifestyle contrast stays absent.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Source text exists but body-site harmonisation and per-species distance models must be built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/ecotype_analysis--aa4707c1|No significant difference in environment effects between free-living and host-associated bacteria]] (In tension with retrieved work)
- Finding: [[findings/env_embedding_explorer--0ef24a89|Embedded genomes are heavily skewed toward human-associated sources]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_env_reanalysis--82307b2c|Environmental species show no stronger environment–gene-content correlation than human-associated species]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--66537c9c|Does a Strong Geographic Signal in AlphaEarth Embeddings Mean Environment Shapes Gene Content More Strongly?]]

## Closest published work

- [PMID 31227022](https://pubmed.ncbi.nlm.nih.gov/31227022/) Microbial indicators of environmental perturbations in coral reef ecosystems.
- [PMID 34523223](https://pubmed.ncbi.nlm.nih.gov/34523223/) Keep your friends close: Host compartmentalisation of microbial communities facilitates decoupling from effects of habitat fragmentation.
- [PMID 32503908](https://pubmed.ncbi.nlm.nih.gov/32503908/) Fish Skin and Gut Microbiomes Show Contrasting Signatures of Host Species and Habitat.
- [PMID 36445161](https://pubmed.ncbi.nlm.nih.gov/36445161/) Genomic and Environmental Factors Shape the Active Gill Bacterial Community of an Amazonian Teleost Holobiont.

PMIDs 31227022, 34523223, 32503908 and 36445161 used direct environmental measurements in host systems; this tests whether host microenvironment, not collection coordinates, explains the missing lifestyle contrast in genome-scale data.
