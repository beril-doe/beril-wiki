---
type: "Summary"
description: "Summary of the project Pan-Bacterial Anti-Phage Defense Arsenal — Distribution, Arms Race, and Syndromes."
doc_type: "short"
full_text: "sources/phage_defense_arsenal__REPORT.md"
---
# Pan-Bacterial Anti-Phage Defense Arsenal — Distribution, Arms Race, and Syndromes

Pan-Bacterial Anti-Phage Defense Arsenal — Distribution, Arms Race, and Syndromes asks how common seven defense families are, whether defense load tracks prophage load, and which systems co-occur. Detection covered 27,626 of 27,690 (99.8 %) species-level pangenomes. [src: phage_defense_arsenal] Defense count correlates with prophage burden after control for genome size and phylum (partial ρ = 0.301). [src: phage_defense_arsenal] 27 of 28 tested system pairs co-occur more than a phylum-preserving null predicts. [src: phage_defense_arsenal] The report flags detection artefacts for DISARM and CRISPR, and it says its prevalence numbers are upper bounds. [src: phage_defense_arsenal] The arms-race result is consistent with, but not a formal test of, a phylogenetically independent arms race, because no phylogenetically corrected regression was run. [src: phage_defense_arsenal]

## Key Findings

### Prevalence across species

Detection of seven defense families gave 930,573 marker hits across 825,476 unique gene clusters. [src: phage_defense_arsenal] Species-level prevalence was computed across all 27,626 species with at least one defense hit. [src: phage_defense_arsenal] After strict/stringent filtering, 27,565 species have at least one defense system. [src: phage_defense_arsenal]

- CBASS: 7.2 % [src: phage_defense_arsenal]
- Gabija: 22.8 % [src: phage_defense_arsenal]
- R-M Type II: 38.9 % [src: phage_defense_arsenal]
- Retron: 54.7 % [src: phage_defense_arsenal]
- DISARM (strict): 58.4 % [src: phage_defense_arsenal]
- R-M Type I: 76.8 % [src: phage_defense_arsenal]
- BREX: 80.1 % [src: phage_defense_arsenal]
- CRISPR-Cas: 96.1 % [src: phage_defense_arsenal]

Phylum-level patterns, for the 9 phyla with ≥100 species in the ≥5-genome analysis set (7,323 species), were consistent with the pan-bacterial totals. [src: phage_defense_arsenal] R-M Type I was nearly ubiquitous in Pseudomonadota and Bacillota (>80 %). [src: phage_defense_arsenal] CBASS stayed sparse across phyla (<20 %, except Bacteroidota at ~10-15 %). [src: phage_defense_arsenal] Gabija was enriched in Bacillota (30-40 %) relative to Actinomycetota (<10 %). [src: phage_defense_arsenal]

The CRISPR figure depends on the detection method. In the same dataset, eggNOG description matches gave 96 % species prevalence for CRISPR, against ~55 % with the specific Cas1 Pfam (PF01867). [src: phage_defense_arsenal] The report says description-based detection over-counts by ~40 percentage points and warns that cross-study CRISPR comparisons must state the method. [src: phage_defense_arsenal] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

Retron results need a separate caveat. The stringent retron variant departs from the planned Millman-2020-effector-Pfam design: it requires ≥1 other narrow defense system in the species, which is a defense-context filter, not a retron-specificity filter. [src: phage_defense_arsenal] The candidate-to-stringent filter is essentially a no-op (15,109 → 15,098; 11 species dropped), because narrow defense systems are near-universal among species carrying RVT_1. [src: phage_defense_arsenal] The report says results should be read as "reverse-transcriptase candidates in defense-syndrome context," not "characterized retron systems." [src: phage_defense_arsenal] It records the deviation in RESEARCH_PLAN.md Revision History v2 and says a proper Millman-2020-Table-S1 retron-effector Pfam filter would sharpen specificity substantially. [src: phage_defense_arsenal]

### Defense burden tracks prophage burden

