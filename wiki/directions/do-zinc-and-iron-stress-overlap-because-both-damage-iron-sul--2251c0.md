---
type: "Research direction"
description: "Iron and zinc showed unexpectedly strong shared fitness effects across 6 organisms. Does zinc excess act on iron-sulfur cluster proteins, so that genes for building and repairing those clusters drive the shared signal?"
hypothesis: "Genes for iron-sulfur cluster assembly and repair carry most of the iron-zinc shared fitness. Removing them should collapse the overlap, and extra iron should relieve zinc sensitivity in their mutants."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Iron and zinc fitness data exist for 6 organisms. The rescue experiment needs new measurements."
collections: ["kescience-fitnessbrowser"]
findings: ["metal_cross_resistance--8b1ef6ba", "metal_cross_resistance--fbb37c50"]
conflicts: []
papers: ["31586033", "37272830", "35019689"]
builds_on: ["findings/metal_cross_resistance--8b1ef6ba", "findings/metal_cross_resistance--fbb37c50"]
projects: ["metal_cross_resistance"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do zinc and iron stress overlap because both damage iron-sulfur cluster proteins?

Iron and zinc showed unexpectedly strong shared fitness effects across 6 organisms. Does zinc excess act on iron-sulfur cluster proteins, so that genes for building and repairing those clusters drive the shared signal?

## Hypothesis

Genes for iron-sulfur cluster assembly and repair carry most of the iron-zinc shared fitness. Removing them should collapse the overlap, and extra iron should relieve zinc sensitivity in their mutants.

## Why it matters

It would explain a cross-organism pattern with a specific cellular mechanism. It would also show that the metal overlap is more than generic stress.

## How to test it

In the 6 organisms with both iron and zinc experiments in the Fitness Browser, mark iron-sulfur assembly, repair and iron-sulfur-enzyme genes. Compare how much of the iron-zinc shared signal sits in them against matched sets of genes with similar overall fitness and conservation. Then, in one organism, grow clean deletions of the assembly genes with zinc, with and without added iron, and measure growth.

## What would support or refute it

Support: iron-sulfur genes hold a disproportionate share of the shared signal, and iron supplementation rescues their zinc sensitivity. Refute: the shared signal is spread across unrelated functions, or iron does not rescue.

## Data

Approach: analysis then experiment. Readiness: needs compute. Iron and zinc fitness data exist for 6 organisms. The rescue experiment needs new measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/metal_cross_resistance--8b1ef6ba|Iron and zinc show unexpectedly strong cross-resistance]] (Extends retrieved work)
- Finding: [[findings/metal_cross_resistance--fbb37c50|Gene-level metal cross-resistance is almost uniformly positive across diverse bacteria]] (Insufficient literature evidence)

## Closest published work

- [PMID 31586033](https://pubmed.ncbi.nlm.nih.gov/31586033/) Zinc excess increases cellular demand for iron and decreases tolerance to copper in Escherichia coli.
- [PMID 37272830](https://pubmed.ncbi.nlm.nih.gov/37272830/) Functional Characterization of FeoAB in Iron Acquisition and Pathogenicity in Riemerella anatipestifer.
- [PMID 35019689](https://pubmed.ncbi.nlm.nih.gov/35019689/) The Role of ZntA in Klebsiella pneumoniae Zinc Homeostasis.

PMID 31586033 shows zinc excess raises the iron demand of E. coli, and PMID 37272830 links iron uptake to zinc responses in a single organism. This direction tests the iron-sulfur cluster explanation across organisms with a gene-level prediction.
