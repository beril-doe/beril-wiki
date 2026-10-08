---
type: "Gene_Or_Pathway"
description: "The dissimilatory sulfate reduction pathway (Sat\u2013AprAB\u2013DsrAB), and how strongly its genomic markers are enriched in clay-confined deep-subsurface genomes, both within Bacillota_B and after a later marker correction."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
## Overview

Dissimilatory sulfate reduction (SR; aliases: the dsrAB-aprAB-sat module, the Sat–AprAB–DsrAB module, the dissimilatory sulfate reduction module) is detected in this corpus through genomic markers rather than measured activity. The marker set is the KEGG orthologs K11180, K11181, K00394, K00395 and K00958, and a later re-audit confirmed that these markers were correctly identified [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

## Enrichment in clay-confined deep-subsurface genomes

Of the 9 KBase Data Lakehouse genomes traceable to clay-confined deep-subsurface biosamples, 8 came from [[entities/mont-terri]] Opalinus boreholes and 1 from a bentonite formation. This cohort is strongly enriched for SR markers: 5/9 (56%) are SR-positive [src: clay_confined_subsurface].

Five of the nine deep-anchor genomes carry the dissimilatory sulfate reduction module (Sat, AprAB, DsrAB), and seven carry group 1 [[entities/nife-hydrogenase]] markers. The hits include the BRH-c8a lineage (Peptococcaceae c8a in Bagnoud's nomenclature) and desulfosporosinus [src: clay_confined_subsurface].

The comparison baseline is the Mitzscherling et al. (2023) rock-attached null distribution (SRB ~0.2%, IRB ~7% of community). Against it the SR enrichment is overwhelming: 5 positives were observed where 0.018 of 9 were expected, binomial p = 4.0×10⁻¹² [src: clay_confined_subsurface].

The central digest turns this into a proposed cultivation-bias diagnostic. For any cohort of cultured clay-isolated genomes, it computes the prevalence of SR markers (dsrAB-aprAB-sat) and iron-reduction markers (omcS / mtrC / mtrA), then compares them with the Mitzscherling rock-attached frequencies (SRB ~0.2%, IRB ~7%) using a binomial test. In the anchor_deep clay cohort, 5/9 genomes are SR-positive, binomial p=4×10⁻¹² against the rock-attached null [src: discoveries].

In the per-marker table, SR completeness was found in 5 of 9 deep genomes and 5 of 140 soil-baseline genomes. The table gives OR=33.8 and a Benjamini–Hochberg-adjusted p=2.5×10⁻⁴; BH is a false-discovery-rate correction for multiple tests [src: clay_confined_subsurface].

The separate H3 pairwise Fisher's exact tests for SR completeness gave three results [src: clay_confined_subsurface]:
- Deep versus shallow anchors: OR=∞, p=2×10⁻⁴ [src: clay_confined_subsurface].
- Deep anchors versus soil baseline: OR=33.8, p=5×10⁻⁵. The report gives this test separately from the BH-adjusted H2 test above [src: clay_confined_subsurface].
- Shallow anchors versus soil baseline: OR=0.0, p=0.59. This is not significant, so it is a null result [src: clay_confined_subsurface].

## Phylogenetic control within Bacillota_B

SR is the only trait that survives the phylogenetic control. Within [[entities/bacillota-b]], all 5/5 deep isolates carry SR, compared with 4/19 soil-baseline Bacillota_B isolates (OR=∞, p=0.003). The report's prose gives p_BH=0.04, but its within-phylum table gives the BH-adjusted value as 0.044. Both reported values are kept here [src: clay_confined_subsurface].

The digest **supports** this result, because the other subsurface traits are not enriched beyond their phylum congeners. Neither the [[entities/wood-ljungdahl-pathway]] (5/5 vs 15/19, p=0.54) nor NiFe-hydrogenase (5/5 vs 14/19, p=0.54) is enriched in deep-clay isolates. Only sulfate reduction (5/5 vs 4/19, p_BH=0.04) survives the control. The deep cohort in these comparisons has only five genomes, so this is a small-sample result [src: discoveries].

## Robustness after the iron-reduction marker correction

A later project re-audited the clay study's markers and found that the SR-side H3 finding **remains robust**. The deep cohort is 5/9 SR-positive against the Mitzscherling rock-attached null of 0.2% (binomial p=4×10⁻¹²), and the SR markers K11180, K11181, K00394, K00395 and K00958 were correctly identified. The clay project's "porewater bias" headline therefore still holds, through SR alone [src: bacillota_b_subsurface_accessory].

The clay project itself records that its SR-side H3 finding stands after the correction. Its deep-cohort result, 5/9 SR-positive against the rock-attached null at p=4×10⁻¹², is robust [src: clay_confined_subsurface].

Caveat: the iron-reduction markers were corrected using [[entities/multi-heme-cytochrome-detection]], and this correction does not fully settle the original H3 narrative. The SR side stays robust, but the iron-reduction side loses its narrative force. The "Mitzscherling rock-attached vs Bagnoud porewater" framing is therefore only half-supported: the SR side supports it, and the iron-reduction side no longer does after the marker correction [src: bacillota_b_subsurface_accessory].

## Related pages

- [[summaries/clay_confined_subsurface__REPORT]]
- [[summaries/bacillota_b_subsurface_accessory__REPORT]]
- [[summaries/discoveries]]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]]
- [[concepts/subsurface-bacillota-specialization]]
- [[concepts/functional-marker-validation]]
