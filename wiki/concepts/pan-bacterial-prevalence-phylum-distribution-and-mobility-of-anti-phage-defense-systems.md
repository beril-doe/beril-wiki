---
type: "Concept"
description: "How common each defense family (including SNIPE) is across bacterial species pangenomes and phyla, how detection method changes prevalence, and what core/accessory/singleton splits imply about horizontal transfer; stops at distribution, not mechanism."
sources: ["summaries/discoveries.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Pan-bacterial prevalence, phylum distribution and mobility of anti-phage defense systems

Defense markers are found in almost every bacterial species pangenome in the KBase Data Lakehouse. [src: phage_defense_arsenal] This page covers how common each defense family is across species pangenomes and phyla, how detection method changes prevalence, and what core/accessory/singleton splits imply about horizontal transfer. The evidence is two computational annotation surveys: a seven-family survey and a survey of the SNIPE domain DUF4041. The CRISPR numbers depend strongly on detection method. [src: phage_defense_arsenal] SNIPE is spread across many phyla, and its patchy distribution is read as consistent with horizontal gene transfer of defense islands. [src: snipe_defense_system] See [[entities/snipe]], [[entities/crispr-cas]] and [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

## Prevalence across species pangenomes

Detection of seven defense families covered 27,626 of 27,690 (99.8 %) species-level pangenomes and gave 930,573 marker hits across 825,476 unique gene clusters. [src: phage_defense_arsenal] After strict/stringent filtering, 27,565 species have at least one defense system. [src: phage_defense_arsenal]

Species-level prevalence across the 27,626 species ranges widely by family [src: phage_defense_arsenal]:

| Family | Prevalence |
|---|---|
| CRISPR-Cas | 96.1 % [src: phage_defense_arsenal] |
| BREX | 80.1 % [src: phage_defense_arsenal] |
| R-M Type I | 76.8 % [src: phage_defense_arsenal] |
| DISARM (strict) | 58.4 % [src: phage_defense_arsenal] |
| Retron | 54.7 % [src: phage_defense_arsenal] |
| R-M Type II | 38.9 % [src: phage_defense_arsenal] |
| Gabija | 22.8 % [src: phage_defense_arsenal] |
| CBASS | 7.2 % [src: phage_defense_arsenal] |

The CRISPR-Cas figure is inflated by method. Permissive eggNOG description matching gives 96 % species prevalence, whereas the specific Cas1 Pfam (PF01867) is present in only about 55 % of species. [src: phage_defense_arsenal] The report calls this an over-count of about 40 percentage points. [src: phage_defense_arsenal] It warns that cross-study CRISPR comparisons must state the detection method. [src: phage_defense_arsenal] It says its prevalence estimates are upper bounds. [src: phage_defense_arsenal]

## Phylum distribution

Phylum-level patterns, restricted to the 9 phyla with ≥100 species in the ≥5-genome analysis set (7,323 species), are consistent with the pan-bacterial totals. [src: phage_defense_arsenal] The ≥5-genome threshold is used because reliable core/accessory calls need at least five genomes per species. [src: phage_defense_arsenal] Specific patterns:

- R-M Type I is nearly ubiquitous in Pseudomonadota and Bacillota (>80 %). [src: phage_defense_arsenal]
- CBASS is sparse across all phyla (<20 % except Bacteroidota at ~10-15 %). [src: phage_defense_arsenal]
- Gabija is enriched in Bacillota (30-40 %) relative to Actinomycetota (<10 %). [src: phage_defense_arsenal]
- CRISPR-Cas is very rare in Mycobacterium and Streptomyces gene-content data. [src: phage_defense_arsenal]

The report cites Vassallo et al. for about 5 defense systems per genome and large variation in repertoires across phyla. [src: phage_defense_arsenal]

## SNIPE distribution

A DUF4041 (PF13250) survey of the 293K-genome pangenome found 4,572 gene clusters across 1,696 species and 33 phyla. [src: discoveries, snipe_defense_system] The report states this exceeds the >500 homologues reported in Saxton et al. 2026. [src: discoveries, snipe_defense_system] An InterPro/UniProt (IPR025280) set lists 1,612 SNIPE proteins across 1,373 species. [src: snipe_defense_system] The report does not relate this count to the pangenome count.

Species counts by phylum, with family and genus counts:

| Phylum | Species | Families | Genera |
|---|---|---|---|
| Pseudomonadota | 556 [src: snipe_defense_system] | 54 | 183 |
| Actinomycetota | 334 [src: snipe_defense_system] | 30 | 105 |
| Bacillota_A | 275 [src: snipe_defense_system] | 28 | 151 |
| Bacillota | 206 [src: snipe_defense_system] | 37 | 83 |
| Bacteroidota | 114 [src: snipe_defense_system] | 32 | 61 |
| Nitrospirota | 45 [src: snipe_defense_system] | 2 | 12 |
| Cyanobacteriota | 28 [src: snipe_defense_system] | 13 | 22 |
| Planctomycetota | 22 [src: snipe_defense_system] | 10 | 18 |

## Core, accessory and singleton splits

Six of seven defense systems show highly significant enrichment in the auxiliary and singleton pangenome. The baseline is 46.8 % core and 37.9 % singleton across 132,531,501 gene clusters. [src: phage_defense_arsenal] Per-system core fractions differ from the baseline with χ² p ≈ 0 for all systems. [src: phage_defense_arsenal]

| System | Core % | Singleton % | Class |
|---|---|---|---|
| Retron | 8.2 [src: phage_defense_arsenal] | 65.8 | Strong accessory |
| Gabija | 9.1 [src: phage_defense_arsenal] | 68.8 | Strong accessory |
| R-M Type II | 9.4 [src: phage_defense_arsenal] | 68.2 | Strong accessory |
| R-M Type I | 9.8 [src: phage_defense_arsenal] | 65.3 | Strong accessory |
| CBASS | 11.8 [src: phage_defense_arsenal] | 61.1 | Strong accessory |
| BREX | 20.7 [src: phage_defense_arsenal] | 55.8 | Moderate accessory |
| CRISPR-Cas | 27.4 [src: phage_defense_arsenal] | 47.2 | Mild accessory |
| DISARM | 40.6 [src: phage_defense_arsenal] | 42.3 | Near baseline |

R-M Type II is 9 % core and 68 % singleton at pangenome scale. [src: phage_defense_arsenal] The accessory-enriched systems have singleton fractions 1.5–1.8× above the 37.9 % baseline. The report reads this as consistent with active horizontal transfer of defense loci through mobile genetic elements. [src: phage_defense_arsenal]

For SNIPE, 86.7 % of genes are accessory or singleton. [src: discoveries, snipe_defense_system] The DUF4041 split is 13.3 % core (604 clusters) and 30.7 % accessory non-core, non-singleton (~1,402 clusters). [src: snipe_defense_system] Singletons alone are 56.1 % (2,566 clusters). [src: snipe_defense_system] The report reads this as strong support for defense island mobility. It concludes SNIPE is typically gained or lost rather than vertically inherited, since only 13.3 % of clusters are core. [src: snipe_defense_system] It also takes the patchy spread across many phyla and families as support for horizontal gene transfer. [src: discoveries, snipe_defense_system] These are interpretations of distribution. Transfer was not measured directly.

The SNIPE report tested a null hypothesis of rare, randomly distributed SNIPE genes against an alternative of cross-phylum, mostly accessory genes enriched in environmental isolates. [src: snipe_defense_system] It rejects random distribution for taxonomic distribution and environmental niche. [src: snipe_defense_system] It concludes the alternative is supported on all four of its axes, and calls the support strong. [src: snipe_defense_system] One planned comparison, COG (clusters of orthologous groups) V defense gene density in SNIPE versus non-SNIPE species, could not be completed through the REST (representational state transfer) API (application programming interface), because the join needs Spark Connect. [src: snipe_defense_system]

## Open Directions

- Rerun the CRISPR-Cas prevalence and core/accessory split using Pfam Cas1 and other specific Cas Pfams alongside eggNOG descriptions. This would show how much of the mild-accessory result depends on permissive matching.
- Run the SNIPE versus non-SNIPE COG V defense-density comparison in Spark Connect. This would close the gap left by the REST API limit.
- Test mobility directly. Check whether accessory and singleton defense clusters sit near mobile-element markers in the same genomes, rather than inferring transfer from singleton fractions alone.
- Reconcile the InterPro 1,373-species set with the pangenome 1,696-species set. This would show which species each method misses.
- Add per-phylum core/accessory splits for each family. The phylum prevalence results do not give them.
