<!-- tension-hash: 07876551f760b60e -->
# Pooled openness signals versus lineage-specific AMR associations

The conflict is whether the relationship between pangenome openness and antimicrobial-resistance (AMR) breadth is genuinely weak, or whether a pooled analysis obscures positive associations within evolutionary lineages. The tension also extends to prophage density and environmental comparisons: related analyses suggest lineage- or ecology-dependent structure, but do not consistently establish that these effects remain after explicit phylogenetic, sampling, or annotation correction. This is the central issue in [[concepts/phylogenetic-confounding-of-pangenome-associations]].

## Evidence Sides

**Pooled analyses and limited generalization.** The overall openness–AMR correlation was near zero (rho=0.006), and openness did not predict the magnitude of environment or phylogeny effects in the matched species set. [src: amr_pangenome_atlas] [src: pangenome_openness] The environmental-resistome analysis also found that the majority of families were not testable or significant because of limited environmental breadth; its species-level classifications, sampling imbalance, and AMRFinderPlus-focused annotation leave unresolved how much of the clinical contrast reflects lineage, representation, or unrecognized environmental resistance. [src: amr_environmental_resistome] Within-species analyses likewise lacked a general statistical demonstration because metadata and within-species environmental diversity were insufficient. [src: amr_strain_variation]

**Stratified, lineage- and mobile-element-associated patterns.** Openness positively correlated with AMR count in 8/10 tested phyla, including Bacillota and Bacillota_C. [src: amr_pangenome_atlas] The report attributes the discrepancy between the pooled and stratified results to phylogenetic dominance of the aggregate signal rather than resolving it as a causal effect. [src: amr_pangenome_atlas] Prophage marker density remained associated with AMR repertoire breadth across all five reported major phyla and after controlling for genome count. [src: prophage_amr_comobilization] Significant environmental effects within five of six phyla and 20 of 141 families support an ecological association, while visible environmental structuring occurred in case-study AMR ecotypes. [src: amr_environmental_resistome] [src: amr_strain_variation]

## Possible Reconciliations

- **Hypothesis — aggregation:** Phylogenetic dominance may dilute positive within-phylum associations in the pooled openness–AMR result, so rho=0.006 and positive associations in 8/10 tested phyla could both be accurate. [src: amr_pangenome_atlas]
- **Hypothesis — predictor and response scope:** Prophage marker density, AMR repertoire breadth, openness, and environmental or phylogeny effect sizes are different predictors and response variables; their associations therefore need not agree. [src: prophage_amr_comobilization] [src: pangenome_openness]
- **Hypothesis — sampling and measurement:** Environmental effects may be real but appear inconsistently because environmental breadth, metadata, lineage representation, and AMRFinderPlus-focused annotation differ across families and species. [src: amr_environmental_resistome] [src: amr_strain_variation]
- **Hypothesis — linked lineage processes:** Prophage density may reflect open-pangenome lineages acquiring multiple mobile elements rather than an association independent of shared ancestry. [src: prophage_amr_comobilization]

## Resolving Work

- Reanalyze openness–AMR associations with phylogenetically independent contrasts or mixed models, asking whether the positive associations in 8/10 tested phyla persist after shared ancestry is modeled.
- Fit a joint model containing openness, prophage marker density, phylum, genome count, and their interactions, asking whether prophage density predicts AMR breadth independently of open-pangenome lineage structure.
- Expand environmental sampling and metadata within species and families, then use balanced within-lineage comparisons to test whether environmental AMR differences remain after controlling for representation.
- Reannotate resistance using multiple AMR databases and equivalent thresholds, asking whether the environmental and clinical contrasts depend on AMRFinderPlus-focused annotation.
