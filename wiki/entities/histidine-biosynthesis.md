---
type: "Gene_Or_Pathway"
description: "Histidine biosynthesis enrichment in AMR cofitness networks"
sources: ["summaries/amr_cofitness_networks__REPORT.md"]
---
# Histidine biosynthesis

## Identity

**Canonical name:** Histidine biosynthesis. [src: amr_cofitness_networks]

**Known alias:** Histidine biosynthetic process. [src: amr_cofitness_networks]

**Stable external identifier:** Gene Ontology term GO:0000105, linked through [[entities/gene-ontology]]. [src: amr_cofitness_networks]

## Evidence from AMR cofitness networks

Histidine biosynthesis was among the top Gene Ontology enrichment signals detected in antimicrobial-resistance (AMR) cofitness neighborhoods using [[entities/interproscan]] annotations. [src: amr_cofitness_networks]

The term was enriched in 3 organisms among the analysis of terms enriched in at least 3 organisms at FDR (false discovery rate) < 0.05, with a mean odds ratio of 5.3. [src: amr_cofitness_networks]

By AMR mechanism, histidine biosynthesis was enriched in 6 organisms for efflux genes and in 3 organisms for metal-resistance genes. [src: amr_cofitness_networks]

Across organisms, histidine biosynthesis occurred in 68% of efflux support networks versus 30% of metal-resistance support networks, with p = 0.013 before correction and q = 0.18 after FDR correction. [src: amr_cofitness_networks]

This pattern was the only reported hint of mechanism specificity among the conserved functional categories, but it was not significant after FDR correction. [src: amr_cofitness_networks]

## Interpretation

The histidine-biosynthesis enrichment may reflect shared co-regulation with AMR genes, or shared dispensability under the laboratory conditions used by [[entities/kescience-fitnessbrowser]]. [src: amr_cofitness_networks]

The report specifically notes that rich or defined media with amino acid supplements can make biosynthesis pathways redundant, so the enrichment should not be treated as evidence of direct regulatory control. [src: amr_cofitness_networks]

Cofitness indicates shared fitness phenotypes rather than direct transcriptional regulation, and the report identifies a fitness-matched permutation as the key test for distinguishing mechanistic co-regulation from shared dispensability. [src: amr_cofitness_networks]

## Related pages

- [[entities/tryptophan-biosynthesis]] — another amino-acid biosynthesis category enriched in AMR cofitness neighborhoods. [src: amr_cofitness_networks]
- [[concepts/condition-specific-fitness]] — the enrichment may depend on condition-specific shared dispensability. [src: amr_cofitness_networks]
- [[concepts/gene-essentiality]] — laboratory fitness phenotypes are central to interpreting the enrichment. [src: amr_cofitness_networks]
- [[summaries/amr_cofitness_networks__REPORT]] — source report for the network analysis. [src: amr_cofitness_networks]

## Open Directions

A fitness-matched permutation using random non-AMR genes with the same mean-fitness distribution should test whether histidine-biosynthesis enrichment exceeds the expectation for conditionally dispensable genes. [src: amr_cofitness_networks]

Cofitness calculated separately for antibiotic and standard-growth conditions should test whether the histidine-biosynthesis signal is specific to AMR-relevant conditions. [src: amr_cofitness_networks]
