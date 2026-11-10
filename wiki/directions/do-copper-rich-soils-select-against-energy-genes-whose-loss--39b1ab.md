---
type: "Research direction"
description: "Are the energy-production gene families that are scarcer in copper-rich soils the same ones whose loss is less harmful under copper in laboratory fitness screens?"
hypothesis: "Energy-production gene families that decline in copper-rich soils are enriched among genes whose mutants are less harmed, or do better, under copper in laboratory fitness screens, and this is not seen under other metals."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Soil COG associations are computed, but whether the Fitness Browser holds copper and other-metal experiments for enough organisms is not established by the findings, and the soil genome matching needs distance sensitivity checks."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["soil_metal_functional_genomics--2a80fc76", "soil_metal_functional_genomics--fd9b94cc", "soil_metal_functional_genomics--becb7d4e"]
conflicts: ["conflict--environment-embedding-geography--32d28f91"]
papers: ["41539526", "30336790", "42150504"]
builds_on: ["findings/soil_metal_functional_genomics--2a80fc76", "findings/soil_metal_functional_genomics--fd9b94cc", "findings/soil_metal_functional_genomics--becb7d4e", "conflicts/conflict--environment-embedding-geography--32d28f91"]
projects: ["microbeatlas_metal_ecology", "soil_metal_functional_genomics"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do copper-rich soils select against energy genes whose loss helps under copper stress?

Are the energy-production gene families that are scarcer in copper-rich soils the same ones whose loss is less harmful under copper in laboratory fitness screens?

## Hypothesis

Energy-production gene families that decline in copper-rich soils are enriched among genes whose mutants are less harmed, or do better, under copper in laboratory fitness screens, and this is not seen under other metals.

## Why it matters

Soil-metal associations are observational and cannot separate copper-specific effects from general multi-metal stress. Linking field patterns to controlled copper fitness would show whether the proposed energy trade-off is a copper mechanism.

## How to test it

From the soil metal-function analysis, take the COG categories negatively associated with copper, first re-checking that the pattern holds when genomes are matched to soil samples at 5 km and 20 km as well as 10 km. In the Fitness Browser, compare fitness of genes in those categories under copper conditions against other metal and non-metal conditions across organisms, if copper experiments exist for enough organisms. Use chromium, lead and zinc, which co-vary with copper in the soils, as controls for a generic multi-metal response.

## What would support or refute it

Support: energy-category genes show less negative or positive fitness under copper but not under the other metals. Refutation: energy-category genes show no copper-specific pattern, or behave the same under all metals, pointing to generic stress; or too few organisms have copper data to test it.

## Data

Approach: lakehouse analysis. Readiness: unknown. Soil COG associations are computed, but whether the Fitness Browser holds copper and other-metal experiments for enough organisms is not established by the findings, and the soil genome matching needs distance sensitivity checks.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/soil_metal_functional_genomics--2a80fc76|Copper-associated COGs suggest an energetic trade-off under copper stress]] (Insufficient literature evidence)
- Finding: [[findings/soil_metal_functional_genomics--fd9b94cc|Metals explain most residual community COG variance after removing project effects]] (Extends retrieved work)
- Finding: [[findings/soil_metal_functional_genomics--becb7d4e|Metal–COG relationships differ among soil, marine and wastewater biomes]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--environment-embedding-geography--32d28f91|Strong metal–microbe associations versus uncertain attribution to metals]]

## Closest published work

- [PMID 41539526](https://pubmed.ncbi.nlm.nih.gov/41539526/) Microbial taxonomic and functional responses to heavy metal gradients in mining-impacted stream sediments.
- [PMID 30336790](https://pubmed.ncbi.nlm.nih.gov/30336790/) Consistent responses of soil microbial taxonomic and functional attributes to mercury pollution across China.
- [PMID 42150504](https://pubmed.ncbi.nlm.nih.gov/42150504/) Multi-metal contamination is associated with microbial network simplification and functional adaptation in paddy soils: Insights from genome-resolved metagenomics.

PMID 41539526 and PMID 42150504 relate metal gradients to community function in field sediments or soils without connecting to gene-level fitness. This direction joins the field association to measured fitness under copper.
