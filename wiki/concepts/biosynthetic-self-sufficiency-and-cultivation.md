---
type: "Concept"
description: "Cultured genomes may miss extreme biosynthetic self-sufficiency."
sources: ["summaries/clay_confined_subsurface__REPORT.md"]
---
# Cultured genomes do not necessarily capture extreme biosynthetic self-sufficiency

Cultured-genome collections can fail to represent the most biosynthetically self-sufficient members of a microbial community, because cultivation selects for organisms that can grow under the available isolation and laboratory conditions. The [[summaries/clay_confined_subsurface__REPORT]] provides a direct test of this issue using clay-associated cultured genomes. [src: clay_confined_subsurface]

## Evidence from the clay-confined cohort

Biosynthetic self-sufficiency was assessed with GapMind amino-acid pathway completeness across an 18-pathway universe. [src: clay_confined_subsurface] In the unfiltered comparison, the deep cultured cohort had a mean completeness of 16.22/18, compared with 16.66/18 for the phylum-stratified soil baseline; the difference was not significant (Mann–Whitney p = 0.153; Cohen’s d = −0.17). [src: clay_confined_subsurface]

After filtering for CheckM completeness of ≥80% and contamination of ≤5%, the deep cohort had a lower mean completeness than the baseline, 15.50/18 versus 17.14/18, with p = 0.009 and Cohen’s d = −0.84. [src: clay_confined_subsurface] This **contradicts** the expectation that the cultured deep-clay genomes in this dataset are unusually biosynthetically self-sufficient. [src: clay_confined_subsurface]

The result is not evidence that biosynthetic self-sufficiency is unimportant in deep subsurface life. Rather, it suggests the hypothesis that the cultured BERDL cohort does not contain the extreme self-sufficient lineages emphasized in studies based on metagenome-assembled genomes or single-cell genomes. [src: clay_confined_subsurface]

## Cultivation and cohort effects

The shallow-clay cultured cohort showed the opposite pattern: its mean completeness was 17.87/18 versus 16.66/18 for the unfiltered baseline, with p = 0.006 and Cohen’s d = +0.52; after quality filtering, it remained 17.87/18 versus 17.14/18, with p = 0.029 and Cohen’s d = +0.43. [src: clay_confined_subsurface] The report interprets this **supports** a cultivation-quality selection explanation for agricultural isolates, while noting that the 18-pathway metric approaches saturation near 18 for many cultured bacteria. [src: clay_confined_subsurface]

The quality-filtered cohort sizes were 9 → 6 genomes for anchor_deep, 30 → 30 for anchor_shallow, and 150 → 137 for soil_baseline. [src: clay_confined_subsurface] The deep cohort therefore provides a small and potentially compositionally selective view of clay-confined life rather than a census of the complete subsurface community. [src: clay_confined_subsurface]

Within Bacillota_B, the deep and baseline means were 16.50 versus 16.79, with p = 0.073 and Cohen’s d = −0.13. [src: clay_confined_subsurface] This **refines** the overall negative result by indicating that the apparent deficit is small within this phylum and that cohort composition contributes to the unstratified comparison. [src: clay_confined_subsurface]

## Measurement limits

GapMind summarizes completeness across only 18 amino-acid pathways, limiting resolution when genomes already score near the upper end of the scale. [src: clay_confined_subsurface] The report therefore recommends a finer-grained sensitivity analysis using all standard amino-acid-biosynthesis EC numbers in eggNOG. [src: clay_confined_subsurface] eggNOG cluster-level annotation propagation within ≥90% average nucleotide identity clusters can also miss strain-level marker variants, including a single non-functional dsrA in an otherwise complete operon, although that example concerns anaerobic metabolism rather than the self-sufficiency score itself. [src: clay_confined_subsurface]

The most defensible interpretation is consequently conditional: the available cultured genomes do not show elevated biosynthetic self-sufficiency, but this negative result cannot exclude highly self-sufficient uncultured lineages. [src: clay_confined_subsurface] This interpretation connects to [[concepts/metabolic-model-gapfilling]], because pathway-completeness metrics can test metabolic capability while still depending on annotation resolution and genome representation. [src: clay_confined_subsurface]

## Tensions

The deep cultured cohort does not support elevated self-sufficiency, whereas the report’s broader interpretation of deep subsurface biology leaves open the possibility that extreme self-sufficient lineages occur outside the cultured collection. [src: clay_confined_subsurface] This is a representation tension rather than a direct contradiction between measurements: the observed cultured genomes and the hypothesized full community refer to different biological subsets. [src: clay_confined_subsurface]

## Open Directions

- Add Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge deep-subsurface MAGs, then compare GapMind and eggNOG amino-acid pathway completeness with the cultured cohort to test whether uncultured lineages contain more extreme self-sufficiency. [src: clay_confined_subsurface]
- Recalculate self-sufficiency from all standard amino-acid-biosynthesis EC numbers in eggNOG and compare the result with the 18-pathway GapMind score to determine whether the apparent deficit is a metric ceiling or a biological difference. [src: clay_confined_subsurface]
- Resolve Bacillota_B differences at genus level and repeat quality-filtered, phylum-stratified comparisons to test whether cohort composition explains the deep-versus-baseline pattern. [src: clay_confined_subsurface]
- Compare BRC-3 and BIC-A1 isolation sources directly, using genome completeness and pathway-level biosynthetic profiles, to test whether borehole source contributes to the observed cultivation bias. [src: clay_confined_subsurface]
