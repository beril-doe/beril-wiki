---
type: "Concept"
description: "How taxonomic resolution, prevalence thresholds and rarity limit linking reference-collection organisms to environmental survey data; stops at this matching problem."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/lab_field_ecology__REPORT.md"]
---
# Genus-level amplicon resolution and rare-taxon limits in matching reference organisms to field data

Linking reference-collection organisms, such as those in the Fitness Browser (FB), to environmental survey data is limited by genus-level 16S resolution, rarity of some reference genera in the field, and prevalence thresholds that remove the rarest ones from analysis. [src: genotype_to_phenotype_enigma, lab_field_ecology] The evidence comes from two reports, [[summaries/lab_field_ecology__REPORT]] and [[summaries/genotype_to_phenotype_enigma__REPORT]]. Both state these limits as caveats of their own analyses. [src: genotype_to_phenotype_enigma, lab_field_ecology]

## Genus-level resolution

Both reports work at genus level. The genotype_to_phenotype_enigma Microbial Atlas biogeography analysis is at genus level (16S resolution). [src: genotype_to_phenotype_enigma] Species-level biogeography is available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma] In lab_field_ecology, Oak Ridge amplicon data resolve only to genus, so species or strain matching to FB organisms is not possible. [src: lab_field_ecology]

This matters because FB organisms are specific strains. A genus like *Pseudomonas* contains thousands of species with vastly different ecologies. [src: lab_field_ecology] The report proposes using metagenomic data, if available in ENIGMA CORAL genome or assembly tables, to match FB organisms at species or strain level. [src: lab_field_ecology] See [[entities/pseudomonas]] and [[entities/fitness-browser]].

## Detection and prevalence at Oak Ridge

Of 26 unique genera represented in the FB, 14 were detected in Oak Ridge groundwater communities by 16S amplicon sequencing. [src: lab_field_ecology] Of those 14, 11 had sufficient prevalence (at least 10 sites) for correlation analysis. [src: lab_field_ecology] Only 12 FB genera had enough data for the metal tolerance correlation, which limits statistical power. [src: lab_field_ecology]

The most prevalent genera were *Sphingomonas* (93% of 108 sites), *Pseudomonas* (91%) and *Caulobacter* (82%). [src: lab_field_ecology] *Shewanella*, *Dechlorosoma* and *Marinobacter* were excluded because their prevalence was below 10 sites. [src: lab_field_ecology]

## Rarity of a model organism

*Desulfovibrio*, the primary ENIGMA model organism, was detected at only 34% of sites, with maximum relative abundance of 0.09%. [src: lab_field_ecology] The report says this rarity makes its correlation analysis unreliable. [src: lab_field_ecology]

*Desulfovibrio* showed no correlation with [[entities/uranium]] (rho=0.022, p=0.82). *Pseudomonas* also showed none (rho=-0.059, p=0.55), although both are ENIGMA model organisms. [src: lab_field_ecology] Given the report's caveats, the *Desulfovibrio* null result is unreliable rather than evidence of no relationship. [src: lab_field_ecology] The *Pseudomonas* result carries the genus-level caveat. [src: lab_field_ecology]

## Missing reference organisms

The report states that *Rhodanobacter* dominates contaminated Oak Ridge wells but is not in the FB. It identifies adding it as a high-impact target. [src: lab_field_ecology] See [[entities/rhodanobacter]].

## Open Directions

- Test whether metagenomic data in ENIGMA CORAL genome or assembly tables allow species- or strain-level matching to FB organisms. This would address the genus-only limit.
- Repeat the *Desulfovibrio*–uranium test with deeper or targeted sequencing, since rarity currently makes it unreliable.
- Extend species-level biogeography beyond the 20 verified pangenome-linked strains by widening verified GTDB matches.
- Add *Rhodanobacter* to the FB and compare its fitness with its field abundance. See [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance]].
