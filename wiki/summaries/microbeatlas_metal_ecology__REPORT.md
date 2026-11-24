---
type: "Summary"
description: "Summary of the project Metal Resistance Ecology — Phylogenetic Conservation vs. Environmental Selection."
doc_type: "short"
full_text: "sources/microbeatlas_metal_ecology__REPORT.md"
---
# Metal Resistance Ecology — Phylogenetic Conservation vs. Environmental Selection

This report asks whether metal resistance in bacteria tracks ancestry (phylogenetic conservation) or environmental selection, using niche breadth from [[entities/microbeatlas]] and phylogenetic generalized least squares (PGLS). Among the metal AMR (antimicrobial resistance) predictors, the number of distinct metal types resisted per genus is the only one that survives Bonferroni correction in the simple PGLS models. [src: microbeatlas_metal_ecology] The report's evolutionary readings are interpretations, not direct tests. [src: microbeatlas_metal_ecology]

## Key Findings

### Phylogenetic signal in niche breadth and metal resistance

Levins' B_std, the niche-breadth measure, shows strong phylogenetic signal across 1,264 bacterial genera with ≥ 3 OTUs (operational taxonomic units) in MicrobeAtlas. [src: microbeatlas_metal_ecology] Bacterial metal-AMR traits are ordered by phylogenetic signal: core fraction λ is above type diversity λ, which is above cluster count λ. The report reads this as consistent with mainly vertical inheritance of constitutive (core) resistance. In this reading, horizontal transfer and local metal exposure shape accessory gene accumulation and metal type expansion. This is an interpretation of the ordering. [src: microbeatlas_metal_ecology]

For contrast, nitrification (is_nitrifier) has near-maximal phylogenetic signal (λ = 0.939 in bacteria, λ = 1.000 in archaea). The report calls this consistent with ancient, vertically inherited metabolic entrenchment. [src: microbeatlas_metal_ecology]

### Metal diversity and niche breadth after accounting for ancestry

The raw OLS (ordinary least squares) correlation between mean metal type diversity and Levins' B_std is modest (r ≈ 0.21). The report says this reflects baseline phylogenetic structure in both variables. [src: microbeatlas_metal_ecology] The PGLS effect of metal diversity is +0.021 per SD (standard deviation) increase. It represents the additional covariation after the λ-transformed VCV matrix removes shared ancestry. [src: microbeatlas_metal_ecology]

Total AMR gene cluster count and core AMR fraction do not predict niche breadth in either the simple or the multi-predictor PGLS models. The report concludes that the breadth of the metal resistance repertoire, not its depth (many genes for few metals), is associated with ecological versatility. [src: microbeatlas_metal_ecology]

## Introduction; Key Findings; Results

This part of the report, the project `microbeatlas_metal_ecology` (status: complete; dated 2026-04-01, updated from 2026-03-26), asks whether genera with broader metal resistance repertoires also occupy broader ecological ranges after phylogeny is controlled. [src: microbeatlas_metal_ecology] Its main answer is that metal type diversity is associated with niche breadth beyond shared ancestry, while gene count and core fraction are not. [src: microbeatlas_metal_ecology]

### Question and approach

The report describes bacterial metal resistance as encoded by many genes for mercury, arsenic, copper, zinc, cadmium, chromium and nickel. Many sit on mobile genetic elements and move among taxa by horizontal gene transfer (HGT). [src: microbeatlas_metal_ecology] It claims to be the first global-scale, phylogenetically controlled test linking genus-level metal type diversity to niche breadth. The metal data come from AMRFinderPlus pangenome annotations across 6,789 GTDB species. Niche breadth comes from the 464,000-sample MicrobeAtlas 16S amplicon atlas. [src: microbeatlas_metal_ecology] Phylogenetic signal was partitioned and controlled with Pagel's λ and PGLS (phylogenetic generalized least squares). [src: microbeatlas_metal_ecology]

The headline result is that genera with broader metal type repertoires have significantly broader ecological ranges than phylogeny predicts. The report states that this holds across genome size, species richness, prevalence filtering, OTU (operational taxonomic unit) abundance filtering, and all 13 environment categories. [src: microbeatlas_metal_ecology] The raw ordinary least squares (OLS) correlation between mean metal type diversity and Levins' B_std is modest (r ≈ 0.21). The report attributes this to baseline phylogenetic structure in both variables. [src: microbeatlas_metal_ecology] See [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]] for the cross-project view.

### Phylogenetic signal

Pagel's λ was computed with `phytools::phylosig(method='lambda', test=TRUE)` against GTDB r214 genus-representative trees. λ = 0 means no phylogenetic signal (environmentally structured). λ = 1 means Brownian motion evolution (fully phylogenetically structured). [src: microbeatlas_metal_ecology] Bacterial Levins' B_std and number of environments, archaeal number of environments, and nitrification in both domains show strong signal (λ from 0.787 to 1.000). Archaeal Levins' B_std is weaker (λ = 0.197). Bacterial metal AMR (antimicrobial resistance) traits show weaker signal (λ from 0.260 to 0.441). [src: microbeatlas_metal_ecology]

| Group | Trait | Genera | λ | p (LRT) |
|---|---|---|---|---|
| Bacteria | Levins' B_std | 1,264 | 0.787 | 7.9×10⁻¹⁰² [src: microbeatlas_metal_ecology] |
| Archaea | Levins' B_std | 132 | 0.197 | 1.1×10⁻⁵ [src: microbeatlas_metal_ecology] |
| Bacteria | # environments | 1,264 | 0.909 | 1.4×10⁻¹⁵⁷ [src: microbeatlas_metal_ecology] |
| Archaea | # environments | 132 | 0.898 | 4.6×10⁻¹⁴ [src: microbeatlas_metal_ecology] |
| Bacteria | Nitrification | 2,286 | 0.939 | 2.5×10⁻¹⁰² [src: microbeatlas_metal_ecology] |
| Archaea | Nitrification | 132 | 1.000 | 2.5×10⁻⁵¹ [src: microbeatlas_metal_ecology] |
| Bacteria | AMR clusters | 606 | 0.260 | 6.1×10⁻²⁸ [src: microbeatlas_metal_ecology] |
| Bacteria | Core AMR fraction | 606 | 0.441 | 1.8×10⁻⁸ [src: microbeatlas_metal_ecology] |
| Bacteria | Metal types | 606 | 0.335 | 1.1×10⁻²³ [src: microbeatlas_metal_ecology] |
| Archaea | AMR clusters | 48 | ≈0 | 1.0 [src: microbeatlas_metal_ecology] |

LRT is the likelihood ratio test. The niche-breadth analysis covers 1,264 bacterial genera with ≥ 3 OTUs. [src: microbeatlas_metal_ecology] The archaeal AMR cluster result is a null, based on only 48 genera. [src: microbeatlas_metal_ecology]

The report reads the bacterial AMR ordering (core fraction λ above type diversity λ above cluster count λ) as consistent with a model. In that model, constitutive core resistance is mainly vertically inherited. Accessory accumulation and type expansion are shaped by horizontal transfer and local metal exposure. This is an interpretation, not a direct test. [src: microbeatlas_metal_ecology] It reads the near-maximal nitrification signal as consistent with ancient, vertically inherited metabolic entrenchment. [src: microbeatlas_metal_ecology]

### PGLS of niche breadth on metal resistance

The PGLS subset has 606 bacterial genera. Each has ≥ 3 OTUs, is in the GTDB r214 bacterial genus tree, and has metal AMR data from kbase_ke_pangenome. Predictors were z-scored. The Bonferroni threshold was p < 0.0083 for 6 simple models. [src: microbeatlas_metal_ecology] Models were fit jointly with λ by maximum likelihood (`ape::gls + nlme::corPagel`), with data sorted to tree tip order. [src: microbeatlas_metal_ecology]

Only metal type diversity predicts Levins' B_std after correction, and it is the only metal AMR predictor to survive Bonferroni. [src: microbeatlas_metal_ecology] Its effect (+0.021 per SD, standard deviation) is the covariation left after removing shared ancestry estimated by the λ-transformed VCV matrix. [src: microbeatlas_metal_ecology] The other five simple models are null at the Bonferroni threshold. [src: microbeatlas_metal_ecology]

| Response | Predictor | λ_PGLS | β | SE | p | ΔAIC | Bonferroni |
|---|---|---|---|---|---|---|---|
| Levins' B_std | Metal types | 0.708 | +0.021 | 0.0056 | 1.5×10⁻⁴ | −12.4 | yes [src: microbeatlas_metal_ecology] |
| Levins' B_std | AMR clusters | 0.700 | +0.010 | 0.0056 | 0.090 | −0.9 | no [src: microbeatlas_metal_ecology] |
| Levins' B_std | Core fraction | 0.701 | +0.003 | 0.0054 | 0.523 | +1.6 | no [src: microbeatlas_metal_ecology] |
| # environments | Core fraction | 0.839 | +0.142 | 0.069 | 0.038 | −2.3 | no [src: microbeatlas_metal_ecology] |
| # environments | AMR clusters | 0.847 | −0.071 | 0.067 | 0.290 | +0.9 | no [src: microbeatlas_metal_ecology] |
| # environments | Metal types | 0.848 | −0.007 | 0.071 | 0.923 | +2.0 | no [src: microbeatlas_metal_ecology] |

The metal-type effect appears for Levins' B_std but not for the number of environments. [src: microbeatlas_metal_ecology]

In the multi-predictor model of Levins' B_std with all 3 AMR predictors (λ = 0.706, AIC = −743.67), metal types stay significant (β = +0.023, SE = 0.0067, p = 5.5×10⁻⁴). [src: microbeatlas_metal_ecology] AMR clusters (β = −0.002, SE = 0.0065, p = 0.789) and core fraction (β = +0.006, SE = 0.0054, p = 0.288) are not significant. [src: microbeatlas_metal_ecology]

The report concludes that the breadth of the metal repertoire, not its depth (many genes for few metals), is associated with ecological versatility. [src: microbeatlas_metal_ecology]

## Robustness Analyses: R4. Prevalence-threshold niche breadth (addressable with existing …

The report ran five robustness analyses, which it says only partially address its main caveats. [src: microbeatlas_metal_ecology] This part covers the pangenome-coverage covariate and the analyses that follow it: rarefaction, an archaeal check, a strict prevalence threshold and a genome-size covariate. The bacterial metal-type effect survives the sampling-depth and genome-size controls. It loses nominal significance under the strict prevalence filter, which the report attributes mainly to lower sample size. [src: microbeatlas_metal_ecology]

### Pangenome coverage covariate

Adding z-scored n_species_with_amr as a fourth predictor controls for genome-sampling depth in the bacterial niche-breadth PGLS (phylogenetic generalized least squares). [src: microbeatlas_metal_ecology] Metal types stayed significant in both models, and n_species was borderline in both. [src: microbeatlas_metal_ecology]

| Model | Term | β | SE | p |
|---|---|---|---|---|
| B_std ~ types + n_species | Metal types (z) | +0.0204 | 0.0057 | 3.4×10⁻⁴ [src: microbeatlas_metal_ecology] |
| B_std ~ types + n_species | n_species (z) | +0.0093 | 0.0051 | 0.068 [src: microbeatlas_metal_ecology] |
| B_std ~ all 3 + n_species | Metal types (z) | +0.0224 | 0.0067 | 8.3×10⁻⁴ [src: microbeatlas_metal_ecology] |
| B_std ~ all 3 + n_species | n_species (z) | +0.0092 | 0.0051 | 0.070 [src: microbeatlas_metal_ecology] |

The report concludes that sampling depth makes a modest but non-dominant contribution and that genome count alone does not explain away the metal-type effect. [src: microbeatlas_metal_ecology]

### Pangenome rarefaction

To remove the genome-count bias formally, the report ran 200 PGLS iterations. In each, every genus was represented by one randomly sampled species from species_metal_amr.csv. [src: microbeatlas_metal_ecology] Of 606 bacterial PGLS genera, 383 had more than one species in the AMR (antimicrobial resistance) database. The other 223 were singletons and were unchanged by rarefaction. [src: microbeatlas_metal_ecology] The script was scripts/pgls_robustness.R. [src: microbeatlas_metal_ecology]

