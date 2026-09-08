---
type: Concept
description: Evidence for conditional, limited concordance between lab fitness and
  environmental gene distributions
sources:
- id: functional_dark_matter
  resource: ../summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: lab_field_ecology
  resource: ../summaries/lab_field_ecology__REPORT.md
  title: lab field ecology
- id: fitness_effects_conservation
  resource: ../summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
title: Testing whether laboratory fitness phenotypes predict environmental gene distributions
---
# Testing whether laboratory fitness phenotypes predict environmental gene distributions

Laboratory fitness phenotypes can be tested as predictors of where genes occur in natural environments by linking within-species carrier-versus-non-carrier comparisons, environmental metadata, and independent metagenomic observations. The evidence supports partial lab–field concordance, but it does not establish that laboratory fitness effects alone determine environmental gene distributions. [^functional_dark_matter]

## Core evidence

The study tested 151 accessory dark-gene clusters across 31 species using carrier-versus-non-carrier environmental comparisons. Of 137 clusters tested for environmental-category enrichment, 10 were significant at FDR < 0.05, where FDR means the false-discovery rate, and 1 of 67 showed significant AlphaEarth embedding divergence. [^functional_dark_matter]

A pre-registered mapping between laboratory fitness conditions and environmental associations found 29 of 47 testable clusters concordant, corresponding to 61.7% concordance. Concordance was 100% across 4 pH tests and 78% across 9 nitrogen-source tests. [^functional_dark_matter]

The 29/47 concordance rate provides suggestive rather than decisive evidence: a one-sided binomial test gave p = 0.072 with Wilson score 95% CI [0.474, 0.742], whereas Fisher’s combined probability across 47 individual tests gave p = 0.031. These statistics answer different questions and should not be treated as a single resolved significance claim. [^functional_dark_matter]

The strongest reported biogeographic associations occurred in *Pseudomonas putida*: PP_0025 had odds ratio 27.5 and FDR 7e-6, while PP_3434 had odds ratio 28.6 and FDR 7e-6. AO356_11255 had odds ratio 44.0 and FDR 0.093, with carriers enriched in soil, freshwater, and wastewater relative to non-carriers. Its environmental pattern matched a nitrogen-utilization fitness phenotype, but this match remains an association rather than direct evidence of ecological causation. [^functional_dark_matter]

A direct test linking laboratory metal-tolerance phenotypes to field abundance **refines** this evidence toward conditional rather than universal concordance. Across 108 Oak Ridge groundwater sites, the aggregate laboratory tolerance score had a positive but non-significant association with the high-uranium/low-uranium abundance ratio (Spearman rho = 0.503, p = 0.095, n = 12 genera), while five of 11 tested genera had significant uranium associations after BH-FDR correction, with effects in both directions. [^lab_field_ecology] This supports the interpretation that environmental structure can be detected at particular taxa or conditions without showing that a general laboratory tolerance ranking predicts field distributions. [^lab_field_ecology]

An ecotype analysis **refines** this evidence by showing that whole-genome gene-content similarity was generally more strongly associated with phylogenetic than environmental similarity: across 172 species, the median partial correlation was 0.0025 for environment versus 0.0143 for phylogeny, with phylogeny dominant in 60.5% of species. A significant positive environmental effect occurred in 12 species (7.0%), a significant negative effect in 4 species (2.3%), and no significant effect in 156 species (90.7%). [^ecotype_analysis] This supports interpreting laboratory–environment concordance as conditional and potentially locus-specific rather than as evidence that environmental conditions broadly explain accessory gene distributions. The analysis also suggests the hypothesis that environmental effects may be more detectable in specific functional subsets than in whole-genome gene content. [^ecotype_analysis]

## Independent metagenomic validation

The National Microbiome Data Collaborative (NMDC) analysis independently mapped 5 of 6 carrier genera to 47 taxon columns across 6,365 metagenomic samples. It confirmed all 4 testable pre-registered abiotic predictions: nitrogen-source carriers correlated with total nitrogen at ρ = +0.109, n = 1,231, FDR = 2.3e-4, and ammonium nitrogen at ρ = +0.231, n = 1,230, FDR = 8.0e-16; pH carriers correlated with pH at ρ = +0.157, n = 4,366, FDR = 7.4e-25; and anaerobic carriers correlated negatively with dissolved oxygen at ρ = -0.298, n = 272, FDR = 1.5e-6. [^functional_dark_matter]

