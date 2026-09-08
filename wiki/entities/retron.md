---
type: Gene_Or_Pathway
description: Anti-phage defense-system candidates detected through reverse-transcriptase
  markers
sources:
- id: phage_defense_arsenal
  resource: ../summaries/phage_defense_arsenal__REPORT.md
  title: phage defense arsenal
title: Retron
---
# Retron

## Identity

**Canonical name:** Retron. [^phage_defense_arsenal]

**Known aliases:** No aliases are reported in the source document. [^phage_defense_arsenal]

**Stable external identifier:** No stable external identifier is reported in the source document. [^phage_defense_arsenal]

Retron is treated in this analysis as an anti-phage defense-system category detected using reverse-transcriptase markers. [^phage_defense_arsenal]

## Evidence from the phage-defense arsenal

Retron markers were assessed as one of seven anti-phage defense-system families across the BERDL pangenome. [^phage_defense_arsenal]

Retron had a species-level prevalence of **54.7%** in the analysis. [^phage_defense_arsenal]

Retron was significantly enriched in the accessory and singleton pangenome relative to the background pangenome, with **8.2%** of Retron-associated gene clusters in the core fraction and **65.8%** in the singleton fraction. [^phage_defense_arsenal]

The Retron singleton fraction was **1.5–1.8×** the **37.9%** background singleton fraction, consistent with mobile acquisition of defense loci, although this interpretation is based on pangenome enrichment rather than direct transfer measurements. [^phage_defense_arsenal]

Retron participated in the broader defense-system syndrome pattern, in which **27 of 28** defense-system pairs showed significant positive co-occurrence after **1,000** phylum-stratified column-permutation tests and Benjamini–Hochberg false-discovery-rate correction. [^phage_defense_arsenal]

The specific Retron pairwise results reported as especially strong included BREX × Retron, with **5,021** observed co-occurrences, a null mean of **4,681**, **z = 29.7**, and **OR = 8.6**, and DISARM × Retron, with **4,280** observed co-occurrences, a null mean of **3,844**, **z = 28.4**, and **OR = 5.2**. [^phage_defense_arsenal]

These co-occurrence results support a relationship between Retron presence and coordinated anti-phage defense architecture, linking Retron to [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) and the broader [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md). [^phage_defense_arsenal]

## Detection caveat

Retron detection used the broad RVT_1 Pfam marker **PF00078**, which is a reverse-transcriptase marker rather than a Retron-specific identifier. [^phage_defense_arsenal]

The stringent Retron call required at least one other narrow defense system, making it a defense-context filter rather than a Retron-specificity filter. [^phage_defense_arsenal]

This filtering reduced the candidate set from **15,109** to **15,098** species, dropping **11** species. [^phage_defense_arsenal]

Accordingly, the report recommends interpreting these results as reverse-transcriptase candidates occurring in defense-syndrome contexts, not as characterized Retron systems. [^phage_defense_arsenal]

The detection limitation qualifies the inference that Retron is mobile or forms specific defense syndromes, and it motivates multi-PFam and gene-order validation with PADLOC MacSyFinder-style rules. [^phage_defense_arsenal]

## Cross-document links

The source report is summarized in [phage_defense_arsenal__REPORT](../summaries/phage_defense_arsenal__REPORT.md). [^phage_defense_arsenal]

Retron's accessory- and singleton-enrichment pattern also contributes to [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md). [^phage_defense_arsenal]

[^phage_defense_arsenal]: [phage defense arsenal](../summaries/phage_defense_arsenal__REPORT.md)
