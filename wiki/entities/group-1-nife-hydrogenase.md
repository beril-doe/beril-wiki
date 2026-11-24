---
type: "Gene_Or_Pathway"
description: "Hydrogenase marker module in the anaerobic toolkit, carried by seven deep clay genomes."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
aliases: ["NiFe hydrogenase", "group 1 [NiFe]-hydrogenase"]
---
# Group 1 [NiFe]-hydrogenase

Deep clay isolates carry NiFe-hydrogenase markers far more often than soil baseline genomes. [src: clay_confined_subsurface] The signal disappears within one phylum, so the evidence points to lineage rather than habitat. [src: clay_confined_subsurface] A separate cultivation-gap comparison found the opposite of its prediction. [src: oak_ridge_cultivation_gap]

## Key facts

- Seven of 9 anchor_deep genomes carry complete NiFe, versus 35 of 140 soil_baseline genomes, with Fisher OR=10.5 and p_BH=0.004. [src: clay_confined_subsurface]
- The same odds ratio and adjusted p-value come from the per-marker Fisher test of deep clay isolates against the soil baseline, with Benjamini-Hochberg false discovery rate (BH-FDR) adjustment. [src: clay_confined_subsurface] See [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]].

## Lineage confounding

Within [[entities/bacillota-b]], NiFe carriage does not differ between deep clay and baseline isolates: 5/5 versus 14/19, p=0.54. [src: clay_confined_subsurface] The table gives OR=∞ and a BH-adjusted p of 1.0 for the same comparison. [src: clay_confined_subsurface] The report reads this as the marker tracking the Bacillota_B lineage, not deep-clay habitat per se. [src: clay_confined_subsurface] The discoveries digest repeats the result: NiFe-hydrogenase is not enriched in deep-clay isolates beyond their phylum congeners. [src: discoveries] Only sulfate reduction (SR) survives the phylogenetic control there. [src: discoveries] See [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]], [[summaries/clay_confined_subsurface__REPORT]] and [[summaries/discoveries]].

## Cultivation gap

In the ENIGMA cultured-isolate versus subsurface-MAG comparison (MAG = metagenome assembled genomes), NiFe-hydrogenase was predicted to be depleted in cultured genomes. Instead, the KEGG orthologs (KOs) K06281 and K06282 occurred in ~7.5% of cultured genomes and 0% of MAGs (log2 = +6.2). [src: oak_ridge_cultivation_gap] The category had 2 KOs, a mean log2 ratio of +6.26, cultured enrichment, and 2/2 significant KOs. [src: oak_ridge_cultivation_gap] The report says this contradicts the prediction of Beaver & Neufeld (2024) that group 1 [NiFe]-hydrogenases concentrate in uncultivated lineages. [src: oak_ridge_cultivation_gap] It offers two possible explanations: the cultured collection captures hydrogenotrophs better than expected, or the KO assignments conflate hydrogenase groups. [src: oak_ridge_cultivation_gap] See [[summaries/oak_ridge_cultivation_gap__REPORT]].
