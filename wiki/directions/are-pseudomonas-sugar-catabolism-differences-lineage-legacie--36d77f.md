---
type: "Research direction"
description: "Does loss of plant-derived sugar pathways in the P. aeruginosa group reflect ancestral divergence, and do lifestyle effects exist within Pseudomonas_E once subgenus is controlled?"
hypothesis: "Within Pseudomonas_E, rhizosphere and soil species differ in specific carbon pathways beyond subgenus effects, and these differences predict condition-specific fitness."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pathway and fitness tables exist, but phylogenetic regression and within-species clustering are unrun."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["pseudomonas_carbon_ecology--9c42f41a", "pseudomonas_carbon_ecology--eb1d58ae", "pseudomonas_carbon_ecology--cbe7e256", "pseudomonas_carbon_ecology--0211e0cd"]
conflicts: ["conflict--ecotype-environment-gene-content--30e389f5"]
papers: ["22576821", "41332517", "29607620", "3922954", "26913973"]
builds_on: ["findings/pseudomonas_carbon_ecology--9c42f41a", "findings/pseudomonas_carbon_ecology--eb1d58ae", "findings/pseudomonas_carbon_ecology--cbe7e256", "findings/pseudomonas_carbon_ecology--0211e0cd", "conflicts/conflict--ecotype-environment-gene-content--30e389f5"]
projects: ["cf_formulation_design", "pseudomonas_carbon_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are Pseudomonas sugar-catabolism differences lineage legacies or niche adaptations?

Does loss of plant-derived sugar pathways in the P. aeruginosa group reflect ancestral divergence, and do lifestyle effects exist within Pseudomonas_E once subgenus is controlled?

## Hypothesis

Within Pseudomonas_E, rhizosphere and soil species differ in specific carbon pathways beyond subgenus effects, and these differences predict condition-specific fitness.

## Why it matters

It would separate recent niche adaptation from deep phylogenetic inertia in carbon metabolism, which is mixed in the current signal (balanced accuracy 0.408 ± 0.169).

## How to test it

Run PGLS (phylogenetic generalized least squares) on GapMind carbon-pathway completeness against environment in 54 species with subgenus as covariate; analyse P. fluorescens and P. putida for within-species metabolic ecotypes using kbase-ke-pangenome. Link pathways to RB-TnSeq fitness from kescience-fitnessbrowser on matching carbon sources.

## What would support or refute it

Support: environment associations remain within Pseudomonas_E and predict fitness. Refute: associations vanish after phylogenetic control, leaving the subgenus split (43 of 62 pathways) as the only signal.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pathway and fitness tables exist, but phylogenetic regression and within-species clustering are unrun.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/pseudomonas_carbon_ecology--9c42f41a|P. aeruginosa group has lost most plant-sugar catabolism relative to Pseudomonas_E]] (Candidate novel)
- Finding: [[findings/pseudomonas_carbon_ecology--eb1d58ae|Carbon pathway profiles associate with isolation environment across free-living and plant-associated species]] (Extends retrieved work)
- Finding: [[findings/pseudomonas_carbon_ecology--cbe7e256|Random Forest predicts environment class from carbon pathways above chance]] (Insufficient literature evidence)
- Finding: [[findings/pseudomonas_carbon_ecology--0211e0cd|Carbon profiles alone cannot discriminate fine-grained environments among free-living species]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--30e389f5|Carbon-Pathway Habitat Signal vs. the Broad Species-Level Null on Environment and Gene Content]]

## Closest published work

- [PMID 22576821](https://pubmed.ncbi.nlm.nih.gov/22576821/) Identification of traits shared by rhizosphere-competent strains of fluorescent pseudomonads.
- [PMID 41332517](https://pubmed.ncbi.nlm.nih.gov/41332517/) Multi-strain Analysis of Pseudomonas putida Reveals the Metabolic and Genetic Diversity of the Species.
- [PMID 29607620](https://pubmed.ncbi.nlm.nih.gov/29607620/) Regulation of carbohydrate degradation pathways in Pseudomonas involves a versatile set of transcriptional regulators.
- [PMID 3922954](https://pubmed.ncbi.nlm.nih.gov/3922954/) Cloning of genes specifying carbohydrate catabolism in Pseudomonas aeruginosa and Pseudomonas putida.
- [PMID 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) The revisited genome of Pseudomonas putida KT2440 enlightens its value as a robust metabolic chassis.

PMID 22576821 links catabolic profiles of 23 strains to rhizosphere competence and 41332517 shows P. putida strain variation; neither separates niche from subgenus across species.
