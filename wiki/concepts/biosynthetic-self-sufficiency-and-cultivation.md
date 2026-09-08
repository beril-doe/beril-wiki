---
type: Concept
description: Cultured genomes may miss extreme biosynthetic self-sufficiency in uncultured
  lineages
sources:
- id: clay_confined_subsurface
  resource: ../summaries/clay_confined_subsurface__REPORT.md
  title: clay confined subsurface
- id: bacillota_b_subsurface_accessory
  resource: ../summaries/bacillota_b_subsurface_accessory__REPORT.md
  title: bacillota b subsurface accessory
- id: conservation_fitness_synthesis
  resource: ../summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: Cultured genomes do not necessarily capture extreme biosynthetic self-sufficiency
---
# Cultured genomes do not necessarily capture extreme biosynthetic self-sufficiency

Cultured-genome collections can fail to represent the most biosynthetically self-sufficient members of a microbial community, because cultivation selects for organisms that can grow under the available isolation and laboratory conditions. The [clay_confined_subsurface__REPORT](../summaries/clay_confined_subsurface__REPORT.md) provides a direct test of this issue using clay-associated cultured genomes. [^clay_confined_subsurface]

The [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) **refines** how such comparisons should be interpreted: genomic pathway capability and experimentally observed dependency are distinct. Across 161 organism–pathway pairs, 66 were complete but showed no significant fitness defects under standard conditions (“Latent Capability”), while all 66 became fitness-important under at least one condition type, especially nitrogen limitation, stress, or carbon limitation. [^pathway_capability_dependency] A broader analysis of 1,695 complete pathway–organism pairs from 48 organisms likewise classified 267 (15.8%) as latent, with carbon-source utilization pathways more often latent than amino-acid biosynthesis pathways (24.3% versus 6.5%). [^metabolic_capability_dependency] This **supports** the conclusion that a complete pathway in a cultured genome does not establish biosynthetic self-sufficiency across environments, just as an apparently dispensable pathway does not establish permanent independence from that function. [^pathway_capability_dependency][^metabolic_capability_dependency]

## Evidence from the clay-confined cohort

Biosynthetic self-sufficiency was assessed with GapMind amino-acid pathway completeness across an 18-pathway universe. [^clay_confined_subsurface] In the unfiltered comparison, the deep cultured cohort had a mean completeness of 16.22/18, compared with 16.66/18 for the phylum-stratified soil baseline; the difference was not significant (Mann–Whitney p = 0.153; Cohen’s d = −0.17). [^clay_confined_subsurface]

After filtering for CheckM completeness of ≥80% and contamination of ≤5%, the deep cohort had a lower mean completeness than the baseline, 15.50/18 versus 17.14/18, with p = 0.009 and Cohen’s d = −0.84. [^clay_confined_subsurface] This **contradicts** the expectation that the cultured deep-clay genomes in this dataset are unusually biosynthetically self-sufficient. [^clay_confined_subsurface]

The result is not evidence that biosynthetic self-sufficiency is unimportant in deep subsurface life. Rather, it suggests the hypothesis that the cultured BERDL cohort does not contain the extreme self-sufficient lineages emphasized in studies based on metagenome-assembled genomes or single-cell genomes. [^clay_confined_subsurface] The capability–dependency analysis **supports** retaining this cautious interpretation: pathway completeness alone does not predict whether a pathway is required under a particular condition, and its fitness classification was based on only 7 model organisms with matching GapMind data. [^pathway_capability_dependency] Its broader dataset also covered only 48 fitness-tested organisms, compared with approximately 293,000 genomes with pathway predictions, which **refines** the generalization limit for extrapolating cultured fitness results to uncultured subsurface lineages. [^metabolic_capability_dependency]

## Cultivation and cohort effects

The shallow-clay cultured cohort showed the opposite pattern: its mean completeness was 17.87/18 versus 16.66/18 for the unfiltered baseline, with p = 0.006 and Cohen’s d = +0.52; after quality filtering, it remained 17.87/18 versus 17.14/18, with p = 0.029 and Cohen’s d = +0.43. [^clay_confined_subsurface] The report interprets this as supporting a cultivation-quality selection explanation for agricultural isolates, while noting that the 18-pathway metric approaches saturation near 18 for many cultured bacteria. [^clay_confined_subsurface]

The quality-filtered cohort sizes were 9 → 6 genomes for anchor_deep, 30 → 30 for anchor_shallow, and 150 → 137 for soil_baseline. [^clay_confined_subsurface] The deep cohort therefore provides a small and potentially compositionally selective view of clay-confined life rather than a census of the complete subsurface community. [^clay_confined_subsurface]

Within Bacillota_B, the deep and baseline means were 16.50 versus 16.79, with p = 0.073 and Cohen’s d = −0.13. [^clay_confined_subsurface] This **refines** the overall negative result by indicating that the apparent deficit is small within this phylum and that cohort composition contributes to the unstratified comparison. [^clay_confined_subsurface]

