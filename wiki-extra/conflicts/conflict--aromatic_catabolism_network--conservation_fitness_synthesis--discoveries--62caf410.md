<!-- tension-hash: 16a40c98a4d16afe -->
# Context Dependence Versus Generality in Fitness and Functional Conservation

The corpus contains a recurring disagreement over whether conservation, essentiality, and environmental or stress-associated fitness effects generalize across organisms and conditions. Some analyses support broadly conserved functions, while others find weaker, condition-specific, or poorly reproducible associations. The distinction matters because genomic potential and comparative conservation may not predict measured fitness outside the tested taxa, media, or environments.

## Evidence Sides

**Conservation and essentiality are broadly associated.** Gene-level analyses associate essentiality and strong fitness effects with higher core fractions [src: metabolic_capability_dependency] metabolic_capability_dependency; [src: conservation_fitness_synthesis] conservation_fitness_synthesis; [src: fitness_effects_conservation] fitness_effects_conservation; [src: essential_genome] essential_genome. Only 15 essential families were essential in all 48 organisms, whereas 859 ortholog families were universally essential within every organism in which they occurred [src: essential_genome] essential_genome.

**Pathway-level results weaken a simple conservation expectation.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, and the active-greater-than-latent comparison was not significant (p = 0.94) [src: metabolic_capability_dependency] metabolic_capability_dependency; [src: conservation_fitness_synthesis] conservation_fitness_synthesis; [src: fitness_effects_conservation] fitness_effects_conservation; [src: essential_genome] essential_genome. A new 7-organism analysis instead found mean core gene completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities [src: pathway_capability_dependency] pathway_capability_dependency.

**Stress and metal signals are definition- and condition-dependent.** The metal atlas found 87.4% core among broad metal-important genes versus 76.9% baseline [src: metal_fitness_atlas] metal_fitness_atlas, whereas a DvH condition-specific heavy-metal result found 71.2% core [src: field_vs_lab_fitness] field_vs_lab_fitness. The metal-specificity analysis found 84.8% pooled core for metal-specific genes and 90.2% for general sick genes [src: metal_specificity] metal_specificity. For truly dark genes, stress represented 28.7% versus 43.2% of strong phenotypes for truly dark versus annotation-lag genes (OR = 0.53, p < 0.001) [src: truly_dark_genes] truly_dark_genes.

**Environmental and mechanistic generalization is modest.** In plant-versus-non-plant tests, 94.2% of 5,671 eggNOG ortholog groups were significant in raw tests, but only 50 retained enrichment after phylum-level control [src: plant_microbiome_ecotypes] plant_microbiome_ecotypes. SNIPE found 22 of 64 AlphaEarth dimensions significant, with a largest Cohen’s d of 0.26 and geographic metadata for only 28.4% of genomes [src: snipe_defense_system] snipe_defense_system. For respiratory wiring, 5 of 14 organisms had validated NDH-2; their mean Complex I aromatic deficit was −0.297 versus −0.156 without validated NDH-2; p = 0.52 [src: respiratory_chain_wiring] respiratory_chain_wiring.

## Possible Reconciliations

- **Hypothesis—measurement layer:** genomic potential, pathway activity, gene essentiality, and measured fitness may capture distinct biological properties [src: nmdc_community_metabolic_ecology] nmdc_community_metabolic_ecology.
- **Hypothesis—scope:** pathway variability may predict pangenome openness without reproducing broader environment or phylogeny relationships [src: pathway_capability_dependency] pathway_capability_dependency; [src: pangenome_openness] pangenome_openness.
- **Hypothesis—context:** media, dose, phylogeny, paralogs, and compensation may change apparent essentiality and respiratory dependence [src: essential_genome] essential_genome; [src: respiratory_chain_wiring] respiratory_chain_wiring.
- **Hypothesis—validation level:** within-pilot association may not equal cross-cohort reproducibility [src: ibd_phage_targeting] ibd_phage_targeting.

## Resolving Work

- Reanalyze shared genomes using common definitions of active, latent, core, essential, and metal-specific functions; test whether activity predicts conservation after phylogenetic control.
- Construct matched metal and non-metal condition matrices with dose-relative-to-MIC normalization; test whether metal-specific core enrichment persists.
- Test matched dark and annotation-lag genes across the same condition matrix, controlling for length, insertion density, organism, and polar effects.
- Replicate respiratory-chain predictions with validated NDH-2 annotations, standardized media, measured flux, and phylogenetic contrasts.
- Use complete environmental and metabolite metadata with nested cross-cohort validation; test whether within-pilot associations reproduce across cohorts.
