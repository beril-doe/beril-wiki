---
type: "Concept"
description: "How well laboratory fitness predicts environmental gene distributions"
sources: ["summaries/functional_dark_matter__REPORT.md"]
---
# Testing whether laboratory fitness phenotypes predict environmental gene distributions

Laboratory fitness phenotypes can be tested as predictors of where genes occur in natural environments by linking within-species carrier-versus-non-carrier comparisons, environmental metadata, and independent metagenomic observations. The evidence supports partial lab–field concordance, but it does not establish that laboratory fitness effects alone determine environmental gene distributions. [src: functional_dark_matter]

## Core evidence

The study tested 151 accessory dark-gene clusters across 31 species using carrier-versus-non-carrier environmental comparisons. Of 137 clusters tested for environmental-category enrichment, 10 were significant at FDR < 0.05, where FDR means the false-discovery rate, and 1 of 67 showed significant AlphaEarth embedding divergence. [src: functional_dark_matter]

A pre-registered mapping between laboratory fitness conditions and environmental associations found 29 of 47 testable clusters concordant, corresponding to 61.7% concordance. Concordance was 100% across 4 pH tests and 78% across 9 nitrogen-source tests. [src: functional_dark_matter]

The 29/47 concordance rate provides suggestive rather than decisive evidence: a one-sided binomial test gave p = 0.072 with Wilson score 95% CI [0.474, 0.742], whereas Fisher’s combined probability across 47 individual tests gave p = 0.031. These statistics answer different questions and should not be treated as a single resolved significance claim. [src: functional_dark_matter]

The strongest reported biogeographic associations occurred in *Pseudomonas putida*: PP_0025 had odds ratio 27.5 and FDR 7e-6, while PP_3434 had odds ratio 28.6 and FDR 7e-6. AO356_11255 had odds ratio 44.0 and FDR 0.093, with carriers enriched in soil, freshwater, and wastewater relative to non-carriers. Its environmental pattern matched a nitrogen-utilization fitness phenotype, but this match remains an association rather than direct evidence of ecological causation. [src: functional_dark_matter]

## Independent metagenomic validation

The National Microbiome Data Collaborative (NMDC) analysis independently mapped 5 of 6 carrier genera to 47 taxon columns across 6,365 metagenomic samples. It confirmed all 4 testable pre-registered abiotic predictions: nitrogen-source carriers correlated with total nitrogen at ρ = +0.109, n = 1,231, FDR = 2.3e-4, and ammonium nitrogen at ρ = +0.231, n = 1,230, FDR = 8.0e-16; pH carriers correlated with pH at ρ = +0.157, n = 4,366, FDR = 7.4e-25; and anaerobic carriers correlated negatively with dissolved oxygen at ρ = -0.298, n = 272, FDR = 1.5e-6. [src: functional_dark_matter]

NMDC trait-feature analysis also confirmed all 7 pre-registered trait-condition predictions at FDR < 10⁻²¹, including associations of nitrogen-source carriers with nitrogen fixation at ρ = 0.60 and nitrate denitrification at ρ = 0.52, and of carbon-source carriers with aerobic chemoheterotrophy at ρ = 0.73 and fermentation at ρ = 0.59. [src: functional_dark_matter]

The independent validation strengthens the hypothesis that some laboratory phenotypes predict environmental distributions, especially for pre-specified abiotic directions. However, 441 of 449 exploratory tests also reached FDR < 0.05, and the report attributes this high rate largely to compositional coupling because abundant genera contribute to both carrier abundance and community trait scores. [src: functional_dark_matter]

## Interpretation and limits

The strongest interpretation is conditional concordance: laboratory fitness can identify environmentally structured genes or carriers when the laboratory condition corresponds to an ecologically relevant resource or stressor, but laboratory phenotypes should not be assumed to predict natural distributions universally. [src: functional_dark_matter]

The environmental analysis is limited by sparse metadata, inconsistent NCBI isolation-source records, and AlphaEarth coverage of only 28% of genomes, or 83K/293K. NMDC validation was conducted at genus level, matched only 5 of 6 carrier genera, and may be influenced by broad correlations involving common genera such as *Pseudomonas*, *Klebsiella*, and *Bacteroides*. [src: functional_dark_matter]

The study did not run equivalent annotated-accessory-gene controls through the complete biogeographic pipeline, so the reported dark-gene associations cannot yet be separated fully from effects of accessory-gene prevalence, taxonomic composition, or analysis design. [src: functional_dark_matter]

The NMDC trait results therefore support [[concepts/environment-embedding-geography]] and [[concepts/ecological-resistance-association-and-causality]] as evidence of testable environmental structure, while also reinforcing [[concepts/coverage-confounding-of-community-functional-scores]] and [[concepts/sampling-composition-confounding-of-environmental-signal]] as safeguards against causal overinterpretation. [src: functional_dark_matter]

## Relation to fitness experiments

The laboratory component used Fitness Browser phenotypes to classify gene-condition relationships, while the environmental component tested whether carrier distributions tracked metadata or embedding dimensions. This cross-domain design connects [[concepts/condition-specific-fitness]] with [[concepts/lab-field-fitness-concordance]] and [[concepts/environmental-embedding-ecological-validity]]. [src: functional_dark_matter]

The result refines a simple laboratory-to-field transfer model: agreement was observed for 29 of 47 testable clusters, but the one-sided binomial result was p = 0.072, metadata coverage was incomplete, and compositional coupling affected exploratory trait associations. [src: functional_dark_matter]

## Open Directions

- Use full NMDC sample labels with within-sample permutation tests that preserve taxonomic structure to determine whether the 441 of 449 exploratory associations remain after compositional coupling is controlled. [src: functional_dark_matter]
- Run the complete carrier-versus-non-carrier biogeographic pipeline on matched annotated-accessory-gene controls to test whether dark-gene associations exceed the background rate for accessory genes. [src: functional_dark_matter]
- Expand environmental validation beyond the 5 of 6 matched carrier genera by integrating species-resolved or strain-resolved observations and asking whether laboratory phenotype–environment concordance persists below genus level. [src: functional_dark_matter]
- Increase environmental metadata coverage beyond the 28% AlphaEarth genome coverage and harmonize isolation-source fields to test whether the 29/47 concordance estimate changes with improved environmental resolution. [src: functional_dark_matter]
- Replicate the pre-registered pH, nitrogen-source, carbon-source, and anaerobic predictions in independent cohorts using partial-correlation or matched-sample models to distinguish ecological signal from study and taxonomic composition. [src: functional_dark_matter]
