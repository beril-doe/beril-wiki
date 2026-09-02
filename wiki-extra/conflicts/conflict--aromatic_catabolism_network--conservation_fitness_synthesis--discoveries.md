<!-- tension-hash: 16a40c98a4d16afe -->
# Context-Dependence Complicates Conservation, Environmental Structure, and Fitness Inference

The corpus contains several related disagreements over whether genomic conservation, pathway activity, environmental association, and measured fitness can be interpreted as general properties. Some analyses support simple conservation or environmental-structure expectations, while others find weaker, context-specific, or poorly reproducible effects. The tensions matter because they determine whether observed associations reflect biology, measurement scope, model assumptions, or cohort-specific structure.

## Evidence Sides

**Conservation and essentiality favor higher core fractions.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, and active-greater-than-latent comparison was not significant (p = 0.94), whereas gene-level analyses associate essentiality and strong fitness effects with higher core fractions. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome] ([[concepts/metabolic_capability_dependency]]; [[concepts/conservation_fitness_synthesis]]; [[concepts/fitness_effects_conservation]]; [[concepts/essential_genome]]) The new 7-organism analysis instead found mean core gene completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities. [src: pathway_capability_dependency] ([[concepts/pathway_capability_dependency]])

**Environmental and metal associations are narrower or inconsistent.** Variable pathway count was positively associated with pangenome openness after genome-count control (rho=0.530, p=2.83e-203), while broader pangenome analyses reported null relationships between openness and environment or phylogeny effect sizes. [src: pathway_capability_dependency; pangenome_openness] ([[concepts/pathway_capability_dependency]]; [[concepts/pangenome_openness]]) The metal atlas found 87.4% core among broad metal-important genes versus 76.9% baseline, whereas the DvH condition-specific heavy-metal result found 71.2% core. The metal-specificity analysis found 84.8% pooled core for metal-specific genes and 90.2% for general sick genes. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity] ([[concepts/metal_fitness_atlas]]; [[concepts/field_vs_lab_fitness]]; [[concepts/metal_specificity]])

**Environmental structure can be statistically detectable but modest.** Stress represented 28.7% versus 43.2% of strong phenotypes for truly dark versus annotation-lag genes (OR = 0.53, p < 0.001), although truly dark genes became important in selected nutrient, stress, iron, community, or rich-media contexts. [src: truly_dark_genes] ([[concepts/truly_dark_genes]]) In plant comparisons, 94.2% of 5,671 eggNOG ortholog groups were significant before control, but only 50 retained enrichment after phylum-level control; compartment separation explained 6.0% of variance, and 78.7% refined dual-nature classification conflicted with four-of-four neutral-control failures. [src: plant_microbiome_ecotypes] ([[concepts/plant_microbiome_ecotypes]]) SNIPE found 22 of 64 AlphaEarth dimensions significant, but the largest Cohen’s d was 0.26 and geographic metadata covered only 28.4% of genomes. [src: snipe_defense_system] ([[concepts/snipe_defense_system]])

**Modeling and reproducibility qualify mechanistic conclusions.** The cross-species test found 5 of 14 organisms with validated NDH-2, whose mean Complex I aromatic deficit was −0.297 versus −0.156 without validated NDH-2; p = 0.52, with only 4 organisms lacking NDH-2. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring] ([[concepts/aromatic_catabolism_network]]; [[concepts/discoveries]]; [[concepts/respiratory_chain_wiring]]) Only 15 essential families were essential in all 48 organisms, whereas 859 ortholog families were universally essential within every organism in which they occurred. [src: essential_genome] ([[concepts/essential_genome]]) The IBD within-pilot taxonomy–metabolite CCA axis had r=0.964, versus pooled metabolomics cross-cohort LOSO ARI=0.000 and ecotype mean LOSO ARI=0.113. [src: ibd_phage_targeting] ([[concepts/ibd_phage_targeting]])

## Possible Reconciliations

- **Hypothesis—scope:** pathway, gene, metal-specific, and general-stress analyses measure different biological scopes.
- **Hypothesis—definition:** “core,” “active,” “dark,” and “essential” classifications are not interchangeable.
- **Hypothesis—cohort and method:** near-complete model genomes, phylogenetic structure, annotation error, and within-pilot versus cross-cohort validation may explain divergent effect sizes.
- **Hypothesis—mechanism:** species-specific wiring and compensatory pathways may produce real context dependence rather than a universal rule.

## Resolving Work

- Reanalyze matched genomes with shared core, activity, essentiality, and metal-specific definitions.
- Test matched dark and annotation-lag genes across the same condition matrix, controlling for length, insertion density, organism, and polar effects.
- Apply phylogenetic independent contrasts and cross-cohort validation to pathway openness, environmental associations, and fitness effects.
- Normalize metal exposures to dose-relative-to-MIC and include non-metal controls.
- Validate NDH-2, pathway flux, and essentiality experimentally across more organisms and media.
