---
type: "Research direction"
description: "Genus-aggregated community function showed no contamination effect, but a covariate-adjusted model hinted at a rise in defense genes. If isolates with known well of origin exist, do strains from more contaminated wells carry more defense genes than strains of the same genus from cleaner wells?"
hypothesis: "Within some genera, such as Rhodanobacter, strains from more contaminated wells carry more defense-related genes than strains from cleaner wells, even where genus-level abundance and genus-aggregated function show no contamination effect."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Strain isolation-well records appear to exist in ENIGMA CORAL, but whether enough isolates per genus carry both a genome and contamination data is not established."
collections: ["enigma-coral", "kbase-ke-pangenome"]
findings: ["enigma_contamination_functional_potential--a97faeef", "enigma_contamination_functional_potential--f4cd1747", "enigma_contamination_functional_potential--606b2ef6"]
conflicts: ["conflict--taxonomic-resolution-dependent-functional-inference--326d40ea"]
papers: ["35107332", "26583008", "30523276"]
builds_on: ["findings/enigma_contamination_functional_potential--a97faeef", "findings/enigma_contamination_functional_potential--f4cd1747", "findings/enigma_contamination_functional_potential--606b2ef6", "conflicts/conflict--taxonomic-resolution-dependent-functional-inference--326d40ea"]
projects: ["ecotype_functional_differentiation", "enigma_contamination_functional_potential"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does contamination select defense-gene-rich strains within genera whose community-level signal is null?

Genus-aggregated community function showed no contamination effect, but a covariate-adjusted model hinted at a rise in defense genes. If isolates with known well of origin exist, do strains from more contaminated wells carry more defense genes than strains of the same genus from cleaner wells?

## Hypothesis

Within some genera, such as Rhodanobacter, strains from more contaminated wells carry more defense-related genes than strains from cleaner wells, even where genus-level abundance and genus-aggregated function show no contamination effect.

## Why it matters

It would show that selection by contaminants acts on strain gene content, which genus-level surveys miss, and would help explain why genus-aggregated nulls do not mean absence of functional response.

## How to test it

First establish what ENIGMA CORAL holds: isolate or strain genomes linked to well of origin, and which contamination measures exist per well. For genera with enough linked isolates, count defense-annotated genes per genome using the Pangenome Collection and compare strains from high- and low-contamination wells. Separately test, using the community data, whether abundance of the same genera varies with contamination, since that has not been tested. Genera with too few isolates are excluded.

## What would support or refute it

Support: defense gene count per genome rises with contamination within genera while genus abundance does not track contamination. Refute: within-genus defense content does not differ by contamination, consistent with the genus-level null, or abundance itself tracks contamination so the premise fails.

## Data

Approach: lakehouse analysis. Readiness: unknown. Strain isolation-well records appear to exist in ENIGMA CORAL, but whether enough isolates per genus carry both a genome and contamination data is not established.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_contamination_functional_potential--a97faeef|Covariate-adjusted models give a positive defense-contamination signal in relaxed mapping]] (Candidate novel)
- Finding: [[findings/enigma_contamination_functional_potential--f4cd1747|No significant defense–contamination association in relaxed mapping]] (Insufficient literature evidence)
- Finding: [[findings/enigma_contamination_functional_potential--606b2ef6|Confirmatory defense null holds across alternative contamination index definitions]] (In tension with retrieved work)
- Conflict: [[conflicts/conflict--taxonomic-resolution-dependent-functional-inference--326d40ea|Within-Species Ecotype Differentiation Versus Genus-Level Contamination Function Signals]]

## Closest published work

- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.
- [PMID 26583008](https://pubmed.ncbi.nlm.nih.gov/26583008/) Comparative metagenomics reveals impact of contaminants on groundwater microbiomes.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.

PMID 35107332 reports expansion of defense gene families in contaminated-site Rhodanobacter, and PMID 26583008 compares two wells; neither tests strain defense content along a contamination gradient across genera.
