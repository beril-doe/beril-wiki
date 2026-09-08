---
type: Gene_Or_Pathway
description: Bacterial chemotaxis signaling associated with AMR cofitness neighborhoods.
sources:
- id: amr_cofitness_networks
  resource: ../summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
title: Bacterial chemotaxis
---
# Bacterial chemotaxis

## What this entity is

**Canonical name:** Bacterial chemotaxis

**Known aliases:** Chemotaxis

**Stable external identifier:** Not specified in the source report. [^amr_cofitness_networks]

Bacterial chemotaxis is a signaling pathway that enables bacteria to respond to chemical gradients; in this report, it is represented through functional enrichment of genes in antimicrobial-resistance (AMR) cofitness neighborhoods. [^amr_cofitness_networks]

## Evidence from AMR cofitness networks

In the analysis of 28 organisms, metal-resistance genes showed stronger enrichment for chemotaxis than other AMR mechanisms in 4 organisms. [^amr_cofitness_networks]

No Gene Ontology (GO) term was significantly mechanism-specific after false discovery rate (FDR) correction, so the chemotaxis pattern does not establish a metal-resistance-specific association. [^amr_cofitness_networks]

The report interprets chemotaxis enrichment as consistent with two alternatives: shared regulation through signaling networks, or shared dispensability under the laboratory conditions used by the Fitness Browser. [^amr_cofitness_networks]

Because Fitness Browser experiments generally use shaken liquid culture, chemotaxis may be unnecessary under some tested conditions; this makes shared laboratory dispensability a plausible explanation, but not a demonstrated one. [^amr_cofitness_networks]

The report identifies fitness-matched permutations, condition-specific cofitness analyses, and direct assessment of mean fitness for chemotaxis-related knockouts as follow-up work needed to distinguish mechanistic co-regulation from shared dispensability. [^amr_cofitness_networks]

## Related pages

- [amr_cofitness_networks__REPORT](../summaries/amr_cofitness_networks__REPORT.md) — source report on AMR cofitness support networks. [^amr_cofitness_networks]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — interpretation of cofitness as condition-specific shared fitness phenotypes. [^amr_cofitness_networks]
- [gene-essentiality](../concepts/gene-essentiality.md) — laboratory-condition fitness phenotypes and dispensability. [^amr_cofitness_networks]
- [flagellar-motility](flagellar-motility.md) — another signaling- and motility-related enrichment category examined in the report. [^amr_cofitness_networks]
- [interproscan](interproscan.md) — annotation resource used for the GO enrichment analysis. [^amr_cofitness_networks]

[^amr_cofitness_networks]: [amr cofitness networks](../summaries/amr_cofitness_networks__REPORT.md)
