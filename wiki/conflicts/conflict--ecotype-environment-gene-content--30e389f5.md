<!-- tension-hash: 30e389f56bb7fccf -->
# Carbon-Pathway Habitat Signal vs. the Broad Species-Level Null on Environment and Gene Content

[[concepts/ecotype-environment-gene-content]] sets two projects' carbon-pathway results against a broad species-level null on environment and gene content, and calls the relation "related but not direct" tension. Both projects report environmental signal in carbon-source pathways. The disagreement is about scope. One question is whether habitat shapes functional gene content at all. The other is whether any such signal sits in specific pathways and specific lineages. This matters because it decides whether this corpus should treat "no environment effect" as general, or as a summary that may hide pathway-level exceptions.

## Evidence Sides

**Side 1: Carbon-pathway profiles carry an environmental signal.**
- Among 54 free-living and plant-associated *Pseudomonas* species, carbon-pathway profiles were associated with isolation environment. A permutation test, which compares observed group distances against label-shuffled ones, gave p = 0.006 [src: pseudomonas_carbon_ecology].
- Within one species, *P. aeruginosa*, seven pathways differ between lung and non-lung isolates at FDR < 0.05. FDR is the false discovery rate, the expected share of false positives among the calls made. All seven are carbon-source pathways [src: cf_formulation_design].

**Side 2: The signal is weak, lineage-structured, and consistent with the null.**
- The strongest separation in PCA (principal component analysis, which projects pathway profiles onto axes of maximal variance) fell between *Pseudomonas* sensu stricto (s.s.) and the *Pseudomonas_E* subgenus [src: pseudomonas_carbon_ecology].
- A classifier predicting environment from pathway profiles reached a balanced accuracy of only 0.408 +/- 0.169. Balanced accuracy is the mean per-class recall, which corrects for unequal class sizes [src: pseudomonas_carbon_ecology].
- In the *P. aeruginosa* comparison, amino acid catabolism stays invariant between lung and non-lung isolates. The habitat signal is concentrated in specific pathways rather than spread across the measured set [src: cf_formulation_design].
- The concept page argues these results do not contradict the species-level null. The analyses use a restricted lineage, pathway completeness rather than broad gene-content similarity, and different environmental summaries [src: pseudomonas_carbon_ecology].

## Possible Reconciliations

- **Hypothesis A (pathway specificity):** Broad gene-content metrics dilute a real signal that sits in a small number of carbon-source pathways. On this view, the null and the positive results measure different quantities and could both hold.
- **Hypothesis B (phylogenetic confounding):** Carbon profiles were associated with environment among the 54 species, and the strongest PCA separation was between *Pseudomonas* s.s. and *Pseudomonas_E* [src: pseudomonas_carbon_ecology]. The hypothesis is that the association partly reflects this lineage split, so it would weaken once lineage is controlled for.
- **Hypothesis C (scale dependence):** Habitat signal appears within a species, as in lung versus non-lung *P. aeruginosa*, but not consistently across species. That would happen if within-lineage loss of specific pathways is visible but swamped by between-lineage variation.

## Resolving Work

- Re-run the 54-species environment test with phylogenetic control, for example PGLS (phylogenetic generalized least squares) or permutations stratified by subgenus. Question: does the association survive within *Pseudomonas_E* alone?
- Apply the same pathway-completeness metric and permutation test to the species sets behind the broad null. Question: does the null hold at pathway resolution, or only for broad gene-content similarity?
- Score lung versus non-lung *P. aeruginosa*, where seven carbon-source pathways differ at FDR < 0.05 [src: cf_formulation_design], with the broad gene-content similarity used for the species-level null. Question: does a metric-driven null appear even there?
- Harmonize environmental summaries across the projects and repeat both analyses on a single shared labelling. Question: how much of the disagreement comes from differing environment categories?
