---
type: "Gene_Or_Pathway"
description: "Leucine biosynthesis pathway, whose community completeness correlated negatively with ambient leucine."
sources: ["summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
aliases: ["leucine"]
---
# Leucine biosynthesis

This page covers leucine biosynthesis, the pathway whose community completeness correlated negatively with ambient leucine. In NMDC, completeness correlated with ambient leucine at Spearman r = −0.390, q (Benjamini-Hochberg, BH) = 0.022, n = 62, and the signal survived false discovery rate (FDR) correction. [src: nmdc_community_metabolic_ecology] The evidence is a single-study correlation, so it is associational. See [[summaries/nmdc_community_metabolic_ecology__REPORT]] for the full analysis.

## Key facts

- Leucine biosynthesis community completeness versus ambient metabolite intensity in NMDC had Spearman r = −0.390, p = 0.002, q (BH) = 0.022, n = 62. [src: nmdc_community_metabolic_ecology]
- In the Soil-only test, leucine stayed FDR-significant (r = −0.390, q = 0.022, n = 62). The result matched the full cohort because all leucine samples were Soil. [src: nmdc_community_metabolic_ecology]
- Leucine and arginine are the two FDR-significant pathways in the NMDC Black Queen analysis. [src: nmdc_community_metabolic_ecology] See [[entities/arginine]] and [[entities/black-queen-hypothesis]].
- In the pan-bacterial GapMind comparison, leucine biosynthesis has all-genes completeness 0.614, core-only completeness 0.468, and gap 0.146. [src: pathway_capability_dependency] See [[summaries/pathway_capability_dependency__REPORT]].

## Interpretation

The report describes leucine synthesis as energetically expensive, at 37 ATP (adenosine triphosphate) equivalents. [src: nmdc_community_metabolic_ecology] It reads the leucine and arginine results as consistent with the Black Queen prediction that costly functions are most likely to be lost when environmental supply is reliable. [src: nmdc_community_metabolic_ecology] This is the report's interpretation, not a direct test. See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]].

For comparison with the literature, the report gives environmental-scale r = −0.33 for leucine and r = −0.30 for arginine. It calls these weaker than, but directionally consistent with, Gowda et al.'s controlled-community finding. [src: nmdc_community_metabolic_ecology]

## Confounding and robustness

Cross-study liquid chromatography-mass spectrometry (LC-MS) protocol heterogeneity is effectively absent as a confounder for leucine. All leucine samples (n = 62) came from one study with consistent analytical methods. [src: nmdc_community_metabolic_ecology] The H1 dataset is effectively single-study, with 95% of H1 samples from nmdc:sty-11-r2h77870. [src: nmdc_community_metabolic_ecology] See [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]].

A compound-mapping bug affected the leucine result. Three isoleucine compounds had been misassigned to leucine. They had near-zero completeness-versus-metabolite correlation and diluted the true leucine signal. [src: nmdc_community_metabolic_ecology] Fixing the bug strengthened the signal from r −0.326 to −0.390 and q from 0.045 to 0.022. [src: nmdc_community_metabolic_ecology] See [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]].
