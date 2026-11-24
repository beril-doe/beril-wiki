---
type: "Summary"
description: "Summary of the project Gene Copy Number Variation Across Pangenome Functional Categories."
doc_type: "short"
full_text: "sources/gene_copy_number_variation__REPORT.md"
---
# Gene Copy Number Variation Across Pangenome Functional Categories

This report asks whether bacterial gene copy number differs between adaptive and housekeeping functional categories across pangenomes. Across 24 species in 5 phyla, adaptive clusters of orthologous groups (COG) categories L, V, M, K have higher multi-copy rates than housekeeping categories F, H in every species. The effect is largely a core versus accessory effect, which weakens the COG-label reading. Evidence is a direct statistical test on 24 species. [src: gene_copy_number_variation] The report says this is, to its knowledge, the first pangenome-scale systematic test of the housekeeping-versus-adaptive copy-number-constraint hypothesis across bacterial phyla. [src: gene_copy_number_variation]

## Key Findings

### Adaptive versus housekeeping at species level

Adaptive categories show higher cluster-carrier-weighted multi-copy rates in 24 of 24 species, with median species-level ratio 8.14× (paired Wilcoxon signed-rank, p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation] The metric is SUM(multicopy) / SUM(carriers). [src: gene_copy_number_variation] The report describes this weighted metric as robust to the sparse, rare-event nature of paralog expansion in bacterial pangenomes. [src: gene_copy_number_variation] All 8 pairwise F/H × L/V/M/K tests reject equal medians at BH-FDR (Benjamini-Hochberg false discovery rate) adjusted p < 0.01; the smallest p-adj is 4.8 × 10⁻⁷ for F–L and H–L. [src: gene_copy_number_variation]

Species-level median multi-copy rates by category:

| COG | Median |
|---|---|
| L (replication/recombination/repair) | 1.12% [src: gene_copy_number_variation] |
| V (defense) | 0.11% [src: gene_copy_number_variation] |
| M (cell wall) | 0.11% [src: gene_copy_number_variation] |
| K (transcription) | 0.12% [src: gene_copy_number_variation] |
| F (nucleotide metabolism) | 0.062% [src: gene_copy_number_variation] |
| H (coenzyme metabolism) | 0.041% [src: gene_copy_number_variation] |

The report reads this as strong support for H1. Housekeeping F and H sit three orders of magnitude below the ~5% pseudogene / rare-variant background expected under neutral drift. [src: gene_copy_number_variation] Housekeeping clusters are near-uniformly single-copy, which the report calls consistent with the dosage-balance hypothesis extended to bacteria. [src: gene_copy_number_variation] Adaptive COGs, especially L, show 20–30× the housekeeping rate. [src: gene_copy_number_variation] L contains transposases, integrases and IS elements, which are known to expand in bacterial pangenomes. [src: gene_copy_number_variation]

### Consistency across phyla

The direction is unanimous across 5 phyla and 24 species, but the effect size varies 4-fold. [src: gene_copy_number_variation] Ratios are of mean adaptive to mean housekeeping rate. [src: gene_copy_number_variation]

| Phylum | n species | Housekeeping (%) | Adaptive (%) | Ratio |
|---|---|---|---|---|
| Pseudomonadota | 5 | 0.034 | 0.528 | 15.4× [src: gene_copy_number_variation] |
| Bacillota | 5 | 0.061 | 0.570 | 9.4× [src: gene_copy_number_variation] |
| Actinomycetota | 5 | 0.078 | 0.705 | 9.0× [src: gene_copy_number_variation] |
| Bacteroidota | 5 | 0.172 | 0.871 | 5.1× [src: gene_copy_number_variation] |
| Campylobacterota | 4 | 0.077 | 0.309 | 4.0× [src: gene_copy_number_variation] |

The report proposes that this variation tracks accessory-genome dynamics. Pseudomonadota has the largest and most mobile accessory genomes in the set, and Campylobacterota the smallest and most streamlined. [src: gene_copy_number_variation]

### Core versus accessory interaction

