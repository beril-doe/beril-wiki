---
type: "Organism"
description: "Ralstonia is a bacterial genus, including plant pathogens, that appears in BERIL work as a conservation\u2013fitness gradient example, as an organism excluded from co-fitness analysis, and as a member of an acid-associated co-occurrence cluster."
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Ralstonia

*Ralstonia* is a bacterial genus that BERIL projects cite as a plant-pathogen example. It appears in three contexts: a conservation–fitness gradient, a co-fitness analysis that had to exclude it, and a global pH-linked co-occurrence cluster [src: conservation_fitness_synthesis, cofitness_coinheritance, genotype_to_phenotype_enigma]. Strain-level designations in the corpus include UW163 and GMI1000 [src: cofitness_coinheritance].

## Conservation–fitness gradient

The conservation–fitness gradient spans 194,216 protein-coding genes across 43 diverse bacteria. *Ralstonia* is the named plant-pathogen example, alongside archaea (*Methanococcus*) and gut commensals (*Bacteroides*); see [[entities/bacteroides]] [src: conservation_fitness_synthesis].

## Exclusion from co-fitness / co-inheritance analysis

Ralstonia UW163 and GMI1000 have zero co-fitness data in the Fitness Browser ([[entities/kescience-fitnessbrowser]]), even though both are in the organism table. This null result excluded them from the primary co-fitness–co-inheritance analysis [src: cofitness_coinheritance].

The report flags this exclusion as a limitation. The two Ralstonia organisms are the most phylogenetically diverse and lowest-ANI (average nucleotide identity) cases, so the analysis lacks the species the report judges likely to be most informative [src: cofitness_coinheritance].

As a proposed remedy, the report suggests computing co-fitness directly as pairwise Pearson correlations from raw `genefitness` data for Ralstonia and other organisms lacking pre-computed co-fitness. This would recover the missing comparisons. The analysis has not been reported as done [src: cofitness_coinheritance].

## Global pH-driven niche partition

A global analysis of 464K samples associates a Rhodanobacter–Ralstonia–Dyella cluster with environments 1.35 pH units more acidic and 6.9°C warmer than a Brevundimonas–Caulobacter–Sphingomonas cluster worldwide. The report offers this niche partition as the explanation for local co-occurrence at Oak Ridge ([[entities/oak-ridge-field-research-center]], [[entities/rhodanobacter]], [[entities/sphingomonas]]). It is a cluster-level environmental association, not a Ralstonia-specific measurement [src: genotype_to_phenotype_enigma].

## Related pages

- ralstonia solanacearum
- [[summaries/cofitness_coinheritance__REPORT]]
- [[summaries/conservation_fitness_synthesis__REPORT]]
- [[summaries/genotype_to_phenotype_enigma__REPORT]]
