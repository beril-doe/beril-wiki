---
type: Organism
description: Archaeal methanogen represented by Fitness Browser and SNIPE analyses
sources:
- id: snipe_defense_system
  resource: ../summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
- id: truly_dark_genes
  resource: ../summaries/truly_dark_genes__REPORT.md
  title: truly dark genes
- id: conservation_vs_fitness
  resource: ../summaries/conservation_vs_fitness__REPORT.md
  title: conservation vs fitness
title: Methanococcus maripaludis
---
# Methanococcus maripaludis

## What this entity is

**Canonical name:** Methanococcus maripaludis. [^snipe_defense_system]  
**Known alias:** *M. maripaludis*. [^snipe_defense_system]  
**Strains represented:** JJ and S2. [^snipe_defense_system][^conservation_vs_fitness]  
**Stable identifier reported:** SNIPE-associated locus **MMJJ_RS01635**; no organism-level stable identifier was provided in the report. [^snipe_defense_system]

Methanococcus maripaludis is an organism represented in the [Fitness Browser](kescience-fitnessbrowser.md) and the only organism in that dataset reported to contain a complete two-domain [SNIPE](snipe-defense-system.md) architecture. [^snipe_defense_system] The [truly dark genes](../summaries/truly_dark_genes__REPORT.md) analysis further identifies Methanococcus strains S2 and JJ as accounting for **55% of truly dark genes**, and Methanococcus_JJ contributes **13 of the top 100** prioritized candidates. [^truly_dark_genes] This **refines** the organism’s context: its representation in Fitness Browser also makes it a major source of unresolved gene-function candidates, although the dark-gene analysis does not establish their functions. [^truly_dark_genes]

The conservation-versus-fitness analysis **supports** the importance of this Fitness Browser representation: Methanococcus maripaludis S2 showed the strongest essential-gene core-conservation enrichment among the compared organisms, with **OR=5.21**. [^conservation_vs_fitness] This result applies to S2 and therefore **refines** the separate SNIPE evidence from strain JJ rather than identifying the SNIPE locus as the enriched gene set. [^conservation_vs_fitness]

## Evidence from the SNIPE analysis

The SNIPE protein at locus MMJJ_RS01635 contained PF13250/DUF4041, PF13455/Mug113, and PF10544, providing the only complete PF13250-plus-PF13455 architecture detected among the surveyed Fitness Browser organisms. [^snipe_defense_system] The relevant domain families are [PF13250/DUF4041](pf13250-duf4041.md) and [PF13455/Mug113](pf13455-mug113.md). [^snipe_defense_system]

The Fitness Browser provided **129 experiments** for this protein. [^snipe_defense_system] Its minimum measured fitness was **-1.16** under formate/[acetate](acetate.md) conditions, and it was dispensable under most tested conditions. [^snipe_defense_system]

PF13455 occurred in **7 genes across 6 Fitness Browser organisms**, including Methanococcus maripaludis, but only Methanococcus maripaludis carried the complete PF13250-plus-PF13455 architecture. [^snipe_defense_system]

## Interpretation and limitation

The Methanococcus maripaludis result demonstrates that a complete SNIPE-like domain architecture occurs in an archaeal Fitness Browser organism, but it does not establish that the Enterobacterales phage-lambda ManYZ transporter mechanism operates in archaea. [^snipe_defense_system] The concentration of unresolved genes in Methanococcus strains **supports** prioritizing archaeal-specific annotation and experimental follow-up, but the dark-gene results do not by themselves establish horizontal transfer, gene function, or a connection to SNIPE. [^truly_dark_genes]

The S2 conservation signal likewise indicates an association between inferred essentiality and core-genome conservation, not a strain-independent property of every Methanococcus maripaludis gene; essentiality was inferred from RB-TnSeq under the library’s represented growth conditions. [^conservation_vs_fitness]

## Related pages

- [snipe_defense_system__REPORT](../summaries/snipe_defense_system__REPORT.md) — source report describing the SNIPE architecture and Fitness Browser evidence. [^snipe_defense_system]
- [truly_dark_genes__REPORT](../summaries/truly_dark_genes__REPORT.md) — source report distinguishing annotation-lag genes from persistent hypothetical genes and prioritizing candidates. [^truly_dark_genes]
- [conservation_vs_fitness__REPORT](../summaries/conservation_vs_fitness__REPORT.md) — source report linking Fitness Browser essentiality to pangenome conservation. [^conservation_vs_fitness]
- [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md) — cross-project synthesis of SNIPE-mediated phage defense and its proposed transporter trade-off. [^snipe_defense_system]
- [kescience-fitnessbrowser](kescience-fitnessbrowser.md) — dataset supplying the organism’s fitness measurements. [^snipe_defense_system]
- [snipe-defense-system](snipe-defense-system.md) — SNIPE defense system investigated in the report. [^snipe_defense_system]

[^snipe_defense_system]: [snipe defense system](../summaries/snipe_defense_system__REPORT.md)
[^conservation_vs_fitness]: [conservation vs fitness](../summaries/conservation_vs_fitness__REPORT.md)
[^truly_dark_genes]: [truly dark genes](../summaries/truly_dark_genes__REPORT.md)
