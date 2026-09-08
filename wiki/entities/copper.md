---
type: Compound
description: Copper evidence spans metal fitness, cross-resistance, and soil functional
  genomics.
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
- id: microbeatlas_metal_ecology
  resource: ../summaries/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Copper
---
# Copper

## What it is

- **Canonical name:** copper. [^counter_ion_effects]
- **Known alias:** Cu. [^counter_ion_effects]
- **Stable external identifier:** No stable external identifier was reported in the source document. [^counter_ion_effects]

## Evidence from counter-ion analysis

Copper was included among 14 metals analyzed across 19 organisms and 86 organism × metal pairs to test whether chloride counter ions confound genome-wide metal-fitness measurements. [^counter_ion_effects]

Copper-important gene records overlapped with NaCl-important records at **41.0%** across **16 organisms**. [^counter_ion_effects] This was close to cobalt at **41.3%** and exceeded nickel at **39.3%**. [^counter_ion_effects] The shared signal was interpreted as shared cellular-stress biology rather than chloride contamination, potentially involving cell-envelope integrity, DNA repair, and ion homeostasis; these mechanistic categories remain hypotheses because formal functional-enrichment tests were not performed. [^counter_ion_effects]

Chloride-delivered metals had a mean NaCl overlap of **41.6%**, versus **37.8%** for non-chloride metals, but chloride dose was not considered the primary driver because zinc sulfate supplied **0 mM chloride** and still had **44.6%** overlap. [^counter_ion_effects]

In *Desulfovibrio vulgaris* Hildenborough (DvH), the whole-genome Pearson correlation between copper and NaCl fitness profiles was **r=0.532**, ranking copper third among 13 metals. [^counter_ion_effects] The DvH hierarchy did not follow chloride concentration: zinc sulfate supplied zero chloride yet ranked first at **r=0.715**, while copper ranked below zinc and manganese (**r=0.545**) and above cobalt (**r=0.498**). [^counter_ion_effects] Copper's relatively high NaCl correlation is consistent with broad toxicity across multiple cellular systems, but this is an extrapolation from fitness-profile patterns rather than a direct biochemical measurement. [^counter_ion_effects]

## Cross-metal fitness evidence

The gene-resolution metal cross-resistance study **supports** a broadly positive shared metal-stress architecture involving copper: **98.1%** of gene-level fitness correlations were positive (**311/317**), and Cu-Zn, Cu-Fe, Co-Cu, and Cu-Ni associations had mean correlations of **r = 0.48** (**n = 16**), **r = 0.45** (**n = 7**), **r = 0.43** (**n = 24**), and **r = 0.43** (**n = 24**), respectively. [^metal_cross_resistance] This **refines** the copper–NaCl evidence because the shared response is not limited to a chloride comparison, although no copper-specific mechanism was established. [^metal_cross_resistance]

No metal pair showed systematically negative cross-resistance; cross-resistance was interpreted as a universal directional layer combined with chemistry-dependent magnitude, based on gene-level fitness correlations rather than direct biochemical measurements. [^metal_cross_resistance] The three-tier classification of general-stress, metal-shared, and metal-specific genes was made across metals rather than copper alone and does not replace copper-specific conservation analysis. [^metal_cross_resistance]

## Within-metal salt comparison

In *Pseudomonas syringae* RCH2 (psRCH2), copper was tested as CuCl₂ and CuSO₄. [^counter_ion_effects] The cross-salt fitness-profile correlation was **r=0.439**, versus within-replicate correlations of **r=0.720** for CuCl₂ and **r=0.859** for CuSO₄. [^counter_ion_effects]

CuSO₄ had a higher NaCl correlation than CuCl₂, **r=0.450** versus **r=0.212**, despite supplying no chloride. [^counter_ion_effects] This argues against chloride as the primary confound, but cannot isolate counter-ion effects because CuCl₂ was tested anaerobically and CuSO₄ aerobically. [^counter_ion_effects]

## Relation to atlas robustness and ecological breadth

The Pan-Bacterial Metal Fitness Atlas **supports** broadly conserved cellular functions among copper-associated fitness defects: among **2,139** copper-important genes, the core fraction was **0.867**, the core-fraction delta **+0.090**, with **OR=1.91** and **p=3.8e-27**. [^metal_fitness_atlas] Copper was tested across **23 organisms**, although exposure concentrations were not normalized by dose or tolerance threshold. [^metal_fitness_atlas]

