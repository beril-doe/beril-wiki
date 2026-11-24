---
type: "Concept"
description: "Covers how vadose versus saturated zones structure community composition relative to well identity; stops at functional process inference."
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Depth and hydrogeological zonation of subsurface microbial communities

In the SSO samples of the enigma_sso_asv_ecology report, hydrogeological zone explains significant community variance and well identity does not. [src: enigma_sso_asv_ecology] The evidence is one dataset of 37 sediment core segments, tested with [[entities/permanova]] (permutational multivariate analysis of variance) and Spearman correlations of phylum abundance with depth. [src: enigma_sso_asv_ecology] The plume explanation for the pattern is the report's interpretation, and the cited claims describe it as an explanation, not as a tested result. [src: enigma_sso_asv_ecology] See also [[summaries/enigma_sso_asv_ecology__REPORT]] and [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

## Literature Context

The candidate papers come from consolidated rock and thermal aquifer settings, not sediment cores, so they bear on the hub's question only by analogy. They suggest that depth, water saturation and hydrology can structure subsurface communities, but that depth alone is not always the dominant control.

In twenty-two shallow limestone-mudstone rock cores, 16S rRNA gene analysis showed a rock matrix microbiome distinct from the surrounding groundwater. Shallow weathered limestones contained bacterial groups most likely originating from soil habitats. Neither depth, matrix permeability nor major mineralogy dominantly controlled endolithic diversity. The authors point instead to a combination of factors that supply niches through fluids, matter and energy, and that govern dispersal [PMID 31078773](https://pubmed.ncbi.nlm.nih.gov/31078773/). A metagenomic study of seven rock specimens from the vadose zone, fractured aquifers and deep aquitards found DNA damage patterns, which the authors read as paleome signatures, in three specimens, all from the vadose zone. DNA from deep aquitards isolated from surface input showed no decay. The authors infer that water saturation, not flow, controls subsurface microbial survival [PMID 37749660](https://pubmed.ncbi.nlm.nih.gov/37749660/). In the Lavey-les-Bains thermal system, microbial communities varied significantly with depth (200 m versus 500 m) but showed minimal seasonal change, even though shallow groundwater mixed seasonally with deep groundwater. The authors propose that intrinsic properties such as temperature matter more than hydrological change [PMID 40478876](https://pubmed.ncbi.nlm.nih.gov/40478876/).

The corpus finding that hydrogeological zone explains 27.5% of community variance (F = 4.05, p = 0.0001) in 37 sediment core segments is broadly consistent with the saturation-linked and depth-dependent structure in the thermal aquifer and the vadose-zone paleome work [PMID 40478876](https://pubmed.ncbi.nlm.nih.gov/40478876/) [PMID 37749660](https://pubmed.ncbi.nlm.nih.gov/37749660/). The vadose versus saturated contrast is particularly in line with the saturation argument. Those studies do not test contaminant plumes, and they use different habitats (rock matrix and a thermal system), so the agreement is qualitative.

The rock-core study reports that depth did not dominantly control endolithic communities [PMID 31078773](https://pubmed.ncbi.nlm.nih.gov/31078773/). That sits in partial tension with the corpus's depth-zone dominance. The habitats differ, since consolidated rock matrix is not unconsolidated sediment. The tension suggests that zone effects depend on the setting and on factors other than depth.

The corpus's plume explanation, that depth controls whether a sample intersects the plume, has no counterpart in these papers and remains the report's untested interpretation. The same applies to the well-identity null result (19.2%, p = 0.979), which these papers do not address. The corpus's phylum-level depth trends are likewise not compared here and still rest on one dataset.

## Zone versus well identity

Zone explains significant community variance and well identity does not. [src: enigma_sso_asv_ecology]

- The 37 samples were classified by depth and description into VZ (33), VSZ (25), SZ1 (54) and SZ2 (45). [src: enigma_sso_asv_ecology]
- Hydrogeological zone (VZ/VSZ/SZ1/SZ2) explains 27.5% of community variance (F = 4.05, p = 0.0001). [src: enigma_sso_asv_ecology]
- Well identity explains 19.2% of variance but is not significant (F = 0.80, p = 0.979). [src: enigma_sso_asv_ecology]

Pairwise dissimilarities agree with this. Samples from the same well at different depths are nearly maximally dissimilar (median Bray-Curtis (BC) = 0.977). Samples from the same depth zone in different wells are substantially more similar (median BC = 0.835). [src: enigma_sso_asv_ecology]

## Phylum-level depth trends

Ten of 12 dominant phyla show significant depth associations (Spearman p < 0.05). They split into two groups. [src: enigma_sso_asv_ecology]

| Group | Phylum (Spearman ρ) |
|---|---|
| Shallow-enriched (vadose, oxic) | Chloroflexi (−0.73) [src: enigma_sso_asv_ecology]; Patescibacteria (−0.70) [src: enigma_sso_asv_ecology]; Myxococcota (−0.54) [src: enigma_sso_asv_ecology]; Spirochaetota (−0.53) [src: enigma_sso_asv_ecology] |
| Deep-enriched (saturated, anoxic) | Firmicutes (+0.76) [src: enigma_sso_asv_ecology]; WPS-2 (+0.52) [src: enigma_sso_asv_ecology]; Bacteroidota (+0.50) [src: enigma_sso_asv_ecology]; Proteobacteria (+0.49) [src: enigma_sso_asv_ecology] |

## Report's interpretation

The report reads the depth pattern as plume-driven. This is its interpretation. [src: enigma_sso_asv_ecology]

- Depth dominance is explained by plume travel through the saturated zone (SZ1/SZ2). Deep samples are affected and shallow samples represent background. [src: enigma_sso_asv_ecology]
- The depth differences are described as consistent with plume travel through the saturated zone. Depth controls whether a sample intersects the plume, and horizontal position is secondary. [src: enigma_sso_asv_ecology]
- The 27.5% vertical zonation is said to reflect the plume's confinement to the saturated zone, not just generic depth gradients. [src: enigma_sso_asv_ecology]
- The report asserts that communities above the water table are unaffected by contamination. [src: enigma_sso_asv_ecology]

## Open Directions

- Test the plume explanation directly. Add measured contaminant concentrations per segment as a covariate in a PERMANOVA that includes zone. This would show whether zone adds explanatory power beyond contamination.
- Re-fit the well term with a design that nests depth within well. This would check whether the non-significant well effect is only a small-sample result, given 37 segments.
- Compare VZ and VSZ directly with SZ1 and SZ2 in pairwise zone contrasts. This would show which boundaries drive the zone effect.
- Check the shallow versus deep phylum trends in an independent set of cores. Only one dataset supports them.
