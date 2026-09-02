<!-- tension-hash: 4df6a4843fa3777d -->
# Phenotypic Signals Versus Lineage and Coverage Effects

The disagreement is whether observed phenotype–metal-tolerance and environment–genome associations represent independent ecological or functional effects, or whether they are primarily consequences of taxonomic structure, sampling coverage, and the composition of the measured feature set. This matters because widespread univariate significance can coexist with little added predictive information after lineage is controlled, while subset-specific or condition-specific effects may still be biologically real. The evidence in [[concepts/phenotype-database-coverage-bias]] therefore supports neither a universal phenotype mechanism nor a universal absence of ecological structuring.

## Evidence Sides

**Phenotypes show broad associations, but limited independent prediction.**  
Seven of ten phenotype features were significant after FDR correction, but phenotype features alone explained 16.3% of variance, taxonomy alone explained 35.4%, and adding phenotype features to taxonomy reduced the model to R² = 0.345. [src: bacdive_phenotype_metal_tolerance] The univariate Gram-stain association supports the hypothesis that cell-envelope architecture may influence metal tolerance, while lineage structure prevents separating that mechanism from taxonomic composition. [src: bacdive_phenotype_metal_tolerance] The overall positive catalase association contradicts the negative within-class associations in Actinomycetes, Gammaproteobacteria, and Betaproteobacteria; the corpus therefore does not support one catalase direction across lineages. [src: bacdive_phenotype_metal_tolerance]

**Lineage and taxonomic sampling often dominate, but do not eliminate ecological or functional subsets.**  
The ecotype analysis found that phylogeny dominated gene-content similarity in 60.5% of species, but environment dominated in 39.5%; significant environmental effects were detected in only 16 of 172 species. [src: ecotype_analysis] The ecotype-functional study further supports functional subset differentiation, but its lack of phylogenetic controls creates a tension: COG differences may represent adaptive ecotypes or lineage-linked gene-content structure. [src: ecotype_functional_differentiation] In the plant study, there were small compartment effects after adversarial correction alongside strong apparent plant-associated marker and gene-family differences before and after some controls; the 86% loss of the original compartment R² after removing genome-rich species and limited phylogenetic-tree coverage prevent separating ecological adaptation from taxonomic sampling across the full cohort. [src: plant_microbiome_ecotypes]

**Some adjusted ecological signals persist, but coverage sensitivity remains.**  
Metal type diversity remained associated with niche breadth after phylogenetic adjustment and coverage control, but the association weakened and lost significance under strict within-environment prevalence filtering (β = +0.0166, p = 0.092). [src: microbeatlas_metal_ecology] This supports a potentially reproducible ecological signal while retaining the competing explanation that detection and sampling coverage influence its strength. [src: microbeatlas_metal_ecology]

## Possible Reconciliations

- **Hypothesis — scope difference:** lineage may dominate genome-wide similarity while environment structures a smaller, functionally important subset.
- **Hypothesis — definition difference:** univariate significance may detect association, whereas taxonomy-adjusted R² measures independent predictive contribution.
- **Hypothesis — condition difference:** a phenotype may have a specific effect under one metal condition without predicting a composite score across metals. [src: bacdive_phenotype_metal_tolerance]
- **Hypothesis — coverage difference:** signals that weaken under prevalence filtering may be real but amplified by uneven detection and sampling.

## Resolving Work

- Assemble per-metal phenotype scores and fit taxonomy-adjusted models to test whether catalase predicts copper, urease predicts nickel, and H₂S predicts zinc, copper, and cadmium tolerance. [src: bacdive_phenotype_metal_tolerance]
- Repeat ecotype-functional and plant analyses with matched phylogenetic controls and expanded tree coverage to test whether COG, marker, and gene-family effects persist independently of lineage.
- Apply standardized within-environment prevalence thresholds across datasets and compare effect sizes to determine whether coverage explains signal attenuation.
- Partition genome-wide versus functional-subset variance to test whether environmental effects are concentrated in specific genes or ecotypes.