All 200 iterations completed. [src: microbeatlas_metal_ecology] The median β for metal types predicting B_std was +0.0147, with an interquartile range of +0.0126 – +0.0166. [src: microbeatlas_metal_ecology] The median p was 0.0054. [src: microbeatlas_metal_ecology] In 89.5% of iterations p was below 0.05, and 57.5% were Bonferroni-significant at p < 0.0083. [src: microbeatlas_metal_ecology] The median λ was 0.704. [src: microbeatlas_metal_ecology] The effect direction was consistent across all 200 iterations. [src: microbeatlas_metal_ecology]

The median β is smaller than the full-data estimate of +0.0215. The report calls this expected, because multi-species genera, which have higher inferred metal types, were reduced to one representative. It concludes that pangenome sampling depth does not explain the association. [src: microbeatlas_metal_ecology]

### Archaeal check

An exploratory archaeal PGLS in 48 genera found a positive but non-significant metal-types effect, β = +0.0145, p = 0.467. [src: microbeatlas_metal_ecology] The analysis had 11% power at α = 0.05. The report cautions that the result is not evidence against an association in archaea. [src: microbeatlas_metal_ecology]

### Strict prevalence threshold

The report recomputed niche breadth with a strict threshold. An OTU (operational taxonomic unit) counted as present in an environment only if it appeared in at least 5% of samples in that category. This aims to reduce detections from contamination, cross-sample bleed-through or rare transient events. [src: microbeatlas_metal_ecology] The filter shrank the data considerably, as the table shows.

| Metric [src: microbeatlas_metal_ecology] | Original | Strict (≥5%) |
|---|---|---|
| OTUs passing filter | 98,919 | 10,433 [src: microbeatlas_metal_ecology] |
| Genera with B_std estimate | 3,160 | 1,120 [src: microbeatlas_metal_ecology] |
| PGLS n (with AMR data) | 606 | 379 [src: microbeatlas_metal_ecology] |
| β (metal types → B_std) | +0.0215 | +0.0166 [src: microbeatlas_metal_ecology] |
| SE | 0.0056 | 0.0099 [src: microbeatlas_metal_ecology] |
| p | 1.5×10⁻⁴ | 0.092 [src: microbeatlas_metal_ecology] |
| λ | 0.708 | 0.526 [src: microbeatlas_metal_ecology] |

Original and strict B_std estimates correlated at Pearson r = 0.680. [src: microbeatlas_metal_ecology]

The effect lost statistical significance under the strict threshold. [src: microbeatlas_metal_ecology] The report attributes this mainly to the 37% drop in sample size (606 → 379), not to a change in direction or magnitude. β fell by 23%, from +0.0215 to +0.0166. [src: microbeatlas_metal_ecology] The report notes that the 5% threshold is conservative. It excludes 89% of OTUs, many genuinely distributed across environments but uncommon within any one. [src: microbeatlas_metal_ecology] It reads the result as suggesting that spurious rare detections do not entirely drive the signal. It adds that strict prevalence-based niche breadth needs substantially higher power. [src: microbeatlas_metal_ecology] It proposes a 1–2% threshold as a reasonable middle ground for future work. [src: microbeatlas_metal_ecology]

### Genome-size covariate

Genus-level mean genome size (bp) was retrieved from kbase_ke_pangenome.gtdb_metadata through the KBase Data Lakehouse REST (representational state transfer) API (application programming interface). It used one representative species per genus and covered 527 of 606 PGLS genera. Z-scored log(genome_size) was added as a covariate alongside metal-type diversity. [src: microbeatlas_metal_ecology] The script was scripts/pgls_genome_size.R. [src: microbeatlas_metal_ecology]

Metal types stayed significant after the adjustment (β = +0.0218, SE = 0.0061, p = 3.6×10⁻⁴, λ = 0.629). Genome size was also independently positive (β = +0.0263, SE = 0.0069, p = 1.5×10⁻⁴). [src: microbeatlas_metal_ecology] The genome-size-only baseline had β = +0.029, p = 2.7×10⁻⁵ and AIC = −630.3. [src: microbeatlas_metal_ecology] Adding metal types gave AIC = −641.1, so ΔAIC = 10.8 favors including them. [src: microbeatlas_metal_ecology]

The report concludes that the metal-type effect is not a genome-size artefact. It says metal resistance breadth has independent predictive power beyond total genomic complexity. [src: microbeatlas_metal_ecology] Caveat: 79 of 606 genera (13%) lacked genome-size data at query time, so n fell from 606 to 527. Direction and significance agreed with the full-data models. [src: microbeatlas_metal_ecology]

## Robustness Analyses; Extended Sensitivity Analyses

This part of the report tests whether the bacterial metal-diversity and niche-breadth association survives three further checks. The checks are a three-covariate phylogenetic generalized least squares (PGLS) model, leave-one-metal-out refits and leave-one-environment-out refits. The association survives the covariate model and the environment exclusions. It loses significance when any single metal is dropped. The report says a distributed signal and a near-threshold result pushed below significance by a compressed predictor range cannot be told apart without a larger metal type vocabulary. [src: microbeatlas_metal_ecology]

### Three-covariate PGLS (genome size and species richness)

The report merged species counts per genus from GTDB r214 taxonomy (all 606 genera present) with mean genome size from kbase_ke_pangenome.gtdb_metadata (527 of 606 genera). It fit B_std ~ metal_types_z + log_n_species_z + log_genome_size_z in n = 527 genera. [src: microbeatlas_metal_ecology] The model had λ = 0.628. [src: microbeatlas_metal_ecology] Metal types stayed significant (β = +0.0218, SE = 0.0061, t = 3.60, p = 3.5×10⁻⁴). [src: microbeatlas_metal_ecology] The report gives q = 0.003 by Benjamini-Hochberg false discovery rate (BH-FDR). [src: microbeatlas_metal_ecology] Genome size was also significant (β = +0.0255, SE = 0.0069, t = 3.68, p = 2.6×10⁻⁴). [src: microbeatlas_metal_ecology] log(n_species) was not significant (β = +0.0052, SE = 0.0057, t = 0.90, p = 0.366). [src: microbeatlas_metal_ecology]

The report reads the loss of the species-richness effect as partial mediation by genome size, because larger genera tend to have larger genomes. [src: microbeatlas_metal_ecology] It concludes that the metal-type effect is not an artefact of genome complexity or sequencing depth. [src: microbeatlas_metal_ecology] The mediation reading is the report's interpretation.

### Leave-one-metal-out

Four extra sensitivity analyses were run to address specific methodological concerns. [src: microbeatlas_metal_ecology] In the first, the report recomputed species-level metal type counts without each of 7 metals (Hg, As, Cu, Zn, Cd, Cr, Ni). It then aggregated the counts to genus and reran PGLS. [src: microbeatlas_metal_ecology] The original model with all 7 metals gave β = +0.0215, SE = 0.0056, p = 1.5×10⁻⁴. [src: microbeatlas_metal_ecology]

No exclusion kept significance, and all seven models had p > 0.10. [src: microbeatlas_metal_ecology] Every coefficient stayed positive. [src: microbeatlas_metal_ecology]

| Metal excluded | β | SE | p |
|---|---|---|---|
| Hg | +0.0082 | 0.0069 | 0.233 [src: microbeatlas_metal_ecology] |
| As | +0.0039 | 0.0061 | 0.518 [src: microbeatlas_metal_ecology] |
| Cu | +0.0102 | 0.0065 | 0.115 [src: microbeatlas_metal_ecology] |
| Zn | +0.0095 | 0.0064 | 0.140 [src: microbeatlas_metal_ecology] |
| Cd | +0.0084 | 0.0064 | 0.186 [src: microbeatlas_metal_ecology] |
| Cr | +0.0088 | 0.0064 | 0.173 [src: microbeatlas_metal_ecology] |
| Ni | +0.0095 | 0.0064 | 0.140 [src: microbeatlas_metal_ecology] |

The report reads this consistency as an effect spread across the metal-type spectrum rather than driven by one dominant metal. [src: microbeatlas_metal_ecology] It also expects some power loss, because each exclusion cuts the maximum diversity score from 7 to 6 and compresses predictor variance. [src: microbeatlas_metal_ecology] It states a caveat. The pattern fits a truly distributed signal. It also fits an original result near the threshold that the compressed range pushed below it. The consistently positive β favours the distributed reading. The two cannot be separated without a larger metal type vocabulary. [src: microbeatlas_metal_ecology] See also [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects]].

### Leave-one-environment-out

The report excluded each of 13 MicrobeAtlas categories in turn. It row-normalised prevalences over the remaining 12 environments, recomputed B_std with J=12 and reran PGLS. [src: microbeatlas_metal_ecology] All 13 models stayed significant at p < 0.05. The association therefore does not depend on any single environment category. [src: microbeatlas_metal_ecology]

| Environment excluded | β | SE | p | λ |
|---|---|---|---|---|
| agricultural | +0.0107 | 0.0040 | 0.0073 | 0.883 [src: microbeatlas_metal_ecology] |
| aquatic | +0.0085 | 0.0039 | 0.031 | 0.880 [src: microbeatlas_metal_ecology] |
| desert | +0.0120 | 0.0042 | 0.0040 | 0.913 [src: microbeatlas_metal_ecology] |
| farm | +0.0115 | 0.0042 | 0.0061 | 0.873 [src: microbeatlas_metal_ecology] |
| field | +0.0118 | 0.0040 | 0.0030 | 0.868 [src: microbeatlas_metal_ecology] |
| flower | +0.0118 | 0.0044 | 0.0077 | 0.898 [src: microbeatlas_metal_ecology] |
| forest | +0.0142 | 0.0042 | 0.0007 | 0.874 [src: microbeatlas_metal_ecology] |
| leaf | +0.0130 | 0.0043 | 0.0025 | 0.893 [src: microbeatlas_metal_ecology] |
| paddy | +0.0123 | 0.0042 | 0.0036 | 0.898 [src: microbeatlas_metal_ecology] |
| peatland | +0.0131 | 0.0044 | 0.0027 | 0.890 [src: microbeatlas_metal_ecology] |
| plant | +0.0105 | 0.0039 | 0.0069 | 0.882 [src: microbeatlas_metal_ecology] |
| shrub | +0.0126 | 0.0043 | 0.0034 | 0.887 [src: microbeatlas_metal_ecology] |
| soil | +0.0113 | 0.0039 | 0.0035 | 0.889 [src: microbeatlas_metal_ecology] |

Excluding aquatic gave the weakest model. Aquatic is the most heterogeneous and over-represented category, with 40,353 operational taxonomic units (OTUs) and 40.8% of the dataset. Excluding it cut β from +0.021 to +0.0085 (−59%), and p stayed at 0.031. [src: microbeatlas_metal_ecology] The three least-sampled environments were flower (898 OTUs, 0.9%), leaf (1,298 OTUs, 1.3%) and plant (2,647 OTUs, 2.7%). Excluding them gave β of +0.012, +0.013 and +0.010, all p < 0.008. [src: microbeatlas_metal_ecology]

The report notes that λ was higher in these runs (0.87–0.91) than in the main analysis (0.71). It attributes this to fewer categories, which raise the relative weight of shared environments and amplify phylogenetic covariation in the rescaled B_std. [src: microbeatlas_metal_ecology]

### Aquatic interpretation and limits

The report treats aquatic over-representation as a possible source of downward bias when aquatic is included. It also notes that excluding aquatic weakens β, which suggests aquatic OTUs contribute disproportionately to the association. [src: microbeatlas_metal_ecology] It reads this as consistent with metal-contaminated coastal, estuarine and hydrothermal waters supplying many broad-niche, metal-tolerant genera. [src: microbeatlas_metal_ecology] On that basis it calls the aquatic-exclusion result a conservative lower bound on the true association. [src: microbeatlas_metal_ecology] These are interpretations, not tests.

One limit remains. MicrobeAtlas has no finer environment classes, so the report cannot test heterogeneity within a category, such as marine versus freshwater. That would need niche breadth recomputed with a revised environment taxonomy. [src: microbeatlas_metal_ecology]

