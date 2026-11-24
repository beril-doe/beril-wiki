---
type: "Concept"
description: "Whether the anion delivered with a metal salt (e.g. chloride) drives measured metal fitness effects, tested by dose-response, chloride-free salts and within-metal salt comparisons; stops at metal-NaCl gene overlap interpretation."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_cross_resistance__REPORT.md"]
---
# Counter-ion confounding in metal fitness assays

This page asks whether the anion delivered with a metal salt (for example chloride) drives measured metal fitness effects. The counter_ion_effects report tests this by comparing metal–NaCl (sodium chloride) gene overlap against chloride load, using chloride-free salts and a within-metal salt comparison. The evidence argues against chloride confounding: overlap did not scale with chloride. The within-metal test is itself confounded, and the dose-response and chloride-specific controls were not done. [src: counter_ion_effects]

## Overlap does not scale with chloride

Across 19 organisms and 14 metals, 39.8% of metal-important genes were also NaCl-important. The report attributes this to shared cell-envelope, ion-homeostasis and DNA-repair stress biology, not chloride contamination. [src: discoveries, counter_ion_effects] Chloride metals as a group (mean 41.6%) were barely different from non-chloride metals (37.8%). [src: counter_ion_effects] Overlap was uncorrelated with effective chloride concentration across 86 organism × metal pairs. [src: counter_ion_effects] The critical test, whether overlap scales with chloride delivered by the metal salt, gave a "No". [src: counter_ion_effects] The report therefore rejects hypothesis H1b (dose-dependent Cl⁻) because ZnSO₄ with 0 Cl⁻ exceeds most chloride metals. [src: counter_ion_effects]

### Per-metal overlap

The table gives mean NaCl overlap, delivered anion, number of organisms and mean maximum Cl⁻ in mM for each metal. [src: counter_ion_effects]

| Metal | Anion | Mean overlap | Organisms | Mean max Cl⁻ (mM) |
|---|---|---|---|---|
| Manganese | chloride | 57.6% | 1 | 200 [src: counter_ion_effects] |
| Cadmium | chloride | 50.5% | 1 | not reported [src: counter_ion_effects] |
| Aluminum | chloride | 46.1% | 12 | 8 [src: counter_ion_effects] |
| Zinc | sulfate | 44.6% | 12 | 0 [src: counter_ion_effects] |
| Cobalt | chloride | 41.3% | 18 | 28 [src: counter_ion_effects] |
| Copper | chloride | 41.0% | 16 | 2 [src: counter_ion_effects] |
| Nickel | chloride | 39.3% | 17 | 2 [src: counter_ion_effects] |
| Uranium | acetate | 37.2% | 2 | 0 [src: counter_ion_effects] |
| Iron | media comp. | 33.3% | 1 | 0 [src: counter_ion_effects] |
| Chromium | media comp. | 29.2% | 2 | 0 [src: counter_ion_effects] |
| Selenium | media comp. | 26.8% | 1 | 0 [src: counter_ion_effects] |
| Mercury | chloride | 23.4% | 1 | 20 [src: counter_ion_effects] |
| Tungsten | media comp. | 10.8% | 1 | 0 [src: counter_ion_effects] |
| Molybdenum | media comp. | 9.2% | 1 | 0 [src: counter_ion_effects] |

## Chloride-free salts as natural controls

Zinc sulfate, with zero chloride, ranked 4th in NaCl overlap, above 10 of 14 metals. [src: counter_ion_effects] Its 44.6% overlap exceeded cobalt (41.3%, up to 500 mM Cl⁻), copper (41.0%) and nickel (39.3%). [src: counter_ion_effects] Zinc also had the highest NaCl profile correlation in *Desulfovibrio vulgaris* Hildenborough (DvH), r=0.715. [src: counter_ion_effects, discoveries] Uranium as acetate, also with zero chloride, ranked 8th. [src: counter_ion_effects] The report calls the zinc sulfate result definitive rejection of counter-ion confounding. [src: counter_ion_effects] See [[entities/zinc-sulfate]], zinc and [[entities/desulfovibrio-vulgaris-hildenborough]]. A later report states that DvH's metal–NaCl correlation hierarchy follows toxicity mechanism, not counter-ion identity. [src: metal_cross_resistance]