The metal-specificity analysis **refines** this result: **1,346/2,594 (51.9%)** copper-important gene records were metal-specific under its threshold, showing significant metal fitness defects but a sick rate below 5% across non-metal experiments. [^metal_specificity] Thus copper-associated fitness includes broadly conserved or shared-stress functions and a substantial condition-specific component; this analysis covered 7,609 metal-important records across 24 organisms, not the full atlas set. [^metal_specificity]

After shared-stress genes were removed, copper's corrected Metal Fitness Atlas core-genome enrichment changed from **+0.090** to **+0.084**. [^counter_ion_effects] Core-genome enrichment was preserved for **12 of 14 metals**, supporting the conclusion that atlas-wide core enrichment was not attributable to shared NaCl-stress genes. [^counter_ion_effects] The atlas result **refines** this evidence because the uncorrected copper enrichment is also statistically strong at cross-species scale, while the two values address different gene sets. [^metal_fitness_atlas]

Metal-important genes overall were **87.4%** core versus **76.9%** for baseline genes (**OR=2.08, p=4.3e-162**) across **22 organisms and 14 metals**. [^metal_fitness_atlas] This **supports** a two-tier interpretation in which core general-stress functions dominate broad metal-fitness signals while accessory efflux, sequestration, and detoxification functions remain plausible specialized mechanisms. [^metal_fitness_atlas] Consistently, metal-specific genes were core-enriched but less so than general sick genes: pooled core fractions were **84.8% (2,969/3,500)** and **90.2% (2,183/2,420)**, respectively, with **p=0.011** between categories. [^metal_specificity]

The field-versus-lab DvH analysis **refines** the atlas result by placing copper in an aggregate heavy-metals category: heavy-metal-important genes had a **71.2%** core fraction versus a **76.3%** all-gene baseline, with **198** genes and **FDR q=0.14**. [^field_vs_lab_fitness] Because this aggregates cobalt, nickel, zinc, copper, manganese, selenium, molybdate, tungstate, and aluminum, it does not establish copper-specific conservation. [^field_vs_lab_fitness] The aggregate pattern **supports** the hypothesis that some efflux-pump and metal-binding functions may be accessory, without contradicting the conclusion that copper–NaCl overlap is not primarily chloride-driven. [^field_vs_lab_fitness]

The cross-resistance study found no association between multi-metal tolerance scores and BacDive metal-environment isolation at Fitness Browser species scale (**Spearman rho approximately -0.02, p > 0.8**); the matched analysis was underpowered, yielding **20 independent species** after strain collapsing. [^metal_cross_resistance] This **refines** the environmental interpretation: species-scale validation remains inconclusive rather than showing that cross-resistance lacks ecological relevance. [^metal_cross_resistance]

The MicrobeAtlas metal-ecology study **supports** a possible ecological link for copper as one component of genus-level metal-type diversity: across 606 genera, diversity across metal types predicted broader inferred niche breadth in phylogenetic generalized least-squares (PGLS; a model accounting for shared ancestry), whereas total AMR cluster count and core AMR fraction did not. [^microbeatlas_metal_ecology] However, the analysis did not isolate copper-specific effects; in leave-one-metal-out tests, excluding Cu retained a positive coefficient (**β = +0.0102, p = 0.115**) but was not significant, and reducing the maximum diversity score from 7 to 6 also reduced predictor variance and power. [^microbeatlas_metal_ecology] This **refines** the fitness evidence by making ecological generalism a hypothesis about repertoires spanning multiple metals, not evidence that copper alone causes habitat expansion. [^microbeatlas_metal_ecology]

The soil functional-genomics analysis **supports** an environmental association for copper at community gene-content scale: among 51,748 soil samples and nine metals, 2,355 significant COG–metal associations were identified at FDR < 0.05, with transporters such as ABC and RND systems and biosynthesis genes prominent among top hits. [^soil_metal_functional_genomics] In the copper-specific subset, 116 COGs were significant at FDR < 0.05 using 7,566 samples with nearby KBase genomes within 10 km; positive associations included cell-division and nucleotide-transport categories, while negative associations included energy-production categories, suggesting an observational energetic trade-off rather than demonstrating mechanism. [^soil_metal_functional_genomics] Biome-stratified PGLS found distinct metal–COG relationships in soil, marine, and wastewater environments, which **refines** the broader ecological-generalism hypothesis toward environment-specific responses rather than a universal copper-resistance programme. [^soil_metal_functional_genomics]

