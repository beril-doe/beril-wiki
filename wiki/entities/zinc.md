---
type: Compound
description: Zinc, a metal linked to shared stress, cross-resistance, and environmental
  gene shifts.
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
title: Zinc
---
# Zinc

## What this entity is

**Canonical name:** Zinc. [^counter_ion_effects]

**Known aliases:** No aliases were reported in this document. [^counter_ion_effects]

**Stable external identifier:** None was reported in this document. [^counter_ion_effects]

Zinc is evaluated as a metal condition in genome-wide fitness measurements and specifically discussed as zinc sulfate in the counter-ion analysis. [^counter_ion_effects]

## Key facts from counter-ion analysis

- Zinc sulfate delivered 0 mM chloride yet produced a 44.6% overlap between zinc-important genes and NaCl-important genes. [^counter_ion_effects]
- The 44.6% zinc–NaCl overlap exceeded the corresponding overlaps for cobalt at 41.3%, copper at 41.0%, and nickel at 39.3%, despite those metals being delivered in chloride-containing conditions. [^counter_ion_effects]
- Across metals, chloride-delivered conditions had a mean NaCl overlap of 41.6%, compared with 37.8% for non-chloride metals, so the zinc result did not support chloride dose as the primary driver of shared fitness signals. [^counter_ion_effects]
- In the DvH dataset, zinc had the highest whole-genome Pearson correlation with NaCl, r=0.715, despite zinc sulfate supplying zero chloride. [^counter_ion_effects]
- Zinc’s high NaCl correlation is consistent with broad toxicity involving essential-cofactor displacement or disruption of multiple cellular systems, but this is an extrapolation from the fitness-profile hierarchy rather than a direct biochemical test. [^counter_ion_effects]
- After shared-stress genes were removed, zinc’s corrected core-genome enrichment changed from +0.145 to +0.115. [^counter_ion_effects]
- This decrease did not overturn the broader conclusion that the Metal Fitness Atlas core-enrichment signal was robust after shared-stress correction. [^counter_ion_effects]

## Zinc specificity and cross-metal relationships

The metal-specificity analysis **refines** the shared-stress interpretation: 843 of 1,786 zinc-important gene records were classified as metal-specific, a fraction of 47.2%, because they showed significant metal fitness defects but a <5% sick rate across non-metal experiments. [^metal_specificity] Zinc therefore combines a substantial zinc-specific component with the broad NaCl-associated signal; the threshold is analysis-dependent and does not establish zinc-specific biochemical mechanisms. [^metal_specificity]

The metal cross-resistance analysis **supports** the existing interpretation of broad shared-stress biology. Zinc participated in positive gene-level fitness correlations across diverse organisms, with mean correlations of r = 0.61 for Fe–Zn (n = 6 organisms), r = 0.52 for Co–Zn (n = 18), r = 0.51 for Ni–Zn (n = 18), r = 0.48 for Cu–Zn (n = 16), and r = 0.44 for Al–Zn (n = 13). [^metal_cross_resistance] Across the study, 98.1% of 317 organism–metal pair observations had positive gene-level correlations, and all 15 metal pairs tested in at least 5 organisms showed greater than 90% sign consistency; these results indicate directional cross-resistance but do not establish zinc-specific biochemical mechanisms. [^metal_cross_resistance]

These cross-metal results **refine** the zinc–NaCl comparison: zinc’s strong association with several metals is consistent with a shared cellular stress component, while differences in pair magnitude suggest chemistry-dependent effects layered onto that common response. [^metal_cross_resistance] Because the analysis included no non-metal stress controls, it cannot distinguish universal metal cross-resistance from a general-stress response to all metals. [^metal_cross_resistance]

## Atlas-scale conservation context

The Pan-Bacterial Metal Fitness Atlas **supports** the interpretation that zinc fitness effects include broadly conserved cellular vulnerabilities rather than only accessory resistance functions. Across 22 organisms and 14 metals, metal-important genes were 87.4% core versus 76.9% for baseline genes (OR=2.08, p=4.3e-162). [^metal_fitness_atlas] Zinc specifically had 1,517 metal-important genes with a core fraction of 0.890, delta +0.151, OR=2.94, and p=2.0e-49, among the strongest per-metal core enrichments reported. [^metal_fitness_atlas]

The metal-specificity analysis **refines** this conservation model: metal-specific genes had a pooled core fraction of 84.8% (2,969/3,500), with a mean delta versus baseline of +6.9%, whereas general sick genes had a pooled core fraction of 90.2% (2,183/2,420). [^metal_specificity] Across organisms, the comparison between these categories was significant (Cochran-Mantel-Haenszel p=0.011), supporting a two-tier model in which broadly stressful functions are more core-enriched than specialized metal-resistance functions, although both remain strongly core-associated. [^metal_specificity]

