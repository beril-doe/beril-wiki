---
type: "Concept"
description: "How KO-level functional profiles partition by habitat and soil pH/horizon in metagenome workflows, and how much of the enrichment reflects taxonomic abundance shifts; stops at single-study NEON evidence."
sources: ["summaries/neon_mag_functional_discovery__REPORT.md"]
---
# Habitat and soil-chemistry structuring of metagenomic functional gene content

In the NEON metagenome study, KEGG ortholog (KO) functional profiles separate strongly by habitat. [src: neon_mag_functional_discovery] Within soil, pH explains more of the variation than horizon does. [src: neon_mag_functional_discovery] Enrichment in universal modules probably reflects taxonomic abundance shifts, not new functional capability. [src: neon_mag_functional_discovery] All of this evidence comes from one study ([[entities/nmdc-neon-metagenome-studies]]; see also [[summaries/neon_mag_functional_discovery__REPORT]]).

## Habitat partitioning of functional gene content

The analysis used Aitchison-distance principal coordinates analysis (PCoA) on 2,506 MetagenomeAnnotation workflows and 9,584 prevalence-filtered KOs. [src: neon_mag_functional_discovery] Habitat partitioned functional content with a PERMANOVA (permutational multivariate analysis of variance) pseudo-F of 137 and p = 0.001. The groups were soil n=1,800, benthic n=618 and water n=88 workflows. [src: neon_mag_functional_discovery] Principal component 1 (PC1) captured 43.8% of variance and cleanly separated cyanobacterial/water samples from soil. [src: neon_mag_functional_discovery] See [[entities/permanova]] for the method.

## Enriched modules and the taxonomic-shift caveat

At Benjamini-Hochberg false discovery rate (BH-FDR) < 0.05, soil had 3 enriched KEGG modules [src: neon_mag_functional_discovery], benthic had 23 [src: neon_mag_functional_discovery] and water had 16. [src: neon_mag_functional_discovery] The list was dominated by central or housekeeping modules: M00178 ribosome, M00184 RNA polymerase, M00155 cytochrome c oxidase and M00159 ATPase. [src: neon_mag_functional_discovery] The report cautions that enrichment of such universal machinery usually reflects a taxonomic-abundance shift, for example Cyanobacteria over-represented in water. It does not usually mean acquisition of a novel capability. [src: neon_mag_functional_discovery] The report finds the interpretable signal in niche-specific modules. These are photosystems M00161 and M00163 in water and benthic samples, anaerobic-respiration markers and transport systems in benthic samples, and substrate-degradation modules in soil. [src: neon_mag_functional_discovery] For related artifacts, see [[concepts/module-level-enrichment-artifacts-from-broad-substrate-enzymes]].

The KBase Data Lakehouse table nmdc_arkin.kegg_module_terms has 370 rows with module_id only. Its name and category fields are empty, so labels for top hits came from external KEGG references. This limited deeper interpretation. [src: neon_mag_functional_discovery] See annotation and environmental metadata table gaps in the data lakehouse and [[entities/kegg]].

## Soil pH versus horizon

Within soil, pH is the stronger factor. The pH bin factor (4 levels, n = 1,700) gave pseudo-F = 32.5, p = 0.001 and R² = 5.4%, which passes the 5% threshold. [src: neon_mag_functional_discovery] Soil horizon (O / M; n = 1,800) gave pseudo-F = 40.5, p = 0.001 and R² = 2.2%, which fails it. [src: neon_mag_functional_discovery] The value p = 0.001 is the smallest attainable with 999 permutations. [src: neon_mag_functional_discovery] The report reads horizon's weak R² as consistent with pH absorbing much of the horizon signal, because organic-horizon samples tend toward lower pH and mineral samples toward neutral pH. [src: neon_mag_functional_discovery] A nested model would likely show pH × horizon interaction capturing additional variance. That test was not pre-registered and is left for follow-up. [src: neon_mag_functional_discovery]

## Archaea and eukaryotes

Of the 1,609 MQ+HQ MAGs (metagenome assembled genomes), only 40 are archaeal. All 40 come from soil, and 4 are HQ. [src: neon_mag_functional_discovery] Fourteen are credibly eukaryotic under the eukaryotic_evaluation_completeness ≥ 50% criterion. [src: neon_mag_functional_discovery] A clean cross-domain functional comparison was not feasible at this sample size, so archaea remain a soil-only side panel for future work. [src: neon_mag_functional_discovery] The report considers 40 soil archaeal MAGs too few for the main analysis. It considers them enough for a focused per-MAG functional contrast, with Methanobacterium, Methanosarcina and Nitrososphaera present. [src: neon_mag_functional_discovery] See [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys]].

## Open Directions

- Fit a nested or interaction PERMANOVA (pH × horizon) on the soil workflows to test whether the interaction recovers the variance that horizon alone misses.
- Repeat the habitat enrichment after adjusting for taxonomic composition, for example by stratifying by taxon. This would show how much housekeeping-module enrichment is only an abundance shift.
- Fill the kegg_module_terms name and category fields, then re-label the enriched modules.
- Run a per-MAG functional contrast of the 40 soil archaeal MAGs (Methanobacterium, Methanosarcina, Nitrososphaera).
- Test whether the habitat and pH patterns replicate in a study other than NEON.
