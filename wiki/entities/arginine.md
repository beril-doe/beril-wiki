---
type: "Compound"
description: "Amino acid with four-way database concordance and 270 fitness genes in FW300-N2E3, also appearing in community metabolic ecology."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["L-arginine", "arginine"]
---
# Arginine

This page covers the amino acid arginine (L-arginine). In FW300-N2E3 it has 270 fitness genes and agrees across four databases. [src: fw300_metabolic_consistency] It also shows a significant negative association in a community-scale metabolic ecology analysis of NMDC data. [src: nmdc_community_metabolic_ecology] The strain evidence comes from database comparisons, including a computationally complete GapMind pathway, and the community result is a cross-sample correlation. [src: fw300_metabolic_consistency, nmdc_community_metabolic_ecology]

## Key facts

- Arginine is among the most genetically complex metabolisms in FW300-N2E3, with 270 genes. [src: fw300_metabolic_consistency]
- The pan-bacterial GapMind comparison gives arginine biosynthesis (arg) all-genes completeness 0.613, core-only completeness 0.472 and gap 0.141. [src: pathway_capability_dependency]

## Cross-database concordance in FW300-N2E3

Arginine agrees across all four databases for this strain. It was Increased in Web of Microbes (WoM) data, supported growth in the Fitness Browser (270 genes), was utilized in BacDive (40/48, 83%), and had a complete GapMind pathway. [src: fw300_metabolic_consistency] The report calls malate, arginine and valine the gold standard of cross-database consistency. The organism produces and grows on them, the species utilizes them, and their pathways are computationally complete. [src: fw300_metabolic_consistency] The WoM arginine entry (action I) maps to the Fitness Browser condition L-Arginine as nitrogen source. [src: webofmicrobes_explorer] See [[concepts/cross-database-concordance-of-metabolite-evidence]] and [[entities/malate]].

## Community metabolic ecology (NMDC)

Arginine is one of two pathways, with leucine, that are significant after false discovery rate (FDR) correction in the NMDC Black Queen analysis. [src: nmdc_community_metabolic_ecology] Arginine biosynthesis community completeness correlated negatively with ambient metabolite intensity. Spearman r was −0.297, p = 0.007, q (Benjamini-Hochberg, BH) = 0.049, n = 80. [src: nmdc_community_metabolic_ecology] The report describes arginine synthesis as energetically expensive, at 26 ATP (adenosine triphosphate) equivalents. [src: nmdc_community_metabolic_ecology] See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]] and [[entities/leucine-biosynthesis]].

The report also gives environmental-scale values of r = −0.33 for leucine and r = −0.30 for arginine. It calls these weaker than, but directionally consistent with, the controlled-community finding of Gowda et al. [src: nmdc_community_metabolic_ecology]

### Robustness and limits

The result is less robust in the Soil-only test. There arginine lost FDR significance (r = −0.264, q = 0.117, n = 78) but stayed directionally consistent. [src: nmdc_community_metabolic_ecology] Excluding the 6-sample second study gave r = −0.264, p = 0.019 (n = 78). The report reads this as showing that the signal was not driven by the minor study. [src: nmdc_community_metabolic_ecology] See [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]].
