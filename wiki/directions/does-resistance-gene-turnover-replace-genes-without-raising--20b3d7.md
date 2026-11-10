---
type: "Research direction"
description: "Within species, does the identity of resistance genes shift over years while the total number per genome stays flat?"
hypothesis: "Total resistance gene count per genome stays constant over time, while the composition changes through replacement of older genes by newer ones, which explains why count trends are absent despite known increases of specific genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Collection dates and gene presence are available but date metadata is sparse and noisy, so power must be checked first."
collections: ["kbase-ke-pangenome"]
findings: ["amr_strain_variation--1d3c3dfa", "amr_strain_variation--f9cc56e8"]
conflicts: []
papers: ["40650755", "41423186", "42424350"]
builds_on: ["findings/amr_strain_variation--1d3c3dfa", "findings/amr_strain_variation--f9cc56e8"]
projects: ["amr_strain_variation"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does resistance gene turnover replace genes without raising the total per genome?

Within species, does the identity of resistance genes shift over years while the total number per genome stays flat?

## Hypothesis

Total resistance gene count per genome stays constant over time, while the composition changes through replacement of older genes by newer ones, which explains why count trends are absent despite known increases of specific genes.

## Why it matters

A flat count alongside rising single genes would suggest a ceiling on resistance load per genome, with new genes displacing old ones. That changes how resistance burden is modeled and monitored.

## How to test it

For species with many dated genomes in the Pangenome Collection, track per-gene prevalence by period together with total count. Compute turnover of gene identity (who is present) separately from count. Restrict to genomes with precise collection dates and to species where count is flat. Compare with the specific genes reported rising in A. baumannii and S. aureus.

## What would support or refute it

Support: composition shifts measurably over time in species whose count is flat, with some genes falling as others rise. Refutation: composition is also stable, meaning dates are too poor to detect change, or genes rise without any losses.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Collection dates and gene presence are available but date metadata is sparse and noisy, so power must be checked first.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_strain_variation--1d3c3dfa|No AMR gene-count temporal trend survives multiple-testing correction]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--f9cc56e8|Most within-species AMR gene occurrences are rare or variable, rarely fixed]] (Insufficient literature evidence)

## Closest published work

- [PMID 40650755](https://pubmed.ncbi.nlm.nih.gov/40650755/) Unravelling the genomic landscape of Acinetobacter baumannii: deep dive into virulence factors, resistance elements, and evolutionary adaptations.
- [PMID 41423186](https://pubmed.ncbi.nlm.nih.gov/41423186/) Comprehensive in silico genomic surveillance of β-lactam and methicillin resistance in Staphylococcus aureus: Machine learning-based analysis of lineage dynamics and global evolution.
- [PMID 42424350](https://pubmed.ncbi.nlm.nih.gov/42424350/) In silico antimicrobial resistance profiling of 1,240 Stenotrophomonas maltophilia genomes: AMR gene prevalence, temporal evolution, and ST-specific associations.

PMID 40650755 and PMID 41423186 report rising specific genes in single species, and PMID 42424350 finds some genes declining. None compares gene identity turnover with total count across many species.
