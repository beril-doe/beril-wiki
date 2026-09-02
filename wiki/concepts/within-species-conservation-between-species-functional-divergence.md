---
type: "Concept"
description: "Within-species conservation can coexist with between-species functional divergence."
sources: ["summaries/bacdive_metal_validation__REPORT.md"]
---
# Conserved Within-Species Functions Can Coexist with Between-Species Functional Divergence

Species can conserve particular functions across their own members while still differing from other species in the total breadth of those functions. In this project, the distinction explains how relatively conserved metal-tolerance functions can coexist with species-level differences in genome-derived metal-tolerance scores and environmental distributions. [src: bacdive_metal_validation]

## Evidence from Metal-Tolerance Scores

The [[summaries/bacdive_metal_validation__REPORT]] tested whether isolation environments provide ecological validation for genome-based metal-tolerance scores by linking [[entities/bacdive]] strains to [[entities/gtdb]] pangenome species. [src: bacdive_metal_validation]

Among 97,334 BacDive strains, 42,227 (43.4%) matched 6,426 GTDB species, and 25,089 matched strains had isolation-source metadata. [src: bacdive_metal_validation] Heavy-metal contamination isolates had a median metal score of 0.240 and a mean of 0.236, compared with an environmental-baseline median of 0.187 and mean of 0.195. [src: bacdive_metal_validation] Their median delta was +0.053, with Cohen's d = +1.00 and Mann-Whitney p=0.006 for n=10 isolates. [src: bacdive_metal_validation]

The contamination gradient supports between-species functional divergence in aggregate metal-tolerance capacity: heavy metal had d=+1.00, waste/sludge d=+0.57, all contamination d=+0.43, and industrial environments d=+0.20. [src: bacdive_metal_validation] The corresponding sample sizes were n=10 for heavy metal, n=305 for waste/sludge, n=176 for all contamination, and n=796 for industrial isolates. [src: bacdive_metal_validation] These environment-associated differences support the interpretation that species can differ in their overall complement of metal-tolerance functions even when individual functions are conserved within species. [src: bacdive_metal_validation]

## Conservation Does Not Require Equal Functional Scores

The report proposes that metal-tolerance genes may be 88% core while species still vary in the total number of metal-tolerance genes represented in their core genomes. [src: bacdive_metal_validation] This hypothesis reconciles within-species conservation of shared metal-tolerance functions with between-species divergence in the number and breadth of encoded functions, but the project did not directly test causality between core-genome size, metal-tolerance score, and contamination occupancy. [src: bacdive_metal_validation]

The metal-tolerance score was normalized as metal clusters divided by annotated clusters, which controls for genome size but does not eliminate the possibility that metal-tolerance functions correlate with total metabolic complexity. [src: bacdive_metal_validation] This limitation refines the interpretation of the observed score differences: they are consistent with functional divergence among species, but they cannot by themselves establish that metal-tolerance functions, rather than correlated genome properties, cause environmental enrichment. [src: bacdive_metal_validation]

## Phylum-Stratified Support

The contamination signal persisted within Pseudomonadota, where contamination isolates had metal scores delta=+0.040 above environmental isolates (p<0.001; n=85 contamination and n=5,655 environmental), and within Actinomycetota, where the delta was +0.035 (p<0.001; n=62 and n=772, respectively). [src: bacdive_metal_validation] These results support functional divergence beyond broad phylum composition in the two most-sampled phyla. [src: bacdive_metal_validation]

The signal was not significant within Bacillota, where delta=-0.012 and p=0.285 (n=19 contamination and n=492 environmental), or Bacteroidota, where delta=-0.008 and p=0.456 (n=5 and n=156, respectively). [src: bacdive_metal_validation] These null results do not distinguish biological differences from limited statistical power because contamination-isolate sample sizes were small. [src: bacdive_metal_validation]

## Interpretation and Tensions

The evidence supports a layered model of functional organization: functions may be relatively conserved among members of a species, while the aggregate number or coverage of related functions differs between species. [src: bacdive_metal_validation] The environmental comparisons provide ecological support for this model because contamination-associated isolates had higher metal-tolerance scores, but the strongest heavy-metal estimate used only n=10 matched isolates and had an observed d=1.00 that barely exceeded an approximately d=0.93 minimum detectable effect size at 80% power. [src: bacdive_metal_validation]

This interpretation is connected to [[concepts/within-species-resistome-heterogeneity]] and [[concepts/environmental-resistome]], because species-level conservation and divergence can be obscured when strain-level variation and environmental sampling are treated as interchangeable. [src: bacdive_metal_validation] It also refines [[concepts/genome-size-confounding-of-functional-scores]]: genome-size normalization is useful, but the remaining association between score and broader metabolic complexity remains a potential confounder. [src: bacdive_metal_validation]

The BacDive bridge itself creates an evidence limitation: 55,107 strains (56.6%) were unmatched, primarily because GTDB species boundaries differed from LPSN/DSMZ-based naming, so the observed pattern may not represent all described or environmental bacteria. [src: bacdive_metal_validation] BacDive also represents culturable, described strains rather than the full diversity of environmental bacteria, which may under-represent metal-tolerant extremophiles. [src: bacdive_metal_validation]

## Open Directions

- Match BacDive GCA accessions directly to `kbase_ke_pangenome.genome` genome IDs and test whether the environmental score gradient persists after recovering part of the 56.6% unmatched set. [src: bacdive_metal_validation]
- Compare within-species strain variation and between-species score differences using accession-linked pangenome genomes, and test whether species-level divergence explains more variance than strain-level heterogeneity. [src: bacdive_metal_validation]
- Fit genome-size- and metabolic-complexity-adjusted models using the BacDive isolation metadata and pangenome annotations to test whether contamination association remains after controlling for correlated functional capacity. [src: bacdive_metal_validation]
- Expand matched metal phenotypes beyond the 24 existing utilization records with MIC and growth-inhibition data, then test whether specific metal-tolerance gene families distinguish contamination environments. [src: bacdive_metal_validation]
- Integrate ENIGMA CORAL community data from the Oak Ridge metal-contaminated site and compare field distributions with species-level pangenome scores to test whether the pattern generalizes beyond culture collections. [src: bacdive_metal_validation]
