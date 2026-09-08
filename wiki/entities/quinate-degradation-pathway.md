---
type: Gene_Or_Pathway
description: Aromatic pathway converting quinate and protocatechuate to TCA-cycle
  intermediates
sources:
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: aromatic_catabolism_network
  resource: ../summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Quinate and Protocatechuate Degradation Pathway
---
# Quinate and Protocatechuate Degradation Pathway

## What this entity is

**Canonical name:** Quinate and Protocatechuate Degradation Pathway. [^adp1_deletion_phenotypes]

**Known aliases:** Quinate/protocatechuate pathway; aromatic degradation pathway. [^adp1_deletion_phenotypes]

**Stable external identifier:** No stable external identifier is reported in the source document. [^adp1_deletion_phenotypes]

This pathway is the aromatic-catabolism system required for growth on quinate and protocatechuate in *Acinetobacter baylyi* ADP1. [^adp1_deletion_phenotypes] The core route converts quinate through protocatechuate and β-ketoadipate to succinyl-CoA and acetyl-CoA, which enter the TCA cycle. [^aromatic_catabolism_network]

The network analysis **supports** this pathway-level interpretation by placing the core route within a 51-gene quinate-specific support network spanning aromatic degradation, respiratory Complex I, iron acquisition, PQQ biosynthesis, and transcriptional regulation. [^aromatic_catabolism_network]

## Evidence from the deletion phenotype analysis

A small discrete module of 24 genes showed extreme quinate-specific defects, with a mean quinate z-score of -7.28 and near-zero scores on the other tested conditions; these genes were identified as aromatic degradation pathway genes. [^adp1_deletion_phenotypes]

Quinate was the most robust of the eight tested carbon sources overall, with only 1.6% of genes showing severe defects at a growth ratio below 0.5 and a mean growth ratio of 1.36. [^adp1_deletion_phenotypes]

The quinate-specific gene set contained 51 genes with specificity greater than 0.5 and z-score below -1. [^adp1_deletion_phenotypes] The network analysis **refines** this result by assigning 44/51 genes (86%) to four functional subsystems: 8 aromatic-pathway genes, 21 Complex I genes, 7 iron-acquisition genes, and 2 PQQ-biosynthesis genes; 6 additional genes are transcriptional regulators and 7 remain unassigned. [^aromatic_catabolism_network]

The top quinate-associated genes included **pcaC**, **pcaG**, **pcaH**, **pcaB**, **quiA**, **quiB**, **pqqC**, and **pqqD**, linking the phenotype to protocatechuate/quinate degradation and [pqq-biosynthesis](pqq-biosynthesis.md). [^adp1_deletion_phenotypes]

The analysis found that [pqq-biosynthesis](pqq-biosynthesis.md) genes were condition-specific for both quinate and glucose, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [^adp1_deletion_phenotypes] The new analysis **supports** the biochemical interpretation that quinate dehydrogenase QuiA requires PQQ, while noting that PQQ dependence is not exclusively aromatic because these genes also appear as glucose-specific in the deletion analysis. [^aromatic_catabolism_network]

The quinate-specific set also included NADH-ubiquinone oxidoreductase subunits from respiratory Complex I, suggesting the hypothesis that aromatic catabolism creates distinctive electron-transport-chain demands rather than establishing that mechanism as a direct causal result. [^adp1_deletion_phenotypes] The network analysis **strengthens** this hypothesis: Complex I accounts for 21/51 quinate-specific genes, and 10/13 Complex I operon subunits independently produce quinate-specific growth defects, although the report cautions that cross-species fitness evidence does not isolate aromatic catabolism from high NADH flux. [^aromatic_catabolism_network]

The respiratory-chain wiring analysis **supports** the association between this pathway and Complex I by reporting that quinate requires Complex I while cytochrome bo3, cytochrome bd, succinate dehydrogenase, and all other listed respiratory components are dispensable. [^respiratory_chain_wiring] It further **refines** the interpretation from total reducing-equivalent yield to flux configuration: quinate produces 4 total NADH, or 0.57 NADH per carbon, and has a Complex I growth ratio of 0.37. [^respiratory_chain_wiring] The proposed explanation is that β-ketoadipate cleavage produces succinyl-CoA and acetyl-CoA simultaneously, creating a concentrated TCA-cycle NADH burst that may exceed NDH-2 reoxidation capacity; this is a biochemical hypothesis based on theoretical stoichiometry, not measured flux distributions. [^respiratory_chain_wiring]

The same analysis **supports** an iron requirement within the pathway because protocatechuate 3,4-dioxygenase PcaGH requires non-heme Fe²⁺ for ring cleavage. [^aromatic_catabolism_network]

## Relation to broader phenotype architecture

The 24-gene quinate module was the only discrete phenotypic module identified in the eight-condition deletion matrix; the remaining gene profiles were interpreted as a continuous condition-dependent essentiality gradient. [^adp1_deletion_phenotypes]

The analysis identified 625 genes, representing 31% of the complete matrix, with a condition-specificity score of at least 1.0, and quinate selected a pathway-level subset of these genes. [^adp1_deletion_phenotypes]