NMDC trait-feature analysis also confirmed all 7 pre-registered trait-condition predictions at FDR < 10⁻²¹, including associations of nitrogen-source carriers with nitrogen fixation at ρ = 0.60 and nitrate denitrification at ρ = 0.52, and of carbon-source carriers with aerobic chemoheterotrophy at ρ = 0.73 and fermentation at ρ = 0.59. [^functional_dark_matter]

The independent validation strengthens the hypothesis that some laboratory phenotypes predict environmental distributions, especially for pre-specified abiotic directions. However, 441 of 449 exploratory tests also reached FDR < 0.05, and the report attributes this high rate largely to compositional coupling because abundant genera contribute to both carrier abundance and community trait scores. [^functional_dark_matter]

## Interpretation and limits

The strongest interpretation is conditional concordance: laboratory fitness can identify environmentally structured genes or carriers when the laboratory condition corresponds to an ecologically relevant resource or stressor, but laboratory phenotypes should not be assumed to predict natural distributions universally. [^functional_dark_matter] The Oak Ridge result **supports** this qualification: genus-level field associations were bidirectional, and the aggregate metal-tolerance relationship was only suggestive rather than statistically significant. [^lab_field_ecology] The ecotype result **supports** this qualification: environmental effects were usually weak or non-significant for whole-genome gene content, and environmental and host-associated bacteria did not differ significantly in environmental effects (p=0.66). [^ecotype_analysis] It also **refines** the interpretation by raising the hypothesis that collection coordinates and AlphaEarth embeddings may fail to represent the relevant microenvironment, particularly for host-associated organisms. [^ecotype_analysis]

A cross-species Fitness Browser–pangenome analysis **supports** this caution while clarifying the distinction between predicting conservation and predicting environmental distribution. Across approximately 194,000 genes from 43 bacteria, essential genes were 82% core whereas always-neutral genes were 66% core; fitness breadth was positively but weakly associated with core status (Spearman rho=0.086, p=8.1e-230). [^fitness_effects_conservation] Thus, laboratory fitness importance can track broad evolutionary conservation, but only weakly, and this result does not show that fitness predicts where genes occur environmentally. The same analysis **refines** the interpretation of condition specificity: strong condition-specific effects were more common among core genes (77.3%) than genes without specific phenotypes (70.3%), and 4,450 genes fit an ephemeral-niche pattern of overall neutrality but criticality in one condition. [^fitness_effects_conservation] This supports treating condition-specific laboratory effects as potentially informative about environmental specialization without assuming they are confined to accessory genes.

A DvH comparison **refines** this interpretation by separating environmental transfer from conservation prediction. Across 757 Fitness Browser experiments, condition class explained less of pangenome conservation than fitness importance: field-stress-important genes were 83.6% core and field-core-important genes were 82.4% core, while the overall non-essential baseline was 76.3%; logistic models had cross-validated AUCs of 0.517 for field fitness alone, 0.531 for lab fitness alone, and 0.548 for both, versus 0.645 after adding gene length. These results are from a single organism and predict core status rather than environmental distribution, so they **support** caution against treating laboratory fitness as a sufficient environmental predictor. [^field_vs_lab_fitness]

The environmental analysis is limited by sparse metadata, inconsistent NCBI isolation-source records, and AlphaEarth coverage of only 28% of genomes, or 83K/293K. [^functional_dark_matter] The ecotype analysis reports AlphaEarth coverage of only 28.4% of genomes and likewise identifies missing or imprecise geographic coordinates as a limitation. [^ecotype_analysis] NMDC validation was conducted at genus level, matched only 5 of 6 carrier genera, and may be influenced by broad correlations involving common genera such as *Pseudomonas*, *Klebsiella*, and *Bacteroides*. [^functional_dark_matter]

The Oak Ridge analysis **further refines** these limitations: 16S amplicon sequencing could not match laboratory organisms at species or strain level, and pH, dissolved oxygen, carbon sources, temporal history, and other geochemical factors were not controlled. [^lab_field_ecology] The ecotype analysis further **refines** the environmental limitation: its partial correlations assume linear relationships between distance matrices, and geographic coordinates may describe collection sites rather than organisms’ actual microenvironments. [^ecotype_analysis] The study did not run equivalent annotated-accessory-gene controls through the complete biogeographic pipeline, so the reported dark-gene associations cannot yet be separated fully from effects of accessory-gene prevalence, taxonomic composition, or analysis design. [^functional_dark_matter]

