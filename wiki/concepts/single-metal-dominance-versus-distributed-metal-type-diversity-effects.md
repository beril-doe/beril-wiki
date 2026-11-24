---
type: "Concept"
description: "Whether a metal-diversity association is driven by one metal, by within-genus outlier species, or is spread across metal types; covers leave-one-metal-out and within-genus variance tests."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Single-metal dominance versus distributed metal-type diversity effects

This page asks whether a metal-diversity association with niche breadth is driven by one metal, by a few outlier species within genera, or is spread across metal types. Two reports bear on it. In the MicrobeAtlas genus-level analysis, no single-metal exclusion keeps significance, but every exclusion keeps a positive sign, and the report reads this as a distributed effect. [src: microbeatlas_metal_ecology] In the global MGnify MAG (metagenome assembled genomes) analysis, all nine metal-specific gene sets show significant negative associations. [src: comprehensive_metal_ecology] The report itself says the MicrobeAtlas data cannot fully separate a distributed signal from a near-threshold result that lost power. [src: microbeatlas_metal_ecology]

## Literature Context

The one candidate paper is only indirectly relevant. It is a survey of aluminum-tolerant bacterial communities in rice paddy soils, with soil pH from 3.6 to 8.7 [PMID 35166564](https://pubmed.ncbi.nlm.nih.gov/35166564/). The abstract reports that soluble Al3+ increased significantly in acidic soil with pH <5.1. Acidic soils held abundant and diverse Al-tolerant microorganisms, including Clostridium, Bacillus, Paenibacillus, Desulfitobacterium and Desulfosporosinus. Their association network was more complex than in neutral and alkaline soils [PMID 35166564](https://pubmed.ncbi.nlm.nih.gov/35166564/).

The paper also says that the influential taxa in the network had a broader niche and contained more antioxidant functional genes to resist Al stress [PMID 35166564](https://pubmed.ncbi.nlm.nih.gov/35166564/). This is a statement about network-influential taxa. It is not a general finding that all taxa carrying Al resistance genes have broader niches. The evidence available here is the abstract only, and it gives no test of niche breadth against metal-gene content across lineages.

The paper does not test the question on this hub page, which is whether a metal-diversity association is driven by one metal, by within-genus outlier species, or is spread across metal types. It has no leave-one-metal-out analysis, no within-genus variance test and no phylogenetic regression. It studies one metal, aluminum, in one habitat type, so it cannot speak to a distributed effect across metals.

The corpus findings therefore extend the literature rather than conflict with it. The MicrobeAtlas genus-level analysis found no leave-one-out model significant, with every p > 0.10, but every model kept a positive coefficient. The report reads this as a distributed effect and also concedes that it cannot exclude a near-threshold result that lost power. The MAG analysis found all nine metal-specific gene sets negatively associated with niche breadth after FDR correction. The paddy-soil paper is loosely compatible with the general idea that metal-linked genes relate to niche breadth. It adds an aluminum-specific, pH-dependent context, and the Al-gene sets in the MAG analysis are a possible bridge to it. It does not support or weaken the distributed-effect reading. The corpus claims about single-metal dominance, within-genus outliers and uniformity across metals have no direct counterpart in the candidate evidence, so they remain novel within this evidence set.

## Leave-one-metal-out in genus-level PGLS

The original genus-level PGLS (phylogenetic generalized least squares) with all 7 metals gave β = +0.0215, SE (standard error) = 0.0056, p = 1.5×10⁻⁴. [src: microbeatlas_metal_ecology] The report recomputed species-level metal type counts without each of 7 metals (Hg, As, Cu, Zn, Cd, Cr, Ni), aggregated them to genus and reran PGLS. [src: microbeatlas_metal_ecology] None of the 7 models kept significance, and all had p > 0.10. [src: microbeatlas_metal_ecology] All 7 kept a positive β. [src: microbeatlas_metal_ecology]

| Metal excluded | β | SE | p |
|---|---|---|---|
| Hg | +0.0082 | 0.0069 | 0.233 [src: microbeatlas_metal_ecology] |
| As | +0.0039 | 0.0061 | 0.518 [src: microbeatlas_metal_ecology] |
| Cu | +0.0102 | 0.0065 | 0.115 [src: microbeatlas_metal_ecology] |
| Zn | +0.0095 | 0.0064 | 0.140 [src: microbeatlas_metal_ecology] |
| Cd | +0.0084 | 0.0064 | 0.186 [src: microbeatlas_metal_ecology] |
| Cr | +0.0088 | 0.0064 | 0.173 [src: microbeatlas_metal_ecology] |
| Ni | +0.0095 | 0.0064 | 0.140 [src: microbeatlas_metal_ecology] |

The same S1 models, run on 606 genera, were also not significant after BH-FDR (Benjamini-Hochberg false discovery rate) adjustment. Their q values were: Hg 0.313 [src: microbeatlas_metal_ecology], As 0.572 [src: microbeatlas_metal_ecology], Cu 0.187 [src: microbeatlas_metal_ecology], Zn 0.212 [src: microbeatlas_metal_ecology], Cd 0.258 [src: microbeatlas_metal_ecology], Cr 0.255 [src: microbeatlas_metal_ecology] and Ni 0.212. [src: microbeatlas_metal_ecology]

The report concludes the effect is distributed across the metal type diversity spectrum, not driven by one dominant metal. [src: microbeatlas_metal_ecology] It also says that even if one metal category had elevated false positives, the result needs contributions from several types. [src: microbeatlas_metal_ecology]

### Limit on that reading

The report calls the loss of significance expected. Each exclusion cuts the maximum diversity score from 7 to 6, which compresses predictor variance and costs power. [src: microbeatlas_metal_ecology] Two readings fit the data: a truly distributed signal, or a near-threshold original result pushed below it. The consistently positive β favours the first reading. The report says the two cannot be separated without a larger metal type vocabulary. [src: microbeatlas_metal_ecology]

The "other" category (17% of annotated clusters) was kept in the analysis. It captures metal-associated genes outside the 7 primary types and may include weaker hits. [src: microbeatlas_metal_ecology] Excluding it would leave the 6 metals Hg, As, Cu, Zn, Cd, Cr and Ni. [src: microbeatlas_metal_ecology] Whether that exclusion changes the result is not reported in these claims.

## Within-genus outlier species

Within-genus variance does not explain the association. The report computed the within-genus SD (standard deviation) of n_metal_types across species, z-scored it and added it to the main PGLS. [src: microbeatlas_metal_ecology] With that covariate, z-scored mean metal types stayed associated with niche breadth (β = +0.0189, SE = 0.0060, p = 0.0016). [src: microbeatlas_metal_ecology] The result was significant after BH-FDR (q = 0.007) in 606 genera. [src: microbeatlas_metal_ecology] The SD term itself was not significant (β = +0.0074, SE = 0.0055, p = 0.181). [src: microbeatlas_metal_ecology] The report concludes that a few outlier species are not pushing genera into the high-diversity category in a way that inflates the association. [src: microbeatlas_metal_ecology] It also says this confirms genus aggregation does not hide a species-level confound. [src: microbeatlas_metal_ecology]

## Uniform effect across metals in MAGs

A separate dataset shows the same pattern. The report says the metal-gene niche-breadth effect is uniform across 9 chemically diverse metals, all FDR-significant. [src: comprehensive_metal_ecology] In the bacterial global MGnify MAG analysis, each metal-specific set of KOs (KEGG orthologs) had a negative association with niche breadth:

| Metal | KOs | β | BH-FDR p |
|---|---|---|---|
| Tl | 45 | −0.027 | 1.1×10⁻⁸ [src: comprehensive_metal_ecology] |
| Fe | 98 | −0.025 | 1.2×10⁻⁷ [src: comprehensive_metal_ecology] |
| Ni | 84 | −0.025 | 1.9×10⁻⁷ [src: comprehensive_metal_ecology] |
| Zn | 67 | −0.023 | 1.1×10⁻⁶ [src: comprehensive_metal_ecology] |
| Al | 34 | −0.023 | 8.8×10⁻⁶ [src: comprehensive_metal_ecology] |
| Co | 101 | −0.022 | 3.9×10⁻⁶ [src: comprehensive_metal_ecology] |
| S | 74 | −0.021 | 4.9×10⁻⁵ [src: comprehensive_metal_ecology] |
| Cu | 71 | −0.019 | 7.7×10⁻⁵ [src: comprehensive_metal_ecology] |
| Mn | 34 | −0.017 | 3.8×10⁻⁴ [src: comprehensive_metal_ecology] |

The report argues that this uniformity argues against any single element driving the signal. [src: comprehensive_metal_ecology] The sign here is negative, and the MicrobeAtlas metric is metal type diversity with a positive sign. The two analyses use different data, different metals and different predictors, so their coefficients should not be compared directly.

## Tensions

- Leave-one-out models lose significance, which could mean a distributed signal [src: microbeatlas_metal_ecology] or a near-threshold result weakened by lost power. [src: microbeatlas_metal_ecology]
- The MAG analysis finds every metal-specific set significant [src: comprehensive_metal_ecology], while no MicrobeAtlas leave-one-out model is. [src: microbeatlas_metal_ecology] These tests ask different questions, so the contrast is not a conflict in the same measure.

## Open Directions

- Rerun the leave-one-out test with a larger metal vocabulary, or with a power-matched design that drops a random category of equal size. This would show whether the loss of significance reflects the 7-to-6 range compression or a real contribution from each metal.
- Run a leave-one-out analysis on the MAG metal-specific sets, dropping each metal's KOs from a pooled score. This would check whether the uniform signal holds in a combined index as well as in separate sets.
- Test the "other" category directly by excluding it, which gives the 6-metal analysis, and compare it with the original. This would show whether weaker annotation hits shape the result.
- See [[concepts/validity-of-curated-metal-gene-annotation]] and [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]] for related annotation and gene-class questions that these tests could be combined with.
