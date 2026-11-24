---
type: "Summary"
description: "Summary of the project Community Metabolic Ecology via NMDC × Pangenome Integration."
doc_type: "short"
full_text: "sources/nmdc_community_metabolic_ecology__REPORT.md"
---
# Community Metabolic Ecology via NMDC × Pangenome Integration

This project asked whether community-level amino acid pathway completeness, predicted from genomes, tracks ambient metabolite levels as the [[entities/black-queen-hypothesis]] predicts. It also asked whether ecosystem types differ in predicted metabolic potential. The answer is a weak but consistent Black Queen signal in soil microbiomes. [src: nmdc_community_metabolic_ecology] Ecosystem type separates communities strongly. [src: nmdc_community_metabolic_ecology] The Black Queen evidence is modest: only leucine and arginine were significant after FDR (false discovery rate) correction [src: nmdc_community_metabolic_ecology], and one study supplies most of the samples. [src: nmdc_community_metabolic_ecology] The report calls this, to its knowledge, the first application of GapMind community-weighted pathway completeness scores to predict environmental metabolomics across a large cross-habitat NMDC dataset. [src: nmdc_community_metabolic_ecology]

## Key Findings

### Black Queen signal in amino acid pathways

Of 13 testable amino acid pathways, 11 (85%) had negative Spearman correlations between community pathway completeness and ambient amino acid metabolite intensity, the direction the Black Queen Hypothesis predicts. [src: nmdc_community_metabolic_ecology] A binomial sign test gave p = 0.011, which the report reads as a weak but consistent community-scale signal. [src: nmdc_community_metabolic_ecology] The report summarises this as weak but consistent support for community-scale Black Queen dynamics in environmental soil microbiomes. [src: nmdc_community_metabolic_ecology] It describes the analysis as extending the hypothesis to community-weighted scores at landscape scale across diverse NMDC soil samples. [src: nmdc_community_metabolic_ecology] It cites Morris et al. (2012) as proposing that biosynthetic gene loss is selectively favoured when the environment reliably supplies the metabolite. [src: nmdc_community_metabolic_ecology] See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]].

Only two pathways were significant after Benjamini-Hochberg (BH) correction [src: nmdc_community_metabolic_ecology]:

- Leucine had r = −0.390, p = 0.002, q = 0.022, n = 62. [src: nmdc_community_metabolic_ecology]
- Arginine had r = −0.297, p = 0.007, q = 0.049, n = 80. [src: nmdc_community_metabolic_ecology]

The report notes both are energetically expensive to synthesise (leucine: 37 ATP (adenosine triphosphate) equivalents [src: nmdc_community_metabolic_ecology]; arginine: 26 ATP equivalents [src: nmdc_community_metabolic_ecology]). It reads this as consistent with the Black Queen prediction that costly functions are most likely to be lost when environmental supply is reliable. [src: nmdc_community_metabolic_ecology]

The other pathways were not significant after correction:

| Pathway | n | r | p | q |
|---|---|---|---|---|
| Methionine | 18 | −0.496 | 0.036 | 0.117 [src: nmdc_community_metabolic_ecology] |
| Tryptophan | 44 | −0.294 | 0.052 | 0.136 [src: nmdc_community_metabolic_ecology] |
| Threonine | 23 | −0.271 | 0.211 | 0.393 [src: nmdc_community_metabolic_ecology] |
| Phenylalanine | 88 | −0.159 | 0.140 | 0.303 [src: nmdc_community_metabolic_ecology] |
| Valine | 54 | −0.151 | 0.275 | 0.446 [src: nmdc_community_metabolic_ecology] |
| Serine | 59 | −0.061 | 0.645 | 0.762 [src: nmdc_community_metabolic_ecology] |
| Asparagine | 73 | −0.061 | 0.610 | 0.762 [src: nmdc_community_metabolic_ecology] |
| Isoleucine | 18 | −0.057 | 0.823 | 0.823 [src: nmdc_community_metabolic_ecology] |
| Chorismate | 65 | −0.038 | 0.765 | 0.823 [src: nmdc_community_metabolic_ecology] |
| Glycine | 114 | +0.081 | 0.389 | 0.562 [src: nmdc_community_metabolic_ecology] |
| Tyrosine | 26 | +0.419 | 0.033 | 0.117 [src: nmdc_community_metabolic_ecology] |

