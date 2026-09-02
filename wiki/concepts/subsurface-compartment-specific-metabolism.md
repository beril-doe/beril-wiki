---
type: "Concept"
description: "How porewater and rock attachment shape subsurface metabolic signals"
sources: ["summaries/clay_confined_subsurface__REPORT.md"]
---
# Subsurface metabolic signatures depend on porewater versus rock-attached compartment

Subsurface metabolic interpretation depends on whether genomes represent porewater-associated cells or rock-attached communities, because these compartments can carry different metabolic signatures. The cultured deep-clay cohort in this study matched the Bagnoud Mont Terri porewater paradigm rather than demonstrating representation of the rock-attached community. [src: clay_confined_subsurface] The study therefore refines [[concepts/subsurface-bacillota-specialization]] by separating a compartment-associated sulfate-reduction signal from broader anaerobic-toolkit patterns that are partly explained by phylogeny. [src: clay_confined_subsurface]

The source report analyzed 9 deep-confined genomes, 30 shallow-clay genomes, and a phylum-stratified soil baseline of 150 genomes, with 137 genomes remaining in the reported quality-filtered baseline. [src: clay_confined_subsurface] The deep cohort included 8 Mont Terri Opalinus borehole genomes and 1 bentonite-formation genome, whereas the shallow cohort included 8 Coalvale silty-clay genomes, 1 Cerrado clay genome, and 21 agricultural-clay genomes. [src: clay_confined_subsurface] Compartment annotations were inferred from keywords in isolation-source strings, so some bentonite or “rock” entries could plausibly represent porewater or rock-attached material. [src: clay_confined_subsurface]

## Porewater-associated sulfate reduction

The strongest compartment-specific result was dissimilatory sulfate reduction: 5/9 deep genomes carried sulfate-reduction markers, compared with 1/9 iron-reduction-marker-positive genomes under the original analysis. [src: clay_confined_subsurface] Relative to the Mitzscherling (2023) rock-attached null, the sulfate-reduction enrichment was highly significant, with 5 observed positives versus 0.018 expected among 9 genomes and binomial p = 4.0×10⁻¹². [src: clay_confined_subsurface] The corresponding comparison for iron-reduction depletion was not significant, with 1 observed versus 0.63 expected and p = 0.87. [src: clay_confined_subsurface]

This **supports** the interpretation that the cultured deep cohort is enriched for a porewater-associated sulfate-reduction signature rather than serving as a representative sample of rock-attached subsurface metabolism. [src: clay_confined_subsurface] The 8 Opalinus genomes traced to BRC-3 or BIC-A1 borehole isolation sources and included Desulfosporosinus, BRH-c8a, BRH-c4a, Lutibacter, BRH-c54, Roseovarius, and Stenotrophomonas lineages. [src: clay_confined_subsurface] Rock-attached Geobacter and Geothrix lineages and CPR/DPANN episymbionts were essentially absent from the cultured cohort, limiting direct inference about the complete rock-attached community. [src: clay_confined_subsurface]

## Corrected iron-reduction interpretation

The original iron-reduction narrative was withdrawn because K07811, K17324, and K17323 were misidentified as iron-reduction markers; they are TMAO reductase, glycerol ABC transport ATP-binding, and glycerol ABC transport permease, respectively. [src: clay_confined_subsurface] A corrected multi-heme cytochrome detector combined PFAM PF02085, PFAM PF22678, and CXXCH heme-binding motif counting, using a threshold of ≥4 motifs. [src: clay_confined_subsurface]

The corrected iron-reduction rates were 55.6% for anchor_deep (n = 9), 40.0% for anchor_shallow (n = 30), and 40.9% for soil_baseline (n = 149), compared with original rates of 11.1%, 50.0%, and 20.1%, respectively. [src: clay_confined_subsurface] All corrected cohort comparisons had Fisher p ≥ 0.46. [src: clay_confined_subsurface] Thus, the corrected analysis **contradicts** the original shallow-greater-than-deep iron-reduction interpretation, while the sulfate-reduction enrichment remains supported. [src: clay_confined_subsurface]

## Anaerobic-toolkit enrichment and phylogenetic confounding