The metal-exclusion and environment-exclusion analyses both come from scripts/pgls_sensitivity.R. [src: microbeatlas_metal_ecology]

## Extended Sensitivity Analyses: S4. Log(n_species) as PGLS covariate: metal types robust …

This part of the report tests three possible confounders of the bacterial niche-breadth results: variance in metal types within genera, genome-count coverage, and rare OTU detections. The first two tests ask whether the metal-diversity and niche-breadth association survives. [src: microbeatlas_metal_ecology] The third asks whether the phylogenetic conservation of niche breadth (Pagel's λ) survives, which is a different result. [src: microbeatlas_metal_ecology]

### Within-genus variance in metal types

The report added the within-genus standard deviation (SD) of n_metal_types across species, z-scored, as a covariate to the main phylogenetic generalized least squares (PGLS) model. [src: microbeatlas_metal_ecology] With this control, z-scored mean metal types stayed associated with niche breadth (β = +0.0189, SE = 0.0060, p = 0.0016). [src: microbeatlas_metal_ecology] The SD term itself was not significant (z-scored SD β = +0.0074, SE = 0.0055, p = 0.181). [src: microbeatlas_metal_ecology] The report concludes that a few outlier species do not push genera into the high-diversity category in a way that inflates the niche-breadth association. [src: microbeatlas_metal_ecology] The analysis is in scripts/pgls_sensitivity.R, Analysis 3. [src: microbeatlas_metal_ecology]

### Log-transformed genome count

The report raised a concern about its earlier coverage adjustment (R1). That adjustment used a linear n_species_with_amr covariate, but genome-count effects are typically log-linear, so it may have been underpowered. [src: microbeatlas_metal_ecology] The report also clarifies that R1 already used PGLS (gls() with corPagel), not only ordinary least squares (OLS). [src: microbeatlas_metal_ecology] The new analysis adds z-scored log1p(n_species_with_amr) alongside metal types. [src: microbeatlas_metal_ecology]

After this adjustment, metal types stayed significant in the bacterial niche-breadth PGLS (β = +0.0195, SE = 0.0057, p = 6.4×10⁻⁴). [src: microbeatlas_metal_ecology] Without the adjustment the p-value was 1.5×10⁻⁴. [src: microbeatlas_metal_ecology] Log(n_species) was itself significant (β = +0.0127, SE = 0.0053, p = 0.016), whereas the linear covariate in R1 was borderline (p = 0.07). [src: microbeatlas_metal_ecology]

The report reads this as a log-linear relationship. Well-sampled genera tend to have slightly broader niches, possibly because they include more ecologically diverse isolates. [src: microbeatlas_metal_ecology] The metal-type coefficient dropped only from +0.021 to +0.020, so the report concludes that the predictor carries independent signal beyond sequencing depth. [src: microbeatlas_metal_ecology] It also states that metal types retain a ΔAIC of approximately −10 beyond a log(n_species)-only model. It notes that a partial R² decomposition would need a likelihood-ratio test (LRT). [src: microbeatlas_metal_ecology] This analysis is Analysis 4 of scripts/pgls_sensitivity.R. [src: microbeatlas_metal_ecology]

### Filtering low-abundance OTUs

The report flagged a concern that low-abundance operational taxonomic units (OTUs), possibly spurious detections, could inflate niche breadth and bias Pagel's λ for B_std. [src: microbeatlas_metal_ecology] This test checks λ for niche breadth, not the metal-diversity association. The report estimated per-OTU mean relative abundance as total_counts / (n_detected_samples × mean_library_size). Mean library size was total_reads / total_samples, or 87,595 reads/sample across 463,972 samples. [src: microbeatlas_metal_ecology]

OTUs with mean relative abundance < 0.01% were excluded. This removed 66% of OTUs and left 34% = 33,676 OTUs. [src: microbeatlas_metal_ecology] Of these, 23,759 were bacterial non-organellar OTUs covering 576 of 606 PGLS genera, and genus-level B_std was recomputed on this set. [src: microbeatlas_metal_ecology] The original Pagel's λ analysis used 1,264 bacterial genera, and the filtered subset used 576. [src: microbeatlas_metal_ecology]

- All OTUs, original analysis: λ = 0.787, LRT p = 7.9×10⁻¹⁰². [src: microbeatlas_metal_ecology]
- Unfiltered OTUs, same 576 genera: λ = 0.763, LRT p = 5.9×10⁻⁴⁰. [src: microbeatlas_metal_ecology]
- Abundance-filtered: λ = 0.750, LRT p = 2.8×10⁻⁴⁰. [src: microbeatlas_metal_ecology]

The report gives the change in λ as −0.013 (−1.7%). [src: microbeatlas_metal_ecology] It concludes that the phylogenetic conservation of niche breadth is not an artefact of rare transient OTU detections. [src: microbeatlas_metal_ecology] This analysis was run as inline Python, with output in data/pgls_subset_filtered_otus.csv. [src: microbeatlas_metal_ecology]

## Study Design and Inferential Framework: Multiple testing count

This part of the report separates its confirmatory analyses from its exploratory ones. It then checks the primary result against multiple-testing correction, reconciles two estimates of phylogenetic signal, and sets out how far the result can be interpreted. The primary result holds under every correction the report applies. The report treats its robustness work as reassurance, not as confirmation. [src: microbeatlas_metal_ecology]

### Confirmatory versus exploratory analyses

The primary confirmatory hypothesis asked whether metal AMR (antimicrobial resistance) trait diversity predicts bacterial niche breadth after phylogenetic correction. The report says it was tested before residuals and interaction effects were examined. [src: microbeatlas_metal_ecology] The confirmatory set is the 6 simple PGLS (phylogenetic generalized least squares) models in NB05, with Bonferroni correction, plus Pagel's λ for niche and AMR traits in NB04. [src: microbeatlas_metal_ecology] The exploratory set is the multi-predictor PGLS, robustness analyses R1–R4, sensitivity analyses S1–S4, archaeal PGLS, and every analysis added during post-hoc review. [src: microbeatlas_metal_ecology]

The robustness analyses came after the main analysis, in response to anticipated reviewer concerns. The report says they should be read as reassurance, not as confirmatory evidence. [src: microbeatlas_metal_ecology] The primary result (metal types → B_std, p = 1.5×10⁻⁴, Bonferroni-corrected) stands on its own regardless of them. [src: microbeatlas_metal_ecology] The report recommends that future studies preregister the primary hypothesis, analysis plan and sample size before collecting data. [src: microbeatlas_metal_ecology]

### Multiple-testing inventory

The report's inventory of tests is:

- Simple PGLS (confirmatory): 6 tests, Bonferroni (α/6 = 0.0083). [src: microbeatlas_metal_ecology]
- Pagel's λ (confirmatory): 6 tests, LRT (likelihood ratio test), no additional correction. [src: microbeatlas_metal_ecology]
- Multi-predictor PGLS: 3 predictors in 1 model, not corrected beyond the model. [src: microbeatlas_metal_ecology]
- Robustness R1–R2, R4–R6: 9 coefficients, exploratory only. [src: microbeatlas_metal_ecology]
- Archaeal PGLS R3 (supplementary): 3 coefficients, exploratory only. [src: microbeatlas_metal_ecology]
- Sensitivity S1–S5: 24 coefficients, exploratory only. [src: microbeatlas_metal_ecology]
- OTU (operational taxonomic unit) abundance filter S5 (Pagel's λ): 1 test, exploratory only. [src: microbeatlas_metal_ecology]

### Correction across all 47 tests

The primary result survives a Bonferroni correction for the full 47-test family (threshold 0.05/47 ≈ 0.0011). This was not the stated correction method. The report calls it an upper bound on conservatism. [src: microbeatlas_metal_ecology] Benjamini-Hochberg FDR (false discovery rate) correction across all 47 tests gives 23 significant tests at q < 0.05. [src: microbeatlas_metal_ecology] The full table is in data/all_tests_fdr.csv. [src: microbeatlas_metal_ecology]

All bacterial metal type diversity effects survive FDR correction. The q-values are:

- Simple PGLS B_std: q = 0.0028. [src: microbeatlas_metal_ecology]
- Multi-predictor PGLS: q = 0.0037. [src: microbeatlas_metal_ecology]
- R1 covariate models: q < 0.004. [src: microbeatlas_metal_ecology]
- R5 genome size covariate: q = 0.0028. [src: microbeatlas_metal_ecology]
- 3-covariate PGLS: q = 0.0028. [src: microbeatlas_metal_ecology]
- S3 within-genus SD (standard deviation): q = 0.007. [src: microbeatlas_metal_ecology]
- S4 log(n_species): q = 0.0037. [src: microbeatlas_metal_ecology]

Some results do not survive. The S2 leave-one-environment-out models are significant at q < 0.05 for 12 of 13 environments. [src: microbeatlas_metal_ecology] The exception is the model excluding aquatic environments, with q = 0.061 despite nominal p = 0.031. [src: microbeatlas_metal_ecology] The S1 leave-one-metal-out models do not survive FDR correction. The report attributes this to reduced predictor variance when one metal is excluded. [src: microbeatlas_metal_ecology] Archaeal PGLS stays non-significant (q = 0.55). [src: microbeatlas_metal_ecology]

### Standalone versus PGLS-estimated λ

Bacterial B_std has a standalone Pagel's λ of 0.787 (NB04) and a PGLS-estimated λ of 0.708 (NB05). The difference is Δλ = 0.079, which the report calls expected and informative. [src: microbeatlas_metal_ecology] Standalone λ is the phylogenetic signal in B_std without a predictor. It measures how much of B_std's total variance Brownian-motion phylogenetic covariance explains. [src: microbeatlas_metal_ecology] PGLS λ is the residual signal after the variance explained by metal type diversity is removed. [src: microbeatlas_metal_ecology]

The report explains the lower PGLS λ by the predictor's own phylogenetic signal (λ_metal_types = 0.335). Including it as a covariate removes some phylogenetically structured variance from the residuals. [src: microbeatlas_metal_ecology] The report reads the drop of about 10% as metal type diversity accounting for approximately 10% of B_std's phylogenetic covariance. [src: microbeatlas_metal_ecology] It says this fits a model in which metal resistance breadth is one of several phylogenetically structured predictors of niche breadth, not the sole driver. [src: microbeatlas_metal_ecology] The residual λ = 0.708 (p ≪ 0.001) shows strong residual signal, which the report says supports the PGLS architecture. [src: microbeatlas_metal_ecology] It finds no evidence of model misspecification from the difference. [src: microbeatlas_metal_ecology]

### Interpretation and causal limits

The PGLS coefficient is a partial correlation after phylogenetic correction, not a causal estimate. [src: microbeatlas_metal_ecology] The report offers three scenarios, which are proposals and not tested results:

1. Metal tolerance enables habitat expansion, because taxa with diverse resistance can colonise chemically diverse environments. [src: microbeatlas_metal_ecology]
2. Ecological generalism enables gene acquisition, because broad-niche genera meet more environments, more HGT (horizontal gene transfer) donors and higher metal concentrations. [src: microbeatlas_metal_ecology]
3. A shared driver, such as genome size, metabolic versatility or biofilm capacity, promotes both broad niches and diverse metal tolerance. [src: microbeatlas_metal_ecology]

The cross-sectional design uses observational global survey data. It cannot establish the direction of the association. [src: microbeatlas_metal_ecology] Telling the scenarios apart would need time-series genomic data on metal resistance and range shifts, or longitudinal metal-enrichment experiments on defined communities. [src: microbeatlas_metal_ecology]

Total AMR cluster count is non-significant while metal type diversity is significant. The report says this slightly favours scenario 1 or 3 over a genome-size-only explanation. A genome-size-only driver would predict a significant cluster count, since that count scales more directly with genome size. [src: microbeatlas_metal_ecology] In R5, metal type diversity stays independently significant after genome-size adjustment (β = +0.022, p = 3.6×10⁻⁴). The report reads this as ruling out genome size as the primary confounder. [src: microbeatlas_metal_ecology] The association nonetheless remains correlational, and its direction cannot be established without time-series data or a natural experiment. [src: microbeatlas_metal_ecology] The report concludes that genera with diverse metal resistance repertoires are, on average, broader ecological generalists in the global microbiome. [src: microbeatlas_metal_ecology]

## Study Design and Inferential Framework; Interpretation

This part of the report sets out how the phylogenetic and annotation analyses were built, what limits they carry, and how the authors interpret the results. The report did not test the tree against alternatives and did no manual validation of annotations. [src: microbeatlas_metal_ecology]

### Phylogenetic framework

All PGLS and Pagel's λ analyses use the GTDB r214 genus-representative tree, built from 120 concatenated marker genes. [src: microbeatlas_metal_ecology] The report calls this the current field standard for bacterial phylogenetics and the best available reconciliation of phylogenomic signal with 16S taxonomy. [src: microbeatlas_metal_ecology] Pruning keeps one tip per genus, chosen as the GTDB species cluster representative, which the report calls standard in macro-ecological PGLS studies of this scale. [src: microbeatlas_metal_ecology]

Two limits apply. Genus-level pruning discards within-genus phylogenetic structure. [src: microbeatlas_metal_ecology] Sensitivity analysis S3 partly compensates: within-genus SD (standard deviation) of metal types was not a significant PGLS covariate (p = 0.18). The report reads this as confirming that genus aggregation does not hide a species-level confound. [src: microbeatlas_metal_ecology] The report did not test NCBI trees, SILVA-based 16S trees or a different GTDB release, and it names this as a methodological gap. [src: microbeatlas_metal_ecology] A 16S-based tree would align more directly with the 16S-derived niche breadth values but has lower resolution at genus level. [src: microbeatlas_metal_ecology]

### Metal annotation and its validation

Metal AMR (antimicrobial resistance) annotations use AMRFinderPlus HMM-based detection against the NCBI Bacterial AMR Reference Gene Database. [src: microbeatlas_metal_ecology] For metals, it uses curated Hidden Markov Models built from experimentally validated sequences, such as merA/merB for mercury, arsABCDR for arsenate and copABCD for copper. [src: microbeatlas_metal_ecology] Gathering thresholds are set during calibration to balance sensitivity and specificity. No extra identity threshold is applied, because HMM scores are not identity values. [src: microbeatlas_metal_ecology]

The report lists several annotation risks:
- Structurally similar metalloproteases or ABC (ATP-binding cassette) transporters could be misclassified as metal resistance proteins. AMRFinderPlus taxon-specific cutoffs are used to reduce this. [src: microbeatlas_metal_ecology]
- The "other" metal category makes up 17% of annotated clusters and captures metal-associated genes outside the 7 primary types. It may include weaker hits. [src: microbeatlas_metal_ecology]
- Excluding "other" would give a 6-metal analysis (Hg, As, Cu, Zn, Cd, Cr, Ni only). [src: microbeatlas_metal_ecology]
- No manual validation of a subset of annotations was performed. [src: microbeatlas_metal_ecology]

Support for the annotations is informal. Spot checks of the prevalent families arsD and merP showed expected distributions, high in contaminated-environment genera and lower in strict aerobes. [src: microbeatlas_metal_ecology] The report recommends randomly sampling 100 annotated gene clusters for manual BLAST verification against the original protein sequences, to quantify the false positive rate. [src: microbeatlas_metal_ecology] Leave-one-metal-out analysis S1 shows that the result needs contributions from several metal types. Spurious annotations in a single category therefore would not explain it. [src: microbeatlas_metal_ecology]

### Interpretation: metal diversity and niche breadth

The positive association between metal type diversity and niche breadth (β = +0.021 SD per SD, Bonferroni-corrected) is consistent, in the report's view, with a metabolic versatility hypothesis. [src: microbeatlas_metal_ecology] Under that hypothesis, genera with diverse metal tolerance repertoires, for example Hg detoxification, As efflux and Cu oxidation, are associated with broader ecological ranges across the global microbiome. [src: microbeatlas_metal_ecology] The report also hypothesizes that broad metal tolerance may proxy overall environmental tolerance. Environments that impose multi-metal stress, such as polymetallic mine tailings, estuarine sediments and biosolid-amended agricultural soils, are also chemically complex in redox gradients, salinity and organic carbon variation. [src: microbeatlas_metal_ecology]

The effect is specific to metal diversity. Total gene burden and core fraction do not show the niche breadth effect. [src: microbeatlas_metal_ecology] Genera with many AMR genes for a single metal type are not ecological generalists, but genera spanning multiple metal resistance families are. [src: microbeatlas_metal_ecology] The report says this parallels other stress domains, where breadth rather than depth of stress response predicts biogeographic range. [src: microbeatlas_metal_ecology] It cites Qi et al. (2022), who independently found that multiple heavy metal contamination favours generalists as network keystones in soil. [src: microbeatlas_metal_ecology]

### Interpretation: phylogenetic signal

Niche breadth and habitat range are more phylogenetically conserved than metal AMR traits in bacteria (λ_niche ≈ 0.79–0.91 vs λ_AMR ≈ 0.26–0.44). [src: microbeatlas_metal_ecology] The report reads this gradient as lineage-constrained ecological range and more labile metal AMR. It proposes that AMR genes sit on mobile genetic elements (MGE) and are exchanged among distant taxa. [src: microbeatlas_metal_ecology] It cites Hemme et al. (2016), who showed recombinational hotspots for metal resistance gene acquisition in contaminated groundwater. [src: microbeatlas_metal_ecology] It also cites Gillieatt & Coleman (2024), who reviewed AMR gene transfer by MGEs under metal co-selection. [src: microbeatlas_metal_ecology] The significant metal-type PGLS β, despite control for intermediate phylogenetic signal, is read as HGT-driven metal type expansion covarying with niche breadth beyond phylogenetic relatedness. [src: microbeatlas_metal_ecology]

Standalone Pagel's λ for B_std is 0.787, against 0.708 within the PGLS. The report explains the drop by metal type diversity, which itself carries signal (λ_metal_types = 0.335) and removes some phylogenetically structured variance. [src: microbeatlas_metal_ecology]

Nitrification is a metabolic positive control, with λ = 0.94–1.00 in both domains. Its genes for ammonia and nitrite oxidation are described as deep, vertically inherited innovations defining major lineages such as Nitrospirota and Thaumarchaeota. Their near-maximal λ contrasts with the intermediate metal AMR signal. [src: microbeatlas_metal_ecology]

### Archaea

Archaeal niche breadth also shows significant phylogenetic signal (B_std λ = 0.197, p = 1.1×10⁻⁵; n_envs λ = 0.898, p = 4.6×10⁻¹⁴). [src: microbeatlas_metal_ecology] The B_std λ is notably lower than the bacterial value. The report calls this consistent with the phylogenetically sparse and ecologically distinct archaeal genera sampled by short-read 16S amplicon surveys. [src: microbeatlas_metal_ecology] It cites Jiao et al. (2021), who found phylogenetic niche conservatism in soil archaea, particularly for moisture niche. The report takes this as support for a real rather than artefactual signal. [src: microbeatlas_metal_ecology]

### Consistency with the literature

The report judges each of the following consistent with its results:

| Report result | Literature | Report's verdict |
|---|---|---|
| Bacterial niche breadth λ = 0.787 | Malfertheiner et al. (2026): community conservatism widespread across phyla [src: microbeatlas_metal_ecology] | Consistent |
| Soil prokaryote niche breadth conserved | Hernandez et al. (2023): conserved multidimensional specialization in soil prokaryotes [src: microbeatlas_metal_ecology] | Consistent |
| Metal type diversity → broader niche (PGLS) | Qi et al. (2022): heavy metal contamination favors generalists [src: microbeatlas_metal_ecology] | Consistent (orthogonal evidence) |
| Intermediate metal AMR λ (0.26–0.44) | Hemme et al. (2016): LGT hotspots for metal resistance [src: microbeatlas_metal_ecology] | Consistent |
| Core fraction λ > total cluster count λ | Gillieatt & Coleman (2024): core and accessory metal AMR differ in MGE association [src: microbeatlas_metal_ecology] | Consistent |
| PGLS β significant for metal type diversity | Ma et al. (2025): generalists have broader metal tolerance repertoire in coastal sediment [src: microbeatlas_metal_ecology] | Consistent |

## Interpretation; Limitations

This part of the report interprets the metal-diversity and niche-breadth result and sets out its limits. It argues that the link is novel and survives several robustness checks. It also states that the evidence rests on inferred traits and uneven data, not on measured physiology. [src: microbeatlas_metal_ecology]

### Interpretation

The report says it is the first analysis to link genus-level metal type diversity, inferred from pangenome antimicrobial resistance (AMR) annotations across 6,789 species, to global niche breadth from a 464K-sample 16S atlas, with phylogenetic control by phylogenetic generalized least squares (PGLS). [src: microbeatlas_metal_ecology] It joins a pangenome database of 6,789 sequenced species across the GTDB bacterial tree with a global atlas of 98,919 OTUs (operational taxonomic units) × 463,972 samples. The report says this gives a taxonomic and geographic scope that site-specific studies lack. [src: microbeatlas_metal_ecology]

Earlier site-specific studies found generalist taxa enriched in metal-contaminated environments. They could not tell whether total gene burden, core resistance or breadth of metal type coverage was the relevant variable. [src: microbeatlas_metal_ecology] The global PGLS identifies metal type diversity, not gene count or core fraction, as the predictor of niche breadth. [src: microbeatlas_metal_ecology] Pagel's λ was 0.26–0.44 for AMR metrics and 0.79–0.91 for niche breadth. The report uses this to separate vertically inherited resistance repertoires from horizontally acquired accessory genes. [src: microbeatlas_metal_ecology] It concludes that the horizontally labile diversity component is the one that covaries with ecological range. [src: microbeatlas_metal_ecology]

### Niche-breadth measurement limits

MicrobeAtlas detection across 13 environment categories confounds habitat use with sampling intensity, V3–V4 or V4 primer bias, and uneven geographic and temporal SRA/ENA contributions. [src: microbeatlas_metal_ecology] Densely sampled soil, marine and plant environments can inflate apparent niche breadth relative to deep subsurface, brine and ice taxa. [src: microbeatlas_metal_ecology] Levins' B_std corrects for unequal environment sizes. It cannot correct for missing environments or differing detection probabilities. [src: microbeatlas_metal_ecology] Correcting primer bias and missing environments would need a multi-primer, multi-region survey design. [src: microbeatlas_metal_ecology]

Genus-level aggregation is a proxy. A genus may look broad-niched because different species occupy different habitats. [src: microbeatlas_metal_ecology] The PGLS β reflects covariation between inferred niche breadth and inferred metal tolerance capacity, not confirmed physiology. [src: microbeatlas_metal_ecology]

A stricter 5% within-environment prevalence threshold for B_std kept the positive direction (β = +0.017 vs +0.022 original). It reduced significance, because 37% fewer genera passed the filter. [src: microbeatlas_metal_ecology] The report concludes that rare transient detections do not explain the effect. [src: microbeatlas_metal_ecology]

### Aquatic category

MicrobeAtlas's 13 broad categories lump heterogeneous habitats. "Aquatic" combines marine, freshwater, estuarine, hydrothermal vent and pond environments. [src: microbeatlas_metal_ecology] A taxon found in both a marine coastal and a freshwater lake sample counts as broad-niched, although this could reflect related but ecologically distinct ecotypes. [src: microbeatlas_metal_ecology] Excluding aquatic gives p = 0.031, the weakest of all 13 exclusions but still significant. [src: microbeatlas_metal_ecology] Excluding any other environment gives p < 0.01, so the report states the result does not depend on the aquatic category. [src: microbeatlas_metal_ecology] Splitting aquatic into marine, freshwater and saline subcategories needs sample metadata re-analysis. That metadata is not available in the current KBase Data Lakehouse extraction. [src: microbeatlas_metal_ecology]

### Genome sampling depth

Sequenced genome count per genus correlates with inferred metal type diversity (Spearman r = 0.35, p = 2.6×10⁻¹⁹). [src: microbeatlas_metal_ecology] Single-genome genera have lower metal type counts than multi-genome genera (Mann-Whitney p = 5.1×10⁻¹⁰). [src: microbeatlas_metal_ecology] The result nevertheless survives several controls:

- With n_species_with_amr as a PGLS covariate, metal type diversity stays significant (β = +0.020, p = 3.4×10⁻⁴). [src: microbeatlas_metal_ecology] The linear pangenome-coverage covariate is borderline (p = 0.07), which the report reads as a modest, non-dominant sampling effect. [src: microbeatlas_metal_ecology]
- Rarefying to 1 species per genus over 200 iterations gives p < 0.05 in 89.5% of iterations, with median β (+0.015) in the same direction. [src: microbeatlas_metal_ecology]
- With z-scored log(n_species) as a covariate, metal types stay significant (p = 6.4×10⁻⁴). Log(n_species) is itself significant (p = 0.016), which confirms a log-linear genome-count effect. [src: microbeatlas_metal_ecology]
- Adding log(n_species) moves the metal type β from +0.021 to +0.020. The report reads this as a small confound with independent effects. [src: microbeatlas_metal_ecology]

A formal pangenome rarefaction curve over several species-per-genus thresholds would quantify the coverage-depth effect more precisely. [src: microbeatlas_metal_ecology] The report marks the genome-size covariate limitation as addressed by robustness analysis R5. [src: microbeatlas_metal_ecology]

### Archaea

Only 48 archaeal genera had both MicrobeAtlas representation (≥ 3 OTUs) and AMR data in kbase_ke_pangenome. [src: microbeatlas_metal_ecology] The archaeal PGLS gave a nonsignificant, positive metal-type coefficient (β = +0.0145, p = 0.467). Its standard errors exceed the coefficient, which the report attributes to severe underpowering, not a true null. [src: microbeatlas_metal_ecology] Power is 11% at α=0.05, so the report warns against reading the result as negative evidence. [src: microbeatlas_metal_ecology]

The report includes the result only to quantify the statistical gap, not as evidence for or against the hypothesis. [src: microbeatlas_metal_ecology] It says stricter readers may treat the section as a power-analysis appendix, not an attempted replication. [src: microbeatlas_metal_ecology] The 48 genera are biased toward cultured methanogens, halophiles and thermoacidophiles. They miss the environmentally dominant MicrobeAtlas archaea, including Thaumarchaeota and Woesearchaeota. [src: microbeatlas_metal_ecology] Adequate power needs ≥200 archaeal genera with AMR data, which requires expanded archaeal pangenome sequencing and annotation. [src: microbeatlas_metal_ecology]

### Trait distribution assumptions

Metal type diversity is an integer count from 1 to 7. The report uses it as a continuous z-scored predictor in a Gaussian PGLS. [src: microbeatlas_metal_ecology] The Gaussian assumption applies to the B_std residuals, not to the metal-type distribution. The report says PGLS residuals should be inspected for normality. [src: microbeatlas_metal_ecology]

If metal type count were the response, a Poisson or negative binomial PGLS would be appropriate (phylolm with Poisson family, or MCMCglmm). [src: microbeatlas_metal_ecology] The Pagel's λ analysis of metal_types assumes Brownian motion with Gaussian increments, which approximates an integer trait. [src: microbeatlas_metal_ecology] Discrete-state (Mk) or threshold models are alternatives, but they are not standard for this continuous-trait PGLS analysis. [src: microbeatlas_metal_ecology]

## Data: Generated Data

This part of the report states where the project's data and code are stored and lists the derived files it provides. Derived data and code are committed to an institutional repository, and a public Zenodo archive with a citable DOI has not yet been prepared. [src: microbeatlas_metal_ecology]

### Availability and reproducibility

Derived CSV files, notebooks and scripts are committed to the BERIL Research Observatory institutional repository. [src: microbeatlas_metal_ecology] A public Zenodo archive with a citable DOI has not yet been prepared. [src: microbeatlas_metal_ecology] Raw source data stay in the KBase Data Lakehouse (`arkinlab_microbeatlas`, `kbase_ke_pangenome`) and are accessible to KBase users. [src: microbeatlas_metal_ecology] The GTDB r214 reference tree is publicly available at https://gtdb.ecogenomic.org/. [src: microbeatlas_metal_ecology] The environment specification for the R analyses is in `projects/microbeatlas_metal_ecology/requirements.txt`. [src: microbeatlas_metal_ecology]

### Source tables

The `arkinlab_microbeatlas` tables `otu_metadata`, `otu_counts_long` and `sample_metadata` supply niche breadth and taxonomy for 98,919 operational taxonomic units (OTUs) across 463,972 samples. [src: microbeatlas_metal_ecology] The `kbase_ke_pangenome` tables `bakta_amr`, `gene_cluster` and `gtdb_species_clade` supply species-level metal antimicrobial resistance (AMR) annotations and GTDB taxonomy. [src: microbeatlas_metal_ecology]

### Derived data files

**Trait tables and phylogenetic signal**

| File | Rows | Contents |
|---|---|---|
| `data/species_metal_amr.csv` | 6,789 | Species-level metal AMR metrics (NB01) [src: microbeatlas_metal_ecology] |
| `data/otu_niche_breadth.csv` | 98,919 | Levins' B_std and n_envs per OTU (NB02) [src: microbeatlas_metal_ecology] |
| `data/otu_pangenome_link.csv` | 22,357 | OTU → GTDB genus mapping (NB03) [src: microbeatlas_metal_ecology] |
| `data/genus_trait_table.csv` | 3,160 | Genus-level trait table: niche + AMR + taxonomy (NB04) [src: microbeatlas_metal_ecology] |
| `data/pagel_lambda_results.csv` | 10 | Pagel's λ per trait × domain (NB04) [src: microbeatlas_metal_ecology] |

**Phylogenetic generalized least squares (PGLS) models and sensitivity analyses**

| File | Rows | Contents |
|---|---|---|
| `data/pgls_subset.csv` | 606 | Filtered genus subset for PGLS (NB05) [src: microbeatlas_metal_ecology] |
| `data/pgls_results.csv` | 6 | Simple PGLS model results (NB05) [src: microbeatlas_metal_ecology] |
| `data/pgls_multi_results.csv` | 3 | Multi-predictor PGLS coefficients (NB05) [src: microbeatlas_metal_ecology] |
| `data/pgls_robustness_results.csv` | 9 | Covariate + archaeal PGLS robustness results [src: microbeatlas_metal_ecology] |
| `data/pgls_rarefied_summary.csv` | 1 | Summary of 200-iteration rarefied PGLS [src: microbeatlas_metal_ecology] |
| `data/pgls_prevalence_threshold_result.csv` | 1 | Strict-prevalence-threshold PGLS result [src: microbeatlas_metal_ecology] |
| `data/pgls_sensitivity_results.csv` | 24 | Extended sensitivity analysis results (S1–S4) [src: microbeatlas_metal_ecology] |
| `data/genus_genome_size.csv` | 527 | Genus-level mean genome size (bp) from the KBase Data Lakehouse kbase_ke_pangenome (R5) [src: microbeatlas_metal_ecology] |
| `data/pgls_genome_size_result.csv` | 2 | PGLS coefficients with genome size covariate (R5) [src: microbeatlas_metal_ecology] |
| `data/pgls_3covariate_result.csv` | 3 | 3-covariate PGLS (metal types + log_n_species + log_genome_size) (R6) [src: microbeatlas_metal_ecology] |
| `data/pgls_subset_filtered_otus.csv` | 576 | PGLS subset with OTU-filtered B_std (≥0.01% rel. abund.) (S5) [src: microbeatlas_metal_ecology] |
| `data/all_tests_fdr.csv` | 47 | All hypothesis tests with Benjamini-Hochberg false discovery rate (BH-FDR) q-values [src: microbeatlas_metal_ecology] |

**Candidates and hypotheses**

The candidate file `data/candidate_otu_list.csv` has 435 rows: OTUs in the top 10% by niche breadth × metal diversity (n=215) plus nitrifier positive controls (n=220). It includes a `top10pct_both` flag and a `nitrifier_role` column. [src: microbeatlas_metal_ecology]

| File | Rows | Contents |
|---|---|---|
| `data/metal_resistance_table_refined.csv` | 15 | Refined genus-level metal resistance: top candidate genera with ≤2 key genes per metal type, representative OTU identifier (ID), and metal types [src: microbeatlas_metal_ecology] |
| `data/hypotheses_refined.md` | — | Per-genus testable hypotheses with specific metal condition, OTU ID, ≥2-fold quantitative prediction, mechanistic basis, and falsification criterion [src: microbeatlas_metal_ecology] |
| `data/honorable_mentions.md` | — | 2,186 genera with metal AMR gene annotations but zero candidate OTUs (not in top-10% by both metrics) [src: microbeatlas_metal_ecology] |

**ENIGMA groundwater validation**

| File | Rows | Contents |
|---|---|---|
| `data/groundwater_enrichment.csv` | 2,135 | Genus-level groundwater prevalence (n_gw_samples, %, fold enrichment) joined to metal AMR traits (ENIGMA Validation Track A) [src: microbeatlas_metal_ecology] |
| `data/enigma_geochemistry.csv` | 20 | PRJNA1084851 SRA experiment summaries fetched via NCBI EUtils (metadata-only archive) [src: microbeatlas_metal_ecology] |
| `data/enigma_otu_table.csv` | 133 samples × 24,295 OTUs | PRJNA1084851 full OTU table (97% OTU clustering, SILVA 138; raw FASTQs deleted post-processing) [src: microbeatlas_metal_ecology] |
| `data/enigma_otu_taxonomy.csv` | 24,295 | OTU taxonomy assignments (domain → genus) for PRJNA1084851 [src: microbeatlas_metal_ecology] |
| `data/enigma_full_metadata.csv` | 133 | Per-sample BioSample attributes (ENIGMA_ID, well, date, experiment, fraction, replicate) [src: microbeatlas_metal_ecology] |
| `data/enigma_cwm_per_sample.csv` | 133 | Community-weighted mean metal-type diversity per sample, joined to well/time metadata [src: microbeatlas_metal_ecology] |

## Supporting Evidence; Experimental Validation Framework

This part of the report turns the global comparative result into a testable plan. It selects candidate MicrobeAtlas OTUs, ranks eight for microcosm experiments, and states falsifiable predictions for each. [src: microbeatlas_metal_ecology] The predictions are hypotheses. The report presents no experimental result for them in these claims.

### Experimental aim and candidate selection

The report extends its global analysis into controlled microcosm experiments that would test its core finding: multi-metal resistance breadth predicts ecological generalism. [src: microbeatlas_metal_ecology] From 98,919 MicrobeAtlas OTUs, it identifies 435 candidates for experimental tracking. [src: microbeatlas_metal_ecology] The candidates have two parts. [src: microbeatlas_metal_ecology]

- 215 OTUs fall in the top 10% by both standardised niche breadth (Levins' B_std ≥ 0.718) and mean metal-type diversity (n_metal_types ≥ 2.0). The report describes them as the frontier of the niche breadth × metal diversity distribution. [src: microbeatlas_metal_ecology]
- 220 nitrifier OTUs serve as positive controls. They come from Nitrosomonas, Nitrosopumilus, Nitrososphaera, Nitrospira, Nitrobacter, Nitrococcus, Nitrosospira and Nitrospina. [src: microbeatlas_metal_ecology]

The report does not expect the metal AMR (antimicrobial resistance)–niche breadth link to apply to the nitrifiers, because nitrification is phylogenetically entrenched (λ = 0.94). [src: microbeatlas_metal_ecology] Sample counts confirm that the candidate OTUs span 13 environment types globally. The full list is in `data/candidate_otu_list.csv`. [src: microbeatlas_metal_ecology]

### Eight-OTU shortlist

The report prioritises eight OTUs by a composite score, Levins' B_std × n_metal_types. Each OTU represents a distinct metal-type signature. [src: microbeatlas_metal_ecology] The table gives Levins' B, metal types and the recommended stress for each OTU.

| Priority | OTU | Genus | Levins' B | Metal types | Recommended stress |
|---|---|---|---|---|---|
| 1 | `97_56843` | Klebsiella | 0.947 | 3.5 | Ag or Te [src: microbeatlas_metal_ecology] |
| 2 | `97_51587` | Enterococcus | 0.948 | 3.3 | Cu or Cd [src: microbeatlas_metal_ecology] |
| 3 | `97_14443` | Citrobacter | 0.854 | 3.7 | As or Hg [src: microbeatlas_metal_ecology] |
| 4 | `97_3668` | Franconibacter | 0.785 | 3.5 | Ag or As [src: microbeatlas_metal_ecology] |
| 5 | `97_12431` | Noviherbaspirillum | 0.770 | 3.0 | As [src: microbeatlas_metal_ecology] |
| 6 | `97_66129` | Serratia | 0.923 | 2.4 | Hg [src: microbeatlas_metal_ecology] |
| 7 | `97_80244` | Aeromonas | 0.981 | 2.2 | As + Hg co-stress [src: microbeatlas_metal_ecology] |
| 8 | `97_39338` | Pseudomonas | 0.999 | 2.1 | Cu [src: microbeatlas_metal_ecology] |

Three genus-level points stand out. Citrobacter tops metal-type diversity (3.7 types) and is linked to `silP/A, arsC/D, chrA, merA/P`. [src: microbeatlas_metal_ecology] Enterococcus (Ag, As, Cd, Cu, Hg, Te) and Klebsiella (Ag, As, Hg, Te) are the broadest multi-metal resisters. [src: microbeatlas_metal_ecology] Pseudomonas ranks eighth by composite score but has the highest niche breadth of all candidate genera (B_std = 0.999). [src: microbeatlas_metal_ecology] It also carries a complete `copA/pco` Cu-resistance operon. [src: microbeatlas_metal_ecology]

### Predictions and falsification

Each of the 8 shortlisted OTUs has a specific, falsifiable prediction in `data/hypotheses_refined.md`. [src: microbeatlas_metal_ecology] The consolidated document is `ENIGMA_PREDICTIONS.md`. [src: microbeatlas_metal_ecology] The template hypothesis is that, under a specific metal stress, an OTU carrying the relevant resistance determinants should increase in relative abundance by ≥2-fold versus metal-free controls after 7–14 days. The reasoning is that the determinants neutralise metal toxicity while susceptible competitors are inhibited. [src: microbeatlas_metal_ecology]

The report also gives falsification criteria. If an OTU does not increase, candidate explanations are (a) the resistance genes sit on accessory elements absent from the soil ecotype, or (b) the metal concentration exceeds the allele-specific MIC. [src: microbeatlas_metal_ecology]

### Supporting code and checks

- Analysis notebooks: `01_metal_amr_species.ipynb` extracts species-level metal AMR metrics from AMRFinderPlus annotations. [src: microbeatlas_metal_ecology] `02_niche_breadth.ipynb` computes Levins' B_std and n_envs from 260M OTU × sample observations. [src: microbeatlas_metal_ecology] `03_taxonomy_bridge.ipynb` links MicrobeAtlas OTU genera to GTDB genus representatives. [src: microbeatlas_metal_ecology] `04_pagel_lambda.ipynb` estimates Pagel's λ with nitrification as a positive control. [src: microbeatlas_metal_ecology] `05_pgls_regression.ipynb` runs PGLS (phylogenetic generalized least squares) of metal AMR predictors on niche breadth. [src: microbeatlas_metal_ecology]
- Robustness scripts: `pgls_robustness.R` implements covariate PGLS, a 200-iteration rarefaction and an archaeal PGLS. [src: microbeatlas_metal_ecology] `pgls_sensitivity.R` implements leave-one-metal-out, leave-one-environment-out, within-genus SD (standard deviation) and log(n_species) analyses. [src: microbeatlas_metal_ecology]
- Ordering test: `test_pgls_ordering.py` passes. On synthetic data with λ = 0.8 and β = 0.05 and scrambled rows, sorted PGLS recovers the correct λ and β within tolerance, and unsorted PGLS fails. [src: microbeatlas_metal_ecology]
- Candidate and design scripts: `make_candidate_otu_list.py` builds the candidate list, flags the top 10% on both axes and appends the nitrifier controls. [src: microbeatlas_metal_ecology] `refine_metal_resistance.py` produces per-genus metal types, at most 2 key genes per metal, and hypotheses with falsification criteria. [src: microbeatlas_metal_ecology] `feasibility_assessment.py` produces a power analysis, detection limits, the 8-OTU shortlist and an ENIGMA experimental design recommendation. [src: microbeatlas_metal_ecology] `package_enigma_predictions.py` produces the consolidated predictions document. [src: microbeatlas_metal_ecology]
- Field validation: `enigma_validation.py` runs a Track A groundwater enrichment in the KBase Data Lakehouse, using Spearman ρ and Mann-Whitney tests on 767 genera × 1,624 groundwater samples. [src: microbeatlas_metal_ecology] See [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater]].
- Sequencing pipeline: `prjna1084851_pipeline.py` processes 81 samples through ENA download, cutadapt trimming, vsearch merging, 97% OTU clustering and SILVA 138 taxonomy. [src: microbeatlas_metal_ecology] `prjna1084851_recover.py` recovers the 52 samples not mirrored to ENA FTP. [src: microbeatlas_metal_ecology]
- Dashboard: `interactive_dashboard.py` produces a three-panel standalone Plotly dashboard with a world map, a niche-breadth scatter and a Pagel's λ bar chart. [src: microbeatlas_metal_ecology]

## Experimental Validation Framework; ENIGMA Validation: Groundwater Enrichment Analysis

This part of the report sets out a proposed ENIGMA metal-stress experiment. It then tests the core PGLS (phylogenetic generalized least squares) finding against 1,624 groundwater samples, and it builds an OTU (operational taxonomic unit) table from the ENIGMA ORFRC (Oak Ridge Field Research Center) study PRJNA1084851. The groundwater test confirms a modest association between metal-type breadth and prevalence. It finds no groundwater-specific enrichment. [src: microbeatlas_metal_ecology]

### Experimental design and power

The design rests on a stated detection limit and a power estimate. The detection limit is ≥ 0.1% relative abundance, which is ≥ 10 reads at 10,000 reads/sample. [src: microbeatlas_metal_ecology] OTUs initially at 1% abundance are quantified with CV (cross-validation) ≈ 10%. [src: microbeatlas_metal_ecology] For such OTUs the power to detect a 2-fold increase is >99% with 3 replicates at 10,000 reads. The report names multiple testing, not sensitivity, as the binding constraint. [src: microbeatlas_metal_ecology]

The proposed experiment uses 4–6 metal-stress treatments × 5 replicates × 7- and 14-day time points. Its primary endpoint is relative abundance fold-change versus a metal-free control. [src: microbeatlas_metal_ecology] The report recommends these steps for the inoculum and the OTU set:
- Sequence the inoculum before treatment, with 5 replicates at ≥ 50,000 reads/sample. [src: microbeatlas_metal_ecology]
- Keep 3–5 priority OTUs that are detectable at ≥ 0.1%. [src: microbeatlas_metal_ecology]
- Apply FDR (false discovery rate) correction within that set only. [src: microbeatlas_metal_ecology]

If OTU-level tracking fails, the report proposes two alternatives. One is genus-specific 16S qPCR for Pseudomonas, Citrobacter and Enterococcus. The other is a defined synthetic community of 8–12 priority taxa. [src: microbeatlas_metal_ecology]

The report cites three studies as support. Farkas et al. (2023) saw community shifts within 7 days in As(III) microcosms, which fits the 7–14-day design. [src: microbeatlas_metal_ecology] Kou et al. (2018) showed selective OTU-level enrichment under Pb/Zn/Cu in a field trial. [src: microbeatlas_metal_ecology] Yuan et al. (2020) found that copper reduces OTU richness in freshwater microcosms. The report reads this as amplifying the advantage of Cu-resistant taxa such as Pseudomonas OTU 97_39338. [src: microbeatlas_metal_ecology]

### Groundwater observational validation (Track A)

The test uses 1,624 groundwater samples (Env_Level_2 = "groundwater") from arkinlab_microbeatlas in the KBase Data Lakehouse. [src: microbeatlas_metal_ecology] OTU × sample counts came through the REST (representational state transfer) API, by joining otu_counts_long and sample_metadata. [src: microbeatlas_metal_ecology] The prediction was that genera with broader metal-type resistance repertoires, if they are ecological generalists, would be more prevalent across chemically challenging groundwater samples. [src: microbeatlas_metal_ecology]

The analysis subset has 767 genera. Each has ≥1 OTU detected in groundwater and non-null mean_n_metal_types. [src: microbeatlas_metal_ecology] Prevalence is the mean fraction of groundwater samples in which ≥1 OTU of the genus was detected. [src: microbeatlas_metal_ecology] Fold enrichment is groundwater prevalence % divided by non-groundwater prevalence % across 462,348 samples. [src: microbeatlas_metal_ecology] Quartile thresholds are Q1 ≤ 1.0 and Q4 ≥ 1.5 metal types. [src: microbeatlas_metal_ecology]

Metal-type breadth is associated with prevalence but not with enrichment. Metal types correlate with groundwater prevalence (Spearman ρ = +0.112, 767 genera, p = 0.0019). [src: microbeatlas_metal_ecology] They do not correlate significantly with fold enrichment (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] Top-Q4 and bottom-Q1 genera (213 vs 429) differ in prevalence (Mann-Whitney p = 0.007). [src: microbeatlas_metal_ecology] They do not differ in fold enrichment (p = 0.181). [src: microbeatlas_metal_ecology]

Median prevalence is 0.81% for Q4 genera and 0.62% for Q1 genera (ratio 1.31×; one-sided Mann-Whitney p = 0.007). [src: microbeatlas_metal_ecology] The report calls the effect modest. It treats it as consistent with the global PGLS β being a partial correlation after removing phylogenetic structure. [src: microbeatlas_metal_ecology]

The report calls the lack of fold-enrichment signal a meaningful null. Track A confirms the prevalence association but not groundwater-specific enrichment. [src: microbeatlas_metal_ecology] It offers two explanations: a general breadth effect, or too little power in the 1,624-sample subset. [src: microbeatlas_metal_ecology] It also states that Track A is consistent with the PGLS finding but does not uniquely support a metal-contamination mechanism. [src: microbeatlas_metal_ecology] Even so, it presents Track A as an independent field-observation cross-validation using a different data source. [src: microbeatlas_metal_ecology] See [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater]] and [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]].