The NMDC trait results therefore support [environment-embedding-geography](environment-embedding-geography.md) and [environmental-resistome](environmental-resistome.md) as evidence of testable environmental structure, while also reinforcing [taxonomic-resolution-dependent-functional-inference](taxonomic-resolution-dependent-functional-inference.md) and [environment-embedding-geography](environment-embedding-geography.md) as safeguards against causal overinterpretation. [^functional_dark_matter]

## Relation to fitness experiments

The laboratory component used Fitness Browser phenotypes to classify gene-condition relationships, while the environmental component tested whether carrier distributions tracked metadata or embedding dimensions. This cross-domain design connects [condition-specific-fitness](condition-specific-fitness.md) with [lab-field-fitness-concordance](lab-field-fitness-concordance.md) and [environment-embedding-geography](environment-embedding-geography.md). [^functional_dark_matter]

The result refines a simple laboratory-to-field transfer model: agreement was observed for 29 of 47 testable clusters, but the one-sided binomial result was p = 0.072, metadata coverage was incomplete, and compositional coupling affected exploratory trait associations. [^functional_dark_matter] The DvH analysis **supports** this refinement: field and laboratory fitness dimensions were only weak predictors of core status individually, with field-plus-lab CV-AUC 0.548, while gene length increased the full-model CV-AUC to 0.645. [^field_vs_lab_fitness] The Oak Ridge test **supports** the same refinement by showing that a field abundance gradient can contain significant taxon-specific signals even when the aggregate laboratory tolerance score is not significant. [^lab_field_ecology] The cross-species conservation analysis further **supports** separating these questions: fitness importance showed a weak association with core status across approximately 194,000 genes, but the analysis did not test environmental distributions directly. [^fitness_effects_conservation]

The ecotype analysis **supports** testing this model at the level of functional subsets rather than only whole-genome gene content: it proposes evaluating COG categories, including V-Defense and L-Mobile, for stronger environmental effects. [^ecotype_analysis] The DvH evidence also **refines** the scope of the transfer question: its 678 essential genes lacked transposon fitness data, and the analysis therefore compared conditionally important non-essential genes with pangenome status rather than testing all genes’ environmental distributions. [^field_vs_lab_fitness]

## Open Directions

- Use full NMDC sample labels with within-sample permutation tests that preserve taxonomic structure to determine whether the 441 of 449 exploratory associations remain after compositional coupling is controlled. [^functional_dark_matter]
- Run the complete carrier-versus-non-carrier biogeographic pipeline on matched annotated-accessory-gene controls to test whether dark-gene associations exceed the background rate for accessory genes. [^functional_dark_matter]
- Expand environmental validation beyond the 5 of 6 matched carrier genera by integrating species-resolved or strain-resolved observations and asking whether laboratory phenotype–environment concordance persists below genus level. [^functional_dark_matter]
- Increase environmental metadata coverage beyond the 28% AlphaEarth genome coverage and harmonize isolation-source fields to test whether the 29/47 concordance estimate changes with improved environmental resolution. [^functional_dark_matter]
- Replicate the pre-registered pH, nitrogen-source, carbon-source, and anaerobic predictions in independent cohorts using partial-correlation or matched-sample models to distinguish ecological signal from study and taxonomic composition. [^functional_dark_matter]
- Compare environmental carrier predictions with condition-specific fitness across additional organisms, using continuous fitness scores and quantitative gene-cluster prevalence rather than binary core/auxiliary status to test whether the DvH pattern generalizes. [^field_vs_lab_fitness]
- Test COG functional subsets, alternative embedding distances, and direct environmental metadata in the 172-species ecotype dataset to determine whether locus-specific environmental effects are obscured by whole-genome analyses. [^ecotype_analysis]
- Match species- or strain-resolved Oak Ridge metagenomic observations to uranium-specific laboratory fitness scores, while controlling for pH, redox, and carbon sources, to test whether the genus-level bidirectional associations persist below 16S resolution. [^lab_field_ecology]
- Test whether the weak fitness–conservation relationship generalizes to environmental prevalence by modeling continuous gene-cluster abundance across matched habitats, while controlling for gene length, transposon coverage, phylogeny, and taxonomic composition. [^fitness_effects_conservation]

See [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) for the DvH analysis details, [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md) for the ecotype correlation analysis, [lab_field_ecology__REPORT](../summaries/lab_field_ecology__REPORT.md) for the Oak Ridge laboratory-to-field test, and [fitness_effects_conservation__REPORT](../summaries/fitness_effects_conservation__REPORT.md) for the cross-species fitness–conservation analysis.

[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
[^lab_field_ecology]: [lab field ecology](../summaries/lab_field_ecology__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../summaries/fitness_effects_conservation__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
