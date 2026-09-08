---
type: Method
description: GOTTCHA2 is a taxonomic classifier used to estimate eukaryotic read fractions.
sources:
- id: euk_in_prok_correlates
  resource: ../summaries/euk_in_prok_correlates__REPORT.md
  title: euk in prok correlates
title: GOTTCHA2
---
# GOTTCHA2

## What this entity is

**Canonical name:** GOTTCHA2. [^euk_in_prok_correlates]

**Type:** Method. [^euk_in_prok_correlates]

**Known aliases:** No aliases were reported in the source document. [^euk_in_prok_correlates]

**Stable external identifier:** No stable external identifier was reported in the source document. [^euk_in_prok_correlates]

GOTTCHA2 is a taxonomic classification method used in this analysis to quantify relative eukaryotic abundance in NMDC ReadbasedAnalysis runs. [^euk_in_prok_correlates]

## Evidence from euk_in_prok_correlates

GOTTCHA2 classifications from native `nmdc.results` tables were used to analyze 2,759 runs from 9 studies. [^euk_in_prok_correlates]

GOTTCHA2 detected eukaryotic reads in 77% of the 2,759 runs. [^euk_in_prok_correlates]

Across all runs, the median eukaryotic fraction was 2.7%, the mean was 13.3%, and 20% of runs exceeded 20% eukaryotic reads. [^euk_in_prok_correlates]

Among runs with detectable eukaryotic signal, plastid sequences represented a median 100% of that signal, indicating that the detected signal was dominated by plant or algal chloroplast DNA in this environmental collection. [^euk_in_prok_correlates]

The response variable was defined as the sum of Eukaryota and plastid abundance at superkingdom rank for each ReadbasedAnalysis run. [^euk_in_prok_correlates]

The GOTTCHA2-derived response was zero-inflated: 23% of runs had no detectable eukaryotic reads, while one in five runs exceeded 20% eukaryotic reads. [^euk_in_prok_correlates]

GOTTCHA2 was the only usable estimator of eukaryotic fraction in this analysis because the deployed [kraken2](kraken2.md) and [centrifuge](centrifuge.md) reference databases were prokaryote-restricted and produced approximately 0 domain-level Eukaryota signal. [^euk_in_prok_correlates]

The source reports that GOTTCHA2 was plastid- and eukaryote-aware, whereas the Kraken2 and Centrifuge deployments were not interchangeable with it for eukaryote quantification. [^euk_in_prok_correlates]

## Interpretation and limitations

GOTTCHA2 values should be interpreted as relative or ordinal contamination measures rather than calibrated absolute eukaryotic fractions because the estimates depend on the classifier and reference database. [^euk_in_prok_correlates]

The study therefore recommends controlling cross-collection contamination-QC correlates by study or batch, using GroupKFold by study or within-study contrasts. [^euk_in_prok_correlates]

This method is central to the source report's integration of taxonomic results with environmental and sequencing metadata, summarized in [euk_in_prok_correlates__REPORT](../summaries/euk_in_prok_correlates__REPORT.md) and related to [multi-omics-integration](../concepts/multi-omics-integration.md). [^euk_in_prok_correlates]

[^euk_in_prok_correlates]: [euk in prok correlates](../summaries/euk_in_prok_correlates__REPORT.md)