### ENIGMA candidate genera

The candidate table reports groundwater prevalence (%), fold enrichment versus non-groundwater, and mean metal types per genus:
- Azospira: 5.21, 2.3×, 3.0 metal types. [src: microbeatlas_metal_ecology]
- Enterobacter: 4.80, 1.1×, 3.1 metal types. [src: microbeatlas_metal_ecology]
- Citrobacter: 0.89, 2.8×, 3.7 metal types. [src: microbeatlas_metal_ecology]
- Enterococcus: 0.71, 2.8×, 3.3 metal types. [src: microbeatlas_metal_ecology]
- Noviherbaspirillum: 1.01, 1.4×, 3.0 metal types. [src: microbeatlas_metal_ecology]
- Franconibacter: 0.39, 1.6×, 3.5 metal types. [src: microbeatlas_metal_ecology]
- Pseudomonas: 2.1 metal types, with no prevalence or enrichment estimate because it is not in the top-15. [src: microbeatlas_metal_ecology]

The report reads the 2.8× enrichment of Citrobacter and Enterococcus as consistent with its ENIGMA predictions. [src: microbeatlas_metal_ecology] It describes Azospira as a denitrifier detected in 5.2% of groundwater samples. Azospira has the highest prevalence among high-metal-diversity genera and an established role in groundwater nitrogen cycling. [src: microbeatlas_metal_ecology]

