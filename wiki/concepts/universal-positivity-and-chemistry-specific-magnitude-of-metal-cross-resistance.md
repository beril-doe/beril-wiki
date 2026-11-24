---
type: "Concept"
description: "Whether gene-level fitness effects of different metals correlate across bacteria, how strongly by metal pair, and how conserved this is across organisms; stops at gene-tier and pangenome questions."
sources: ["summaries/metal_cross_resistance__REPORT.md"]
---
# Universal positivity and chemistry-specific magnitude of metal cross-resistance

This page covers whether gene-level fitness effects of different metals correlate across bacteria, how strongly by metal pair, and how conserved the pattern is across organisms. All evidence comes from one report, [[summaries/metal_cross_resistance__REPORT]]. It finds that direction is universal (nearly all correlations positive) and magnitude varies by metal pair and is only moderately conserved across organisms. [src: metal_cross_resistance]

## Universal positivity

Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), 98.1% of gene-level fitness correlations were positive (311/317). [src: metal_cross_resistance] In the same data, 99.1% of correlations were statistically significant (p < 0.05). [src: metal_cross_resistance] All 15 metal pairs tested in at least 5 organisms showed >90% sign consistency. [src: metal_cross_resistance] The report finds no metal pair with systematic negative cross-resistance in any organism. [src: metal_cross_resistance] It calls universal positivity the dominant signal. [src: metal_cross_resistance]

The report interprets this as shared tolerance machinery. All metals disrupt protein stability, DNA (deoxyribonucleic acid) integrity, membrane function and cofactor insertion, and the repair machinery is shared. [src: metal_cross_resistance] This is an interpretation, not a tested result. The report cannot tell universal cross-resistance from general stress caused by all metals, because it has no non-metal stress controls. The counter_ion_effects project partly addresses this. [src: metal_cross_resistance]

The metal-label permutation test was non-significant (p = 0.42). [src: metal_cross_resistance] The report explains that all metal pairs are positive, so shuffling labels does not change the mean. [src: metal_cross_resistance] It reads this as showing that the signal lies in universal positivity, not in specific metal-pair identities. [src: metal_cross_resistance]

## Chemistry-specific magnitude

The report proposes a second, chemistry-specific layer. The degree of cross-resistance varies by metal pair and is strongest for divalent cations that compete for the same binding sites (Co, Ni, Zn). It is weakest for metals with unique toxicity mechanisms (Al, Mo). [src: metal_cross_resistance]

Cobalt-nickel was the strongest pair by median r (≈ 0.58) across 28 organisms spanning Proteobacteria, Bacteroidetes, Firmicutes and Actinobacteria. [src: metal_cross_resistance] Aluminum-cobalt and aluminum-nickel were the weakest by median r (≈ 0.30), consistent with aluminum's distinct toxicity mechanism. [src: metal_cross_resistance] Individual organism heatmaps showed positive cross-resistance throughout, with the Ni-Co/Co-Zn block consistently among the strongest. [src: metal_cross_resistance]

The report's consensus matrix gives mean Pearson r, number of organisms and sign consistency per pair:

| Pair | Mean r | Organisms | Sign consistency |
|---|---|---|---|
| Fe-Zn | 0.61 | 6 | 100% [src: metal_cross_resistance] |
| Co-Ni | 0.56 | 28 | 100% [src: metal_cross_resistance] |
| Co-Zn | 0.52 | 18 | 100% [src: metal_cross_resistance] |
| Ni-Zn | 0.51 | 18 | 100% [src: metal_cross_resistance] |
| Cu-Zn | 0.48 | 16 | 100% [src: metal_cross_resistance] |
| Cu-Fe | 0.45 | 7 | 100% [src: metal_cross_resistance] |
| Co-Fe | 0.45 | 7 | 100% [src: metal_cross_resistance] |
| Al-Zn | 0.44 | 13 | 100% [src: metal_cross_resistance] |
| Co-Cu | 0.43 | 24 | 96% [src: metal_cross_resistance] |
| Cu-Ni | 0.43 | 24 | 96% [src: metal_cross_resistance] |
| Al-Fe | 0.38 | 5 | 100% [src: metal_cross_resistance] |
| Fe-Ni | 0.38 | 7 | 100% [src: metal_cross_resistance] |
| Al-Cu | 0.34 | 17 | 94% [src: metal_cross_resistance] |
| Al-Ni | 0.34 | 20 | 95% [src: metal_cross_resistance] |
| Al-Co | 0.30 | 20 | 95% [src: metal_cross_resistance] |