Methionine had the largest effect, but its small sample size limited significance. [src: nmdc_community_metabolic_ecology] The report gives its effect size as r = −0.50 with n = 18 and q = 0.117, and predicts a larger metabolomics dataset would likely reach significance. [src: nmdc_community_metabolic_ecology] Isoleucine was included as a 13th testable pathway and was not significant (r = −0.057). [src: nmdc_community_metabolic_ecology]

Tyrosine was the main outlier, with a positive correlation. The report hypothesizes that alternative sources, such as phenylalanine hydroxylation, may explain it. [src: nmdc_community_metabolic_ecology] It cautions that tyrosine can be produced from phenylalanine by non-biosynthetic hydroxylation (r = +0.42). [src: nmdc_community_metabolic_ecology] Phenylalanine biosynthesis completeness is not captured in the tyr completeness score, so such communities may still supply tyrosine and decouple biosynthesis from the pool. [src: nmdc_community_metabolic_ecology] Glutamine (n = 4) and proline (n = 9) were skipped. [src: nmdc_community_metabolic_ecology] Cysteine, histidine and lysine remained untestable because their compounds were not detected. [src: nmdc_community_metabolic_ecology] The metabolomics_gold annotations currently lack KEGG compound annotations for these three pathways (cys, his, lys). [src: nmdc_community_metabolic_ecology]

The chorismate pathway used shikimic acid and 3-dehydroshikimic acid as proxies. [src: nmdc_community_metabolic_ecology] These are upstream intermediates that reflect precursor availability rather than chorismate pool size, so the chorismate correlation (r = −0.038) should be read cautiously. [src: nmdc_community_metabolic_ecology]

### Effect of fixing the leucine compound-mapping bug

Automated review found that isoleucine compounds matched the "leucine" substring. The bug was corrected using first-match-wins in NB04 cell-14, and reported results reflect the corrected run. [src: nmdc_community_metabolic_ecology] The fix strengthened the leucine signal from r −0.326 → −0.390 and q 0.045 → 0.022. [src: nmdc_community_metabolic_ecology] Three misassigned isoleucine compounds had near-zero completeness-versus-metabolite correlation and had diluted the true leucine signal. [src: nmdc_community_metabolic_ecology]

### Robustness of the Black Queen result

Restricting to the 125 Soil samples and excluding 6 Unknown-ecosystem samples left leucine unchanged (r = −0.390, q = 0.022, n = 62), because all leucine samples were Soil. [src: nmdc_community_metabolic_ecology] Arginine lost FDR significance (r = −0.264, q = 0.117, n = 78) but kept its direction. [src: nmdc_community_metabolic_ecology] The sign test was unchanged (11/13 negative, p = 0.011), so the report treats the majority-negative direction as robust to ecosystem stratification. [src: nmdc_community_metabolic_ecology]

Study structure is a limit. In the H1 dataset (the metabolite-correlation analysis), 95% of samples (125/131) came from nmdc:sty-11-r2h77870, and the other 6 came from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology] The report states the current H1 dataset is effectively single-study. [src: nmdc_community_metabolic_ecology] The 175 metabolomics samples overall derive from multiple studies, but the report treats cross-study LC-MS (liquid chromatography-mass spectrometry) heterogeneity as largely absent for leucine and arginine. [src: nmdc_community_metabolic_ecology] All leucine samples (n = 62) came from one study with consistent analytical methods. [src: nmdc_community_metabolic_ecology] The second study (n = 6) does not materially affect the results. [src: nmdc_community_metabolic_ecology] Excluding the minor study gave arginine r = −0.264, p = 0.019 (n = 78). The report reads this as showing the arginine signal is not driven by that study. [src: nmdc_community_metabolic_ecology] For future multi-study analyses it suggests modelling study-level random effects to improve power. [src: nmdc_community_metabolic_ecology] See [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]].

The report argues that completeness negatively predicting ambient amino acid concentrations, even in noisy cross-study data, suggests community metabolic potential predicts ecosystem chemistry beyond taxonomic composition alone. [src: nmdc_community_metabolic_ecology]

### Ecosystem differentiation of pathway completeness

