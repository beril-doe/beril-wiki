---
type: "Compound"
description: "Tyrosine, an amino acid whose community biosynthesis completeness in NMDC metagenomes was an outlier both in Black Queen Hypothesis tests and in ecosystem-type differentiation."
sources: ["summaries/discoveries.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
# Tyrosine

Tyrosine (`tyr` in the pathway-completeness tables) appears in this corpus mainly as one of the amino-acid biosynthesis pathways scored for community completeness in NMDC metagenomes. It is an outlier in two separate analyses of that data [src: nmdc_community_metabolic_ecology]. See also [[entities/aromatic-amino-acid-biosynthesis]] and [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Black Queen Hypothesis tests

The report tested the Black Queen Hypothesis (BQH) by correlating community pathway completeness with ambient amino-acid metabolite intensity. Under the BQH, that correlation should be negative [src: nmdc_community_metabolic_ecology]. Tyrosine was the outlier in the opposite (anti-BQH) direction: r = +0.419 with n = 26, a nominal p = 0.033 and q = 0.117. It was therefore not significant after Benjamini–Hochberg FDR correction (false discovery rate), and the report labels it "ns" [src: nmdc_community_metabolic_ecology]. This positive association conflicts with the predicted direction, and the report treats it as an outlier rather than discarding it [src: nmdc_community_metabolic_ecology]. By contrast, [[entities/isoleucine]] biosynthesis (r = −0.057, n = 18, q = 0.823) could be tested as the 13th pathway but showed no BQH signal at this sample size [src: nmdc_community_metabolic_ecology]. Related pages: [[concepts/community-metabolic-interdependence]] and [[concepts/null-results-under-limited-statistical-resolution]].

The central discoveries digest gives the same outlier as r = +0.42 (ns) and calls it an anti-BQH outlier [src: discoveries]. The project report gives r = +0.419 for this correlation [src: nmdc_community_metabolic_ecology]. Each figure is recorded here as its source states it.

## Proposed explanation (hypothesis, not tested)

The report says the tyrosine outlier (r = +0.42) "merits caution". Tyrosine can be made from phenylalanine by non-biosynthetic hydroxylation. Communities with high phenylalanine biosynthesis completeness could therefore still supply tyrosine, and the `tyr` completeness score does not capture that route. This would decouple biosynthesis from pool size [src: nmdc_community_metabolic_ecology]. The discoveries digest calls this explanation "likely" [src: discoveries]. The report only says the outlier "may" reflect alternative tyrosine sources, and neither source tests the idea directly [src: nmdc_community_metabolic_ecology]. It remains a hypothesis: phenylalanine hydroxylation may make the tyrosine completeness score a poor proxy for tyrosine supply [src: discoveries, nmdc_community_metabolic_ecology].

## Ecosystem-type differentiation

The report ran a separate [[entities/kruskal-wallis-test]] on each pathway, corrected with [[entities/benjamini-hochberg-fdr]] (BH-FDR). It found that 17 of 18 amino-acid pathways differed significantly in community completeness across ecosystem types (q < 0.05). The largest differences were in the biosynthesis of [[entities/glycine]] (H = 92.98, q = 1.2×10⁻¹⁹), [[entities/asparagine]] (H = 66.19, q = 3.8×10⁻¹⁴) and cysteine (H = 62.66, q = 1.5×10⁻¹³). Tyrosine was the only pathway without a significant difference (q = 0.71) [src: nmdc_community_metabolic_ecology]. This makes tyrosine the exception to the habitat structuring described in [[concepts/habitat-structured-community-metabolic-potential]] [src: nmdc_community_metabolic_ecology].
