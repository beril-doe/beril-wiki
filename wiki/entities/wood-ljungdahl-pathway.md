---
type: "Gene_Or_Pathway"
description: "Reductive acetyl-CoA pathway, an anaerobic toolkit module tested in deep clay isolates."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
aliases: ["WL", "acetyl-CoA pathway", "reductive acetyl-CoA pathway"]
---
# Wood–Ljungdahl pathway

In the ENIGMA cultured collection it is underrepresented relative to subsurface MAGs (metagenome assembled genomes). [src: oak_ridge_cultivation_gap]

## Key facts

- WL is a toolkit module tested in deep clay isolates. Beaver & Neufeld (2024) predicted that Bacillota dominate deeper isolated fluids partly because they favor this pathway and form spores. [src: clay_confined_subsurface]
- It is described as a hallmark of autotrophic lifestyles under energy limitation. [src: oak_ridge_cultivation_gap] The CO dehydrogenase components K00194, K00197 and K00198 are linked to autotrophic carbon fixation under anaerobic, energy-limited conditions. [src: oak_ridge_cultivation_gap]

## Deep clay isolates versus soil baseline

WL markers are strongly enriched in deep clay isolates against soil, but the within-phylum control shows the signal tracks lineage. [src: clay_confined_subsurface] This is a result from one clay cohort.

- WL_complete occurred in 5 of 9 anchor_deep genomes versus 15 of 140 soil_baseline genomes. Fisher OR (odds ratio) was 10.4 and p_BH was 0.004 after BH-FDR (Benjamini-Hochberg false discovery rate) adjustment. [src: clay_confined_subsurface]
- The Bacillota_B soil baseline already carries WL and [NiFe]-hydrogenase at high background rates. Its toolkit mean is 1.65. [src: clay_confined_subsurface] See [[entities/bacillota-b]].
- Within Bacillota_B, WL_complete occurred in 5 of 5 deep genomes versus 15 of 19 baseline genomes. This is not significant (p=0.54, BH-adjusted p=1.0). [src: clay_confined_subsurface]
- The report concludes that WL tracks the Bacillota_B lineage, not deep-clay habitat per se. [src: clay_confined_subsurface] The central digest repeats that WL is not enriched in deep-clay isolates beyond phylum congeners. [src: discoveries]

The lineage confound is discussed in [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]]. [src: clay_confined_subsurface, discoveries] The test is described in [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]. [src: clay_confined_subsurface] See also [[summaries/clay_confined_subsurface__REPORT]] [src: clay_confined_subsurface] and [[summaries/discoveries]]. [src: discoveries]

## Cultivation gap in ENIGMA

Cultured genomes carry less WL than subsurface MAGs. [src: oak_ridge_cultivation_gap] This concerns what culturing recovers, not habitat enrichment among isolates. See [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]] [src: oak_ridge_cultivation_gap] and [[summaries/oak_ridge_cultivation_gap__REPORT]]. [src: oak_ridge_cultivation_gap]

- 4 of 5 WL marker KOs (KEGG orthologs) were significantly depleted in cultured genomes. The mean log2 ratio was -1.58, and this matched the predicted depletion. [src: oak_ridge_cultivation_gap]
- The CO dehydrogenase/acetyl-CoA synthase complex (K00194, K00197, K00198) showed 3.5-3.8 log2 depletion. The report calls this consistent with a hallmark of uncultivated deep-subsurface lineages. [src: oak_ridge_cultivation_gap]
- K15023 (methyltransferase) was in 0.6% of cultured genomes and no MAGs. The report suggests it is likely a mis-annotated or divergent variant. [src: oak_ridge_cultivation_gap]
- The report warns that WL carbon fixation is systematically underrepresented in ENIGMA's cultured collection for subsurface metabolic characterization. [src: oak_ridge_cultivation_gap]

## Literature the report cites

- Takami et al. (2012) showed that a deeply branching thermophilic bacterium with the acetyl-CoA pathway dominated a subsurface ecosystem. They also showed that the pathway is among the most ancient bacterial metabolic strategies. [src: oak_ridge_cultivation_gap]
- Jungbluth et al. (2017) found deep-subsurface Firmicutes with WL, hydrogenotrophy and dissimilatory sulfate reduction in marine and terrestrial systems. The report takes this as confirming these as core deep-subsurface metabolisms. [src: oak_ridge_cultivation_gap]
- Merino et al. (2020) found novel Actinobacteria with WL in a serpentinizing system. This was the first report for Actinobacteriota and suggests the pathway is widespread among uncultivated subsurface lineages. [src: oak_ridge_cultivation_gap]
