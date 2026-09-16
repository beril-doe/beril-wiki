<!-- tension-hash: cad34cc630fab898 -->
# Ecotype signal: an unresolved correlation magnitude and two claims of niche structure the whole-genome analysis does not see

Four projects in this corpus ask whether bacterial gene content tracks environment, and they do not line up. The disagreements are of two kinds. First, a straight numerical discrepancy: two runs of essentially the same partial-correlation analysis — the correlation between environmental distance and gene-content distance after removing the phylogenetic contribution — report median values differing by a factor characterized as 27x, so the corpus has no agreed magnitude for the environment–gene-content association even where it agrees on the direction of a group comparison. Second, two scope tensions: analyses restricted to prophage gene modules and to curated plant-function markers each report an environmental or compartment effect that whole-genome comparisons describe as weak or usually nonsignificant. Whether those are genuine refinements (adaptation concentrated in a gene subset) or artifacts of marker choice, annotation, and sampling is not settled by the evidence in hand. This page records all three disagreements; the source tension text lives on [[concepts/ecotype-clustering-validity]].

## Evidence Sides

### Disagreement 1 — What is the median partial correlation?

**Original ecotype analysis.** The original ecotype analysis reported a median partial correlation of 0.003 across its analysis. [src: ecotype_env_reanalysis] Its coarse classification of species returned p=0.66 for the environmental-group comparison. [src: ecotype_analysis, ecotype_env_reanalysis]

**Reanalysis.** The reanalysis reported 0.081, characterized as a 27x difference. [src: ecotype_env_reanalysis] It used all genomes with embeddings, including up to 3,505 genomes per species, rather than diversity-maximizing downsampling with a maximum of 250 genomes, and used different genome sets and distance distributions. [src: ecotype_env_reanalysis] Its genome-level harmonized reanalysis yielded p=0.83. [src: ecotype_analysis, ecotype_env_reanalysis]

The reanalysis itself states that these absolute values are not comparable across methodologies, while holding that the Environmental versus Human-associated comparison remains valid because it was performed within one consistent method. [src: ecotype_env_reanalysis] Both runs support a null environmental-group comparison, but the methodological discrepancy leaves the magnitude of the correlations unresolved. [src: ecotype_analysis, ecotype_env_reanalysis]

### Disagreement 2 — Whole genomes versus prophage modules

**Whole-genome side.** Whole-genome comparisons found weak or usually nonsignificant environment–gene-content relationships. [src: ecotype_analysis, ecotype_env_reanalysis]

**Prophage-module side.** Prophage-module composition — the presence/absence profile of functional blocks of phage genes integrated in bacterial genomes — showed an environmental effect after genome-size and family-level comparisons. [src: prophage_ecology] The source frames this as a related scope tension, not a direct contradiction. [src: ecotype_analysis, ecotype_env_reanalysis, prophage_ecology] The evidence cannot determine whether the difference reflects genuine concentration of ecological adaptation in prophage modules, annotation or sampling differences, or residual confounding; it therefore does not justify treating prophage-module structure as validated ecotype structure. [src: prophage_ecology]

### Disagreement 3 — Whole genomes versus plant-compartment markers

**Plant-marker side.** Refined plant-marker data detected significant compartment separation with PERMANOVA pseudo-F = 23.2, p = 0.001, and R² = 0.071 — PERMANOVA being a permutation test for whether group centroids differ in a distance matrix — but db-RDA (distance-based redundancy analysis, a constrained ordination that separates centroid location shifts from within-group dispersion) gave location-only R² = 0.060, and the effect was highly sensitive to genome-rich taxa. [src: plant_microbiome_ecotypes]

**Whole-genome side.** The same weak whole-genome environmental signal as above. [src: ecotype_analysis, ecotype_env_reanalysis] The plant result is presented as a second scope tension rather than a contradiction: it **refines** the null environmental interpretation, in that ecological structure may be detectable in selected functional markers or particular host-associated lineages without producing strong, generalizable whole-genome ecotypes. [src: plant_microbiome_ecotypes]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the cited evidence.

