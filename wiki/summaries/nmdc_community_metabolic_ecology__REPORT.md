---
type: Summary
description: NMDC–pangenome integration reveals community metabolic and Black Queen
  signals
doc_type: short
full_text: ../sources/nmdc_community_metabolic_ecology__REPORT.md
title: Community Metabolic Ecology via NMDC × Pangenome Integration
sources:
- id: nmdc_community_metabolic_ecology
  resource: ../sources/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
---
# Community Metabolic Ecology via NMDC × Pangenome Integration

## Overview

This report integrates NMDC community taxonomic and metabolomics data with GTDB pangenome and GapMind pathway records to test community-scale Black Queen Hypothesis (BQH) dynamics and ecosystem differentiation. GapMind pathway completeness measures whether taxa possess all required steps for a pathway; the analysis used community-weighted completeness across 220 samples, 27,690 GTDB species, and 80 pathways. The integration included 305M GapMind pathway records and NMDC multi-omics data spanning soil and freshwater communities. [^nmdc_community_metabolic_ecology]

The community pathway matrix contained 220 samples and 80 pathways, comprising 18 amino-acid and 62 carbon-utilization pathways. The metabolomics overlap contained 175 samples, the H1 pathway–metabolomics matrix contained 131 samples, and the full analysis-ready merged matrix contained 174 samples. The full cohort included 126 Soil samples, 33 Freshwater samples, and 61 samples with unrecorded ecosystem type. All 33 Freshwater samples lacked paired metabolomics and were excluded from H1 but retained for H2. Mean taxonomy-bridge coverage was 94.6%; all 220 samples passed the 30% quality-control threshold, and 92% mapped at least 85% of community abundance to GTDB pangenome species. [^nmdc_community_metabolic_ecology]

## Key Findings

### Community-scale Black Queen dynamics

Across 13 testable amino-acid biosynthesis pathways, 11 of 13 (85%) showed negative Spearman correlations between community pathway completeness and ambient amino-acid metabolite intensity. A binomial sign test showed that this majority-negative direction was significantly non-random (p = 0.011), indicating a weak but consistent community-scale BQH signal. [^nmdc_community_metabolic_ecology]

Leucine biosynthesis was negatively correlated with metabolite intensity (r = −0.390, q = 0.022, n = 62), and arginine biosynthesis was also negatively correlated (r = −0.297, q = 0.049, n = 80); these were the two pathways significant after Benjamini-Hochberg false-discovery-rate correction (q < 0.05). Methionine had the largest effect (r = −0.496, n = 18, q = 0.117) but was underpowered. Tyrosine was an outlier in the anti-BQH direction (r = +0.419, ns), while isoleucine showed no signal (r = −0.057, n = 18, q = 0.823). [^nmdc_community_metabolic_ecology]

The H1 predictor was binary `frac_complete`, the fraction of community taxa with a GapMind score of 5, indicating a complete pathway with no missing steps. The alternative `frac_likely_complete` metric uses a score of at least 4 and was retained for sensitivity comparisons. Glutamine (n = 4) and proline (n = 9) were skipped because of insufficient metabolomics coverage. [^nmdc_community_metabolic_ecology]

Soil-only analysis used 125 Soil samples after excluding 6 Unknown-ecosystem samples. Leucine remained significant with r = −0.390, q = 0.022, n = 62; arginine remained directionally consistent but lost FDR significance (r = −0.264, q = 0.117, n = 78). The sign test remained 11/13 negative with p = 0.011. Excluding the 6-sample second study gave arginine r = −0.264, p = 0.019, n = 78. [^nmdc_community_metabolic_ecology]

The H1 dataset was dominated by one NMDC study: 125/131 samples (95%) came from `nmdc:sty-11-r2h77870`, while 6 came from `nmdc:sty-11-547rwq94`. All 62 leucine samples came from the first study, so cross-study LC-MS protocol heterogeneity was not a confounder for the leucine result; the arginine result was not driven by the minor study. [^nmdc_community_metabolic_ecology]

The report interprets the leucine and arginine results as weak but consistent support for community-scale BQH dynamics, with the energetic cost of synthesis offered as a mechanistic interpretation: leucine was reported as requiring 37 ATP equivalents and arginine 26 ATP equivalents. The leucine correlation strengthened from r = −0.326 to r = −0.390 and its q value from 0.045 to 0.022 after correcting an isoleucine/leucine compound-mapping collision. [^nmdc_community_metabolic_ecology]

### Ecosystem differentiation of metabolic potential

PCA of the 220-sample × 80-pathway completeness matrix explained 49.4% of variance in PC1 and 16.6% in PC2, with PC1–5 explaining 83.0% in total. Kruskal-Wallis tests across three ecosystem types were significant for PC1 (H = 52.98, p < 0.0001) and PC2 (H = 123.74, p < 0.0001). Soil and Freshwater communities occupied nearly non-overlapping PCA regions; pairwise Soil versus Freshwater separation was Mann-Whitney U = 3,674, p < 0.0001, with median PC1 values of +3.86 for Soil and −6.28 for Freshwater. [^nmdc_community_metabolic_ecology]

