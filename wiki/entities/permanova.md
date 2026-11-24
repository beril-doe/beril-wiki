---
type: "Method"
description: "Permutational multivariate analysis of variance used to partition community or profile variance among factors; does not cover PERMDISP dispersion tests or db-RDA."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/harvard_forest_warming__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
aliases: ["PERMANOVA-like test", "PERMDISP", "db-RDA", "distance-based redundancy analysis", "permutational multivariate analysis of variance"]
---
# PERMANOVA

This page covers PERMANOVA, permutational multivariate analysis of variance, as used across BERIL reports. The reports use it to partition community or profile variance among factors. [src: enigma_sso_asv_ecology, harvard_forest_warming, neon_mag_functional_discovery]

Several reports caution that R² and significance need careful reading: a permutation p-value floor, an inflated Phase 1 R², dispersion effects, and a conditional db-RDA R². [src: neon_mag_functional_discovery, plant_microbiome_ecotypes, soil_metal_functional_genomics]

## Key facts

- For the NEON soil two-factor PERMANOVA, p = 0.001 is the smallest permutation p-value attainable with 999 permutations. [src: neon_mag_functional_discovery]
- The prophage analysis used 99 permutations and reported p = 0.01. [src: prophage_ecology]
- Pairwise PERMANOVA with 3 vs 3 samples has a permutation floor of p~0.10. [src: lignin_community_enrichment]

## Examples across projects

### Habitat and soil chemistry (NEON)

NEON functional gene content partitions by habitat with PERMANOVA pseudo-F = 137, p = 0.001. The groups were soil n=1,800, benthic n=618 and water n=88 workflows. [src: neon_mag_functional_discovery] In soil, pH bin (4 levels, n = 1,700) gave pseudo-F = 32.5, p = 0.001 and R² = 5.4%, which passes the 5% threshold. [src: neon_mag_functional_discovery] Soil horizon (O / M, n = 1,800) gave pseudo-F = 40.5, p = 0.001 and R² = 2.2%, which fails the threshold. [src: neon_mag_functional_discovery] Both factors are significant, but only pH clears the pre-registered effect-size threshold. [src: neon_mag_functional_discovery] See [[concepts/habitat-and-soil-chemistry-structuring-of-metagenomic-functional-gene-content]].

### Subsurface sediment and groundwater (SSO)

In 37 sediment core segments, hydrogeological zone explained 27.5% of community variance (F = 4.05, p = 0.0001). [src: enigma_sso_asv_ecology] Well identity explained 19.2% but was not significant (F = 0.80, p = 0.979). [src: enigma_sso_asv_ecology] In the groundwater stability analysis the pattern differed. Well explained R² = 49.9% (p = 0.001) and filter size explained 10.1% (p = 0.001). [src: enigma_sso_asv_ecology] Depth explained 2.5% (p = 0.430) and date explained 0.8% (p = 0.998), so no temporal change was detectable. [src: enigma_sso_asv_ecology] See [[concepts/depth-and-hydrogeological-zonation-of-subsurface-microbial-communities]] and [[concepts/temporal-stability-of-groundwater-communities]].

### Warming (Harvard Forest)

On Bray-Curtis genus distances, treatment explained R²=7.6% (p=0.069). [src: harvard_forest_warming] Horizon explained R²=30.6% (p=0.0002). [src: harvard_forest_warming] The treatment × horizon 4-cell model explained R²=41% (p=0.0002). [src: harvard_forest_warming] In the paired n=25 subset, treatment pseudo-F was 3.12 in DNA (R²=11.9%, p=0.020) and 0.76 in RNA (R²=3.2%, p=0.60). [src: harvard_forest_warming] In the direct-only sensitivity analysis, none of these results was significant:

| Pool × horizon | n | F | R² | p |
|---|---|---|---|---|
| DNA × mineral | 14 | 1.75 | 12.7% | 0.081 [src: harvard_forest_warming] |
| RNA × mineral | 11 | 1.15 | 11.4% | 0.254 [src: harvard_forest_warming] |
| RNA × organic | 14 | 1.33 | 10.0% | 0.190 [src: harvard_forest_warming] |