## Within-metal copper comparison

*Pseudomonas stutzeri* RCH2 (psRCH2) is the only organism tested with copper as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates). [src: counter_ion_effects] The cross-salt fitness correlation was r=0.439, lower than the within-replicate correlations (CuCl₂ r=0.720; CuSO₄ r=0.859). [src: counter_ion_effects] Chloride-free CuSO₄ correlated more with NaCl (r=0.450) than CuCl₂ did (r=0.212). [src: counter_ion_effects] The report reads this as arguing against chloride confounding and suggesting shared aerobic stress mechanisms. [src: counter_ion_effects] This comparison is severely confounded by aerobic versus anaerobic growth, because hundreds of genes differ between those conditions independent of copper. [src: counter_ion_effects] See [[entities/pseudomonas-stutzeri-rch2]] and [[entities/copper]].

## Interpretation and scope

The report partially supports H0: counter ions specifically are negligible, while shared stress biology is real but does not undermine the Metal Fitness Atlas conclusions. [src: counter_ion_effects] It cites Danilova et al. (2020) for 2.5-fold CuSO₄–CuCl₂ toxicity differences at 0.5 M, where osmotic effects dominate. [src: counter_ion_effects] It infers that counter-ion effects would be proportionally smaller at typical RB-TnSeq (random barcode transposon sequencing) concentrations of 0.05–2 mM. [src: counter_ion_effects] The wider shared-stress issue is in [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]] and [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].

## Proposed controls

The report proposes these tests.

- Metal–choline chloride overlap compared with metal–NaCl overlap, since several Fitness Browser (FB) organisms have choline chloride experiments. [src: counter_ion_effects]
- RB-TnSeq with matched metal chloride and sulfate concentrations in one organism under identical growth conditions. [src: counter_ion_effects]
- CuCl₂ 0.5 mM versus CuSO₄ 0.5 mM in MR-1 or DvH, because copper is the most-tested metal and both salts are commercially available. [src: counter_ion_effects]
- ZnCl₂ 0.2 mM versus ZnSO₄ 0.2 mM in MR-1, adding chloride to the already-tested sulfate form. [src: counter_ion_effects]
- CoCl₂ 0.1 mM versus CoSO₄ 0.1 mM in DvH, because cobalt has the highest Cl⁻ load in the current data. [src: counter_ion_effects]
- NaCl dose-response at 0.1, 1, 10, 100 and 500 mM in DvH, to dose-match NaCl stress to effective Cl⁻ from metal salts. [src: counter_ion_effects]

## Tensions

- The report calls the rejection definitive, based on zinc sulfate. [src: counter_ion_effects] It also says the only within-metal counter-ion comparison is severely confounded [src: counter_ion_effects], and that it only partially supports H0. [src: counter_ion_effects]
- NaCl is not a pure chloride control. It delivers Na⁺ and Cl⁻, so its profile includes sodium toxicity and osmotic stress, and the report suggests KCl or choline chloride as more specific controls. [src: counter_ion_effects]
- Hypothesis H1d, that chloride and oxyanion functional profiles differ, was dropped and not tested. [src: counter_ion_effects]

## Open Directions

- Compare metal–choline chloride overlap with metal–NaCl overlap in Fitness Browser organisms that have choline chloride experiments. Choline chloride supplies Cl⁻ without Na⁺ or osmotic effects, so this would separate chloride from osmotic confounding.
- Run matched metal chloride and sulfate RB-TnSeq in a single organism under identical growth conditions. This removes the aerobic/anaerobic confound of the psRCH2 comparison. Zinc and cobalt pairs in DvH or MR-1 are natural first tests.
- Run NaCl dose-response in DvH to dose-match NaCl stress to the chloride delivered by metal salts. This would test directly what the zero-chloride controls only imply.
- Test the dropped H1d by comparing functional profiles of chloride and oxyanion metals.
