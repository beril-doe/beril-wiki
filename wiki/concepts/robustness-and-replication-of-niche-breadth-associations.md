---
type: "Concept"
description: "Whether genus-level niche-breadth associations survive permutation, within-clade tests, alternative metrics, detection thresholds, environment categories, MAG filters and geographic-subset replication; stops at genome-side confounders."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Robustness and replication of niche-breadth associations

Genera with higher per-Mb metal-gene density have narrower Levins' B_std niche breadth (see [[entities/levins-niche-breadth]]), with an observed β = −0.0207 in the permutation test. [src: comprehensive_metal_ecology] Within phyla, it was significant in two of four phyla, and all four coefficients were negative. [src: comprehensive_metal_ecology] It lost significance with the independent Earth Microbiome Project (EMP) metric. [src: comprehensive_metal_ecology] The Australian subset is not an independent replication. [src: comprehensive_metal_ecology] The Australia-only soil-concentration replication (P3) was near zero (β = −0.002, n = 482), and soil metal concentrations (P4) gave only a partial replication. [src: comprehensive_metal_ecology] Most of the robustness checks are labelled exploratory. See [[summaries/comprehensive_metal_ecology__REPORT]] for the whole report.

A second report, [[summaries/microbeatlas_metal_ecology__REPORT]], tests a related MicrobeAtlas metal-types association with B_std (positive coefficients, bacterial genera). That association survived leaving out any one environment category, but it lost significance under a strict 5% within-environment prevalence threshold, mainly through lower sample size. [src: microbeatlas_metal_ecology] The aquatic exclusion was the weakest case, and it did not survive false discovery rate correction. [src: microbeatlas_metal_ecology]

## Literature Context

