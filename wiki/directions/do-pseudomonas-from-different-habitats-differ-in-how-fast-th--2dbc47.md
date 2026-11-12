---
type: "Research direction"
description: "Pathway presence alone discriminated habitats only modestly among free-living Pseudomonas. Do isolates of one species from soil, plant roots and water differ in growth rate on plant-derived sugars even when the same pathway is present in all of them?"
hypothesis: "Within Pseudomonas fluorescens-group and P. putida species, plant-root isolates grow faster than water isolates on xylose, arabinose and myo-inositol. The pathway genes are present in both, so the difference lies in transport or regulation that pathway-presence calls cannot see."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Pathway calls and isolation metadata are in the catalog, but growth rates of habitat-sorted isolates on these sugars must be measured, and how many species have enough isolates per habitat was not shown."
databases: ["kbase.ke_pangenome", "kescience.bacdive", "kescience.fitnessbrowser"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env", "kescience.fitnessbrowser.experiment", "kescience.bacdive.isolation"]
findings: ["pseudomonas_carbon_ecology--0211e0cd", "pseudomonas_carbon_ecology--cbe7e256", "pseudomonas_carbon_ecology--eb1d58ae"]
conflicts: ["conflict--ecotype-environment-gene-content--30e389f5"]
papers: ["22576821", "41332517", "26194109", "19137341"]
builds_on: ["findings/pseudomonas_carbon_ecology--0211e0cd", "findings/pseudomonas_carbon_ecology--cbe7e256", "findings/pseudomonas_carbon_ecology--eb1d58ae", "conflicts/conflict--ecotype-environment-gene-content--30e389f5"]
projects: ["cf_formulation_design", "pseudomonas_carbon_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do Pseudomonas from different habitats differ in how fast they use plant sugars despite equal pathways?

Pathway presence alone discriminated habitats only modestly among free-living Pseudomonas. Do isolates of one species from soil, plant roots and water differ in growth rate on plant-derived sugars even when the same pathway is present in all of them?

## Hypothesis

Within Pseudomonas fluorescens-group and P. putida species, plant-root isolates grow faster than water isolates on xylose, arabinose and myo-inositol. The pathway genes are present in both, so the difference lies in transport or regulation that pathway-presence calls cannot see.

## Why it matters

It would show that habitat adaptation in carbon use sits in quantitative performance, not gene presence. That would explain the weak habitat signal in pathway profiles, and it would redirect the search for niche markers toward regulation and transport variants.

## How to test it

From the pangenome collection, choose species with isolates from at least two habitats whose genomes all carry the three pathways. Order or obtain about 10 isolates per habitat. Measure growth rate and yield on each sugar as sole carbon source in plate readers. Compare habitats within species. Check whether growth tracks the pathway-completeness scores, and compare with carbon-source growth in the Putida mutant-fitness experiments and in the strain-level utilization records for the same species. Then compare sugar-transporter and regulator gene variants between fast and slow growers.

## What would support or refute it

Support: growth rates differ by habitat on these sugars among isolates with identical pathway calls, and fast and slow growers differ in transporter or regulator variants. Refutation: rates are similar across habitats, or they track pathway completeness only. The coarse-pathway explanation for the weak habitat signal would then fall away.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Pathway calls and isolation metadata are in the catalog, but growth rates of habitat-sorted isolates on these sugars must be measured, and how many species have enough isolates per habitat was not shown.

## Builds on

- Finding: [[findings/pseudomonas_carbon_ecology--0211e0cd|Carbon profiles alone cannot discriminate fine-grained environments among free-living species]] (Extends retrieved work)
- Finding: [[findings/pseudomonas_carbon_ecology--cbe7e256|Random Forest predicts environment class from carbon pathways above chance]] (Insufficient literature evidence)
- Finding: [[findings/pseudomonas_carbon_ecology--eb1d58ae|Carbon pathway profiles associate with isolation environment across free-living and plant-associated species]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--30e389f5|Carbon-Pathway Habitat Signal vs. the Broad Species-Level Null on Environment and Gene Content]]

## Closest published work

- [PMID 22576821](https://pubmed.ncbi.nlm.nih.gov/22576821/) Identification of traits shared by rhizosphere-competent strains of fluorescent pseudomonads.
- [PMID 41332517](https://pubmed.ncbi.nlm.nih.gov/41332517/) Multi-strain Analysis of Pseudomonas putida Reveals the Metabolic and Genetic Diversity of the Species.
- [PMID 26194109](https://pubmed.ncbi.nlm.nih.gov/26194109/) Molecular mechanisms of xylose utilization by Pseudomonas fluorescens: overlapping genetic responses to xylose, xylulose, ribose and mannitol.
- [PMID 19137341](https://pubmed.ncbi.nlm.nih.gov/19137341/) Carbon utilization profiles of bacteria colonizing the headbox water of two paper machines in a Canadian mill.

PMID 22576821 links substrate-use profiles of 23 Pseudomonas strains to rhizosphere competence, and PMID 41332517 reports strain-level metabolic variation within P. putida. Neither compares growth rates among isolates of one species with identical pathway content across habitats.
