<!-- tension-hash: 41c8eb80aa09c458 -->
# Conservation Signal vs Null Species-Scale Association

The disagreement is whether metal-related functional conservation is accompanied by a positive ecological association between metal tolerance and metal-contaminated environments. BacDive reports a positive contamination signal, while a cross-resistance analysis finds no species-scale correlation after matching and collapsing strains. Additional atlas and ecological results support parts of the positive interpretation but leave open whether the discrepancy arises from scale, phenotype definition, sampling, taxonomy, or the incomplete [[concepts/pangenome-integration]] bridge. This matters because species-level conservation and divergence may be obscured when strain-level variation and environmental sampling are treated as interchangeable, as emphasized in [[concepts/environmental-resistome]].

## Evidence Sides

### **Positive association and conserved functional architecture**

BacDive found Cohen's d = +1.00 for heavy-metal contamination in n=10 isolates, while the pangenome-scale Metal Fitness Atlas found Cohen's d = +1.0 across 42K strains. [src: bacdive_metal_validation] The heavy-metal estimate is imprecise: n=10 matched isolates produced an observed d=1.00 that barely exceeded the approximately d=0.93 minimum detectable effect size reported for 80% power with n=10 heavy-metal isolates versus approximately 5,000 environmental-baseline strains. [src: bacdive_metal_validation]

The Metal Fitness Atlas supports conservation through its 87.4% core fraction, while its broad metal-important definition (fit < -1 OR n_sick ≥ 1) captures general stress functions as well as metal-specific resistance. [src: metal_fitness_atlas] The simple repertoire score failed to predict fitness. [src: metal_fitness_atlas] MicrobeAtlas found that metal-type diversity predicted broader inferred niche breadth after phylogenetic adjustment; metal-type diversity also correlated with groundwater prevalence (Spearman ρ = +0.112, p = 0.0019). [src: microbeatlas_metal_ecology] These results support a broader-range association but do not demonstrate a uniquely metal-contamination-driven mechanism. [src: microbeatlas_metal_ecology]

### **Null species-scale test and limits on interpretation**

The cross-resistance study found no correlation between multi-metal tolerance scores and BacDive metal-environment isolation at Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8); after matching and collapsing strains, it retained 20 independent species and judged the test underpowered. [src: metal_cross_resistance] Its gene-level conservation analysis does not directly measure within-species environmental occupancy. [src: metal_cross_resistance]

The MicrobeAtlas groundwater-specific fold-enrichment was null (ρ = +0.042, p = 0.242), and its analysis used genus-level occurrence proxies rather than direct metal-exposure phenotypes. [src: microbeatlas_metal_ecology] The BacDive bridge also left 55,107 of 97,334 strains (56.6%) unmatched, primarily because GTDB species boundaries differed from LPSN/DSMZ-based naming. [src: bacdive_metal_validation] BacDive represents culturable, described strains rather than the full diversity of environmental bacteria and may under-represent metal-tolerant extremophiles. [src: bacdive_metal_validation]

## Possible Reconciliations

- **Scale hypothesis:** A positive strain- or gene-level architecture may disappear after aggregation to 20 independent species.
- **Phenotype-definition hypothesis:** The broad definition fit < -1 OR n_sick ≥ 1 may measure general stress functions, whereas multi-metal tolerance and contamination isolation measure narrower phenotypes.
- **Sampling and matching hypothesis:** The 56.6% unmatched BacDive strains and differing taxonomy may alter which genome-size, annotation-breadth, and environmental classes are represented.
- **Ecological-proxy hypothesis:** Genus-level occurrence, groundwater prevalence, and direct contamination exposure may capture related but nonidentical ecological signals.

## Resolving Work

- Reanalyze matched strains with mixed-effects models separating strain, species, and environment, asking whether the BacDive effect persists within species.
- Replicate the n=10 heavy-metal comparison with larger, independently sampled isolate sets and explicit adjustment for genome size, annotated-cluster count, taxonomy, and sampling source.
- Apply PGLS or independent contrasts to gene-level conservation and environmental occupancy, testing whether the positive architecture remains after phylogenetic correction.
- Harmonize GTDB, LPSN, and DSMZ species assignments, then repeat the analysis on matched and unmatched strata to measure the effect of taxonomy and bridge completeness.
- Compare direct metal-exposure phenotypes with normalized repertoire scores, asking whether general stress fitness or metal-specific resistance best predicts environmental isolation.