- **Sample-size and downsampling artifact (Disagreement 1).** Hypothesis: the gap between 0.003 and 0.081 is entirely a property of the genome sets, since the reanalysis used up to 3,505 genomes per species against a maximum of 250 under diversity-maximizing downsampling, and different genome sets change the distance distributions. [src: ecotype_env_reanalysis] Under this hypothesis neither value is "the" correlation, and only within-method contrasts — such as the Environmental versus Human-associated test — carry meaning. [src: ecotype_env_reanalysis]
- **Classification granularity (Disagreement 1).** Hypothesis: the shift from p=0.66 to p=0.83 reflects coarse classification versus genome-level harmonized classification rather than any change in the underlying biology, since both remain null. [src: ecotype_analysis, ecotype_env_reanalysis]
- **Signal dilution (Disagreements 2 and 3).** Hypothesis: adaptation is real but confined to small gene subsets, so whole-genome distances average it away while prophage modules or a curated marker panel retain it. The prophage source explicitly lists this "genuine concentration" reading as one of three it cannot distinguish. [src: prophage_ecology]
- **Annotation and sampling differences (Disagreement 2).** Hypothesis: module calls and uneven sampling, not ecology, generate the environmental effect — the second alternative the prophage source cannot rule out, alongside residual confounding. [src: prophage_ecology]
- **Taxon-composition artifact (Disagreement 3).** Hypothesis: the compartment effect is carried by a few genome-rich taxa rather than by communities, consistent with the reported high sensitivity to genome-rich taxa and with the gap between PERMANOVA R² = 0.071 and db-RDA location-only R² = 0.060. [src: plant_microbiome_ecotypes]

## Resolving Work

**Disagreement 1 — magnitude.**
- Rerun both pipelines on one fixed species set under both genome-selection rules (all embedded genomes up to 3,505 per species; diversity-maximizing downsampling at 250) and report the paired median partial correlations — does the 27x gap close entirely under matched inputs? [src: ecotype_env_reanalysis]
- Sweep the downsampling cap across its range and plot median partial correlation against cap, to test whether the statistic is monotone in sample size rather than a stable biological quantity. [src: ecotype_env_reanalysis]
- Re-express both runs on a sample-size-invariant scale (e.g. permutation-standardized effect sizes per species) so that a magnitude claim can be made at all, since the reanalysis states the absolute values are not comparable across methodologies. [src: ecotype_env_reanalysis]
- Repeat the environmental-group comparison under both classification schemes on the same genomes, checking whether the p=0.66 and p=0.83 results are the same test on different labels. [src: ecotype_analysis, ecotype_env_reanalysis]

**Disagreement 2 — prophage modules.**
- Run the whole-genome partial-correlation analysis and the prophage-module analysis on the identical species set with identical environment variables, so the "weak whole-genome" and "environmental effect in modules" claims are comparable rather than method-paired. [src: ecotype_analysis, ecotype_env_reanalysis, prophage_ecology]
- Recompute the module-level environmental effect after excluding annotation-ambiguous module calls, testing the annotation-difference alternative the source cannot currently exclude. [src: prophage_ecology]
- Apply the same genome-size and family-level controls used for prophage modules to matched random gene-module sets of equal size; if random modules show comparable environmental effects, the concentration hypothesis fails. [src: prophage_ecology]
- Test residual confounding directly by stratifying the module analysis on the sampling variables that differ between environments. [src: prophage_ecology]

**Disagreement 3 — plant compartments.**
- Recompute the compartment test with genome-rich taxa downweighted or excluded, and report whether PERMANOVA pseudo-F = 23.2 / R² = 0.071 and db-RDA location-only R² = 0.060 survive, given the reported high sensitivity to genome-rich taxa. [src: plant_microbiome_ecotypes]
- Run the same PERMANOVA and db-RDA on whole-genome gene content for the identical plant-compartment species, to test whether compartment structure exists only in the refined marker panel. [src: plant_microbiome_ecotypes]
- Randomize the marker panel (equal-size random marker sets) and compare the resulting location-only R² to 0.060, to test whether marker curation manufactures the effect. [src: plant_microbiome_ecotypes]
- Check whether the compartment effect holds within single host-associated lineages, which would separate "particular host-associated lineages" from a community-wide compartment signal. [src: plant_microbiome_ecotypes]
