---
type: "Gene_Or_Pathway"
description: "Mobile SNIPE phage-defense system with PF13250 and PF13455 domains"
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
---
# SNIPE defense system

## Identity

The canonical name is SNIPE defense system, with the alias SNIPE. [src: discoveries] SNIPE is a phage-defense system associated with the PF13250/DUF4041 domain and the PF13455 (Mug113) nuclease domain. [src: snipe_defense_system] The stable identifier reported for its nuclease domain is Pfam PF13455 (Mug113). [src: discoveries] The nuclease domain is PF13455 (Mug113), not PF01541, although both domains belong to the GIY-YIG clan. [src: discoveries] The new analysis refines this assignment: PF13455 belongs to the GIY-YIG clan but is distinct from canonical GIY-YIG PF01541, and no surveyed gene cluster contained both PF13250 and PF01541. [src: snipe_defense_system]

## Key facts

SNIPE occurred in 4,572 gene clusters across 1,696 species and 33 phyla. [src: discoveries] Of these gene clusters, 86.7% were accessory or singleton. [src: discoveries] This accessory-plus-singleton distribution supports the interpretation that SNIPE is predominantly mobile and commonly gained or lost rather than stably core-inherited. [src: snipe_defense_system]

A full two-domain SNIPE protein with 129 experiments was identified in *Methanococcus maripaludis* JJ. [src: discoveries] In the new analysis, its PF13250-plus-PF13455 architecture was the only complete two-domain SNIPE architecture found among Fitness Browser examples; it was dispensable under most tested conditions. [src: snipe_defense_system]

The document reports SNIPE alongside phage-infection data from [[entities/phagefoundry]], whose strain-modelling database contained 17,672 binary infection outcomes from 188 *Escherichia coli* strains and 96 phages. [src: discoveries] The associated machine-learning model achieved an AUC of 0.883. [src: discoveries] Lambda infected 1/188 strains (0.5%), whereas Myoviridae infected 43.4% of strains. [src: discoveries] These results are consistent with SNIPE acting at a phage adsorption/injection interface, but do not establish that mechanism across the surveyed strains. [src: snipe_defense_system]

Klebsiella had 1 DUF4041 annotation across 3 proteins and 4,619 PTS_EIIC annotations, making it the only PhageFoundry species with both SNIPE and the ManX-family PTS domain. [src: discoveries] The new analysis supports, but does not directly demonstrate, a SNIPE–ManYZ transporter connection: SNIPE is proposed to cleave phage DNA entering through ManYZ while preserving mannose transport, whereas *manY*/*manZ* loss carries transporter costs. [src: snipe_defense_system]

## Related research

The SNIPE findings contribute to [[concepts/environmental-resistome]] by documenting the distribution and accessory status of a defense-system gene family. [src: discoveries] They also connect defense-system analysis with [[entities/phagefoundry]] and with the broader gene-content synthesis in [[concepts/pangenome-integration]]. [src: discoveries] The source document is summarized at [[summaries/discoveries]] and [[summaries/snipe_defense_system__REPORT]]. [src: snipe_defense_system]
