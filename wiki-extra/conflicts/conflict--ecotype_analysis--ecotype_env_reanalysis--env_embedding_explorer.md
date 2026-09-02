<!-- tension-hash: 882e35637190c0fc -->
# Ecological Signal or Analytical Artifact?

The corpus repeatedly finds ecological, geographic, and functional structure, but disagrees about how strong, general, and causally interpretable those signals are. The central tension is whether observed associations reflect biology—or instead genome-set construction, taxonomy, coverage, spatial confounding, correlated tests, annotation, or weak validation. This conflict links the environmental-embedding results in [[concepts/environment-embedding-geography]] to broader disagreements over ecological prediction and functional interpretation.

## Evidence Sides

### **Side A: Environmental and geographic structure is detectable**

Embeddings show clear geographic distance-decay, while the environmental-only reanalysis found median 0.051 versus 0.084 for human-associated species, U=1536, p=0.83. [src: env_embedding_explorer] [src: ecotype_env_reanalysis] Pseudomonas carbon profiles were environmentally associated (p=0.006). [src: pseudomonas_carbon_ecology] Soil-metal models found conditional db-RDA R²=0.799, p=0.005. [src: soil_metal_functional_genomics] MicrobeAtlas produced β=+0.021, p=1.5×10^-4. [src: microbeatlas_metal_ecology] Prophage module effects remained significant within genome-size quartiles, and plant-associated mobilome burden was higher (3.7 versus 2.8). [src: prophage_ecology] [src: plant_microbiome_ecotypes]

### **Side B: The apparent signal is weak, unstable, or confounded**

Environment similarity had median partial correlation 0.0025 with gene content; the ecotype analysis found environmental median 0.0025 and phylogenetic median 0.0143. [src: env_embedding_explorer] [src: ecotype_analysis] These estimates cannot be reconciled by averaging because the reanalysis used all embedded genomes, up to 3,505 per species, whereas the original used diversity-maximized samples with a maximum of 250. [src: ecotype_env_reanalysis] Carbon classification had balanced accuracy 0.408 +/- 0.169, with PCA primarily separating Pseudomonas s.s. from Pseudomonas_E. [src: pseudomonas_carbon_ecology] PHB breadth changed from rho=0.106, p=1.77×10^-06 to genome-size-controlled partial rho=-0.047, p=0.037. [src: phb_granule_ecology] Conditional metal association lacks reported unconditional metal-only R²; metals co-vary, and proximity within 10 km does not guarantee co-location. [src: soil_metal_functional_genomics] Strict prevalence gave p=0.092, and groundwater-specific fold enrichment was null (rho=+0.042, p=0.242). [src: microbeatlas_metal_ecology]

### **Side C: Validation supports broad ecological interpretation**

SNIPE was statistically detectable in 22/64 AlphaEarth dimensions, and its 86.7% accessory-plus-singleton distribution supports mobile defense-island turnover. [src: snipe_defense_system] Forest GDI=902.36 and cropland GDI=890.82 were jointly highest. [src: soil_frontier_genomics]

### **Side D: Validation limits those interpretations**

AlphaEarth’s largest SNIPE effect was d=0.26, it covered only 28.4% of genomes, and no dimension had a biological interpretation; only 54/4,572 DUF4041 clusters carried Mug113. [src: snipe_defense_system] Soil-frontier models had negative out-of-sample R², and the low- versus high-clay difference was 0.024 with 95% CI [-0.423, 0.161]. [src: soil_frontier_genomics] Held-out-species Jaccard values were 0.230 for E1 and 0.064 for E3; independent validation reduced the list to 3 candidates. [src: pitfalls]

## Possible Reconciliations

- **Hypothesis—sampling scope:** genome-set composition, species filters, and downsampling may explain why environmental medians differ without requiring contradictory biology.
- **Hypothesis—measurement coverage:** env_broad_scale covers 42%, while keyword isolation_source covers 71% of genomes with a label but leaves 17% Other and 12.5% Unknown; precision and coverage may alter category balance.
- **Hypothesis—confounding:** geography may encode environmental context, epidemiological structure, institutional clustering, or approximate coordinates; genome size, taxonomy, and correlated metals may similarly generate apparent associations.
- **Hypothesis—scale and definition:** modular mobile-element turnover, complete-lineage adaptation, laboratory tolerance, field abundance, and predictive generalization may be distinct claims rather than interchangeable evidence.

## Resolving Work

- Reanalyze identical genome sets with matched species filters and maximum sample sizes; test whether environmental median correlations remain different.
- Fit spatially blocked, genome-size- and phylogeny-controlled models; compare geographic, environmental, epidemiological, and institutional predictors.
- Report unconditional and conditional metal models with collinearity diagnostics and true co-location metadata; test whether metal effects persist.
- Repeat ecological classifications on held-out species and independent cohorts, reporting calibration, balanced accuracy, Jaccard stability, and biological interpretation.
- Separate annotation-based calls from experimentally validated functions and test whether signals predict new samples rather than only explaining existing clusters.
