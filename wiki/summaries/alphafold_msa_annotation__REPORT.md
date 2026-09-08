---
type: Summary
description: AlphaFold MSA depth reveals pangenome-linked annotation gaps and conserved
  paradox proteins.
doc_type: short
full_text: ../sources/alphafold_msa_annotation__REPORT.md
title: AlphaFold MSA Depth as a Lens on the Bacterial Annotation Gap
sources:
- id: alphafold_msa_annotation
  resource: ../sources/alphafold_msa_annotation__REPORT.md
  title: alphafold msa annotation
---
# AlphaFold MSA Depth as a Lens on the Bacterial Annotation Gap

## Overview

This report evaluates AlphaFold multiple-sequence-alignment (MSA) depth as a proxy for functional annotation richness across bacterial pangenome gene clusters, using joins among `kbase_ke_pangenome`, `bakta_annotations`, `interproscan_domains`, and `kescience_alphafold`. Of 132,531,501 total gene clusters, 38,804,903 (29.3%) had a real UniProt accession and 38,051,842 (28.7%) bridged successfully to AlphaFold MSA depths; 70.7% lacked UniRef100 IDs or had UniParc-only identifiers without an AlphaFold entry. The analysed subset is biased toward better-studied organisms, so the annotation gap among the remaining 70.7% is likely larger. [^alphafold_msa_annotation]

## Key Findings

### Core and accessory structural representation

Core gene clusters had a median MSA depth of 15,308, compared with 5,299 for auxiliary+singleton clusters and 5,527 for auxiliary non-singleton clusters: 2.89× higher than auxiliary+singleton and 2.77× higher than auxiliary non-singleton. The 10th-percentile MSA depth was 334 for core genes versus 25–32 for accessory genes. [^alphafold_msa_annotation]

Among bridged clusters, the core class contained 25,571,299 clusters, with 415,733 (1.6%) having MSA depth < 10 and 979,912 (3.8%) hypothetical; auxiliary non-singleton contained 5,384,900 clusters, with 245,002 (4.6%) below MSA depth 10 and 622,748 (11.6%) hypothetical; auxiliary+singleton contained 7,095,643 clusters, with 392,959 (5.5%) below MSA depth 10 and 979,300 (13.8%) hypothetical. [^alphafold_msa_annotation]

Hypothetical-protein rates decreased from 13.8% in auxiliary+singleton clusters to 11.6% in auxiliary non-singleton clusters and 3.8% in core clusters. Chi-square tests were overwhelmingly significant (χ² > 500,000; p ≈ 0), with odds ratios of 0.25 for core versus auxiliary+singleton and 0.31 for core versus auxiliary non-singleton. [^alphafold_msa_annotation]

### MSA depth and domain annotation richness

Across 38,051,842 gene cluster–UniProt pairs, MSA depth and domain-hit count had Spearman ρ = 0.7563. Mean domain hits increased from 0.59 for MSA depth < 10 to 10.83 for MSA depth ≥ 10,000, while mean distinct InterPro (IPR) families increased from 0.059 to 4.601, an 18× span in mean domain hits. [^alphafold_msa_annotation]

The MSA-depth bins contained 415,733 core clusters below 10, 1,143,785 at 10–99, 2,301,137 at 100–999, 3,126,558 at 1,000–4,999, 2,591,011 at 5,000–9,999, and 15,993,075 at ≥ 10,000. The monotone relationship between MSA depth and domain hits held within core, auxiliary non-singleton, and auxiliary+singleton classes, with core genes showing slightly higher domain richness per MSA bin than accessory genes at equivalent depth. [^alphafold_msa_annotation]

Of all 132,531,501 gene clusters, 111,035,431 (83.8%) had at least one InterProScan domain annotation; mean hits were 7.5 and mean distinct IPR families were 3.3. This domain-annotation coverage exceeded the 29.3% AlphaFold bridge coverage. [^alphafold_msa_annotation]

### Conserved, structurally unprecedented core proteins

The report identified 415,603 distinct core clusters with MSA depth < 10, represented across 14,768 species clades. Their mean and median MSA depths were 4.57 and 4.0, respectively; 286,439 (68.9%) were hypothetical, 137 (0.033%) were EC-annotated, and 346 (0.083%) were KEGG-mapped. [^alphafold_msa_annotation]

The paradox-protein subset therefore had a 68.9% hypothetical rate versus 3.8% for all core genes, while EC and KEGG annotations were below 0.1%. The report interprets these proteins as conserved by pangenome classification yet structurally isolated from characterised sequence space, making them candidates for experimental structural characterisation; this interpretation is a prioritisation hypothesis rather than direct experimental validation. [^alphafold_msa_annotation]

Top-ranked paradox proteins with MSA depth = 1 came primarily from poorly characterised marine and soil bacteria, including *Oceanicoccus*, *Dwaynesavagella*, and CAILRJ01. Non-hypothetical entries at MSA depth = 1 included an RNA polymerase ω-subunit family protein and an FXSXX-COOH domain protein, both described as conserved structural components without solved structures for those specific lineages. [^alphafold_msa_annotation]

### Resolution of the apparent core/accessory tension

The report resolves the apparent contradiction between lower overall hypothetical rates in core genes and the 415,603 low-MSA-depth core clusters by distinguishing two annotation-gap layers: an MSA-depth-driven gap affecting all pangenome classes, and a pangenome-class gap in which accessory and singleton genes have higher hypothetical rates, likely associated with horizontal transfer, rapid evolution, and taxonomically narrow distribution. The cross-class comparison is dominated by the higher average MSA depth of core genes, whereas the paradox subset exposes a severe annotation gap within core genes. [^alphafold_msa_annotation]

## Caveats

- Only 29.3% of gene clusters bridged to AlphaFold MSA depths because the analysis required a non-UPI UniProt accession; the remaining 70.7% likely contains a larger annotation gap, but that inference is not directly measured. [^alphafold_msa_annotation]
- MSA depth was looked up for each gene cluster's representative sequence, so within-cluster sequence diversity was ignored and the representative may have higher or lower MSA depth than typical cluster members. [^alphafold_msa_annotation]
- The 293K genomes were not phylogenetically balanced; common taxa such as *Pseudomonas* and *E. coli* were over-represented, influencing core-gene counts and MSA-depth distributions. [^alphafold_msa_annotation]
- Spearman ρ = 0.7563 was computed on the full 38,051,842-pair dataset without subgroup stratification, so its value may differ among core, auxiliary, and singleton clusters and among organisms with different annotation gaps. [^alphafold_msa_annotation]
- The analysis used a static version-6 BERDL AlphaFold snapshot, and later UniProt deposits may change MSA depths. [^alphafold_msa_annotation]

## Slots Into

- [pangenome-integration](../concepts/pangenome-integration.md) — the 2.9× core/accessory MSA-depth gradient, class-specific hypothetical rates, and conserved low-MSA-depth core subset connect pangenome structure to annotation coverage. [^alphafold_msa_annotation]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — the proposed integration of paradox-protein clusters with Fitness Browser measurements provides a route to connect structural novelty with experimentally observed fitness phenotypes. [^alphafold_msa_annotation]
- [gene-essentiality](../concepts/gene-essentiality.md) — the report proposes joining the 415,603 paradox clusters to fitness scores to identify conserved, structurally novel proteins with condition-specific or growth-essential phenotypes. [^alphafold_msa_annotation]

[^alphafold_msa_annotation]: [alphafold msa annotation](../sources/alphafold_msa_annotation__REPORT.md)