See [[concepts/warming-response-of-soil-microbial-community-composition]] and [[concepts/dna-versus-rna-pool-sensitivity-to-environmental-perturbation]].

### Lignin enrichment

The report used a 3-tier design with 999 permutations and Bray-Curtis distances. [src: lignin_community_enrichment] Bacterial and fungal results differ strongly in R².

| Model | Factor | Bacteria F, R², p | Fungi F, R², p |
|---|---|---|---|
| M1: Base vs R1 | group | 394.42, 0.992, 0.008 [src: lignin_community_enrichment] | 6.92, 0.698, 0.003 [src: lignin_community_enrichment] |
| M2: R2 factorial | group | 41.12, 0.939, 0.001 [src: lignin_community_enrichment] | 1.72, 0.424, 0.011 [src: lignin_community_enrichment] |
| M3: all 7 groups | group | 111.35, 0.979, 0.001 [src: lignin_community_enrichment] | 3.02, 0.582, 0.001 [src: lignin_community_enrichment] |

In the M2 bacterial model, R1 history gave F=14.31, R²=0.589, p=0.002. R2 labile C gave F=4.85, R²=0.327, p=0.018. [src: lignin_community_enrichment] See selective filtering of communities by lignin enrichment and [[concepts/small-sample-limits-in-community-amplicon-statistics]].

### Prophage modules

PERMANOVA on Bray-Curtis distances of prophage module composition (n=1,773 species subsample, 99 permutations) found three significant predictors. [src: prophage_ecology] Genome size quartile had F 212.99 (4 groups). [src: prophage_ecology] Environment had F 30.04 (10 groups). [src: prophage_ecology] Host family phylogeny had F 6.17 (294 groups). [src: prophage_ecology] See [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny]].

### Pseudomonas carbon pathway profiles

Among 54 free-living and plant-associated Pseudomonas species (>=5 genomes, >=60% majority environment agreement), a PERMANOVA-like permutation test with 999 permutations associated carbon profiles with isolation environment (p = 0.006). Between-group mean distance was 2.054 and within-group mean distance was 1.890. [src: pseudomonas_carbon_ecology] The test compared within-group and between-group Euclidean distances and gave a between/within ratio of 1.087 (p = 0.006). [src: pseudomonas_carbon_ecology] The report reads this as evidence of metabolic niche partitioning, because pathway composition is non-randomly associated with isolation environment even among free-living species. [src: pseudomonas_carbon_ecology] See [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle]].

### Soil metals and community COG profiles (db-RDA)

A db-RDA (distance-based redundancy analysis) gave R² = 0.799, p = 0.005 with 999 permutations. The report describes this as metal concentrations explaining 80% of variance in community COG (clusters of orthologous groups) profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics] The report argues the metal–functional gene association is not a statistical artefact of batch effects, because project accession was conditioned out. [src: soil_metal_functional_genomics] It also cautions that if project effects account for most of the variance, R² = 0.799 describes the residual variance, not the total. [src: soil_metal_functional_genomics] The unconditional R² for metals alone is not reported and may be substantially lower. [src: soil_metal_functional_genomics] Reporting it remains pending. [src: soil_metal_functional_genomics] See [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]].

### Related variance partitioning (not PERMANOVA)

The NB28 metal analysis is a separate method, not a PERMANOVA. It partitioned CLR (centered log-ratio) abundances of top-200 genera in n=5,000 MicrobeAtlas samples across metals (Cu, Zn, Pb, Ni) and pH+climate axes. [src: comprehensive_metal_ecology] All variables together explained R²=0.110. [src: comprehensive_metal_ecology] Unique metals explained R²=0.064, unique pH+climate R²=0.041 and shared R²=0.005. [src: comprehensive_metal_ecology] The report calls the metal fraction 58% larger, a reversal of the expectation that pH dominates. [src: comprehensive_metal_ecology] The R² values are unadjusted, come from a linear model without permutation testing, and are read descriptively. [src: comprehensive_metal_ecology]