Defense-system count and prophage-cluster burden correlate across bacterial species, and the association survives control for genome size and phylum. The arms-race and syndrome tests used the ≥5-genome analysis set, because reliable core/accessory calls need ≥5 sequenced genomes per species. [src: phage_defense_arsenal] The marginal Spearman ρ was 0.609 (p ≈ 0, n = 7,323). [src: phage_defense_arsenal] After residualizing on log₁₀(median genome size) and phylum, partial ρ was 0.301 (p = 1.6 × 10⁻¹⁵³). [src: phage_defense_arsenal] The report compares this residual ρ = 0.30 to phylogenetic-signal strength typical of labile microbial traits. [src: phage_defense_arsenal]

A negative-binomial GLM (generalized linear model) gave independent contributions from both predictors. Prophage-cluster count had β = 2.0 × 10⁻⁴ (p < 0.001). [src: phage_defense_arsenal] log10_genome_size had β = 0.755 (p < 0.001), so each 10-fold genome-size increase went with e^0.755 ≈ 2.1× more defense systems. [src: phage_defense_arsenal] The report uses n_prophage_clusters, an unbounded continuous count, as its primary predictor because the module classifier over-counts. [src: phage_defense_arsenal]

The GLM was fit with statsmodels NegativeBinomial(alpha=1.0), so dispersion was held at 1.0 rather than estimated from the data. [src: phage_defense_arsenal] The report expects a small effect on the n_prophage_clusters and log10_genome_size coefficients, both significant at p<0.001 with wide margins, but says standard errors may be slightly under- or over-stated. [src: phage_defense_arsenal] It states that qualitative direction and per-phylum consistency, the load-bearing pieces of the arms-race claim, are not affected. [src: phage_defense_arsenal] It proposes refitting after two-step alpha estimation to sharpen inference. [src: phage_defense_arsenal]

All 9 major phyla showed positive, significant partial correlations, Bonferroni-safe at 9 tests. [src: phage_defense_arsenal] The values ran from 0.18 in Actinomycetota to 0.53 in Campylobacterota. [src: phage_defense_arsenal] The effect is about 3× weaker in Actinomycetota than in Campylobacterota. The report notes that covariates predicting this heterogeneity are worth exploring. [src: phage_defense_arsenal] Even in Actinomycetota, where CRISPR-Cas is very rare in Mycobacterium and Streptomyces gene-content data, partial ρ = 0.18 (p < 10⁻⁷). [src: phage_defense_arsenal] The report reads the universal positive partial-ρ as extending the Stern & Sorek and Koskella & Brockhurst predictions to the 293K-genome scale. [src: phage_defense_arsenal] Vassallo et al. reported ~5 defense systems per genome on average and substantial variation across phyla, findings that predict but did not directly test the arms-race hypothesis at pangenome scale. [src: phage_defense_arsenal]

| Phylum | Species | Partial ρ | p |
|---|---|---|---|
| Campylobacterota | 102 | 0.530 | 9.8×10⁻⁹ [src: phage_defense_arsenal] |
| Bacillota | 735 | 0.481 | 8.4×10⁻⁴⁴ [src: phage_defense_arsenal] |
| Bacillota_A | 1,134 | 0.419 | 2.0×10⁻⁴⁹ [src: phage_defense_arsenal] |
| Verrucomicrobiota | 129 | 0.369 | 1.6×10⁻⁵ [src: phage_defense_arsenal] |
| Patescibacteria | 191 | 0.343 | 1.2×10⁻⁶ [src: phage_defense_arsenal] |
| Pseudomonadota | 2,172 | 0.342 | 9.6×10⁻⁶¹ [src: phage_defense_arsenal] |
| Cyanobacteriota | 124 | 0.309 | 4.9×10⁻⁴ [src: phage_defense_arsenal] |
| Bacteroidota | 925 | 0.261 | 6.3×10⁻¹⁶ [src: phage_defense_arsenal] |
| Actinomycetota | 803 | 0.185 | 1.3×10⁻⁷ [src: phage_defense_arsenal] |

