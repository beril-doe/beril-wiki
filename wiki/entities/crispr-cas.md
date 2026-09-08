---
type: Gene_Or_Pathway
description: CRISPR-Cas microbial defense-system gene category and anti-phage defense
  system
sources:
- id: gene_function_ecological_agora
  resource: ../summaries/gene_function_ecological_agora__REPORT.md
  title: gene function ecological agora
- id: phage_defense_arsenal
  resource: ../summaries/phage_defense_arsenal__REPORT.md
  title: phage defense arsenal
title: CRISPR-Cas
---
# CRISPR-Cas

## What this entity is

CRISPR-Cas is a microbial defense-system gene category associated with clustered regularly interspaced short palindromic repeats and CRISPR-associated proteins. [^gene_function_ecological_agora]

- **Canonical name:** CRISPR-Cas. [^gene_function_ecological_agora]
- **Known aliases:** No additional aliases were reported in the source project. [^gene_function_ecological_agora]
- **Stable external identifier:** No stable external identifier was reported in the source project. [^gene_function_ecological_agora]

## Acquisition and defense-arsenal evidence

CRISPR-Cas showed the strongest recent-to-ancient acquisition-depth contrast among the function classes reported in the atlas, with 58.7% of Sankoff gain events classified as recent and 2.4% classified as ancient. [^gene_function_ecological_agora] The resulting recent-to-ancient acquisition ratio for CRISPR-Cas was 24.5×. [^gene_function_ecological_agora] These acquisition-depth results support using [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) to compare the evolutionary-age signatures of defense, regulatory, metabolic, and housekeeping functions. [^gene_function_ecological_agora]

The CRISPR-Cas acquisition signature is also relevant to [environmental-resistome](../concepts/environmental-resistome.md), where recent gene acquisition is used as a comparative signal across mobile and defense-associated functions. [^gene_function_ecological_agora] In the pan-bacterial defense analysis, CRISPR-Cas was detected in 96.1% of species-level pangenomes, the highest reported prevalence among seven defense-system families. [^phage_defense_arsenal] This **refines** the acquisition-depth result by showing that a broadly distributed defense category can also carry a strong recent-acquisition signature. [^phage_defense_arsenal]

The reported 96% prevalence is method-dependent: EggNOG description matching gave 96%, whereas the specific Cas1 Pfam marker PF01867 gave approximately 55% on the same pangenome, a difference of approximately 40 percentage points. [^phage_defense_arsenal] Thus, the new analysis **qualifies** cross-study comparisons of CRISPR-Cas prevalence, treating 96% as an upper bound rather than an unambiguous system-specific estimate. [^phage_defense_arsenal]

CRISPR-Cas had 27.4% core and 47.2% singleton gene-cluster fractions in the defense pangenome analysis, compared with a background of 46.8% core and 37.9% singleton clusters. [^phage_defense_arsenal] This **supports** the existing interpretation of defense-associated functions as acquisition-relevant while indicating a weaker accessory-enrichment pattern for CRISPR-Cas than for several other systems. [^phage_defense_arsenal] CRISPR-Cas × CBASS was the only one of 28 defense-system pairs without significant positive co-occurrence, with z = 0.21 and p_emp = 0.98. [^phage_defense_arsenal]

The project’s CRISPR-Cas result was generated within a GTDB-r214 atlas containing 18,989 species representatives and 17,073,194 Sankoff-parsimony gain events assigned to recipient-rank depth bins. [^gene_function_ecological_agora]

## Source

The detailed acquisition-depth evidence is summarized in [gene_function_ecological_agora__REPORT](../summaries/gene_function_ecological_agora__REPORT.md). [^gene_function_ecological_agora] The pan-bacterial prevalence, detection-method comparison, and defense-syndrome evidence are summarized in [phage_defense_arsenal__REPORT](../summaries/phage_defense_arsenal__REPORT.md). [^phage_defense_arsenal]

[^gene_function_ecological_agora]: [gene function ecological agora](../summaries/gene_function_ecological_agora__REPORT.md)
[^phage_defense_arsenal]: [phage defense arsenal](../summaries/phage_defense_arsenal__REPORT.md)
