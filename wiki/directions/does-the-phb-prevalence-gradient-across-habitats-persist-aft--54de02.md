---
type: "Research direction"
description: "Is the environmental gradient in PHB capacity a habitat effect, or a by-product of genome size and lineage, as genome size already reversed the niche-breadth association?"
hypothesis: "Genome size and lineage absorb much of the gradient, but a smaller habitat effect remains between soil/plant and animal species within the same families."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Catalog shows genome metadata, pangenome sizes and environment tables; PHB gene-call tables were not shown and would need to be located."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.alphaearth_embeddings_all_years", "kbase.ke_pangenome.ncbi_env"]
findings: ["phb_granule_ecology--2bce1246", "phb_granule_ecology--4fff149b"]
conflicts: []
papers: ["14973198", "33941890", "37076457", "33118006"]
builds_on: ["findings/phb_granule_ecology--2bce1246", "findings/phb_granule_ecology--4fff149b"]
projects: ["phb_granule_ecology"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does the PHB prevalence gradient across habitats persist after controlling for genome size and lineage?

Is the environmental gradient in PHB capacity a habitat effect, or a by-product of genome size and lineage, as genome size already reversed the niche-breadth association?

## Hypothesis

Genome size and lineage absorb much of the gradient, but a smaller habitat effect remains between soil/plant and animal species within the same families.

## Why it matters

It would decide whether carbon storage is selected by fluctuating environments or simply tracks large metabolically versatile genomes.

## How to test it

Join species PHB status to genome size and environment labels using the pangenome and GTDB metadata, and fit within-family models of PHB presence on environment with genome size as covariate. Repeat on species with embedding-derived environment (28% of genomes) versus all, to test coverage bias, and treat the 34.9% unknown-environment species as a sensitivity group.

## What would support or refute it

Support: a habitat difference remains within families after genome-size control. Refute: the difference vanishes or reverses, as for niche breadth.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Catalog shows genome metadata, pangenome sizes and environment tables; PHB gene-call tables were not shown and would need to be located.

## Builds on

- Finding: [[findings/phb_granule_ecology--2bce1246|Genome size, not PHB, explains the apparent niche-breadth association]] (Candidate novel)
- Finding: [[findings/phb_granule_ecology--4fff149b|PHB prevalence falls steeply from plant and soil to animal environments]] (Candidate novel)

## Closest published work

- [PMID 14973198](https://pubmed.ncbi.nlm.nih.gov/14973198/) Trends between gene content and genome size in prokaryotic species with larger genomes.
- [PMID 33941890](https://pubmed.ncbi.nlm.nih.gov/33941890/) Metabolic flexibility allows bacterial habitat generalists to become dominant in a frequently disturbed ecosystem.
- [PMID 37076457](https://pubmed.ncbi.nlm.nih.gov/37076457/) Intracellular carbon storage by microorganisms is an overlooked pathway of biomass growth.
- [PMID 33118006](https://pubmed.ncbi.nlm.nih.gov/33118006/) The protective role of PHB and its degradation products against stress situations in bacteria.

14973198 links gene content to genome size and 37076457 covers soil carbon storage; neither tests PHB prevalence by habitat with genome size controlled.