Soil and Freshwater communities occupied nearly non-overlapping regions of PCA (principal component analysis) space. [src: nmdc_community_metabolic_ecology] The PCA used a 220-sample × 80-pathway completeness matrix. [src: nmdc_community_metabolic_ecology] PC1 (principal component 1) explained 49.4% of variance (Kruskal-Wallis H = 52.98, p < 0.0001). PC2 explained 16.6% (H = 123.74, p < 0.0001). [src: nmdc_community_metabolic_ecology] PC3, PC4 and PC5 explained 7.9%, 5.2% and 3.9%. [src: nmdc_community_metabolic_ecology] The first five components together explained 83.0%. [src: nmdc_community_metabolic_ecology] The Soil versus Freshwater PC1 separation had Mann-Whitney U = 3,674, p < 0.0001, with median PC1 of +3.86 for Soil and −6.28 for Freshwater. [src: nmdc_community_metabolic_ecology]

PC1 loaded almost entirely on carbon utilization pathways with near-uniform positive loadings. The report reads this as broadly higher carbon substrate completeness in Soil. [src: nmdc_community_metabolic_ecology] It further interprets it as higher predicted carbon metabolic diversity in Soil. [src: nmdc_community_metabolic_ecology] The top PC1 loadings were glucuronate (0.146) [src: nmdc_community_metabolic_ecology], fumarate (0.144) [src: nmdc_community_metabolic_ecology], succinate (0.143) [src: nmdc_community_metabolic_ecology], lysine (0.140) [src: nmdc_community_metabolic_ecology] and cellobiose (0.139). [src: nmdc_community_metabolic_ecology] Amino acid pathways loaded more on PC2 and separated communities within the Soil cluster. [src: nmdc_community_metabolic_ecology]

The report reads the dominance of carbon pathways on PC1 as suggesting that carbon substrate availability is the primary axis differentiating ecosystem metabolic type, with amino acid biosynthesis secondary at PC2. [src: nmdc_community_metabolic_ecology] It interprets the strong separation as consistent with a metabolic niche hypothesis: aquatic versus terrestrial physicochemistry selects different community metabolic configurations, not just different taxa. [src: nmdc_community_metabolic_ecology] It also describes the result as extending meta-metabolome ecology to genome-predicted metabolic potential. [src: nmdc_community_metabolic_ecology]

Per-pathway Kruskal-Wallis tests with BH-FDR correction found differences across ecosystems for 17 of 18 amino acid pathways (q < 0.05). [src: nmdc_community_metabolic_ecology] The largest were:

- Glycine: H = 92.98, q = 1.2×10⁻¹⁹. [src: nmdc_community_metabolic_ecology]
- Asparagine: H = 66.19, q = 3.8×10⁻¹⁴. [src: nmdc_community_metabolic_ecology]
- Cysteine: H = 62.66, q = 1.5×10⁻¹³. [src: nmdc_community_metabolic_ecology]

Tyrosine was the only exception (q = 0.71). [src: nmdc_community_metabolic_ecology] The report suggests freshwater taxa may face different selective pressures for retaining amino acid biosynthesis than soil taxa. [src: nmdc_community_metabolic_ecology] See [[concepts/ecosystem-differentiation-of-community-metabolic-potential]].

The report suggests the 61 samples with "Unknown" ecosystem likely represent a mix of soil subtypes or sediment environments. [src: nmdc_community_metabolic_ecology]

### Relation to the literature

The report places its results alongside prior work.

- It cites Ramoneda et al. (2023) as finding amino acid auxotrophy rates taxonomically structured and environmentally distributed [src: nmdc_community_metabolic_ecology], and as using GapMind to show non-random auxotrophy across phyla and environments. [src: nmdc_community_metabolic_ecology] It says 17/18 pathways differing by ecosystem is consistent with that work. [src: nmdc_community_metabolic_ecology] It says its community-weighted extension shows these taxon-level patterns aggregate into ecosystem-level signals. [src: nmdc_community_metabolic_ecology]
- It cites Mallick et al. (2019) and Noecker et al. (2016) as showing community metabolomics is partially predictable from genomic or metagenomic functional profiles. [src: nmdc_community_metabolic_ecology] Its pathway-completeness predictor differs from flux-based or PICRUSt-style models but reaches comparable conclusions. [src: nmdc_community_metabolic_ecology]
- It cites Danczak et al. (2020) as establishing a meta-metabolome ecology framework in which assembly processes govern metabolite accumulation. [src: nmdc_community_metabolic_ecology]
- It cites Gowda et al. (2022) as showing metabolite dynamics in model communities are predictable from gene content. [src: nmdc_community_metabolic_ecology] Its environmental-scale leucine (r = −0.33) and arginine (r = −0.30) are weaker but directionally consistent. [src: nmdc_community_metabolic_ecology]