Full output is in data/arms_race_results.tsv, data/arms_race_per_phylum.tsv and data/arms_race_nb_model.txt. [src: phage_defense_arsenal]

### Defense syndromes

Defense systems co-occur far more than chance. Under a phylum-stratified column-permutation null (N = 1,000 permutations), 27 of 28 tested pairs showed significant positive co-occurrence at BH-FDR (Benjamini-Hochberg false discovery rate) q < 0.05. [src: phage_defense_arsenal] All 28 pairs are in data/syndrome_pairs.tsv. [src: phage_defense_arsenal] The top pairs are below (OR = odds ratio).

| Pair | Observed | Null mean | z | OR |
|---|---|---|---|---|
| R-M Type II × Gabija | 2,429 | 1,555 | 46.1 | 24.0 [src: phage_defense_arsenal] |
| BREX × DISARM | 4,968 | 4,629 | 31.1 | 8.2 [src: phage_defense_arsenal] |
| BREX × Retron | 5,021 | 4,681 | 29.7 | 8.6 [src: phage_defense_arsenal] |
| DISARM × Retron | 4,280 | 3,844 | 28.4 | 5.2 [src: phage_defense_arsenal] |
| R-M Type I × DISARM | 4,970 | 4,673 | 27.5 | 8.4 [src: phage_defense_arsenal] |
| R-M Type I × BREX | 5,963 | 5,732 | 26.9 | 8.7 [src: phage_defense_arsenal] |
| R-M Type II × DISARM | 3,424 | 2,981 | 24.4 | 4.1 [src: phage_defense_arsenal] |
| R-M Type II × BREX | 3,929 | 3,637 | 23.0 | 6.4 [src: phage_defense_arsenal] |
| R-M Type I × R-M Type II | 3,948 | 3,665 | 22.5 | 7.6 [src: phage_defense_arsenal] |

The only exception was CRISPR-Cas × CBASS (z = 0.21, p_emp = 0.98). These two systems have the largest prevalence gap (96 % vs 7 %), and CBASS is essentially independent of CRISPR-Cas presence. [src: phage_defense_arsenal]

The report calls R-M Type II × Gabija the strongest pan-bacterial defense syndrome to date, with OR ≈ 24 and z ≈ 46 under a phylum-preserving null. [src: phage_defense_arsenal] The two systems co-occur in 2,429 of 4,096 R-M Type II-carrying species (59 %), against an expected 1,555 (38 %). [src: phage_defense_arsenal] To the report's knowledge, this is a novel pan-bacterial finding at this scale. [src: phage_defense_arsenal] It has not been named in the defense-syndrome literature and merits mechanistic follow-up. [src: phage_defense_arsenal] Both systems act on double-stranded DNA (deoxyribonucleic acid): Type II R-M by sequence-specific cleavage, Gabija by a nuclease/helicase pair triggered by nucleotide-pool depletion. [src: phage_defense_arsenal] The report hypothesizes that the pairing may reflect complementary layered defense against different phage life-cycle stages. [src: phage_defense_arsenal]

The report reads BREX × DISARM (OR = 8.2) as consistent with the "defense island" pattern and with a framework predicting co-clustering of defense systems on mobile genetic elements. [src: phage_defense_arsenal] Rocha & Bikard proposed defense islands as the ecological unit of defense diversity, and Tesson et al. reported that defense systems tend to co-cluster. [src: phage_defense_arsenal] The report says its 27/28 significant pairs directly support that framework. [src: phage_defense_arsenal] It states that prior work gave distributions and pairwise heatmaps but did not control for phylum plus genome size in arms-race regression or test syndromes against a phylum-preserving null with corrected q-values. [src: phage_defense_arsenal] To its knowledge, it is the first pan-bacterial (293K-genome) systematic test of the arms-race, syndrome and accessory-enrichment hypotheses for this seven-family panel. [src: phage_defense_arsenal]

## Core versus Accessory Placement

