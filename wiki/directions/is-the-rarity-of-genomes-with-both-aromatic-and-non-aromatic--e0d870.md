---
type: "Research direction"
description: "Is the scarcity of genomes carrying both an aromatic and a non-aromatic callable capacity (25 of 3109) explained by lineage alone, or does it suggest an additional exclusion or cost between the two capacity types?"
hypothesis: "Against a null that conditions on lineage, the observed co-occurrence is lower than expected. That would suggest an exclusion beyond lineage, such as a metabolic or regulatory cost of holding both, rather than lineage membership alone."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The capacity matrix and GTDB placement exist and the reanalysis used saved 2x2 counts, so the phylogenetic models are new compute; the module-transfer test needs new strain work."
collections: ["kbase-ke-pangenome"]
findings: ["enigma_carbon_census_1--16f93626", "enigma_carbon_census_1--8b8214bb", "enigma_carbon_census_1--bc52527b", "enigma_carbon_census_1--f8b7ca8b"]
conflicts: []
papers: ["22026719", "17030797", "30811107", "34067383"]
builds_on: ["findings/enigma_carbon_census_1--16f93626", "findings/enigma_carbon_census_1--8b8214bb", "findings/enigma_carbon_census_1--bc52527b", "findings/enigma_carbon_census_1--f8b7ca8b"]
projects: ["enigma_carbon_census_1"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Is the rarity of genomes with both aromatic and non-aromatic capacity beyond lineage expectation?

Is the scarcity of genomes carrying both an aromatic and a non-aromatic callable capacity (25 of 3109) explained by lineage alone, or does it suggest an additional exclusion or cost between the two capacity types?

## Hypothesis

Against a null that conditions on lineage, the observed co-occurrence is lower than expected. That would suggest an exclusion beyond lineage, such as a metabolic or regulatory cost of holding both, rather than lineage membership alone.

## Why it matters

The specialist excess (675 specialists vs 18 generalists among genomes carrying at least 1 of 8 capacities) is descriptive. A below-null result would suggest a trade-off that limits combining catabolic modules. A null-consistent result would show that lineage alone is enough.

## How to test it

With the 3109-genome capacity matrix and GTDB phylogeny, run trait-evolution or lineage-stratified permutation models of aromatic and non-aromatic co-occurrence. Note that capacities are only the 8 called ones, not total carbon-use breadth, and the xanthine call is a known mis-inclusion. Experimentally, introduce a paa-route aromatic module into a non-aromatic specialist and measure growth cost on non-aromatic carbon sources, with Paraburkholderia and Burkholderia generalists as references.

## What would support or refute it

Support: lineage-conditioned co-occurrence is below the null and the engineered strain pays a measurable growth cost. Refute: co-occurrence matches the lineage null and the module is neutral, so rarity reflects lineage and annotation sparsity.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The capacity matrix and GTDB placement exist and the reanalysis used saved 2x2 counts, so the phylogenetic models are new compute; the module-transfer test needs new strain work.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_carbon_census_1--16f93626|Aromatic and non-aromatic capacities almost never occur in the same genome]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--8b8214bb|Callable capacity mostly single-capacity, Burkholderiales-concentrated, suggesting a clade trait]] (Extends retrieved work)
- Finding: [[findings/enigma_carbon_census_1--bc52527b|Xanthine was mis-included as a carbon-catabolic callable compound]] (Established in retrieved literature)
- Finding: [[findings/enigma_carbon_census_1--f8b7ca8b|Uniform class coverage of isolate-callable compounds not rejected, by an underpowered test]] (Insufficient literature evidence)

## Closest published work

- [PMID 22026719](https://pubmed.ncbi.nlm.nih.gov/22026719/) Genomic analysis of the potential for aromatic compounds biodegradation in Burkholderiales.
- [PMID 17030797](https://pubmed.ncbi.nlm.nih.gov/17030797/) Burkholderia xenovorans LB400 harbors a multi-replicon, 9.73-Mbp genome shaped for versatility.
- [PMID 30811107](https://pubmed.ncbi.nlm.nih.gov/30811107/) Comparative genomics of Paraburkholderia kururiensis and its potential in bioremediation, biofertilization, and biocontrol of plant pathogens.
- [PMID 34067383](https://pubmed.ncbi.nlm.nih.gov/34067383/) Pan-Genome Analysis Reveals Host-Specific Functional Divergences in Burkholderia gladioli.

PMID 22026719 reports aromatic versatility as a lineage-level property in 80 Burkholderiales genomes. This asks whether co-occurrence of aromatic and non-aromatic capacity across 3109 genomes falls below a lineage-conditioned null, and tests the cost of combining them.
