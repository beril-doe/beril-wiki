---
type: "Concept"
description: "Batch-controlled variation of eukaryotic read fraction with vegetation and geography inside a single soil study; stops at one study and does not extend to aquatic or host-associated collections."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Within-study environmental drivers of eukaryotic DNA in soil metagenomes

Within one batch-controlled NEON soil metagenome study, the eukaryotic read fraction varies strongly with local vegetation and with site geography. The evidence comes from a single report and a single soil study, so it does not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates] See [[summaries/euk_in_prok_correlates__REPORT]] for the whole report and [[concepts/study-and-batch-confounding-of-cross-collection-metadata-correlates]] for the batch problem this design avoids.

## Design

The analysis restricts to the dominant study, a NEON soil metagenome study with 1,186 runs, one sampling program and constant protocol/batch. [src: euk_in_prok_correlates] The report says the genuine environmental signal is recoverable only within a batch-controlled study. [src: euk_in_prok_correlates] Sampling depth is not measured in this study (zero non-null depth values), so the report's depth association is cross-study and not part of this result. [src: euk_in_prok_correlates] See also [[entities/nmdc-neon-metagenome-studies]].

## Vegetation

Eukaryotic fraction differs across 11 levels of local vegetation (env_local_scale; Kruskal H=119.1, p=7.6×10⁻²¹). [src: euk_in_prok_correlates] Medians are highest in sedge/forb herbaceous soil (23%), then emergent wetland (14%), dwarf scrub (13%) and evergreen forest (2%). [src: euk_in_prok_correlates] The fraction is ≈0 in deciduous forest, cropland and pasture. [src: euk_in_prok_correlates]

## Geography

Eukaryotic fraction also varies across 47 sites (Kruskal H=310.4, p=2.4×10⁻⁴⁶). [src: euk_in_prok_correlates] Arctic tundra sites are highest: Utqiaġvik 30%, Caribou-Poker Creeks 22% and Toolik 17%. [src: euk_in_prok_correlates] Temperate forests are at 2–8%. [src: euk_in_prok_correlates]

## Predictability and interpretation

Local environment plus geography predicts the fraction with within-study 5-fold R² = +0.17 ± 0.06. This contrasts with the cross-study out-of-study R² = −0.30. [src: euk_in_prok_correlates] The report reads the +0.17 as a genuine fine-scale environment effect. [src: euk_in_prok_correlates] It interprets the pattern as eukaryotic contamination of soil metagenomes being set largely by aboveground photosynthetic input. [src: euk_in_prok_correlates] This is the report's interpretation, not a direct measurement.

## Caveats

Within-study control is the best available, not randomized: env_local_scale and geography may track sampling-campaign sub-batches. [src: euk_in_prok_correlates] The result is shown for one soil study only. [src: euk_in_prok_correlates] The report proposes extending the design to aquatic and plant-associated NMDC studies to test whether the vegetation/geography effect generalizes beyond soil. [src: euk_in_prok_correlates]

## Open Directions

- Repeat the within-study design in the aquatic and plant-associated NMDC studies. This tests whether the effect generalizes beyond soil, and whether the algal-plastid versus root-fungal source split holds within batch-controlled cohorts.
- Test whether sampling campaign explains the vegetation and site effects. Add campaign as a covariate or stratum in the NEON study. This addresses the sub-batch confounding caveat.
- Compare the Arctic tundra sites with other cold or peat sites, to see whether the high fraction follows vegetation or climate.
