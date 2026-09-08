---
title: Context Dependence Versus Generality in Fitness and Functional Conservation
type: Conflict
sources:
- id: metabolic_capability_dependency
  resource: ../../wiki/summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: conservation_fitness_synthesis
  resource: ../../wiki/summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: essential_genome
  resource: ../../wiki/summaries/essential_genome__REPORT.md
  title: essential genome
- id: pathway_capability_dependency
  resource: ../../wiki/summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: metal_fitness_atlas
  resource: ../../wiki/summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: field_vs_lab_fitness
  resource: ../../wiki/summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: metal_specificity
  resource: ../../wiki/summaries/metal_specificity__REPORT.md
  title: metal specificity
- id: truly_dark_genes
  resource: ../../wiki/summaries/truly_dark_genes__REPORT.md
  title: truly dark genes
- id: plant_microbiome_ecotypes
  resource: ../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: snipe_defense_system
  resource: ../../wiki/summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
- id: respiratory_chain_wiring
  resource: ../../wiki/summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
- id: nmdc_community_metabolic_ecology
  resource: ../../wiki/summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
- id: pangenome_openness
  resource: ../../wiki/summaries/pangenome_openness__REPORT.md
  title: pangenome openness
- id: ibd_phage_targeting
  resource: ../../wiki/summaries/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
---
<!-- tension-hash: 16a40c98a4d16afe -->
# Context Dependence Versus Generality in Fitness and Functional Conservation

The corpus contains a recurring disagreement over whether conservation, essentiality, and environmental or stress-associated fitness effects generalize across organisms and conditions. Some analyses support broadly conserved functions, while others find weaker, condition-specific, or poorly reproducible associations. The distinction matters because genomic potential and comparative conservation may not predict measured fitness outside the tested taxa, media, or environments.

## Evidence Sides

**Conservation and essentiality are broadly associated.** Gene-level analyses associate essentiality and strong fitness effects with higher core fractions [^metabolic_capability_dependency] metabolic_capability_dependency; [^conservation_fitness_synthesis] conservation_fitness_synthesis; [^fitness_effects_conservation] fitness_effects_conservation; [^essential_genome] essential_genome. Only 15 essential families were essential in all 48 organisms, whereas 859 ortholog families were universally essential within every organism in which they occurred [^essential_genome] essential_genome.

**Pathway-level results weaken a simple conservation expectation.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, and the active-greater-than-latent comparison was not significant (p = 0.94) [^metabolic_capability_dependency] metabolic_capability_dependency; [^conservation_fitness_synthesis] conservation_fitness_synthesis; [^fitness_effects_conservation] fitness_effects_conservation; [^essential_genome] essential_genome. A new 7-organism analysis instead found mean core gene completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities [^pathway_capability_dependency] pathway_capability_dependency.

**Stress and metal signals are definition- and condition-dependent.** The metal atlas found 87.4% core among broad metal-important genes versus 76.9% baseline [^metal_fitness_atlas] metal_fitness_atlas, whereas a DvH condition-specific heavy-metal result found 71.2% core [^field_vs_lab_fitness] field_vs_lab_fitness. The metal-specificity analysis found 84.8% pooled core for metal-specific genes and 90.2% for general sick genes [^metal_specificity] metal_specificity. For truly dark genes, stress represented 28.7% versus 43.2% of strong phenotypes for truly dark versus annotation-lag genes (OR = 0.53, p < 0.001) [^truly_dark_genes] truly_dark_genes.

**Environmental and mechanistic generalization is modest.** In plant-versus-non-plant tests, 94.2% of 5,671 eggNOG ortholog groups were significant in raw tests, but only 50 retained enrichment after phylum-level control [^plant_microbiome_ecotypes] plant_microbiome_ecotypes. SNIPE found 22 of 64 AlphaEarth dimensions significant, with a largest Cohen’s d of 0.26 and geographic metadata for only 28.4% of genomes [^snipe_defense_system] snipe_defense_system. For respiratory wiring, 5 of 14 organisms had validated NDH-2; their mean Complex I aromatic deficit was −0.297 versus −0.156 without validated NDH-2; p = 0.52 [^respiratory_chain_wiring] respiratory_chain_wiring.

## Possible Reconciliations

- **Hypothesis—measurement layer:** genomic potential, pathway activity, gene essentiality, and measured fitness may capture distinct biological properties [^nmdc_community_metabolic_ecology] nmdc_community_metabolic_ecology.
- **Hypothesis—scope:** pathway variability may predict pangenome openness without reproducing broader environment or phylogeny relationships [^pathway_capability_dependency] pathway_capability_dependency; [^pangenome_openness] pangenome_openness.
- **Hypothesis—context:** media, dose, phylogeny, paralogs, and compensation may change apparent essentiality and respiratory dependence [^essential_genome] essential_genome; [^respiratory_chain_wiring] respiratory_chain_wiring.
- **Hypothesis—validation level:** within-pilot association may not equal cross-cohort reproducibility [^ibd_phage_targeting] ibd_phage_targeting.

## Resolving Work

- Reanalyze shared genomes using common definitions of active, latent, core, essential, and metal-specific functions; test whether activity predicts conservation after phylogenetic control.
- Construct matched metal and non-metal condition matrices with dose-relative-to-MIC normalization; test whether metal-specific core enrichment persists.
- Test matched dark and annotation-lag genes across the same condition matrix, controlling for length, insertion density, organism, and polar effects.
- Replicate respiratory-chain predictions with validated NDH-2 annotations, standardized media, measured flux, and phylogenetic contrasts.
- Use complete environmental and metabolite metadata with nested cross-cohort validation; test whether within-pilot associations reproduce across cohorts.

[^metabolic_capability_dependency]: [metabolic capability dependency](../../wiki/summaries/metabolic_capability_dependency__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../../wiki/summaries/conservation_fitness_synthesis__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^essential_genome]: [essential genome](../../wiki/summaries/essential_genome__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../../wiki/summaries/pathway_capability_dependency__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../../wiki/summaries/metal_fitness_atlas__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../../wiki/summaries/field_vs_lab_fitness__REPORT.md)
[^metal_specificity]: [metal specificity](../../wiki/summaries/metal_specificity__REPORT.md)
[^truly_dark_genes]: [truly dark genes](../../wiki/summaries/truly_dark_genes__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md)
[^snipe_defense_system]: [snipe defense system](../../wiki/summaries/snipe_defense_system__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../../wiki/summaries/respiratory_chain_wiring__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../../wiki/summaries/nmdc_community_metabolic_ecology__REPORT.md)
[^pangenome_openness]: [pangenome openness](../../wiki/summaries/pangenome_openness__REPORT.md)
[^ibd_phage_targeting]: [ibd phage targeting](../../wiki/summaries/ibd_phage_targeting__REPORT.md)
