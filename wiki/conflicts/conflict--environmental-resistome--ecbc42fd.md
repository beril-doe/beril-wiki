<!-- tension-hash: ecbc42fd1f199bb8 -->
# Does a broad antimicrobial-resistance (AMR) catalog measure antibiotic resistance or a wider stress-resistance landscape?

Two projects in this corpus annotate bacterial genomes with the same reference catalog, AMRFinderPlus (a curated collection of antimicrobial-resistance gene models), yet describe the resulting gene set in incompatible vocabularies. One frames the catalog output as a broad stress-resistance landscape that happens to include classical antibiotic-resistance genes; the other reports and interprets it under narrow antibiotic-resistance language. The disagreement matters because every downstream claim about "resistome" abundance, environmental structuring, and core/accessory composition inherits whichever reading is correct. A second, smaller disagreement rides along: the two projects report different unclassified fractions over different denominators, and these must not be silently reconciled. [src: amr_pangenome_atlas, amr_environmental_resistome]

## Evidence Sides

**Broad catalog: the detected gene set exceeds antibiotic resistance.** The AMRFinderPlus catalog detects metal and stress systems alongside classical antibiotic-resistance determinants, so a catalog-defined AMR count is partly a measure of general stress resistance rather than a narrow antibiotic-resistance count. [src: amr_pangenome_atlas] On this side, the narrow interpretation is weakened by mercury- and arsenic-resistance families among the detected genes and by the 22.2% Other/Unclassified category. [src: amr_pangenome_atlas, amr_environmental_resistome]

**Narrow interpretation: the same gene set read as antibiotic resistance.** Narrow antibiotic-resistance language persists alongside the broad catalog, and the unclassified fractions carried under the two vocabularies do not match. The environmental-resistome analysis reports 15,550 unassigned clusters (18.7%), not 18,448 (22.2%). [src: amr_pangenome_atlas, amr_environmental_resistome] The two numbers are not alternative estimates of one quantity: the denominators and the classification vocabularies differ, and neither figure may be substituted for, averaged with, or corrected against the other. [src: amr_pangenome_atlas, amr_environmental_resistome]

## Possible Reconciliations

*Hypothesis 1 — vocabulary, not measurement.* The sides may agree on which genes are detected and disagree only on what to call them; if so, the tension is resolved by relabelling catalog-defined AMR as stress resistance without altering any count. [src: amr_pangenome_atlas]

*Hypothesis 2 — the unclassified categories are different objects.* The 22.2% Other/Unclassified and the 15,550 (18.7%) unassigned clusters may be produced by different classification procedures over different cluster sets, in which case both figures stand and neither is an error. [src: amr_pangenome_atlas, amr_environmental_resistome]

*Hypothesis 3 — partition, not reinterpretation.* The metal- and stress-resistance families may form a separable subset, so that a narrow antibiotic-resistance resistome and a broad stress resistome can both be reported from one catalog run. This remains a hypothesis until the partition is actually drawn. [src: amr_pangenome_atlas]

## Resolving Work

- Take the detected gene set and partition it by determinant class (antibiotic vs. metal vs. general stress), then recompute every environmental-structuring result on the antibiotic-only subset: do the conclusions survive the narrow reading? [src: amr_environmental_resistome]
- Reconcile the two cluster inventories explicitly — align the denominators behind 22.2% and 18.7% (15,550) and report both side by side rather than as one number. [src: amr_pangenome_atlas, amr_environmental_resistome]
- Quantify the mercury- and arsenic-resistance families as a share of the detected set, to test whether they are marginal or load-bearing for the broad reading. [src: amr_pangenome_atlas]
- Re-annotate the Other/Unclassified category against an ontology-based mechanism scheme and ask how much of it is antibiotic-directed at all. [src: amr_pangenome_atlas]
- Report catalog-defined counts under a stress-resistance label throughout and check which published claims change wording versus change conclusion. [src: amr_pangenome_atlas, amr_environmental_resistome]

Source concept: [[concepts/environmental-resistome]]
