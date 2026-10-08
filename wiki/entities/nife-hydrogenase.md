---
type: "Gene_Or_Pathway"
description: "[NiFe]-hydrogenase, studied in this corpus as group 1 [NiFe]-hydrogenase markers in deep-clay subsurface genomes, where its apparent enrichment reflects Bacillota_B lineage background rather than habitat."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
# [NiFe]-hydrogenase

**Aliases:** NiFe-hydrogenase, NiFe hydrogenase. The corpus evidence concerns **group 1 [NiFe]-hydrogenase**, a subgroup of this enzyme class, and does not cover the class as a whole. The cohort comparison table in the clay analysis uses the label `NiFe_complete` for its [NiFe]-hydrogenase completeness call. That label is an analysis marker, not another name for the enzyme. The deep-clay subsurface analysis scored [NiFe]-hydrogenase markers as part of an anaerobic "toolkit" in confined-clay genomes, together with the [[entities/wood-ljungdahl-pathway]] and [[entities/dissimilatory-sulfate-reduction]] [src: clay_confined_subsurface, discoveries].

## Prevalence in deep-clay genomes

Among the 9 deep-clay anchor genomes in the KBase Data Lakehouse, 7 carry group 1 [NiFe]-hydrogenase markers and 5 carry the dissimilatory sulfate reduction module (Sat, AprAB, DsrAB). These include direct hits on the BRH-c8a lineage, which Bagnoud's nomenclature calls Peptococcaceae c8a, and on the desulfosporosinus lineage [src: clay_confined_subsurface].

At cohort level, the [NiFe]-hydrogenase completeness marker (NiFe_complete) occurred in 7 of 9 deep anchor genomes versus 35 of 140 soil-baseline genomes. The odds ratio was 10.5 with an adjusted p of 0.004. As the next section shows, this apparent enrichment does not survive within-phylum control [src: clay_confined_subsurface].

The report cites Bagnoud's finding of a minimalistic Opalinus clay food web. In that food web, Desulfobulbaceae c16a expressed the complete Wood–Ljungdahl pathway, group 1 [NiFe]-hydrogenase and Sat–AprAB–DsrAB, and three metagenome-assembled genomes (MAGs, genomes reconstructed from metagenomic reads) recurred across seven independent boreholes. This is literature context reported by the project, not a measurement made in the corpus [src: clay_confined_subsurface].

## Phylogenetic confound (Bacillota_B)

Caveat: the [[entities/bacillota-b]] phylum contains Desulfosporosinus, BRH-c4a and BRH-c8a, which are the lineages that dominate the deep anchor cohort and cultured clay isolates. This phylum carries Wood–Ljungdahl and group 1 [NiFe]-hydrogenase at high background rates even in soil samples, with a Bacillota_B baseline mean toolkit score of 1.65. Cohort-level enrichment of these markers is therefore confounded by phylogeny [src: clay_confined_subsurface, discoveries].

Null result: within Bacillota_B, [NiFe]-hydrogenase is not enriched in deep-clay isolates relative to phylum congeners (5/5 vs 14/19, p=0.54), and neither is Wood–Ljungdahl (5/5 vs 15/19, p=0.54). These markers track the Bacillota_B lineage, not deep-clay habitat per se. Only sulfate reduction survives the phylogenetic control (5/5 vs 4/19, p_BH=0.04) [src: clay_confined_subsurface, discoveries].

## Related pages

- [[entities/bacillota-b]], desulfosporosinus, [[entities/wood-ljungdahl-pathway]], [[entities/dissimilatory-sulfate-reduction]]
- [[concepts/subsurface-bacillota-specialization]], [[concepts/phylogenetic-confounding-of-pangenome-associations]]
- [[summaries/clay_confined_subsurface__REPORT]], [[summaries/discoveries]]
