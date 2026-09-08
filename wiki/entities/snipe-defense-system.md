---
type: Gene_Or_Pathway
description: Mobile SNIPE phage-defense system with PF13250 and PF13455 domains
sources:
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: snipe_defense_system
  resource: ../summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
title: SNIPE defense system
---
# SNIPE defense system

## Identity

The canonical name is SNIPE defense system, with the alias SNIPE. [^discoveries] SNIPE is a phage-defense system associated with the PF13250/DUF4041 domain and the PF13455 (Mug113) nuclease domain. [^snipe_defense_system] The stable identifier reported for its nuclease domain is Pfam PF13455 (Mug113). [^discoveries] The nuclease domain is PF13455 (Mug113), not PF01541, although both domains belong to the GIY-YIG clan. [^discoveries] The new analysis refines this assignment: PF13455 belongs to the GIY-YIG clan but is distinct from canonical GIY-YIG PF01541, and no surveyed gene cluster contained both PF13250 and PF01541. [^snipe_defense_system]

## Key facts

SNIPE occurred in 4,572 gene clusters across 1,696 species and 33 phyla. [^discoveries] Of these gene clusters, 86.7% were accessory or singleton. [^discoveries] This accessory-plus-singleton distribution supports the interpretation that SNIPE is predominantly mobile and commonly gained or lost rather than stably core-inherited. [^snipe_defense_system]

A full two-domain SNIPE protein with 129 experiments was identified in *Methanococcus maripaludis* JJ. [^discoveries] In the new analysis, its PF13250-plus-PF13455 architecture was the only complete two-domain SNIPE architecture found among Fitness Browser examples; it was dispensable under most tested conditions. [^snipe_defense_system]

The document reports SNIPE alongside phage-infection data from [phagefoundry](phagefoundry.md), whose strain-modelling database contained 17,672 binary infection outcomes from 188 *Escherichia coli* strains and 96 phages. [^discoveries] The associated machine-learning model achieved an AUC of 0.883. [^discoveries] Lambda infected 1/188 strains (0.5%), whereas Myoviridae infected 43.4% of strains. [^discoveries] These results are consistent with SNIPE acting at a phage adsorption/injection interface, but do not establish that mechanism across the surveyed strains. [^snipe_defense_system]

Klebsiella had 1 DUF4041 annotation across 3 proteins and 4,619 PTS_EIIC annotations, making it the only PhageFoundry species with both SNIPE and the ManX-family PTS domain. [^discoveries] The new analysis supports, but does not directly demonstrate, a SNIPE–ManYZ transporter connection: SNIPE is proposed to cleave phage DNA entering through ManYZ while preserving mannose transport, whereas *manY*/*manZ* loss carries transporter costs. [^snipe_defense_system]

## Related research

The SNIPE findings contribute to [environmental-resistome](../concepts/environmental-resistome.md) by documenting the distribution and accessory status of a defense-system gene family. [^discoveries] They also connect defense-system analysis with [phagefoundry](phagefoundry.md) and with the broader gene-content synthesis in [pangenome-integration](../concepts/pangenome-integration.md). [^discoveries] The source document is summarized at [discoveries](../summaries/discoveries.md) and [snipe_defense_system__REPORT](../summaries/snipe_defense_system__REPORT.md). [^snipe_defense_system]

[^discoveries]: [discoveries](../summaries/discoveries.md)
[^snipe_defense_system]: [snipe defense system](../summaries/snipe_defense_system__REPORT.md)
