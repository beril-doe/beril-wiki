---
type: "Research direction"
description: "Only 25 of 3109 genomes carry both an aromatic and a non-aromatic capacity from the carbon census, and the few genomes with three or more capacities concentrate in Paraburkholderia, Burkholderia and Hydrogenophaga. Is this separation a metabolic or regulatory conflict, or simply lineage history?"
hypothesis: "The separation is stronger than shared ancestry predicts, because carrying both kinds of capacity creates a redox or regulatory conflict. Isolates that carry both should therefore use an aromatic compound more slowly or less fully when a non-aromatic carbon source is present."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The decisive mixed-substrate growth tests need new measurements; for the shuffle, the catalog shows only per-isolate orthologous-group presence, and the 3109-genome capacity matrix and its gene-to-capacity mapping were not shown, so their availability is unknown."
databases: ["arkinlab.enigma_comparative", "kbase.ke_pangenome"]
tables: ["arkinlab.enigma_comparative.isolate_og_presence", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["enigma_carbon_census_1--16f93626", "enigma_carbon_census_1--8b8214bb", "enigma_carbon_census_1--bc52527b"]
conflicts: []
papers: ["22026719", "17030797", "30811107", "34067383"]
builds_on: ["findings/enigma_carbon_census_1--16f93626", "findings/enigma_carbon_census_1--8b8214bb", "findings/enigma_carbon_census_1--bc52527b"]
projects: ["enigma_carbon_census_1"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Do aromatic and non-aromatic catabolic capacities avoid each other beyond what lineage predicts?

Only 25 of 3109 genomes carry both an aromatic and a non-aromatic capacity from the carbon census, and the few genomes with three or more capacities concentrate in Paraburkholderia, Burkholderia and Hydrogenophaga. Is this separation a metabolic or regulatory conflict, or simply lineage history?

## Hypothesis

The separation is stronger than shared ancestry predicts, because carrying both kinds of capacity creates a redox or regulatory conflict. Isolates that carry both should therefore use an aromatic compound more slowly or less fully when a non-aromatic carbon source is present.

## Why it matters

A real conflict would explain why specialists dominate and would make aromatic-degrading chassis for bioremediation hard to combine with broad carbon use. If lineage alone explains it, versatility is limited by evolutionary history, not by physiology.

## How to test it

Step 1: build a lineage-aware expectation by shuffling capacity calls among genomes within the same genus, and ask whether the observed number of genomes carrying both kinds is lower than the shuffled genomes give. Use the census capacity calls as defined (eight aromatic/alkaloid capacities); the xanthine call that was mis-scored as carbon catabolism must be excluded, since the committed tables predate its removal. Step 2: grow versatile Paraburkholderia and Hydrogenophaga isolates on an aromatic compound alone, a non-aromatic census compound alone, and both together, recording growth timing and the NADH/NAD+ balance.

## What would support or refute it

Support: co-occurrence is lower than the within-genus shuffles give and aromatic use is delayed or reduced when the second carbon source is present. Refutation: co-occurrence matches the within-genus shuffles and mixed-substrate growth is simply the sum of the two single-substrate results.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The decisive mixed-substrate growth tests need new measurements; for the shuffle, the catalog shows only per-isolate orthologous-group presence, and the 3109-genome capacity matrix and its gene-to-capacity mapping were not shown, so their availability is unknown.

## Builds on

- Finding: [[findings/enigma_carbon_census_1--16f93626|Aromatic and non-aromatic capacities almost never occur in the same genome]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--8b8214bb|Callable capacity mostly single-capacity, Burkholderiales-concentrated, suggesting a clade trait]] (Extends retrieved work)
- Finding: [[findings/enigma_carbon_census_1--bc52527b|Xanthine was mis-included as a carbon-catabolic callable compound]] (Established in retrieved literature)

## Closest published work

- [PMID 22026719](https://pubmed.ncbi.nlm.nih.gov/22026719/) Genomic analysis of the potential for aromatic compounds biodegradation in Burkholderiales.
- [PMID 17030797](https://pubmed.ncbi.nlm.nih.gov/17030797/) Burkholderia xenovorans LB400 harbors a multi-replicon, 9.73-Mbp genome shaped for versatility.
- [PMID 30811107](https://pubmed.ncbi.nlm.nih.gov/30811107/) Comparative genomics of Paraburkholderia kururiensis and its potential in bioremediation, biofertilization, and biocontrol of plant pathogens.
- [PMID 34067383](https://pubmed.ncbi.nlm.nih.gov/34067383/) Pan-Genome Analysis Reveals Host-Specific Functional Divergences in Burkholderia gladioli.

PMID 22026719 finds aromatic versatility in Burkholderiales to be a lineage-level property shaped by habitat; it does not test whether aromatic and non-aromatic capacities exclude each other beyond lineage expectation.
