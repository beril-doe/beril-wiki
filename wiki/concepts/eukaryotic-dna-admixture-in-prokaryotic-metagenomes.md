---
type: "Concept"
description: "How much eukaryotic and plastid DNA appears in prokaryote-targeted metagenomes, where it comes from by habitat, and what that means for interpreting metagenomic profiles."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Eukaryotic and Plastid DNA Admixture in Prokaryotic Metagenomes

Metagenomes sequenced to profile prokaryotic communities also carry eukaryotic reads. The size and source of that signal limit how such profiles can be read: a eukaryotic fraction that varies by habitat lowers prokaryotic depth unevenly across samples. The quantitative evidence here comes from one project, [[summaries/euk_in_prok_correlates__REPORT]]. It used read-based taxonomic classifications from [[entities/gottcha2]] stored in the [[entities/nmdc-results]] tables of [[entities/nmdc]] [src: euk_in_prok_correlates].

## Prevalence of the Eukaryotic Signal

The project examined 2,759 NMDC ReadbasedAnalysis runs from 9 studies. Of these, 77% carry detectable eukaryotic reads, with a median eukaryotic fraction of 2.7% and a mean of 13.3%. In 20% of runs the eukaryotic fraction exceeds 20%. Among runs with detectable eukaryotic reads, plastid (plant or algal chloroplast) DNA makes up a median 100% of the eukaryotic signal. Because the mean sits well above the median, the distribution of per-run fractions has a long upper tail. These are per-run summaries, not read-count-weighted totals, so they do not show what share of all eukaryotic reads comes from which runs. Only GOTTCHA2 gave a usable eukaryotic fraction. The report states that its absolute values depend on the reference database and should be read as relative or ordinal, not as calibrated absolute contamination [src: euk_in_prok_correlates].

## Habitat-Specific Sources

The composition of the eukaryotic signal differs sharply by habitat [src: euk_in_prok_correlates]:
- **Freshwater (aquatic):** 99.5% eukaryote detection, a plastid share of 1.00, dominated by algal plastid from phytoplankton chloroplasts [src: euk_in_prok_correlates].
- **Soil (terrestrial):** 55.7% eukaryote detection, a plastid share of 0.43, a mix of plant plastid and soil fungi or protists [src: euk_in_prok_correlates].
- **Plant roots:** 100% eukaryote detection, a plastid share of 0.03, dominated by non-plastid root-associated fungi or protists [src: euk_in_prok_correlates].

## Interpretation: Co-Sampled Environmental DNA, Not Contamination

The report interprets the eukaryotic "contamination" in these metagenomes mainly as co-sampled photosynthetic environmental DNA rather than laboratory or animal-host contamination. In this reading, the signal comes from algal chloroplasts in freshwater, plant chloroplasts and soil fungi in terrestrial samples, and root-associated fungi or protists in plant samples. This is an interpretation of the source composition, not a direct test of contamination pathways. The habitat-level source split has not yet been confirmed within batch-controlled cohorts (see Open Directions), so it may be partly entangled with study-level differences of the kind discussed in [[concepts/study-batch-confounding-of-environmental-associations]] [src: euk_in_prok_correlates].

## Literature Context

The project places its findings against published work. The items below are literature findings reported by the source, not project measurements [src: euk_in_prok_correlates]:
- Eisenhofer, Alberdi & Woodcroft (2026, *mSystems*, PMID 41854267) report biome-specific prokaryotic fractions across 136,284 metagenomes. This is consistent with the habitat dependence observed here [src: euk_in_prok_correlates].
- Sobolev et al. (2025, *IJMS*, PMID 41373768) show that sample matrix, together with extraction kit, drives eukaryotic admixture. This supports a habitat or matrix explanation, but it also raises extraction protocol as a co-varying factor that the habitat comparison does not separate out [src: euk_in_prok_correlates].
- The plastid/chloroplast dominance is reported to match Chevokina et al. (2025, *Front Plant Sci*, PMID 41560914) and the plant-host-depletion literature (Wang et al. 2026, *Plant Biotechnol J*, PMID 41078118) [src: euk_in_prok_correlates].
- Anthony et al. (2024, *Environ Microbiome*, PMID 39095861) likewise attribute poor soil-metagenome resolution to plant/eukaryotic DNA [src: euk_in_prok_correlates].

## Open Directions

- **Extend the within-study design beyond soil:** test, in the aquatic and plant-associated studies, whether the vegetation/geography effect seen within soil generalizes, and whether the split between algal plastid and root fungal sources holds within batch-controlled cohorts. This would close the gap between cross-habitat contrasts and study or batch effects [src: euk_in_prok_correlates].
- **Separate matrix from extraction protocol:** NMDC does not populate DNA-extraction kit, host-depletion or library-prep fields, so extraction kit currently remains an unmeasured residual. The first step is to get per-study wet-lab protocols from the original study records or publications, or to use a collection that records them. Eukaryotic fraction can then be modelled on habitat and kit jointly, to test the matrix-plus-kit driver cited from Sobolev et al. against the habitat-only reading [src: euk_in_prok_correlates].
- **Classifier dependence:** re-estimate plastid share on a subset of runs with a second read classifier and reference database. This would check whether the median 100% plastid share among detectable runs reflects the biology or the GOTTCHA2 reference database [src: euk_in_prok_correlates].