The species-level 8× effect collapses to 2× when restricted to fixation-level (core) clusters. [src: gene_copy_number_variation] Core clusters are copy-number-constrained regardless of category: adaptive-core median 0.06% exceeds housekeeping-core 0.03% by only 2× (p = 4.9 × 10⁻⁴). [src: gene_copy_number_variation] Core clusters are close to strictly single-copy regardless of function. [src: gene_copy_number_variation] Accessory clusters carry the effect. Adaptive accessory clusters have median 1.55%, 25× adaptive core at 0.06% (Wilcoxon p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation] Housekeeping accessory clusters are at 0.29%, 10× housekeeping core at 0.03% (p = 1.2 × 10⁻⁴). [src: gene_copy_number_variation] Within the accessory pool, adaptive is 5× housekeeping (1.55% vs 0.29%; p = 3.3 × 10⁻⁶). [src: gene_copy_number_variation] Accessory clusters accommodate paralogs, and adaptive categories accommodate them 5× more than housekeeping. [src: gene_copy_number_variation] All four one-sided Wilcoxon tests in the 2×2 analysis were significant. [src: gene_copy_number_variation]

The report says the class × core-status interaction is much stronger than either main effect alone: adaptive-accessory is 25× adaptive-core, versus 5× for housekeeping-accessory to housekeeping-core. [src: gene_copy_number_variation] It claims, to its knowledge, the first demonstration that the class effect concentrates in accessory clusters. [src: gene_copy_number_variation]

The report concludes that paralog expansion happens in accessory clusters, preferentially in L, V, M, K. [src: gene_copy_number_variation] It says the pattern is largely encoded in the core/accessory split rather than the COG label, with core medians of 0.03–0.06% across categories. [src: gene_copy_number_variation] It considers H4 strongly supported and reads the class effect as about which clusters get to expand into paralogy, not which genes tolerate paralogy at fixation. [src: gene_copy_number_variation] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

### Category J and C classification

Category J (translation) behaves as mixed rather than housekeeping at species scale in these pangenome projects. [src: gene_copy_number_variation] Pilot NB01 found J at 2.07% multi-copy, 5th of 21 categories, driven by ribosomal protein paralogs, tRNA duplications and rRNA operon multiplicity. [src: gene_copy_number_variation] J was reclassified as mixed, alongside C (energy production, with cytochrome paralogs), which made the test tight. [src: gene_copy_number_variation] The report calls F and H a much stricter housekeeping definition than the textbook informational-versus-operational divide. [src: gene_copy_number_variation] See [[entities/clusters-of-orthologous-groups-functional-categories]].

### Metric choice

The metric changed the apparent effect. A binary any-multi-copy-in-≥1-genome flag gave 1.4× (NB01 cell 15). The carrier-weighted rate on the same pilot data gave 3.3× (NB01b cell 9) and 8.1× at scale (NB03 cell 6). [src: gene_copy_number_variation] In the pilot the binary metric showed the expected direction in 5/5 species but a weak effect, which triggered plan revision. [src: gene_copy_number_variation] The report says binary any-multi-copy flags underestimate the effect by ~6× at pilot scale. [src: gene_copy_number_variation] It says the binary flag is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation] It proposes carrier-weighted rates for any sparse event whose signal lies in degree rather than presence. [src: gene_copy_number_variation] See [[concepts/carrier-weighted-versus-binary-metrics-for-sparse-pangenome-events]].

### Relation to prior literature

