---
type: Compound
description: Cobalt and its conserved, environment-dependent microbial fitness responses
sources:
- id: counter_ion_effects
  resource: ../summaries/counter_ion_effects__REPORT.md
  title: counter ion effects
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: metal_cross_resistance
  resource: ../summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: metal_specificity
  resource: ../summaries/metal_specificity__REPORT.md
  title: metal specificity
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Cobalt
---
# Cobalt

## Identity

- **Canonical name:** cobalt. [^counter_ion_effects]
- **Known alias:** Co. [^counter_ion_effects]
- **Stable external identifier:** No stable external identifier was reported in [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md). [^counter_ion_effects]

## Evidence from Counter-Ion Effects

Cobalt was one of 14 metals evaluated across 19 organisms and 86 organism × metal pairs in a study of whether counter ions confound genome-wide metal-fitness measurements. [^counter_ion_effects]

Cobalt-associated metal-important genes had a 41.3% overlap with NaCl-important genes. [^counter_ion_effects] Cobalt delivered up to 500 mM chloride in the tested metal-salt experiments. [^counter_ion_effects] The mean NaCl overlap for metals delivered with chloride was 41.6%, compared with 37.8% for metals delivered without chloride; cobalt’s 41.3% overlap therefore did not establish a chloride-dose relationship. [^counter_ion_effects]

In the DvH whole-genome correlation analysis, cobalt fitness profiles had a Pearson correlation of **r=0.498** with NaCl fitness profiles. [^counter_ion_effects] The DvH correlation hierarchy did not follow chloride concentration, because zinc sulfate supplied 0 mM chloride yet ranked above cobalt with **r=0.715** versus cobalt’s **r=0.498**. [^counter_ion_effects]

The report interprets cobalt’s relatively high NaCl correlation as consistent with broad toxicity involving essential-cofactor displacement or disruption of multiple cellular systems, but this is an extrapolation from fitness-profile correlations rather than a direct biochemical test. [^counter_ion_effects] After shared-stress genes were removed, cobalt’s corrected core-genome enrichment remained **+0.076**, unchanged from the original value. [^counter_ion_effects] This unchanged enrichment supports the conclusion that cobalt’s Metal Fitness Atlas core-enrichment signal was not produced by genes shared with NaCl stress responses. [^counter_ion_effects]

## Evidence from Cross-Resistance

Across 452 metal experiments, cobalt participated in a gene-level cross-resistance analysis spanning 37 organisms and 14 metals; among 28 organisms with data for at least 3 metals, the Co–Ni fitness correlation was **r = 0.56** across **n = 28** organisms, Co–Zn was **r = 0.52** across **n = 18**, Co–Fe was **r = 0.45** across **n = 7**, and Co–Cu was **r = 0.43** across **n = 24**. [^metal_cross_resistance]

These consistently positive associations **support** the existing interpretation of broad cobalt toxicity, while **refining** it: cross-resistance showed a universal positive directional layer, whereas the magnitude of the association varied by metal pair. [^metal_cross_resistance] No tested metal pair showed systematically negative cross-resistance, and all 15 pairs tested in at least 5 organisms had greater than 90% sign consistency; the report therefore suggests that cobalt-associated fitness responses are part of a conserved cross-metal stress architecture rather than evidence of cobalt-specific antagonism. [^metal_cross_resistance]

Cobalt was among the more strongly connected metals in the cross-resistance network, while Al–Co was among the weaker listed pairings at **r = 0.30**; this **refines** the interpretation that chemistry influences response magnitude without overturning the general positive direction. [^metal_cross_resistance] The cross-resistance analysis identified 318 ortholog groups that were metal-shared in at least 2 organisms, with broadly conserved functions including cell envelope, energy metabolism, DNA repair, and ion homeostasis; these findings **support** a shared cellular basis for cobalt responses but do not identify a cobalt-exclusive mechanism. [^metal_cross_resistance]

## Evidence from the Pan-Bacterial Metal Fitness Atlas

The Metal Fitness Atlas included cobalt in 559 metal-related experiments across 31 organisms and 16 metals; cobalt had cross-species coverage in **27 organisms**, among the broadest coverage in the atlas. [^metal_fitness_atlas] Among cobalt-associated metal-important genes, **1,859** were identified, with a core fraction of **0.859**, a core-fraction delta of **+0.072**, **OR=1.67**, and **p=8.1e-16**. [^metal_fitness_atlas] This **supports** the counter-ion result that cobalt’s core-enrichment signal persists after removing shared-stress genes, while **refining** the interpretation: cobalt responses include broadly conserved cellular functions, not only accessory cobalt-resistance genes. [^metal_fitness_atlas]

The metal-specificity analysis **refines** this broad atlas classification: **1,167 of 2,324 cobalt-associated records (50.2%)** were metal-specific, defined as significant under metal stress but sick in fewer than 5% of 5,945 non-metal experiments. [^metal_specificity] Thus, cobalt combines a substantial condition-specific component with the broadly conserved component captured by the atlas’s wider metal-important definition. [^metal_specificity]