### PRJNA1084851 ENIGMA ORFRC amplicon data (Track B)

The Track B pipeline finished all 133 of 133 samples and yielded 24,295 OTUs. [src: microbeatlas_metal_ecology] The study is the ENIGMA-funded ORFRC Tennessee Water Research 2024 paper, "Reproducible responses of geochemical and microbial successional patterns in the subsurface to carbon source amendment" (doi:10.1016/j.watres.2024.121460). It deposited 133 MiSeq 16S runs, SRR28246018–SRR28246150. [src: microbeatlas_metal_ecology]

The pipeline used cutadapt 5.2 primer trimming, vsearch 2.30.6 paired-end merging and 97% OTU clustering, and SILVA 138 taxonomy. [src: microbeatlas_metal_ecology] Of the samples, 81 came via ENA FTP. The other 52 came via NCBI fasterq-dump v3.4.1, because they were not yet mirrored to ENA. [src: microbeatlas_metal_ecology]

The final table has 133 samples × 24,295 OTUs, with a median of 56,908 reads/sample. [src: microbeatlas_metal_ecology] Of these OTUs, 14,021 have genus-level taxonomy. [src: microbeatlas_metal_ecology] Separately, 1,637 OTUs, representing 16.8% of reads, could be joined to genus metal diversity data. [src: microbeatlas_metal_ecology]