The report states that six of seven defense systems show highly significant enrichment in the auxiliary and singleton pangenome. The background was 46.8 % core and 37.9 % singleton across 132,531,501 gene clusters. [src: phage_defense_arsenal] The report's per-system table below lists eight rows, because it gives R-M Type I and R-M Type II separately and includes DISARM. The report does not say how its "six of seven" count maps onto these rows. The table does classify DISARM as near baseline. [src: phage_defense_arsenal] Per-system core fractions differed from the 46.8 % baseline with χ² p ≈ 0 for all. [src: phage_defense_arsenal] Per-system χ² tests are in data/accessory_enrichment.tsv. [src: phage_defense_arsenal]

| System | Core % | Singleton % | Class |
|---|---|---|---|
| Retron | 8.2 [src: phage_defense_arsenal] | 65.8 [src: phage_defense_arsenal] | Strong accessory |
| Gabija | 9.1 [src: phage_defense_arsenal] | 68.8 [src: phage_defense_arsenal] | Strong accessory |
| R-M Type II | 9.4 [src: phage_defense_arsenal] | 68.2 [src: phage_defense_arsenal] | Strong accessory |
| R-M Type I | 9.8 [src: phage_defense_arsenal] | 65.3 [src: phage_defense_arsenal] | Strong accessory |
| CBASS | 11.8 [src: phage_defense_arsenal] | 61.1 [src: phage_defense_arsenal] | Strong accessory |
| BREX | 20.7 [src: phage_defense_arsenal] | 55.8 [src: phage_defense_arsenal] | Moderate accessory |
| CRISPR-Cas | 27.4 [src: phage_defense_arsenal] | 47.2 [src: phage_defense_arsenal] | Mild accessory |
| DISARM | 40.6 [src: phage_defense_arsenal] | 42.3 [src: phage_defense_arsenal] | Near baseline |

For the accessory-enriched systems, singleton fractions were 1.5–1.8× above the 37.9 % baseline. The report reads this as consistent with active horizontal transfer of defense loci through mobile genetic elements. [src: phage_defense_arsenal] This is an interpretation, not a direct measurement of transfer. R-M enzymes have been known to be mobile since the 1990s, and the report says its R-M Type II result (9 % core, 68 % singleton) quantifies this at unprecedented scope. [src: phage_defense_arsenal] It reads the Retron 8 % core / 66 % singleton pattern as consistent with retrons being small-genetic-element hitchhikers. [src: phage_defense_arsenal]

## Prophage Burden Classification

Prophage burden was re-derived with the classifier from projects/prophage_ecology/src/prophage_utils.py. [src: phage_defense_arsenal] It classified 4,005,537 gene-cluster hits into 4,228,150 module-hits across 7 modules. [src: phage_defense_arsenal] Species counts by number of modules present:

| Modules present | Species | % of pangenome |
|---|---|---|
| 2 | 3 [src: phage_defense_arsenal] | <0.01 [src: phage_defense_arsenal] |
| 3 | 178 [src: phage_defense_arsenal] | 0.6 [src: phage_defense_arsenal] |
| 4 | 4,577 [src: phage_defense_arsenal] | 16.5 [src: phage_defense_arsenal] |
| 5 | 6,897 [src: phage_defense_arsenal] | 24.9 [src: phage_defense_arsenal] |
| 6 | 6,389 [src: phage_defense_arsenal] | 23.1 [src: phage_defense_arsenal] |
| 7 | 9,658 [src: phage_defense_arsenal] | 34.9 [src: phage_defense_arsenal] |

The distribution saturates at 7 modules for 35 % of species because the eggNOG-description classifier is deliberately broad, capturing integrase, holin, endolysin, CI-like repressor and tail proteins as candidates. [src: phage_defense_arsenal] The report says the classifier over-counts by design, because integrase, holin, endolysin and related terms also match non-phage bacterial genes such as host integrases and cell-wall lysins. [src: phage_defense_arsenal] Consequently n_prophage_modules saturates at 7 for 35 % of species and is not a specific prophage count. [src: phage_defense_arsenal] For the regression, n_prophage_clusters (an unbounded continuous count) is the primary predictor and n_prophage_modules is a coarse categorical secondary one. [src: phage_defense_arsenal]

