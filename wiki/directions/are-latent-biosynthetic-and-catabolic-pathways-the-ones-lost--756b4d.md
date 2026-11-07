---
type: "Research direction"
description: "Do pathways that are genomically complete but show no fitness importance in the laboratory vary more across strains of the same species than pathways that are fitness-important, and does this account for the link between latent pathways and open pangenomes?"
hypothesis: "Within a species, pathways classed as latent are missing from a larger fraction of genomes than active pathways of the same organism. Carbon-utilization pathways, which are more often latent than amino acid pathways, show the most within-species loss."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Latent and active labels and per-genome pathway completeness already exist for the organisms involved."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["metabolic_capability_dependency--6a369153", "metabolic_capability_dependency--b6cd74ee", "metabolic_capability_dependency--88a382b0", "metabolic_capability_dependency--f41ac91a"]
conflicts: ["conflict--community-metabolic-interdependence--cdc57135"]
papers: ["24910088", "35575545", "40568968"]
builds_on: ["findings/metabolic_capability_dependency--6a369153", "findings/metabolic_capability_dependency--b6cd74ee", "findings/metabolic_capability_dependency--88a382b0", "findings/metabolic_capability_dependency--f41ac91a", "conflicts/conflict--community-metabolic-interdependence--cdc57135"]
projects: ["metabolic_capability_dependency", "pathway_capability_dependency"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Are latent biosynthetic and catabolic pathways the ones lost first within species?

Do pathways that are genomically complete but show no fitness importance in the laboratory vary more across strains of the same species than pathways that are fitness-important, and does this account for the link between latent pathways and open pangenomes?

## Hypothesis

Within a species, pathways classed as latent are missing from a larger fraction of genomes than active pathways of the same organism. Carbon-utilization pathways, which are more often latent than amino acid pathways, show the most within-species loss.

## Why it matters

It would turn a laboratory classification into a testable signature of ongoing gene loss and give the Black Queen idea at species scale a prediction that can fail. The pathway-level conservation comparison found no difference, so this is the first check of loss across strains.

## How to test it

For the Fitness Browser organisms already classified as latent or active, use the Pangenome Collection to compute, for each pathway, the fraction of genomes of the same species that carry it complete. Compare latent against active pathways within the same organism, separately for carbon and amino acid pathways. Also ask whether species with more latent pathways have more strain-to-strain variable pathways.

## What would support or refute it

Support: latent pathways are absent from more conspecific genomes than active ones, and the effect is largest for carbon pathways. Refutation: latent and active pathways are equally conserved across strains, so latency reflects limited laboratory conditions rather than relaxed selection.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Latent and active labels and per-genome pathway completeness already exist for the organisms involved.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/metabolic_capability_dependency--6a369153|Clades with more latent pathways have more open pangenomes]] (Candidate novel)
- Finding: [[findings/metabolic_capability_dependency--b6cd74ee|Latent pathways are not less conserved than active pathways]] (Insufficient literature evidence)
- Finding: [[findings/metabolic_capability_dependency--88a382b0|Carbon utilization pathways are far more often latent than amino acid biosynthesis]] (Insufficient literature evidence)
- Finding: [[findings/metabolic_capability_dependency--f41ac91a|Many genomically complete pathways show no detectable fitness importance]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--community-metabolic-interdependence--cdc57135|Is Latent Metabolic Capability Condition-Dependent or Partly Fitness-Neutral?]]

## Closest published work

- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.
- [PMID 40568968](https://pubmed.ncbi.nlm.nih.gov/40568968/) Microbial cross-feeding stabilized by segregation of a dependent mutant from its independent ancestor.

PMID 24910088 and PMID 35575545 treat biosynthetic gene loss in experiments and theory, and PMID 40568968 shows cross-feeding dependence arising in culture. None tests whether laboratory-latent pathways are the ones that vary across strains in natural populations.
