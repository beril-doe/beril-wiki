---
type: "Method"
description: "Multiple-testing correction controlling false discovery rates across microbial ecology analyses"
sources: ["summaries/metal_resistance_global_biogeography__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Benjamini–Hochberg FDR

## What this entity is

**Canonical name:** Benjamini–Hochberg false discovery rate correction. [src: metal_resistance_global_biogeography]

**Known aliases:** BH FDR; Benjamini–Hochberg FDR. [src: metal_resistance_global_biogeography]

**Stable external identifier:** None is specified in the source document. [src: metal_resistance_global_biogeography]

This method corrects multiple-testing results by producing q-values for spatial and biome-stratified Fisher's exact tests. [src: metal_resistance_global_biogeography] Its use in community metabolic ecology **extends** this role to pathway–metabolite correlations and ecosystem-comparison tests. [src: nmdc_community_metabolic_ecology] Its application to PGP gene co-occurrence and environmental-enrichment tests further **supports** its cross-domain use for controlling discovery claims across many gene pairs and ecological comparisons. [src: pgp_pangenome_ecology] Application to phage-defense syndromes **further supports** this cross-domain use: 1,000 phylum-stratified column-permutation tests were corrected with BH-FDR, and 27 of 28 defense-system pairs were significant at q < 0.05. [src: phage_defense_arsenal]

Application to soil-metal functional genomics **extends** this record to high-throughput COG–metal associations: 2,355 associations were reported at FDR < 0.05 among 3,915 implied tests across nine metals and 435 COGs, a 60% discovery rate. [src: soil_metal_functional_genomics] The report cautions that co-varying metals make tests non-independent, so BH-FDR may be anti-conservative under positive correlation and the true FDR may be higher than reported. [src: soil_metal_functional_genomics]

## Use in metal-resistance biogeography

The study applied Fisher's exact tests with Benjamini–Hochberg false discovery rate correction to a 5° grid containing **289 cells with at least 5 MAGs**. [src: metal_resistance_global_biogeography] The corrected analysis identified **11 significant hotspots** meeting **OR>2** and **q<0.05**, plus **3 coldspots** meeting **OR<0.5** and **q<0.05**. [src: metal_resistance_global_biogeography] The top hotspot, in the Atacama/Andean region of Chile at **lat=-25°, lon=-70°**, had **21.8% prevalence**, **OR=9.83**, **q=7.6e-12**, and **n=101 MAGs**. [src: metal_resistance_global_biogeography]

The study also used the correction for biome-stratified tests against the global baseline. [src: metal_resistance_global_biogeography] For soil, the corrected result was **5.8% prevalence**, **OR=5.05**, and **q=1.8e-82**; for rhizosphere, **1.9% prevalence**, **OR=0.66**, and **q=0.30 (NS)**; and for marine samples, **1.2% prevalence**, **OR=0.20**, and **q=9.2e-80**. [src: metal_resistance_global_biogeography] These results support [[concepts/environmental-resistome]] by quantifying evidence for soil enrichment and marine depletion of metal resistance in the coordinate-filtered environmental MAG dataset. [src: metal_resistance_global_biogeography]

The soil-metal analysis **refines** this environmental-resistome record: chromium and lead produced the strongest signals among nine metals, with transporters including ABC and RND systems and biosynthesis genes among the top hits. [src: soil_metal_functional_genomics] However, the associations are observational, and co-contamination among chromium, copper, lead, and zinc leaves metal-specificity unresolved pending partial-correlation analysis. [src: soil_metal_functional_genomics]

## Use in community metabolic ecology

The NMDC × pangenome analysis **supports** the method's cross-domain applicability: BH correction identified leucine and arginine as the only two tested pathway–metabolite associations significant at **q < 0.05**, with leucine **r = −0.390, q = 0.022, n = 62** and arginine **r = −0.297, q = 0.049, n = 80**. [src: nmdc_community_metabolic_ecology] The same correction found significant ecosystem differences for **17 of 18 amino-acid pathways**; glycine, asparagine, and cysteine had **q = 1.2×10⁻¹⁹**, **q = 3.8×10⁻¹⁴**, and **q = 1.5×10⁻¹³**, respectively, while tyrosine was not significant (**q = 0.71**). [src: nmdc_community_metabolic_ecology] These results **refine** its established use in spatial and biome-stratified enrichment testing by covering both correlation-level and omnibus ecosystem comparisons. [src: nmdc_community_metabolic_ecology]

## Use in PGP pangenome ecology

In the PGP pangenome analysis, BH-FDR correction found **8 of 10** focal-gene pairs significant: **five positive** and **three negative** associations. [src: pgp_pangenome_ecology] The strongest positive association was **pqqC × acdS** (**OR = 7.24, n = 286 co-occurring species, q = 1.2e-83**); nifH was negatively associated with hcnC (**OR = 0.23, q = 5.8e-29**) and pqqC (**OR = 0.57, q = 2.9e-19**). [src: pgp_pangenome_ecology] This **supports** using the correction to identify robust gene-gene ecological associations rather than treating unadjusted co-occurrences as discoveries.

The correction also supported soil/rhizosphere enrichment claims: acdS had **OR = 7.02, q = 5.1e-62**, pqqC had **OR = 2.90, q = 2.8e-53**, and hcnC had **OR = 1.85, q = 6.1e-08**; nifH was depleted (**OR = 0.60, q = 5.5e-08**). [src: pgp_pangenome_ecology] These results **refine** the prior record of corrected biome comparisons by extending it from metal-resistance prevalence to gene-trait distribution across pangenomes. [src: pgp_pangenome_ecology]

## Use in phage-defense and prophage ecology

The phage-defense study used BH-FDR after 1,000 phylum-stratified column-permutation tests to assess 28 pairwise defense-system co-occurrences. [src: phage_defense_arsenal] **Twenty-seven of 28** pairs showed significant positive co-occurrence at **q < 0.05**; the strongest was R-M Type II × Gabija, with **z = 46.1** and **OR = 24.0**. [src: phage_defense_arsenal] CRISPR-Cas × CBASS was the only nonsignificant pair (**z = 0.21, p_emp = 0.98**). [src: phage_defense_arsenal] This **refines** the method's existing record by demonstrating its use with empirical permutation nulls and phylum-stratified syndrome tests, while the report cautions that permissive CRISPR-Cas detection may reduce syndrome specificity. [src: phage_defense_arsenal]

Application to prophage ecology **supports** this broader use in module-level environmental testing: constrained permutations preserving host-family and genome-size-quartile strata identified **8 significant module-by-environment enrichments at FDR < 0.05**, including tail, head morphogenesis, and anti-defense enrichment in human-associated environments. [src: prophage_ecology] BH-FDR also **refines** the interpretation by showing that 57 module–abiotic correlations in 6,365 NMDC metagenomic samples passed **FDR < 0.05**, whereas no individual TerL lineage was environment-enriched after correction in **0/500 tests**. [src: prophage_ecology] Together with the defense-syndrome results, these applications support [[concepts/phage-defense-syndromes-and-arms-race]] as a cross-domain setting for distinguishing reproducible phage-associated patterns from multiple-testing artifacts. [src: phage_defense_arsenal, prophage_ecology]

## Use in Pseudomonas carbon ecology

Application to standardized GapMind carbon-pathway comparisons **supports** the method's use for correcting many pathway-level ecological tests: among 7 *Pseudomonas* s.s. species and 189 *Pseudomonas_E* species, **43 of 62 pathways** differed significantly by Mann–Whitney U testing after Benjamini–Hochberg correction at **q < 0.05**. [src: pseudomonas_carbon_ecology] This **refines** the existing record from gene-pair, ecosystem, and enrichment tests to comparative metabolic-pathway completeness across clades. [src: pseudomonas_carbon_ecology]

The corrected comparison supports pathway-loss claims rather than treating the numerous pathway differences as unadjusted discoveries; the largest reported contrasts included xylose completeness of **0.0% versus 74.4%**, ribose **27.9% versus 92.0%**, and arabinose **0.0% versus 62.6%** between the *P. aeruginosa* and *P. fluorescens* groups. [src: pseudomonas_carbon_ecology] The same analysis found **19 pathways** with no significant subgenus difference, showing that correction also preserves a distinction between broadly conserved pathways and pathway-specific contrasts. [src: pseudomonas_carbon_ecology] A 999-permutation environment-association test additionally reported **p = 0.006** for carbon profiles among free-living and plant-associated species, while a Random Forest achieved balanced accuracy of **0.408 +/- 0.169** against a **0.250** chance baseline. [src: pseudomonas_carbon_ecology] These results **support** a modest ecological signal but **refine** interpretation by showing that statistically detectable pathway differences do not make carbon profiles sufficient for fine-grained environment prediction. [src: pseudomonas_carbon_ecology]

## Interpretation and limitations in soil-metal genomics

The soil-metal report **refines** the interpretation of corrected discovery counts by reporting that effect sizes have not been systematically examined across all 2,355 associations; a planned audit will inspect Spearman rho values and flag associations with rho < 0.05. [src: soil_metal_functional_genomics] Planned partial-correlation tests, spatial-autocorrelation testing, and validation of unconditional versus conditional db-RDA R² are needed before the corrected associations can be interpreted as metal-specific or biologically substantial. [src: soil_metal_functional_genomics] The report states that these validations require Spark access to the `kescience_mgnify` and `kbase_ke_pangenome` tables because no local CSV contains the Spearman rho values or model residuals. [src: soil_metal_functional_genomics]

## Related pages

- [[summaries/metal_resistance_global_biogeography__REPORT]] — source summary reporting spatial and biome-corrected results. [src: metal_resistance_global_biogeography]
- [[summaries/nmdc_community_metabolic_ecology__REPORT]] — source summary reporting pathway–metabolite and ecosystem-comparison applications. [src: nmdc_community_metabolic_ecology]
- [[summaries/pgp_pangenome_ecology__REPORT]] — source summary reporting corrected PGP gene co-occurrence and environmental-enrichment analyses. [src: pgp_pangenome_ecology]
- [[summaries/phage_defense_arsenal__REPORT]] — source summary reporting BH-FDR correction of phage-defense syndrome tests. [src: phage_defense_arsenal]
- [[summaries/prophage_ecology__REPORT]] — source summary reporting corrected prophage module-environment and TerL-lineage tests. [src: prophage_ecology]
- [[summaries/pseudomonas_carbon_ecology__REPORT]] — source summary reporting corrected carbon-pathway comparisons and ecological association tests. [src: pseudomonas_carbon_ecology]
- [[summaries/soil_metal_functional_genomics__REPORT]] — source summary reporting corrected COG–metal associations and their validation limits. [src: soil_metal_functional_genomics]
- [[concepts/environmental-resistome]] — concept supported by biome-specific corrected prevalence and enrichment results. [src: metal_resistance_global_biogeography]
- [[concepts/environment-embedding-geography]] — concept related to the spatial grid analysis and geographic interpretation of corrected hotspot results. [src: metal_resistance_global_biogeography]
- [[concepts/phage-defense-syndromes-and-arms-race]] — concept related to corrected defense-system and prophage module enrichment tests. [src: phage_defense_arsenal, prophage_ecology]
- [[entities/fishers-exact-test]] — statistical test used with this correction for hotspot, coldspot, and biome comparisons. [src: metal_resistance_global_biogeography]
