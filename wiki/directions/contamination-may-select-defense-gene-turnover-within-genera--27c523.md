---
type: "Research direction"
description: "Do strains within contamination-associated genera differ in defense-related gene content along the contamination gradient, even though genus-aggregated profiles show no association?"
hypothesis: "Defense-category gene content varies among strains of the same genus along the contamination gradient. This explains why the genus-aggregated confirmatory test is null (rho = 0.0587, p = 0.546) while the covariate-adjusted relaxed-mapping model is positive."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genus-level bridging is built, but species- or strain-level mapping needs new computation, and the current bridge did not map 862 of 1,392 observed genera."
collections: ["enigma-coral", "kbase-ke-pangenome"]
findings: ["enigma_contamination_functional_potential--a97faeef", "enigma_contamination_functional_potential--f4cd1747", "enigma_contamination_functional_potential--606b2ef6", "cog_analysis--62995938", "cog_analysis--7a21065f"]
conflicts: ["conflict--taxonomic-resolution-dependent-functional-inference--326d40ea"]
papers: ["35107332", "26583008", "30523276", "41588461"]
builds_on: ["findings/enigma_contamination_functional_potential--a97faeef", "findings/enigma_contamination_functional_potential--f4cd1747", "findings/enigma_contamination_functional_potential--606b2ef6", "findings/cog_analysis--62995938", "findings/cog_analysis--7a21065f", "conflicts/conflict--taxonomic-resolution-dependent-functional-inference--326d40ea"]
projects: ["cog_analysis", "ecotype_functional_differentiation", "enigma_contamination_functional_potential"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Contamination may select defense-gene turnover within genera that genus-level community profiles hide

Do strains within contamination-associated genera differ in defense-related gene content along the contamination gradient, even though genus-aggregated profiles show no association?

## Hypothesis

Defense-category gene content varies among strains of the same genus along the contamination gradient. This explains why the genus-aggregated confirmatory test is null (rho = 0.0587, p = 0.546) while the covariate-adjusted relaxed-mapping model is positive.

## Why it matters

Retrieved work reports expanded defense COGs in contaminated-site Rhodanobacter and reduced functional redundancy under contamination. Strain-level selection would show that functional response to contamination can sit below genus resolution, and would explain differences between mapping modes.

## How to test it

Bridge ENIGMA community sequence variants to species or strain pangenome clades where possible, then compare defense and mobile-element COG content (cf. the +2.83% V and +10.88% L enrichment in novel genes) among strains of the same genus across sites. Test along uranium and contamination indices with depth and location as covariates, and include the 862 unmapped genera as a sensitivity check.

## What would support or refute it

Support: within-genus defense content shifts with contamination at finer resolution while the genus-aggregated test stays null. Refute: no association at species or strain level either, or the signal tracks mapped coverage. Gene-content ecotype structure inside species may be lineage-linked rather than ecological.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genus-level bridging is built, but species- or strain-level mapping needs new computation, and the current bridge did not map 862 of 1,392 observed genera.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_contamination_functional_potential--a97faeef|Covariate-adjusted models give a positive defense-contamination signal in relaxed mapping]] (Candidate novel)
- Finding: [[findings/enigma_contamination_functional_potential--f4cd1747|No significant defense–contamination association in relaxed mapping]] (Insufficient literature evidence)
- Finding: [[findings/enigma_contamination_functional_potential--606b2ef6|Confirmatory defense null holds across alternative contamination index definitions]] (In tension with retrieved work)
- Finding: [[findings/cog_analysis--62995938|Defense mechanisms are consistently enriched among novel genes]] (Insufficient literature evidence)
- Finding: [[findings/cog_analysis--7a21065f|Mobile elements dominate enrichment among novel genes across sampled species]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--taxonomic-resolution-dependent-functional-inference--326d40ea|Within-Species Ecotype Differentiation Versus Genus-Level Contamination Function Signals]]

## Closest published work

- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.
- [PMID 26583008](https://pubmed.ncbi.nlm.nih.gov/26583008/) Comparative metagenomics reveals impact of contaminants on groundwater microbiomes.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.
- [PMID 41588461](https://pubmed.ncbi.nlm.nih.gov/41588461/) Plasmids as persistent genetic reservoirs of bacterial defense systems in wastewater treatment.

PMID 35107332 reports defense-COG pan-genome expansion in contaminated-site Rhodanobacter and PMID 26583008 compares two wells; neither tests strain-level defense content along a contamination gradient across many genera.
