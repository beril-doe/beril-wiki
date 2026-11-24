---
type: "Concept"
description: "Statistical power, genus clumping, taxonomy tier mismatches and cohort-construction biases limiting lineage-level genome-content comparisons."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md"]
---
# Small-cohort and phylogenetic confounding in lineage-level comparisons

This page covers small-cohort and phylogenetic confounding in lineage-level genome-content comparisons. The evidence comes from one project, the Bacillota_B subsurface comparison, so these are single-case caveats. The comparison used 10 anchor genomes against 62 baseline genomes, and the anchor is genus-clumped. [src: bacillota_b_subsurface_accessory] See [[summaries/bacillota_b_subsurface_accessory__REPORT]] and [[concepts/accessory-gene-content-enrichment-in-subsurface-lineages-relative-to-soil-congeners]] for the comparison itself.

## Cohort size and statistical power

The Bacillota_B comparison has 10 anchor genomes against 62 baseline genomes. [src: bacillota_b_subsurface_accessory] Fisher's exact test (see [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]) is adequate for large effects, and the report considers the 547 enriched ortholog groups (OGs) robust. [src: bacillota_b_subsurface_accessory] Marginal effects with anchor counts of 3–5 should be treated descriptively, not inferentially. [src: bacillota_b_subsurface_accessory] A per-genus analysis with n=10 is at the limit of statistical resolution. [src: bacillota_b_subsurface_accessory]

The report gives two facts about the size of the available pool. The KBase Data Lakehouse pangenome holds only 334 Bacillota_B genomes, far below the 6,700 estimated in the v1.1 plan. [src: bacillota_b_subsurface_accessory] Expanding through [[entities/bacdive]] isolation and taxonomy yielded zero additional Bacillota_B in this run, and the 10-genome anchor came almost entirely from an ncbi_env keyword search. [src: bacillota_b_subsurface_accessory] The report says more clay-isolated Bacillota_B from BacDive linkage, or from future pangenome ingests, would improve power. [src: bacillota_b_subsurface_accessory]

## Genus clumping and phylogenetic confounding

The anchor is clumped in a few genera: 3 BRH-c8a, 2 BRH-c4a, 2 Desulfosporosinus, Desulforudis, Ch130 and 1 other. [src: bacillota_b_subsurface_accessory] It draws on the Mont Terri Opalinus borehole, Mont Terri rock-porewater MAGs (metagenome assembled genomes) and the Russian Beyelii Yar borehole. [src: bacillota_b_subsurface_accessory] The baseline has 62 phylum-matched soil/sediment genomes, dominated by Syntrophomonadales (29) and Desulfitobacteriales (16). [src: bacillota_b_subsurface_accessory]

The cohort spans four orders: Desulfotomaculales, Desulfitobacteriales, Ammonifexales and Thermacetogeniales. This partly mitigates genus-level phylogenetic confounding but does not eliminate it. [src: bacillota_b_subsurface_accessory]

## Taxonomy tier mismatch

Some enriched OGs sit at the coarse root level. [src: bacillota_b_subsurface_accessory] A Bacillota_B-specific OG level would be better, but eggNOG ([[entities/eggnog-orthologous-groups]]) has no such tier. Bacillota_B is defined by GTDB, while eggNOG uses NCBI taxonomy. Under NCBI taxonomy, Bacillota_B genomes are spread across Firmicutes, Negativicutes and Tissierellia at the legacy class level. [src: bacillota_b_subsurface_accessory]

## Cohort-construction bias

The anchor is borehole/porewater-dominated by construction, following the clay-project lesson on cultivation bias toward porewater isolates. [src: bacillota_b_subsurface_accessory] Rock-attached Bacillota_B may differ in gene content, and this comparison cannot test that. [src: bacillota_b_subsurface_accessory] See [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]].

## Open Directions

- Add clay-isolated Bacillota_B through new BacDive linkage or later pangenome ingests. Then rerun the per-genus analysis to see whether it moves beyond the n=10 resolution limit.
- Rerun the enrichment test with genus-level resampling, or with one genome per genus. This would show how much of the 547 enriched OGs depends on clumping.
- Map GTDB Bacillota_B genomes onto NCBI-based eggNOG levels to find finer OG tiers than root. This would address the coarse-tier problem.
- Add rock-attached Bacillota_B genomes or metagenomes to the anchor. This would test the porewater-bias caveat.
