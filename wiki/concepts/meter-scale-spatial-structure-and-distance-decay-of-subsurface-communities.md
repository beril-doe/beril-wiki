---
type: "Concept"
description: "Covers distance-decay, directional turnover and well-pair residuals in sediment communities on a small grid; stops at depth effects and functional inference."
sources: ["summaries/discoveries.md", "summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Meter-scale spatial structure and distance-decay of subsurface communities

Sediment communities across a 3×3 grid of nine Subsurface Observatory wells (about 6 m span) show significant distance-decay of similarity. [src: discoveries, enigma_sso_asv_ecology] The signal runs along the east-west axis, not the hillslope. [src: discoveries] A NE→SW corridor of wells is more similar than distance predicts. [src: discoveries, enigma_sso_asv_ecology] The evidence comes from one sampling event at one site, so it is suggestive and not general. [src: enigma_sso_asv_ecology] See [[entities/subsurface-observatory-well-grid]], [[entities/distance-decay]] and [[entities/mantel-test]].

## Literature Context

The two candidate papers address distance-decay of microbial similarity, but at scales and in habitats very different from a roughly 6 m well grid. Both are abstracts only, so what follows rests on their summary statements.

A cave study of 333 weathered rock and sediment samples from karst caves in southwestern China, India, Italy and Mexico reports distance-decay relationships in both habitats. Sediment communities had higher alpha diversity and showed more pronounced compositional shifts with distance from the cave entrance [PMID 42032767](https://pubmed.ncbi.nlm.nih.gov/42032767/). The authors conclude that stochastic processes, especially dispersal limitation, dominate assembly. Ecological drift matters more at local scales and declines at larger ones. They also state that geographic distance matters less than local environmental and habitat-specific controls [PMID 42032767](https://pubmed.ncbi.nlm.nih.gov/42032767/). An ocean study of 153 free-living samples across a frontal zone in the southwest Indian Ocean notes that distance-decay is expected to be weak where dispersal is high. It found communities structured more strongly by depth than by latitude, with OTU turnover across fronts in the sub-surface and intermediate layers. The deep layer was homogeneous across the survey area, and turnover tracked water masses [PMID 28405400](https://pubmed.ncbi.nlm.nih.gov/28405400/).

The corpus finding of significant distance-decay across the nine-well Subsurface Observatory grid (Mantel ρ = 0.323, p = 0.029) is consistent with the cave result that sediment communities show distance-decay in a subsurface setting [PMID 42032767](https://pubmed.ncbi.nlm.nih.gov/42032767/). It also fits the broader view that turnover follows a structuring gradient and not distance alone. The corpus reads the east-west signal as a lateral force, possibly the NE→SW plume corridor. That parallels the ocean finding that turnover follows water masses [PMID 28405400](https://pubmed.ncbi.nlm.nih.gov/28405400/). The parallel is an analogy only, and the corpus's directional result is borderline (column Mantel ρ = 0.227, p = 0.092). The Procrustes match to the physical grid is also a null result at conventional thresholds (p = 0.080). Residuals showing U3, M6 and L7 more similar than distance predicts are consistent with the cave authors' caution that distance is weaker than local environmental controls [PMID 42032767](https://pubmed.ncbi.nlm.nih.gov/42032767/).

The corpus extends this literature by working at meter scale in a contaminated aquifer sediment. Neither candidate paper examines that scale or contamination plumes, so the plume-structuring interpretation is novel here and untested by these papers. The corpus is also limited to one sampling event at one site, whereas the cave dataset spans four countries. Its assembly inference (dispersal limitation versus drift) has no counterpart in the corpus, which did not test assembly processes. Nothing in the candidates contradicts the corpus findings.

See [[entities/distance-decay]] and [[entities/mantel-test]].

## Distance-decay across the grid

The grid shows significant distance-decay of community similarity (Mantel ρ = 0.323, p = 0.029, 9,999 permutations). [src: discoveries, enigma_sso_asv_ecology] The analysis used 9 wells, 23,458 ASVs (amplicon sequence variants) and 37 sediment core samples aggregated per well. [src: enigma_sso_asv_ecology] Mean Bray-Curtis (BC) dissimilarity was 0.747. It ranged from 0.558 for U3–M6, the most similar pair, to 0.872 for U3–L9, the most dissimilar. [src: enigma_sso_asv_ecology] NMDS ordination reached low stress (0.067). [src: enigma_sso_asv_ecology] Procrustes analysis showed only marginal correspondence between the ordination and the physical grid (m² = 0.379, p = 0.080), so this is a null result at conventional thresholds. [src: enigma_sso_asv_ecology]

The report calls meter-scale turnover noteworthy. It argues that the SSO shows contamination plumes can structure communities at sub-decameter resolution. [src: enigma_sso_asv_ecology] This is the report's interpretation, not a tested result.

## Directional turnover

Turnover is not aligned with the hillslope (uphill-downhill Mantel ρ = −0.049, p = 0.580). [src: enigma_sso_asv_ecology] It aligns more with the east-west axis (column Mantel ρ = 0.227, p = 0.092). [src: enigma_sso_asv_ecology] The east-west value does not reach p < 0.05. The report reads this as pointing to a lateral structuring force, not topography-driven hydrology. [src: enigma_sso_asv_ecology]

## Well-pair residuals

Wells U3, M6 and L7 are far more similar to each other than their geographic distances predict. [src: enigma_sso_asv_ecology] They form a diagonal corridor along the NE→SW plume flow path. [src: discoveries] These three pairs had the three most negative residuals. [src: enigma_sso_asv_ecology] U3–M6 has BC = 0.558 and residual = −0.170, and is the most similar pair in the grid. [src: enigma_sso_asv_ecology] M6–L7 has BC = 0.615 and residual = −0.154. [src: enigma_sso_asv_ecology] U3–L7 has BC = 0.646 and residual = −0.133. [src: enigma_sso_asv_ecology]

At the other extreme, U3–M4 and U3–L9 had the most positive residuals, so they are more different than expected. [src: enigma_sso_asv_ecology] The report gives two answers for the most dissimilar pair. One passage calls U3–M4 the largest dissimilarity (BC = 0.871, residual = +0.105), spanning the plume entry point to the well farthest from the plume core. [src: enigma_sso_asv_ecology] Another identifies U3–L9 as the most dissimilar pair (BC = 0.872). [src: enigma_sso_asv_ecology] The two values differ by 0.001 and the report does not reconcile them. See [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]] for the plume link.

## Tensions

- One passage of the report names U3–M4 as the largest dissimilarity, at BC = 0.871. [src: enigma_sso_asv_ecology] Another names U3–L9 as the most dissimilar pair, at BC = 0.872. [src: enigma_sso_asv_ecology]

## Limits

Sediment was sampled at a single timepoint. Temporal plume dynamics and community responses therefore cannot be assessed. [src: enigma_sso_asv_ecology] See [[concepts/temporal-stability-of-groundwater-communities]] for the temporal context.

## Open Directions

- Resample the grid at several times to test whether the east-west axis and the U3-M6-L7 corridor persist. This would close the single-timepoint gap.
- Link the residuals to measured plume geochemistry at each well. This would test whether the corridor tracks the flow path.
- Add wells along the east-west axis, or use a denser grid, to see whether the borderline directional Mantel result (p = 0.092) strengthens.
- Recompute the full pairwise Bray-Curtis matrix to settle whether U3–M4 or U3–L9 is the most dissimilar pair.
- Repeat the analysis at larger spacings to compare meter-scale decay with kilometer-scale studies.
