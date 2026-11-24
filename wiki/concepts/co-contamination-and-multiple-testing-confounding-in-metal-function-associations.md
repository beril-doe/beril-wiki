---
type: "Concept"
description: "Covers how correlated metal exposures, non-independent tests, conditioning on project effects and unreported effect sizes limit interpretation of metal-COG association counts and db-RDA variance explained; stops at the statistical remedies proposed."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Co-contamination and multiple-testing confounding in metal-function associations

This page covers how correlated metal exposures, non-independent tests, project-effect conditioning and unreported effect sizes limit interpretation of metal-COG (clusters of orthologous groups) association counts and db-RDA variance explained. The evidence is mostly caveats stated in the soil_metal_functional_genomics report [src: soil_metal_functional_genomics], plus one caveat from comprehensive_metal_ecology. [src: comprehensive_metal_ecology] The proposed remedies are still pending. [src: soil_metal_functional_genomics] See [[summaries/soil_metal_functional_genomics__REPORT]] and [[summaries/comprehensive_metal_ecology__REPORT]].

## Literature Context

The two candidate papers are laboratory soil studies of metal stress. Neither tests the statistical problems this page raises: correlated metal exposures, non-independent tests, project conditioning and unreported effect sizes. They give only indirect context.

One study sampled millet rhizosphere soil before Cr stress and at 6 h and 6 days after it [PMID 36910173](https://pubmed.ncbi.nlm.nih.gov/36910173/). Bacterial community composition changed considerably and α-diversity fell (p < 0.05). Nitrogen-cycle genes responded, with AOA-amoA and AOB-amoA abundance first decreasing and then increasing. In redundancy analysis (RDA) and PERMANOVA, soil physicochemical parameters were significantly correlated with the nitrogen-cycle functional genes (r: 0.4195, p < 0.01). The authors concluded that physicochemical parameters influenced these genes more than the bacterial community did. This is a single-metal, controlled laboratory design, so co-contamination is not an issue. It does show that soil properties such as pH and available N, P and K are a second source of variation next to the metal. That is consistent with the hub's caution that variance explained depends on what else is modelled.

The second study amended soil with copper and zinc, as sulfate or nitrate salts at 20 mM, in microcosms [PMID 33773246](https://pubmed.ncbi.nlm.nih.gov/33773246/). The abstract does not say whether the two metals were applied together or separately, so it does not separate their individual contributions. Metal amendment was associated with a significant decrease in bacterial community diversity and richness. A carbapenem-resistant Pseudomonas aeruginosa isolate and its acquired genes stayed quantifiable for up to one month, in both amended and non-amended soil. The authors used descriptive statistics and multivariate analysis. Because the metal identity and the counter-ion (sulfate or nitrate) are varied together in the design, this study illustrates how exposure factors can be entangled.

The corpus claims sit alongside this literature as consistent but not directly tested by it. The soil_metal_functional_genomics report describes 2,355 significant metal-COG associations at FDR < 0.05, among 3,915 tests. It argues that Benjamini-Hochberg correction is anti-conservative when co-varying metals (Cr, Cu, Pb and Zn) make tests dependent. It also reports a conditional db-RDA R² of 0.799 and cautions that the unconditional R² is unreported. The candidate papers support the general expectation that metals reduce diversity and shift community and functional gene profiles. They do not address the 60% discovery rate, the partial-correlation remedy or the unconditional R². Those points are novel relative to these two papers, and they remain the corpus's own untested caveats. Neither paper offers a null result or an effect-size audit to compare against.

## Co-contamination and non-independent tests

Co-contamination is a significant confound: Cr, Cu, Pb and Zn co-vary in many industrial soils. [src: soil_metal_functional_genomics] The report describes 2,355 significant associations at FDR (false discovery rate) < 0.05 in 51,748 samples, from 9 metals × 435 COGs = 3,915 tests, and calls the 60% discovery rate high. [src: soil_metal_functional_genomics] The report argues that co-varying metals make the tests non-independent. It says Benjamini-Hochberg FDR correction assumes independent tests and is anti-conservative under positive correlation, so the true FDR is likely higher than reported. [src: soil_metal_functional_genomics] This is the report's argument, not a measured FDR. See also [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]].

Whether individual COG-metal associations are metal-specific or reflect a generic stress response to multi-metal contamination is unresolved, with partial correlation models pending. [src: soil_metal_functional_genomics] All associations are also observational. [src: soil_metal_functional_genomics]

## Effect sizes

Spearman ρ effect sizes have not been systematically reported across all 2,355 associations. Many may be statistically significant but biologically small. [src: soil_metal_functional_genomics]

## Conditioning on project effects in db-RDA

The soil db-RDA gave R² = 0.799, p = 0.005 (permutation test, 999 permutations). This was reported as metals explaining 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics] The report reads this as not a statistical artefact of batch effects, because project accession was conditioned out. [src: soil_metal_functional_genomics]

The report also cautions against over-reading the figure. If project effects account for most of the community COG variance, R² describes how well metals explain the residual variance, not the total. [src: soil_metal_functional_genomics] The unconditional R² for metals alone is not reported and may be substantially lower. The report says it must be reported next to the conditional figure. [src: soil_metal_functional_genomics]

A related limit applies in comprehensive_metal_ecology. Its variance-partitioning R² values are unadjusted linear-model results without permutation testing, and are interpreted descriptively. [src: comprehensive_metal_ecology]

## Proposed statistical remedies

The report names the partial correlation model as the correct remedy for co-contamination confounding. [src: soil_metal_functional_genomics] The model is COG ~ Cr | Cu + Zn + Pb, meant to separate metal-specific from general responses. [src: soil_metal_functional_genomics] Two further items are pending: an effect size audit of the ρ distribution across 2,355 associations that flags ρ < 0.05 [src: soil_metal_functional_genomics], and reporting the unconditional db-RDA R² with metals only and no project conditioning. [src: soil_metal_functional_genomics] Broader context is in [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]].

## Open Directions

- Run the partial correlation models for each metal against COGs, controlling for the other co-varying metals. This tests whether associations are metal-specific.
- Complete the ρ audit, then recompute the count of associations above a minimum effect size. This shows how many of the 2,355 are biologically meaningful.
- Fit the metals-only db-RDA without project conditioning and report it with the conditional R² = 0.799. Also report how much variance project alone explains.
- Use a permutation scheme or an FDR method that allows for dependence among tests, and compare its count with the Benjamini-Hochberg count. This quantifies the anti-conservative bias.
- Permutation-test the variance-partitioning R² values in comprehensive_metal_ecology.
