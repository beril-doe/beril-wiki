---
type: "Concept"
description: "Covers statistical and data-handling pitfalls in genus-level abundance atlases: non-independent samples, rank tests, rollup to genus, denominators and label coverage."
sources: ["summaries/enigma_carbon_census_1__REPORT.md", "summaries/pitfalls.md"]
---
# Calibration and denominators in environmental abundance contrasts

This page covers three pitfalls in genus-level abundance atlases built on NMDC and Planet Microbe data: species-to-genus rollup, the choice of denominator and labels, and the calibration of significance tests. The evidence comes from one project, enigma_carbon_census_1, and from the cross-project pitfalls digest, which repeats only the rollup bug. [src: pitfalls] Denominator, label and calibration results therefore come from a single project. The direction and rank of the contrasts are trustworthy, but the p-values are not calibrated. [src: enigma_carbon_census_1] See [[summaries/enigma_carbon_census_1__REPORT]] and [[summaries/pitfalls]]. The wider context is in [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]].

## Literature Context

The candidate papers show that differential abundance analysis of microbiome count data is statistically hard. The data are sparse and compositional, and they are over-dispersed. Feature tables give relative rather than absolute abundance, because microbial load and sequencing depth are unknown and vary between samples. [PMID 38701410](https://pubmed.ncbi.nlm.nih.gov/38701410/) proposes a zero-inflated negative binomial model with a compositional-bias correction. The authors report that it compares favorably with state-of-the-art methods in simulations and real datasets. A review of compositional-data methods finds no consensus on which approach best addresses compositionality. It also stresses careful study design and covariates, and it says the limits of sequencing-derived data should be recognized explicitly [PMID 42805588](https://pubmed.ncbi.nlm.nih.gov/42805588/). A benchmarking protocol describes testing 22 differential abundance methods on simulated data built from 38 real templates, which include soil and marine habitats. It examines how sparsity, effect size and sample size affect sensitivity and specificity [PMID 40388544](https://pubmed.ncbi.nlm.nih.gov/40388544/). That is a study protocol, and the abstract reports no results.

Several papers address non-independence and false discovery control. MaAsLin 3 is a framework that controls false discovery rates while allowing random effects and repeated measures [PMID 39713460](https://pubmed.ncbi.nlm.nih.gov/39713460/). A generalized linear mixed model approach to metabarcoding read counts decomposes variation among drivers through random-effects terms. It was illustrated on two cross-sectional Soay sheep datasets [PMID 37489890](https://pubmed.ncbi.nlm.nih.gov/37489890/). Soil and rhizosphere work shows that genus-level enrichment patterns, such as Streptomyces enrichment toward the maize root, can be consistent across two field sites [PMID 39091306](https://pubmed.ncbi.nlm.nih.gov/39091306/).

The corpus's calibration finding is consistent with this literature. The enigma_carbon_census_1 project treats thousands of metagenomes as independent in a rank test. All 83 genera reach q<0.05, many at q~1e-70, and the report calls this massively inflated significance. The literature agrees that compositional, zero-inflated data call for models that account for study structure, and the report's recommendation of a study-aware mixed model or a study-respecting permutation matches the mixed-model approaches above [PMID 39713460](https://pubmed.ncbi.nlm.nih.gov/39713460/), [PMID 37489890](https://pubmed.ncbi.nlm.nih.gov/37489890/). The report's textbook soil-versus-freshwater ranking is only loosely comparable to the maize root-gradient result, which comes from a different system.

The other pitfalls are not covered by these candidates. They are species-to-genus rollup, the choice of 3825 taxonomy-bearing covstats files rather than the ~6700 lookup rows (a ~1.75× deflation), and label coverage of 99% against ~13%. None of the papers addresses them, so they are novel, corpus-specific data-handling findings. The compositional-bias literature motivates caution about relative abundance in general [PMID 38701410](https://pubmed.ncbi.nlm.nih.gov/38701410/). It does not bear on the choice of denominator count. The corpus's calibration findings come from a single project.

## Rollup to genus

Both NMDC covstats and Planet Microbe `taxonomy.name` are species-level. Any genus-level abundance claim therefore needs species-to-genus aggregation first. [src: enigma_carbon_census_1, pitfalls] This applies to any project using `covstats_taxonomy_rollup` or Planet Microbe `run_to_taxonomy`. [src: enigma_carbon_census_1]

Filtering on a bare genus name matches only the near-zero rows that carry the genus rank as a literal name. It does not sum the species in that genus. [src: enigma_carbon_census_1, pitfalls] This bug first showed 0/68 marine genera in Planet Microbe. The genera were present, but the filter matched genus-rank reference rows instead of aggregating species. [src: enigma_carbon_census_1, pitfalls]

The failure is silent. The query returns rows and non-null numbers, so nothing errors, but abundances are ~0 and whole genera look absent. [src: pitfalls] A genus filter that returns rows is therefore not evidence that the rollup happened. [src: pitfalls]

The recommended fix is to derive the genus from the species name, group by genus and sum abundance. Only then should the query filter to the genera of interest. [src: pitfalls]

## Denominators and label coverage

The NMDC abundance denominator is the set of covstats files that carry taxonomy, which is 3825. It is not the larger `sample_file_lookup` row count of ~6700. Using the lookup count deflates relative abundances by ~1.75×. [src: enigma_carbon_census_1]

Sample-level environment labels come from `nmdc_metadata.biosample_set`, joined to covstats `sample_id` through `kbase.nmdc_arkin.sample_file_lookup`. [src: enigma_carbon_census_1] This join gives 99% coverage across two ontologies, against ~13% for `study_table` GOLD alone. [src: enigma_carbon_census_1] The two independent ontologies are the Environment Ontology (ENVO) MIxS triad and the GOLD ecosystem path. [src: enigma_carbon_census_1] See also [[entities/nmdc-integrated-collections]] and [[entities/planet-microbe]].

## Calibration of the soil-versus-freshwater contrast

The report labels the soil-versus-freshwater contrast exploratory. [src: enigma_carbon_census_1] The reason is that the rank test treats each metagenome as independent. The abundances are compositional and zero-inflated, and the thousands of samples are not independent. [src: enigma_carbon_census_1] All 83 genera reach q<0.05, many at q~1e-70, and the report attributes this to massively inflated significance. [src: enigma_carbon_census_1] The report regards the current contrast as an exploratory ranking. It recommends a study-aware mixed model or a sample-level permutation respecting study structure to get defensible statistics. [src: enigma_carbon_census_1]

The ranking is still sensible. The report regards the direction and rank of the contrast as trustworthy, and the p-values as not usable as calibrated significance. [src: enigma_carbon_census_1] The contrast recovers textbook biogeography:

- Soil-enriched genera include Mycobacterium (log2 +5.09), Terriglobus (+5.29) and Nitrobacter (+4.79). [src: enigma_carbon_census_1]
- Afipia, Streptomyces, Nocardioides and Mesorhizobium are also soil-enriched. [src: enigma_carbon_census_1]
- Cellvibrio is freshwater-enriched (log2 −2.19). [src: enigma_carbon_census_1]
- Curvibacter, Rhodoferax, Comamonas and Acidovorax are also freshwater-enriched. [src: enigma_carbon_census_1]

The report treats label-free outlier discovery, called Arm B, as the more defensible signal and as robust to label noise. [src: enigma_carbon_census_1] The report's top spikes are Nocardioides at 0.43 in epipsammon, Hydrogenophaga at 0.28 in epiphyton and Mycobacterium at 0.22 in soil. [src: enigma_carbon_census_1]

## Open Directions

- Replace the per-sample rank test with a study-aware mixed model, or a sample-level permutation that respects study structure. This would give defensible enrichment statistics in place of the current exploratory ranking.
- Re-run the marine Planet Microbe contrast after species-to-genus rollup, and check that the 0/68 result no longer appears. This would confirm the fix.
- Recompute NMDC relative abundances with both denominators (3825 and ~6700) on a few genera. This would show how large the ~1.75× deflation is in practice.
- Compare the label-dependent contrast with the label-free outlier mode. This would show how much label noise matters.
- Check denominators, label coverage and test calibration in other atlas projects. This would show whether these weak points recur beyond enigma_carbon_census_1.
