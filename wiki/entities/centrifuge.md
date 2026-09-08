---
type: Method
description: Taxonomic classifier with genus-level ambiguity in this NMDC deployment
sources:
- id: euk_in_prok_correlates
  resource: ../summaries/euk_in_prok_correlates__REPORT.md
  title: euk in prok correlates
- id: nmdc_community_metabolic_ecology
  resource: ../summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
title: Centrifuge
---
# Centrifuge

## What this entity is

**Canonical name:** Centrifuge. [^euk_in_prok_correlates]

**Known aliases:** No aliases were reported in this document. [^euk_in_prok_correlates]

**Stable external identifier:** None was reported in this document. [^euk_in_prok_correlates]

Centrifuge is a taxonomic classification method used among the native NMDC read-based classification outputs. [^euk_in_prok_correlates]

## Key facts from the documents

In the earlier NMDC deployment, Centrifuge produced approximately 0 domain-level Eukaryota signal because its reference database was prokaryote-restricted. [^euk_in_prok_correlates]

Centrifuge therefore did not provide a usable estimator of eukaryotic fraction for that analysis, unlike the eukaryote- and plastid-aware GOTTCHA2 classification. [^euk_in_prok_correlates]

In the NMDC community-metabolic-ecology deployment, approximately 1,352 Centrifuge taxa matched multiple GTDB clades within the same genus; one representative clade was selected by alphabetical tiebreaking on `gtdb_species_clade_id`, and these genus-proxy-ambiguous taxa accounted for approximately 6.5% of mapped abundance. [^nmdc_community_metabolic_ecology]

This **refines** the earlier database-compatibility limitation: even when Centrifuge taxa support broad community-to-pangenome mapping, genus-level ambiguity can affect which GTDB species-clade pathway records are assigned. [^nmdc_community_metabolic_ecology]

The result illustrates that classifier databases were not interchangeable for eukaryote quantification in the [euk_in_prok_correlates__REPORT](../summaries/euk_in_prok_correlates__REPORT.md) analysis. [^euk_in_prok_correlates]

This limitation is relevant to [multi-omics-integration](../concepts/multi-omics-integration.md), because integrating read-based taxonomic results with environmental metadata requires checking whether each classifier and database can detect the target domain. [^euk_in_prok_correlates]

Centrifuge was evaluated alongside [kraken2](kraken2.md) in the NMDC classification workflow, while GOTTCHA2 supplied the usable eukaryotic-fraction response variable. [^euk_in_prok_correlates]

[^euk_in_prok_correlates]: [euk in prok correlates](../summaries/euk_in_prok_correlates__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../summaries/nmdc_community_metabolic_ecology__REPORT.md)
