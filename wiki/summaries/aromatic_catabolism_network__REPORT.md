---
type: Summary
description: ADP1 aromatic catabolism depends on a 51-gene support network.
doc_type: short
full_text: ../sources/aromatic_catabolism_network__REPORT.md
title: Aromatic Catabolism Support Network in ADP1
sources:
- id: aromatic_catabolism_network
  resource: ../sources/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
---
# Aromatic Catabolism Support Network in ADP1

## Overview

This report defines a 51-gene support network for quinate catabolism in *Acinetobacter baylyi* ADP1. The network surrounds the [beta-ketoadipate-pathway](../entities/beta-ketoadipate-pathway.md) and spans core aromatic degradation, Complex I / NADH dehydrogenase, iron acquisition, PQQ biosynthesis, and transcriptional regulation. The analysis combines growth phenotypes, flux-balance analysis (FBA), genomic organization, co-fitness correlations, and cross-species ortholog-transferred fitness data. [^aromatic_catabolism_network]

## Key Findings

### A 51-gene support network

The 51 quinate-specific genes organize into a coherent dependency network around the β-ketoadipate pathway. Co-fitness analysis assigns 44/51 genes (86%) to four functional subsystems: 8 aromatic-pathway genes, 21 Complex I genes, 7 iron-acquisition genes, and 2 PQQ-biosynthesis genes; 6 additional genes are transcriptional regulators and 7 remain unassigned. The core pathway converts quinate through protocatechuate and β-ketoadipate to succinyl-CoA and acetyl-CoA, which enter the TCA cycle. [^aromatic_catabolism_network]

The biochemical rationale is that quinate dehydrogenase (quiA) requires the PQQ cofactor, protocatechuate 3,4-dioxygenase (pcaGH) requires non-heme Fe²⁺ for ring cleavage, and TCA-cycle oxidation generates NADH that must be reoxidized by respiratory machinery. [^aromatic_catabolism_network]

### Complex I is the largest support subsystem and an FBA blind spot

Complex I, or NADH:ubiquinone oxidoreductase, accounts for 21/51 quinate-specific genes (41%) and is the largest support subsystem. FBA captures 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31, but predicts 0% essentiality. The model therefore detects increased respiratory demand without identifying Complex I as a bottleneck. [^aromatic_catabolism_network]

A total of 30/51 quinate-specific genes have no FBA reaction mappings. These unmapped genes include cofactor-supply, iron-acquisition, regulatory, and newly identified Complex I-associated functions, showing that the model represents core metabolism more completely than the infrastructure required to support it. [^aromatic_catabolism_network]

The report interprets this discrepancy as a limitation of growth-optimizing linear programming: FBA can redistribute flux through alternative routes, whereas Complex I is a single multi-subunit complex whose disruption can eliminate complex function. This interpretation is supported by the observation that 10/13 Complex I operon subunits independently produce quinate-specific growth defects. [^aromatic_catabolism_network]

### Genomic independence with metabolic coupling

The support subsystems occupy distinct chromosomal regions rather than a shared genomic neighborhood. The Complex I operon lies at 714–729 kb, the pca/qui pathway at 1,709–1,724 kb, PQQ biosynthesis at 2,461 kb, and iron-acquisition genes are scattered across 4 loci. No cross-category operons were identified, except within the aromatic pathway itself. [^aromatic_catabolism_network]

The Complex I operon contains 13 nuoA–N subunits on the same strand with <100 bp intergenic distances. The pca/qui region forms a 12-gene operon spanning pcaIJFBDCHG-quiABC plus transport genes. Across the chromosome, 9 genomic clusters contain ≥2 quinate-specific genes, with mild overall clustering expressed as an observed/expected nearest-neighbor distance ratio of 0.89. [^aromatic_catabolism_network]

### Co-fitness assigns previously unknown genes

Of 23 genes initially categorized as Other or Unknown, co-fitness assigns 16 to support subsystems with medium or high confidence. Two DUF-domain proteins, ACIAD3137 (UPF0234) and ACIAD2176 (DUF2280), correlate with Complex I genes at r > 0.98 and are candidate uncharacterized Complex I accessory factors. Within-category correlations are higher than between-category correlations, with mean r = 0.992 for Complex I and r = 0.961 for the aromatic pathway. [^aromatic_catabolism_network]

