---
type: "Other"
description: "The COG functional classification scheme (single-letter categories such as J, L, V, S) used to compare gene classes."
sources: ["summaries/cog_analysis__REPORT.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
aliases: ["COG", "COG categories"]
---
# Clusters of Orthologous Groups functional categories

This page covers the COG functional classification scheme (single-letter categories such as J, L, V, S) used to compare gene classes. The clusters of orthologous groups (COG) letters appear in reports on ecotype-differentiated genes [src: ecotype_functional_differentiation] and on multi-copy genes. [src: gene_copy_number_variation] A soil analysis also uses COG-metal associations, where transporter and biosynthesis genes dominate the top hits. [src: soil_metal_functional_genomics]

## Key facts

- Letters used in these reports include J (translation), L (mobile elements, or replication/recombination/repair), V (defense), S (unknown function), C (energy production), E (amino acid metabolism), F (nucleotide metabolism), H (coenzyme metabolism), G (carbohydrate metabolism), M (cell wall), P (inorganic ion transport), Q (secondary metabolites), and K (transcription). [src: cog_analysis, ecotype_functional_differentiation]
- The cog_analysis report uses composite codes. "LV" means mobile plus defense, and "EGP" means amino acid plus carbohydrate plus inorganic ion functions. [src: cog_analysis] The report states that such composite assignments are not annotation artifacts. [src: cog_analysis]
- Composite categories are counted once per gene rather than split. [src: cog_analysis]
- eggNOG v6 annotations may differ from the original COG assignments. [src: cog_analysis]
- In the ecotype analysis, only about 38% of gene clusters have COG annotations (from NB01). [src: ecotype_functional_differentiation]

## Core versus novel genes

An analysis of 32 species across 9 phyla (357,623 genes) found a consistent "two-speed genome". [src: cog_analysis] Novel/singleton genes were enriched for L (mobile elements) by +10.88%, with 100% consistency across species. The report called this the strongest signal. [src: cog_analysis] They were also enriched for V (defense) by +2.83% with 100% consistency. [src: cog_analysis] They were enriched for S (unknown function) by +1.64% with 69% consistency. [src: cog_analysis] LV showed +0.34% enrichment and 76% consistency. [src: cog_analysis]

The report identifies core genes as enriched in several metabolic and translation categories. It reports these values, which are negative in its novel-versus-core comparison:

- J (translation): -4.65%, 97% consistency, the strongest depletion. [src: cog_analysis]
- F (nucleotide metabolism): -2.09%, 100% consistency. [src: cog_analysis]
- H (coenzyme metabolism): -2.06%, 97% consistency. [src: cog_analysis]
- E (amino acid metabolism): -1.81%, 81% consistency. [src: cog_analysis]
- C (energy production): -1.75%, 88% consistency. [src: cog_analysis]

The report calls the J and C result consistent with Charlesworth & Jensen (2022) and the minimal-genome literature. [src: cog_analysis] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]] and [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]].

## Ecotype differentiation

In 12 bacterial species, the share of species with significant ecotype differentiation varied by category. G differentiated in 10/12 species (83.3%). [src: ecotype_functional_differentiation] E, S and V each differentiated in 11/12 species (91.7%). [src: ecotype_functional_differentiation] The least differentiated categories were A (RNA processing, 1/9), B (chromatin, 1/8) and Z (cytoskeleton, 2/6). [src: ecotype_functional_differentiation]

Adaptive categories had a significance rate of 79.8% (67/84), against 68.8% (33/48) for housekeeping categories, a ratio of 1.16x. [src: ecotype_functional_differentiation] Mean effect size was 0.0136 for adaptive and 0.0064 for housekeeping categories, a ratio of 2.13x. [src: ecotype_functional_differentiation] S (mean effect 0.039, 11/12 species) and L (mean effect 0.034, 9/12 species) had the largest mean effects. [src: ecotype_functional_differentiation] The report says P (9/12 species) and S (11/12 species, largest effect) confirm earlier single-species findings and extend them to 12 species. [src: ecotype_functional_differentiation]

Per-category results, as significant species out of 12 and mean effect:

- E, Adaptive: 11/12, 0.0120. [src: ecotype_functional_differentiation]
- S, Other: 11/12, 0.0392. [src: ecotype_functional_differentiation]
- V, Adaptive: 11/12, 0.0078. [src: ecotype_functional_differentiation]
- G, Adaptive: 10/12, 0.0176. [src: ecotype_functional_differentiation]
- M, Adaptive: 9/12, 0.0155. [src: ecotype_functional_differentiation]
- L, Other: 9/12, 0.0337. [src: ecotype_functional_differentiation]
- C, Housekeeping: 9/12, 0.0095. [src: ecotype_functional_differentiation]
- P, Adaptive: 9/12, 0.0170. [src: ecotype_functional_differentiation]
- Q, Adaptive: 9/12, 0.0112. [src: ecotype_functional_differentiation]
- K, Adaptive: 8/12, 0.0141. [src: ecotype_functional_differentiation]
- J, Housekeeping: 8/12, 0.0051. [src: ecotype_functional_differentiation]
- F, Housekeeping: 8/12, 0.0041. [src: ecotype_functional_differentiation]
- H, Housekeeping: 8/12, 0.0069. [src: ecotype_functional_differentiation]

See [[concepts/functional-differentiation-of-gene-content-ecotypes-across-cog-categories]].

## Multi-copy genes and class definitions

The gene copy-number report shows that the housekeeping label does not fit all COG categories. Species-level median multi-copy rates were L 1.12%, V 0.11%, M 0.11% and K 0.12%. F was 0.062% and H was 0.041%. [src: gene_copy_number_variation] A pilot (NB01) found J at 2.07% multi-copy, 5th of 21 categories. The report attributes this to ribosomal protein paralogs, tRNA duplications and rRNA operon multiplicity. [src: gene_copy_number_variation]

J was therefore treated as "mixed" rather than housekeeping in the KBase Data Lakehouse pangenome projects. [src: gene_copy_number_variation] C was also reclassified as mixed, because cytochrome paralogs cause the same problem. [src: gene_copy_number_variation] NB01b classified F and H as housekeeping, L, V, M and K as adaptive, and C and J as mixed. [src: gene_copy_number_variation] The report argues that housekeeping = {F, H} is stricter than the textbook informational-versus-operational divide, because J is intermediate rather than strictly dosage-constrained. [src: gene_copy_number_variation] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

## Use as a coarse proxy

In an ENIGMA subset, contamination gradients did not produce a robust community-level shift in inferred stress-related functional potential. That result was aggregated at genus resolution from broad COG categories. [src: enigma_contamination_functional_potential] Genus-level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential] COG-fraction proxies are coarse summaries, not curated resistance pathways. [src: enigma_contamination_functional_potential] See [[concepts/coarse-cog-fraction-proxies-versus-pathway-level-stress-evidence]].

## COG-metal associations in soil

In soil, the analysis found 2,355 significant COG-metal associations (false discovery rate, FDR, < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 samples. [src: soil_metal_functional_genomics] Chromium and lead drive the strongest signals, and transporters (ABC, RND) and biosynthesis genes dominate the top hits. [src: soil_metal_functional_genomics] ABC means ATP-binding cassette. The report calls the 60% discovery rate from 9 metals × 435 COGs = 3,915 tests high. [src: soil_metal_functional_genomics] Spearman ρ effect sizes have not been systematically reported, so many associations may be statistically significant but biologically small. [src: soil_metal_functional_genomics] Mechanistic classification of significant COGs into resistance, stress, membrane, energy and unknown categories is still pending. [src: soil_metal_functional_genomics]