## Plant compartments: location versus dispersion

PERMANOVA mixes location and dispersion effects, so the plant microbiome report added PERMDISP (permutational analysis of multivariate dispersions) and db-RDA (distance-based redundancy analysis). It ran them on 607 root, rhizosphere and phyllosphere species with a refined 17-marker panel and Jaccard distance. [src: plant_microbiome_ecotypes] PERMANOVA gave pseudo-F = 23.2, p = 0.001, R² = 0.071. [src: plant_microbiome_ecotypes] PERMDISP gave F = 15.6, p = 0.001. [src: plant_microbiome_ecotypes] Root was tightest (mean centroid distance 0.452), phyllosphere intermediate (0.503) and rhizosphere most variable (0.528). [src: plant_microbiome_ecotypes] db-RDA gave a location-only R² of 0.060 (p = 0.001). [src: plant_microbiome_ecotypes] A db-RDA on plant-compartment functional profiles is also reported as R² = 0.0595 (p = 0.001). [src: plant_microbiome_ecotypes] The location fraction was 0.060 / 0.071 = 84%. [src: plant_microbiome_ecotypes] About 84% of R² was centroid shift and 16% was dispersion. [src: plant_microbiome_ecotypes] The report still treats PERMANOVA R² as an upper bound because PERMDISP was significant. [src: plant_microbiome_ecotypes]

The original Phase 1 25-marker PERMANOVA gave R² = 0.527 (pseudo-F = 235.1, p = 0.001). [src: plant_microbiome_ecotypes] Excluding the top-3 species per compartment dropped it to 0.072, an 86% loss, and it stayed significant at p = 0.001. [src: plant_microbiome_ecotypes] The full 607-species v2 analysis matched this (0.071 vs 0.072). The report attributes the gap to the marker panel and genome-count distribution, not sample size. [src: plant_microbiome_ecotypes] It calls the 0.527 an inflated artifact of the panel and a few genome-rich species. [src: plant_microbiome_ecotypes] A separate NB08 PERMDISP found cohort dispersion heterogeneity (H=33.12, p=3.0e-7), so R²=0.53 may partly reflect variance differences. [src: plant_microbiome_ecotypes] PERMDISP also confirmed heterogeneity in functional profiles (F=15.6, p=0.001). [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]] and [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

## Tensions

- Well identity: it was not significant in sediment PERMANOVA (R² = 19.2%, p = 0.979). [src: enigma_sso_asv_ecology] It was dominant in groundwater (R² = 49.9%, p = 0.001). [src: enigma_sso_asv_ecology]
- Plant compartment R² was 0.527 on the Phase 1 panel and 0.071 on the refined panel. [src: plant_microbiome_ecotypes] The report calls the 0.527 an inflated artifact. [src: plant_microbiome_ecotypes]
- Soil db-RDA: the report reads R² = 0.799 as showing the association is not a batch artefact. [src: soil_metal_functional_genomics] The same report cautions that this conditional R² may describe only residual variance and that the unconditional R² is unreported. [src: soil_metal_functional_genomics]

## Open Directions

- Run PERMDISP alongside the SSO and Harvard Forest PERMANOVAs to check whether dispersion differences drive the R² values.
- Re-test the lignin pairwise contrasts with more replicates, since 3 vs 3 samples cannot give p below about 0.10.
- Permutation-test the NB28 metal versus pH+climate variance partition to see whether the metal-unique fraction still exceeds the pH+climate fraction.
- Increase the prophage permutations above 99 to resolve p-values finer than 0.01.
- Report the unconditional soil metals-only db-RDA R² next to the conditional 0.799.
- Run PERMDISP on the Pseudomonas carbon profiles to check whether dispersion differences contribute to the environment association.
