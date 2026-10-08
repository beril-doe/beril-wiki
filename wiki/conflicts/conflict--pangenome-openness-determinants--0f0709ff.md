<!-- tension-hash: 0f0709ff9c0b0eac -->
# Does a Null Pooled Openness Association Mean No Association Within Lineages?

Pangenome openness is the tendency of a species' gene repertoire to keep expanding as more genomes are sampled. Analyses of what drives it disagree depending on phylogenetic scale. When species are pooled across the whole atlas, openness shows essentially no association with antimicrobial resistance (AMR) gene count (rho=0.006, where rho is a correlation coefficient). Within individual phyla, however, positive correlations appear in 8/10 phyla [src: amr_pangenome_atlas]. Separately, an atlas-scale test of openness against M22 is null, while clade-targeted tests point in a positive direction but are underpowered [src: gene_function_ecological_agora]. This matters because it decides whether pooled null results can stand as evidence that openness is unrelated to gene content and acquisition, or whether they hide lineage-level associations. The disagreement is recorded on [[concepts/pangenome-openness-determinants]].

## Evidence Sides

**Pooled, atlas-scale analyses: null association**

- Across all species, the correlation between openness and AMR count is near zero (rho=0.006). The project reads this as phylogeny dominating the signal [src: amr_pangenome_atlas].
- At atlas scale, the test of openness against M22 returned a null result. The evidence available here does not define M22 [src: gene_function_ecological_agora].

**Lineage-resolved analyses: positive association**

- When the analysis is stratified by phylum, openness correlates positively with AMR count in 8/10 phyla. This **refines** the null phylogeny-effect result. Pooling across phyla can mask lineage-level associations, so a null pooled correlation does not establish that there is no within-lineage association [src: amr_pangenome_atlas].
- Clade-targeted tests of openness against M22 are directionally positive but underpowered. This leaves open whether openness tracks gene acquisition within specific lineages [src: gene_function_ecological_agora].

## Possible Reconciliations

- **Hypothesis 1 (aggregation masking):** Associations of different strength or sign in different lineages may cancel when pooled. If so, the atlas-scale nulls would reflect aggregation rather than a true absence of effect. This is not established for the M22 axis, whose clade-targeted tests are underpowered [src: gene_function_ecological_agora].
- **Hypothesis 2 (between-lineage confounding):** Phylum-level differences in baseline openness and gene content may swamp within-lineage covariation. In that case the pooled and stratified results would answer different questions rather than contradict each other.
- **Hypothesis 3 (power limitation):** The directionally positive clade-targeted M22 signals may be noise. While they remain underpowered [src: gene_function_ecological_agora], the data cannot distinguish a genuine within-lineage association, which could coexist with the atlas-scale null, from no association.

## Resolving Work

- Use per-species openness and AMR counts from amr_pangenome_atlas. Fit a mixed model (a regression combining fixed effects with random effects, which let each group have its own baseline) with phylum as the random effect, or use phylogenetic generalized least squares (PGLS, a regression that accounts for shared ancestry). Question: does a within-lineage slope persist once between-phylum variance is partitioned out?
- Run a power analysis (an estimate of the sample size needed to detect an effect of a given size with a chosen probability) on the gene_function_ecological_agora clade-targeted openness-versus-M22 tests. Question: how many additional genera or species per clade would a directionally positive effect need to reach significance?
- Apply the same phylum-stratified design used for AMR to the M22 axis. Question: does M22 show a pooled null alongside within-phylum positive associations?
- Run a heterogeneity test across the phyla, comparing the 8/10 positive phyla with the remainder. Question: are lineage-level associations consistent in direction, or does pooling average opposing signs?
