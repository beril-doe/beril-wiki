---
type: "Concept"
description: "Core genes can be conserved yet poorly characterized in sequence and function."
sources: ["summaries/alphafold_msa_annotation__REPORT.md"]
---
# Conserved Core Genes Can Remain Structurally and Functionally Uncharacterized

Core classification indicates broad pangenome conservation, but it does not guarantee that a gene has substantial representation in characterized sequence space or a well-defined molecular function. The [[summaries/alphafold_msa_annotation__REPORT]] examines this distinction by relating pangenome gene-cluster classes to AlphaFold multiple-sequence-alignment (MSA) depth, where MSA depth is the number of homologous sequences represented in the alignment. [src: alphafold_msa_annotation]

## Core Genes Usually Have Greater Sequence Representation

Among gene clusters bridged to AlphaFold, core clusters had a median MSA depth of 15,308, compared with 5,299 for auxiliary+singleton clusters and 5,527 for auxiliary non-singleton clusters. [src: alphafold_msa_annotation] This corresponds to a 2.89× higher median for core genes than auxiliary+singleton genes and a 2.77× higher median than auxiliary non-singleton genes. [src: alphafold_msa_annotation] The 10th-percentile MSA depth was 334 for core genes versus 25–32 for accessory classes. [src: alphafold_msa_annotation]

These distributions are consistent with a broad class-level annotation advantage for core genes, but they do not eliminate poorly represented core proteins. Among bridged clusters, 415,733 core clusters (1.6%) had MSA depth below 10, compared with 245,002 auxiliary non-singleton clusters (4.6%) and 392,959 auxiliary+singleton clusters (5.5%). [src: alphafold_msa_annotation]

## A Conserved Low-MSA Core Subset

The analysis identified 415,603 distinct core clusters with MSA depth below 10 across 14,768 species clades. [src: alphafold_msa_annotation] Their mean MSA depth was 4.57 and their median MSA depth was 4.0. [src: alphafold_msa_annotation] Of these clusters, 286,439 (68.9%) were annotated as hypothetical, 137 (0.033%) had an EC annotation, and 346 (0.083%) were mapped to KEGG. [src: alphafold_msa_annotation]

The low-MSA core subset therefore had a 68.9% hypothetical-protein rate, whereas all bridged core genes had a 3.8% hypothetical-protein rate. [src: alphafold_msa_annotation] This contrast supports the interpretation that pangenome conservation and functional characterization measure different properties: a gene can be retained broadly while remaining distant from experimentally or computationally characterized sequence space. [src: alphafold_msa_annotation]

The report treats these proteins as candidates for experimental structural characterization, rather than as experimentally validated examples of novel function. [src: alphafold_msa_annotation] The prioritization hypothesis is strongest for proteins that are conserved by pangenome classification but have very shallow alignments and little EC, KEGG, or domain-level annotation. [src: alphafold_msa_annotation]

## Functional Annotation Tracks MSA Depth

Across 38,051,842 gene cluster–UniProt pairs, MSA depth and domain-hit count had a Spearman correlation of ρ = 0.7563. [src: alphafold_msa_annotation] Mean domain hits increased from 0.59 for clusters with MSA depth below 10 to 10.83 for clusters with MSA depth of at least 10,000. [src: alphafold_msa_annotation] Mean distinct InterPro families increased from 0.059 to 4.601 across the same MSA-depth range. [src: alphafold_msa_annotation] The monotone relationship held within core, auxiliary non-singleton, and auxiliary+singleton classes, with core genes showing slightly higher domain richness per MSA bin than accessory genes at equivalent depth. [src: alphafold_msa_annotation]

This relationship supports MSA depth as a useful prioritization signal for annotation scarcity, but it does not establish that sequence abundance causes functional knowledge or that shallow MSA depth proves biological novelty. [src: alphafold_msa_annotation] Of all 132,531,501 gene clusters, 111,035,431 (83.8%) had at least one InterProScan domain annotation, whereas only 38,804,903 (29.3%) had a real UniProt accession and 38,051,842 (28.7%) bridged successfully to AlphaFold MSA depths. [src: alphafold_msa_annotation]

## Two Annotation-Gap Layers

The evidence distinguishes two related annotation-gap layers. [src: alphafold_msa_annotation] First, an MSA-depth-driven gap affects genes in every pangenome class, because domain richness decreases sharply in shallow-MSA bins. [src: alphafold_msa_annotation] Second, a pangenome-class gap is visible in the higher hypothetical-protein rates of accessory classes: 13.8% for auxiliary+singleton clusters, 11.6% for auxiliary non-singleton clusters, and 3.8% for core clusters. [src: alphafold_msa_annotation]

The class-level comparison is dominated by the higher average MSA depth of core genes, while the low-MSA core subset reveals a severe annotation gap within the core itself. [src: alphafold_msa_annotation] This distinction refines [[concepts/pangenome-integration]] by showing that core status should not be treated as a proxy for complete annotation. [src: alphafold_msa_annotation]

## Scope and Interpretation

Only 38,051,842 of 132,531,501 total gene clusters (28.7%) bridged successfully to AlphaFold MSA depths, while 70.7% lacked UniRef100 IDs or had UniParc-only identifiers without an AlphaFold entry. [src: alphafold_msa_annotation] Because the analysed subset is biased toward better-studied organisms, the annotation gap among the remaining 70.7% is likely larger, although that inference was not directly measured. [src: alphafold_msa_annotation]

MSA depth was obtained for each cluster's representative sequence, so the analysis did not measure sequence-level variation within each cluster. [src: alphafold_msa_annotation] The 293K genomes were not phylogenetically balanced, and common taxa such as *Pseudomonas* and *E. coli* were over-represented. [src: alphafold_msa_annotation] The reported Spearman ρ = 0.7563 was calculated on the full 38,051,842-pair dataset without subgroup stratification. [src: alphafold_msa_annotation] These limitations mean that the low-MSA core set is a defensible discovery and prioritization set, not a complete census of conserved functionally dark genes. [src: alphafold_msa_annotation]

## Open Directions

- Join the 415,603 low-MSA core clusters to [[entities/kescience-fitnessbrowser]] measurements and use condition-specific fitness analysis to ask whether structurally isolated core proteins have essential or condition-dependent phenotypes. [src: alphafold_msa_annotation]
- Recompute MSA depth and InterPro-family richness after stratifying the 38,051,842 bridged pairs by pangenome class and organismal lineage, using Spearman correlations and balanced taxon sampling to ask whether the ρ = 0.7563 relationship is consistent across taxa. [src: alphafold_msa_annotation]
- Compare representative-sequence MSA depths with member-level sequence diversity for the 415,603 low-MSA core clusters, using within-cluster pangenome sequence analysis to ask whether representatives conceal deeper or shallower support among cluster members. [src: alphafold_msa_annotation]
- Prioritize the 286,439 hypothetical low-MSA core clusters for structure prediction and experimental characterization, using the 137 EC-annotated and 346 KEGG-mapped clusters as annotated comparators to ask which structural features predict recoverable function. [src: alphafold_msa_annotation]
- Extend the bridge analysis to the 70.7% of clusters without AlphaFold MSA depth, using alternative sequence-similarity and domain resources to ask whether the unbridged population contains a larger conserved annotation gap. [src: alphafold_msa_annotation]