## Data and Methods

The report's primary Pfam-based detection table is interproscan_domains (833M rows), which is far broader than bakta_pfam_domains (18.8M rows). [src: phage_defense_arsenal] bakta_pfam_domains misses classical markers: CRISPR Cas1 PF01867 returns 0 hits there against ~25K in InterProScan. [src: phage_defense_arsenal] Filtering interproscan_domains to ~20 curated Pfam accessions and joining gene_cluster returned ~500K rows in under 90 s in one query, with no per-species batching. [src: phage_defense_arsenal] Phase-A feasibility was tested for 19 markers across 7 systems against both tables. [src: phage_defense_arsenal]

The report draws on the KBase Data Lakehouse collection kbase_ke_pangenome for defense-marker Pfam hits, core/aux/singleton flags, phylum and genome-size covariates, and species-level pangenome statistics. [src: phage_defense_arsenal] Broad-Pfam markers (Retron RVT_1, DISARM PLD/SNF2, Gabija UvrD) needed species-level anchor+context filtering. [src: phage_defense_arsenal] Specific markers (CRISPR Cas1, CBASS SAVED, BREX PglZ, Gabija OLD_TOPRIM_C) can serve as single-marker calls. [src: phage_defense_arsenal] The species-level matrix covers 27,626 species × 8 system flags (7 systems plus Retron_candidate versus Retron_stringent) with phylum, median_genome_size, no_genomes and n_clusters covariates. [src: phage_defense_arsenal]

The seven-family panel was assembled from the primary discovery papers. [src: phage_defense_arsenal] R-M and CRISPR-Cas represent the classical, decades-old literature. [src: phage_defense_arsenal] CBASS, Gabija and DISARM emerged from the Sorek-lab bioinformatic discovery era. [src: phage_defense_arsenal] BREX was characterized by Goldfarb et al. in 2015, and retrons were retrofitted to anti-phage systems by Millman et al. in 2020. [src: phage_defense_arsenal] DefenseFinder and PADLOC established the modern consolidated inventories and detection rules. [src: phage_defense_arsenal]

Lakehouse pitfalls: interproscan_domains.signature_acc uses version-free Pfam accessions (PF01867), whereas bakta_pfam_domains.pfam_id uses versioned ones (PF01867.29). [src: phage_defense_arsenal] Cross-database joins must strip versions on the Bakta side. The mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal] Spark Connect .write.parquet() writes to cluster storage (S3), not the client notebook filesystem, and can report success while leaving only an empty local _SUCCESS marker. [src: phage_defense_arsenal] For on-cluster notebook artifacts the report recommends .toPandas() then pandas.to_csv(..., compression="gzip"), citing projects/prophage_ecology/notebooks/01_prophage_gene_discovery.ipynb as the canonical example. [src: phage_defense_arsenal] See [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]].

## Caveats and Open Work

### Detection caveats

The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact. The DrmB SNF2 helicase Pfam anchor (PF00176) is a widespread housekeeping-helicase domain, and it inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal] A DISARM-specific refinement using PADLOC's MacSyFinder-style HMM+context rules would remedy this. [src: phage_defense_arsenal] The DISARM arms-race and syndrome results survive this caveat because they use species-level presence/absence, not per-cluster core/auxiliary calls. [src: phage_defense_arsenal] The CRISPR over-counting from description matching is a further detection caveat. [src: phage_defense_arsenal] Prevalence numbers should be read as upper bounds. The combined eggNOG OR Pfam presence set used for syndromes favors recall, so CRISPR-Cas syndromes may be slightly underestimated in specificity but not in significance. [src: phage_defense_arsenal] Retron detection uses only RVT_1 (PF00078), a broad reverse-transcriptase Pfam. [src: phage_defense_arsenal] Housekeeping-helicase false positives inflate DISARM and reduce retron specificity. [src: phage_defense_arsenal]

