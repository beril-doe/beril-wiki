---
type: "Organism"
description: "Archaeal methanogen represented by Fitness Browser and SNIPE analyses"
sources: ["summaries/snipe_defense_system__REPORT.md", "summaries/truly_dark_genes__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md"]
---
# Methanococcus maripaludis

## What this entity is

**Canonical name:** Methanococcus maripaludis. [src: snipe_defense_system]  
**Known alias:** *M. maripaludis*. [src: snipe_defense_system]  
**Strains represented:** JJ and S2. [src: snipe_defense_system, conservation_vs_fitness]  
**Stable identifier reported:** SNIPE-associated locus **MMJJ_RS01635**; no organism-level stable identifier was provided in the report. [src: snipe_defense_system]

Methanococcus maripaludis is an organism represented in the [[entities/kescience-fitnessbrowser|Fitness Browser]] and the only organism in that dataset reported to contain a complete two-domain [[entities/snipe-defense-system|SNIPE]] architecture. [src: snipe_defense_system] The [[summaries/truly_dark_genes__REPORT|truly dark genes]] analysis further identifies Methanococcus strains S2 and JJ as accounting for **55% of truly dark genes**, and Methanococcus_JJ contributes **13 of the top 100** prioritized candidates. [src: truly_dark_genes] This **refines** the organism’s context: its representation in Fitness Browser also makes it a major source of unresolved gene-function candidates, although the dark-gene analysis does not establish their functions. [src: truly_dark_genes]

The conservation-versus-fitness analysis **supports** the importance of this Fitness Browser representation: Methanococcus maripaludis S2 showed the strongest essential-gene core-conservation enrichment among the compared organisms, with **OR=5.21**. [src: conservation_vs_fitness] This result applies to S2 and therefore **refines** the separate SNIPE evidence from strain JJ rather than identifying the SNIPE locus as the enriched gene set. [src: conservation_vs_fitness]

## Evidence from the SNIPE analysis

The SNIPE protein at locus MMJJ_RS01635 contained PF13250/DUF4041, PF13455/Mug113, and PF10544, providing the only complete PF13250-plus-PF13455 architecture detected among the surveyed Fitness Browser organisms. [src: snipe_defense_system] The relevant domain families are [[entities/pf13250-duf4041|PF13250/DUF4041]] and [[entities/pf13455-mug113|PF13455/Mug113]]. [src: snipe_defense_system]

The Fitness Browser provided **129 experiments** for this protein. [src: snipe_defense_system] Its minimum measured fitness was **-1.16** under formate/[[entities/acetate|acetate]] conditions, and it was dispensable under most tested conditions. [src: snipe_defense_system]

PF13455 occurred in **7 genes across 6 Fitness Browser organisms**, including Methanococcus maripaludis, but only Methanococcus maripaludis carried the complete PF13250-plus-PF13455 architecture. [src: snipe_defense_system]

## Interpretation and limitation

The Methanococcus maripaludis result demonstrates that a complete SNIPE-like domain architecture occurs in an archaeal Fitness Browser organism, but it does not establish that the Enterobacterales phage-lambda ManYZ transporter mechanism operates in archaea. [src: snipe_defense_system] The concentration of unresolved genes in Methanococcus strains **supports** prioritizing archaeal-specific annotation and experimental follow-up, but the dark-gene results do not by themselves establish horizontal transfer, gene function, or a connection to SNIPE. [src: truly_dark_genes]

The S2 conservation signal likewise indicates an association between inferred essentiality and core-genome conservation, not a strain-independent property of every Methanococcus maripaludis gene; essentiality was inferred from RB-TnSeq under the library’s represented growth conditions. [src: conservation_vs_fitness]

## Related pages

- [[summaries/snipe_defense_system__REPORT]] — source report describing the SNIPE architecture and Fitness Browser evidence. [src: snipe_defense_system]
- [[summaries/truly_dark_genes__REPORT]] — source report distinguishing annotation-lag genes from persistent hypothetical genes and prioritizing candidates. [src: truly_dark_genes]
- [[summaries/conservation_vs_fitness__REPORT]] — source report linking Fitness Browser essentiality to pangenome conservation. [src: conservation_vs_fitness]
- [[concepts/phage-defense-syndromes-and-arms-race]] — cross-project synthesis of SNIPE-mediated phage defense and its proposed transporter trade-off. [src: snipe_defense_system]
- [[entities/kescience-fitnessbrowser]] — dataset supplying the organism’s fitness measurements. [src: snipe_defense_system]
- [[entities/snipe-defense-system]] — SNIPE defense system investigated in the report. [src: snipe_defense_system]