BioSample attributes describe two experiments. EVO09 has 52 samples from Jan 2009. EVO17 has 81 samples from 2017–2018. [src: microbeatlas_metal_ecology] They cover 8 groundwater monitoring wells (FW202, FW215, FW216, GP01, GP03, MLSA3, MLSB3, MLSG4) at ENIGMA ORFRC, Oak Ridge, Tennessee. [src: microbeatlas_metal_ecology] All samples were collected at 0.2 µm filtration. [src: microbeatlas_metal_ecology] Replicate codes R0–R20 represent successive time points before and after ethanol carbon amendment. [src: microbeatlas_metal_ecology]

CWM (community weighted mean) metal-type diversity is the abundance-weighted mean of genus-level mean_n_metal_types across OTUs with AMR (antimicrobial resistance) data. These OTUs average 16.8% of reads per sample. [src: microbeatlas_metal_ecology] Sample CWM ranged from 1.01–1.83, with mean 1.28 ± 0.19. [src: microbeatlas_metal_ecology] This coverage is a limit: the remaining ~83% of reads come from genera without SILVA-to-GTDB AMR taxonomy matches, and CWM excludes them. [src: microbeatlas_metal_ecology]

## ENIGMA Validation: Groundwater Enrichment Analysis: Track B: PRJNA1084851 (ENIGMA ORFRC …

