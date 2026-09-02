---
type: "Method"
description: "Prokaryote-restricted classifier evaluated for eukaryotic read detection."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/harvard_forest_warming__REPORT.md"]
---
# Kraken2

## What it is

**Canonical name:** Kraken2. [src: euk_in_prok_correlates]

**Known aliases:** No aliases were reported in the source document. [src: euk_in_prok_correlates]

**Stable external identifier:** None was reported in the source document. [src: euk_in_prok_correlates]

Kraken2 is a taxonomic classification method whose NMDC deployment used a prokaryote-restricted reference database. [src: euk_in_prok_correlates]

## Evidence from euk_in_prok_correlates

Kraken2 produced approximately 0 domain-level Eukaryota signal in the analysis of 2,759 NMDC ReadbasedAnalysis runs because its NMDC reference database was prokaryote-restricted. [src: euk_in_prok_correlates]

The only eukaryotic kingdom represented in the Kraken2 deployment was Metazoa/human. [src: euk_in_prok_correlates]

Because Kraken2 produced approximately 0 usable domain-level Eukaryota signal, it was not used to estimate the eukaryotic fraction in this analysis. [src: euk_in_prok_correlates]

The result demonstrates that Kraken2 and [[entities/centrifuge]] were not interchangeable with [[entities/gottcha2]] for eukaryote quantification in this NMDC deployment, because GOTTCHA2 was plastid- and eukaryote-aware whereas the Kraken2 and Centrifuge databases were prokaryote-restricted. [src: euk_in_prok_correlates]

Accordingly, cross-collection contamination-quality-control analyses should account for classifier and database compatibility rather than treating Kraken2-derived and GOTTCHA2-derived eukaryotic fractions as equivalent. [src: euk_in_prok_correlates]

## Evidence from harvard_forest_warming

The Harvard Forest study **refines** the eukaryote-detection limitation: despite the prokaryote-restricted deployment, Kraken2 read-based relative abundance was used for bacterial community comparison and detected Actinobacteria increasing from 0.249 to 0.315 and Acidobacteria decreasing from 0.035 to 0.024 in heated organic soil, with q=0.049 for both changes. [src: harvard_forest_warming]

This **supports** using Kraken2 for prokaryotic community-level contrasts while retaining the existing warning that its output is unsuitable for estimating eukaryotic fractions in this deployment. [src: harvard_forest_warming, euk_in_prok_correlates]

This method-specific limitation is relevant to [[concepts/multi-omics-integration]], which concerns integration of taxonomic results with environmental and sequencing metadata, and to [[concepts/cross-tenant-data-bridging]], which covers linking NMDC workflow results with sample metadata. [src: euk_in_prok_correlates]

See the project summaries: [[summaries/euk_in_prok_correlates__REPORT]] and [[summaries/harvard_forest_warming__REPORT]]. [src: euk_in_prok_correlates, harvard_forest_warming]
