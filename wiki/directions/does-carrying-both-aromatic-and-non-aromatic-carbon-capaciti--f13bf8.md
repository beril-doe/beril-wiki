---
type: "Research direction"
description: "Why do only a few genomes carry both an aromatic-compound capacity and a non-aromatic one, and does holding both capacities slow growth on each substrate compared with relatives that hold only one?"
hypothesis: "Co-carriage is rarer than the lineage structure of Burkholderiales alone predicts. Generalist isolates grow more slowly on a single substrate, such as phenylethylamine, than same-genus specialists do on that same substrate, and they use a mixture one substrate at a time rather than together."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The capacity calls over 3109 genomes exist, but growth of generalist and matched specialist isolates on shared single substrates needs new assays."
collections: ["kbase-ke-pangenome", "kbase-genomes", "enigma-coral"]
findings: ["enigma_carbon_census_1--16f93626", "enigma_carbon_census_1--8b8214bb"]
conflicts: []
papers: ["22026719", "17030797", "30811107", "34067383"]
builds_on: ["findings/enigma_carbon_census_1--16f93626", "findings/enigma_carbon_census_1--8b8214bb"]
projects: ["enigma_carbon_census_1"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does carrying both aromatic and non-aromatic carbon capacities slow growth on either substrate?

Why do only a few genomes carry both an aromatic-compound capacity and a non-aromatic one, and does holding both capacities slow growth on each substrate compared with relatives that hold only one?

## Hypothesis

Co-carriage is rarer than the lineage structure of Burkholderiales alone predicts. Generalist isolates grow more slowly on a single substrate, such as phenylethylamine, than same-genus specialists do on that same substrate, and they use a mixture one substrate at a time rather than together.

## Why it matters

It would explain why versatility looks like a clade trait rather than a portable module. It would also indicate whether engineering aromatic degraders into other chassis carries a hidden growth cost.

## How to test it

Within the Pangenome Collection genomes that carry at least one census capacity, compare how often aromatic and non-aromatic capacities co-occur against a null that shuffles capacities among genomes of the same genus. Then pick generalists (Paraburkholderia, Burkholderia, Hydrogenophaga) and single-capacity specialists from the same genera. Grow all of them on the same single substrates: phenylethylamine alone and a non-aromatic substrate alone, so substrate is held fixed and only the number of capacities differs. Also grow the generalists on the mixture and record whether the two substrates are used together or in sequence.

## What would support or refute it

Support: co-carriage falls below the genus-shuffled expectation, generalists grow more slowly than same-genus specialists on the same single substrate, and mixture use is sequential. Refutation: co-carriage matches the genus null and generalists match specialists on each shared substrate, so any difference is strain identity rather than a burden of co-carriage.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The capacity calls over 3109 genomes exist, but growth of generalist and matched specialist isolates on shared single substrates needs new assays.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/enigma_carbon_census_1--16f93626|Aromatic and non-aromatic capacities almost never occur in the same genome]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--8b8214bb|Callable capacity mostly single-capacity, Burkholderiales-concentrated, suggesting a clade trait]] (Extends retrieved work)

## Closest published work

- [PMID 22026719](https://pubmed.ncbi.nlm.nih.gov/22026719/) Genomic analysis of the potential for aromatic compounds biodegradation in Burkholderiales.
- [PMID 17030797](https://pubmed.ncbi.nlm.nih.gov/17030797/) Burkholderia xenovorans LB400 harbors a multi-replicon, 9.73-Mbp genome shaped for versatility.
- [PMID 30811107](https://pubmed.ncbi.nlm.nih.gov/30811107/) Comparative genomics of Paraburkholderia kururiensis and its potential in bioremediation, biofertilization, and biocontrol of plant pathogens.
- [PMID 34067383](https://pubmed.ncbi.nlm.nih.gov/34067383/) Pan-Genome Analysis Reveals Host-Specific Functional Divergences in Burkholderia gladioli.

PMID 22026719 reports that aromatic catabolic versatility in Burkholderiales is shaped by lineage and habitat. It does not ask whether combining aromatic and non-aromatic capacities is disfavoured or slows growth, which neither PMID 17030797 nor PMID 30811107 tests.
