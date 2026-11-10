---
type: "Research direction"
description: "Genus-level community profiles show no clear link between contamination and defense gene content, but a covariate-adjusted model hints at one. Does defense content differ between strains of the same genus taken from more and less contaminated wells?"
hypothesis: "Contamination selects defense gene content within genera, so strains of one genus from more contaminated wells carry more defense genes than strains of the same genus from cleaner wells, even though genus-level averages show no trend."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "It is not established that enough isolate genomes carry both well location and geochemistry; 862 of 1,392 observed genera did not map to the pangenome bridge."
collections: ["enigma-coral", "kbase-ke-pangenome"]
findings: ["enigma_contamination_functional_potential--f4cd1747", "enigma_contamination_functional_potential--606b2ef6", "enigma_contamination_functional_potential--a97faeef"]
conflicts: []
papers: ["35107332", "26583008", "30523276"]
builds_on: ["findings/enigma_contamination_functional_potential--f4cd1747", "findings/enigma_contamination_functional_potential--606b2ef6", "findings/enigma_contamination_functional_potential--a97faeef"]
projects: ["enigma_contamination_functional_potential"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is defense-gene enrichment under contamination hidden inside genera rather than between them?

Genus-level community profiles show no clear link between contamination and defense gene content, but a covariate-adjusted model hints at one. Does defense content differ between strains of the same genus taken from more and less contaminated wells?

## Hypothesis

Contamination selects defense gene content within genera, so strains of one genus from more contaminated wells carry more defense genes than strains of the same genus from cleaner wells, even though genus-level averages show no trend.

## Why it matters

A within-genus signal would reconcile the null at the genus scale with the contaminated-site reports of defense gene expansion in Rhodanobacter. It would also show that community-level proxies miss strain-scale selection.

## How to test it

Take isolate genomes from Oak Ridge wells in ENIGMA CORAL that can be linked to well coordinates and geochemistry, and link them to species pangenomes in the Pangenome Collection. For genera with isolates from both contaminated and clean wells (Rhodanobacter first), compare defense gene counts between wells using a model with genus as a grouping factor and well as a random effect.

## What would support or refute it

Support: within genera, defense counts rise with contamination level while the between-genus trend stays flat. Refute: within-genus differences are absent or fully explained by genome size or well identity.

## Data

Approach: analysis then experiment. Readiness: unknown. It is not established that enough isolate genomes carry both well location and geochemistry; 862 of 1,392 observed genera did not map to the pangenome bridge.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_contamination_functional_potential--f4cd1747|No significant defense–contamination association in relaxed mapping]] (Insufficient literature evidence)
- Finding: [[findings/enigma_contamination_functional_potential--606b2ef6|Confirmatory defense null holds across alternative contamination index definitions]] (In tension with retrieved work)
- Finding: [[findings/enigma_contamination_functional_potential--a97faeef|Covariate-adjusted models give a positive defense-contamination signal in relaxed mapping]] (Candidate novel)

## Closest published work

- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.
- [PMID 26583008](https://pubmed.ncbi.nlm.nih.gov/26583008/) Comparative metagenomics reveals impact of contaminants on groundwater microbiomes.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.

PMID 35107332 reports defense-gene expansion in Rhodanobacter from a contaminated aquifer and PMID 26583008 compares contaminated and pristine groundwater metagenomes. Neither tests defense content across a contamination gradient within a genus.
