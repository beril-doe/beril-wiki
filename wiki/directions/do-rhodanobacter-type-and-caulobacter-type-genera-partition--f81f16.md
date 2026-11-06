---
type: "Research direction"
description: "Which genomic features explain the global pH and temperature separation between the Rhodanobacter-Ralstonia-Dyella cluster and the Brevundimonas-Caulobacter-Sphingomonas cluster?"
hypothesis: "Acid tolerance genes (proton homeostasis, acid resistance) distinguish the acidic cluster, so genus-blocked models trained on these features predict pH-dependent growth of strains from both clusters."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Clusters were defined across 464K samples but pH growth data for isolates need to be measured."
collections: ["kbase-ke-pangenome", "kbase-phenotype", "enigma-coral"]
findings: ["genotype_to_phenotype_enigma--a6ede42b", "genotype_to_phenotype_enigma--602fd76d", "genotype_to_phenotype_enigma--ccab2bff"]
conflicts: []
papers: ["38366921", "40118314", "42271456", "22179233"]
builds_on: ["findings/genotype_to_phenotype_enigma--a6ede42b", "findings/genotype_to_phenotype_enigma--602fd76d", "findings/genotype_to_phenotype_enigma--ccab2bff"]
projects: ["genotype_to_phenotype_enigma"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do Rhodanobacter-type and Caulobacter-type genera partition by pH through identifiable genes?

Which genomic features explain the global pH and temperature separation between the Rhodanobacter-Ralstonia-Dyella cluster and the Brevundimonas-Caulobacter-Sphingomonas cluster?

## Hypothesis

Acid tolerance genes (proton homeostasis, acid resistance) distinguish the acidic cluster, so genus-blocked models trained on these features predict pH-dependent growth of strains from both clusters.

## Why it matters

It would give mechanism to a correlational niche partition (1.35 pH units more acidic and 6.9°C warmer) and a basis for predicting contaminated-site community shifts from genomes.

## How to test it

Fit genus-blocked models of growth pH optimum from KO content (kbase-ke-pangenome, kbase-phenotype) and compare features with cluster-distinguishing KOs. Measure growth of Cluster A and B isolates across pH. Test co-occurrence with compositionally aware SparCC on the 100WS ASV matrix.

## What would support or refute it

Support: cluster-distinguishing KOs predict pH tolerance under genus-blocked validation. Refute: no predictive power across genera, as with the continuous growth-parameter null.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Clusters were defined across 464K samples but pH growth data for isolates need to be measured.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--a6ede42b|Global pH niche partition separates two Oak Ridge genus clusters]] (Candidate novel)
- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Finding: [[findings/genotype_to_phenotype_enigma--ccab2bff|Continuous growth parameters are not predictable across genera from gene content]] (Insufficient literature evidence)

## Closest published work

- [PMID 38366921](https://pubmed.ncbi.nlm.nih.gov/38366921/) Influence of host phylogeny and water physicochemistry on microbial assemblages of the fish skin microbiome.
- [PMID 40118314](https://pubmed.ncbi.nlm.nih.gov/40118314/) The response and ecological implications between various sulfur forms and environmental factors in acid mine drainage.
- [PMID 42271456](https://pubmed.ncbi.nlm.nih.gov/42271456/) Machine learning-based linking of bacterial genomes to optimal growth pH: a foundation for rational microbial engineering.
- [PMID 22179233](https://pubmed.ncbi.nlm.nih.gov/22179233/) Denitrifying bacteria from the genus Rhodanobacter dominate bacterial communities in the highly contaminated subsurface of a nuclear legacy waste site.

PMID 38366921 and 40118314 link pH and temperature to Ralstonia and Sphingomonas in other settings, and 42271456 predicts optimal pH from genomes; none tests this cluster contrast.