The co-fitness analysis also recovered pcaC, a 4-carboxymuconolactone decarboxylase that was initially miscategorized by keyword matching. However, the analysis uses only 8 conditions and 8-dimensional growth vectors, limiting the resolution of gene-gene correlations; the 11 Complex I-associated assignments beyond the core nuo operon are based on phenotypic correlation and may represent indirect connections rather than physical association. [^aromatic_catabolism_network]

### Complex I dependence tracks NADH-generating substrates

Ortholog-transferred fitness data from the [kescience-fitnessbrowser](../entities/kescience-fitnessbrowser.md) contains 12,241 entries covering 2,005 genes and 13 conditions. Complex I orthologs have significantly worse fitness on aromatic conditions than on the comparison conditions, with mean fitness values of -1.35 versus -0.77 and Mann-Whitney p < 0.0001. [^aromatic_catabolism_network]

Per-condition analysis refines this result: the largest Complex I defects relative to background occur on acetate (-1.55) and succinate (-1.39), which are non-aromatic substrates that also generate high NADH flux through the TCA cycle. Complex I fitness is reported as dispensable on glucose and lactate, consistent with the hypothesis that an alternative NADH dehydrogenase, NDH-2, compensates under lower NADH flux. [^aromatic_catabolism_network]

The cross-species evidence is not definitive for ADP1 because the transferred data mixes organisms with different respiratory-chain architectures. Direct Complex I fitness measurements on aromatic substrates in a single organism would provide a stronger test of whether the dependency is caused by aromatic catabolism itself or by high NADH flux. [^aromatic_catabolism_network]

### Relation to established pathway biology

The PQQ and iron dependencies are consistent with established biochemistry: PQQ-dependent quinate dehydrogenases require PQQ, and protocatechuate 3,4-dioxygenase is a non-heme Fe²⁺-dependent intradiol ring-cleavage enzyme. In ADP1, the growth-phenotype specificity of PQQ genes is consistent with prior transcriptomic evidence that 4/5 PQQ-biosynthesis genes are upregulated on quinate versus succinate. [^aromatic_catabolism_network]

The report presents the Complex I dependency as its novel finding. Bacterial respiratory chains can contain both proton-pumping Complex I (NDH-1) and non-pumping NDH-2; the proposed interpretation is that NDH-2 can substitute under lower NADH flux but cannot match Complex I capacity under high flux. [^aromatic_catabolism_network]

## Caveats and Open Directions

The PQQ dependency is not exclusively aromatic: PQQ-biosynthesis genes also appear as glucose-specific in the adp1_deletion_phenotypes project, where they are associated with PQQ-dependent glucose dehydrogenase. [^aromatic_catabolism_network]

The 8-condition co-fitness matrix provides approximately 5 independent dimensions, so additional conditions are needed to sharpen subsystem boundaries. The ortholog-transferred cross-species data is confounded by organism-specific respiratory architectures, and the non-core Complex I assignments rely on correlation rather than direct physical evidence. [^aromatic_catabolism_network]

The report proposes searching the ADP1 genome for NDH-2 and testing its deletion on quinate versus glucose; experimentally validating ACIAD3137 and ACIAD2176 by protein-protein interaction or co-purification studies; expanding the condition panel with benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors; comparing Complex I retention across aromatic-degrading species using pangenome data; and adding PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model. [^aromatic_catabolism_network]

## Slots Into

- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — the 51-gene co-fitness network, subsystem assignments, r > 0.98 DUF candidates, and within-category correlations provide a condition-specific functional architecture. [^aromatic_catabolism_network]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the quinate-specific phenotypes and cross-condition Complex I results refine the distinction between aromatic dependence and high-NADH-flux dependence. [^aromatic_catabolism_network]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — the 0% predicted Complex I essentiality, 1.76× flux increase, and 30/51 unmapped genes identify cofactor, respiratory, and regulatory blind spots for FBA. [^aromatic_catabolism_network]
- [gene-essentiality](../concepts/gene-essentiality.md) — the contrast between model-predicted 0% essentiality and observed defects for 10/13 Complex I subunits tests how complex-level constraints shape gene essentiality. [^aromatic_catabolism_network]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — the report integrates fitness phenotypes, FBA, genomic organization, co-fitness, and prior transcriptomic evidence to explain aromatic-catabolism dependencies. [^aromatic_catabolism_network]

[^aromatic_catabolism_network]: [aromatic catabolism network](../sources/aromatic_catabolism_network__REPORT.md)
