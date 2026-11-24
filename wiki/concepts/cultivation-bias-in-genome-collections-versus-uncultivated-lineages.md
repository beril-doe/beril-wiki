---
type: "Concept"
description: "Which metabolic functions isolate genome collections over- or under-represent versus metagenome-assembled genomes, including absent Patescibacteria; stops at genome-size and taxonomy confounds."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Cultivation bias in genome collections versus uncultivated lineages

Isolate genome collections and metagenome-assembled genomes (MAGs) from the same subsurface system differ in function content. The main evidence is one Oak Ridge comparison of ENIGMA cultured isolates with subsurface MAGs, plus a caveat from a clay-confined subsurface report. Cultured genomes carry more of most functions. The report says most of that enrichment is not specifically selected for by cultivation, because the functions sit in larger genomes that happen to be cultivable. It treats the 813 MAG-enriched KOs as the biologically informative cultivation gaps. [src: oak_ridge_cultivation_gap]

## Scale of the gap

Of 10,845 KEGG orthologs (KOs) tested, 8,482 (78.2%) differed significantly in prevalence between 3,102 cultured ENIGMA Genome Depot isolates and 2,279 subsurface/groundwater MAGs (Fisher's exact, Benjamini-Hochberg false discovery rate (BH-FDR) < 0.05). [src: oak_ridge_cultivation_gap] Of these, 7,669 were enriched in cultured genomes and 813 were depleted. [src: oak_ridge_cultivation_gap] A further 6,387 KOs occurred only in the cultured collection and 554 only in MAGs. [src: oak_ridge_cultivation_gap] The median log2 ratio for shared KOs was +2.22. [src: oak_ridge_cultivation_gap]

The report says the cultured collection genuinely does not sample CPR (candidate phyla radiation) organisms. It concludes that most of the 7,669 "enriched" KOs are not specifically selected for by cultivation. They are simply present in larger genomes that happen to be cultivable. [src: oak_ridge_cultivation_gap] The 813 MAG-enriched KOs are the informative cultivation gaps, because subsurface organisms carry them despite smaller genomes. [src: oak_ridge_cultivation_gap]

## Functions under-represented in isolates

Across 10 marker categories (36 KOs), the report finds partial support for depletion of deep-subsurface functions in cultures (H1). It finds strong support for enrichment of cultivation-favorable functions (H2). [src: oak_ridge_cultivation_gap]

- **Wood-Ljungdahl pathway:** 4 of 5 marker KOs were significantly depleted in cultured genomes (mean log2 ratio -1.58). [src: oak_ridge_cultivation_gap] The CO dehydrogenase/acetyl-CoA synthase KOs K00194, K00197 and K00198 were 3.5-3.8 log2 depleted. The report calls this consistent with a hallmark of uncultivated deep-subsurface lineages. [src: oak_ridge_cultivation_gap] See [[entities/wood-ljungdahl-pathway]].
- **Sulfate reduction:** The result is heterogeneous. The dsrAB KOs K11180 and K11181 were 3.0-3.1 log2 depleted in cultures. [src: oak_ridge_cultivation_gap] aprAB (K00394) showed no significant difference. [src: oak_ridge_cultivation_gap] sat/PAPSS (K00395, K00958) were enriched in cultures. [src: oak_ridge_cultivation_gap] The report suggests the two subsystems have different taxonomic distributions. [src: oak_ridge_cultivation_gap] The category mean was +0.79 with 4/5 KOs significant. [src: oak_ridge_cultivation_gap] See [[entities/dissimilatory-sulfate-reduction-pathway]].
- **Methanogenesis:** mcrABG (K00399-K00402) occurred in only 3 cultured genomes (0.1%) and in no MAGs. That is too rare for a meaningful signal, and 0/3 KOs were significant. [src: oak_ridge_cultivation_gap]

The report advises that users of the ENIGMA cultured collection should expect Wood-Ljungdahl carbon fixation and dissimilatory sulfite reduction to be systematically underrepresented. [src: oak_ridge_cultivation_gap]

## Functions over-represented in isolates

- **Aerobic respiration:** coxABC had mean log2 +7.29 and 91% prevalence in cultured genomes. [src: oak_ridge_cultivation_gap] coxA and coxC were completely absent from the MAGs. [src: oak_ridge_cultivation_gap]
- **Motility/chemotaxis:** fliC, cheA and cheW had mean log2 +7.23 and 80% cultured prevalence. [src: oak_ridge_cultivation_gap] cheA and cheW were absent from all MAGs. [src: oak_ridge_cultivation_gap]
- **Denitrification:** All 6 marker KOs were enriched in cultures (log2 +1.5 to +3.0), with narGH strongest. [src: oak_ridge_cultivation_gap]
- **Metal resistance:** All 4 KOs were enriched in cultures (log2 +1.5 to +5.9). [src: oak_ridge_cultivation_gap] arsC was present in 89% of cultured genomes versus 14% of MAGs. [src: oak_ridge_cultivation_gap] See [[entities/arsenic-resistance-ars-genes]].
- **N-fixation:** The 3 KOs were mixed (mean log2 +1.56), with 2/3 significant. [src: oak_ridge_cultivation_gap] See bacterial nitrogen fixation nif genes.

## Absent Patescibacteria and the confounds

Patescibacteria (CPR) make up approximately 40% of the 2,279 MAGs. [src: oak_ridge_cultivation_gap] The report describes them as having ultra-small genomes (typically 0.5-1.5 Mbp), reduced metabolic capacity and probable obligate symbiotic lifestyles. [src: oak_ridge_cultivation_gap] It treats their near-complete absence from cultures as expected, because host dependence and metabolic complementation resist standard cultivation. [src: oak_ridge_cultivation_gap] It calls the roughly 40% versus near-zero contrast the single largest taxonomic bias in cultivation-based subsurface genomics. [src: oak_ridge_cultivation_gap] See [[entities/patescibacteria]].

This dominance is also a genome-size confound. The report attributes the median MAG genome size of 1.5 Mbp to CPR dominance. [src: oak_ridge_cultivation_gap] It predicts that excluding Patescibacteria would leave MAGs with substantially more KOs per genome and narrow the apparent gap. [src: oak_ridge_cultivation_gap] This is a prediction, not a tested result. See [[concepts/genome-size-and-taxonomic-composition-confounding-of-cultured-versus-mag-functional-comparisons]].

Other literature cited in the report fits this picture:
- Cell-size fractionation of deep groundwater enriches Patescibacteria, Nanobdellota and Omnitrophota, which have very small genomes and resist cultivation (Westmeijer et al. 2026). [src: oak_ridge_cultivation_gap]
- Patescibacteria assemblages along a subterranean estuary show high taxonomic novelty (Ruiz-Gonzalez et al. 2025). [src: oak_ridge_cultivation_gap]
- Horizontal gene transfer (HGT) shapes Patescibacteria metabolism, with up to 13% of genome content attributed to HGT (Gios et al. 2025). [src: oak_ridge_cultivation_gap]
- Parcubacteria show genome streamlining from soil to groundwater (Chaudhari et al. 2024). [src: oak_ridge_cultivation_gap]

## The MAG-only tail

The 554 MAG-only KOs are interpreted as the most extreme cultivation gap, since cultured-isolate genomics at this site would not detect them. [src: oak_ridge_cultivation_gap] The report hypothesizes they likely include Patescibacteria-specific functions. [src: oak_ridge_cultivation_gap] It also identifies a long tail of MAG-enriched KOs of unknown function that may represent novel subsurface metabolisms. [src: oak_ridge_cultivation_gap] The report proposes cross-referencing the MAG-only functions with the HGT analysis of Gios et al. (2025) to investigate horizontal acquisition. [src: oak_ridge_cultivation_gap] The report presents the work as the first quantitative per-function cultivation-coverage analysis comparing matched cultured and MAG cohorts for a well-characterized subsurface system. [src: oak_ridge_cultivation_gap]

## Related evidence from clay

A separate clay-confined subsurface report has the same limit. CPR/DPANN episymbionts and rock-attached Geobacter/Geothrix lineages are essentially absent from its cultured cohort. [src: clay_confined_subsurface] It says MAG-augmented work is needed to test whether the genuine clay-confined community matches literature predictions. [src: clay_confined_subsurface] It proposes adding deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite and Oak Ridge to test whether self-sufficiency emerges with rock-attached and uncultivated lineages. [src: clay_confined_subsurface] See [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]].

## Open Directions

- Repeat the cultured-versus-MAG KO test with Patescibacteria removed from the MAG cohort. This would test the prediction that the gap narrows, and it would show which of the 813 MAG-enriched KOs survive.
- Cross-reference the 554 MAG-only KOs with the HGT analysis of Gios et al. (2025) to see which were horizontally acquired.
- Annotate the unknown-function MAG-enriched KOs and test for Patescibacteria-specific novel metabolisms.
- Ingest deep-subsurface MAGs from the clay report's sites into the pangenome and re-run its H1/H2/H3 framework. This would test whether the self-sufficiency signal appears once rock-attached lineages are present.
- Compare KO prevalence within matched genome-size bins, to separate genome-size effects from selection by cultivation.
