<!-- tension-hash: 01fcee6705e4ec70 -->
# Broad Environmental Null vs Subsystem-Specific Environmental Signals

The central disagreement is whether environment has little relationship to microbial gene content overall, or whether broad null results conceal strong effects confined to particular functional systems, lineages, compartments, or environmental variables. The distinction matters because a whole-genome similarity measure may miss ecologically important pathway, prophage, metal-response, or plant-interaction changes. The [[concepts/ecotype-environment-gene-content]] synthesis therefore asks whether reported exceptions are genuine subsystem-level effects or structured confounding.

## Evidence Sides

**Broad gene-content and comparative analyses find weak or null environmental effects.** The ecotype reanalysis found environmental median partial correlation 0.051 versus human-associated 0.084 (U=1536, p=0.83), and the prior AlphaEarth-based analysis reported median partial correlation 0.0025. [src: ecotype_env_reanalysis] Openness did not predict environment or phylogeny effect sizes (rho = -0.05 and 0.03; p-values 0.54 and 0.73). [src: pangenome_openness] MicrobeAtlas’s strict prevalence analysis was non-significant at p = 0.092. [src: microbeatlas_metal_ecology] At the conservation level, active mean conservation was 0.829 versus latent 0.869, p = 0.94. [src: metabolic_capability_dependency] Species-level environmental comparison was null despite Harvard Forest treatment × horizon explaining 41% of genus-level variance. [src: harvard_forest_warming; ecotype_env_reanalysis]

**Specific functions, lineages, and compartments show environmental or ecological signals.** Prophage modules showed environment effects after genome-size and host-family controls, with environment F=30.04 versus phylogeny F=6.17 and significant within-quartile tests. [src: prophage_ecology] Soil-metal analysis found 2,355 significant COG–metal associations and a conditional db-RDA R² = 0.799. [src: soil_metal_functional_genomics] Carbon profiles were associated with environment among 54 free-living and plant-associated species (permutation p = 0.006), although classifier balanced accuracy was only 0.408 +/- 0.169. [src: pseudomonas_carbon_ecology] AlphaEarth showed a 3.4x environmental geographic gradient. [src: env_embedding_explorer] Refined plant-marker profiles differed by compartment at PERMANOVA R² = 0.071 and db-RDA R² = 0.060. [src: plant_microbiome_ecotypes] Latent capability rate correlated with openness (ρ = 0.69, p = 0.0004, n = 22), and variable pathway count correlated with openness (partial rho=0.530, p=2.83e-203). [src: metabolic_capability_dependency; pathway_capability_dependency] Soil enriched acdS, pqqC, and hcnC and depleted nifH, while NMDC found Soil and Freshwater pathway separation (median PC1 +3.86 versus −6.28). [src: pgp_pangenome_ecology; nmdc_community_metabolic_ecology]

## Possible Reconciliations

- **Hypothesis — feature-space difference:** broad gene-content similarity, pathway completeness, prophage modules, COG profiles, and embeddings may measure different biological phenomena.
- **Hypothesis — phylogenetic or sampling structure:** the *Pseudomonas* separation, plant-compartment effect, and metal associations may reflect lineage, genome size, co-contamination, or spatial mismatch rather than environment itself.
- **Hypothesis — scale and response differences:** treatment-by-horizon effects, niche breadth, and pathway-level responses may exist without producing a detectable species-level whole-genome signal.
- **Hypothesis — core versus mobilome biology:** beneficial plant-interaction clusters were 64.6% core versus 45.2% for pathogenic clusters, while plant-associated genera had median mobilome burden 3.7 versus 2.8 mobile elements per genome. [src: plant_microbiome_ecotypes]

## Resolving Work

- Assemble matched species and samples with common environmental metadata; test broad gene content, pathways, prophage modules, and COGs in the same multivariate model.
- Use variance partitioning and phylogenetically informed permutations to separate environment, host family, genome size, geography, and taxonomic sampling.
- Apply partial correlations and multivariable metal models to distinguish chromium, copper, lead, and zinc effects from co-varying contamination.
- Compare effect sizes and power across whole-genome, pathway, mobilome, and embedding distances to determine whether subsystem signals persist after harmonization.
