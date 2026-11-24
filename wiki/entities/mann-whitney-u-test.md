---
type: "Method"
description: "Nonparametric two-group rank test, with or without Benjamini-Hochberg correction, used to compare scores or pathway completeness between groups; stops at multi-group tests such as Kruskal-Wallis."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/bacdive_metal_validation__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md", "summaries/harvard_forest_warming__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["Benjamini-Hochberg FDR", "Mann-Whitney", "Mann-Whitney U", "Mann-Whitney U test with Benjamini-Hochberg correction"]
---
# Mann-Whitney U test

Mann-Whitney U test is the page topic: a nonparametric two-group rank test, with or without Benjamini-Hochberg correction. Reports use it to compare scores or pathway completeness between groups. [src: amr_environmental_resistome, pseudomonas_carbon_ecology]

## Key facts

- Cohen's d (see [[entities/cohen-s-d-effect-size]]) accompanied the test in the clay-confined subsurface report, where self-sufficiency was tested with a two-sided Mann–Whitney U test. [src: clay_confined_subsurface]

## Uses with significant results

### Antimicrobial resistance (AMR) across environments

Of 15 pairwise environment comparisons of species AMR diversity, 13 are significant after false discovery rate (FDR) correction. [src: amr_environmental_resistome] The largest effect is clinical versus aquatic (rank-biserial r = −0.49). [src: amr_environmental_resistome] In the clinical-exposure proxy analysis, clinical-dominated species have 4.4× more AMR clusters than the environmental comparison group (mean 72.9 vs 16.4, MWU p = 2×10⁻¹⁸). [src: amr_environmental_resistome] They also have a higher percentage of accessory AMR (MWU p=0.004). [src: amr_environmental_resistome] See [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]] and [[summaries/amr_environmental_resistome__REPORT]].

### Metal tolerance and BacDive

BacDive isolates from heavy metal contamination sites have metal tolerance scores a full standard deviation above the environmental baseline (Cohen's d = +1.00, Mann-Whitney p=0.006, n=10). [src: bacdive_metal_validation] The metal utilization comparison, with 8 positive and 16 negative results, is underpowered (Mann-Whitney p=0.14, d=-0.57). [src: bacdive_metal_validation] See [[summaries/bacdive_metal_validation__REPORT]].

### Other projects

- Gene copy number variation: the refined bacterial pilot gave a pooled ratio of 3.3× and a Mann-Whitney test on cluster CVs (cross-validation) of p = 1.6 × 10⁻⁷, passing all 4 pre-registered gates. [src: gene_copy_number_variation]
- Community metabolic ecology: Soil versus Freshwater principal component 1 (PC1) separation had Mann-Whitney U = 3,674, p < 0.0001, with median PC1 Soil = +3.86 and Freshwater = −6.28. [src: nmdc_community_metabolic_ecology]

### Pseudomonas carbon pathways

Comparing 7 *Pseudomonas* s.s. species with 189 *Pseudomonas_E* species (each with >=5 genomes), Mann-Whitney U tests with Benjamini-Hochberg FDR correction identified 43 of 62 pathways as significantly different (q < 0.05). [src: pseudomonas_carbon_ecology] Nineteen pathways showed no significant difference between subgenera. [src: pseudomonas_carbon_ecology] See [[concepts/host-adaptation-pathway-loss-in-pseudomonas-carbon-catabolism]].

## Null, underpowered and uncorrected results

Rhamnose pathway completeness was higher in *P. aeruginosa* (66.8%) than the *P. fluorescens* group (41.3%), and fucose was also higher (45.1% for the fluorescens group). Neither difference was significant after FDR correction. [src: pseudomonas_carbon_ecology]

In Harvard Forest warming, heated mineral samples have a mean ChEBI count of 155 ± 4 with heated-versus-control MW (molecular weight, as the report abbreviates it) p=0.012. [src: harvard_forest_warming] Heated organic samples have 160 ± 13 with p=0.209, in the same direction as mineral samples. [src: harvard_forest_warming] See [[concepts/soil-metabolite-richness-under-warming-and-substrate-depletion]].

In the ENIGMA carbon census, only n=9 compounds were callable, so the physicochemical comparison is directional, not inferential. It uses Mann–Whitney tests reported as direction plus uncorrected p values. [src: enigma_carbon_census_1] The contrasts showing smaller or simpler callable compounds are descriptive, not calibrated significance. [src: enigma_carbon_census_1] See [[concepts/annotation-coverage-bias-in-chemical-class-callability]].

## Open Directions

- Re-run the ENIGMA callable-compound contrasts with more callable compounds and FDR correction, to move them from directional to inferential.
- Extend the BacDive metal utilization comparison with more isolates to test whether the non-significant result reflects low power.
