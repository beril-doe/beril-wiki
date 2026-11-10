---
type: "Research direction"
description: "Efflux resistance genes neighbor histidine and tryptophan biosynthesis genes in fitness-correlation networks across several organisms, although no function was specific to a resistance mechanism once corrected for repeated testing. Does biosynthesis status modulate efflux dependence?"
hypothesis: "Efflux pump mutants will be more sensitive to antibiotics when histidine or tryptophan is limiting, and amino acid supplementation will reduce that sensitivity. Other resistance mechanisms will not respond this way."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Antibiotic and standard-condition fitness data exist, but the supplementation contrast needs new experiments."
collections: ["kescience-fitnessbrowser"]
findings: ["amr_cofitness_networks--6571fdb3", "amr_cofitness_networks--9d334076", "amr_cofitness_networks--284c5695"]
conflicts: ["conflict--cofitness-network-architecture--268ee500"]
papers: ["21645016", "39038993", "25968644", "23499305"]
builds_on: ["findings/amr_cofitness_networks--6571fdb3", "findings/amr_cofitness_networks--9d334076", "findings/amr_cofitness_networks--284c5695", "conflicts/conflict--cofitness-network-architecture--268ee500"]
projects: ["amr_cofitness_networks"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Does amino acid biosynthesis shape how much efflux pumps matter for antibiotic tolerance?

Efflux resistance genes neighbor histidine and tryptophan biosynthesis genes in fitness-correlation networks across several organisms, although no function was specific to a resistance mechanism once corrected for repeated testing. Does biosynthesis status modulate efflux dependence?

## Hypothesis

Efflux pump mutants will be more sensitive to antibiotics when histidine or tryptophan is limiting, and amino acid supplementation will reduce that sensitivity. Other resistance mechanisms will not respond this way.

## Why it matters

A metabolic dependence of efflux-mediated tolerance would show that nutrient state changes drug susceptibility, so culture medium choice would matter for resistance testing. A null result would support the view that this enrichment only reflects genes being dispensable in the lab.

## How to test it

In a Fitness Browser organism with many efflux genes, run barcoded transposon fitness under a sub-inhibitory antibiotic with and without histidine and tryptophan supplementation. Compare efflux, enzymatic-inactivation and metal-resistance genes. Use existing Fitness Browser data to check whether the histidine and tryptophan biosynthesis neighborhoods are stronger under antibiotics than in standard growth.

## What would support or refute it

Support: efflux gene fitness shifts with amino acid supplementation under antibiotic, while other mechanism classes do not. Refute: supplementation changes nothing for efflux genes, or changes all gene classes equally.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Antibiotic and standard-condition fitness data exist, but the supplementation contrast needs new experiments.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/amr_cofitness_networks--6571fdb3|No GO term is mechanism-specific after FDR correction]] (Insufficient literature evidence)
- Finding: [[findings/amr_cofitness_networks--9d334076|InterProScan GO annotations reveal AMR cofitness enrichment across organisms]] (Insufficient literature evidence)
- Finding: [[findings/amr_cofitness_networks--284c5695|Flagellum-dependent motility GO term enriched across several organisms]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cofitness-network-architecture--268ee500|AMR Fitness Cost: Uniform and Structure-Independent, or Mechanism-Dependent?]]

## Closest published work

- [PMID 21645016](https://pubmed.ncbi.nlm.nih.gov/21645016/) Metabolic regulation of antibiotic resistance.
- [PMID 39038993](https://pubmed.ncbi.nlm.nih.gov/39038993/) Tryptophan transport gene inactivation promotes the development of antibiotic resistance in Escherichia coli.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 23499305](https://pubmed.ncbi.nlm.nih.gov/23499305/) Intrinsic antibiotic resistance: mechanisms, origins, challenges and solutions.

PMID 21645016 and PMID 39038993 link metabolism and tryptophan transport to antibiotic resistance. They do not test whether efflux dependence changes with amino acid biosynthesis status.
