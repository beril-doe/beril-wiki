---
type: "Research direction"
description: "Gene-level fitness is positively correlated between nearly all metal pairs, and iron with zinc more strongly than expected, but that Fe-Zn estimate rests on only 6 organisms and no non-metal stress controls exist. Is this a general-stress signal or a specific metal-damage mechanism such as iron-sulfur cluster damage?"
hypothesis: "Iron-zinc cross-resistance is carried mainly by iron-sulfur cluster biogenesis and repair genes. Removing those genes weakens the iron-zinc correlation much more than the correlation of metal pairs that do not target iron-sulfur proteins, and non-metal stressors correlate with metals far less."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The correlation analysis uses Fitness Browser data, but the deciding deletion measurements under zinc and iron excess are new, and the Fe-Zn estimate currently covers only 6 organisms."
collections: ["kescience-fitnessbrowser"]
findings: ["metal_cross_resistance--fbb37c50", "metal_cross_resistance--8b1ef6ba", "metal_cross_resistance--fe1c0679"]
conflicts: ["conflict--cofitness-network-architecture--2d1b0ad4", "conflict--shared-stress-versus-stressor-specific-fitness--07279e23"]
papers: ["31586033", "37272830", "16537105", "28528649"]
builds_on: ["findings/metal_cross_resistance--fbb37c50", "findings/metal_cross_resistance--8b1ef6ba", "findings/metal_cross_resistance--fe1c0679", "conflicts/conflict--cofitness-network-architecture--2d1b0ad4", "conflicts/conflict--shared-stress-versus-stressor-specific-fitness--07279e23"]
projects: ["counter_ion_effects", "metal_cross_resistance"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Could iron-sulfur cluster damage underlie the cross-resistance between zinc and iron?

Gene-level fitness is positively correlated between nearly all metal pairs, and iron with zinc more strongly than expected, but that Fe-Zn estimate rests on only 6 organisms and no non-metal stress controls exist. Is this a general-stress signal or a specific metal-damage mechanism such as iron-sulfur cluster damage?

## Hypothesis

Iron-zinc cross-resistance is carried mainly by iron-sulfur cluster biogenesis and repair genes. Removing those genes weakens the iron-zinc correlation much more than the correlation of metal pairs that do not target iron-sulfur proteins, and non-metal stressors correlate with metals far less.

## Why it matters

It would separate a specific chemical mechanism from a generic stress response in a result that currently reads as 'all metals are alike', and tell us which tolerance genes are worth engineering.

## How to test it

In the Fitness Browser organisms that have both iron and zinc experiments (only 6 so far), recompute metal-metal correlations after removing iron-sulfur biogenesis genes, and compare with removing size-matched random gene sets. Add non-metal stress conditions (antibiotics, oxidative, osmotic) as controls in the same organisms. Then, in one tractable organism, measure deletions of iron-sulfur biogenesis genes under zinc and iron excess.

## What would support or refute it

Support: removing iron-sulfur genes selectively lowers the iron-zinc correlation, non-metal stressors correlate much more weakly, and the deletions are sensitive to both metals. Refute: correlation is unchanged after removal and non-metal stressors correlate as strongly as metals, pointing to a general stress axis.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The correlation analysis uses Fitness Browser data, but the deciding deletion measurements under zinc and iron excess are new, and the Fe-Zn estimate currently covers only 6 organisms.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/metal_cross_resistance--fbb37c50|Gene-level metal cross-resistance is almost uniformly positive across diverse bacteria]] (Insufficient literature evidence)
- Finding: [[findings/metal_cross_resistance--8b1ef6ba|Iron and zinc show unexpectedly strong cross-resistance]] (Extends retrieved work)
- Finding: [[findings/metal_cross_resistance--fe1c0679|Cross-resistance direction is universal but its magnitude is only moderately conserved]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cofitness-network-architecture--2d1b0ad4|Metal Cross-Resistance: Metal-Specific Shared Mechanisms or General Stress Response?]]
- Conflict: [[conflicts/conflict--shared-stress-versus-stressor-specific-fitness--07279e23|Universal Positive Metal Cross-Resistance or Metal-Dependent Overlap with Salt Stress?]]

## Closest published work

- [PMID 31586033](https://pubmed.ncbi.nlm.nih.gov/31586033/) Zinc excess increases cellular demand for iron and decreases tolerance to copper in Escherichia coli.
- [PMID 37272830](https://pubmed.ncbi.nlm.nih.gov/37272830/) Functional Characterization of FeoAB in Iron Acquisition and Pathogenicity in Riemerella anatipestifer.
- [PMID 16537105](https://pubmed.ncbi.nlm.nih.gov/16537105/) Co-selection of antibiotic and metal resistance.
- [PMID 28528649](https://pubmed.ncbi.nlm.nih.gov/28528649/) Metal Resistance and Its Association With Antibiotic Resistance.

PMID 31586033 shows zinc excess raises iron demand in E. coli and PMID 37272830 links iron uptake to zinc, manganese and copper responses; they do not test a shared iron-sulfur mechanism across organisms or compare against non-metal stress.
