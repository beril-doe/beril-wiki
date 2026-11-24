---
type: "Concept"
description: "Evidence on prophage-borne anti-defense genes: their environmental enrichment, genomic placement away from the prophage backbone and the arms-race interpretation; stops at defense-system biology outside prophages."
sources: ["summaries/prophage_ecology__REPORT.md"]
---
# Prophage anti-defense genes and host-phage arms races

Prophage anti-defense genes (module G in the prophage ecology report) are the most environmentally responsive prophage module. They are enriched in human-associated bacteria and depleted in freshwater and animal-associated bacteria, and this holds after controlling for host family composition and genome size. [src: prophage_ecology] Their genomic placement is scattered, which the report reads as defense islands separate from the prophage backbone. [src: prophage_ecology] The arms-race reading is the report's interpretation. The report proposes a direct co-localization test but did not run it. [src: prophage_ecology]

## Prevalence and environmental enrichment

Anti-defense module G occurs in 64.3% of bacterial species in the KBase Data Lakehouse pangenome. It is among the modules with the most phylogenetic and environmental variation. [src: prophage_ecology] Its prevalence ranges from 3.1% in Patescibacteria to 97.8% in Campylobacterota. [src: prophage_ecology] A chi-squared test found a significant environment association for G_anti_defense (chi2=818, p=2.58e-170). [src: prophage_ecology]

Anti-Defense was enriched in human-associated and human-clinical bacteria and depleted in freshwater and animal-associated bacteria, relative to a null that constrains phylogeny and genome size. Each row gives log2(OR) and Z-score, where OR = odds ratio. [src: prophage_ecology] See [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny]] for the wider framework.

| Environment | log2(OR) | Z-score | Result |
|---|---|---|---|
| human_associated | 1.70 | 8.76 | Enriched [src: prophage_ecology] |
| human_clinical | 0.14 | 5.14 | Enriched [src: prophage_ecology] |
| freshwater | -0.74 | -4.74 | Depleted [src: prophage_ecology] |
| animal_associated | -0.24 | -8.77 | Depleted [src: prophage_ecology] |

Host-associated environments show increases specifically in prophage structural completeness and anti-defense repertoire. The report states this goes beyond an increase in lysogeny. [src: prophage_ecology]

## Genomic placement

For module G, the report gives a mean contig co-localization of 0.281, with 3/11 species tests significant and a mean Z-score of 1.50. It summarizes this as weak co-occurrence and scattered genomic placement. [src: prophage_ecology] The report reads this as consistent with defense islands separate from the core prophage backbone. [src: prophage_ecology] It cites Pinilla-Redondo et al. (2020) and Rahimian et al. (2026), who found that anti-defense and defense systems co-localize into defense islands genomically distinct from the core prophage. [src: prophage_ecology] See [[concepts/modular-architecture-and-co-occurrence-of-prophage-genes]] for the module structure.

## Arms-race interpretation

Tesson et al. (2024) found that 89% of anti-defense systems localize in mobile genetic elements, predominantly prophages. [src: prophage_ecology] Bernheim & Sorek (2020) proposed a pan-immune system model in which defense system diversity drives counter-defense evolution. [src: prophage_ecology] The report suggests that human-associated bacteria face more intense phage-mediated selective pressure. It proposes this drives retention of complete prophage lytic machinery and counter-defense genes. [src: prophage_ecology] It also suggests that depletion in freshwater and animal-associated bacteria means arms races are most intense in human-associated niches. In its account, CRISPR-Cas and restriction-modification systems are under stronger selection there. [src: prophage_ecology] These are interpretations of enrichment patterns, not direct measurements of selection. The report's own test of the genomic arms-race hypothesis is still to be done. [src: prophage_ecology]

## Open Directions

- Test whether module G anti-defense genes co-localize with defense system genes in the same genomes. This would check the defense-island reading, which currently rests on low co-localization of 0.281 and on prior literature.
- Compare defense-system repertoire and anti-defense repertoire per genome across human-associated and freshwater bacteria. This would test whether the enrichment tracks defense diversity, as the pan-immune model predicts.
- Measure how the enrichment varies within lineages that are high (Campylobacterota) or low (Patescibacteria) in module G prevalence. This would show whether the environmental signal holds within single clades.
