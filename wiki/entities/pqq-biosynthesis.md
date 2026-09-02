---
type: "Gene_Or_Pathway"
description: "PQQ biosynthesis pathway and its condition-specific, ecological, and pangenome evidence"
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md"]
---
# PQQ Biosynthesis

## What this entity is

**Canonical name:** PQQ biosynthesis. [src: adp1_deletion_phenotypes]

**Known aliases:** No aliases are reported in the source document. [src: adp1_deletion_phenotypes]

**Stable external identifier:** None is provided in the source document. [src: adp1_deletion_phenotypes]

PQQ biosynthesis is a pathway that produces pyrroloquinoline quinone, a cofactor used by PQQ-dependent dehydrogenases. [src: adp1_deletion_phenotypes]

## Evidence from ADP1 carbon-source phenotypes

PQQ biosynthesis genes, including **pqqC** and **pqqD**, are among the condition-specific genes selected by quinate growth phenotypes and are associated with [[entities/quinate-degradation-pathway]]. [src: adp1_deletion_phenotypes]

PQQ biosynthesis genes are condition-specific for both quinate and glucose, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [src: adp1_deletion_phenotypes]

The glucose-associated pathway includes glucose dehydrogenase (PQQ) and the [[entities/entner-doudoroff-pathway]], while the quinate-associated pathway is linked to [[entities/quinate]] degradation. [src: adp1_deletion_phenotypes]

The report identifies 625 genes, representing 31% of the complete matrix, with a condition-specificity score of at least 1.0; PQQ biosynthesis is part of the pathway-level structure observed among these condition-specific phenotypes. [src: adp1_deletion_phenotypes]

The complete growth matrix measured 2,034 genes across 8 carbon sources, and the PQQ-related condition-specificity results were obtained from this matrix. [src: adp1_deletion_phenotypes]

The aromatic-catabolism analysis **supports** the shared quinate and glucose interpretation: it identifies 2 PQQ-biosynthesis genes in the 51-gene quinate support network and reports that quinate dehydrogenase (quiA) requires the PQQ cofactor. [src: aromatic_catabolism_network]

It also **supports** the quinate association with prior transcriptomic evidence that 4/5 PQQ-biosynthesis genes are upregulated on quinate versus succinate. [src: aromatic_catabolism_network]

## Evidence across genomes and environments

The PGP pangenome analysis **supports and broadens** the condition-specific evidence by finding that **pqqC** was present in 11,272 of 27,702 species carrying at least one of 13 PGP markers, within an analysis of 32,736 PGP gene clusters. [src: pgp_pangenome_ecology]

Across the pangenome, pqqC was 81.5% core, 7.8% auxiliary, and 10.7% singleton, while pqqD was 55.5% core, 17.0% auxiliary, and 27.5% singleton. These distributions **refine** the earlier ADP1 phenotype interpretation: PQQ-associated genes can be conditionally important in a model organism while also commonly residing in conserved genomic components, with pqqD a partial exception that may sometimes spread as a standalone gene. [src: pgp_pangenome_ecology]

PQQ-associated genes also showed ecological structure: pqqC co-occurred positively with **acdS** (OR = 7.24, n = 286 co-occurring species, q = 1.2e-83), and pqqC was enriched in soil/rhizosphere species at 43.8% versus 21.2% in other species (OR = 2.90, q = 2.8e-53). These findings **support** a specialized, predominantly non-diazotrophic rhizosphere PGP module rather than contradicting the carbon-source-specific role observed in ADP1. [src: pgp_pangenome_ecology]

## Evidence from the lanthanide methylotrophy atlas

The 293,059-genome atlas **refines** the ADP1-centered evidence by evaluating PQQ markers alongside xoxF and mxaF methanol dehydrogenases across diverse taxa. Among 2,320 xoxF-bearing genomes initially lacking any eggNOG PQQ annotation, 33 had complete eggNOG pqqA-E calls, 1,472 had partial calls covering 1–4 genes, 899 had strong Bakta-only evidence with at least 3 PQQ products, 389 had Bakta-only partial evidence with 1–2 products, and 897 had no PQQ detected by either source. [src: lanthanide_methylotrophy_atlas]

This **supports** annotation-gap concerns rather than demonstrating universal absence of PQQ: among 2,185 genomes with no eggNOG PQQ annotation, 1,288 (59 %) had at least 1 Bakta PQQ product, while 897 genomes, equal to 24 % of all xoxF carriers, lacked evidence from either source. [src: lanthanide_methylotrophy_atlas]

The 897 genomes are candidates for assembly incompleteness, pseudogenization, or genuine reliance on community-acquired PQQ; sequence-level analysis is required to distinguish these possibilities. [src: lanthanide_methylotrophy_atlas]

## Interpretation and limitations

The shared quinate and glucose association supports the interpretation that PQQ biosynthesis contributes to carbon-source-specific oxidation requirements in [[entities/acinetobacter-baylyi-adp1]]. [src: adp1_deletion_phenotypes]

The new atlas evidence **refines** this interpretation by showing that PQQ-marker detection is source-dependent and that PQQ-associated oxidation potential extends beyond the ADP1 carbon-source context, while annotation evidence alone does not establish pathway activity. [src: lanthanide_methylotrophy_atlas]

The source notes that growth ratios were single-timepoint measurements with unknown technical noise, so condition-specificity scores may reflect measurement error as well as biological effects. [src: adp1_deletion_phenotypes]

The source does not establish that PQQ biosynthesis genes are essential under every tested condition, because the analysis concerns condition-dependent growth phenotypes rather than a universal essentiality classification. [src: adp1_deletion_phenotypes]

The pangenome results likewise do not establish that every annotated pqqC or pqqD cluster is functional: PGP cluster annotations were not functionally validated, and truncations, frameshifts, and pseudogenization were not filtered. [src: pgp_pangenome_ecology]

Future validation should assess ORF integrity and genome completeness, for example with CheckM2, in the 897 xoxF genomes lacking PQQ evidence. [src: lanthanide_methylotrophy_atlas]

## Related source

The evidence summarized here is from [[summaries/adp1_deletion_phenotypes__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], [[summaries/lanthanide_methylotrophy_atlas__REPORT]], and [[summaries/pgp_pangenome_ecology__REPORT]]. [src: adp1_deletion_phenotypes, aromatic_catabolism_network, lanthanide_methylotrophy_atlas, pgp_pangenome_ecology]