The anaerobic toolkit combined Wood–Ljungdahl (WL), group 1 [NiFe]-hydrogenase (NiFe), and dissimilatory sulfate-reduction (SR) modules. [src: clay_confined_subsurface] Mean toolkit scores were 1.889 for anchor_deep (n = 9), 0.033 for anchor_shallow (n = 30), and 0.393 for soil_baseline (n = 140), while the proportions containing all three modules were 0.556, 0.000, and 0.021, respectively. [src: clay_confined_subsurface]

Against the soil baseline, deep-cohort Fisher tests adjusted by BH-FDR, the Benjamini–Hochberg false-discovery-rate procedure, gave WL OR = 10.4, p_BH = 0.004; NiFe OR = 10.5, p_BH = 0.004; SR OR = 33.8, p_BH = 2.5×10⁻⁴; IR OR = 0.46, p_BH = 0.69; and nitrogenase OR = 5.4, p_BH = 0.035. [src: clay_confined_subsurface] These cohort-level results **support** a broad anaerobic-toolkit contrast but do not by themselves establish that every component is caused by the porewater-versus-rock-attached compartment. [src: clay_confined_subsurface]

Within Bacillota_B, WL occurred in 5/5 deep genomes versus 15/19 baseline genomes, with p = 0.54 and p_BH = 0.54 (1.0 as reported in the within-phylum table), while NiFe occurred in 5/5 versus 14/19, also with p = 0.54 and p_BH = 0.54 (1.0 as reported). [src: clay_confined_subsurface] SR occurred in 5/5 deep genomes versus 4/19 baseline genomes, with OR = ∞, p = 0.003, and p_BH = 0.044. [src: clay_confined_subsurface] This **refines** the broad anaerobic-toolkit result: WL and NiFe primarily tracked the Bacillota_B lineage, whereas sulfate reduction remained associated with the deep cohort after the within-phylum comparison. [src: clay_confined_subsurface] This distinction connects the compartment question to [[concepts/subsurface-bacillota-specialization]] and [[concepts/phylogenetic-confounding-of-phenotype-associations]]. [src: clay_confined_subsurface]

## Limits of the compartment inference

After the stated CheckM quality filter, anchor_deep changed from 9 to 6 genomes, anchor_shallow remained 30 genomes, and soil_baseline changed from 150 to 137 genomes. [src: clay_confined_subsurface] The deep anchor cohort was small, with n = 9 before quality filtering, so the report states that only large effects, described as Cohen’s d > 0.7 for unfiltered comparisons, are reliably detectable. [src: clay_confined_subsurface] The study applies only to cultivable porewater-cultured deep-clay isolates and not to the full Mont Terri or bentonite microbial communities. [src: clay_confined_subsurface]

The sulfate-reduction result was reported as robust to two stricter compartment definitions, but the keyword-derived annotations and the absence of many rock-attached lineages mean that the result should be interpreted as evidence about the sampled cultured cohort rather than a complete census of compartment-specific metabolism. [src: clay_confined_subsurface] MAG-augmented work is required to test whether the complete clay-confined community follows the same metabolic patterns. [src: clay_confined_subsurface] The source summary and project context are available at [[summaries/clay_confined_subsurface__REPORT]], with [[concepts/metabolic-model-gapfilling]] providing a related perspective on how metabolic-capability metrics can constrain interpretation. [src: clay_confined_subsurface]

## Open Directions

- Add deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge, then apply the same sulfate-reduction and corrected iron-reduction detectors to ask whether the porewater signature persists when rock-attached and uncultivated lineages are represented. [src: clay_confined_subsurface]
- Compare BRC-3 and BIC-A1 genomes directly using compartment-resolved marker analysis to test whether borehole source explains part of the deep-cohort signal. [src: clay_confined_subsurface]
- Link genome-predicted sulfate-reduction markers to Bagnoud’s metaproteomic evidence to test whether the inferred porewater signature is expressed in situ. [src: clay_confined_subsurface]
- Resolve Bacillota_B differences at genus level and repeat the WL, NiFe, and SR comparisons to distinguish lineage-specific metabolism from a compartment effect. [src: clay_confined_subsurface]
- Apply the sulfate-reduction and corrected iron-reduction diagnostic to other subsurface settings to test whether the compartment distinction generalizes beyond the Mont Terri and bentonite-associated cohorts. [src: clay_confined_subsurface]
