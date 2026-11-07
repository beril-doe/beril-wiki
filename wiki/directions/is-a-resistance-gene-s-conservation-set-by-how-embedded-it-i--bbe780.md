---
type: "Research direction"
description: "Resistance mechanism strongly predicts whether a resistance gene is core or accessory, yet it does not predict knockout fitness cost. Intrinsic efflux pumps such as emhABC are more than 95% core, beta-lactamases are 54.9% core, regulatory genes are 6.5% core, and blaTEM, tet(C) and ant(2'')-Ia are 0% core. What besides cost explains this spread?"
hypothesis: "Resistance genes that are core are those whose products also serve non-antibiotic roles, such as envelope maintenance or stress handling. Within a mechanism class they should show fitness effects under non-antibiotic stresses and co-vary with non-resistance genes, whereas accessory ones should be functionally isolated."
approach: "analysis then experiment"
readiness: "data in the lakehouse"
readiness_basis: "Resistance genes were already linked to fitness data and core status across 25 organisms, so the first step uses existing linked tables; the knockout step needs new measurements."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["amr_fitness_cost--67395444", "amr_pangenome_atlas--9947286c"]
conflicts: []
papers: ["35873140", "25861385", "20208551", "34135355", "26203082"]
builds_on: ["findings/amr_fitness_cost--67395444", "findings/amr_pangenome_atlas--9947286c"]
projects: ["amr_fitness_cost", "amr_pangenome_atlas"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Is a resistance gene's conservation set by how embedded it is in physiology?

Resistance mechanism strongly predicts whether a resistance gene is core or accessory, yet it does not predict knockout fitness cost. Intrinsic efflux pumps such as emhABC are more than 95% core, beta-lactamases are 54.9% core, regulatory genes are 6.5% core, and blaTEM, tet(C) and ant(2'')-Ia are 0% core. What besides cost explains this spread?

## Hypothesis

Resistance genes that are core are those whose products also serve non-antibiotic roles, such as envelope maintenance or stress handling. Within a mechanism class they should show fitness effects under non-antibiotic stresses and co-vary with non-resistance genes, whereas accessory ones should be functionally isolated.

## Why it matters

It would separate resistance genes that are permanent parts of cell physiology from true add-ons. That changes which resistance genes can be targeted without side effects, and explains conservation without invoking cost.

## How to test it

The mechanism labels came from keyword matching on product descriptions, so first re-assign them from the gene annotations and check that the core-versus-accessory spread survives. Then, for resistance genes in Fitness Browser organisms with conservation status from the Pangenome Collection, compare core and accessory genes within each mechanism class. Measure (a) fitness under non-antibiotic stresses such as detergents, osmotic stress and metals, and (b) how closely each gene's fitness pattern tracks that of non-resistance genes across all experiments. Then knock out a core efflux operon such as emhABC in a host that carries it and test growth under envelope stress.

## What would support or refute it

Support: core resistance genes show more non-antibiotic phenotypes and stronger co-variation with envelope or regulatory genes than accessory ones of the same mechanism. Refute: the two groups look alike once mechanism is held fixed, which would point to mobility rather than physiological integration.

## Data

Approach: analysis then experiment. Readiness: data in the lakehouse. Resistance genes were already linked to fitness data and core status across 25 organisms, so the first step uses existing linked tables; the knockout step needs new measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_fitness_cost--67395444|Resistance mechanism predicts conservation status though not fitness cost]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--9947286c|Core versus accessory status of AMR genes depends on resistance mechanism]] (Insufficient literature evidence)

## Closest published work

- [PMID 35873140](https://pubmed.ncbi.nlm.nih.gov/35873140/) Comparative Genomic Analysis of the Human Pathogen Wohlfahrtiimonas Chitiniclastica Provides Insight Into the Identification of Antimicrobial Resistance Genotypes and Potential Virulence Traits.
- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?
- [PMID 34135355](https://pubmed.ncbi.nlm.nih.gov/34135355/) AMRFinderPlus and the Reference Gene Catalog facilitate examination of the genomic links among antimicrobial resistance, stress response, and virulence.
- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.

PMID 35873140 shows some efflux genes are core in one species and PMID 25861385 shows cost varies by drug class, but neither asks what non-antibiotic role could make a resistance gene permanent.