The evidence is correlational. The report notes that robustness to coverage has not been formally tested. [src: microbeatlas_metal_ecology]

### CWM across wells, time and sampling groups

CWM differed across 8 wells (Kruskal-Wallis H = 29.10, n = 133 samples, p = 0.0001). [src: microbeatlas_metal_ecology] It correlated positively with time point (Spearman ρ = +0.383, n = 133, p < 0.0001). [src: microbeatlas_metal_ecology] Within well FW216 the correlation was stronger (Spearman ρ = +0.576, n = 40, p = 0.0001). [src: microbeatlas_metal_ecology] CWM also differed between EVO09 (n = 52) and EVO17 (n = 81) in a Mann-Whitney test (p = 0.0012). The report gives no U statistic. [src: microbeatlas_metal_ecology]

Median CWM by well, from high to low:

| Well | Median CWM |
|---|---|
| FW215 | 1.37 [src: microbeatlas_metal_ecology] |
| FW216 | 1.36 [src: microbeatlas_metal_ecology] |
| GP01 | 1.23 [src: microbeatlas_metal_ecology] |
| GP03 | 1.22 [src: microbeatlas_metal_ecology] |
| MLSB3 | 1.14 [src: microbeatlas_metal_ecology] |
| MLSA3 | 1.09 [src: microbeatlas_metal_ecology] |
| FW202 | 1.08 [src: microbeatlas_metal_ecology] |
| MLSG4 | 1.08 [src: microbeatlas_metal_ecology] |

Wells FW215 and FW216 are known to lie within the U/NO₃ contamination plume at the Oak Ridge Field Research Center (ORFRC). [src: microbeatlas_metal_ecology] The report reads their higher CWM as consistent with the hypothesis that metal-contaminated subsurface environments select for genera with broader metal resistance repertoires. [src: microbeatlas_metal_ecology]

### Interpretation of the temporal rise

The report suggests that carbon amendment progressively selects metal-diverse communities. It proposes, as a possible mechanism, reducing conditions that shift the speciation of redox-active U, Fe and S. [src: microbeatlas_metal_ecology] It concludes that the rise in CWM after amendment points to active ecological selection for metal-diverse communities under geochemical stress. [src: microbeatlas_metal_ecology] The mechanism is presented as a possibility. [src: microbeatlas_metal_ecology]

### Candidate genera

Sulfurimonas is a sulfur-oxidizing chemolithotroph and the dominant flagged genus, with 80 OTUs (operational taxonomic units) and 96.2% prevalence. [src: microbeatlas_metal_ecology] Its relative abundance fell with time (Spearman ρ = −0.323, n = 133, p = 0.0002). [src: microbeatlas_metal_ecology] The report proposes that carbon amendment depletes nitrate and oxygen, its preferred electron acceptors. [src: microbeatlas_metal_ecology] It presents Sulfurimonas as a counterexample: a prevalent generalist whose abundance follows electron-acceptor availability rather than metal resistance. Not all dominant groundwater taxa are therefore metal-diverse. [src: microbeatlas_metal_ecology]

Nitrospira (25 OTUs, 88.7% prevalence) was most abundant in plume well FW215. [src: microbeatlas_metal_ecology] Candidatus Jorgensenbacteria (Patescibacteria/CPR, candidate phyla radiation; 122 OTUs, 99.2% prevalence) was ubiquitous. [src: microbeatlas_metal_ecology] Citrobacter and Thermodesulfovibrio were not detected. They may have been below detection, or their genus names may not match SILVA nomenclature. [src: microbeatlas_metal_ecology]

### Caveats

CWM would be biased upward if uncovered genera were systematically more metal-sensitive than covered genera. [src: microbeatlas_metal_ecology] The between-sample CWM variance (1.01–1.83) and the correlation with plume status fit real biology. Robustness to variation in coverage fraction has not been formally tested. [src: microbeatlas_metal_ecology] The report recommends correlating per-sample CWM with per-sample covered-read fraction before the metric is used further. [src: microbeatlas_metal_ecology]

## Future Directions; Peer Review Query Index

This part of the report lists proposed follow-up analyses and reports which reviewer queries were already addressed. It also records the ENIGMA field validation, which the report treats as complete. Some proposals have since been done (R5 genome size, ENIGMA Tracks A and B). Others are open, and the report states several gaps itself. [src: microbeatlas_metal_ecology]

### Proposed future analyses

The report proposes work on confounders, mechanism, validation and annotation quality.