This atlas result **refines** the earlier grouped heavy-metal finding rather than replacing it: the field-versus-lab analysis placed zinc among heavy-metal conditions in which 71.2% of 198 genes important at fitness < -2 were core (OR=0.77 versus baseline, FDR q=0.14), whereas the atlas used a broader genome-wide definition and found stronger core enrichment. [^field_vs_lab_fitness] The difference is consistent with condition-definition effects: broad zinc-associated fitness defects capture general cellular processes, while stricter or grouped heavy-metal analyses can emphasize less-conserved functions. [^field_vs_lab_fitness]

The atlas proposes a two-tier interpretation: zinc-associated fitness defects may include core general-stress functions, while specialized accessory mechanisms such as efflux, sequestration, and enzymatic detoxification remain a separate resistance tier. [^metal_fitness_atlas] This is a model inferred from cross-species fitness and pangenome data, not a zinc-specific biochemical demonstration. Zinc was tested across 17 organisms in the atlas, but metal exposure concentrations were not normalized by dose or tolerance threshold, limiting direct comparisons among organisms. [^metal_fitness_atlas]

## Field-versus-lab conservation context

The field-versus-lab analysis **refines** the counter-ion results by grouping zinc with heavy-metal conditions rather than reporting zinc separately: the heavy-metals category included cobalt, nickel, zinc, copper, manganese, selenium, molybdate, tungstate, and aluminum. [^field_vs_lab_fitness] Among 198 genes important at fitness < -2 in heavy-metal conditions, 71.2% were core (OR=0.77 versus baseline, FDR q=0.14), below the 76.3% all-gene baseline but not significantly so after BH-FDR correction. [^field_vs_lab_fitness] This grouped result **supports** the interpretation that metal-associated fitness signals can include comparatively less-conserved functions, but it does not establish a zinc-specific conservation pattern. [^field_vs_lab_fitness]

## Environmental resistance ecology

The MicrobeAtlas metal-ecology analysis **extends** zinc’s cross-metal context from laboratory fitness to genus-level environmental distributions. Across 606 bacterial genera, metal type diversity—not total AMR cluster count or core AMR fraction—was positively associated with inferred niche breadth after phylogenetic correction (PGLS β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴); the study is correlational and does not establish that zinc resistance causes ecological generalism. [^microbeatlas_metal_ecology] Zinc was one of the seven metal types in the analysis, and excluding Zn retained a positive but non-significant association (β = +0.003, p = 0.518), which **supports** a distributed cross-metal signal rather than a result driven solely by zinc, while also reflecting reduced predictor variance and power. [^microbeatlas_metal_ecology]

The environmental result **refines** the fitness-based interpretation: metal-resistance breadth may track ecological breadth, but MicrobeAtlas niche breadth is a sequencing-effort proxy affected by sampling, primer, geographic, and temporal biases, and genus aggregation can combine different species’ habitats. [^microbeatlas_metal_ecology] Independent groundwater data showed a positive association between metal type diversity and groundwater prevalence (Spearman ρ = +0.112, p = 0.0019), but not groundwater-specific fold enrichment (ρ = +0.042, p = 0.242), so the evidence does not identify a zinc-specific environmental mechanism. [^microbeatlas_metal_ecology]

The soil functional-genomics analysis **supports** an environmental link between zinc and microbial gene content but **refines** the resistance interpretation: across 51,748 soil samples and nine metals, 2,355 significant COG–metal associations were detected at FDR < 0.05, with transporters including ABC and RND systems and biosynthesis genes among the dominant hits. COG means Cluster of Orthologous Groups, and FDR means false discovery rate. [^soil_metal_functional_genomics] Chromium and lead produced the strongest signals, so the result does not establish that zinc was a dominant driver. [^soil_metal_functional_genomics] The association set is especially vulnerable to co-contamination because chromium, copper, lead, and zinc co-vary in many industrial soils; whether zinc-associated COGs are zinc-specific or reflect multi-metal stress remains unresolved. [^soil_metal_functional_genomics]

In the copper-specific subset, 116 COGs were significant at FDR < 0.05 among 7,566 samples matched to nearby KBase genomes within 10 km; the strongest positive categories included cell division and nucleotide transport, while energy-production categories were negative. [^soil_metal_functional_genomics] This **refines** the laboratory two-tier model by suggesting energetic trade-offs under metal exposure, but the observation is not zinc-specific and remains unvalidated. [^soil_metal_functional_genomics] A conditional db-RDA model explained R² = 0.799 with p = 0.005 using 999 permutations after conditioning on batch and project effects; this value describes residual variance and cannot be treated as unconditional variance explained by zinc or metals generally. [^soil_metal_functional_genomics]