- Pushker et al. 2004 reported remarkable preservation of copy numbers in housekeeping gene sets across closely related bacteria. [src: gene_copy_number_variation] The report says its finding extends this from same-species comparisons to a pangenome-wide, 24-species, 5-phylum picture and quantifies the class × core-status interaction directly. [src: gene_copy_number_variation]
- Gevers et al. 2004 noted that housekeeping (core) genes are duplicated less frequently and, when duplicated, are more likely to be pseudogenized. [src: gene_copy_number_variation] The report says its pangenome-scale reproduction of the housekeeping-versus-adaptive gradient complements Gevers' single-genome paralog-retention framing. [src: gene_copy_number_variation]
- Sotiropoulos et al. 2026 reported high levels of TE (transposable element) insertion driving accessory-gene copy-number variation in wheat pathogens. [src: gene_copy_number_variation] The report calls its L-dominance and adaptive-accessory enrichment consistent with the same transposable-element expansion mechanism operating across the bacterial tree of life. [src: gene_copy_number_variation]
- Elliott, Cuff & Neidle 2013 discussed positive selection for gene dosage in microbial genome amplification. [src: gene_copy_number_variation] The report calls its finding that adaptive-accessory clusters are the primary site of copy-number variation consistent with dosage-driven amplification of environmentally responsive genes. [src: gene_copy_number_variation]
- Prior work by Pushker, Gevers and Lalanne tested individual related-bacterium pairs or single organisms. The report instead tests 24 species across 5 phyla with a uniform pipeline built on the KBase Data Lakehouse. [src: gene_copy_number_variation]

## Data and Methods

The workflow had five stages, NB01, NB01b, NB02, NB03 and NB04, the last being the interaction analysis:
- NB01 was the pilot extraction of per-cluster per-genome copy counts, 5 species × 5 phyla. [src: gene_copy_number_variation]
- NB01b switched to the carrier-weighted rate. F and H were housekeeping, L, V, M and K adaptive, and C and J mixed. [src: gene_copy_number_variation] The pooled ratio was 3.3×, with Mann-Whitney on cluster CVs (cross-validation) p = 1.6 × 10⁻⁷, and all 4 pre-registered gates passed. [src: gene_copy_number_variation]
- NB02 used src/extract_multi_species.py for 24 species × 5 phyla, with incremental per-species CSV output. [src: gene_copy_number_variation] Species ran in two batches (18 + 6 after a background-task timeout), and resumable-skip logic made the interruption cost-free. [src: gene_copy_number_variation]
- NB03 ran the primary species-level test. [src: gene_copy_number_variation]
- NB04 ran the class × core-status 2×2 analysis. [src: gene_copy_number_variation]

The analysis spanned about 2.4 million gene-cluster × genome observations (approximate: 24 species × ~100 genomes × ~1000 carrier-clusters). [src: gene_copy_number_variation] It produced 2,768 per-species per-COG per-is_core rows [src: gene_copy_number_variation] and 481 single-letter COG species-level rows for tests. [src: gene_copy_number_variation] Species had 50–249 genomes each. [src: gene_copy_number_variation]

The report draws on the KBase Data Lakehouse kbase_ke_pangenome collection. It uses the gene, gene_genecluster_junction, gene_cluster, genome, eggnog_mapper_annotations, pangenome and gtdb_species_clade tables for gene-to-genome-to-cluster mapping, COG annotations, species selection metadata, and core/accessory flags. [src: gene_copy_number_variation] Gene clusters come from motupan at 90% AAI. [src: gene_copy_number_variation]

Output files include per-cluster pilot copy statistics (236,326 rows for the 5 pilot species), a 24-row reduced species manifest used in NB02, and 8 rows of pairwise Wilcoxon tests with BH-FDR. [src: gene_copy_number_variation] The 24-species pilot took ~80 min on JupyterHub. [src: gene_copy_number_variation]

## Caveats and Open Work

