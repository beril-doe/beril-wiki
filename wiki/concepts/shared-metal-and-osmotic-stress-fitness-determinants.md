---
type: "Concept"
description: "How much of the gene-level fitness response to metals overlaps with the response to NaCl (osmotic/ionic stress), how it varies by metal and organism, and what mechanisms explain it; stops short of conservation consequences."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/pitfalls.md"]
---
# Shared metal and osmotic stress fitness determinants

Metal stress and NaCl (sodium chloride) stress share a large part of their gene-level fitness determinants. In the counter_ion_effects analysis, 4,304 of 10,821 metal-important gene records (39.8%) were also important under NaCl, across 19 organisms and 14 metals. [src: counter_ion_effects] The report treats this as real shared biology, not a counter-ion artifact. [src: counter_ion_effects] The overlap is a direct measurement, but the mechanism claims are mostly hypotheses. A later analysis (metal_specificity) found 14.7% overlap, a 2.7x discrepancy [src: metal_specificity], and that report attributes most of the gap to threshold stringency. [src: metal_specificity] The pitfalls digest adds that the NaCl-importance definition in counter_ion_effects is biased by experiment count, though excluding the main outlier organism changes the overlap only modestly. [src: pitfalls]

## How large is the overlap?

The overlap was seen for every metal tested, from 9.2% for molybdenum to 57.6% for manganese. [src: counter_ion_effects] The analysis used 71 NaCl experiments across 25 organisms and found 4,648 NaCl-important genes. Only 19 of the 25 organisms entered the overlap analysis. [src: counter_ion_effects] The remaining 6,517 records (60.2%) were metal-specific, meaning important for metals but not NaCl. [src: counter_ion_effects] The report's hypothesis H1a (more than 20% overlap) was supported. [src: counter_ion_effects] The report presents this as the first systematic quantification of metal–salt overlap in genome-wide fitness data. [src: counter_ion_effects]

Organisms differ. *Synechococcus elongatus* was an outlier at 88.6% shared-stress (565/638 genes). It had 12 NaCl dose-response experiments spanning 0.5–250 mM, against 1–6 for other organisms. [src: counter_ion_effects, discoveries] The pitfalls digest reports that it flags 32.6% of genes as NaCl-important, 3× higher than the next organism. [src: pitfalls] The n_sick >= 1 threshold (at least one NaCl experiment with fit < -1) is easier to meet with 12 experiments [src: counter_ion_effects, discoveries], and the pitfalls digest calls it biased by the number of NaCl experiments per organism. [src: pitfalls] Unequal experiment counts inflate cross-condition overlap statistics, with SynE showing 88.6% shared-stress. [src: pitfalls] Excluding it lowered the overlap from 39.8% to 36.7% (3,739/10,183), so the report concludes the finding is not driven by this outlier. [src: counter_ion_effects, discoveries, pitfalls] The pitfalls digest calls this drop modest but worth documenting. [src: pitfalls] The next-highest organisms were Korea 58.6%, Phaeo 56.4% and Pedo557 53.0%, each with typical NaCl experiment counts. [src: counter_ion_effects] See [[entities/synechococcus-elongatus]].

## Variation among metals in *Desulfovibrio vulgaris* Hildenborough

In DvH (13 metals, 6 NaCl experiments) the whole-genome fitness correlation with NaCl falls from zinc to iron. [src: counter_ion_effects] See [[entities/desulfovibrio-vulgaris-hildenborough]].

| Metal | r with NaCl |
|---|---|
| Zinc | 0.715 [src: counter_ion_effects] |
| Manganese | 0.545 [src: counter_ion_effects] |
| Copper | 0.532 [src: counter_ion_effects] |
| Cobalt | 0.498 [src: counter_ion_effects] |
| Mercury | 0.478 [src: counter_ion_effects] |
| Nickel | 0.446 [src: counter_ion_effects] |
| Aluminum | 0.420 [src: counter_ion_effects] |
| Molybdenum | 0.396 [src: counter_ion_effects] |
| Uranium | 0.350 [src: counter_ion_effects] |
| Selenium | 0.342 [src: counter_ion_effects] |
| Chromium | 0.318 [src: counter_ion_effects] |
| Tungsten | 0.298 [src: counter_ion_effects] |
| Iron | 0.086 [src: counter_ion_effects] |

The central-digest report gives the same order with values rounded to two decimals. [src: discoveries] The report reads the order as a gradient from general to pathway-specific toxicity. [src: counter_ion_effects]

## Proposed mechanisms