- **Genome-sampling depth:** Resample genera to equal genome coverage (for example n = 1 or 2 species) and repeat PGLS (phylogenetic generalized least squares). [src: microbeatlas_metal_ecology] This needs a species-level AMR (antimicrobial resistance) table stratified by genome count. [src: microbeatlas_metal_ecology]
- **Archaea:** Expand archaeal coverage in kbase_ke_pangenome with environmental metagenome-assembled genomes (MAGs), particularly Thaumarchaeota. Repeat PGLS once at least 100 archaeal genera have AMR data. [src: microbeatlas_metal_ecology] See [[concepts/statistical-power-and-database-coverage-gap-for-archaeal-trait-analyses]].
- **Genome size:** The report marks this item as done. Robustness Analysis R5 added genus-level mean genome size from kbase_ke_pangenome.gtdb_metadata to PGLS. The metal type diversity effect stayed independent of genome size (ΔAIC = 10.8). [src: microbeatlas_metal_ecology] R5 gave metal types β = +0.022 (p = 3.6×10⁻⁴). [src: microbeatlas_metal_ecology]
- **Accessory genome:** Estimate genus-level pangenome openness, defined as the proportion of genes in the accessory genome. Use it with metal type diversity to predict niche breadth. [src: microbeatlas_metal_ecology] The report hypothesizes that a broader accessory genome may drive both niche breadth and metal type diversity. [src: microbeatlas_metal_ecology]
- **Site-level validation:** Test whether MicrobeAtlas genera with high metal type diversity are enriched in mining-impacted, biosolid-amended and estuarine samples versus clean references. The report says this would directly validate the environmental co-selection hypothesis. [src: microbeatlas_metal_ecology]
- **Co-resistance clustering:** Group metal types by genetic co-occurrence, such as Cu-Zn versus Hg-As. Test whether specific combinations predict niche breadth better than the raw count. [src: microbeatlas_metal_ecology]
- **Count models:** Apply MCMCglmm with Poisson or negative binomial families. These would test whether niche breadth predicts metal type count in the reverse regression direction. [src: microbeatlas_metal_ecology]
- **Environment taxonomy:** Re-run niche breadth with finer categories, such as splitting aquatic into marine, freshwater and estuarine. This tests whether category heterogeneity inflates B_std for certain genera. [src: microbeatlas_metal_ecology]
- **Annotation validation:** Randomly sample 100 annotated metal AMR gene clusters for manual BLAST verification against reference sequences. This would quantify the HMM-based false positive rate for each metal type. [src: microbeatlas_metal_ecology]
- **Data archive:** Deposit notebooks, derived CSVs and a conda lockfile in Zenodo. Archive the data/*.csv and figures/*.png files under a citable DOI before manuscript submission. [src: microbeatlas_metal_ecology]

### ENIGMA field validation

The report states that ENIGMA Tracks A and B are complete and produced a candidate OTU (operational taxonomic unit) list and shortlist. [src: microbeatlas_metal_ecology] It also states that both tracks independently confirm the PGLS prediction in field data. [src: microbeatlas_metal_ecology] See [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater]].

- **Track A:** In 1,624 KBase Data Lakehouse groundwater samples, metal-diverse genera were significantly more prevalent in groundwater (Spearman ρ = +0.112, p = 0.0019; Mann-Whitney p = 0.007). [src: microbeatlas_metal_ecology] Top-quartile metal-diversity genera were 31% more prevalent in groundwater. [src: microbeatlas_metal_ecology]
- **Track B pipeline:** The amplicon pipeline ran on all 133 PRJNA1084851 samples, giving 24,295 OTUs and 133/133 QC (quality control) pass. [src: microbeatlas_metal_ecology]
- **Track B plume wells:** Community-weighted mean (CWM) metal-type diversity was significantly higher in contamination-plume wells FW215/FW216 (Kruskal-Wallis p = 0.0001). [src: microbeatlas_metal_ecology]
- **Track B carbon amendment:** CWM metal-type diversity rose with time after carbon amendment across all wells (Spearman ρ = +0.383, p < 0.0001). [src: microbeatlas_metal_ecology] In FW216 alone the correlation was ρ = +0.576 (p = 0.0001). [src: microbeatlas_metal_ecology]

### Peer review query index

The report's query index shows reviewer queries handled in several ways: some addressed with results, some partly, and some acknowledged as gaps. [src: microbeatlas_metal_ecology]

**Addressed with results**
- The report states that the metal-type β remains significant after PGLS covariate adjustment for pangenome coverage. [src: microbeatlas_metal_ecology] R1 and S4 both use gls() + corPagel PGLS, not OLS (ordinary least squares). [src: microbeatlas_metal_ecology]
- All 7 single-metal exclusions gave positive associations, so no one metal drives the result. [src: microbeatlas_metal_ecology] See [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects]].
- Within-genus heterogeneity was non-significant in S3, which confirms genus means are not inflated by outlier species. [src: microbeatlas_metal_ecology]
- R2 rarefaction shows a consistent positive direction. [src: microbeatlas_metal_ecology]
- The PGLS λ discrepancy of Δλ = 0.079 is expected given the predictor's own phylogenetic signal. [src: microbeatlas_metal_ecology]
- The report tabulates 47 tests and applies BH-FDR (Benjamini-Hochberg false discovery rate) across all of them. The primary result survives Bonferroni (α/47=0.0011) and FDR (q=0.003). [src: microbeatlas_metal_ecology]
- A unit test, scripts/test_pgls_ordering.py, generates synthetic data and scrambles order. It verifies that the sorted model recovers correct λ and β, and it passes. [src: microbeatlas_metal_ecology]
- The report claims novelty for the phylogenetic partitioning of core versus type diversity and for the global pangenome × atlas × PGLS integration. [src: microbeatlas_metal_ecology]
- Archaeal PGLS results moved to a Supplementary section. Main-text R3 keeps only a summary pointer. [src: microbeatlas_metal_ecology]

**Limits and acknowledged gaps**
- Environment categories were only partly addressed. Leave-one-out analysis (S2) was done, but sub-category splitting requires new metadata. [src: microbeatlas_metal_ecology]
- Primer bias and differential sequencing depth cannot be quantitatively corrected with the available data. [src: microbeatlas_metal_ecology]
- Continuous PGLS on a count predictor is standard, and MCMCglmm is proposed as future work. [src: microbeatlas_metal_ecology]
- GTDB r214 is the best available tree, but no alternative tree comparison was performed. [src: microbeatlas_metal_ecology]
- Only spot checks were done. Formal AMRFinderPlus validation was not. [src: microbeatlas_metal_ecology]
- The cross-sectional design cannot distinguish 3 causal-direction scenarios. Causal phrasing was removed from Key Findings and Interpretation. [src: microbeatlas_metal_ecology]
- All robustness and sensitivity analyses are labelled exploratory. The primary confirmatory result (6 PGLS tests with Bonferroni) stands independently. [src: microbeatlas_metal_ecology] The plan was not preregistered, and the confirmatory/exploratory distinction was documented post-hoc. [src: microbeatlas_metal_ecology]
- There is no public Zenodo archive yet, only an institutional repository. Zenodo archiving was added as Future Direction #11. [src: microbeatlas_metal_ecology]

## Supplementary: Archaeal Analyses {supplementary-archaeal-analyses}: Supplementary …

The archaeal supplement shows that archaeal niche breadth carries phylogenetic signal, but the archaeal metal-resistance association is not detectable with 48 genera. The report treats this as a severely underpowered analysis, not a negative result. [src: microbeatlas_metal_ecology] The bacterial robustness table that the report places next to it shows a positive metal-types effect that survives most covariate checks. It loses significance after BH-FDR adjustment when any single metal is dropped or when aquatic samples are excluded. [src: microbeatlas_metal_ecology]

### Archaeal Pagel's λ

Archaeal niche breadth shows significant phylogenetic signal on both measures. λ = 0.197 (p = 1.1×10⁻⁵) for B_std, and λ = 0.898 (p = 4.6×10⁻¹⁴) for n_envs. [src: microbeatlas_metal_ecology] The archaeal B_std λ is lower than the bacterial value of 0.787. The report calls this consistent with the phylogenetically sparse and ecologically distinct archaeal genera captured by 16S amplicon surveys. [src: microbeatlas_metal_ecology] That explanation is the report's interpretation, not a tested result.

### Observed archaeal PGLS

The observed archaeal phylogenetic generalized least squares (PGLS) used scripts/pgls_robustness.R on 48 genera with antimicrobial resistance (AMR) data. [src: microbeatlas_metal_ecology] None of the three predictors was significant: metal types, AMR clusters and core fraction (z-scored) are listed below with β, SE, t, p and λ. [src: microbeatlas_metal_ecology]

- Metal types: β = +0.0145, SE = 0.0198, t = 0.73, p = 0.467, λ = 0.567 [src: microbeatlas_metal_ecology]
- AMR clusters: β = +0.0146, SE = 0.0209, t = 0.70, p = 0.488, λ = 0.567 [src: microbeatlas_metal_ecology]
- Core fraction: β = +0.0002, SE = 0.0211, t = 0.01, p = 0.991, λ = 0.553 [src: microbeatlas_metal_ecology]

The archaeal metal-types β has the same positive direction as the bacterial β (+0.0215). Its SE is nearly as large as the estimate (t = 0.73), which indicates severe underpowering. [src: microbeatlas_metal_ecology] The 48 genera are biased toward cultured methanogens, halophiles and thermoacidophiles. They miss the environmentally dominant Thaumarchaeota and Woesearchaeota in MicrobeAtlas. [src: microbeatlas_metal_ecology]

### Power analysis

The power analysis used a non-central t-distribution. SE scaled as SE_obs × √(n_obs/n), with β_true = +0.0145 and λ fixed at 0.567. [src: microbeatlas_metal_ecology] Power stays low until several hundred genera. Bonferroni α is 0.0083. Each item gives expected SE, expected t, power at α = 0.05 and power at Bonferroni α.

- n = 48 (current): 0.0198, 0.73, 11%, 3% [src: microbeatlas_metal_ecology]
- n = 100: 0.0137, 1.06, 18%, 6% [src: microbeatlas_metal_ecology]
- n = 200: 0.0097, 1.50, 32%, 12% [src: microbeatlas_metal_ecology]
- n = 300: 0.0079, 1.83, 45%, 21% [src: microbeatlas_metal_ecology]
- n = 400: 0.0069, 2.12, 56%, 30% [src: microbeatlas_metal_ecology]
- n = 600: 0.0056, 2.59, 74%, 48% [src: microbeatlas_metal_ecology]
- n = 800: 0.0048, 3.00, 85%, 64% [src: microbeatlas_metal_ecology]
- n = 1,000: 0.0043, 3.35, 92%, 76% [src: microbeatlas_metal_ecology]

Reaching 80% power requires n ≥ 702 at α = 0.05, or n ≥ 1,084 with Bonferroni correction. [src: microbeatlas_metal_ecology] The report therefore says the non-significant archaeal result should not be read as evidence against the association. [src: microbeatlas_metal_ecology] See [[concepts/statistical-power-and-database-coverage-gap-for-archaeal-trait-analyses]].

### Robustness table for the metal-types effect

The report supplies the false-discovery-rate (FDR) table in data/all_tests_fdr.csv. [src: microbeatlas_metal_ecology] Below, each item gives the metal-types β for one test. Benjamini-Hochberg FDR is abbreviated BH-FDR, and q is the adjusted value.

**Main models and covariate checks (bacterial genera).** These models stay significant after BH-FDR adjustment. [src: microbeatlas_metal_ecology]

- Simple PGLS: n = 606, β = +0.0215, SE = 0.0056, p = 1.5×10⁻⁴, q = 0.003 [src: microbeatlas_metal_ecology]
- Multi-predictor PGLS: n = 606, β = +0.0231, SE = 0.0067, p = 5.5×10⁻⁴, q = 0.004 [src: microbeatlas_metal_ecology]
- R1 + n_species (simple): n = 606, β = +0.0204, SE = 0.0057, p = 3.4×10⁻⁴, q = 0.003 [src: microbeatlas_metal_ecology]
- R1 + n_species (multi): n = 606, β = +0.0224, SE = 0.0067, p = 8.3×10⁻⁴, q = 0.004 [src: microbeatlas_metal_ecology]
- R5 + genome size: n = 527, β = +0.0218, SE = 0.0061, p = 3.6×10⁻⁴, q = 0.003 [src: microbeatlas_metal_ecology]
- R6 + log_n_species + log_genome_size: n = 527, β = +0.0218, SE = 0.0061, p = 3.5×10⁻⁴, q = 0.003 [src: microbeatlas_metal_ecology]
- S3 + within-genus standard deviation (SD) of metal types: n = 606, β = +0.0189, SE = 0.0060, p = 0.0016, q = 0.007 [src: microbeatlas_metal_ecology]
- S4 + log(n_species): n = 606, β = +0.0195, SE = 0.0057, p = 6.4×10⁻⁴, q = 0.004 [src: microbeatlas_metal_ecology]

R4, the strict prevalence filter (≥5%), gave β = +0.0166 (n = 379, SE = 0.0099, p = 0.092), which is not significant. [src: microbeatlas_metal_ecology] The archaeal model (R3) gave β = +0.0145 (n = 48, SE = 0.0198, p = 0.467, q = 0.548), which is not significant after BH-FDR adjustment. [src: microbeatlas_metal_ecology]

**Leave-one-metal-out (S1, 606 genera).** Dropping any single metal removed significance after BH-FDR adjustment. [src: microbeatlas_metal_ecology] The effect is therefore not robust to losing any one metal. See [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects]].

- Excluding Hg: β = +0.0082, SE = 0.0069, p = 0.233, q = 0.313 [src: microbeatlas_metal_ecology]
- Excluding As: β = +0.0039, SE = 0.0061, p = 0.518, q = 0.572 [src: microbeatlas_metal_ecology]
- Excluding Cu: β = +0.0102, SE = 0.0065, p = 0.115, q = 0.187 [src: microbeatlas_metal_ecology]
- Excluding Zn: β = +0.0095, SE = 0.0064, p = 0.140, q = 0.212 [src: microbeatlas_metal_ecology]
- Excluding Cd: β = +0.0084, SE = 0.0064, p = 0.186, q = 0.258 [src: microbeatlas_metal_ecology]
- Excluding Cr: β = +0.0088, SE = 0.0064, p = 0.173, q = 0.255 [src: microbeatlas_metal_ecology]
- Excluding Ni: β = +0.0095, SE = 0.0064, p = 0.140, q = 0.212 [src: microbeatlas_metal_ecology]

**Leave-one-environment-out (S2, 606 genera).** Excluding the aquatic environment gave β = +0.0085 (SE = 0.0039, p = 0.031, q = 0.061). This is nominally significant but not significant after BH-FDR adjustment. [src: microbeatlas_metal_ecology] Every other exclusion stayed significant. [src: microbeatlas_metal_ecology]

- Excluding agricultural: β = +0.0107, SE = 0.0040, p = 0.0073, q = 0.016 [src: microbeatlas_metal_ecology]
- Excluding desert: β = +0.0120, SE = 0.0042, p = 0.0040, q = 0.011 [src: microbeatlas_metal_ecology]
- Excluding farm: β = +0.0115, SE = 0.0042, p = 0.0061, q = 0.015 [src: microbeatlas_metal_ecology]
- Excluding field: β = +0.0118, SE = 0.0040, p = 0.0030, q = 0.010 [src: microbeatlas_metal_ecology]
- Excluding flower: β = +0.0118, SE = 0.0044, p = 0.0077, q = 0.017 [src: microbeatlas_metal_ecology]
- Excluding forest: β = +0.0142, SE = 0.0042, p = 0.0007, q = 0.004 [src: microbeatlas_metal_ecology]
- Excluding leaf: β = +0.0130, SE = 0.0043, p = 0.0025, q = 0.010 [src: microbeatlas_metal_ecology]
- Excluding paddy: β = +0.0123, SE = 0.0042, p = 0.0036, q = 0.010 [src: microbeatlas_metal_ecology]
- Excluding peatland: β = +0.0131, SE = 0.0044, p = 0.0027, q = 0.010 [src: microbeatlas_metal_ecology]
- Excluding plant: β = +0.0105, SE = 0.0039, p = 0.0069, q = 0.016 [src: microbeatlas_metal_ecology]
- Excluding shrub: β = +0.0126, SE = 0.0043, p = 0.0034, q = 0.010 [src: microbeatlas_metal_ecology]
- Excluding soil: β = +0.0113, SE = 0.0039, p = 0.0035, q = 0.010 [src: microbeatlas_metal_ecology]

**Abundance filter.** With bacterial operational taxonomic units (OTUs) filtered to ≥0.01% relative abundance, Pagel's λ was 0.750 (n = 576, p = 2.8×10⁻⁴⁰). [src: microbeatlas_metal_ecology]

## Caveats and Open Work

The evolutionary readings are interpretations. They are not direct tests of vertical versus horizontal inheritance. [src: microbeatlas_metal_ecology] The breadth-versus-depth conclusion rests on PGLS associations, not on experiments. [src: microbeatlas_metal_ecology]

## Slots Into

- [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]]: metal type diversity, not gene count or core fraction, is associated with niche breadth. [src: microbeatlas_metal_ecology]
- [[concepts/phylogenetic-signal-of-gene-content-and-traits]]: the ordering of signal (core fraction, then type diversity, then cluster count) and the near-maximal nitrification signal. [src: microbeatlas_metal_ecology]
- [[concepts/phylogenetic-confounding-of-environment-amr-associations]]: the raw correlation between metal diversity and niche breadth is modest (r ≈ 0.21) and reflects baseline phylogenetic structure, and the PGLS effect is the additional covariation after removing shared ancestry (+0.021 per SD). [src: microbeatlas_metal_ecology]