- Copy-number analyses should stratify by is_core before inferring functional constraint, because an unstratified 8× effect becomes 2× within core and 5× within accessory. [src: gene_copy_number_variation]
- Clusters come from motupan at 90% AAI. Recent paralogs diverged <10% merge into one cluster and ancient paralogs diverged >10% appear as separate clusters, so the analysis captures operationally recognized rather than phylogenetically complete paralogs. [src: gene_copy_number_variation]
- Fragmented metagenome-assembled genomes (MAGs) can inflate or deflate multi-copy counts, and contig artifacts enter the per-cluster-per-genome metrics linearly. [src: gene_copy_number_variation] The report does not condition on checkm_completeness or contig N50 and says a robustness pass on the tightest-quality genome subset would strengthen the claim. [src: gene_copy_number_variation] It proposes restricting to checkm_completeness ≥ 95 and checkm_contamination ≤ 2 and rerunning NB03 to test whether fragmented assemblies inflate the L effect. [src: gene_copy_number_variation]
- The 24 species were selected for 50–300-genome coverage, which oversamples clinically important and well-studied taxa. [src: gene_copy_number_variation]
- The 5 phyla (Pseudomonadota, Bacillota, Bacteroidota, Actinomycetota, Campylobacterota) are the top 5 by candidate count, and candidate phyla radiation (CPR), Patescibacteria, Spirochaetota and archaea are left out. [src: gene_copy_number_variation]
- The Spirochaetota pilot species Borreliella burgdorferi was retained but flagged as a multi-partite-genome outlier. Plasmid-borne duplication raises housekeeping and adaptive rates together and breaks the direction test. [src: gene_copy_number_variation]
- Housekeeping {F, H} covers ~5% of species-level rows and adaptive {L, V, M, K} ~15%. [src: gene_copy_number_variation] Roughly 80% of clusters are "other" and excluded from the primary test, so extrapolating the class effect to all bacterial genes is not automatic. [src: gene_copy_number_variation]
- The report does not test direct positive selection on copy number. Its observations fit purifying selection against dosage imbalance for housekeeping paralogs, neutral tolerance for adaptive paralogs plus positive selection on some, or proximity to mobile elements. [src: gene_copy_number_variation] Distinguishing these needs dN/dS on paralog pairs and mobile-element context data. [src: gene_copy_number_variation]
- The three-way join (gene × gene_genecluster_junction × gene_cluster, ~1B rows each) took 140–290 s per species, median ~200 s. [src: gene_copy_number_variation] The 24-species pilot needs ~80 min. The report recommends CTS batch processing rather than a JupyterHub notebook loop for 100+ species. [src: gene_copy_number_variation] See [[entities/spark-extraction-of-per-species-pangenome-copy-counts]].
- A background jupyter nbconvert run of the Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV. [src: gene_copy_number_variation] The standalone resumable script streamed progress with print(flush=True) and finished within the same wall-clock budget. [src: gene_copy_number_variation]
- Per-phylum ratios rest on 4–5 species each. [src: gene_copy_number_variation]

### Proposed next analyses

- Split cluster L into IS-element loci (via bakta_amr or genomad_mobile_elements cross-reference, if available in the current KBase Data Lakehouse migration state) versus true DNA repair loci (recA, mutL, uvr*). [src: gene_copy_number_variation] If the effect concentrates in IS elements, the story becomes transposition-mediated copy-number variation rather than adaptive paralogy, which matters for the dosage-balance interpretation. [src: gene_copy_number_variation]
- Scale to 100–200 species for phylum-specific tests and to decompose the Pseudomonadota versus Campylobacterota effect-size difference, using CTS batch processing. [src: gene_copy_number_variation]
- Run a within-genome analysis on species with 200+ high-quality genomes, testing whether adaptive clusters have heavier-tailed copy-count distributions than housekeeping ones, since the current rate metric is between-genome. [src: gene_copy_number_variation]
- Cross-reference with the ~30 Fitness Browser–pangenome-linked species to ask whether paralog copy count correlates with fitness in relevant conditions. [src: gene_copy_number_variation] This would connect the copy-number story to the dosage-selection story of Elliott, Cuff & Neidle 2013. [src: gene_copy_number_variation]

## Slots Into

- [[concepts/paralog-expansion-and-gene-copy-number-constraint]]: core clusters are near-uniformly single-copy, and expansion is accessory and enriched in L, V, M, K. [src: gene_copy_number_variation]
- [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes]]: the 8× class effect falls to 2× within core, so core status confounds it. [src: gene_copy_number_variation]
- [[concepts/carrier-weighted-versus-binary-metrics-for-sparse-pangenome-events]]: binary flag 1.4× versus carrier-weighted 8.1× at scale. [src: gene_copy_number_variation]
- [[entities/clusters-of-orthologous-groups-functional-categories]]: J and C are treated as mixed rather than housekeeping. [src: gene_copy_number_variation]
- [[entities/cog-category-l-replication-recombination-and-repair]]: L has the highest median multi-copy rate, 1.12%. [src: gene_copy_number_variation]
