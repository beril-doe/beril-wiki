---
type: Summary
description: Pan-bacterial analysis of anti-phage defense prevalence, syndromes, and
  arms-race patterns
doc_type: short
full_text: ../sources/phage_defense_arsenal__REPORT.md
title: Pan-Bacterial Anti-Phage Defense Arsenal
sources:
- id: phage_defense_arsenal
  resource: ../sources/phage_defense_arsenal__REPORT.md
  title: phage defense arsenal
---
# Pan-Bacterial Anti-Phage Defense Arsenal

## Overview

This report analyzes seven anti-phage defense-system families across the BERDL pangenome. Markers were detected in 27,626 of 27,690 species-level pangenomes (99.8%), producing 930,573 marker hits across 825,476 unique gene clusters. The ≥5-genome quality-filtered analysis set contains 7,323 species and is used for arms-race and syndrome tests. [^phage_defense_arsenal]

## Key Findings

### Defense-system prevalence

Species-level prevalence ranged from 7.2% for CBASS to 96.1% for CRISPR-Cas, with BREX at 80.1%, restriction-modification (R-M) Type I at 76.8%, DISARM at 58.4% under the strict call, Retron at 54.7%, R-M Type II at 38.9%, and Gabija at 22.8%. R-M Type I exceeded 80% in Pseudomonadota and Bacillota, CBASS remained below 20% in all phyla except Bacteroidota at approximately 10–15%, and Gabija reached 30–40% in Bacillota versus below 10% in Actinomycetota. [^phage_defense_arsenal]

### Defense count and prophage burden

Species-level defense-system count correlated with prophage-cluster burden at Spearman ρ = 0.609 (p ≈ 0, n = 7,323). After residualizing on log10 median genome size and phylum, partial ρ remained 0.301 (p = 1.6 × 10⁻¹⁵³). A negative-binomial generalized linear model found positive contributions from prophage-cluster count (β = 2.0 × 10⁻⁴, p < 0.001) and log10 genome size (β = 0.755, p < 0.001); each 10-fold genome-size increase was associated with e^0.755 ≈ 2.1× more defense systems. [^phage_defense_arsenal]

All nine major phyla showed positive, significant partial correlations: Campylobacterota, n = 102, ρ = 0.530, p = 9.8×10⁻⁹; Bacillota, n = 735, ρ = 0.481, p = 8.4×10⁻⁴⁴; Bacillota_A, n = 1,134, ρ = 0.419, p = 2.0×10⁻⁴⁹; Verrucomicrobiota, n = 129, ρ = 0.369, p = 1.6×10⁻⁵; Patescibacteria, n = 191, ρ = 0.343, p = 1.2×10⁻⁶; Pseudomonadota, n = 2,172, ρ = 0.342, p = 9.6×10⁻⁶¹; Cyanobacteriota, n = 124, ρ = 0.309, p = 4.9×10⁻⁴; Bacteroidota, n = 925, ρ = 0.261, p = 6.3×10⁻¹⁶; and Actinomycetota, n = 803, ρ = 0.185, p = 1.3×10⁻⁷. [^phage_defense_arsenal]

### Defense-system syndromes

Using 1,000 phylum-stratified column-permutation null permutations and Benjamini–Hochberg false-discovery-rate correction (BH-FDR), 27 of 28 defense-system pairs showed significant positive co-occurrence at q < 0.05. The strongest pair was R-M Type II × Gabija, with 2,429 observed co-occurrences versus a null mean of 1,555, z = 46.1, and odds ratio (OR) = 24.0. Other strong pairs included BREX × DISARM (n = 4,968, null mean = 4,629, z = 31.1, OR = 8.2), BREX × Retron (5,021, 4,681, z = 29.7, OR = 8.6), DISARM × Retron (4,280, 3,844, z = 28.4, OR = 5.2), R-M Type I × DISARM (4,970, 4,673, z = 27.5, OR = 8.4), R-M Type I × BREX (5,963, 5,732, z = 26.9, OR = 8.7), R-M Type II × DISARM (3,424, 2,981, z = 24.4, OR = 4.1), R-M Type II × BREX (3,929, 3,637, z = 23.0, OR = 6.4), and R-M Type I × R-M Type II (3,948, 3,665, z = 22.5, OR = 7.6). [^phage_defense_arsenal]

CRISPR-Cas × CBASS was the only pair that did not reach significance (z = 0.21, p_emp = 0.98). CRISPR-Cas and CBASS also had the largest prevalence gap, at 96% versus 7%. The R-M Type II × Gabija pairing is presented as a novel pan-bacterial syndrome at this scale; its two systems both act on double-stranded DNA, with Type II R-M using sequence-specific cleavage and Gabija using a nuclease/helicase pair triggered by nucleotide-pool depletion. [^phage_defense_arsenal]

### Accessory-pangenome enrichment

Six of seven systems were significantly enriched in the auxiliary and singleton pangenome relative to a background of 46.8% core and 37.9% singleton gene clusters, with χ² p ≈ 0 for all systems. Core and singleton fractions were: Retron, 8.2% and 65.8%; Gabija, 9.1% and 68.8%; R-M Type II, 9.4% and 68.2%; R-M Type I, 9.8% and 65.3%; CBASS, 11.8% and 61.1%; BREX, 20.7% and 55.8%; CRISPR-Cas, 27.4% and 47.2%; and DISARM, 40.6% and 42.3%. [^phage_defense_arsenal]

