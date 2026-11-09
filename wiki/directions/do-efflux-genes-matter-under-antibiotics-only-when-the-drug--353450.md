---
type: "Research direction"
description: "Resistance mechanisms showed no detected difference in baseline knockout fitness, yet efflux genes flip toward importance under antibiotics more than enzymatic inactivation genes do. Is that flip set by how well each antibiotic matches the gene product's substrates, rather than by the mechanism class?"
hypothesis: "The antibiotic-dependent flip toward importance is set by substrate match between the drug and the gene product. Broad-spectrum pumps flip under many antibiotic classes, narrow pumps only under their own drugs, and enzymatic genes only under their specific drug."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Knockout fitness for resistance genes under antibiotic and non-antibiotic conditions is already compiled for 25 Fitness Browser organisms; drug-spectrum labels must be added from annotations, and the existing classifier leaves some genes (about 25) in an unknown mechanism class."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["amr_fitness_cost--7ffc7d6b", "amr_fitness_cost--104baecc", "amr_fitness_cost--4f2f8508"]
conflicts: ["conflict--antimicrobial-resistance-fitness-cost--3139de09"]
papers: ["26203082", "25861385", "20208551", "34827256"]
builds_on: ["findings/amr_fitness_cost--7ffc7d6b", "findings/amr_fitness_cost--104baecc", "findings/amr_fitness_cost--4f2f8508", "conflicts/conflict--antimicrobial-resistance-fitness-cost--3139de09"]
projects: ["amr_fitness_cost", "fitness_effects_conservation"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do efflux genes matter under antibiotics only when the drug matches their substrates?

Resistance mechanisms showed no detected difference in baseline knockout fitness, yet efflux genes flip toward importance under antibiotics more than enzymatic inactivation genes do. Is that flip set by how well each antibiotic matches the gene product's substrates, rather than by the mechanism class?

## Hypothesis

The antibiotic-dependent flip toward importance is set by substrate match between the drug and the gene product. Broad-spectrum pumps flip under many antibiotic classes, narrow pumps only under their own drugs, and enzymatic genes only under their specific drug.

## Why it matters

Mechanism class did not predict baseline fitness, but efflux and enzymatic genes differ once antibiotics are present, and about 43% of resistance genes do not flip at all. If substrate match explains this, a gene's value could be predicted from the drugs it covers, which would change how resistance maintenance is modelled in mixed-drug environments.

## How to test it

In the Fitness Browser, take the resistance genes with knockout fitness data across the 25 organisms. Label each gene's likely drug spectrum from its annotation, and subdivide efflux genes into narrow-spectrum drug pumps and general multidrug systems. For every antibiotic experiment, mark whether the drug lies in the gene's expected spectrum. Compare the change in knockout fitness for matched versus unmatched drug-gene pairs, separately for efflux and enzymatic genes. Include organism as a grouping term so the large gene sets in Cupriavidus and BFirm do not dominate.

## What would support or refute it

Support: knockout fitness shifts mainly in matched drug-gene pairs, and the efflux versus enzymatic contrast shrinks once matching is accounted for. Refutation: efflux genes still flip under unmatched antibiotics, or matched enzymatic genes also fail to flip, so mechanism class rather than substrate match drives the pattern.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Knockout fitness for resistance genes under antibiotic and non-antibiotic conditions is already compiled for 25 Fitness Browser organisms; drug-spectrum labels must be added from annotations, and the existing classifier leaves some genes (about 25) in an unknown mechanism class.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_fitness_cost--7ffc7d6b|Efflux genes flip toward importance under antibiotics more than enzymatic inactivation genes]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--104baecc|Fitness cost does not vary by resistance mechanism]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--4f2f8508|AMR gene knockouts are less costly than other knockouts without antibiotics]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--antimicrobial-resistance-fitness-cost--3139de09|Do AMR genes follow the all-gene link between fitness importance and conservation?]]

## Closest published work

- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.
- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?
- [PMID 34827256](https://pubmed.ncbi.nlm.nih.gov/34827256/) In-Vitro Selection of Ceftazidime/Avibactam Resistance in OXA-48-Like-Expressing Klebsiella pneumoniae: In-Vitro and In-Vivo Fitness, Genetic Basis and Activities of β-Lactam Plus Novel β-Lactamase Inhibitor or β-Lactam Enhancer Combinations.

PMID 26203082 shows resistance genes can give an advantage in vivo but does not split the effect by mechanism or drug match; PMIDs 25861385 and 20208551 cover costs of resistance mutations, not condition-matched knockout effects of native genes.
