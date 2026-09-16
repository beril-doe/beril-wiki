---
type: "Organism"
description: "Geobacter is an iron-reducing bacterial genus that this corpus places on Opalinus clay rock surfaces at Mont Terri and finds at trace levels in ENIGMA groundwater."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Geobacter

*Geobacter* is a bacterial genus that this corpus treats as an iron reducer. In the cited literature, it and *Geothrix* (geothrix) are the signature lineages of rock-attached Opalinus clay communities. [src: discoveries, clay_confined_subsurface]

## Mont Terri: porewater versus rock surfaces

At [[entities/mont-terri]], two literature paradigms describe qualitatively different microbial communities at the *same* clay site. The Bagnoud (2016) Opalinus porewater paradigm describes porewater dominated by sulfate reducers ([[entities/dissimilatory-sulfate-reduction]]). The Mitzscherling (2023) rock-attached paradigm describes rock surfaces dominated by *Geobacter*/*Geothrix* iron reducers. The corpus records this as a contrast between habitats within one site. It is not a disagreement about a single community. [src: discoveries]

The Mitzscherling et al. (2023) rock-attached community profile reports sulfate-reducing bacteria (SRB) at <0.2% and iron-reducing bacteria (IRB) at 4.3–10.2%, dominated by *Geobacter* and *Geothrix*. In the clay_confined_subsurface project this profile is only a literature comparator. It is not an iron-marker result measured in that project's cultured-genome cohort. [src: clay_confined_subsurface]

Caveat: rock-attached *Geobacter*/*Geothrix* lineages are essentially absent from the genome cohort that clay_confined_subsurface analysed. CPR/DPANN episymbionts (Bell 2022) are also essentially absent. The project therefore could not test the rock-attached iron-reducer paradigm directly. The report states that MAG-augmented future work is needed to test whether the genuine clay-confined community matches the literature predictions. MAGs are metagenome-assembled genomes reconstructed from environmental sequencing. [src: clay_confined_subsurface]

## ENIGMA groundwater versus sediment

In the ENIGMA ASV ecology analysis, the source table reports abundances as percentages in two columns, "Sediment %" and "GW %" (GW is groundwater), followed by a fold enrichment. All pairs below are listed as Sediment % / GW %. *Geobacter* (iron reduction) is 0.00 / 0.01, with a 5.5× ▲GW enrichment. Because these percentages are very small, the fold enrichment rests on trace abundances. The other iron-cycling genera show different patterns. The iron oxidizers [[entities/gallionella]] (0.01 / 0.14, 8.9× ▲GW) and [[entities/sideroxydans]] (0.01 / 0.06, 7.0× ▲GW) are also enriched in groundwater. In contrast, the iron/U reducer [[entities/anaeromyxobacter]] (1.24 / 0.03, 0.02× ▼GW) is depleted in groundwater. For comparison, [[entities/rhodanobacter]] (denitrification) is 1.23 / 3.62 (2.9× ▲GW), [[entities/arcobacter]] (sulfur oxidation) is 0.54 / 0.00 (0× ▼GW), and Ca. [[entities/methanoperedens]] (methane oxidation) is 0.42 / 0.00 (0× ▼GW). [src: enigma_sso_asv_ecology]

## Related pages

- [[summaries/clay_confined_subsurface__REPORT]]: uses the Opalinus rock-attached *Geobacter*/*Geothrix* profile as a literature comparator. [src: clay_confined_subsurface]
- [[summaries/discoveries]]: records the contrast between the Mont Terri porewater and rock-attached communities. [src: discoveries]
- [[summaries/enigma_sso_asv_ecology__REPORT]]: reports sediment and groundwater abundances (%) for the iron-cycling genera. [src: enigma_sso_asv_ecology]
- [[concepts/subsurface-hydrogeological-zonation]]: covers the habitat-partitioned subsurface communities in which *Geobacter* appears. [src: discoveries, enigma_sso_asv_ecology]