For the accessory-enriched systems, singleton fractions were 1.5–1.8× above the 37.9% background baseline, consistent with horizontal transfer of defense loci through mobile genetic elements. DISARM was near baseline and is treated as an unreliable accessory-enrichment result because the DrmB SNF2 helicase Pfam anchor (PF00176) is a widespread housekeeping-helicase domain. [^phage_defense_arsenal]

### Detection and data-engineering findings

EggNOG description-based CRISPR detection produced 96% species prevalence, whereas detection using the specific Cas1 Pfam marker PF01867 produced approximately 55% prevalence on the same pangenome, a difference of approximately 40 percentage points. The report therefore treats the 96% value as an upper bound and warns that CRISPR comparisons must specify their detection method. [^phage_defense_arsenal]

The primary Pfam-domain source was the 833-million-row `interproscan_domains` table rather than the 18.8-million-row `bakta_pfam_domains` table. Filtering InterProScan for `analysis = 'Pfam'` and a curated signature list of approximately 20 accessions, followed by joining to `gene_cluster`, returned ~500K rows in under 90 seconds; `bakta_pfam_domains` contained 0 Cas1 PF01867 hits compared with ~25K in InterProScan. InterProScan uses version-free accessions such as PF01867, whereas Bakta uses versioned accessions such as PF01867.29, so cross-database joins must strip Bakta versions. [^phage_defense_arsenal]

Spark Connect `.write.parquet()` writes to cluster storage rather than the client notebook filesystem. The report recommends converting results with `.toPandas()` and then using `pandas.to_csv(..., compression="gzip")` when notebook-local artifacts are required. [^phage_defense_arsenal]

## Caveats and Limitations

CRISPR-Cas prevalence is inflated by permissive EggNOG description matching. The combined EggNOG-or-Pfam presence set used for syndrome analysis prioritizes recall, so CRISPR-Cas syndrome specificity may be reduced even though the significance results are not expected to be invalidated. [^phage_defense_arsenal]

The DISARM accessory-enrichment result is unreliable because PF00176 also identifies widespread non-DISARM SNF2 helicases. A PADLOC MacSyFinder-style HMM-plus-context refinement is needed; the report states that arms-race and syndrome results involving DISARM are unaffected because they use species-level presence/absence rather than per-cluster classification. [^phage_defense_arsenal]

Retron detection uses the broad RVT_1 Pfam PF00078. The stringent call requires at least one other narrow defense system and is therefore a defense-context filter rather than a retron-specificity filter; it reduced candidates from 15,109 to 15,098, dropping 11 species. Results should be interpreted as reverse-transcriptase candidates in defense-syndrome context, not as characterized retron systems. [^phage_defense_arsenal]

The prophage classifier deliberately captures broad module candidates including integrase, holin, endolysin, CI-like repressor, and tail proteins, which can also match non-phage bacterial genes. Consequently, `n_prophage_modules` saturates at 7 for 35% of species; the primary arms-race predictor is instead the unbounded `n_prophage_clusters` count. [^phage_defense_arsenal]

The ≥5-genome filter reduced the analysis set to 7,323 of 27,690 pangenome species, or 26%, biasing the analysis toward well-sampled, culturable, high-priority organisms. Extrapolation to the full 293K-genome tree, including many environmental MAGs, remains untested. [^phage_defense_arsenal]

The arms-race analysis controls for phylum categorically but does not use a phylogenetically corrected regression. Its partial correlations and negative-binomial GLM are therefore consistent with, but do not formally establish, a phylogenetically independent arms race. [^phage_defense_arsenal]

The negative-binomial GLM fixes dispersion at alpha = 1.0 rather than estimating it. Both focal coefficients remained significant at p < 0.001 with wide margins, but standard errors may be slightly under- or over-stated; refitting with an estimated alpha would sharpen inference. [^phage_defense_arsenal]

## Future Directions

The report recommends PADLOC MacSyFinder-style multi-PFam and gene-order rules for Retron, DISARM, and Gabija; expansion to more than 20 systems, including Zorya, Thoeris, Wadjet, Druantia, pAgo, PARIS, ThsA-ThsB, and defense-associated antitoxin cassettes; a GTDB-tree phylogenetic mixed-effects arms-race model; mechanistic phage-challenge experiments comparing R-M Type II-only and R-M Type II-plus-Gabija species; and environmental cross-referencing with NCBI isolation-source metadata or AlphaEarth embeddings. [^phage_defense_arsenal]

## Slots Into

- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — the 27-of-28 defense-system co-occurrence pattern and the R-M Type II × Gabija syndrome extend network-level analysis of coordinated gene-system architecture. [^phage_defense_arsenal]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — accessory and singleton enrichment of six defense systems, together with the DISARM detection caveat, provides evidence about mobile acquisition and annotation depth. [^phage_defense_arsenal]
- [environmental-resistome](../concepts/environmental-resistome.md) — the proposed environmental-defense layer and the report’s pan-bacterial defense repertoire provide a basis for testing habitat-specific defense syndromes. [^phage_defense_arsenal]

[^phage_defense_arsenal]: [phage defense arsenal](../sources/phage_defense_arsenal__REPORT.md)
