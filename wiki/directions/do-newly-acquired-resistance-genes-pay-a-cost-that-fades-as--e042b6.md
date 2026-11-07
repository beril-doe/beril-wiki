---
type: "Research direction"
description: "Core and accessory resistance genes have identical baseline knockout fitness, yet a separate analysis finds that single-genome resistance genes are the costliest class. Is cost tied to how recently a gene arrived rather than to its core or accessory label?"
hypothesis: "Resistance genes whose base and codon composition differs most from their host genome, an indirect hint of more recent acquisition, carry the highest cost, and cost shrinks as composition becomes host-like and prevalence within a species rises."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Gene linking and fitness exist, but composition-deviation metrics must be computed from genome sequences."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "kbase-genomes"]
findings: ["amr_fitness_cost--95a8021f"]
conflicts: ["conflict--pangenome-conservation-fitness-decoupling--8173d997"]
papers: ["29439838", "25861385", "20208551", "33423895", "22761588"]
builds_on: ["findings/amr_fitness_cost--95a8021f", "conflicts/conflict--pangenome-conservation-fitness-decoupling--8173d997"]
projects: ["amr_fitness_cost", "amr_pangenome_atlas"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do newly acquired resistance genes pay a cost that fades as they are integrated?

Core and accessory resistance genes have identical baseline knockout fitness, yet a separate analysis finds that single-genome resistance genes are the costliest class. Is cost tied to how recently a gene arrived rather than to its core or accessory label?

## Hypothesis

Resistance genes whose base and codon composition differs most from their host genome, an indirect hint of more recent acquisition, carry the highest cost, and cost shrinks as composition becomes host-like and prevalence within a species rises.

## Why it matters

If true, cost is transient after acquisition, and the absent core-versus-accessory difference hides a time-dependent cost. That would help explain how resistance persists once acquired.

## How to test it

In Fitness Browser organisms with linked pangenomes, take each resistance gene's sequence from KBase Genomes and compute its deviation in base composition and codon usage from the host genome, together with within-species prevalence from the Pangenome Collection. Composition deviation is only a proxy and does not give acquisition history, so also check whether it separates singleton genes from widely shared ones. Ask whether baseline knockout fitness is predicted by the deviation among non-singleton genes as well as singletons. For a strain carrying a likely recent acquisition, run a competition assay between carrier and knockout strain without antibiotic.

## What would support or refute it

Support: cost falls steadily as composition becomes host-like, independent of singleton status. Refute: cost is flat across the composition gradient, or the singleton signal disappears when one gene-linking method is used for all classes.

## Data

Approach: analysis then experiment. Readiness: needs compute. Gene linking and fitness exist, but composition-deviation metrics must be computed from genome sequences.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/amr_fitness_cost--95a8021f|Core and accessory AMR genes show identical fitness]] (Candidate novel)
- Conflict: [[conflicts/conflict--pangenome-conservation-fitness-decoupling--8173d997|Do AMR genes of different pangenome prevalence carry different fitness costs?]]

## Closest published work

- [PMID 29439838](https://pubmed.ncbi.nlm.nih.gov/29439838/) Evolutionary Mechanisms Shaping the Maintenance of Antibiotic Resistance.
- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?
- [PMID 33423895](https://pubmed.ncbi.nlm.nih.gov/33423895/) Mechanisms That Shape Microbial Pangenomes.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.

PMID 25861385 and PMID 29439838 describe cost and compensation for resistance mutations, but they do not test whether the cost of native resistance genes decays with time since acquisition in genome-wide knockout data.
