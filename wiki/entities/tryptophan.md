---
type: "Compound"
description: "Aromatic amino acid that FW300-N2E3 produces but whose species-level catabolism is absent in BacDive."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["L-tryptophan"]
---
# Tryptophan

Tryptophan (L-tryptophan) is an aromatic amino acid. In the report on [[entities/pseudomonas-fluorescens-fw300-n2e3|Pseudomonas FW300-N2E3]], it is the one metabolite with enough BacDive data for a confident conclusion, and the report calls it the most robust discordance in that dataset. [src: fw300_metabolic_consistency] The strain produces tryptophan, but BacDive shows no species-level catabolism. The overflow explanation is the report's hypothesis, not a tested result. [src: fw300_metabolic_consistency] See also [[concepts/metabolite-production-versus-utilization-discordance]].

## Key facts

- FW300-N2E3 increases tryptophan in its exometabolome in Web of Microbes (WoM, action = I). [src: fw300_metabolic_consistency]
- The strain has 231 genes with significant fitness when grown on tryptophan in the Fitness Browser (FB). [src: fw300_metabolic_consistency]
- GapMind predicts a complete tryptophan biosynthesis pathway in the strain. [src: fw300_metabolic_consistency]
- 0 of 50 *P. fluorescens* strains in BacDive can use tryptophan as a carbon source. The report rates this high confidence (n=50, per-strain consensus). [src: fw300_metabolic_consistency]
- The report's summary table lists tryptophan as Increased in WoM, with BacDive counts 0+/50-, High confidence (n=50), and reads it as a robust overflow/cross-feeding signal. [src: fw300_metabolic_consistency]
- The report says only tryptophan (n=52) has sufficient BacDive data for a confident conclusion. [src: fw300_metabolic_consistency] This caveat limits every other metabolite comparison in that report.
- The WoM tryptophan (action I) entry is linked to the Fitness Browser condition L-Tryptophan as nitrogen source. [src: webofmicrobes_explorer] See [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]].

## The discordance

The report says the organism produces tryptophan and grows on it as a sole carbon source, but the species as a whole cannot catabolize it. [src: fw300_metabolic_consistency] The report reads the 231 fitness-important genes as complex regulatory and transport machinery rather than simple catabolism. It calls this consistent with a secretion or signaling role. [src: fw300_metabolic_consistency] Related concepts are [[concepts/metabolic-capability-versus-fitness-dependency]] and [[concepts/reliability-of-species-level-bacdive-consensus-phenotypes]].

## Overflow and cross-feeding hypothesis

The report proposes a tryptophan overflow hypothesis. It rests on four databases: production in WoM, genetic importance for growth in FB, a complete biosynthetic pathway in GapMind, and universal non-utilizability at species level in BacDive. [src: fw300_metabolic_consistency] The pattern is consistent with overflow metabolism serving a cross-feeding or signaling function rather than a catabolic one. [src: fw300_metabolic_consistency]

The report interprets secretion by a prototroph that cannot re-assimilate tryptophan as a hallmark of cross-feeding potential for auxotrophic community members. [src: fw300_metabolic_consistency] It cites Ramoneda et al. (2023), who found tryptophan auxotrophy particularly common across thousands of bacterial genomes. The report says this creates niches for tryptophan-producing prototrophs such as FW300-N2E3. [src: fw300_metabolic_consistency] It also says the finding aligns with Fritts et al. (2021), a review of extracellular metabolism as a driver of cross-feeding. It adds Sibanyoni et al. (2025), who documented amino acid cross-feeding between *Priestia megaterium* and *P. fluorescens* in the rhizosphere. [src: fw300_metabolic_consistency]

Source summaries: [[summaries/fw300_metabolic_consistency__REPORT]], [[summaries/webofmicrobes_explorer__REPORT]].