The new [bacillota_b_subsurface_accessory__REPORT](../summaries/bacillota_b_subsurface_accessory__REPORT.md) **supports** the representation concern from a different angle: its 10 deep-clay Bacillota_B genomes were larger and contained more eggNOG orthologous groups than 62 soil-baseline genomes, with mean genome sizes of 4,110,038 bp versus 3,046,124 bp (Cohen’s d=+1.39, p=0.025) and mean OG counts of 2,630 versus 2,106 (Cohen’s d=+1.30, p=0.022). [^bacillota_b_subsurface_accessory] Because CheckM completeness was effectively identical between cohorts at 94.7% and 94.3% (p=0.93), the difference was not attributed to genome-quality artifacts. [^bacillota_b_subsurface_accessory] This **supports** a self-sufficiency model for cultivable subsurface Bacillota_B, but it does not overturn the GapMind result: larger, functionally richer genomes are not equivalent to elevated completeness across the particular 18 amino-acid pathways measured. [^bacillota_b_subsurface_accessory]

The capability–dependency analysis **supports** this distinction at broader scale: accessory genes contributed to amino-acid pathway completeness, with all-gene versus core-only gaps of 0.146 for leucine and valine, 0.141 for arginine, 0.140 for lysine, and 0.140 for threonine biosynthesis. [^pathway_capability_dependency] These results make genome expansion mechanistically relevant to pathway capacity, but do not demonstrate metabolite exchange or prove self-sufficiency in the subsurface community. [^pathway_capability_dependency]

The same analysis **refines** the cultivation interpretation by showing that latent capability was associated with pangenome openness at the clade level: latent-capability rate correlated positively with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [^metabolic_capability_dependency] This is consistent with genome dynamics and community context influencing the persistence of complete but fitness-neutral pathways, but it does not show that cultured genomes capture the most self-sufficient lineages or establish a Black Queen mechanism in the subsurface. [^metabolic_capability_dependency]

The broader [conservation_fitness_synthesis__REPORT](../summaries/conservation_fitness_synthesis__REPORT.md) **refines** this cultivation interpretation by showing that laboratory fitness and genome conservation are not direct measurements of natural-environment fitness: essential genes were 82% core, whereas always-neutral genes were 66% core, and 28,017 genes were both costly in the laboratory and conserved in the pangenome. [^conservation_fitness_synthesis] Thus, cultured-genome representation and laboratory performance should not be treated as equivalent evidence about the biosynthetic capabilities or selective importance of uncultured subsurface lineages. [^conservation_fitness_synthesis]

## Measurement limits

GapMind summarizes completeness across only 18 amino-acid pathways, limiting resolution when genomes already score near the upper end of the scale. [^clay_confined_subsurface] The report therefore recommends a finer-grained sensitivity analysis using all standard amino-acid-biosynthesis EC numbers in eggNOG. [^clay_confined_subsurface] eggNOG cluster-level annotation propagation within ≥90% average nucleotide identity clusters can also miss strain-level marker variants, including a single non-functional dsrA in an otherwise complete operon, although that example concerns anaerobic metabolism rather than the self-sufficiency score itself. [^clay_confined_subsurface]

The pathway-capability analysis **refines** this limitation by extending the completeness comparison beyond amino-acid biosynthesis: its broader survey covered 80 GapMind pathways, including 18 amino-acid biosynthesis and 62 carbon-source utilization pathways, across approximately 293,000 genomes. [^pathway_capability_dependency] It found that variable pathway count correlated with pangenome openness after controlling for genome count (partial Spearman rho=0.530, p=2.83e-203), supporting a relationship between genome fluidity and metabolic variation, but not proving that cultured genomes capture the most self-sufficient lineages. [^pathway_capability_dependency]

The new analysis **supports** the concern that pathway capability is annotation- and mapping-dependent: it used SEED subsystem annotations as a pathway-membership proxy, excluded deoxyribonate and myoinositol because no matching SEED role descriptions were found, and excluded alanine from classification because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [^metabolic_capability_dependency] It also found that the latent fraction was sensitive to threshold choices, ranging from 4.7% to 21.1% across 16 tested combinations, although the qualitative carbon-pathway result persisted. [^metabolic_capability_dependency] These limitations **refine** rather than overturn the use of pathway completeness as evidence about genomic capability.

The Bacillota_B comparison further shows that enrichment of broad functional capacity can coexist with unresolved annotation: 547 orthologous groups were significantly enriched in deep-clay genomes, but 462 were classified as other or unannotated, and manual inspection indicated that this category contained additional anaerobic-respiration and electron-transfer functions. [^bacillota_b_subsurface_accessory] This **refines** the interpretation of genome expansion by showing that OG-count differences alone do not identify which added functions contribute to biosynthetic self-sufficiency. [^bacillota_b_subsurface_accessory]

