---
type: "Concept"
description: "Whether cultivation depletes mobile genetic elements and conjugation machinery, and whether genomic sequencing of isolates captures episomal elements; stops at conjugation and metal-resistance markers."
sources: ["summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Mobile genetic element retention in cultured isolates versus episomal loss

This page asks whether cultivation depletes mobile genetic elements (MGE) and conjugation machinery in isolate genomes, and whether sequencing isolates captures episomal elements. The evidence comes from one report, the Oak Ridge cultivation-gap comparison of cultured isolates with subsurface metagenome assembled genomes (MAG). It found no depletion of genomically encoded conjugation markers. Its explanation, that episomal loss is hidden from genome sequencing, is a hypothesis. [src: oak_ridge_cultivation_gap]

## Conjugation and MGE markers

The prediction of depletion through plasmid loss during cultivation failed for the two conjugation markers tested. virB4 and virD4 were instead enriched in cultured genomes (log2 +2.8 to +3.3). [src: oak_ridge_cultivation_gap] The summary table gives 2 KOs (KEGG orthologs), a mean log2 ratio of +3.08, cultured enrichment and 2/2 significant KOs, marked "No (predicted depleted)". [src: oak_ridge_cultivation_gap] See [[entities/type-iv-secretion-system]] and [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]].

## Metal-resistance markers

All 4 metal-resistance marker KOs were enriched in cultured genomes (log2 +1.5 to +5.9). [src: oak_ridge_cultivation_gap] The marker arsC was present in 89% of cultured genomes versus 14% of MAGs. [src: oak_ridge_cultivation_gap] The table lists mean log2 +3.33 and 4/4 significant KOs, and calls this a partial match to predictions, through genomic enrichment. [src: oak_ridge_cultivation_gap] See [[entities/arsenic-resistance-ars-genes]]. The report proposes a separate accessory-genome comparison of plasmid-borne and prophage-borne content to test whether MGE-borne metal resistance is specifically depleted in isolates. [src: oak_ridge_cultivation_gap]

## Interpretation: episomal loss

The report says the result contradicts the prediction drawn from Goff et al. (2024). That study found MGEs from the contaminated Oak Ridge subsurface enriched in heavy-metal-resistance gene clusters, which suggests MGE-borne adaptation. [src: oak_ridge_cultivation_gap] The report's explanation is that the result likely reflects genomically integrated conjugation machinery, retained by isolates, versus episomal MGEs, lost during cultivation. [src: oak_ridge_cultivation_gap] It calls this consistent with Kothari et al. (2019), who observed large circular plasmids in ORFRC (Oak Ridge Field Research Center) plasmidomes. [src: oak_ridge_cultivation_gap] The report's caveat is that the Goff et al. prediction may apply specifically to episomal elements that whole-genome sequencing of either cohort does not capture. [src: oak_ridge_cultivation_gap]

## Open Directions

- Compare plasmid-borne and prophage-borne accessory content between cohorts, using the pangenome's bakta annotations. This tests whether MGE-borne metal resistance is specifically depleted in isolates. [src: oak_ridge_cultivation_gap]
- Classify each arsC and virB4/virD4 hit as chromosomal or plasmid-contig. This would show whether the enrichment sits in integrated elements, as the hypothesis requires.
