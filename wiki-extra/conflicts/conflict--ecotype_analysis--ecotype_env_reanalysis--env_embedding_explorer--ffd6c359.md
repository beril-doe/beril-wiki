---
title: Environmental association is detectable, but its magnitude and attribution
  remain disputed
type: Conflict
sources:
- id: env_embedding_explorer
  resource: ../../wiki/summaries/env_embedding_explorer__REPORT.md
  title: env embedding explorer
- id: ecotype_env_reanalysis
  resource: ../../wiki/summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
- id: pseudomonas_carbon_ecology
  resource: ../../wiki/summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
- id: soil_metal_functional_genomics
  resource: ../../wiki/summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
- id: microbeatlas_metal_ecology
  resource: ../../wiki/summaries/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
- id: ecotype_analysis
  resource: ../../wiki/summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: phb_granule_ecology
  resource: ../../wiki/summaries/phb_granule_ecology__REPORT.md
  title: phb granule ecology
- id: plant_microbiome_ecotypes
  resource: ../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: soil_frontier_genomics
  resource: ../../wiki/summaries/soil_frontier_genomics__REPORT.md
  title: soil frontier genomics
- id: snipe_defense_system
  resource: ../../wiki/summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
- id: pitfalls
  resource: ../../wiki/summaries/pitfalls.md
  title: pitfalls
- id: prophage_ecology
  resource: ../../wiki/summaries/prophage_ecology__REPORT.md
  title: prophage ecology
---
<!-- tension-hash: 24b2cb7583cf0497 -->
# Environmental association is detectable, but its magnitude and attribution remain disputed

The disagreement concerns whether environmental and geographic structure explains microbial gene content and ecological traits, or whether apparent associations mainly reflect genome composition, sampling structure, and measurement choices. The conflict on [environment-embedding-geography](../../wiki/concepts/environment-embedding-geography.md) matters because the studies detect environmental patterning but disagree about its size, generality, and causal interpretation.

## Evidence Sides

**Environmental and geographic structure is detectable.** Embeddings show clear geographic distance-decay, while the environmental-only reanalysis found median partial correlation 0.051 versus 0.084 for human-associated species, U=1536, p=0.83. [^env_embedding_explorer][^ecotype_env_reanalysis] Pseudomonas carbon profiles were environmentally associated (p=0.006). [^pseudomonas_carbon_ecology] Conditional soil-metal db-RDA reported R²=0.799, p=0.005. [^soil_metal_functional_genomics] MicrobeAtlas produced β=+0.021, p=1.5×10^-4. [^microbeatlas_metal_ecology]

**The estimated environmental effect is small or unstable.** Environment similarity had median partial correlation 0.0025 with gene content; the ecotype analysis found environmental median 0.0025 and phylogenetic median 0.0143. [^env_embedding_explorer][^ecotype_analysis] The original environment measure had median 0.0025, compared with 0.081 across all 183 species in the reanalysis. [^ecotype_analysis][^ecotype_env_reanalysis] These estimates cannot be reconciled by averaging because the studies used different genome sets, species filters, and downsampling. [^ecotype_env_reanalysis][^env_embedding_explorer]

**Associations can weaken or reverse after controls.** Pseudomonas carbon classification had balanced accuracy 0.408 +/- 0.169, and PCA primarily separated Pseudomonas s.s. from Pseudomonas_E. [^pseudomonas_carbon_ecology] PHB had raw breadth association rho=0.106, p=1.77×10^-06, but genome-size-controlled partial rho=-0.047, p=0.037. [^phb_granule_ecology] Plant-compartment PERMANOVA had refined R²=0.071, while an earlier R²=0.527 collapsed to 0.072 after removing genome-rich species. [^plant_microbiome_ecotypes] Strict MicrobeAtlas prevalence gave p=0.092, and groundwater-specific fold enrichment was null (rho=+0.042, p=0.242). [^microbeatlas_metal_ecology]

**Causal and predictive interpretations remain under-validated.** Metal variables co-vary, the 60% discovery rate may be inflated by correlated tests, and proximity within 10 km does not guarantee co-location; unconditional metal-only R² was not reported. [^soil_metal_functional_genomics] Soil-frontier models all had negative out-of-sample R², with a low- versus high-clay difference of 0.024 and 95% CI [-0.423, 0.161]. [^soil_frontier_genomics] SNIPE was statistically detectable in 22/64 AlphaEarth dimensions, but its largest effect was d=0.26 and AlphaEarth covered only 28.4% of genomes. [^snipe_defense_system] Held-out-species Jaccard values were 0.230 for E1 and 0.064 for E3; independent within-substudy evidence reduced the list to 3 candidates. [^pitfalls]

## Possible Reconciliations

- **Hypothesis—measurement differences:** Different genome sets, species filters, full-genome extraction, and downsampling procedures could produce different effect-size medians without requiring contradictory biology. [^ecotype_env_reanalysis][^env_embedding_explorer]
- **Hypothesis—scope differences:** Distance-decay may reflect environmental context, epidemiological structure, institutional clustering, or approximate coordinates rather than environment alone. [^env_embedding_explorer][^ecotype_env_reanalysis]
- **Hypothesis—conditional effects:** Apparent environmental associations may be mediated by genome size, species composition, correlated metals, or prevalence.
- **Hypothesis—feature validity:** Annotation-based calls, genus-inferred burden, incomplete embeddings, and dimensions without biological interpretation may limit ecological conclusions. [^prophage_ecology][^snipe_defense_system]

## Resolving Work

- Reanalyze the same genomes using harmonized species filters, full-genome extraction, and downsampling; test whether the reported partial-correlation medians persist.
- Fit spatially blocked models that jointly control for geographic distance, phylogeny, genome size, sampling structure, and environmental similarity.
- Report unconditional and conditional metal models, correct for correlated tests, and use verified co-location data to test attribution.
- Evaluate environmental classifiers and ecotype lists on held-out species and independent sites, separating prediction failure from distributional shift.
- Replicate the strongest trait associations after genome-size and species-composition controls, asking whether their signs and effect sizes remain stable.

[^env_embedding_explorer]: [env embedding explorer](../../wiki/summaries/env_embedding_explorer__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../../wiki/summaries/ecotype_env_reanalysis__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../../wiki/summaries/pseudomonas_carbon_ecology__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../../wiki/summaries/soil_metal_functional_genomics__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../../wiki/summaries/microbeatlas_metal_ecology__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../../wiki/summaries/ecotype_analysis__REPORT.md)
[^phb_granule_ecology]: [phb granule ecology](../../wiki/summaries/phb_granule_ecology__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md)
[^soil_frontier_genomics]: [soil frontier genomics](../../wiki/summaries/soil_frontier_genomics__REPORT.md)
[^snipe_defense_system]: [snipe defense system](../../wiki/summaries/snipe_defense_system__REPORT.md)
[^pitfalls]: [pitfalls](../../wiki/summaries/pitfalls.md)
[^prophage_ecology]: [prophage ecology](../../wiki/summaries/prophage_ecology__REPORT.md)
