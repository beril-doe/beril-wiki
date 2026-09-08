---
title: Pooled openness effects versus lineage-specific and ecological signals
type: Conflict
sources:
- id: amr_pangenome_atlas
  resource: ../../wiki/summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: pangenome_openness
  resource: ../../wiki/summaries/pangenome_openness__REPORT.md
  title: pangenome openness
- id: amr_environmental_resistome
  resource: ../../wiki/summaries/amr_environmental_resistome__REPORT.md
  title: amr environmental resistome
- id: amr_strain_variation
  resource: ../../wiki/summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: prophage_amr_comobilization
  resource: ../../wiki/summaries/prophage_amr_comobilization__REPORT.md
  title: prophage amr comobilization
---
<!-- tension-hash: 3cf7b398dd185709 -->
# Pooled openness effects versus lineage-specific and ecological signals

The disagreement is whether apparent associations between pangenome openness, antimicrobial resistance (AMR), prophage content, and environment reflect general effects or lineage-specific structure. The pooled openness–AMR result is near zero, while stratified analyses report positive associations in many phyla; related analyses find prophage–AMR associations and ecological structuring, but do not establish whether these effects remain after explicit phylogenetic correction. The unresolved issue is therefore whether aggregate results are masking real within-lineage effects, or whether the apparent within-lineage and environmental signals arise from sampling, annotation, or limited scope. See [phylogenetic-confounding-of-pangenome-associations](../../wiki/concepts/phylogenetic-confounding-of-pangenome-associations.md).

## Evidence Sides

### **Pooled and phylogeny-sensitive results show limited general effects**

The overall openness–AMR correlation was near zero (rho=0.006), and openness did not predict either environment or phylogeny effect sizes in the matched species set. [^amr_pangenome_atlas] [^pangenome_openness] These results do not establish that within-phylum AMR patterns persist after explicit phylogenetic correction. [^pangenome_openness][^amr_pangenome_atlas]

The environmental-resistome analysis also found that significant effects occurred within five of six phyla and 20 of 141 families, while the majority of families were not testable or significant because of limited environmental breadth. [^amr_environmental_resistome] The within-species analysis did not provide a general statistical demonstration of environmental structuring because metadata and within-species environmental diversity were insufficient. [^amr_strain_variation]

### **Stratified and mobile-element results show positive associations**

Openness positively correlated with AMR count in 8/10 tested phyla, including Bacillota and Bacillota_C. [^amr_pangenome_atlas] This contrasts with the pooled result and was attributed to phylogenetic dominance of the aggregate signal rather than resolved as a causal effect. [^amr_pangenome_atlas]

Prophage marker density remained associated with AMR repertoire breadth across all five reported major phyla and after controlling for genome count. [^prophage_amr_comobilization] Significant environmental effects within five of six phyla and 20 of 141 families also support an ecological association. [^amr_environmental_resistome] However, species-level classifications, sampling imbalance, and AMRFinderPlus-focused annotation leave unresolved how much of the clinical contrast reflects lineage, representation, or unrecognized environmental resistance. [^amr_environmental_resistome]

## Possible Reconciliations

- **Hypothesis — aggregation and Simpson-like effects:** phylogenetic dominance could drive the pooled rho=0.006 while genuine positive associations remain within 8/10 phyla. [^amr_pangenome_atlas]
- **Hypothesis — predictor and response differences:** prophage density, AMR repertoire breadth, openness, environment effects, and AMR count measure different relationships, so their results need not agree. [^prophage_amr_comobilization] [^pangenome_openness]
- **Hypothesis — incomplete environmental coverage:** ecological signals may be real but detectable only in better-sampled phyla or families, with limited environmental breadth obscuring broader effects. [^amr_environmental_resistome] [^amr_strain_variation]
- **Hypothesis — shared mobile-element biology:** open-pangenome lineages may acquire multiple mobile elements, producing prophage–AMR associations that are not independent of ancestry. [^prophage_amr_comobilization]

## Resolving Work

- Reanalyze openness, AMR count, and AMR breadth with phylogenetic mixed models and within-phylum contrasts; test whether positive associations remain after controlling for shared ancestry.
- Fit joint models containing openness, prophage marker density, genome count, environment, and lineage; test whether prophage density has an independent association with AMR.
- Expand balanced environmental sampling across the 141 families and five of six phyla; test whether nonsignificant results reflect limited environmental breadth.
- Reannotate genomes with multiple resistance-gene methods and compare species-level and within-species results; test whether clinical contrasts persist beyond AMRFinderPlus-focused calls.
- Increase within-species metadata and environmental diversity; test whether case-study AMR ecotypes generalize statistically.

[^amr_pangenome_atlas]: [amr pangenome atlas](../../wiki/summaries/amr_pangenome_atlas__REPORT.md)
[^pangenome_openness]: [pangenome openness](../../wiki/summaries/pangenome_openness__REPORT.md)
[^amr_environmental_resistome]: [amr environmental resistome](../../wiki/summaries/amr_environmental_resistome__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../../wiki/summaries/amr_strain_variation__REPORT.md)
[^prophage_amr_comobilization]: [prophage amr comobilization](../../wiki/summaries/prophage_amr_comobilization__REPORT.md)
