---
type: Gene_Or_Pathway
description: Histidine biosynthesis enrichment in AMR cofitness networks
sources:
- id: amr_cofitness_networks
  resource: ../summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
title: Histidine biosynthesis
---
# Histidine biosynthesis

## Identity

**Canonical name:** Histidine biosynthesis. [^amr_cofitness_networks]

**Known alias:** Histidine biosynthetic process. [^amr_cofitness_networks]

**Stable external identifier:** Gene Ontology term GO:0000105, linked through [gene-ontology](gene-ontology.md). [^amr_cofitness_networks]

## Evidence from AMR cofitness networks

Histidine biosynthesis was among the top Gene Ontology enrichment signals detected in antimicrobial-resistance (AMR) cofitness neighborhoods using [interproscan](interproscan.md) annotations. [^amr_cofitness_networks]

The term was enriched in 3 organisms among the analysis of terms enriched in at least 3 organisms at FDR (false discovery rate) < 0.05, with a mean odds ratio of 5.3. [^amr_cofitness_networks]

By AMR mechanism, histidine biosynthesis was enriched in 6 organisms for efflux genes and in 3 organisms for metal-resistance genes. [^amr_cofitness_networks]

Across organisms, histidine biosynthesis occurred in 68% of efflux support networks versus 30% of metal-resistance support networks, with p = 0.013 before correction and q = 0.18 after FDR correction. [^amr_cofitness_networks]

This pattern was the only reported hint of mechanism specificity among the conserved functional categories, but it was not significant after FDR correction. [^amr_cofitness_networks]

## Interpretation

The histidine-biosynthesis enrichment may reflect shared co-regulation with AMR genes, or shared dispensability under the laboratory conditions used by [kescience-fitnessbrowser](kescience-fitnessbrowser.md). [^amr_cofitness_networks]

The report specifically notes that rich or defined media with amino acid supplements can make biosynthesis pathways redundant, so the enrichment should not be treated as evidence of direct regulatory control. [^amr_cofitness_networks]

Cofitness indicates shared fitness phenotypes rather than direct transcriptional regulation, and the report identifies a fitness-matched permutation as the key test for distinguishing mechanistic co-regulation from shared dispensability. [^amr_cofitness_networks]

## Related pages

- [tryptophan-biosynthesis](tryptophan-biosynthesis.md) — another amino-acid biosynthesis category enriched in AMR cofitness neighborhoods. [^amr_cofitness_networks]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the enrichment may depend on condition-specific shared dispensability. [^amr_cofitness_networks]
- [gene-essentiality](../concepts/gene-essentiality.md) — laboratory fitness phenotypes are central to interpreting the enrichment. [^amr_cofitness_networks]
- [amr_cofitness_networks__REPORT](../summaries/amr_cofitness_networks__REPORT.md) — source report for the network analysis. [^amr_cofitness_networks]

## Open Directions

A fitness-matched permutation using random non-AMR genes with the same mean-fitness distribution should test whether histidine-biosynthesis enrichment exceeds the expectation for conditionally dispensable genes. [^amr_cofitness_networks]

Cofitness calculated separately for antibiotic and standard-growth conditions should test whether the histidine-biosynthesis signal is specific to AMR-relevant conditions. [^amr_cofitness_networks]

[^amr_cofitness_networks]: [amr cofitness networks](../summaries/amr_cofitness_networks__REPORT.md)
