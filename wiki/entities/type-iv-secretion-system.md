---
type: "Gene_Or_Pathway"
description: "Conjugative/secretion machinery (VirB4/6/8/9/10/11, VirD4, TraI/D, TrwB, TraG) used to identify transfer-capable genomes, including virB4/virD4 enrichment in cultured genomes."
sources: ["summaries/oak_ridge_cultivation_gap__REPORT.md", "summaries/t4ss_cazy_environmental_hgt__REPORT.md"]
aliases: ["Conjugation machinery virB4 and virD4", "T4SS", "virB4", "virD4"]
---
# Type IV secretion system

T4SS markers identify transfer-capable genomes: the environmental report finds them in 21.8% of 30,497 high-quality environmental MAGs (6,652 MAGs). [src: t4ss_cazy_environmental_hgt] The Oak Ridge report finds virB4 and virD4 enriched in cultured genomes (log2 +2.8 to +3.3), against its prediction of depletion. [src: oak_ridge_cultivation_gap]

## Key facts

- The environmental report defines T4SS/conjugative machinery with multiple markers: VirB4/6/8/9/10/11, VirD4, TraI/D, TrwB and TraG. [src: t4ss_cazy_environmental_hgt]
- Environmental T4SS+ genomes have 10× higher density of mobile genetic elements (MGE) (p<0.001). The report calls this consistent with chromosomal/integrative transfer. [src: t4ss_cazy_environmental_hgt]

## Enrichment in cultured genomes

The Oak Ridge cultivation-gap report predicted depletion of conjugation/MGE markers through plasmid loss during cultivation. [src: oak_ridge_cultivation_gap] In the cultured-isolate versus subsurface-MAG comparison, the conjugation/MGE category had 2 KEGG orthologs (KOs), a mean log2 ratio of +3.08, cultured enrichment, and 2/2 significant KOs. [src: oak_ridge_cultivation_gap]

The report hypothesizes that this reflects genomically integrated conjugation machinery being retained by isolates, while episomal MGEs are lost during cultivation. [src: oak_ridge_cultivation_gap] It suggests that the Goff et al. (2024) depletion prediction may apply only to episomal elements, which whole-genome sequencing of either cohort does not capture. [src: oak_ridge_cultivation_gap] See [[concepts/mobile-genetic-element-retention-in-cultured-isolates-versus-episomal-loss]] and [[summaries/oak_ridge_cultivation_gap__REPORT]].

## Link to carbohydrate-active enzyme transfer

The environmental report finds T4SS machinery significantly co-localised with GT2 glycosyltransferase cassettes in MAGs. It also reports phylogenetic incongruence in the GT2 gene tree as positive evidence for 32 cross-phylum horizontal gene transfer (HGT) events. [src: t4ss_cazy_environmental_hgt] In the neighbourhood analysis, list-format parsing found T4SS in 503 neighbourhood entries and GT2 in 495. The report reads this as confirming syntenic co-localisation at the contig level. [src: t4ss_cazy_environmental_hgt] See [[concepts/horizontal-transfer-of-carbohydrate-active-enzymes-via-conjugative-machinery]], [[entities/glycosyl-transferases]] and [[summaries/t4ss_cazy_environmental_hgt__REPORT]].
