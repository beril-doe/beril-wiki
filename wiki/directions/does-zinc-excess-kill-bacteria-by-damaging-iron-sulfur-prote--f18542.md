---
type: "Research direction"
description: "Iron and zinc show unexpectedly strong shared gene-level tolerance across organisms. Does zinc toxicity act through iron-sulfur cluster damage?"
hypothesis: "Genes for iron-sulfur cluster assembly and repair, and for iron-sulfur enzymes, account for most of the iron\u2013zinc overlap. Iron supplementation will relieve zinc-sensitive fitness defects in those genes but not in zinc-export genes."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The overlap analysis uses existing Fitness Browser data, but the decisive iron-rescue experiment has no existing data."
collections: ["kescience-fitnessbrowser"]
findings: ["metal_cross_resistance--8b1ef6ba", "metal_cross_resistance--fbb37c50"]
conflicts: ["conflict--shared-stress-versus-stressor-specific-fitness--07279e23"]
papers: ["31586033", "37272830", "35019689", "27474723"]
builds_on: ["findings/metal_cross_resistance--8b1ef6ba", "findings/metal_cross_resistance--fbb37c50", "conflicts/conflict--shared-stress-versus-stressor-specific-fitness--07279e23"]
projects: ["counter_ion_effects", "metal_cross_resistance"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Does zinc excess kill bacteria by damaging iron-sulfur proteins?

Iron and zinc show unexpectedly strong shared gene-level tolerance across organisms. Does zinc toxicity act through iron-sulfur cluster damage?

## Hypothesis

Genes for iron-sulfur cluster assembly and repair, and for iron-sulfur enzymes, account for most of the iron–zinc overlap. Iron supplementation will relieve zinc-sensitive fitness defects in those genes but not in zinc-export genes.

## Why it matters

A mechanism for the iron–zinc link would show which cellular targets make metals toxic together. It would also separate chemistry-specific cross-tolerance from a generic stress response, which the metal studies could not do.

## How to test it

In the Fitness Browser organisms with iron and zinc experiments, split the genes behind the iron–zinc overlap by function. Test whether iron-sulfur assembly, repair and iron-sulfur-containing enzyme genes are over-represented compared with the rest of the overlap. In one tractable organism, run barcoded transposon fitness under zinc with and without added iron.

## What would support or refute it

Support: iron-sulfur genes dominate the overlap and iron addition rescues their zinc defects selectively. Refute: the overlap is spread across unrelated functions, or iron rescues all zinc defects equally, suggesting general stress.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The overlap analysis uses existing Fitness Browser data, but the decisive iron-rescue experiment has no existing data.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/metal_cross_resistance--8b1ef6ba|Iron and zinc show unexpectedly strong cross-resistance]] (Extends retrieved work)
- Finding: [[findings/metal_cross_resistance--fbb37c50|Gene-level metal cross-resistance is almost uniformly positive across diverse bacteria]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--shared-stress-versus-stressor-specific-fitness--07279e23|Universal Positive Metal Cross-Resistance or Metal-Dependent Overlap with Salt Stress?]]

## Closest published work

- [PMID 31586033](https://pubmed.ncbi.nlm.nih.gov/31586033/) Zinc excess increases cellular demand for iron and decreases tolerance to copper in Escherichia coli.
- [PMID 37272830](https://pubmed.ncbi.nlm.nih.gov/37272830/) Functional Characterization of FeoAB in Iron Acquisition and Pathogenicity in Riemerella anatipestifer.
- [PMID 35019689](https://pubmed.ncbi.nlm.nih.gov/35019689/) The Role of ZntA in Klebsiella pneumoniae Zinc Homeostasis.
- [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/) Novel Metal Cation Resistance Systems from Mutant Fitness Analysis of Denitrifying Pseudomonas stutzeri.

PMID 31586033 shows zinc excess raises iron demand in Escherichia coli, and PMID 37272830 links iron uptake to zinc responses in one species. Neither tests iron-sulfur damage as the shared mechanism across many organisms.