### Sampling and inference caveats

Requiring ≥5 genomes reduces the bacterial analysis set to 7,323 species (26 % of 27,690 pangenome species), which biases it toward well-sampled, culturable, high-priority organisms. [src: phage_defense_arsenal] The universal-phylum arms-race pattern applies within this set. Extrapolation to the full 293K-genome tree, which includes many metagenome assembled genomes (MAGs) from environmental samples, is plausible but untested. [src: phage_defense_arsenal] Partial correlation and the GLM control for phylum categorically but not for finer phylogenetic structure. [src: phage_defense_arsenal] The report calls categorical control a coarse-grained analog and leaves open whether the arms race is independent of shared ancestry or partly a within-genus pattern amplified to appear cross-phylum. [src: phage_defense_arsenal]

### Proposed next analyses

- Refine broad-marker detection for Retron, DISARM and Gabija with PADLOC's MacSyFinder-style operon-level rules (multi-Pfam plus gene-order constraints). [src: phage_defense_arsenal] The report predicts this would fix the DISARM accessory-enrichment result and sharpen the syndrome and arms-race analyses without changing the qualitative conclusions. [src: phage_defense_arsenal]
- Extend detection to 20+ defense systems using DefenseFinder/PADLOC HMMs, including CRISPR-Cas subtypes, Zorya, Thoeris, Wadjet, Druantia, pAgo, PARIS, ThsA-ThsB and defense-associated antitoxin cassettes. [src: phage_defense_arsenal] The report expects the focused 7-system panel to generalize, and says a larger panel would enable a defense-repertoire principal-component analysis and genus-level clustering of defensive phenotype. [src: phage_defense_arsenal]
- Refit the negative-binomial GLM with the GTDB tree as a phylogenetic covariance structure, for example with phyr::pglmm, as a stronger arms-race test. [src: phage_defense_arsenal]
- Follow up R-M Type II × Gabija (OR = 24): compare species carrying only R-M Type II with those carrying both, then test for a quantitative fitness advantage from Gabija in phage-challenge experiments in Escherichia coli or Bacillus subtilis. [src: phage_defense_arsenal]
- Add an environment layer, cross-referencing defense repertoires with NCBI-env isolation source or AlphaEarth embeddings to test whether defense syndromes are habitat-specific. [src: phage_defense_arsenal] The report deferred this third pillar at the plan-review checkpoint. [src: phage_defense_arsenal]
- The report suggests exploring which covariates predict the variation in effect size across phyla. [src: phage_defense_arsenal] It also says the R-M Type II–Gabija pairing merits mechanistic follow-up. [src: phage_defense_arsenal]

## Slots Into

- [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems]]: species prevalence runs from CBASS 7.2 % to CRISPR-Cas 96.1 %, and most systems are accessory-enriched. [src: phage_defense_arsenal]
- [[concepts/defense-system-burden-scaling-with-prophage-load-anti-phage-arms-race]]: partial ρ = 0.301 after controlling for genome size and phylum, positive in all 9 phyla. [src: phage_defense_arsenal]
- [[concepts/defense-system-co-occurrence-syndromes-and-defense-islands]]: 27 of 28 pairs co-occur, led by R-M Type II × Gabija (OR 24.0). [src: phage_defense_arsenal]
- [[concepts/domain-based-marker-detection-and-annotation-method-bias]]: CRISPR prevalence is 96 % by eggNOG description versus ~55 % by Cas1 Pfam, and DISARM has a helicase-anchor artefact. [src: phage_defense_arsenal]
- [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]]: defense clusters are 8.2–40.6 % core against a 46.8 % baseline. [src: phage_defense_arsenal]
- [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]]: interproscan_domains finds Cas1 where bakta_pfam_domains returns 0, and the two tables use different Pfam accession versioning. [src: phage_defense_arsenal]
