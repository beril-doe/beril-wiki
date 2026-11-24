---
type: "Method"
description: "Machine-learning classifier used to predict Pseudomonas isolation environment from pathway profiles."
sources: ["summaries/discoveries.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["Random Forest"]
---
# Random Forest classification

Machine-learning classifier used to predict Pseudomonas isolation environment from pathway profiles.

## Key facts

- Task: classify Pseudomonas into 4 environment classes: soil, freshwater, plant_surface and rhizosphere. [src: pseudomonas_carbon_ecology]
- Sample: 51 species after filtering, with soil 13, freshwater 13, plant_surface 19 and rhizosphere 6. [src: pseudomonas_carbon_ecology]
- Validation: 5-fold stratified cross-validation (CV). [src: pseudomonas_carbon_ecology]
- Result: balanced accuracy of 0.408 +/- 0.169, against a 0.250 chance baseline. [src: pseudomonas_carbon_ecology]
- The discoveries digest describes carbon-profile predictive accuracy among free-living Pseudomonas species as modest, with random forest balanced accuracy 0.41 versus 0.25 chance. [src: discoveries]
- That digest also notes that carbon profiles are significantly associated with isolation environment by permutational multivariate analysis of variance (PERMANOVA, p = 0.006). [src: discoveries]

## Most important pathways

The classifier ranks pathways by importance. The top five include several plant-related sugars, and D-serine ranks first. [src: pseudomonas_carbon_ecology]

| Rank | Pathway | Importance | Description in the report |
|---|---|---|---|
| 1 | D-serine | 0.132 | associated with rhizosphere niches [src: pseudomonas_carbon_ecology] |
| 2 | Arabinose | 0.094 | plant-derived pentose sugar [src: pseudomonas_carbon_ecology] |
| 3 | Rhamnose | 0.086 | plant cell wall component [src: pseudomonas_carbon_ecology] |
| 4 | Fucose | 0.085 | plant/animal glycan sugar [src: pseudomonas_carbon_ecology] |
| 5 | Xylose | 0.070 | hemicellulose-derived sugar [src: pseudomonas_carbon_ecology] |

## Caveats

The rhizosphere class has only 6 species. [src: pseudomonas_carbon_ecology] The discoveries digest explicitly calls the accuracy modest. [src: discoveries]

## Related pages

For how this result fits with other evidence, see [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle]], [[summaries/pseudomonas_carbon_ecology__REPORT]] and [[summaries/discoveries]]. [src: pseudomonas_carbon_ecology, discoveries]