## Data and Methods

The report integrates 305M GapMind pathway records (27,690 GTDB species × 80 pathways) with NMDC multi-omics for 220 samples spanning two habitat types, and presents this as a scalable approach for testing metabolic ecological hypotheses from public data lakehouses. [src: nmdc_community_metabolic_ecology] The community pathway matrix held 220 samples and 80 GapMind pathways (18 amino acid, 62 carbon). [src: nmdc_community_metabolic_ecology] Other matrices were:

- Metabolomics overlap: 175 samples with at least one metabolomics file. [src: nmdc_community_metabolic_ecology] The normalised metabolomics matrix holds 175 samples × 476 compounds. [src: nmdc_community_metabolic_ecology]
- H1 analysis matrix: 131 samples with both amino acid pathway completeness and metabolomics. [src: nmdc_community_metabolic_ecology] The H1 results table has 15 rows, with Spearman r, p and BH-FDR q per pathway. [src: nmdc_community_metabolic_ecology]
- Analysis-ready matrix: 174 samples in the full merged matrix of pathway completeness, metabolomics and abiotic features. [src: nmdc_community_metabolic_ecology]
- Long-format community pathway matrix: ~17,600 rows. [src: nmdc_community_metabolic_ecology] The amino acid metabolite table has 737 rows of sample-by-pathway log-intensities for 15 matched pathways. [src: nmdc_community_metabolic_ecology]
- PCA outputs: scores for 220 samples on PC1–5 with ecosystem labels, and loadings of all 80 pathways on PC1 and PC2. [src: nmdc_community_metabolic_ecology]

The cohort had 126 Soil samples, 33 Freshwater samples and 61 with unrecorded ecosystem type. [src: nmdc_community_metabolic_ecology] Taxonomy bridge coverage averaged 94.6%, and all 220 samples passed the 30% QC (quality control) threshold. [src: nmdc_community_metabolic_ecology] In addition, 92% of samples mapped at least 85% of community abundance to GTDB pangenome species. [src: nmdc_community_metabolic_ecology]

Data came from the KBase Data Lakehouse. The nmdc_arkin collection supplied centrifuge_gold, omics_files_table, study_table and abiotic_features for species-level taxonomy, sample-to-file bridging, study metadata and environmental measurements. [src: nmdc_community_metabolic_ecology] Its metabolomics_gold table supplied per-sample LC-MS metabolomics of 3.1M records across 48 studies. [src: nmdc_community_metabolic_ecology] The kbase_ke_pangenome collection supplied gapmind_pathways, gtdb_species_clade and pangenome for GapMind completeness scores (305M rows), GTDB taxonomy bridging and per-species statistics. [src: nmdc_community_metabolic_ecology]

Community completeness used frac_complete, the fraction of taxa with GapMind score ≥ 5 and no missing steps. [src: nmdc_community_metabolic_ecology] The report chose it over frac_likely_complete (score ≥ 4) because a score of 5 is the unambiguous complete call. That call matches the Black Queen prediction that taxa without a complete pathway depend on environmental supply. [src: nmdc_community_metabolic_ecology] frac_likely_complete was computed for sensitivity comparisons. [src: nmdc_community_metabolic_ecology] Metabolites were matched to pathways by string-based compound names. [src: nmdc_community_metabolic_ecology] For ~1,352 Centrifuge taxa matching multiple GTDB clades within a genus, one representative clade was chosen by alphabetical tiebreaking on gtdb_species_clade_id, documented in NB03 cell-17. [src: nmdc_community_metabolic_ecology] Genus-proxy-ambiguous taxa account for ~6.5% of mapped abundance, which bounds the sensitivity to this choice. [src: nmdc_community_metabolic_ecology]