The most defensible interpretation is consequently conditional: the available cultured genomes do not show elevated biosynthetic self-sufficiency, but this negative result cannot exclude highly self-sufficient uncultured lineages. [^clay_confined_subsurface] This interpretation connects to [metabolic-model-gapfilling](metabolic-model-gapfilling.md), because pathway-completeness metrics can test metabolic capability while still depending on annotation resolution and genome representation. [^clay_confined_subsurface]

## Tensions

The deep cultured cohort does not support elevated self-sufficiency, whereas the report’s broader interpretation of deep subsurface biology leaves open the possibility that extreme self-sufficient lineages occur outside the cultured collection. [^clay_confined_subsurface] This is a representation tension rather than a direct contradiction between measurements: the observed cultured genomes and the hypothesized full community refer to different biological subsets. [^clay_confined_subsurface]

The Bacillota_B evidence also **supports** a self-sufficiency model for cultivable subsurface genomes through larger genome size and OG content, while the GapMind comparison finds no elevated amino-acid pathway completeness and, after quality filtering, finds lower completeness in the deep cohort. [^bacillota_b_subsurface_accessory][^clay_confined_subsurface] These findings should not be reconciled by treating genome expansion as proof of biosynthetic self-sufficiency: they measure different aspects of genomic and metabolic capacity. [^bacillota_b_subsurface_accessory][^clay_confined_subsurface]

The conservation–fitness synthesis adds a related interpretive tension: conserved genes can be costly under laboratory conditions, so laboratory burden does not by itself show that a cultured or uncultured lineage lacks natural selective value. [^conservation_fitness_synthesis] This **refines** rather than overturns the page’s representation argument, because neither conservation nor laboratory fitness directly establishes biosynthetic self-sufficiency in the deep subsurface. [^conservation_fitness_synthesis]

The condition-dependent fitness result introduces a further measurement tension: all 66 aggregate Latent Capability pairs became important under at least one condition type, but the report cautions that median-based condition-specific thresholds can cause reclassification by construction. [^pathway_capability_dependency] This **supports** treating cultured laboratory observations as condition-bounded evidence rather than as definitive evidence for or against environmental self-sufficiency. [^pathway_capability_dependency]

The broader capability analysis adds a related tension: pathway-level conservation did not distinguish latent capabilities from active dependencies, whereas latent-capability rate correlated positively with pangenome openness at the clade level (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [^metabolic_capability_dependency] The result **refines** the representation argument by placing the signal at the level of genome dynamics and clade context rather than simple conservation of individual complete pathways; it does not resolve whether cultured subsurface genomes are representative of extreme self-sufficient lineages. [^metabolic_capability_dependency]

## Open Directions

- Add Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge deep-subsurface MAGs, then compare GapMind and eggNOG amino-acid pathway completeness with the cultured cohort to test whether uncultured lineages contain more extreme self-sufficiency. [^clay_confined_subsurface]
- Recalculate self-sufficiency from all standard amino-acid-biosynthesis EC numbers in eggNOG and compare the result with the 18-pathway GapMind score to determine whether the apparent deficit is a metric ceiling or a biological difference. [^clay_confined_subsurface]
- Resolve Bacillota_B differences at genus level and repeat quality-filtered, phylum-stratified comparisons to test whether cohort composition explains the deep-versus-baseline pattern. [^clay_confined_subsurface]
- Compare BRC-3 and BIC-A1 isolation sources directly, using genome completeness and pathway-level biosynthetic profiles, to test whether borehole source contributes to the observed cultivation bias. [^clay_confined_subsurface]
- Decompose the 547 enriched Bacillota_B OGs into amino-acid biosynthesis and other functional classes, then compare those annotations with pathway-level completeness to test whether genome expansion reflects biosynthetic self-sufficiency or primarily anaerobic persistence functions. [^bacillota_b_subsurface_accessory]
- Calibrate condition-specific pathway-importance thresholds against independently defined essentials, then test whether apparent Latent Capability reclassification predicts biosynthetic capacity in uncultured subsurface genomes. [^pathway_capability_dependency]
- Combine subsurface MAG pathway profiles with conservation and laboratory-fitness annotations to test whether candidate self-sufficient lineages carry costly-and-conserved biosynthetic functions or the costly-and-dispensable signature identified across bacteria. [^conservation_fitness_synthesis]
- Replace SEED-proxy pathway membership with direct GapMind per-step gene assignments, then test whether the latent-capability association with pangenome openness persists without proxy-mapping exclusions. [^metabolic_capability_dependency]
- Compare the environmental pathway profiles of subsurface MAGs with the condition-specific fitness classes from the Fitness Browser to test whether candidate self-sufficient lineages retain pathways that are latent in laboratory conditions but important under stress or nutrient limitation. [^metabolic_capability_dependency]

[^clay_confined_subsurface]: [clay confined subsurface](../summaries/clay_confined_subsurface__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^bacillota_b_subsurface_accessory]: [bacillota b subsurface accessory](../summaries/bacillota_b_subsurface_accessory__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../summaries/conservation_fitness_synthesis__REPORT.md)