The candidate papers address bacterial niche breadth broadly, and none tests metal-gene density or the robustness checks on it. A comparative study across 25,785 species found a positive correlation between the proportion of genes for cooperation and niche breadth. It also found that a decreased proportion of such genes promoted niche contraction as the predominant evolutionary direction [PMID 41774808](https://pubmed.ncbi.nlm.nih.gov/41774808/). Its authors say the relationship is consistent with a simple model, but that more complex causal scenarios are possible, including factors that influence both cooperation and breadth. A large soil survey across China found that regional species pools were the primary factor affecting the transition rate from generalists to specialists. Transitions from specialists to generalists depended on soil pH in agricultural fields, standardised phylogenetic diversity in forests and wetlands, and soil moisture in grasslands [PMID 41054278](https://pubmed.ncbi.nlm.nih.gov/41054278/). In river sediments, specialists showed a stronger phylogenetic signal in ecological preferences (p < 0.05), and generalists showed higher phylogenetic species variability (p < 0.001) [PMID 42498700](https://pubmed.ncbi.nlm.nih.gov/42498700/). Work on Chloroflexus strains along a geothermal gradient found that a lineage with a wide thermal niche was made up of strains that had diverged in temperature range for growth. Apparent generalism at the 16S level can therefore hide cryptic specialists [PMID 23263946](https://pubmed.ncbi.nlm.nih.gov/23263946/). A seaweed epiphyte study classified 39% of ASVs as phylum specialists and 13% as generalists, using niche breadth indices [PMID 39128929](https://pubmed.ncbi.nlm.nih.gov/39128929/).

The corpus's findings are consistent with this literature in three ways. First, a genome-encoded trait is linked to niche breadth: higher per-Mb metal-gene density goes with narrower Levins' B_std. This parallels the gene-content association reported for cooperation genes [PMID 41774808](https://pubmed.ncbi.nlm.nih.gov/41774808/). Second, the clade-level conservation of B_std (Pagel's λ of 0.750 to 0.787 in the MicrobeAtlas analysis) fits the phylogenetic signal reported for specialist preferences [PMID 42498700](https://pubmed.ncbi.nlm.nih.gov/42498700/). Third, the 16S-resolution caveat in the corpus is that a genus may look broad because different species occupy different habitats. This matches the cryptic-specialist concern in Chloroflexus [PMID 23263946](https://pubmed.ncbi.nlm.nih.gov/23263946/). That Chloroflexus result is a single lineage, so it supports the concern only as an example.

The corpus extends the literature by stress-testing a niche-breadth association. It runs permutation, within-phylum PGLS, bootstrap, detection-threshold, leave-one-environment-out and MAG-quality checks. None of the candidate papers reports comparable checks. The corpus also keeps its weaker results as weaker. The association lost significance with the EMP metric (p = 0.099). Within phyla it was significant in only two of four. The MicrobeAtlas association lost significance at a 5% prevalence threshold (p = 0.092). The Australia-only soil-concentration replication was near zero (β = −0.002, n = 482). The candidates cannot confirm or contradict these results. They do bear on interpretation. Regional species pools and environment-specific drivers of transition rates [PMID 41054278](https://pubmed.ncbi.nlm.nih.gov/41054278/) suggest that composition of the geographic panel could shape effect sizes. This fits the corpus's own, untested explanation for the larger β in the Australian subset. The metal-density link to breadth is novel relative to these papers. Whether it replicates in an independent genus panel remains open.

## Permutation and within-phylum tests

The report reads 1,000 predictor-permutations (empirical p < 0.001) as confirming that the primary signal is not a phylogenetic artefact. [src: comprehensive_metal_ecology] In the metal-density permutation test (n = 1,000), the null β had mean ≈ 0 and SD = 0.0029. The observed β = −0.0207 lay 7.14 SD below the null mean, with empirical p = 0/1000 (< 0.001). [src: comprehensive_metal_ecology]

Levins' B_std was computed from MicrobeAtlas Env_Level_1 habitat categories, not from soil chemistry. This keeps the niche-breadth and metal-concentration axes independent. [src: comprehensive_metal_ecology]

Phylogenetic generalized least squares (PGLS) within the four most speciose bacterial phyla tests whether inter-phylum contrasts drive the signal. [src: comprehensive_metal_ecology] Proteobacteria (n = 677, λ = 0.778, β = −0.021, 95% CI [−0.031, −0.011], q_BH = 0.00018) and Actinobacteria (n = 204, λ = 0.779, β = −0.035, 95% CI [−0.057, −0.014], q_BH = 0.0025) were significant after false discovery rate correction. [src: comprehensive_metal_ecology] Firmicutes was borderline and nonsignificant (n = 334, λ = 0.629, β = −0.015, CI [−0.031, +0.000], q_BH = 0.073). [src: comprehensive_metal_ecology] Bacteroidetes was nonsignificant (n = 183, λ = 0.917, β = −0.009, CI [−0.029, +0.011], q_BH = 0.397). [src: comprehensive_metal_ecology]

All four estimates are negative. [src: comprehensive_metal_ecology] Heterogeneity was not significant (Cochran's Q = 3.60, df = 3, p = 0.309, I² = 16.6%). [src: comprehensive_metal_ecology] The report reads this as a signal not confined to one clade and consistent with a common underlying effect. [src: comprehensive_metal_ecology]

## Alternative niche metrics

The report's exploratory NB24 analysis tests the sensitivity of Levins' B_std to measurement choices. [src: comprehensive_metal_ecology] Genus-level mean B_std was parametrically bootstrapped 100 times from its OTU-level values. Draws came from N(mean, SD) and were clipped to [0, 1]. Single-OTU genera were held fixed. [src: comprehensive_metal_ecology] The bootstrap mean correlated almost perfectly with the original (Pearson r = 0.99869; max |Δ| per genus = 0.064, driven by boundary effects in extreme-valued genera). [src: comprehensive_metal_ecology] The primary PGLS on the bootstrap mean gave β = −0.01987 (SE = 0.00365, p = 6.1×10⁻⁸, λ = 0.756, n = 1,574), a change of |Δβ| = 0.00083 (4.0%) from P1. [src: comprehensive_metal_ecology] The report concludes the signal is not sensitive to OTU-level aggregation uncertainty. [src: comprehensive_metal_ecology]

The report cautions that B_std from 16S OTUs may carry noise from coarse OTU–genus matching and MicrobeAtlas annotations. [src: comprehensive_metal_ecology] It proposes replacing the 16S OTU–genus bridge with niche breadth computed directly from MGnify metagenomic genus-level classifications. [src: comprehensive_metal_ecology]

As a genome-based check independent of the 16S survey, the report computed per-genus Shannon entropy of biome_name across MGnify MAGs (n = 1,006 genera with both metrics). [src: comprehensive_metal_ecology] Specialists by Levins B_std tended to have lower entropy (Spearman ρ = +0.063, p = 0.046, n = 1,006). [src: comprehensive_metal_ecology] The distinct-biome-count metric gave a concordant but nonsignificant trend (ρ = +0.044, p = 0.165). [src: comprehensive_metal_ecology] The report attributes the weak agreement to imprecise mapping between a 16S survey and MAGs. [src: comprehensive_metal_ecology]

EMP-derived and [[entities/microbeatlas]] B_std correlated across 539 overlapping genera (Spearman ρ = 0.211, p = 7.7×10⁻⁷). The report reads this as showing that B_std captures genuine ecological breadth rather than database bias. [src: comprehensive_metal_ecology]

The EMP PGLS (EMPO level-2 habitat categories, n = 539 genera) gave β = −0.019 (SE = 0.012, p = 0.099, λ = 0.055). That is not significant at α = 0.05. [src: comprehensive_metal_ecology] The report calls the effect size virtually identical to P1 (−0.019 vs −0.021). [src: comprehensive_metal_ecology] The near-zero λ suggests limited phylogenetic signal in EMPO-2 breadth at this coarse resolution. [src: comprehensive_metal_ecology]

## Detection thresholds

The report cautions that genera detected in fewer MicrobeAtlas samples may have less reliable breadth estimates. [src: comprehensive_metal_ecology] The primary bacterial PGLS was therefore restricted by sample count:

| Threshold | n genera | β | SE | p |
|---|---|---|---|---|
| ≥10 samples | 1,572 | −0.021 | 0.00368 | 1.38×10⁻⁸ [src: comprehensive_metal_ecology] |
| ≥20 samples | 1,570 | −0.021 | 0.00368 | 1.69×10⁻⁸ [src: comprehensive_metal_ecology] |
| ≥50 samples | 1,559 | −0.021 | 0.00370 | 2.22×10⁻⁸ [src: comprehensive_metal_ecology] |

The report concludes that sparse detection does not drive the association. [src: comprehensive_metal_ecology]

### Relative-abundance filter (metal-types analysis)

The MicrobeAtlas report flagged low-abundance OTUs as possibly spurious detections that could inflate niche breadth and bias Pagel's λ for B_std. [src: microbeatlas_metal_ecology] It estimated per-OTU mean relative abundance as total_counts / (n_detected_samples × mean_library_size), with mean_library_size = total_reads / total_samples (87,595 reads/sample across 463,972 samples). [src: microbeatlas_metal_ecology] Excluding OTUs below 0.01% mean relative abundance removed 66% of OTUs and left 34% = 33,676. [src: microbeatlas_metal_ecology] Of these, 23,759 bacterial non-organellar OTUs covered 576 of 606 PGLS genera, and genus-level B_std was recomputed on them. [src: microbeatlas_metal_ecology]

Bacterial Pagel's λ for B_std was 0.787 for all OTUs (1,264 genera), 0.763 for unfiltered OTUs in the same 576 genera, and 0.750 after filtering. [src: microbeatlas_metal_ecology] The LRT (likelihood ratio test) p-values were 7.9×10⁻¹⁰², 5.9×10⁻⁴⁰ and 2.8×10⁻⁴⁰ respectively. [src: microbeatlas_metal_ecology] The λ change was −0.013 (−1.7%). [src: microbeatlas_metal_ecology] The report concludes that phylogenetic conservation of niche breadth is not an artefact of rare transient OTU detections. [src: microbeatlas_metal_ecology]

### Strict within-environment prevalence (metal-types analysis)

In the MicrobeAtlas metal-types analysis, the strict threshold weakened the bacterial result. The report recomputed niche breadth so that an OTU counted as present in an environment only if it appeared in ≥5% of samples in that category. The aim was to reduce detections from contamination, cross-sample bleed-through or rare transient events. [src: microbeatlas_metal_ecology] The effect lost statistical significance at this threshold (p = 0.092). [src: microbeatlas_metal_ecology] Original and strict values were:

- OTUs (operational taxonomic units) passing the filter: 98,919 originally, 10,433 at ≥5%. [src: microbeatlas_metal_ecology]
- Genera with a B_std estimate: 3,160 originally, 1,120 at ≥5%. [src: microbeatlas_metal_ecology]
- PGLS n (with antimicrobial resistance data): 606 originally, 379 at ≥5%. [src: microbeatlas_metal_ecology]
- β (metal types → B_std): +0.0215 originally, +0.0166 at ≥5%. [src: microbeatlas_metal_ecology]
- SE: 0.0056 originally, 0.0099 at ≥5%. [src: microbeatlas_metal_ecology]
- p: 1.5×10⁻⁴ originally, 0.092 at ≥5%. [src: microbeatlas_metal_ecology]
- PGLS λ: 0.708 originally, 0.526 at ≥5%. [src: microbeatlas_metal_ecology]

Original and strict B_std estimates correlated at Pearson r = 0.680. [src: microbeatlas_metal_ecology] The report attributes the loss of significance primarily to the 37% drop in sample size (606 → 379), not to a change in direction or magnitude, since β fell by 23%. [src: microbeatlas_metal_ecology] It notes that the 5% threshold is conservative and excludes 89% of OTUs, many genuinely distributed across environments but uncommon within any one. [src: microbeatlas_metal_ecology] It reads the result as suggesting that spurious rare detections do not entirely drive the signal, while strict prevalence-based breadth needs substantially higher power. [src: microbeatlas_metal_ecology] It proposes a 1–2% threshold as a reasonable middle ground for future work. [src: microbeatlas_metal_ecology]

A separate sensitivity check kept OTUs at ≥0.01% relative abundance. Pagel's λ was then 0.750 (n = 576, p = 2.8×10⁻⁴⁰). [src: microbeatlas_metal_ecology]

The report's own summary of the 5% check gives β = +0.017 versus +0.022 original, confirming direction but with reduced significance because 37% fewer genera passed. [src: microbeatlas_metal_ecology] It concludes that rare transient detections do not explain the metal-diversity–niche-breadth effect. [src: microbeatlas_metal_ecology]

## Environment categories

Among soil-specialist genera by MicrobeAtlas Env_Level_1 (n = 162, >50% of OTUs with soil/agricultural dominant environment), the association strengthened (β = −0.033, SE = 0.012, p = 0.007, λ = 0.471). [src: comprehensive_metal_ecology] The report calls this consistent with the predecessor project's MicrobeAtlas result (β = −0.023, n = 603, p = 0.0002). [src: comprehensive_metal_ecology] It proposes that soil's chemical complexity and metal heterogeneity explain the stronger effect. [src: comprehensive_metal_ecology]

### Leave-one-environment-out (metal-types analysis)

For each of 13 environment categories, the analysis excluded that category, row-normalised prevalences over the remaining 12 environments, recomputed B_std with J=12, and reran PGLS. [src: microbeatlas_metal_ecology] All 13 models were significant at p < 0.05, so the association was not contingent on any single environment category. [src: microbeatlas_metal_ecology] Excluding any category other than aquatic gave p < 0.01, so the report states the result does not depend on the heterogeneous "aquatic" category. [src: microbeatlas_metal_ecology] Excluding aquatic gave p = 0.031, the weakest of all 13 exclusions but still significant. [src: microbeatlas_metal_ecology] Aquatic is the most heterogeneous and over-represented category (40,353 OTUs; 40.8% of the dataset), and excluding it cut β from +0.021 to +0.0085 (−59%). [src: microbeatlas_metal_ecology] That significance is nominal, because the BH-FDR (Benjamini-Hochberg false discovery rate) q was 0.061. [src: microbeatlas_metal_ecology] Overall the models were significant at q < 0.05 for 12 of 13 environments. [src: microbeatlas_metal_ecology] The other twelve exclusions stayed significant after BH-FDR. [src: microbeatlas_metal_ecology] The three least-sampled environments (flower: 898 OTUs, 0.9%; leaf: 1,298 OTUs, 1.3%; plant: 2,647 OTUs, 2.7%) gave β = +0.012, +0.013, +0.010, all p < 0.008. [src: microbeatlas_metal_ecology] In the table below, every exclusion has a positive coefficient and used n = 606 genera. [src: microbeatlas_metal_ecology]

| Exclusion | β | SE | p | BH-FDR q |
|---|---|---|---|---|
| aquatic | +0.0085 | 0.0039 | 0.031 | 0.061 (not significant) [src: microbeatlas_metal_ecology] |
| agricultural | +0.0107 | 0.0040 | 0.0073 | 0.016 [src: microbeatlas_metal_ecology] |
| desert | +0.0120 | 0.0042 | 0.0040 | 0.011 [src: microbeatlas_metal_ecology] |
| farm | +0.0115 | 0.0042 | 0.0061 | 0.015 [src: microbeatlas_metal_ecology] |
| field | +0.0118 | 0.0040 | 0.0030 | 0.010 [src: microbeatlas_metal_ecology] |
| flower | +0.0118 | 0.0044 | 0.0077 | 0.017 [src: microbeatlas_metal_ecology] |
| forest | +0.0142 | 0.0042 | 0.0007 | 0.004 [src: microbeatlas_metal_ecology] |
| leaf | +0.0130 | 0.0043 | 0.0025 | 0.010 [src: microbeatlas_metal_ecology] |
| paddy | +0.0123 | 0.0042 | 0.0036 | 0.010 [src: microbeatlas_metal_ecology] |
| peatland | +0.0131 | 0.0044 | 0.0027 | 0.010 [src: microbeatlas_metal_ecology] |
| plant | +0.0105 | 0.0039 | 0.0069 | 0.016 [src: microbeatlas_metal_ecology] |
| shrub | +0.0126 | 0.0043 | 0.0034 | 0.010 [src: microbeatlas_metal_ecology] |
| soil | +0.0113 | 0.0039 | 0.0035 | 0.010 [src: microbeatlas_metal_ecology] |

The report attributes the higher λ in these analyses (0.87–0.91 vs 0.71 in the main analysis) to the smaller number of categories. This raises the relative weight of shared environments and amplifies phylogenetic covariation in the rescaled B_std. [src: microbeatlas_metal_ecology] It reads the weaker aquatic-exclusion β as a sign that aquatic OTUs contribute disproportionately, and as a potential source of downward bias when aquatic is included. [src: microbeatlas_metal_ecology] It calls this consistent with metal-contaminated coastal, estuarine and hydrothermal environments supplying many broad-niche metal-tolerant genera, and calls the aquatic-exclusion result a conservative lower bound on the true association. [src: microbeatlas_metal_ecology] These are interpretations, not tests.

The report only partly addresses whether the environment categories are ecologically meaningful. Leave-one-out is done, but splitting "aquatic" into marine, freshwater and saline subcategories needs sample metadata that the current KBase Data Lakehouse extraction lacks. [src: microbeatlas_metal_ecology] It proposes rerunning breadth with a finer taxonomy (marine, freshwater, estuarine) to test whether category heterogeneity inflates B_std for some genera. [src: microbeatlas_metal_ecology] It also states that primer bias and differential sequencing depth cannot be corrected quantitatively with the available data. [src: microbeatlas_metal_ecology]

### Limits of the environment categories

MicrobeAtlas uses 13 broad categories that lump heterogeneous habitats. "Aquatic" combines marine, freshwater, estuarine, hydrothermal vent and pond environments. [src: microbeatlas_metal_ecology] A taxon found in both a marine coastal and a freshwater lake sample counts as broad-niched, even if this reflects related but distinct ecotypes. [src: microbeatlas_metal_ecology] The report cannot test within-category heterogeneity because MicrobeAtlas has no finer classification. Doing so requires recomputing niche breadth with a revised taxonomy. [src: microbeatlas_metal_ecology]

Detection across the categories also conflates habitat use with sampling intensity, V3–V4 or V4 primer bias, and uneven geographic and temporal SRA/ENA contributions. [src: microbeatlas_metal_ecology] Densely sampled soil, marine and plant environments can inflate apparent niche breadth relative to deep subsurface, brine and ice taxa. [src: microbeatlas_metal_ecology] Levins' B_std corrects unequal environment sizes but not missing environments or differing detection probabilities. [src: microbeatlas_metal_ecology] Genus-level aggregation is a proxy: a genus may look broad because different species occupy different habitats. [src: microbeatlas_metal_ecology] Correcting primer bias and missing environments needs a multi-primer, multi-region survey design. [src: microbeatlas_metal_ecology]

## MAG quality filters and covariates

MAG (metagenome assembled genomes) quality covariates (mean completeness and contamination per genus from [[entities/kescience-mgnify]]) were tested in an exploratory analysis of n = 1,107 genera. [src: comprehensive_metal_ecology] The concern is that per-Mb density may be affected by MAG incompleteness distributed non-randomly across taxa. [src: comprehensive_metal_ecology] Adding completeness left β(density) = −0.023 (p = 2.9×10⁻⁸), unchanged from baseline. [src: comprehensive_metal_ecology] The completeness coefficient was β = −0.003 (p = 0.43, NS). [src: comprehensive_metal_ecology] Adding contamination gave β(density) = −0.023 (p = 5.4×10⁻⁸), with <1.2% change in β. [src: comprehensive_metal_ecology] Contamination itself had β = +0.007 (p = 0.042), a slight positive association with broader niches. [src: comprehensive_metal_ecology] Restricting to high-quality MAGs (completeness ≥ 90%, contamination ≤ 5%, n = 511 genera) gave β = −0.018 (SE = 0.0063, p = 0.005). The report reads this as showing the signal is not driven by low-quality MAGs. [src: comprehensive_metal_ecology] It states that the MAG-quality concern is addressed. [src: comprehensive_metal_ecology]

Other covariates attenuated the metal-gene coefficient modestly, and all were classed as robust:

| Covariate | Coefficient change | Attenuation | p |
|---|---|---|---|
| GC content | 0.021 → 0.016 | 23.7% | 7.5×10⁻⁵ [src: comprehensive_metal_ecology] |
| Isolation source | 0.021 → 0.018 | 14.5% | 3×10⁻⁶ [src: comprehensive_metal_ecology] |
| Dominant biome | 0.021 → 0.020 | 5.8% | <10⁻⁴ [src: comprehensive_metal_ecology] |

## Geographic-subset replication

The AusMicrobiome density analysis (P5) has n = 482, β = −0.052, SE = 0.0063, t = −8.20, p = 2.2×10⁻¹⁵, partial R² = 0.194, ΔAIC = −61.2 and λ = 0.734. [src: comprehensive_metal_ecology] It confirms the primary direction. [src: comprehensive_metal_ecology] The report nonetheless classifies it as consistent within-dataset, not an independent replication. All 482 genera are a subset of P1 and the density predictor is identical. [src: comprehensive_metal_ecology] Both analyses use per-Mb density from the same MGnify MAG file, so the predictor is consistent by construction. [src: comprehensive_metal_ecology]

The P5 coefficient is 2.5× that of P1 (z ≈ 4.1, p < 0.001), and the report says soil enrichment alone cannot explain the difference. [src: comprehensive_metal_ecology] A z-test also gives P5 > P1-full (z = −4.24, p = 2.2×10⁻⁵) and P5 ≠ P3-soil (z = −2.29, p = 0.022). [src: comprehensive_metal_ecology] Exploratory diagnostics point to composition rather than measurement:
- B_std is identical in P1 and P5 because both use the same Env_Level_1 computation, which rules out a response-variable artefact. [src: comprehensive_metal_ecology]
- Restricting P1 to the 482 shared genera gives β = −0.052 (SE = 0.0063), identical to P5. The report attributes the larger β entirely to the continental subset's phylogenetic composition. [src: comprehensive_metal_ecology]
- The subset is Proteobacteria-enriched and Firmicutes-depleted, which the report says reduces effective phylogenetic diversity and concentrates the signal. [src: comprehensive_metal_ecology]

The report proposes that reduced diversity concentrates the signal among closely related specialist/generalist genus pairs and amplifies β. [src: comprehensive_metal_ecology] It also reads the lower λ in P5 (0.734 vs 0.757 in P1) as slightly less residual phylogenetic structure. [src: comprehensive_metal_ecology] Both are explanations, not direct tests.

### Australia-only soil-concentration replication (P3)

The NGSA Australia-only replication (P3, n = 482, β = −0.002) is consistently near zero. [src: comprehensive_metal_ecology] The report offers three probable explanations: Australia's relative geological stability gives lower cross-biome variation in metal-gene investment [src: comprehensive_metal_ecology]; NGSA soil geochemistry covers a narrower chemical gradient [src: comprehensive_metal_ecology]; and all P3 genera also appear in P1, which reduces independent information without adding new signal. [src: comprehensive_metal_ecology] The within-dataset genomic density analysis (P5, same genera and genomic predictor) recovers a strong and larger signal. The report reads this as showing the near-zero P3 result reflects the soil-concentration predictor rather than the genus panel. [src: comprehensive_metal_ecology] It proposes a northern-hemisphere soil amplicon-survey replication, which would strengthen the Australian-null explanation. [src: comprehensive_metal_ecology]

Soil metal concentrations from the AusMicrobiome+NGSA data (P4) were tested on the same 482 genera. The report classes the result as partial replication: Cu and Zn were significant after BH-FDR (q = 0.041 each), and λ = 0.32–0.35 was substantially lower than P1. [src: comprehensive_metal_ecology]

| Metal | β | p (q) | λ | Result |
|---|---|---|---|---|
| Cu | −0.011 | 0.016 (q=0.041) | 0.319 | significant [src: comprehensive_metal_ecology] |
| Zn | −0.011 | 0.016 (q=0.041) | 0.318 | significant [src: comprehensive_metal_ecology] |
| Pb | −0.009 | 0.034 (q=0.057) | 0.326 | NS at q > 0.05 [src: comprehensive_metal_ecology] |
| Ni | −0.009 | 0.049 (q=0.061) | 0.354 | NS at q > 0.05 [src: comprehensive_metal_ecology] |
| Co | +0.001 | 0.776 | 0.353 | NS; wrong direction [src: comprehensive_metal_ecology] |

## Open Directions

- Replicate the density–breadth association in a genuinely independent genus panel with different MAG sources. This would close the gap left by P5 being a subset of P1.
- Run a targeted replication with a northern-hemisphere soil amplicon survey. This would test the Australian-null explanation.
- Replace the 16S OTU–genus bridge with niche breadth computed directly from MGnify metagenomic genus-level classifications. This would remove the OTU-matching noise.
- Test the reduced-phylogenetic-diversity explanation directly. Subsample P1 to match the Proteobacteria/Firmicutes mix of the Australian panel, and check whether β rises to −0.052.
- Rerun the EMP PGLS with finer habitat resolution than EMPO level 2, or with more genera. This would show whether the nonsignificant result reflects coarse resolution or a weaker true effect.
- Apply formal multiple-testing control across all exploratory checks, as in [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].
- Add a power analysis for the Firmicutes and Bacteroidetes within-phylum tests. It would show whether their nonsignificant results reflect low power.
- Rerun the metal-types analysis at a 1–2% within-environment prevalence threshold. This would test whether the lost significance at 5% reflects power (n = 379) or a weaker effect.
- Split "aquatic" into marine, freshwater and estuarine using MicrobeAtlas sample metadata, and repeat the exclusion test. This would show whether the one weak case (q = 0.061) comes from category heterogeneity.