The analysis ran in five notebooks: NMDC exploration (schema, sample inventory, classifier comparison, annotation rates) [src: nmdc_community_metabolic_ecology]; taxonomy bridging of Centrifuge taxa to GTDB species with per-sample coverage [src: nmdc_community_metabolic_ecology]; community-weighted GapMind completeness for 220 samples × 80 pathways [src: nmdc_community_metabolic_ecology]; metabolomics processing and merging [src: nmdc_community_metabolic_ecology]; and statistics, namely H1 Spearman/BH-FDR tests, H2 PCA with Kruskal-Wallis tests, and per-pathway boxplots. [src: nmdc_community_metabolic_ecology]

## Caveats and Open Work

- All 33 Freshwater samples lacked paired metabolomics. They were excluded from the metabolite correlation tests (H1) but kept for the PCA (H2). [src: nmdc_community_metabolic_ecology] H1 is therefore effectively soil-only, and Black Queen dynamics in freshwater communities at this scale are untested. [src: nmdc_community_metabolic_ecology]
- Most pathways were not significant after FDR correction, and several had small n. [src: nmdc_community_metabolic_ecology]
- Nearly all H1 samples came from a single study. [src: nmdc_community_metabolic_ecology]
- Abiotic features (pH, temperature, total organic carbon and others) were all NaN (not a number) in the 174-sample matrix. Partial correlations controlling for environmental gradients were therefore impossible, and these variables could confound both H1 and H2. [src: nmdc_community_metabolic_ecology]
- GapMind completeness indicates gene presence, not expression. Transcriptomics would be needed to test whether expressed biosynthesis correlates more strongly with metabolite pools. [src: nmdc_community_metabolic_ecology]
- KEGG compound IDs (identifiers) in NMDC have a 2% annotation rate, limiting KEGG-based matching. [src: nmdc_community_metabolic_ecology]
- The 61 Unknown-ecosystem samples are unresolved in habitat identity. [src: nmdc_community_metabolic_ecology]

Next analyses the report proposes:

- Control H1 for pH, temperature and total organic carbon with partial correlation or mixed-effects modelling once abiotic data are populated for the metabolomics-overlap samples, to strengthen the signal or identify confounders. [src: nmdc_community_metabolic_ecology]
- Replicate across additional NMDC studies with paired taxonomy and metabolomics, to test whether the leucine and arginine signals generalise beyond the current cohort. [src: nmdc_community_metabolic_ecology]
- Obtain or generate metabolomics for the 33 Freshwater samples, to test whether Black Queen dynamics differ between aquatic and terrestrial communities. [src: nmdc_community_metabolic_ecology]
- Pair metatranscriptomics with metabolomics in a subset of samples, to compare expressed pathway completeness, genomic potential and metabolite abundance, and test whether expression rather than gene presence drives the signal. [src: nmdc_community_metabolic_ecology]
- Improve KEGG compound annotations in metabolomics_gold for cys, his and lys, which would expand the H1 test set from 13 to 16 testable pathways and improve power. [src: nmdc_community_metabolic_ecology]
- Resolve habitat identity of the Unknown samples via NMDC ENVO (Environment Ontology) annotations or study metadata, which could improve H2 power and reveal finer-scale metabolic niche structure. [src: nmdc_community_metabolic_ecology]

## Slots Into

- [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]]: 11 of 13 pathways were negative (sign test p = 0.011), but only leucine and arginine were FDR-significant. [src: nmdc_community_metabolic_ecology]
- [[concepts/ecosystem-differentiation-of-community-metabolic-potential]]: Soil and Freshwater separate on carbon pathway completeness, and 17 of 18 amino acid pathways differ by ecosystem. [src: nmdc_community_metabolic_ecology]
- [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]]: The Soil-only rerun kept leucine significant and arginine directionally consistent. [src: nmdc_community_metabolic_ecology] Study-level checks found no cross-study protocol confound for leucine and an arginine signal not driven by the minor study. [src: nmdc_community_metabolic_ecology] The compound-mapping fix strengthened leucine. [src: nmdc_community_metabolic_ecology] The dataset is effectively single-study, so replication is proposed. [src: nmdc_community_metabolic_ecology]