Several pairs carry specific remarks in the report.
- Ni-Co (r = 0.56, n = 28 organisms) is the classic divalent cation pair, which the report says is now validated at gene resolution across diverse phyla. [src: metal_cross_resistance] Nies (1999, 2003) described Co-Ni-Zn cross-resistance mediated by CzcCBA efflux systems. [src: metal_cross_resistance] The report says its data show the entire genome responds similarly to Co and Ni, not just efflux genes. [src: metal_cross_resistance]
- Fe-Zn (r = 0.61, n = 6) was unexpectedly strong. The report suggests this likely reflects shared disruption of iron-sulfur cluster proteins. [src: metal_cross_resistance]
- Cu-U had r = 0.51 (n = 5), and the report states both cause membrane/oxidative damage. [src: metal_cross_resistance]
- Aluminum was the most independent metal in the consensus (mean r = 0.34), which the report ties to its unique trivalent toxicity mechanism. [src: metal_cross_resistance] In [[entities/desulfovibrio-vulgaris-hildenborough]], the richest single-organism view with 13 metals, Mo stood out as the most independent metal. [src: metal_cross_resistance]
- The report says the metal-metal correlations across 28 organisms reproduce the mechanistic grouping found in the counter_ion_effects project. [src: metal_cross_resistance]

## Conservation across organisms

Magnitude is moderately conserved. Leave-one-out consensus prediction gave mean r = 0.41, and Mantel tests across 351 organism pairs gave mean r = 0.23 with 62% positive. [src: metal_cross_resistance] See [[entities/mantel-test]]. The report calls this moderate but consistent conservation of cross-resistance architecture. [src: metal_cross_resistance] It also describes the chemistry-specific layer as moderately conserved (LOO r = 0.41). [src: metal_cross_resistance] Pairwise Spearman correlations of pair rankings, on the 10 common metal pairs across 12 organisms with ≥5 metals, were mostly positive, so organisms rank metal pairs similarly. [src: metal_cross_resistance]

The report says a universal map is a useful predictor of individual organism patterns (mean r = 0.41). [src: metal_cross_resistance] Only 2/28 organisms reached individual significance, so individual organisms deviate meaningfully from the average trend. [src: metal_cross_resistance]

## Novelty claims

The report presents this as the first gene-resolution cross-resistance analysis. It contrasts it with binary resistant/sensitive MIC work. [src: metal_cross_resistance] It says prior MIC studies used 1-5 model organisms. Its own analysis covers 28 organisms and 13 metals, which the report calls a 100× increase in resolution and 5× in taxonomic breadth. [src: metal_cross_resistance] These are the report's own claims.

## Tensions

- Direction versus magnitude: nearly all correlations are positive and significant. [src: metal_cross_resistance] Yet cross-organism agreement on magnitude is only moderate (Mantel mean r = 0.23, 62% positive), and only 2/28 organisms individually reach significance against the consensus. [src: metal_cross_resistance]

## Caveats

- Different experiments used different metal concentrations, so dose-response effects could influence the estimates. [src: metal_cross_resistance]
- Organisms range from 3 to 112 metal experiments, which affects the reliability of per-organism matrices. [src: metal_cross_resistance]
- The 28 organisms are not phylogenetically independent. The report says formal methods such as PGLS (phylogenetic generalized least squares) or independent contrasts would strengthen the conservation claim. [src: metal_cross_resistance] See [[entities/phylogenetic-generalized-least-squares]].
- With no non-metal stress controls, general stress cannot be excluded as the cause of universal positivity. [src: metal_cross_resistance]

## Open Directions

- Fit PGLS or independent-contrast models to the pair-by-organism correlations. This would test whether the moderate conservation (Mantel r = 0.23) survives phylogenetic non-independence.
- Add non-metal stress conditions (for example osmotic or oxidative) from the same organisms. This would separate universal metal cross-resistance from general stress response. See [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].
- Model concentration as a covariate, or restrict to matched doses. This would test the dose-response caveat.
- Subsample organisms to equal experiment counts. This would show whether the 3-to-112 range drives per-organism deviations from the consensus.
- Test whether the iron-sulfur cluster explanation for Fe-Zn holds. Compare iron-sulfur biogenesis gene fitness in the six organisms with the pair. See also [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses]].