The quinate/protocatechuate pathway specificity agrees with Fischer et al. (2008), although the source characterizes this comparison as interpretive support rather than a new direct measurement of pathway flux. [^adp1_deletion_phenotypes]

The new report **refines** the pathway’s architecture by showing genomic independence with metabolic coupling: the Complex I operon lies at 714–729 kb, the pca/qui pathway at 1,709–1,724 kb, PQQ biosynthesis at 2,461 kb, and iron-acquisition genes across 4 loci, with no cross-category operons identified. [^aromatic_catabolism_network] The pca/qui region forms a 12-gene operon spanning pcaIJFBDCHG-quiABC plus transport genes. [^aromatic_catabolism_network]

Co-fitness analysis further **extends** the pathway-associated gene set by assigning 16 of 23 initially Other or Unknown genes to support subsystems; ACIAD3137 and ACIAD2176 correlate with Complex I genes at r > 0.98 and are candidate uncharacterized Complex I accessory factors. [^aromatic_catabolism_network] These assignments remain provisional because the analysis uses only 8 conditions and 8-dimensional growth vectors. [^aromatic_catabolism_network]

The respiratory-chain study also **qualifies** the apparent pathway–Complex I relationship: ADP1 contains three parallel NADH dehydrogenases, but FBA predicts zero flux through NDH-2 and ACIAD3522 on standard media because growth optimization routes NADH through the ATP-favorable Complex I pathway. [^respiratory_chain_wiring] Thus, the observed quinate requirement may reflect respiratory capacity constraints that are not represented by the optimized model. [^respiratory_chain_wiring]

## Related pages

- [pqq-biosynthesis](pqq-biosynthesis.md) — biosynthetic genes associated with both quinate and glucose phenotypes. [^adp1_deletion_phenotypes]
- [beta-ketoadipate-pathway](beta-ketoadipate-pathway.md) — the central aromatic-catabolism route surrounding this pathway. [^aromatic_catabolism_network]
- [complex-i](complex-i.md) — the respiratory support subsystem implicated by quinate-specific defects. [^aromatic_catabolism_network]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the cross-condition framework in which quinate-specific requirements were identified. [^adp1_deletion_phenotypes]
- [gene-essentiality](../concepts/gene-essentiality.md) — the essentiality interpretation of the quinate-specific deletion defects. [^adp1_deletion_phenotypes]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — model limitations in representing alternative respiratory flux. [^respiratory_chain_wiring]
- [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md) — source summary for the complete deletion-collection analysis. [^adp1_deletion_phenotypes]
- [aromatic_catabolism_network__REPORT](../summaries/aromatic_catabolism_network__REPORT.md) — source summary for the integrated 51-gene support-network analysis. [^aromatic_catabolism_network]
- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — source summary for condition-specific respiratory-chain configuration in ADP1. [^respiratory_chain_wiring]

## Evidence limitations

The growth ratios were single-timepoint measurements with unknown technical noise, so some quinate-specificity scores may reflect measurement error as well as biology. [^adp1_deletion_phenotypes]

The complete matrix contained 2,034 genes and excluded 499 essential genes plus 316 genes with incomplete data, limiting pathway conclusions to genes represented by successful deletion measurements. [^adp1_deletion_phenotypes]

Only 8 carbon sources were tested, so the pathway’s apparent condition specificity may change when additional growth conditions are measured. [^adp1_deletion_phenotypes]

The new network analysis **qualifies** the Complex I interpretation: its model records 1.76× higher Complex I flux on aromatic substrates, with fluxes of 0.55 versus 0.31, but predicts 0% essentiality, and 30/51 quinate-specific genes have no FBA reaction mappings. [^aromatic_catabolism_network] The co-fitness matrix has limited resolution, and 11 non-core Complex I assignments may be indirect rather than physical associations. [^aromatic_catabolism_network]

The respiratory-chain interpretation remains provisional because the stoichiometric explanation uses theoretical rather than measured flux distributions; NDH-2 has no growth data; the cross-species comparison had only 4 organisms without NDH-2 and was underpowered; annotation variation may cause missed NDH-2 orthologs; and ACIAD3522 may not be a true respiratory NADH dehydrogenase. [^respiratory_chain_wiring] Text matching also produced likely false-positive NDH-2 calls, while the planned pangenome KO co-occurrence analysis was not performed. [^respiratory_chain_wiring]

The reports propose testing NDH-2 deletion on quinate versus glucose, measuring NADH/NAD⁺ ratios on each carbon source, experimentally validating ACIAD3137 and ACIAD2176, expanding conditions to benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors, adding PQQ, iron-homeostasis, and respiratory-capacity constraints to the ADP1 FBA model, expanding cross-species K03885 and K00330–K00343 analysis across 27K species, characterizing ACIAD3522, and reanalyzing quinate-versus-succinate proteomics for respiratory-chain proteins. [^aromatic_catabolism_network] [^respiratory_chain_wiring]

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^aromatic_catabolism_network]: [aromatic catabolism network](../summaries/aromatic_catabolism_network__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
