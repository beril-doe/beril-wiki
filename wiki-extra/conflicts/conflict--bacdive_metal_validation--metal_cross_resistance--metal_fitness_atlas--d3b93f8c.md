<!-- tension-hash: 41c8eb80aa09c458 -->
# Species-Scale Null Versus Positive Metal-Conservation Associations

The disagreement concerns whether metal-associated conservation and environmental occupancy produce a reproducible positive association across biological scales. The positive results support a layered model in which metal-related functions are conserved and linked to contaminated environments, while the null species-scale test questions whether that relationship survives strain matching, aggregation, and phenotype definition. Resolving the tension matters for interpreting the incomplete [[concepts/pangenome-integration]] bridge and for distinguishing species-level conservation from strain-level ecological specialization, a distinction also connected to [[concepts/environmental-resistome]].

## Evidence Sides

**Positive conservation and ecological-association side.** BacDive found Cohen's d = +1.00 for heavy-metal contamination in n=10 isolates, while the pangenome-scale Metal Fitness Atlas found Cohen's d = +1.0 across 42K strains. [src: bacdive_metal_validation] The Metal Fitness Atlas reported an 87.4% core fraction, supporting broad conservation, although its broad metal-important definition (fit < -1 OR n_sick ≥ 1) includes general stress functions as well as metal-specific resistance, and its simple repertoire score failed to predict fitness. [src: metal_fitness_atlas] MicrobeAtlas found that metal-type diversity predicted broader inferred niche breadth after phylogenetic adjustment. [src: microbeatlas_metal_ecology] In groundwater, metal-type diversity correlated with prevalence (Spearman ρ = +0.112, p = 0.0019), although groundwater-specific fold-enrichment was null (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] The metal-cross-resistance study also found broadly positive gene-level responses across 28 organisms. [src: metal_cross_resistance]

**Null species-scale and qualification side.** The cross-resistance study found no correlation between multi-metal tolerance scores and BacDive metal-environment isolation at Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8); after matching and collapsing strains, it retained 20 independent species and judged the test underpowered. [src: metal_cross_resistance] The n=10 BacDive estimate of observed d=1.00 barely exceeded the approximately d=0.93 minimum detectable effect size reported for 80% power with n=10 heavy-metal isolates versus approximately 5,000 environmental-baseline strains. [src: bacdive_metal_validation] Of 97,334 strains, 55,107 (56.6%) were unmatched, primarily because GTDB species boundaries differed from LPSN/DSMZ-based naming. [src: bacdive_metal_validation] BacDive represents culturable, described strains rather than the full diversity of environmental bacteria and may under-represent metal-tolerant extremophiles. [src: bacdive_metal_validation] The gene-level conservation analysis was not based on phylogenetically independent organisms and did not directly measure within-species environmental occupancy. [src: metal_cross_resistance]

## Possible Reconciliations

- **Hypothesis — scale:** strain- or pangenome-level associations may be positive while aggregation to 20 independent species removes the signal.
- **Hypothesis — phenotype definition:** the Atlas’s broad metal-important definition may capture general stress functions, whereas multi-metal tolerance and environmental isolation measure narrower phenotypes.
- **Hypothesis — sampling and matching:** the 55,107 unmatched strains and culturable-strain bias may alter the observed association.
- **Hypothesis — ecological proxy:** genus-level occurrence and groundwater prevalence may reflect broad niche breadth rather than uniquely metal-contamination-driven adaptation.
- **Hypothesis — phylogenetic dependence:** positive gene-level responses across 28 organisms may partly reflect shared ancestry rather than independent conservation.

## Resolving Work

- Reanalyze matched BacDive and Fitness Browser strains with hierarchical models retaining strain-level variation, asking whether the positive association persists before species collapsing. [src: bacdive_metal_validation] [src: metal_cross_resistance]
- Replicate the heavy-metal comparison with a substantially larger, independently sampled isolate set and explicit adjustment for genome size, annotated-cluster count, taxonomy, and sampling source. [src: bacdive_metal_validation]
- Test narrow metal-specific phenotypes separately from general stress functions, asking whether the result changes when fit < -1 OR n_sick ≥ 1 is decomposed. [src: metal_fitness_atlas]
- Apply PGLS or independent contrasts to the 28-organism gene-level data and directly compare phylogenetically adjusted results with species-level occupancy measures. [src: metal_cross_resistance]
- Replace genus-level occurrence proxies with direct, standardized metal-exposure measurements and test whether they predict both niche breadth and metal-specific enrichment. [src: microbeatlas_metal_ecology]
