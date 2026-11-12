---
type: "Research direction"
description: "Efflux genes had cofitness neighbours enriched in histidine biosynthesis in 6 organisms and tryptophan biosynthesis in 5, while metal-resistance genes showed a weaker version of this. The apparent difference between efflux and metal-resistance genes was only a hint and was not firm once the many comparisons were accounted for. Does amino-acid metabolism set how efflux genes act?"
hypothesis: "Efflux gene mutants change their antibiotic sensitivity when histidine or tryptophan availability changes. This reflects metabolic control of efflux, not shared lab dispensability."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Cofitness is in the Fitness Browser. Amino-acid supplementation contrasts may be sparse, so new assays are likely needed."
collections: ["kescience-fitnessbrowser"]
findings: ["amr_cofitness_networks--6571fdb3", "amr_cofitness_networks--9d334076", "amr_cofitness_networks--ca058750"]
conflicts: ["conflict--cofitness-network-architecture--268ee500"]
papers: ["21645016", "39038993", "23499305"]
builds_on: ["findings/amr_cofitness_networks--6571fdb3", "findings/amr_cofitness_networks--9d334076", "findings/amr_cofitness_networks--ca058750", "conflicts/conflict--cofitness-network-architecture--268ee500"]
projects: ["amr_cofitness_networks"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Are efflux pumps tied to amino-acid biosynthesis through the cell's metabolic state?

Efflux genes had cofitness neighbours enriched in histidine biosynthesis in 6 organisms and tryptophan biosynthesis in 5, while metal-resistance genes showed a weaker version of this. The apparent difference between efflux and metal-resistance genes was only a hint and was not firm once the many comparisons were accounted for. Does amino-acid metabolism set how efflux genes act?

## Hypothesis

Efflux gene mutants change their antibiotic sensitivity when histidine or tryptophan availability changes. This reflects metabolic control of efflux, not shared lab dispensability.

## Why it matters

It would tie resistance to nutrient state, which affects how resistance is treated or predicted. A null would show that the enrichment reflects shared dispensability.

## How to test it

Take efflux genes with biosynthesis neighbours in the Fitness Browser organisms where both were found. Use conditions with and without histidine or tryptophan to see whether efflux fitness shifts with supplementation more than for non-efflux genes of similar overall fitness. Then, in one organism, measure efflux mutants and biosynthesis mutants for sensitivity to a substrate antibiotic at graded amino-acid levels.

## What would support or refute it

Support: efflux mutant sensitivity shifts with amino-acid supply and the biosynthesis neighbours explain it. Refute: sensitivity does not change with supplementation, so the neighbourhood is shared dispensability.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Cofitness is in the Fitness Browser. Amino-acid supplementation contrasts may be sparse, so new assays are likely needed.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/amr_cofitness_networks--6571fdb3|No GO term is mechanism-specific after FDR correction]] (Insufficient literature evidence)
- Finding: [[findings/amr_cofitness_networks--9d334076|InterProScan GO annotations reveal AMR cofitness enrichment across organisms]] (Insufficient literature evidence)
- Finding: [[findings/amr_cofitness_networks--ca058750|Support-network size does not predict AMR gene fitness cost]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cofitness-network-architecture--268ee500|AMR Fitness Cost: Uniform and Structure-Independent, or Mechanism-Dependent?]]

## Closest published work

- [PMID 21645016](https://pubmed.ncbi.nlm.nih.gov/21645016/) Metabolic regulation of antibiotic resistance.
- [PMID 39038993](https://pubmed.ncbi.nlm.nih.gov/39038993/) Tryptophan transport gene inactivation promotes the development of antibiotic resistance in Escherichia coli.
- [PMID 23499305](https://pubmed.ncbi.nlm.nih.gov/23499305/) Intrinsic antibiotic resistance: mechanisms, origins, challenges and solutions.

PMID 21645016 reviews metabolic regulation of resistance and PMID 39038993 shows tryptophan transport loss promotes resistance. Neither tests efflux genes against biosynthesis cofitness neighbours.
