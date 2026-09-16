---
type: "Gene_Or_Pathway"
description: "The Wood\u2013Ljungdahl pathway as a genomic marker in this corpus, whose apparent enrichment in deep clay-confined subsurface isolates turns out to track the Bacillota_B lineage rather than the habitat."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
In this corpus the Wood–Ljungdahl (WL) pathway is a genomic marker. It was tested, alongside [NiFe]-hydrogenase and sulfate reduction, for enrichment in isolates from deep clay-confined subsurface settings [src: clay_confined_subsurface, discoveries].

Aliases: WL; `WL_complete`, the completeness flag used in the clay-subsurface comparison tables [src: clay_confined_subsurface].

## Cohort-level enrichment

At cohort level, a complete Wood–Ljungdahl pathway was scored in 5 of 9 deep-cohort genomes versus 15 of 140 soil-baseline genomes. The odds ratio was 10.4, with a Benjamini–Hochberg-adjusted p (p_BH, a false-discovery-rate-corrected p-value) of 0.004 [src: clay_confined_subsurface]. This enrichment did not survive within-phylum control, described below, so it should not be read as evidence of a habitat-specific signal [src: clay_confined_subsurface].

## Phylogenetic confound (Bacillota_B)

The [[entities/bacillota-b]] phylum includes desulfosporosinus, BRH-c4a and BRH-c8a, the lineages that dominate the deep anchor cohort and the cultured clay isolates. It carries Wood–Ljungdahl and group 1 [[entities/nife-hydrogenase]] at high background rates even in soil samples. Its soil-baseline mean toolkit score, a per-genome count of the marker toolkit as defined in the report, was 1.65 [src: clay_confined_subsurface, discoveries]. This caveat **refines** the cohort-level result above: a lineage effect confounds the enrichment [src: clay_confined_subsurface, discoveries].

Within Bacillota_B, deep-clay isolates were not enriched for Wood–Ljungdahl beyond their phylum congeners (5/5 vs 15/19, p=0.54). The same null held for NiFe-hydrogenase (5/5 vs 14/19, p=0.54) [src: clay_confined_subsurface, discoveries]. These markers therefore track the Bacillota_B lineage rather than deep-clay habitat per se [src: clay_confined_subsurface]. Only [[entities/dissimilatory-sulfate-reduction]] survived the phylogenetic control (5/5 vs 4/19, p_BH=0.04), where p_BH is the Benjamini–Hochberg-adjusted p-value [src: discoveries]. This null rests on a small within-phylum sample of 5 deep-clay isolates. It means no enrichment was detectable at this resolution, not that any effect is ruled out [src: clay_confined_subsurface, discoveries].

## Literature context

The clay report attributes to Bagnoud a minimalistic Opalinus clay food web in which Desulfobulbaceae c16a expressed the complete Wood–Ljungdahl pathway, group 1 [NiFe]-hydrogenase and Sat–AprAB–DsrAB. In that work, three MAGs (metagenome-assembled genomes, reconstructed from community sequencing) recurred across seven independent boreholes [src: clay_confined_subsurface]. This is a cited literature result, not a measurement made by the project [src: clay_confined_subsurface].

## Related

- [[summaries/clay_confined_subsurface__REPORT]]
- [[summaries/discoveries]]
- [[concepts/subsurface-bacillota-specialization]]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]]