The report explains the gradient by toxicity mechanism. It names Zn, Mn, Cu, Co, Hg and Ni as a high-overlap group (r > 0.4) that displaces cofactors broadly and disrupts many systems, giving profiles like general ionic stress. [src: counter_ion_effects] The table shows aluminum (r=0.420) [src: counter_ion_effects] also above 0.4, yet the report's named group omits it, so the 0.4 cutoff does not exactly match the named groups. The report also names Mo, U, Se, Cr, W and Fe as a low-overlap group (r < 0.4) that hits specific pathways such as molybdopterin, iron-sulfur clusters and selenoprotein biosynthesis. [src: counter_ion_effects, discoveries] Iron's low r (0.086) is attributed to iron limitation affecting specific Fe-dependent enzymes rather than general damage. [src: counter_ion_effects] The report says this hierarchy aligns with Nies (2003), which separates broad damage by Fenton chemistry (Cu, Fe) or cofactor displacement (Zn, Co, Ni) from specific targets (Mo, W, Se). [src: counter_ion_effects] The metal_cross_resistance report says DvH's hierarchy follows toxicity mechanism, and that the same mechanistic grouping emerges from metal–metal correlations across 28 organisms. [src: metal_cross_resistance]

For the shared genes themselves, the report hypothesizes three functions. These are cell envelope integrity, sensitive to divalent cation imbalance and osmolarity changes [src: counter_ion_effects]; DNA (deoxyribonucleic acid) repair, where metal-induced oxidative damage overlaps with NaCl stress [src: counter_ion_effects]; and ion homeostasis, where metal influx competes with Na⁺/K⁺/Cl⁻ transporters. [src: counter_ion_effects] It also sees the ~40% overlap as consistent with the general stress response paradigm, in which RpoS-dependent genes respond to heavy metals, osmolarity and oxidative damage. [src: counter_ion_effects] The discoveries digest repeats the cell-envelope, ion-homeostasis and DNA-repair attribution. [src: discoveries]

### DvH gene-level support

In DvH, 495 unique metal-important genes split into 73 shared-stress (14.7%) and 422 metal-specific (85.3%). [src: counter_ion_effects] Shared-stress genes were important across a mean 4.1 metals per gene versus 2.5 for metal-specific genes, consistent with broad cellular vulnerability. [src: counter_ion_effects] Metal-specific genes were more often annotated in SEED (90.5% vs 78.1%). The report suggests they include Ni/Fe-hydrogenase, nitrogenase regulators and metal transporters, while shared-stress genes include more uncharacterized general-stress proteins. [src: counter_ion_effects] This is descriptive only, with no hypergeometric enrichment test. [src: counter_ion_effects] The report frames the result as a gene classification into shared-stress (40%) and metal-specific (60%) classes. [src: counter_ion_effects] See also [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]] and [[concepts/counter-ion-confounding-in-metal-fitness-assays]].

## Tensions and limits

- The 39.8% overlap depends on the NaCl-importance threshold (fit < -1 or n_sick ≥ 1). Stricter thresholds would lower it and more permissive ones raise it. [src: counter_ion_effects] The discoveries digest advises accounting for experiment count when setting thresholds. [src: discoveries] The pitfalls digest recommends n_sick >= 2 or mean_fit < threshold instead of n_sick >= 1, or sensitivity analyses excluding outlier organisms. [src: pitfalls]
- The metal_specificity analysis found 14.7% of metal-important genes sick under osmotic stress, a 2.7x discrepancy from the 39.8% it cites for counter_ion_effects. [src: metal_specificity] That report says methodological differences (threshold stringency) explain most of the gap, and that matching the counter_ion_effects methodology would strengthen validation. [src: metal_specificity] It specifies the difference as a stricter threshold (fit < -1 AND |t| > 4) versus fit < -1 only, and notes the organism sets also differ partially. [src: metal_specificity] It reads the directional agreement, substantial overlap between metal and osmotic stress genes, as supporting the validity of both analyses. [src: metal_specificity] It proposes replicating that method (fit < -1 without |t| > 4). [src: metal_specificity]
- Mn, Cd, Se, Hg, Fe, Mo and W were tested in only DvH, so their overlap statistics have no cross-organism replication. [src: counter_ion_effects]
- The metal_cross_resistance report notes it lacks non-metal stress controls, which counter_ion_effects only partly addresses. [src: metal_cross_resistance]
- After removing the ~40% NaCl-overlapping genes, core-genome enrichment persisted for 12 of 14 metals. [src: discoveries] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].

## Open Directions

- Re-run the overlap with both studies' thresholds, and with thresholds scaled to NaCl experiment count (for example n_sick >= 2 or mean_fit), to see how far the 39.8% versus 14.7% gap is a threshold effect.
- Profile Mn, Cd, Se, Hg, Fe, Mo and W in more organisms to test whether the DvH hierarchy holds beyond one organism.
- Run hypergeometric enrichment tests on shared-stress versus metal-specific genes to test the proposed envelope, DNA-repair and ion-homeostasis functions.
- Add NaCl dose-response experiments for more organisms, as for *Synechococcus elongatus*, to separate dose effects from metal effects.
