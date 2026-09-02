---
type: "Compound"
description: "Nickel, a metal linked to broad and condition-specific microbial stress"
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Nickel

## What this entity is

**Nickel** is a chemical element and metal examined through genome-wide fitness measurements. [src: counter_ion_effects]

Known alias: **Ni**. [src: counter_ion_effects]

No stable external identifier is specified in the source document. [src: counter_ion_effects]

## Fitness and stress-response evidence

Nickel had a 39.3% overlap between nickel-important genes and NaCl-important genes in the cross-organism analysis, based on 17 organism × nickel comparisons. [src: counter_ion_effects]

In the DvH whole-genome correlation hierarchy, nickel fitness profiles correlated with NaCl fitness profiles at Pearson **r=0.446**. [src: counter_ion_effects]

Nickel’s NaCl overlap was lower than zinc at 44.6%, cobalt at 41.3%, and copper at 41.0%, but higher than uranium at 37.2%, iron at 33.3%, chromium at 29.2%, selenium at 26.8%, mercury at 23.4%, tungsten at 10.8%, and molybdenum at 9.2%. [src: counter_ion_effects]

The report interprets nickel’s relatively high NaCl correlation as consistent with broad toxicity involving essential-cofactor displacement or disruption of multiple cellular systems, but this is an extrapolation from fitness-profile hierarchy rather than a direct biochemical test. [src: counter_ion_effects]

After removing genes shared between metal and NaCl stress responses, nickel’s core-genome enrichment delta increased from **+0.088** to **+0.098**. [src: counter_ion_effects] This increase supports the conclusion that the Metal Fitness Atlas nickel signal was not produced solely by shared NaCl-stress genes. [src: counter_ion_effects]

The report classifies the shared NaCl and metal signal as shared-stress biology rather than evidence that chloride delivered by nickel salts is the primary driver, although the analysis did not isolate chloride from sodium or osmotic effects. [src: counter_ion_effects]

The metal-specificity analysis **refines** this broad-stress interpretation: 993 of 2,271 nickel-important gene records, or 43.7%, were classified as metal-specific because they showed significant metal fitness defects but a sick rate below 5% across non-metal experiments. [src: metal_specificity] Thus, nickel has a substantial condition-specific component alongside the previously observed NaCl overlap. [src: metal_specificity]

## Cross-metal fitness evidence

The metal cross-resistance analysis **supports** the broad-stress interpretation: nickel fitness profiles were positively associated with cobalt, zinc, and copper, with mean correlations of **r = 0.56** across 28 organisms, **r = 0.51** across 18 organisms, and **r = 0.43** across 24 organisms, respectively. [src: metal_cross_resistance]

Nickel also showed a weaker listed association with aluminum (**r = 0.34**), which **refines** the existing interpretation by indicating a universal positive direction alongside chemistry-dependent magnitudes rather than uniformly interchangeable metal responses. [src: metal_cross_resistance]

Across the study, 98.1% of gene-level metal-fitness correlations were positive (311/317), and no metal pair showed systematically negative cross-resistance; these results **support** nickel’s association with shared cellular stress, while not by themselves identifying the biochemical mechanism. [src: metal_cross_resistance]

## Pan-bacterial atlas evidence

The Pan-Bacterial Metal Fitness Atlas **supports** the existing core-enrichment signal: across 26 nickel-profiled organisms, it identified 1,760 nickel-important genes with a core fraction of 0.877, a core-fraction delta of **+0.088**, OR=1.93, and p=3.0e-22. [src: metal_fitness_atlas] This genome-wide result complements the counter-ion analysis because removing genes shared with NaCl increased the delta to **+0.098**, rather than eliminating the enrichment. [src: counter_ion_effects]

The atlas **refines** the interpretation of nickel resistance by placing nickel among metals whose important genes are predominantly core-genome genes, while the report’s two-tier model reserves specialized accessory functions such as efflux, sequestration, and enzymatic detoxification for a narrower resistance layer. [src: metal_fitness_atlas] This distinction qualifies the field-versus-lab inference that specific resistance mechanisms may be accessory rather than contradicting it. [src: field_vs_lab_fitness]

## Field-versus-lab fitness evidence

The field-versus-lab analysis **refines** the broad-stress interpretation by placing nickel in a heavy-metals category whose important genes had a 71.2% core fraction among 198 genes (OR=0.77 versus baseline, FDR q=0.14); this was lower than the 76.3% all-gene baseline but not statistically significant after correction. [src: field_vs_lab_fitness]

Across fitness thresholds, the heavy-metals category was 70.6%, 71.2%, 76.7%, and 76.7% core at thresholds -3.0, -2.0, -1.5, and -1.0, respectively. [src: field_vs_lab_fitness] The report **supports and qualifies** the existing inference about broad metal stress: it suggests the hypothesis that specific metal-resistance mechanisms, such as efflux pumps and metal-binding proteins, may be accessory, while noting that this is not a direct measurement of genomic acquisition history. [src: field_vs_lab_fitness]

## Environmental metal-resistance ecology

The MicrobeAtlas analysis **refines** nickel-specific interpretation by showing that the broader ecological association was tested for aggregate metal type diversity, not for nickel as an isolated causal factor. In the leave-one-metal-out analysis, excluding nickel retained a positive but non-significant association between metal-type diversity and inferred niche breadth (**β = +0.0095, p = 0.140**); the report notes that removing any one of the 7 metals also compressed predictor variance and reduced power. [src: microbeatlas_metal_ecology] Thus, the result supports a distributed cross-metal pattern rather than establishing that nickel alone drives ecological generalism. [src: microbeatlas_metal_ecology]

## Soil functional-genomics evidence

A separate observational soil analysis included nickel among nine measured metals and identified 2,355 significant COG–metal associations at FDR < 0.05 across 51,748 samples; COG means Cluster of Orthologous Groups functional category and FDR means false discovery rate. [src: soil_metal_functional_genomics] This **supports** the relevance of nickel-associated functional shifts beyond laboratory fitness assays, but does not establish nickel-specific causation or effect size. [src: soil_metal_functional_genomics]

The soil result **refines** the existing cross-metal interpretation: metal co-contamination and non-independence among tests leave it unresolved whether individual associations reflect nickel itself or a broader multi-metal response, and planned partial-correlation, effect-size, and spatial analyses remain pending. [src: soil_metal_functional_genomics]

## Related pages

- [[summaries/counter_ion_effects__REPORT]]
- [[summaries/field_vs_lab_fitness__REPORT]]
- [[summaries/metal_cross_resistance__REPORT]]
- [[summaries/metal_fitness_atlas__REPORT]]
- [[summaries/metal_specificity__REPORT]]
- [[summaries/microbeatlas_metal_ecology__REPORT]]
- [[summaries/soil_metal_functional_genomics__REPORT]]
- [[concepts/condition-specific-fitness]]
- [[concepts/gene-essentiality]]
- [[concepts/cofitness-network-architecture]]
- [[concepts/metal-cross-resistance]]
- [[entities/cobalt]]
- [[entities/copper]]
- [[entities/zinc]]