Biome-stratified PGLS found distinct metal–COG relationships in soil, marine, and wastewater environments, **supporting** environment-dependent rather than universal functional responses. [^soil_metal_functional_genomics] Planned partial-correlation, effect-size, spatial-autocorrelation, unconditional-db-RDA, and 5 km/20 km proximity-sensitivity analyses are needed before these associations can be assigned to zinc-specific mechanisms. [^soil_metal_functional_genomics]

## Interpretation and limitations

Zinc–NaCl overlap is consistent with substantial shared-stress biology, but the zero-chloride zinc sulfate result argues against attributing that overlap primarily to chloride contamination. [^counter_ion_effects]

NaCl is not a pure chloride control because it supplies both sodium and chloride and produces osmotic stress, so the zinc comparison cannot isolate chloride-specific effects. [^counter_ion_effects]

The report proposes matched ZnCl₂/ZnSO₄ RB-TnSeq experiments under identical conditions to test counter-ion effects more directly. [^counter_ion_effects]

The heavy-metal result is a grouped, single-organism DvH analysis, so it cannot determine whether zinc-specific resistance mechanisms are accessory or whether zinc directly explains the observed conservation value. [^field_vs_lab_fitness]

The 47.2% zinc-specific fraction depends on a 5% sick-rate threshold; the metal-specificity analysis found qualitatively stable results across 1–20% thresholds, but exact fractions varied. [^metal_specificity] Its zinc estimate also belongs to the subset of organisms whose locus identifiers matched the fitness-matrix format, so excluded records may have different specificity profiles. [^metal_specificity]

The cross-resistance estimates may be influenced by differing metal concentrations and unequal numbers of experiments per organism; phylogenetically comparative analyses and concentration normalization would strengthen the conservation claim. [^metal_cross_resistance]

The atlas likewise recommends concentration-relative-to-MIC normalization, phylogenetic independent contrasts, and analysis restricted to genes important for metals but not for other stresses to distinguish zinc-specific resistance from general stress. [^metal_fitness_atlas]

The MicrobeAtlas association is further limited by uneven pangenome coverage, heterogeneous environment categories, genus-level aggregation, and AMRFinderPlus annotation uncertainty; the strict 5% prevalence analysis retained a positive but non-significant coefficient (β = +0.0166, SE = 0.0099, p = 0.092). [^microbeatlas_metal_ecology] Follow-up work should validate annotations, rarefy genomes across species-per-genus thresholds, subdivide aquatic environments, and test alternative phylogenetic models. [^microbeatlas_metal_ecology]

The soil associations are preliminary: effect sizes and spatial validation remain pending, the 2,355 discoveries may have an inflated true FDR because co-contaminating metals make tests non-independent, and no local Spearman-rho or residual files are available for validation without Spark access. [^soil_metal_functional_genomics] The planned analyses include partial correlation of COG ~ Cr | Cu + Zn + Pb, mechanistic classification of significant COGs, Moran’s I with SEVM if needed, unconditional db-RDA R², and copper matching at 5 km and 20 km. [^soil_metal_functional_genomics]

## Related pages

- [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md) — source summary for the counter-ion analysis. [^counter_ion_effects]
- [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) — source summary for field-versus-lab fitness and pangenome conservation. [^field_vs_lab_fitness]
- [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md) — source summary for gene-resolution metal cross-resistance. [^metal_cross_resistance]
- [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) — source summary for the cross-species metal fitness atlas. [^metal_fitness_atlas]
- [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) — source summary for metal-specific versus general stress genes. [^metal_specificity]
- [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md) — source summary for phylogenetic and environmental metal-resistance ecology. [^microbeatlas_metal_ecology]
- [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md) — source summary for soil metal–functional-gene associations. [^soil_metal_functional_genomics]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — shared and metal-specific condition responses in fitness profiles. [^counter_ion_effects]
- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — conserved positive cross-metal fitness relationships involving zinc. [^metal_cross_resistance]
- [gene-essentiality](../concepts/gene-essentiality.md) — persistence of core-genome enrichment after shared-stress correction. [^counter_ion_effects]
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — cross-condition correlations between zinc and NaCl fitness profiles. [^counter_ion_effects]
- [pangenome-integration](../concepts/pangenome-integration.md) — core-versus-accessory conservation of zinc-associated fitness genes. [^metal_fitness_atlas]
- [sodium-chloride](sodium-chloride.md) — the comparator condition used for the overlap and correlation analyses. [^counter_ion_effects]

[^counter_ion_effects]: [counter ion effects](../summaries/counter_ion_effects__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../summaries/metal_cross_resistance__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../summaries/microbeatlas_metal_ecology__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
