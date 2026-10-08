---
type: "Concept"
description: "Contaminant concentration, especially uranium together with low pH and metals, as an axis that selects subsurface microbial community composition, distinct from hydrogeological zonation."
sources: ["summaries/lab_field_ecology__REPORT.md"]
---
# Contaminant Gradients Select Subsurface Community Composition

This page tracks evidence that contaminant load, chiefly [[entities/uranium]] with co-occurring low pH and metals, acts as a selective axis on subsurface microbial communities. It is treated separately from physical and hydrological structuring, which is covered in [[concepts/subsurface-hydrogeological-zonation]]. All current evidence comes from a single project, [[summaries/lab_field_ecology__REPORT]], which studied Oak Ridge groundwater communities. The axis is therefore provisional until other projects test it [src: lab_field_ecology].

## Evidence

When sites are split at the median uranium concentration, the high- and low-uranium groups show distinct community compositions [src: lab_field_ecology]. The report describes this compositional difference without a test statistic, effect size or confound control. The finding therefore establishes a uranium-associated compositional contrast, not a causal effect of uranium separable from correlated site properties [src: lab_field_ecology].

The top genera differ between high-uranium and low-uranium sites. Rare-biosphere taxa and subsurface specialists become more prominent at contaminated sites [src: lab_field_ecology]. This **refines** the median-split result: contamination is associated with a shift toward rare-biosphere taxa and subsurface specialists, not only with a generic compositional difference [src: lab_field_ecology].

The report cites Carlson et al. (2019), who showed that low pH combined with elevated uranium and metals selectively inhibits non-*Rhodanobacter* taxa at the [[entities/oak-ridge-field-research-center]]. That work explains the dominance of [[entities/rhodanobacter]] at contaminated wells [src: lab_field_ecology]. This is a published finding brought in from prior literature, not a measurement made in this project. Applying it to explain the contaminant-associated composition contrast observed in this project is an extrapolation. It suggests the hypothesis that the same acid-plus-metal selective inhibition contributes to the rare-biosphere and specialist shift reported here [src: lab_field_ecology].

## Relation to Other Axes

The uranium split is reported as a compositional contrast, while low pH and metals are named as co-stressors in the cited *Rhodanobacter* mechanism. As a result, the current evidence cannot separate uranium-specific selection from selection by acidity or other metals that co-vary with it. Nor can it separate contaminant selection from the hydrogeological structuring described in [[concepts/subsurface-hydrogeological-zonation]] [src: lab_field_ecology].

## Open Directions

- Proposal: replace the median split with a continuous-gradient ordination. One option is db-RDA (distance-based redundancy analysis, which partitions community dissimilarity among environmental predictors), using uranium, pH and other metal concentrations as joint predictors on the project's Oak Ridge groundwater 16S amplicon sites. This would test whether uranium explains composition beyond pH and co-occurring metals. The gap exists because the reported composition result is a median split [src: lab_field_ecology].
- Proposal: model *Rhodanobacter* relative abundance against pH, uranium and metal concentrations, including their interactions, across Oak Ridge wells. This would test whether the selective-inhibition mechanism from Carlson et al. (2019) predicts abundance in this corpus's data, because the report cites that mechanism from the literature rather than testing it [src: lab_field_ecology].
- Proposal: fit a model that includes both hydrogeological zone and contaminant terms. This would test whether the enrichment of rare-biosphere taxa and subsurface specialists at contaminated sites persists within zones, separating contaminant selection from [[concepts/subsurface-hydrogeological-zonation]] [src: lab_field_ecology].