## Limitations and next tests

Copper's **41.0%** overlap is threshold-dependent because NaCl importance was defined as fit < -1 or n_sick ≥ 1. [^counter_ion_effects] NaCl is not a pure chloride control because it supplies both Na⁺ and Cl⁻ and produces osmotic effects. [^counter_ion_effects] Matched CuCl₂/CuSO₄ RB-TnSeq experiments under identical conditions are needed to isolate counter-ion effects. [^counter_ion_effects]

The copper-specific fraction is threshold- and coverage-dependent: the metal-specificity analysis used a 5% non-metal sick-rate threshold, excluded 40.7% of metal-important gene records because of locusId mismatches, and did not validate classifications against Fitness Browser `specificphenotype` annotations. [^metal_specificity] It therefore complements rather than replaces the atlas estimate. [^metal_specificity]

The soil associations **refine** but do not overturn the fitness-based evidence because co-contamination among chromium, copper, lead, and zinc may make apparent copper associations non-specific; the conditional db-RDA result was **R² = 0.799, p = 0.005** with **999 permutations**, and its unconditional metal-only R² was not reported. [^soil_metal_functional_genomics] Planned partial-correlation, effect-size, spatial-residual, and 5 km/20 km proximity sensitivity analyses are needed before interpreting these associations as copper-specific or biologically large. [^soil_metal_functional_genomics]

Copper-specific DvH fitness–conservation analysis, quantitative gene-cluster prevalence, and genomic-context analysis would test whether the aggregate heavy-metal pattern applies to copper resistance rather than other metals. [^field_vs_lab_fitness] Metal-concentration normalization relative to MIC, phylogenetic independent contrasts, and pangenome-scale validation are needed to distinguish universal stress responses from chemistry-specific copper effects. [^metal_cross_resistance] The atlas further recommends separating genes important for metals but not other stresses and testing regulatory or expression-based models after concentration-relative-to-MIC normalization. [^metal_fitness_atlas] Further work should resolve locusId mismatches and use concentration-normalized experiments to test whether copper-specific determinants remain specific across organisms. [^metal_specificity] The soil analysis additionally requires Spark access to rerun tables from `kescience_mgnify` and `kbase_ke_pangenome`, because no local Spearman-rho or residual files were available. [^soil_metal_functional_genomics]

Copper-related evidence connects to [condition-specific-fitness](../concepts/condition-specific-fitness.md), which synthesizes shared and condition-specific fitness responses, and [cofitness-network-architecture](../concepts/cofitness-network-architecture.md), which addresses cross-condition fitness-profile structure. [^counter_ion_effects] The findings also bear on [gene-essentiality](../concepts/gene-essentiality.md) because removal of shared-stress genes left the atlas core-enrichment conclusion robust. [^counter_ion_effects] Cross-metal correlations connect copper to [metal-cross-resistance](../concepts/metal-cross-resistance.md), which synthesizes universal directional cross-resistance and chemistry-dependent magnitude. [^metal_cross_resistance] The atlas evidence connects copper to [pangenome-integration](../concepts/pangenome-integration.md) through core/accessory conservation analysis. [^metal_fitness_atlas] The metal-specificity result additionally connects it to [condition-specific-fitness](../concepts/condition-specific-fitness.md) by separating copper-associated genes with metal-specific defects from broadly sick genes. [^metal_specificity]

The source analyses are summarized in [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md), [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md), [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md), [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md), [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md), [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md), and [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md). [^counter_ion_effects] [^field_vs_lab_fitness] [^metal_cross_resistance] [^metal_fitness_atlas] [^metal_specificity] [^microbeatlas_metal_ecology] [^soil_metal_functional_genomics]

[^counter_ion_effects]: [counter ion effects](../summaries/counter_ion_effects__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../summaries/metal_cross_resistance__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../summaries/microbeatlas_metal_ecology__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
