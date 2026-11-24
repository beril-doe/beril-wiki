---
type: "Concept"
description: "Whether clinical-biased public genome collections and databases represent the niches of subsurface isolates, and the consequences for transfer learning; it stops at name-matching errors."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Representativeness of reference genome collections for environmental field isolates

The evidence here suggests that the NCBI genome collection under-represents the niches of ENIGMA subsurface field isolates. It comes from one report, [[summaries/genotype_to_phenotype_enigma__REPORT]], and its biogeography is genus-level at 16S resolution. [src: genotype_to_phenotype_enigma] Transfer learning from clinical phenotype databases may therefore be biased for these isolates. [src: genotype_to_phenotype_enigma] For the general bias, see [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

## Genus-level environmental profiles

Genus-level profiling across all GTDB genomes shows that [[entities/pseudomonas]] globally is 37.8% clinical (driven by P. aeruginosa), 12.9% soil/plant and 9.4% aquatic. [src: genotype_to_phenotype_enigma] All ENIGMA Pseudomonas belong to Pseudomonas_E, the fluorescens/protegens clade, which is environmental rather than clinical. [src: genotype_to_phenotype_enigma] So the genus-level clinical share does not describe the ENIGMA strains. [src: genotype_to_phenotype_enigma]

[[entities/rhodanobacter]] is described as purely aquatic/contaminated, with 55% aquatic, 10% contaminated and 0% clinical assignments. [src: genotype_to_phenotype_enigma] The report concludes that ENIGMA's subsurface field isolates occupy environmental niches underrepresented in the NCBI genome collection. [src: genotype_to_phenotype_enigma]

## Ubiquity of the ENIGMA genera

All 14 ENIGMA genera are globally ubiquitous. They were detected in 4,086-288,686 of 464,000 samples in the Microbial Atlas 16S database ([[entities/microbeatlas]]). [src: genotype_to_phenotype_enigma] The report calls them ecologically significant genera, not rare specialists. [src: genotype_to_phenotype_enigma]

## Caveats

The biogeography is genus-level at 16S resolution, so it cannot show whether the specific ENIGMA strains match the niches of reference genomes. [src: genotype_to_phenotype_enigma] See [[concepts/genus-level-amplicon-resolution-and-rare-taxon-limits-in-matching-reference-organisms-to-field-data]]. The bias in transfer learning is stated as a possibility, not a measured effect. [src: genotype_to_phenotype_enigma]

## Open Directions

- Compare phenotype predictions for Pseudomonas_E and Rhodanobacter isolates when the training set is clinical-heavy and when it is environment-matched. This would measure the transfer-learning bias that the report only raises.
- Repeat the environmental profiling at species or strain level, for example with shotgun data. This would test whether the genus-level clinical share hides niche differences.
- Compute the clinical share for each of the 14 ENIGMA genera, as was done for Pseudomonas and Rhodanobacter. This would show which genera are most affected.
