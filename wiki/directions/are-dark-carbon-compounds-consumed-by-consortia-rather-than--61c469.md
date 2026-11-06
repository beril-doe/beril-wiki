---
type: "Research direction"
description: "Most compounds in the ENIGMA Carbon Census (74 of 83) have no isolate known to use them. Is that because their breakdown requires several organisms working in sequence, rather than missing annotation in single genomes?"
hypothesis: "Freshwater biofilm communities rich in Burkholderiales and Comamonadaceae will consume some dark compounds, but no single isolate from the enrichment will grow on them alone. Consumption will need a pair or small group."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The compounds and candidate sources are identified, but the isolates, enrichments and chemical measurements do not exist yet."
collections: ["nmdc-arkin", "enigma-coral", "kbase-ke-pangenome"]
findings: ["enigma_carbon_census_1--5022536d", "enigma_carbon_census_1--8512f374", "enigma_carbon_census_1--f8b7ca8b"]
conflicts: []
papers: ["22026719", "34612321", "40960580", "19457026"]
builds_on: ["findings/enigma_carbon_census_1--5022536d", "findings/enigma_carbon_census_1--8512f374", "findings/enigma_carbon_census_1--f8b7ca8b"]
projects: ["enigma_carbon_census_1"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Are dark carbon compounds consumed by consortia rather than by any single isolate?

Most compounds in the ENIGMA Carbon Census (74 of 83) have no isolate known to use them. Is that because their breakdown requires several organisms working in sequence, rather than missing annotation in single genomes?

## Hypothesis

Freshwater biofilm communities rich in Burkholderiales and Comamonadaceae will consume some dark compounds, but no single isolate from the enrichment will grow on them alone. Consumption will need a pair or small group.

## Why it matters

It would show that the unexplained part of environmental carbon turnover reflects community division of labour as well as unannotated enzymes. This would change how enrichments and isolate screens are designed.

## How to test it

Using NMDC Multi-omics and the Carbon Census compounds, choose the dark alkaloids and terpenoids with no pathway annotations. Inoculate freshwater biofilm (periphyton) samples onto minimal medium with each compound as sole carbon source, and confirm loss of the compound by chemical measurement. Isolate members, test each alone and in pairs, and sequence the enriched communities. Compare against the known-callable aromatic compounds as a positive control.

## What would support or refute it

Support: communities consume dark compounds while single isolates fail, and specific pairs restore growth. Refutation: single isolates grow on the compounds, which would point to annotation gaps, or no community consumes them.

## Data

Approach: experiment. Readiness: needs new measurements. The compounds and candidate sources are identified, but the isolates, enrichments and chemical measurements do not exist yet.

- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_carbon_census_1--5022536d|Most census compounds lack utilizer calls, biased by chemical class]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--8512f374|Freshwater biofilm samples show high prevalence of Burkholderiales/Comamonadaceae genera]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--f8b7ca8b|Uniform class coverage of isolate-callable compounds not rejected, by an underpowered test]] (Insufficient literature evidence)

## Closest published work

- [PMID 22026719](https://pubmed.ncbi.nlm.nih.gov/22026719/) Genomic analysis of the potential for aromatic compounds biodegradation in Burkholderiales.
- [PMID 34612321](https://pubmed.ncbi.nlm.nih.gov/34612321/) Biosynthesis, evolution and ecology of microbial terpenoids.
- [PMID 40960580](https://pubmed.ncbi.nlm.nih.gov/40960580/) Atranone-an underestimated secondary metabolite?
- [PMID 19457026](https://pubmed.ncbi.nlm.nih.gov/19457026/) Polaromonas and Hydrogenophaga species are the predominant bacteria cultured from granular activated carbon filters in water treatment.

PMID 22026719 shows aromatic versatility is lineage-bound in Burkholderiales, and PMID 34612321 and PMID 40960580 note poorly understood terpenoid biology. None tests single-organism versus consortium use of compounds that lack known catabolic routes.