The atlas’s two-tier model distinguishes core general-stress functions from accessory specialized mechanisms such as efflux, sequestration, and enzymatic detoxification. [^metal_fitness_atlas] This **supports** the existing evidence for broad cobalt toxicity but **refines** it by treating accessory cobalt-specific resistance as a second tier that is less visible under a genome-wide metal-important definition. [^metal_fitness_atlas] The atlas also cautions that its broad definition, fit < -1 OR n_sick ≥ 1, captures many general-stress genes; it recommends testing genes important for metals but not other stresses to isolate cobalt-specific resistance. [^metal_fitness_atlas] The 50.2% cobalt-specific fraction directly implements that proposed separation, although it was calculated from 24 organisms included after locusId filtering rather than all 31 metal-tested organisms. [^metal_specificity]

## Evidence from Field-vs-Lab Fitness

The field-vs-lab analysis included cobalt among the heavy-metal conditions, alongside nickel, zinc, copper, manganese, selenium, molybdate, tungstate, and aluminum. [^field_vs_lab_fitness] This **refines** the counter-ion analysis by placing cobalt-associated fitness measurements within a broader environmental heavy-metal category rather than treating them as a direct cobalt-specific conservation result.

Across heavy-metal-important genes in *Desulfovibrio vulgaris* Hildenborough, 71.2% were core, compared with a 76.3% all-gene baseline; the difference was not statistically significant (OR=0.77, FDR q=0.14). [^field_vs_lab_fitness] This **supports** the existing interpretation that cobalt-related stress can involve broad toxicity, while **refining** it by showing that the low conservation pattern was reported for the combined heavy-metals category, not cobalt alone. [^field_vs_lab_fitness]

The report suggests the hypothesis that specific metal-resistance mechanisms, such as efflux pumps and metal-binding proteins, may be accessory, whereas uranium- and mercury-related responses may involve more fundamental stress pathways; this is a category-level hypothesis, not a direct demonstration for cobalt. [^field_vs_lab_fitness] Cross-resistance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8); because the validation was underpowered and not cobalt-specific, this **refines** rather than contradicts the broader environmental interpretation. [^metal_cross_resistance]

## Evidence from Soil Functional Genomics

A soil metagenomic analysis found cobalt among nine metals associated with microbial functional gene content across **51,748** soil samples. Across the nine metals, **2,355** significant COG–metal associations were identified at FDR < 0.05; transporters, including ABC and RND systems, and biosynthesis genes dominated the top hits, while chromium and lead produced the strongest signals. [^soil_metal_functional_genomics] This **supports** the existing evidence that cobalt responses can involve transport and biosynthetic functions, but **refines** it by showing that the result is observational, community-level, and not necessarily cobalt-specific. [^soil_metal_functional_genomics]

The soil result does not establish a cobalt-exclusive mechanism: chromium, copper, lead, and zinc co-vary in many industrial soils, and partial-correlation analyses are planned to distinguish individual-metal associations from generic multi-metal contamination responses. [^soil_metal_functional_genomics] This **refines** the positive cross-resistance evidence by identifying co-contamination as a potential confound, rather than contradicting the observed conserved direction of cobalt-associated responses. [^soil_metal_functional_genomics]

## Related Pages

Cobalt’s results relate to [sodium-chloride](sodium-chloride.md) through the comparison of shared NaCl and metal-fitness signals, and to [copper](copper.md) and [nickel](nickel.md) as other tested metals. [^counter_ion_effects]

The findings contribute to [condition-specific-fitness](../concepts/condition-specific-fitness.md) by separating shared-stress responses from cobalt-specific fitness responses. [^counter_ion_effects] They also contribute to [metal-cross-resistance](../concepts/metal-cross-resistance.md) and [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) through conserved positive cross-metal fitness correlations. [^metal_cross_resistance] The atlas additionally connects cobalt to [pangenome-integration](../concepts/pangenome-integration.md) through its core/accessory conservation analysis. [^metal_fitness_atlas] The specificity classification further connects cobalt to [metal-cross-resistance](../concepts/metal-cross-resistance.md) by distinguishing its metal-specific records from broadly shared stress responses. [^metal_specificity] The soil analysis connects cobalt to [environmental-resistome](../concepts/environmental-resistome.md), [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md), [metal-cross-resistance](../concepts/metal-cross-resistance.md), and [environment-embedding-geography](../concepts/environment-embedding-geography.md) through environment-dependent functional associations and unresolved co-contamination and spatial-matching issues. [^soil_metal_functional_genomics]

The complete analyses are summarized in [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md), [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md), [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md), [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md), [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md), and [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md). [^counter_ion_effects][^field_vs_lab_fitness][^metal_cross_resistance][^metal_fitness_atlas][^metal_specificity][^soil_metal_functional_genomics]

[^counter_ion_effects]: [counter ion effects](../summaries/counter_ion_effects__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../summaries/metal_cross_resistance__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