PC1 was dominated by carbon-utilization pathways, including glucuronate, fumarate, succinate, cellobiose, and galactose, with near-uniform positive loadings. The largest listed PC1 loadings were glucuronate (0.146), fumarate (0.144), succinate (0.143), lysine (0.140), and cellobiose (0.139). The report interprets this axis as indicating broadly higher carbon-substrate completeness in Soil communities, while amino-acid pathways contributed more strongly to PC2. [^nmdc_community_metabolic_ecology]

Per-pathway Kruskal-Wallis tests with Benjamini-Hochberg correction found significant ecosystem-type differences for 17 of 18 amino-acid pathways (q < 0.05). The strongest differences were glycine (H = 92.98, q = 1.2×10⁻¹⁹), asparagine (H = 66.19, q = 3.8×10⁻¹⁴), and cysteine (H = 62.66, q = 1.5×10⁻¹³) biosynthesis; tyrosine was the only pathway not significantly differentiated (q = 0.71). [^nmdc_community_metabolic_ecology]

The report interprets the strong PCA separation and 17/18 amino-acid pathway differences as evidence consistent with distinct metabolic configurations across aquatic and terrestrial habitats, while noting that the data do not establish whether the differences arise from habitat physicochemistry, taxonomic composition, or both. [^nmdc_community_metabolic_ecology]

## Caveats and Limitations

Metabolomics technical heterogeneity could affect broader multi-study analyses, although 95% of H1 samples (125/131) came from one NMDC study, and the second study contained only 6 samples. The report recommends study-level random-effects models when broader multi-study coverage becomes available. [^nmdc_community_metabolic_ecology]

All 33 Freshwater samples lacked paired metabolomics, so H1 was effectively a soil-only test. Whether BQH dynamics operate at the same scale in freshwater communities remains untested. [^nmdc_community_metabolic_ecology]

Abiotic features, including pH, temperature, and total organic carbon, were absent as usable measurements: all were NaN in the 174-sample analysis matrix. Consequently, partial correlations controlling for environmental gradients could not be performed, and abiotic variables may confound H1 and H2. [^nmdc_community_metabolic_ecology]

GapMind measures genomic potential rather than expression. The presence of pathway genes does not show that biosynthesis is active; metatranscriptomic data would be needed to test whether expressed pathway completeness correlates more strongly with metabolite pools. [^nmdc_community_metabolic_ecology]

Metabolite-to-pathway matching used string-based compound-name matching. An isoleucine substring collision with the leucine pattern was corrected in NB04 cell-14 using first-match-wins, and the reported results use the corrected run. KEGG compound IDs had only a 2% annotation rate; cysteine, histidine, and lysine remained untestable because corresponding compounds were absent from detections. [^nmdc_community_metabolic_ecology]

Shikimic acid and 3-dehydroshikimic acid were used as metabolomics proxies for chorismate, but they are upstream intermediates rather than chorismate itself. Their concentrations therefore reflect precursor availability rather than the chorismate pool directly, making the chorismate correlation (r = −0.038) especially uncertain. [^nmdc_community_metabolic_ecology]

Approximately 1,352 Centrifuge taxa matched multiple GTDB clades within the same genus. One representative clade was selected by alphabetical tiebreaking on `gtdb_species_clade_id`; these genus-proxy-ambiguous taxa accounted for approximately 6.5% of mapped abundance. [^nmdc_community_metabolic_ecology]

Sample-size imbalance limited testing of glutamine (n = 4) and proline (n = 9), despite their biological importance. Methionine also had limited power (n = 18, q = 0.117), and the report identifies larger metabolomics datasets as necessary to evaluate these pathways more reliably. [^nmdc_community_metabolic_ecology]

The 61 Unknown-ecosystem samples may comprise mixed soil subtypes or sediment environments. Resolving their habitat identity through NMDC ENVO annotations or study metadata could improve ecosystem comparisons and reveal finer-scale metabolic niche structure. [^nmdc_community_metabolic_ecology]

## Future Directions

The report proposes adding pH, temperature, and total organic carbon to partial-correlation or mixed-effects models; replicating H1 across additional NMDC studies; obtaining metabolomics for the 33 Freshwater samples; pairing metatranscriptomics with metabolomics; improving KEGG compound annotations to test the 3 currently missing amino-acid pathways (cysteine, histidine, and lysine); and resolving the habitat identities of Unknown samples. [^nmdc_community_metabolic_ecology]

## Slots Into

- [multi-omics-integration](../concepts/multi-omics-integration.md) — Supports integration of community taxonomy, pangenome pathway potential, and metabolomics by demonstrating a 220-sample NMDC workflow and testing pathway completeness against metabolite intensity. [^nmdc_community_metabolic_ecology]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — Extends GapMind-based pathway completeness from species-level annotation to community-weighted metabolic potential and ecosystem-scale analysis. [^nmdc_community_metabolic_ecology]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — Supports ecosystem-associated differentiation of community gene-content potential, including 17 of 18 amino-acid pathways and strong Soil–Freshwater PCA separation. [^nmdc_community_metabolic_ecology]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — Provides a related environmental-metabolism comparison in which pathway completeness and ambient metabolite availability are negatively associated for leucine and arginine, while identifying expression and abiotic controls as unresolved. [^nmdc_community_metabolic_ecology]

[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../sources/nmdc_community_metabolic_ecology__REPORT.md)
