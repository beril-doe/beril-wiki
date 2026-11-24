---
type: "Organism"
description: "GTDB phylum-level lineage of anaerobic Firmicutes, including Desulfosporosinus and Desulforudis, compared between deep-clay and soil genomes."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
aliases: ["Bacillota B"]
---
# Bacillota_B

This page covers Bacillota_B, the GTDB phylum-level lineage of anaerobic Firmicutes that includes Desulfosporosinus and Desulforudis, compared between deep-clay and soil genomes. Deep-clay genomes are larger than soil genomes of the same phylum. [src: bacillota_b_subsurface_accessory] Most of the toolkit signal in clay isolates tracks the lineage, and only sulfate reduction (SR) stays enriched after phylogenetic control. [src: discoveries]

## Key facts

- The KBase Data Lakehouse pangenome contains 334 Bacillota_B genomes, far fewer than the v1.1 plan's 6,700 estimate. [src: bacillota_b_subsurface_accessory]
- A project table lists 314 Bacillota_B genomes with quality control (QC) and isolation metadata. [src: bacillota_b_subsurface_accessory]
- The phylum contains Desulfosporosinus, BRH-c4a and BRH-c8a, the lineages that dominate cultured clay isolates. [src: discoveries]
- The soil baseline carries Wood–Ljungdahl and group 1 [NiFe]-hydrogenase at high background rates, with a toolkit mean of 1.65. [src: clay_confined_subsurface, discoveries]

## Cohorts compared

The deep-clay anchor has 10 genomes. Mont Terri Opalinus borehole supplies 5 (Desulfosporosinus, BRH-c8a×2, BRH-c4a and one metagenomic Desulfosporosinus). [src: bacillota_b_subsurface_accessory] Mont Terri rock-porewater metagenome assembled genomes (MAGs) supply 3. [src: bacillota_b_subsurface_accessory] The Russian Beyelii Yar borehole supplies 2, Candidatus Desulforudis audaxviator and Ch130 Thermacetogeniaceae. [src: bacillota_b_subsurface_accessory] The anchor is genus-clumped: 3 BRH-c8a, 2 BRH-c4a, 2 Desulfosporosinus, Desulforudis, Ch130 and 1 other. [src: bacillota_b_subsurface_accessory] It includes 3 Desulfosporosinus genomes that contributed to the sporulation ortholog group (OG) signal. [src: bacillota_b_subsurface_accessory]

The soil baseline has 62 phylum-matched soil/sediment genomes. These are Syntrophomonadales 29, Desulfitobacteriales 16, Moorellales 6, Thermacetogeniales 4, Ammonifexales 2, Carboxydocellales 2, Desulfotomaculales 1, Heliobacteriales 1 and Thermincolales 1. [src: bacillota_b_subsurface_accessory]

## Genome size

Deep-clay Bacillota_B genomes are significantly larger than soil-baseline genomes. The mean difference is 35%, and deep-clay genomes carry about 25% more eggNOG OGs per genome. This rejected hypothesis H2, which predicted the opposite direction. [src: bacillota_b_subsurface_accessory] Mean genome size was 4,110,038 bp in the anchor (n=10) and 3,046,124 bp in the baseline (n=62), with Cohen's d +1.39 and Mann–Whitney p 0.025. [src: bacillota_b_subsurface_accessory]

The central digest reports a CheckM-rescaled version of the same comparison. Genome size is 4.3 Mbp in the anchor and 3.2 Mbp in the baseline (Cohen's d = +1.37, Mann–Whitney p=0.013), and the anchor is 35% larger. [src: discoveries]

## Gene content within the phylum

Phylogenetic control removes most of the apparent clay enrichment. Wood–Ljungdahl carriage does not differ between deep clay and baseline isolates (5/5 vs 15/19, p=0.54). [src: clay_confined_subsurface, discoveries] [NiFe]-hydrogenase carriage does not differ either (5/5 vs 14/19, p=0.54). [src: clay_confined_subsurface, discoveries] These markers track the Bacillota_B lineage, not deep-clay habitat. [src: clay_confined_subsurface]

Only dissimilatory sulfate reduction (dsrAB-aprAB-sat) survives. Five of 5 deep Bacillota_B isolates carry it, against 4/19 soil-baseline isolates (OR=∞, p=0.003, p_BH=0.04). OR is the odds ratio. [src: clay_confined_subsurface, discoveries] The report notes that the "n=5 vs 19" structure may hide differences among Desulfosporosinus, BRH-c8a and BRH-c4a. [src: clay_confined_subsurface]

The report reads the cohort-level depth signal as oversampling. Sampling clay-confined habitats over-samples Bacillota_B Desulfotomaculales and Desulfitobacteriales, which already carry the toolkit. It does not read the signal as a habitat-specific broader toolkit. [src: clay_confined_subsurface]

GapMind pathway completeness within Bacillota_B is not significantly higher in deep clay. The anchor_deep mean is 16.5 against 16.8 for baseline (p=0.07, d=−0.13). [src: clay_confined_subsurface] The underlying table gives n_a=4, n_b=19, means 16.50 and 16.79, and p=0.073. [src: clay_confined_subsurface]

## Caveats

The clay_confined_subsurface soil_baseline cohort changed from 150 to 137 after quality filtering. It was phylum-stratified soil/sediment with no clay mention, and its listed phylum counts (Pseudomonadota 50, Bacillota 40, Bacillota_B 20, Bacteroidota 20, Actinomycetota 20) sum to 150, the pre-filter total. [src: clay_confined_subsurface]

The 10-genome anchor is genus-clumped, as listed under Cohorts compared. [src: bacillota_b_subsurface_accessory]

Related: [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]] and [[entities/dissimilatory-sulfate-reduction-pathway]].
