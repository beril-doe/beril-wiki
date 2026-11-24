---
type: "Gene_Or_Pathway"
description: "Amino acid biosynthesis pathways enriched in AMR support networks, strongest for efflux genes."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md"]
aliases: ["amino acid biosynthesis"]
---
# Histidine and tryptophan biosynthesis

This page covers histidine and tryptophan biosynthesis (also called amino acid biosynthesis) in antimicrobial resistance (AMR) support networks. Both Gene Ontology (GO) categories are enriched in AMR cofitness networks, and enrichment is strongest for efflux genes. [src: amr_cofitness_networks] The evidence comes from one cofitness analysis, [[summaries/amr_cofitness_networks__REPORT]], and the digest [[summaries/discoveries]] repeats it. The mechanism-specific part is only a hint after multiple-testing correction. [src: amr_cofitness_networks]

## Key facts

- GO:0000105, histidine biosynthesis, is enriched in AMR support networks in 3 organisms (false discovery rate, FDR<0.05), with mean odds ratio (OR) 5.3. [src: amr_cofitness_networks]
- GO:0000162, tryptophan biosynthesis, is enriched in 3 organisms (FDR<0.05), with mean OR 5.3. [src: amr_cofitness_networks]
- The digest reports the same result for a cofitness analysis of 801 AMR genes across 28 organisms: AMR cofitness neighborhoods are enriched for histidine biosynthesis (3 organisms). [src: discoveries]
- It reports the same for tryptophan biosynthesis (3 organisms). [src: discoveries]
- Amino acid biosynthesis (30–73%) forms a second tier of AMR support-network conservation. [src: amr_cofitness_networks]

## Mechanism specificity

Efflux AMR genes show the strongest amino acid biosynthesis enrichment, with histidine in 6 organisms and tryptophan in 5. [src: amr_cofitness_networks] See [[entities/efflux-pumps]]. In the mechanism-specific GO analysis, 212 of 9,244 tests were significant at FDR<0.05. The top signal was efflux histidine biosynthesis in 6 organisms. [src: amr_cofitness_networks]

This specificity is weak. Histidine biosynthesis shows only a hint of mechanism specificity: efflux 68% versus metal 30%, p = 0.013 uncorrected, q = 0.18 after FDR. [src: amr_cofitness_networks] The efflux-specific enrichment therefore does not survive correction as a mechanism difference. [src: amr_cofitness_networks]

## Context

For the wider composition of support networks, see [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]]. [src: amr_cofitness_networks]
